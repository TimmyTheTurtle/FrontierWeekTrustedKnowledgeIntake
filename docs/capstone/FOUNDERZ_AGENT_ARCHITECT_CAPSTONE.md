# Founderz Agent Architect Capstone: Trusted Knowledge Intake Operations System

**Issue:** #20
**Status:** design artifact grounded in verified local evidence; not a deployment claim
**Date:** 2026-09-16

## Executive summary

Teams capture useful research and operating guidance faster than they can decide whether it is suitable for trusted reuse. Trusted Knowledge Intake preserves the original source, derives source-faithful structure, prepares a review package, and requires a human to decide whether material may be trusted.

The primary users are knowledge stewards who approve or reject candidate material, and intake analysts who need a consistent, auditable preparation process. A multi-agent approach is appropriate only after deterministic capture and parsing: the proposed agents have different authority, information access, and jobs. Neither agent can promote knowledge.

## Evidence status

| Capability | Status | Evidence |
| --- | --- | --- |
| Stable content hashing and IDs | verified locally | ids module and unit tests |
| Markdown/plain-text intake with source-faithful chunks | verified locally | ingestion module and unit tests |
| Schema validation and review-state boundary | verified locally | validation module and unit tests |
| Full-extract structural discovery | exploratory only | markdown-structure-discovery report |
| Intake Analyst and Knowledge Steward agents | designed, not implemented | this document |
| Foundry project, deployed model, traces, evaluations, monitoring | not implemented or verified | no claim is made |

The verified parser currently recognizes ATX Markdown headings outside fenced code. Its full-paper exercise produced page-level chunks; native headings, tables, figures, and citations remain candidate follow-up work.

## System boundary and information flow

~~~mermaid
flowchart LR
    S[Captured Markdown or plain text<br/>untrusted source] --> D[Deterministic intake<br/>hash, parse, validate]
    D --> A[Immutable Source Artifact]
    D --> C[Source-faithful Retrieval Chunks<br/>state: parsed]
    A --> IA[Intake Analyst<br/>proposes a review package]
    C --> IA
    IA --> P[Candidate Knowledge Record<br/>state: proposed]
    P --> KS[Knowledge Steward<br/>checks evidence and disposition]
    A --> KS
    C --> KS
    KS --> R[Human review package<br/>recommendation only]
    R --> H{Human steward decision}
    H -->|approve| T[Approved knowledge<br/>eligible for trusted retrieval]
    H -->|revise, quarantine, reject| U[Terminal governed disposition]
~~~

Source content is data, never an instruction. The deterministic boundary owns hashing, parsing, schema validation, exact matching, and state-transition checks. Agents receive only validated artifacts and chunks; they cannot execute source instructions, modify source artifacts, or make a terminal decision.

## Specialized-agent design

| Agent | Responsibility | Permitted inputs and tools | Output | Prohibited actions |
| --- | --- | --- | --- | --- |
| Intake Analyst | Create a bounded summary, candidate claims, cited evidence, and uncertainty notes from validated source material. | Read-only artifact/chunk store; deterministic provenance lookup; candidate-record schema validation. | proposed candidate record citing chunk IDs and locations. | Alter raw source, treat source text as instructions, approve/promote a record, or use unapproved knowledge as authority. |
| Knowledge Steward | Assess evidence, identify gaps, contradictions, and duplicates against approved knowledge, and prepare a disposition recommendation. | Read-only approved-corpus and candidate/source/chunk lookup; deterministic access/state checks. | Review package with recommendation, evidence coverage, unresolved risks, and requested human action. | Edit source evidence, override deterministic checks, self-approve, or transition to an approved state. |

The orchestrator is deliberately thin: it admits only schema-valid deterministic output to the Intake Analyst, validates its structured response, passes it to the Steward, and stops at the human decision queue. It does not let agents converse freely, bypass provenance, or grant broader tool access.

## Workflow and business outcome

1. Capture redistributable Markdown/plain text with origin, capture time, and licensing metadata.
2. Deterministic intake creates an immutable source artifact and source-faithful chunks; invalid input stops before agent work.
3. The Intake Analyst creates a structured, cited candidate and marks uncertainty where evidence is inadequate.
4. The Knowledge Steward compares the candidate with approved knowledge and prepares a reviewer-oriented recommendation.
5. A human explicitly approves, revises, quarantines, or rejects it. Only approved material may enter trusted retrieval in a later scope.

