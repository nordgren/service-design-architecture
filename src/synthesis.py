"""
Synthesis Prompt Builder

Constructs the meta-prompt that asks a synthesizer model to combine multiple
individual model responses into a single, superior answer.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .fusion import ModelResponse


def create_synthesis_prompt(prompt: str, responses: list["ModelResponse"]) -> str:
    """
    Build a prompt that instructs the synthesizer to merge valid individual
    responses into one coherent, high-quality answer.
    """
    responses_text = ""
    for i, resp in enumerate(responses, 1):
        model_name = resp.model.split("/")[-1].replace(":free", "")
        snippet = resp.content[:3000] + ("..." if len(resp.content) > 3000 else "")
        responses_text += f"\n### Response {i} ({model_name}):\n{snippet}\n"

    return f"""You are a master synthesizer. Your task is to combine the following AI responses \
into a single, superior answer that captures the best reasoning, facts, and clarity from each.

## Original Query
{prompt}

## Individual Responses
{responses_text}

## Synthesis Instructions
- Integrate the strongest insights from every response.
- Resolve any contradictions by favouring the most well-reasoned position.
- Eliminate redundancy while preserving depth.
- Write in clear, direct prose. Do not mention or quote the individual responses.
- Begin your answer immediately—no preamble.

## Synthesized Response"""
