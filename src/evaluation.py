"""
Evaluation Tools

Compare fusion results against individual model responses to measure the quality
improvement from synthesis.

Bias controls:
- The judge defaults to a model that is NOT in the pool (avoids self-enhancement
  bias from a model grading its own / its synthesizer's output).
- Candidate responses are anonymized to "Response A/B/C..." and shuffled before
  the judge sees them, so the "Fused" answer gets no positional or label
  advantage. The mapping is restored after parsing.
"""

import asyncio
import json
import random
import re
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from .fusion import FusionOrchestrator, FusionResult
from .models import get_pool

console = Console()

# Preference order (strongest free reasoners first). evaluate() picks the first
# entry that is NOT a member or synthesizer of the pool under test.
JUDGE_PREFERENCE = [
    "deepseek/deepseek-r1:free",
    "qwen/qwen3-coder-480b-instruct:free",
    "meta-llama/llama-3.3-70b-instruct:free",
    "google/gemma-2-27b-it:free",
    "mistralai/mistral-7b-instruct:free",
]


@dataclass
class EvaluationScores:
    model: str
    factual_accuracy: float  # 1-10
    reasoning_depth: float   # 1-10
    completeness: float      # 1-10
    clarity: float           # 1-10

    @property
    def overall(self) -> float:
        return (
            self.factual_accuracy * 0.3
            + self.reasoning_depth * 0.3
            + self.completeness * 0.2
            + self.clarity * 0.2
        )


@dataclass
class EvaluationResult:
    prompt: str
    timestamp: str
    pool_name: str
    judge_model: str
    individual_scores: list[EvaluationScores]
    fused_scores: EvaluationScores
    improvement_pct: float
    preferred_by_judge: str  # "Fused" or a model name
    judge_reasoning: str
    latency_ms: float
    valid: bool = True


