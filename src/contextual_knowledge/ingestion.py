"""Deterministic, local Markdown ingestion for untrusted source content.

This module only derives provenance-preserving source artifacts and chunks.  It
does not interpret source text as instructions or promote it to knowledge.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import re

from .ids import stable_content_hash, stable_id
from .models import RetrievalChunk, SourceArtifact
from .validation import validate_retrieval_chunk, validate_source_artifact


_ATX_HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*#*[ \t]*$")
_FENCE = re.compile(r"^[ \t]*(`{3,}|~{3,})")


@dataclass(frozen=True)
class IngestionResult:
    """The deterministic output from ingesting one local Markdown source."""

    source_artifact: SourceArtifact
    chunks: tuple[RetrievalChunk, ...]


@dataclass(frozen=True)
class _Section:
    heading_path: tuple[str, ...]
    body_start_line: int
    body_end_line: int
    content: str


def ingest_markdown(
    document: str | bytes,
    *,
    origin: str,
    captured_at: str,
    license_note: str,
    raw_reference: str | None = None,
) -> IngestionResult:
    """Ingest one UTF-8 Markdown document using only deterministic local code.

    ``captured_at`` is caller-provided rather than generated so repeated calls
    over the same capture metadata have identical output.  ``document`` is
    treated solely as untrusted content; this parser recognizes structure but
    never executes or follows instructions embedded in the source.
    """
    source_text = _decode_utf8(document)
    if not origin:
        raise ValueError("origin must not be empty")
    if not captured_at:
        raise ValueError("captured_at must not be empty")
    if not license_note:
        raise ValueError("license_note must not be empty")

    content_hash = stable_content_hash(source_text)
    source_id = stable_id("source", {"content_hash": content_hash})
    artifact = SourceArtifact(
        source_id=source_id,
        origin=origin,
        content_type="text/markdown",
        captured_at=captured_at,
        content_hash=content_hash,
        license_note=license_note,
        trust_classification="untrusted",
        raw_reference=raw_reference or origin,
    )
    _validate_or_raise("source artifact", validate_source_artifact(asdict(artifact)))

    chunks = tuple(_make_chunk(source_id, section) for section in _parse_sections(source_text))
    for chunk in chunks:
        _validate_or_raise("retrieval chunk", validate_retrieval_chunk(asdict(chunk)))
    return IngestionResult(source_artifact=artifact, chunks=chunks)


def _decode_utf8(document: str | bytes) -> str:
    if isinstance(document, str):
        return document
    if isinstance(document, bytes):
        return document.decode("utf-8")
    raise TypeError("document must be str or UTF-8 bytes")


def _parse_sections(source_text: str) -> tuple[_Section, ...]:
    """Return non-empty section bodies, excluding headings and preserving text."""
    lines = source_text.splitlines(keepends=True)
    headings: list[tuple[int, int, str]] = []
    fence_marker: str | None = None
    for index, line in enumerate(lines):
        fence = _FENCE.match(line)
        if fence:
            marker = fence.group(1)
            if fence_marker is None:
                fence_marker = marker[0]
            elif marker[0] == fence_marker:
                fence_marker = None
            continue
        if fence_marker is not None:
            continue
        match = _ATX_HEADING.match(line.rstrip("\r\n"))
        if match:
            headings.append((index, len(match.group(1)), match.group(2)))

    sections: list[_Section] = []
    heading_path: list[str] = []
    body_start = 0
    for line_index, level, title in headings:
        section = _section_from_lines(lines, body_start, line_index, tuple(heading_path))
        if section is not None:
            sections.append(section)
        del heading_path[level - 1 :]
        heading_path.append(title)
        body_start = line_index + 1

    section = _section_from_lines(lines, body_start, len(lines), tuple(heading_path))
    if section is not None:
        sections.append(section)
    return tuple(sections)


def _section_from_lines(
    lines: list[str], start: int, end: int, heading_path: tuple[str, ...]
) -> _Section | None:
    while start < end and not lines[start].strip():
        start += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    if start == end:
        return None
    return _Section(
        heading_path=heading_path,
        body_start_line=start + 1,
        body_end_line=end,
        content="".join(lines[start:end]),
    )


def _make_chunk(source_id: str, section: _Section) -> RetrievalChunk:
    parent_section_id = stable_id(
        "section", {"source_id": source_id, "heading_path": section.heading_path}
    )
    location = f"lines:{section.body_start_line}-{section.body_end_line}"
    content_hash = stable_content_hash(section.content)
    chunk_id = stable_id(
        "chunk",
        {
            "source_id": source_id,
            "parent_section_id": parent_section_id,
            "location": location,
            "content_hash": content_hash,
        },
    )
    return RetrievalChunk(
        chunk_id=chunk_id,
        source_id=source_id,
        parent_section_id=parent_section_id,
        content=section.content,
        content_hash=content_hash,
        heading_path=section.heading_path,
        location=location,
        chunk_type="section",
        review_state="parsed",
    )


def _validate_or_raise(entity_name: str, errors: list[str]) -> None:
    if errors:
        raise ValueError(f"invalid {entity_name}: {', '.join(errors)}")
