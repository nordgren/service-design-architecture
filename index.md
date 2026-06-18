---
title: Home
layout: home
nav_order: 1
---

# Fusion AI Harness

Query multiple LLMs in parallel and synthesize their outputs into a single,
higher-quality response — then evaluate how much better the fused answer is
compared to any individual model.

## Quick start

```bash
pip install -r requirements.txt
export OPENROUTER_API_KEY=sk-or-...

# Run a fusion query
python -m src.fusion "Explain backpressure in distributed systems" general

# Run fusion + blind evaluation
python -m src.evaluation "Explain backpressure in distributed systems" general
```

## How it works

1. **Parallel queries** — all models in the chosen pool are queried simultaneously.
2. **Synthesis** — the synthesizer model merges the best reasoning from each response.
3. **Evaluation** — an independent judge (not in the pool) scores all responses
   blind and shuffled to avoid positional and self-preference bias.

## Available pools

| Pool | Models | Best for |
|------|--------|----------|
| `general` | llama-3.3-70b, gemma-2-27b, deepseek-r1 | Most tasks |
| `reasoning` | deepseek-r1, qwen3-coder-480b, llama-3.3-70b | Complex analysis |
| `technical` | qwen3-coder-480b, deepseek-r1, llama-3.3-70b | Code & architecture |
| `speed` | gemma-2-9b, llama-3.1-8b, mistral-7b | Low-latency drafts |
| `minimal` | deepseek-r1, llama-3.3-70b | Quick testing |

Pool definitions live in [`configs/model-pools.yaml`](https://github.com/nordgren/service-design-architecture/blob/main/configs/model-pools.yaml)
— edit that file to add or change pools without touching any Python.