class FusionEvaluator:
    """
    Evaluates fusion quality by having an independent LLM judge compare
    individual responses against the fused output (blind + shuffled).
    """

    def __init__(self, orchestrator: FusionOrchestrator):
        self.orchestrator = orchestrator
        self.results_dir = (
            Path(__file__).resolve().parent.parent / "tests" / "benchmarks" / "results"
        )
        self.results_dir.mkdir(parents=True, exist_ok=True)

    def _select_judge(self, pool_name: str, requested: Optional[str]) -> str:
        """Pick a judge that is independent of the pool under test."""
        pool = get_pool(pool_name)
        in_pool = set(pool.models) | {pool.synthesizer}

        if requested:
            if requested in in_pool:
                console.print(
                    f"[yellow]Warning: requested judge {requested} is part of pool "
                    f"'{pool_name}'. Self-evaluation bias is likely.[/yellow]"
                )
            return requested

        for candidate in JUDGE_PREFERENCE:
            if candidate not in in_pool:
                return candidate

        # Every preferred judge is in the pool; fall back with a warning.
        fallback = JUDGE_PREFERENCE[0]
        console.print(
            f"[yellow]Warning: no independent judge available for pool "
            f"'{pool_name}'; using {fallback}.[/yellow]"
        )
        return fallback

    async def evaluate(
        self,
        prompt: str,
        pool: str = "general",
        judge_model: Optional[str] = None,
    ) -> EvaluationResult:
        """Run a fusion query and evaluate the results with an independent judge."""
        judge = self._select_judge(pool, judge_model)

        console.print("\n[bold]Running fusion query...[/bold]")
        fusion_result = await self.orchestrator.fuse(prompt, pool=pool)

        console.print(f"\n[bold]Evaluating responses[/bold] (judge: [cyan]{judge}[/cyan])...")
        return await self._judge_responses(prompt, fusion_result, judge)

    async def _judge_responses(
        self,
        prompt: str,
        fusion_result: FusionResult,
        judge_model: str,
    ) -> EvaluationResult:
        """Have the judge evaluate all responses, blind and shuffled."""
        eval_prompt, mapping = self._build_evaluation_prompt(prompt, fusion_result)

        response = await self.orchestrator._chat_completion_with_retry(
            judge_model, [{"role": "user", "content": eval_prompt}]
        )
        judge_response = response.choices[0].message.content or ""

        return self._parse_judge_response(
            judge_response, fusion_result, mapping, judge_model
        )

    def _build_evaluation_prompt(
        self,
        prompt: str,
        fusion_result: FusionResult,
    ) -> tuple[str, dict[str, str]]:
        """
        Build the judge prompt with anonymized, shuffled candidates.

        Returns (prompt, mapping) where mapping is {label: identity}, and
        identity is a model name or "Fused".
        """
        candidates: list[tuple[str, str]] = []
        for resp in fusion_result.individual_responses:
            if not resp.error and resp.content:
                model_name = resp.model.split("/")[-1].replace(":free", "")
                candidates.append((model_name, resp.content))
        candidates.append(("Fused", fusion_result.fused_response))

        random.shuffle(candidates)
        labels = [chr(ord("A") + i) for i in range(len(candidates))]
        mapping = {label: identity for label, (identity, _) in zip(labels, candidates)}

        sections = ""
        for label, (_, content) in zip(labels, candidates):
            snippet = content[:2000] + ("..." if len(content) > 2000 else "")
            sections += f"\n### Response {label}:\n{snippet}\n"

        label_list = ", ".join(labels)
        scores_template = ",\n    ".join(
            f'{{"label": "{lbl}", "factual": 8, "reasoning": 7, '
            f'"completeness": 8, "clarity": 9}}'
            for lbl in labels
        )

        return (
            f"""You are an expert, impartial evaluator comparing AI responses to the same query.

## Original Query
{prompt}

## Responses to Evaluate (anonymized)
{sections}

## Evaluation Task
For EACH response ({label_list}), give integer scores from 1-10 on:
1. Factual Accuracy
2. Reasoning Depth
3. Completeness
4. Clarity

Then choose the single best response by its label.

Respond with ONLY this JSON (no prose, no markdown fence):
{{
  "scores": [
    {scores_template}
  ],
  "best_overall": "{labels[0]}",
  "reasoning": "Brief explanation of your choice."
}}""",
            mapping,
        )

    def _parse_judge_response(
        self,
        judge_response: str,
        fusion_result: FusionResult,
        mapping: dict[str, str],
        judge_model: str,
    ) -> EvaluationResult:
        """Parse the judge's labeled response and restore identities."""
        try:
            json_match = re.search(r"```json\s*(.*?)\s*```", judge_response, re.DOTALL)
            if json_match:
                data = json.loads(json_match.group(1))
            else:
                json_match = re.search(r"\{.*\}", judge_response, re.DOTALL)
                data = json.loads(json_match.group(0) if json_match else judge_response)

            individual_scores: list[EvaluationScores] = []
            fused_scores: Optional[EvaluationScores] = None

            for score_data in data.get("scores", []):
                label = str(score_data.get("label", "")).strip()
                identity = mapping.get(label, label)  # tolerate raw identity too
                scores = EvaluationScores(
                    model=identity,
                    factual_accuracy=float(score_data.get("factual", 5)),
                    reasoning_depth=float(score_data.get("reasoning", 5)),
                    completeness=float(score_data.get("completeness", 5)),
                    clarity=float(score_data.get("clarity", 5)),
                )
                if identity.lower() == "fused":
                    fused_scores = scores
                else:
                    individual_scores.append(scores)

            best_label = str(data.get("best_overall", "")).strip()
            preferred = mapping.get(best_label, best_label)

            best_individual = (
                max(s.overall for s in individual_scores) if individual_scores else 0
            )
            fused_overall = fused_scores.overall if fused_scores else 0
            improvement = (
                ((fused_overall - best_individual) / best_individual) * 100
                if best_individual
                else 0.0
            )

            return EvaluationResult(
                prompt=fusion_result.prompt,
                timestamp=datetime.now().isoformat(),
                pool_name=fusion_result.pool_name,
                judge_model=judge_model,
                individual_scores=individual_scores,
                fused_scores=fused_scores or EvaluationScores("Fused", 5, 5, 5, 5),
                improvement_pct=improvement,
                preferred_by_judge=preferred or "unknown",
                judge_reasoning=data.get("reasoning", ""),
                latency_ms=fusion_result.total_latency_ms,
                valid=fused_scores is not None and bool(individual_scores),
            )

        except (json.JSONDecodeError, AttributeError, KeyError, TypeError) as e:
            console.print(f"[yellow]Warning: could not parse judge response: {e}[/yellow]")
            return EvaluationResult(
                prompt=fusion_result.prompt,
                timestamp=datetime.now().isoformat(),
                pool_name=fusion_result.pool_name,
                judge_model=judge_model,
                individual_scores=[],
                fused_scores=EvaluationScores("Fused", 5, 5, 5, 5),
                improvement_pct=0,
                preferred_by_judge="parse_error",
                judge_reasoning=judge_response[:500],
                latency_ms=fusion_result.total_latency_ms,
                valid=False,
            )

    def display_results(self, result: EvaluationResult):
        """Display evaluation results in a table."""
        table = Table(title="Evaluation Scores")
        table.add_column("Model", style="cyan")
        table.add_column("Factual", justify="center")
        table.add_column("Reasoning", justify="center")
        table.add_column("Completeness", justify="center")
        table.add_column("Clarity", justify="center")
        table.add_column("Overall", justify="center", style="bold")

        for scores in result.individual_scores:
            table.add_row(
                scores.model,
                f"{scores.factual_accuracy:.1f}",
                f"{scores.reasoning_depth:.1f}",
                f"{scores.completeness:.1f}",
                f"{scores.clarity:.1f}",
                f"{scores.overall:.1f}",
            )

        table.add_row(
            "[bold green]Fused[/bold green]",
            f"[green]{result.fused_scores.factual_accuracy:.1f}[/green]",
            f"[green]{result.fused_scores.reasoning_depth:.1f}[/green]",
            f"[green]{result.fused_scores.completeness:.1f}[/green]",
            f"[green]{result.fused_scores.clarity:.1f}[/green]",
            f"[bold green]{result.fused_scores.overall:.1f}[/bold green]",
        )

        console.print(table)

        if not result.valid:
            console.print("[yellow]Run marked INVALID (judge output incomplete).[/yellow]")

        improvement_color = "green" if result.improvement_pct > 0 else "red"
        console.print(
            f"\n[bold]Improvement over best individual:[/bold] "
            f"[{improvement_color}]{result.improvement_pct:+.1f}%[/{improvement_color}]"
        )
        console.print(f"[bold]Judge ({result.judge_model}) preferred:[/bold] {result.preferred_by_judge}")
        console.print(Panel(result.judge_reasoning, title="Judge Reasoning"))

    def save_result(self, result: EvaluationResult, filename: Optional[str] = None):
        """Save evaluation result to JSON file."""
        if filename is None:
            filename = f"eval_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = self.results_dir / filename
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "prompt": result.prompt,
                    "timestamp": result.timestamp,
                    "pool_name": result.pool_name,
                    "judge_model": result.judge_model,
                    "individual_scores": [asdict(s) for s in result.individual_scores],
                    "fused_scores": asdict(result.fused_scores),
                    "improvement_pct": result.improvement_pct,
                    "preferred_by_judge": result.preferred_by_judge,
                    "judge_reasoning": result.judge_reasoning,
                    "latency_ms": result.latency_ms,
                    "valid": result.valid,
                },
                f,
                indent=2,
            )
        console.print(f"\n[dim]Results saved to {filepath}[/dim]")


async def main():
    """CLI entry point for evaluation."""
    import sys
    import os

    if len(sys.argv) < 2:
        console.print("[red]Usage:[/red] python -m src.evaluation \"Your query\" [pool_name]")
        sys.exit(1)

    prompt = sys.argv[1]
    pool = sys.argv[2] if len(sys.argv) > 2 else "general"

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        console.print("[red]Error:[/red] Set OPENROUTER_API_KEY environment variable")
        sys.exit(1)

    orchestrator = FusionOrchestrator(api_key=api_key)
    evaluator = FusionEvaluator(orchestrator)

    result = await evaluator.evaluate(prompt, pool=pool)
    evaluator.display_results(result)
    evaluator.save_result(result)


if __name__ == "__main__":
    asyncio.run(main())
