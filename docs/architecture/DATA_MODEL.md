# Data Model

The model keeps three distinct concepts.

## Source Artifact
Immutable captured source and provenance anchor.

Minimum fields:
- `source_id`
- `origin`
- `content_type`
- `captured_at`
- `content_hash`
- `license_note`
- `trust_classification`
- `raw_reference`

## Knowledge Record
Structured candidate/approved knowledge derived from one or more sources.

Minimum fields:
- `record_id`
- `source_ids`
- `title`
- `summary`
- `concepts`
- `candidate_claims`
- `authority_class`
- `relationships`
- `review_state`
- `decision_provenance`

## Retrieval Chunk
Source-faithful retrieval/citation unit tied to structural location.

Minimum fields:
- `chunk_id`
- `source_id`
- `record_id` (optional)
- `parent_section_id`
- `content`
- `content_hash`
- `heading_path`
- `location`
- `chunk_type`
- `review_state`

## Review-state boundary
Required transition pattern:
`captured -> parsed -> proposed -> reviewed -> approved | revised | quarantined | rejected`

Only `approved` records/chunks are eligible for trusted retrieval.
