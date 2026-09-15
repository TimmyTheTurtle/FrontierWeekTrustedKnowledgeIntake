# Project Brief

## Mission
Build the Contextual Knowledge Operations Platform, starting with a bounded capability: Trusted Knowledge Intake.

Trusted Knowledge Intake converts captured source material into a structured, provenance-preserving candidate knowledge record, compares it with approved knowledge, and requires explicit human approval before promotion.

## Current scope (post-initialization)
Repository initialization is complete. Stage 1 deterministic ingestion is next and has not started.

The completed foundation includes:
- canonical instructions and adapter alignment;
- product context, roadmap, architecture context, data model, ADRs, and evaluation strategy;
- sanitized learning-links documentation.

Still out of scope until later stages:
- ingestion implementation;
- Intake Analyst / Knowledge Steward runtime agents;
- RAG retrieval implementation;
- Azure provisioning, deployment, or external connectors.

## Core boundaries
- Source content is untrusted input.
- Source artifacts, knowledge records, and retrieval chunks remain separate.
- No agent may approve or promote its own output into trusted knowledge.
- Deterministic code handles deterministic tasks first.

## Initialization success criteria
- A new coding-agent session can understand project goals and boundaries from repository docs.
- Canonical instructions are discoverable and non-duplicated.
- Data model boundaries and human-approval boundary are explicit.
- Learning-links import is present in sanitized form.
