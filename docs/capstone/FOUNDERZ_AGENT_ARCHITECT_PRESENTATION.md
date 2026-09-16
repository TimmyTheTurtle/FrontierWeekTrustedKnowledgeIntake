# Founderz Agent Architect capstone presentation

**Target duration:** 2 minutes 40 seconds to 2 minutes 55 seconds
**Recording status:** script and visual plan only; no recording has been made

## Slide/scene plan and narration

### 0:00-0:20 - The problem

Show the first diagram from the capstone design document.

“Teams collect valuable material faster than they can decide whether it should be trusted. Trusted Knowledge Intake makes that decision auditable. It preserves the source, prepares a review package, and keeps final authority with a human knowledge steward.”

### 0:20-0:50 - What is real today

Show the evidence-status table and deterministic intake test output.

“The foundation is deliberately narrow. Local deterministic code hashes Markdown, preserves source-faithful chunks with line provenance, and validates schemas and review-state rules. A full-paper discovery exercise showed where native structure is still flattened. I do not claim agents, Foundry, traces, or deployment are already implemented.”

### 0:50-1:30 - Why two agents

Show the specialized-agent table.

“The proposed Intake Analyst reads validated artifacts and chunks to produce cited candidate claims and uncertainty notes. The proposed Knowledge Steward checks that package against approved knowledge and prepares a human recommendation. Their tools are read-only and deliberately different. Neither agent can approve knowledge.”

### 1:30-2:05 - Reliability and governance

Show the human-decision portion of the workflow.

“Source content is untrusted data, never an instruction. Deterministic code owns hashes, parsing, validation, and state transitions. Every claim needs a source chunk and location. A human explicitly approves, revises, quarantines, or rejects the recommendation.”

### 2:05-2:35 - Measuring useful behavior

Show the evaluation table.

“I would evaluate groundedness, provenance coverage, invented structure, uncertainty handling, reviewer usefulness, and deterministic repeatability. The existing scenarios include prompt injection, malformed extraction, and contradictions. Failed cases become regression cases; reviewer feedback guides the next improvement.”

### 2:35-2:55 - Production path

Show the delivery-path diagram.

“The path to production is evidence-led: first a human-approved parser increment, then an explicitly approved thin Foundry slice, trace and evaluation evidence, and only then a monitored deployment decision. The outcome is not an automated truth machine; it is a more consistent, source-linked human decision.”

## Recording checklist

- Capture only verified local code/test output and capstone diagrams; label proposed architecture as proposed.
- Keep the final recording at or below three minutes.
- Do not show secrets, private source material, unverified Foundry resources, or fabricated traces/evaluation results.
- Review the final video against Issue #20 acceptance criteria before upload.
