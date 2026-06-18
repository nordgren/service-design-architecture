"""
Core Fusion Orchestrator

Queries multiple models in parallel and synthesizes their outputs into a
unified response. Adds retry/backoff, rate-limit throttling, and synthesizer
failover so a single rate-limited model no longer silently degrades or crashes
the whole fusion.
"""

import asyncio
import os
import random
import time
from dataclasses import dataclass, field
from typing import Optional

from asyncio_throttle import Throttler
from openai import AsyncOpenAI
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from .models import get_pool
from .synthesis import create_synthesis_prompt

console = Console()

# Transient errors worth retrying. Imported defensively so the module still
# loads if the installed openai version renames a symbol.
try:
    from openai import (
        APIConnectionError,
        APITimeoutError,
        InternalServerError,
        RateLimitError,
    )
    RETRYABLE_ERRORS: tuple = (
        RateLimitError,
        APITimeoutError,
        APIConnectionError,
        InternalServerError,
    )
except Exception:  # pragma: no cover - defensive
    RETRYABLE_ERRORS = ()


@dataclass
class ModelResponse:
    model: str
    content: str
    latency_ms: float = 0
    tokens_in: int = 0
    tokens_out: int = 0
    error: Optional[str] = None


@dataclass
class FusionResult:
    prompt: str
    pool_name: str
    individual_responses: list[ModelResponse] = field(default_factory=list)
    fused_response: str = ""
    synthesis_latency_ms: float = 0
    total_latency_ms: float = 0
    synthesis_failed: bool = False


