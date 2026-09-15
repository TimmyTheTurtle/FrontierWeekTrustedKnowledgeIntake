"""Validation helpers for initialization schema and boundary checks."""

from __future__ import annotations

from typing import Any

from .review_state import can_transition, requires_human_decision
from .schemas import (
    KNOWLEDGE_RECORD_REQUIRED_FIELDS,
    RETRIEVAL_CHUNK_REQUIRED_FIELDS,
    REVIEW_STATES,
    SOURCE_ARTIFACT_REQUIRED_FIELDS,
)


def _missing_fields(payload: dict[str, Any], required_fields: tuple[str, ...]) -> list[str]:
    return [name for name in required_fields if name not in payload or payload[name] in (None, "")]


def validate_source_artifact(payload: dict[str, Any]) -> list[str]:
    """Return validation errors for source artifacts."""
    return [f"missing field: {name}" for name in _missing_fields(payload, SOURCE_ARTIFACT_REQUIRED_FIELDS)]


def validate_knowledge_record(
    payload: dict[str, Any],
    *,
    from_state: str | None = None,
    human_decision_evidence: str | None = None,
) -> list[str]:
    """Return validation errors for knowledge records."""
    errors = [f"missing field: {name}" for name in _missing_fields(payload, KNOWLEDGE_RECORD_REQUIRED_FIELDS)]

    to_state = payload.get("review_state")
    if to_state and to_state not in REVIEW_STATES:
        errors.append(f"invalid review_state: {to_state}")

    if from_state and to_state and not can_transition(from_state, to_state):
        errors.append(f"invalid transition: {from_state} -> {to_state}")

    if to_state and requires_human_decision(to_state) and not human_decision_evidence:
        errors.append(f"human decision evidence required for review_state: {to_state}")

    return errors


def validate_retrieval_chunk(payload: dict[str, Any]) -> list[str]:
    """Return validation errors for retrieval chunks."""
    errors = [f"missing field: {name}" for name in _missing_fields(payload, RETRIEVAL_CHUNK_REQUIRED_FIELDS)]

    state = payload.get("review_state")
    if state and state not in REVIEW_STATES:
        errors.append(f"invalid review_state: {state}")

    return errors
