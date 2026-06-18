---
title: Why Fusion Works
layout: default
nav_order: 4
---

# Why Fusion Works
{: .no_toc }

<details open markdown="block">
<summary>Contents</summary>
{: .text-delta }
1. TOC
{:toc}
</details>

## The core idea

No single model is uniformly best across all sub-tasks within a complex
question. One model may reason precisely but omit context; another may cover
breadth at the cost of depth. A synthesis step that sees all responses can
combine the strongest parts of each.

## Error independence

When models are chosen to be architecturally and training-data diverse
(different families, scales, and fine-tunes), their errors are more likely to
be *independent*. A synthesis model that sees multiple independent high-quality
signals can more reliably distinguish correct reasoning from noise.

## Why the bias controls matter

Without them, evaluation results are systematically misleading:

- **Self-preference**: if the judge is deepseek-r1 and the synthesizer is also
  deepseek-r1, the judge is grading its own style. Studies show LLMs rate their
  own outputs 10–20 pp higher than independent judges do.
- **Positional bias**: LLMs disproportionately prefer the first or last response
  in a list. Shuffling + anonymizing removes this confound.
- **Label leak**: showing "Fused" as a label signals special status to the judge.
  Anonymous A/B/C labels prevent this.

## Failure modes

| Failure | Detection | Mitigation |
|---------|-----------|-----------|
| All models rate-limited | `synthesis_failed=True` | Exponential backoff (up to 4 retries) |
| Synthesizer crashes | `synthesis_failed=True` | Falls back to longest individual response |
| Judge output unparseable | `valid=False` in result | Run is flagged, not discarded |
| Pool and judge overlap | Warning printed | Independent judge auto-selected |

## References

- Wan et al., "Knowledge Fusion of Large Language Models" (2024)
- Wang et al., "Self-Consistency Improves Chain of Thought Reasoning" (2022)
- Zheng et al., "Judging LLM-as-a-Judge with MT-Bench" (2023) — positional bias evidence
