"""Initialization schemas for core trusted-knowledge entities."""

REVIEW_STATES = (
    "captured",
    "parsed",
    "proposed",
    "reviewed",
    "approved",
    "revised",
    "quarantined",
    "rejected",
)

TERMINAL_REVIEW_STATES = ("approved", "revised", "quarantined", "rejected")

TRUST_CLASSIFICATIONS = ("untrusted", "trusted", "quarantined", "unknown")

SOURCE_ARTIFACT_REQUIRED_FIELDS = (
    "source_id",
    "origin",
    "content_type",
    "captured_at",
    "content_hash",
    "license_note",
    "trust_classification",
    "raw_reference",
)

KNOWLEDGE_RECORD_REQUIRED_FIELDS = (
    "record_id",
    "source_ids",
    "title",
    "summary",
    "concepts",
    "candidate_claims",
    "authority_class",
    "relationships",
    "review_state",
    "decision_provenance",
)

RETRIEVAL_CHUNK_REQUIRED_FIELDS = (
    "chunk_id",
    "source_id",
    "parent_section_id",
    "content",
    "content_hash",
    "heading_path",
    "location",
    "chunk_type",
    "review_state",
)

REVIEW_STATE_TRANSITIONS = {
    "captured": ("parsed",),
    "parsed": ("proposed",),
    "proposed": ("reviewed",),
    "reviewed": TERMINAL_REVIEW_STATES,
    "approved": (),
    "revised": (),
    "quarantined": (),
    "rejected": (),
}
