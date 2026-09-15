"""Minimal typed models for initialization boundaries."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class SourceArtifact:
    source_id: str
    origin: str
    content_type: str
    captured_at: str
    content_hash: str
    license_note: str
    trust_classification: str
    raw_reference: str


@dataclass(frozen=True)
class KnowledgeRelationship:
    relation_type: str
    target_id: str
    note: str | None = None


@dataclass(frozen=True)
class KnowledgeRecord:
    record_id: str
    source_ids: tuple[str, ...]
    title: str
    summary: str
    concepts: tuple[str, ...] = field(default_factory=tuple)
    candidate_claims: tuple[str, ...] = field(default_factory=tuple)
    authority_class: str = "unknown"
    relationships: tuple[KnowledgeRelationship, ...] = field(default_factory=tuple)
    review_state: str = "proposed"
    decision_provenance: str | None = None


@dataclass(frozen=True)
class RetrievalChunk:
    """Source-faithful retrieval unit; only approved chunks are eligible for trusted retrieval."""

    chunk_id: str
    source_id: str
    parent_section_id: str
    content: str
    content_hash: str
    heading_path: tuple[str, ...]
    location: str
    chunk_type: str
    review_state: str = "proposed"
    record_id: str | None = None
