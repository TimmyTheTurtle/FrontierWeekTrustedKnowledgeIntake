"""Review-state transition helpers with human-approval boundary enforcement."""

from __future__ import annotations

from .schemas import REVIEW_STATE_TRANSITIONS, TERMINAL_REVIEW_STATES


HUMAN_DECISION_STATES = TERMINAL_REVIEW_STATES


def can_transition(from_state: str, to_state: str) -> bool:
    """Return whether a transition is allowed by the initialization state model."""
    if from_state == to_state:
        return True
    return to_state in REVIEW_STATE_TRANSITIONS.get(from_state, ())


def is_terminal_state(state: str) -> bool:
    """Return True when a state is terminal."""
    return state in TERMINAL_REVIEW_STATES


def requires_human_decision(to_state: str) -> bool:
    """Return True when entering the state requires explicit human decision evidence."""
    return to_state in HUMAN_DECISION_STATES
