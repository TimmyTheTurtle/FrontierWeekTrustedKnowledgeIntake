"""Foundational models and deterministic ingestion for trusted knowledge intake."""

from .ingestion import IngestionResult, ingest_markdown
from .ids import stable_content_hash, stable_id
from .models import KnowledgeRecord, KnowledgeRelationship, RetrievalChunk, SourceArtifact
from .review_state import can_transition, is_terminal_state, requires_human_decision
from .validation import validate_knowledge_record, validate_retrieval_chunk, validate_source_artifact

__all__ = [
    "IngestionResult",
    "ingest_markdown",
    "KnowledgeRecord",
    "KnowledgeRelationship",
    "RetrievalChunk",
    "SourceArtifact",
    "stable_content_hash",
    "stable_id",
    "can_transition",
    "is_terminal_state",
    "requires_human_decision",
    "validate_source_artifact",
    "validate_knowledge_record",
    "validate_retrieval_chunk",
]
