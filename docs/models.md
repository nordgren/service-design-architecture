---
title: Model Pools
layout: default
nav_order: 2
---

# Model Pools
{: .no_toc }

<details open markdown="block">
<summary>Contents</summary>
{: .text-delta }
1. TOC
{:toc}
</details>

## Configuration

All pools are defined in `configs/model-pools.yaml`. The Python code reads
this file at startup via `src/models.py` — editing the YAML takes effect
immediately without changing any code.

```yaml
pools:
  my-pool:
    description: "Custom pool for my use case"
    models:
      - deepseek/deepseek-r1:free
      - meta-llama/llama-3.3-70b-instruct:free
    synthesizer: deepseek/deepseek-r1:free
    use_cases:
      - custom tasks
```

## Environment override

Set `FUSION_POOLS_CONFIG` to point at a different YAML file:

```bash
FUSION_POOLS_CONFIG=/path/to/my-pools.yaml python -m src.fusion "..."
```

## Runtime reload

After editing the YAML while a long-running process is active:

```python
from src.models import reload_pools
reload_pools()  # clears the lru_cache — next call re-reads the file
```

## Python API

```python
from src.models import get_pool, list_pools

pool = get_pool("reasoning")
print(pool.models)       # ['deepseek/deepseek-r1:free', ...]
print(pool.synthesizer)  # 'deepseek/deepseek-r1:free'

all_pools = list_pools()  # {'reasoning': 'Deep analysis...', ...}
```