class FusionOrchestrator:
    """
    Orchestrates multi-model fusion queries.

    Usage:
        orchestrator = FusionOrchestrator()
        result = await orchestrator.fuse("Your complex query", pool="reasoning")
        print(result.fused_response)
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: str = "https://openrouter.ai/api/v1",
        max_tokens: int = 4096,
        requests_per_minute: int = 20,
        max_concurrency: int = 8,
        max_retries: int = 4,
        retry_base_delay: float = 2.0,
    ):
        """
        Args:
            api_key: OpenRouter API key (or set OPENROUTER_API_KEY env var).
            base_url: API base URL (default: OpenRouter).
            max_tokens: Default completion cap (overridable per call).
            requests_per_minute: Throttle to stay under the free-tier limit.
            max_concurrency: Max simultaneous in-flight requests.
            max_retries: Retry attempts on transient errors (429/5xx/timeouts).
            retry_base_delay: Base seconds for exponential backoff.
        """
        self.client = AsyncOpenAI(api_key=api_key, base_url=base_url)
        self.extra_headers = {
            "HTTP-Referer": "https://github.com/nordgren/fusion-ai-harness",
            "X-Title": "Fusion AI Harness",
        }
        self.max_tokens = max_tokens
        self.max_retries = max_retries
        self.retry_base_delay = retry_base_delay
        self.throttler = Throttler(rate_limit=requests_per_minute, period=60)
        self.semaphore = asyncio.Semaphore(max_concurrency)

    async def _chat_completion_with_retry(
        self,
        model: str,
        messages: list[dict],
        max_tokens: Optional[int] = None,
    ):
        """Call the chat endpoint with throttling, concurrency cap, and backoff."""
        max_tokens = max_tokens or self.max_tokens
        last_exc: Optional[Exception] = None

        for attempt in range(self.max_retries + 1):
            try:
                async with self.semaphore, self.throttler:
                    return await self.client.chat.completions.create(
                        model=model,
                        messages=messages,
                        max_tokens=max_tokens,
                        extra_headers=self.extra_headers,
                    )
            except RETRYABLE_ERRORS as e:
                last_exc = e
                if attempt >= self.max_retries:
                    break
                delay = self.retry_base_delay * (2 ** attempt) + random.uniform(0, 1)
                await asyncio.sleep(delay)
            # Non-retryable errors propagate immediately.

        assert last_exc is not None
        raise last_exc

    async def _query_model(
        self,
        model: str,
        prompt: str,
        max_tokens: Optional[int] = None,
    ) -> ModelResponse:
        """Query a single model and return its response (errors captured, not raised)."""
        start_time = time.perf_counter()
        try:
            response = await self._chat_completion_with_retry(
                model, [{"role": "user", "content": prompt}], max_tokens
            )
            latency_ms = (time.perf_counter() - start_time) * 1000
            return ModelResponse(
                model=model,
                content=response.choices[0].message.content or "",
                latency_ms=latency_ms,
                tokens_in=response.usage.prompt_tokens if response.usage else 0,
                tokens_out=response.usage.completion_tokens if response.usage else 0,
            )
        except Exception as e:
            latency_ms = (time.perf_counter() - start_time) * 1000
            return ModelResponse(
                model=model, content="", latency_ms=latency_ms, error=str(e)
            )

    async def _query_models_parallel(
        self, models: list[str], prompt: str
    ) -> list[ModelResponse]:
        """Query multiple models in parallel (order preserved)."""
        tasks = [self._query_model(model, prompt) for model in models]
        return await asyncio.gather(*tasks)

    async def _synthesize(
        self,
        prompt: str,
        responses: list[ModelResponse],
        synthesizer: str,
    ) -> tuple[str, float, bool]:
        """
        Synthesize multiple responses into one.

        Returns (content, latency_ms, failed). On synthesizer failure, falls back
        to the longest valid individual response so a successful set of model
        calls is never thrown away.
        """
        valid_responses = [r for r in responses if not r.error and r.content]

        if not valid_responses:
            return "Error: No valid responses to synthesize.", 0.0, True

        if len(valid_responses) == 1:
            return valid_responses[0].content, 0.0, False

        synthesis_prompt = create_synthesis_prompt(prompt, valid_responses)
        start_time = time.perf_counter()
        try:
            response = await self._chat_completion_with_retry(
                synthesizer, [{"role": "user", "content": synthesis_prompt}]
            )
            latency_ms = (time.perf_counter() - start_time) * 1000
            return response.choices[0].message.content or "", latency_ms, False
        except Exception as e:
            latency_ms = (time.perf_counter() - start_time) * 1000
            fallback = max(valid_responses, key=lambda r: len(r.content))
            console.print(
                f"[yellow]Synthesizer failed ({e}). "
                f"Falling back to best individual response "
                f"({fallback.model}).[/yellow]"
            )
            return fallback.content, latency_ms, True

    async def fuse(
        self,
        prompt: str,
        pool: str = "general",
        show_progress: bool = True,
    ) -> FusionResult:
        """Execute a fusion query against the named pool."""
        start_time = time.perf_counter()
        model_pool = get_pool(pool)
        result = FusionResult(prompt=prompt, pool_name=pool)

        if show_progress:
            console.print(f"\n[bold blue]Fusion Query[/bold blue] using pool: [green]{pool}[/green]")
            console.print(f"Models: {', '.join(model_pool.models)}")
            console.print(f"Synthesizer: {model_pool.synthesizer}\n")

        # Stage 1: Parallel model queries
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            disable=not show_progress,
        ) as progress:
            progress.add_task("Stage 1: Querying models in parallel...", total=None)
            result.individual_responses = await self._query_models_parallel(
                model_pool.models, prompt
            )

        if show_progress:
            for resp in result.individual_responses:
                status = "[red]FAILED[/red]" if resp.error else f"[green]{resp.latency_ms:.0f}ms[/green]"
                console.print(f"  • {resp.model}: {status}")

        # Stage 2 & 3: Synthesis
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            disable=not show_progress,
        ) as progress:
            progress.add_task("Stage 2-3: Analyzing and synthesizing...", total=None)
            (
                result.fused_response,
                result.synthesis_latency_ms,
                result.synthesis_failed,
            ) = await self._synthesize(
                prompt, result.individual_responses, model_pool.synthesizer
            )

        result.total_latency_ms = (time.perf_counter() - start_time) * 1000

        if show_progress:
            console.print(f"\n[bold]Synthesis complete[/bold] in {result.synthesis_latency_ms:.0f}ms")
            console.print(f"[dim]Total time: {result.total_latency_ms:.0f}ms[/dim]\n")

        return result


async def main():
    """CLI entry point."""
    import sys

    if len(sys.argv) < 2:
        console.print("[red]Usage:[/red] python -m src.fusion \"Your query here\" [pool_name]")
        console.print("\nAvailable pools: reasoning, general, technical, speed, minimal")
        sys.exit(1)

    prompt = sys.argv[1]
    pool = sys.argv[2] if len(sys.argv) > 2 else "general"

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        console.print("[red]Error:[/red] Set OPENROUTER_API_KEY environment variable")
        console.print("Get a free key at: https://openrouter.ai/keys")
        sys.exit(1)

    orchestrator = FusionOrchestrator(api_key=api_key)
    result = await orchestrator.fuse(prompt, pool=pool)

    console.print(Panel(
        result.fused_response,
        title="[bold green]Fused Response[/bold green]",
        border_style="green",
    ))


if __name__ == "__main__":
    asyncio.run(main())
