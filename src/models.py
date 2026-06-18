"""
Model Pool Configuration

Loads model-pool combinations from configs/model-pools.yaml so the YAML is the
single source of truth. Previously the pools were ALSO hard-coded here and the
YAML was never read, so editing the YAML had no effect.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path

import yaml


@dataclass
class ModelPool:
    name: str
    description: str
    models: list[str]
    synthesizer: str
    use_cases: list[str] = field(default_factory=list)


def _config_path() -> Path:
    """Locate the pools config; override with FUSION_POOLS_CONFIG."""
    override = os.environ.get("FUSION_POOLS_CONFIG")
    if override:
        return Path(override).expanduser()
    return Path(__file__).resolve().parent.parent / "configs" / "model-pools.yaml"


@lru_cache(maxsize=1)
def _load_pools() -> dict[str, "ModelPool"]:
    path = _config_path()
    if not path.exists():
        raise FileNotFoundError(
            f"Model pool config not found at {path}. "
            "Set FUSION_POOLS_CONFIG to point at your model-pools.yaml."
        )

    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    raw_pools = data.get("pools", {})
    pools: dict[str, ModelPool] = {}

    for name, cfg in raw_pools.items():
        models = cfg.get("models", [])
        if not models:
            raise ValueError(f"Pool '{name}' defines no models.")
        synthesizer = cfg.get("synthesizer") or models[0]
        pools[name] = ModelPool(
            name=name,
            description=cfg.get("description", ""),
            models=list(models),
            synthesizer=synthesizer,
            use_cases=list(cfg.get("use_cases", [])),
        )

    if not pools:
        raise ValueError(f"No pools found in {path}.")

    return pools


def reload_pools() -> None:
    """Clear cached pools (e.g. after editing the YAML at runtime)."""
    _load_pools.cache_clear()


def get_pool(name: str) -> ModelPool:
    """Get a model pool by name. Raises ValueError if not found."""
    pools = _load_pools()
    if name not in pools:
        available = ", ".join(sorted(pools.keys()))
        raise ValueError(f"Unknown pool '{name}'. Available: {available}")
    return pools[name]


def list_pools() -> dict[str, str]:
    """Return dict of pool names to descriptions."""
    return {name: pool.description for name, pool in _load_pools().items()}
