---
title: Evaluation
layout: default
nav_order: 3
---

# Evaluation
{: .no_toc }

<details open markdown="block">
<summary>Contents</summary>
{: .text-delta }
1. TOC
{:toc}
</details>

## Overview

`src/evaluation.py` measures how much better the fused response is compared to
any individual model, using an independent LLM judge with bias controls.

## Bias controls

| Risk | Mitigation |
|------|-----------|
| Self-preference | Judge is automatically chosen from outside the pool |
| Positional bias | Candidates are shuffled before the judge sees them |
| Label leak | Responses are anonymized to A/B/C… — "Fused" is never shown |

## Usage

```bash
python -m src.evaluation "Your query here" [pool_name]
```

Results are printed as a Rich table and saved to
`tests/benchmarks/results/eval_<timestamp>.json`.

## Judge selection

The judge defaults to the highest-ranked model in `JUDGE_PREFERENCE` that is
**not** a member or synthesizer of the pool under test. To override:

```python
result = await evaluator.evaluate(prompt, pool="general", judge_model="google/gemma-2-27b-it:free")
```

A warning is printed if the requested judge is inside the pool.

## Output schema

```json
{
  "prompt": "...",
  "timestamp": "2026-06-18T...",
  "pool_name": "general",
  "judge_model": "meta-llama/llama-3.3-70b-instruct:free",
  "individual_scores": [
    {"model": "llama-3.3-70b", "factual_accuracy": 8.0, "reasoning_depth": 7.0,
     "completeness": 8.0, "clarity": 9.0, "overall": 8.0}
  ],
  "fused_scores": {"model": "Fused", "factual_accuracy": 9.0, ...},
  "improvement_pct": 12.5,
  "preferred_by_judge": "Fused",
  "judge_reasoning": "...",
  "latency_ms": 4200.0,
  "valid": true
}
```

`valid: false` means the judge output could not be fully parsed (scores or
fused entry missing). These runs are kept in the results directory but flagged
so they can be excluded from aggregate statistics.
