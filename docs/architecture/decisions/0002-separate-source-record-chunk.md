# ADR 0002: Separate source artifact, knowledge record, and retrieval chunk

## Status
Accepted

## Decision
Keep immutable source artifacts, structured knowledge records, and retrieval chunks as separate model entities.

## Consequences
- Provenance remains traceable to immutable source text.
- Derived content cannot overwrite source truth.
- Retrieval optimization does not redefine knowledge approval state.
