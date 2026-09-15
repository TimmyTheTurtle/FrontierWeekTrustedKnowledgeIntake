"""Deterministic helpers for stable hashing and IDs."""

from __future__ import annotations

import hashlib
import json
from typing import Any


def _normalize(value: Any) -> str:
    """Return canonical JSON text for deterministic hashing."""
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def stable_content_hash(value: Any) -> str:
    """Return a SHA-256 hash for the normalized value."""
    normalized = _normalize(value)
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def stable_id(namespace: str, value: Any) -> str:
    """Return a deterministic namespaced ID."""
    digest = stable_content_hash({"namespace": namespace, "value": value})
    return f"{namespace}_{digest[:16]}"