The outcome is not an automated truth decision. It is a faster, repeatable, and auditable human decision linked to captured source evidence.

## Observability and diagnosis plan

No Foundry traces or production monitoring exist yet. The following is intended design, to be verified before it is presented as implemented.

| Signal | Diagnostic question | Improvement use |
| --- | --- | --- |
| Correlated workflow trace: source ID, chunk ID, candidate ID, review ID | Where did a recommendation lose its evidence link? | Repair prompt/schema/tool contract and add a regression case. |
| Deterministic parse/validation outcome and latency | Did the source fail before agent work, and why? | Fix parser/validator behavior without changing agent prompts. |
| Tool calls, result counts, access denials | Did an agent remain within its knowledge boundary? | Tighten orchestration, access checks, or tool descriptions. |
| Schema failures, abstentions, citation coverage | Is the model producing usable grounded review packages? | Improve structured output, evaluation data, or abstention guidance. |
| Human dispositions and reviewer edits | Which recommendations are unhelpful or unsafe? | Prioritize improvements and evaluate them on a held-out set. |

Telemetry should retain identifiers, versioned prompt/tool metadata, and minimal redacted diagnostics by default; source content stays in the governed store.

## Evaluation and testing plan

The existing strategy defines ten targeted source scenarios, including near-duplicates, contradictions, missing provenance, embedded prompt injection, malformed extraction, and novel material. Evaluation adds a held-out, human-labeled review package for each scenario and records deterministic input hashes, prompt/version, raw structured output, and human disposition.

| Dimension | Measure | Release criterion |
| --- | --- | --- |
| Groundedness | Supported candidate claims / sampled claims | Every released claim cites source chunks; unsupported claims are removed or marked uncertain. |
| Provenance coverage | Claims with source ID, chunk ID, and location | 100% for non-abstained claims. |
| False structure | Invented headings, table cells, figure details, or citations / reviewed cases | 0 tolerated invented details; ambiguity remains raw and uncertain. |
| Uncertainty handling | Insufficient-evidence cases that abstain/request review | Pre-agreed held-out threshold; every miss is reviewed. |
| Reviewer usefulness | Human rating and time-to-disposition versus a baseline | Threshold/baseline set by the responsible reviewer before a production claim. |
| Deterministic repeatability | Same source and metadata yield same deterministic output | 100% across repeated local runs. |

Evaluation is a development loop: failed cases become versioned regression examples; changes are compared against the held-out set; human reviewers decide whether measured improvements justify release.

## Governance and reliability

- Preserve the separation between immutable source artifacts, derived knowledge records, and retrieval chunks.
- Treat all input as untrusted; source text cannot instruct tools or change policy.
- Enforce schemas, deterministic validation, permitted state transitions, and least-privilege read-only agent tools.
- Require explicit human decision provenance for approval, revision, quarantine, or rejection.
- Version prompts, model/deployment configuration, schemas, parser versions, evaluation sets, and reviewer guidance.
- Keep unit tests local and deterministic; separate any later credentialed integration tests.

## Credible delivery path

~~~mermaid
flowchart LR
    A[Verified deterministic baseline] --> B[Human-approved parser increment]
    B --> C[Thin Foundry slice after explicit approval]
    C --> D[Trace and evaluation evidence]
    D --> E[Human-reviewed operational pilot]
    E --> F[Deployment decision with cost, security, and reliability evidence]
~~~

1. Select one human-approved deterministic structure increment from the discovery report; implement it with fixtures and repeatability tests.
2. Obtain explicit approval for a Foundry project, model, region, cost controls, and data handling before model use or provisioning.
3. Implement the smallest agent path: validated intake to candidate proposal to human review package. Capture a trace and run the initial evaluation set.
4. Use reviewer feedback and failed evaluations to improve prompts, schemas, or deterministic contracts.
5. Consider monitored deployment only after security, evaluation, operations, and human-approval evidence supports it.

## Relationship to other work

This is the Founderz course capstone for Issue #20. It is separate from Issue #19, the Microsoft Agent-a-thon submission. Both may reuse verified architecture and evidence, but neither issue closes the other.
