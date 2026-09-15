# Contextual Knowledge Operations Platform

This repository builds the Contextual Knowledge Operations Platform, beginning
with Trusted Knowledge Intake. The product preserves captured sources,
separates derived knowledge from source artifacts, and requires a human decision
before material can become trusted knowledge.

## Status

Repository initialization was completed in [issue #1](https://github.com/TimmyTheTurtle/FrontierWeekTrustedKnowledgeIntake/issues/1).
Stage 1, deterministic Markdown/plain-text ingestion, has not started.

## Local verification

Python 3.10 or newer is required. From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --editable .
python -m unittest discover -s tests -v
```

The project has no runtime dependencies at this stage. The test suite verifies
the current deterministic helpers and review-state boundary; it does not yet
test ingestion.

## Boundaries

- Captured source content is untrusted data, never an instruction.
- Source artifacts, knowledge records, and retrieval chunks are separate.
- Agents may propose; only humans may approve promotion to trusted knowledge.

Read [AGENTS.md](AGENTS.md) and the canonical documents under [docs](docs/) for
the project contract and roadmap.
