# Policy-to-Configuration Regression Tribunal — Project Handoff

**Status:** planning handoff; no new repository created yet  
**Created:** 2026-09-17  
**Intended use:** seed a brand-new, user-selected repository for the Microsoft Agent-a-thon Level 3: Architect competition.

## 1. Product in one sentence

Build an evidence-first, multi-agent review system that detects when a proposed
operational configuration may silently change the meaning of an approved policy,
then requires a human to decide the disposition.

This is decision support, not legal, regulatory, or compliance advice.

## 2. Why this is the competition slice

The Agent-a-thon winner examples favored a consequential decision, specialized
agent roles, a clear orchestration path, testing/iteration, and measurable or
forecast impact. This concept is not a generic legal-document summarizer:
it catches a plausible regression *before release* and shows exactly why a
human should review it.

The project takes architectural inspiration from `Dorian-Klingenberg/legal-tech-debt`
but must be an original project. Do not copy its corpus, findings, prompts,
fixtures, screenshots, or wording into the new repository.

## 3. Core review question

> Does a proposed configuration faithfully implement the selected approved policy
> baseline, or does it introduce a material semantic regression that needs human
> review?

## 4. In-scope smells

Use only these three, narrowly defined candidate-review smells in the first
vertical slice:

1. **Scope inversion** — the configuration broadens, narrows, or reverses a
   conditional policy rule.
2. **Exception-path erasure** — an approved exception, escalation, or human
   review path disappears from the operational configuration.
3. **Authority propagation drift** — a newer approved baseline or dated change
   bulletin is not reflected in the proposed configuration.

A smell is an evidence-backed *candidate review case*, never a legal conclusion.

## 5. Non-goals

- Do not build a generic legal-smell detector or reproduce the 159-smell Legal
  Tech Debt taxonomy.
- Do not determine legal compliance, coverage, enforceability, or liability.
- Do not auto-approve, auto-deploy, or mutate a configuration.
- Do not add RAG, vector search, external connectors, customer data, persistence,
  authentication, or production deployment in the first slice.
- Do not make a multi-agent chain where roles merely restate one another.

## 6. Source-material and rights policy

All first-slice artifacts must be newly authored, fictional, and safe to show
in source control, Foundry prompts/traces, screenshots, video, supporting files,
and a shared competition activity page.

Use a fictional jurisdiction, organization, policy, configuration, and release
history. Do not reuse real carrier forms, SERFF filings, ISO material, regulatory
documents, Legal Tech Debt corpus material, prior-project fixtures, or source text
without a separately documented source-by-source reuse basis.

Every source artifact needs provenance metadata: origin, content hash, rights
classification/reuse basis, and whether it is eligible for the public demo.

## 7. Fictional source pack

Create four small original Markdown/plain-text documents:

1. **Approved policy baseline** — primary rule plus a narrow escalation or
   exception condition.
2. **Approved change bulletin** — newer effective date and an updated obligation.
3. **Proposed operational configuration** — a realistic declarative workflow
   configuration that may diverge from the first two documents.
4. **Release note** — claims what was changed and sets up a possible conflict.

Later, an original PDF generated from this source text may be added only after
the Markdown path works and only if it materially strengthens the demo.

## 8. Minimum architecture

```text
Validated fictional sources
        |
        v
Deterministic intake and gates
hashes, parsing, source identity/rights, dates, structural chunks, schemas,
citation resolution, instruction-as-data protection
        |
        v
Evidence Mapper (Foundry agent)
source chunks -> cited factual evidence ledger and ambiguity list
        |
        v
Drift Investigator (Foundry agent)
ledger + selected policy baseline -> one regression hypothesis or abstention
        |
        v
Skeptical Reviewer (Foundry agent)
original ledger + hypothesis -> confirmed | refuted | insufficient review packet
        |
        v
Deterministic orchestrator and renderer
validates typed handoffs; blocks invalid claims; produces human-review package
        |
        v
Human reviewer
review | revise | quarantine | reject
```

### Why orchestration is required

The Investigator is rewarded for finding a plausible semantic regression. The
Skeptical Reviewer has the opposite success condition: it must disprove the
hypothesis with counterevidence or mark it insufficient. A single agent doing
both makes confirmation bias unobservable. The deterministic orchestrator is
not an agent and must retain all exact validation and state-transition work.

## 9. Required output contracts

Every agent output must be typed JSON and validated before handoff. A
non-abstained proposition must include only supplied source IDs, chunk IDs, and
locations. No output may contain a terminal human disposition.

Required high-level fields:

- `workflow_id`
- `agent`, `agent_version`, and model/deployment identity
- cited evidence and counterevidence
- `outcome` or `verdict`
- `uncertainties`, `missing_evidence`, and `limitations`
- reviewer question and required human action

## 10. Monitoring and trace evidence

Generate one deterministic `workflow_id` and include it in every source record,
agent request, agent response, gate event, trace, and final review package.

Record:

- source IDs/hashes, rights classification, parser/schema versions;
- agent/prompt/model versions, trace IDs, per-step duration, token count,
  failure/retry count;
- schema, citation, integrity, and route-gate outcomes;
- evidence-ledger count, hypothesis/abstention, reviewer verdict, and missing
  evidence reason;
- human disposition, reviewer edits, and overturn reason.

The first evidence view should show a correlated workflow timeline and an
evidence-continuity path from each final proposition to a chunk location and
source hash. Do not claim distributed tracing unless directly verified.

## 11. Six-case evaluation matrix

| Case | Expected reviewer result | Primary evidence |
| --- | --- | --- |
| Clear regression | `confirmed` | Detects a material policy-to-config meaning change. |
| Equivalent wording | `refuted` | Avoids mistaking paraphrase for a defect. |
| Missing proposed configuration | `insufficient` | Does not infer a configuration change. |
| Superseded baseline | `refuted` or `insufficient` | Honors source role, recency, and effective date. |
| Conflicting source roles | `insufficient` | Escalates disagreement rather than selecting authority. |
| Embedded instruction | integrity route / quarantine | Treats source text as data, never as an instruction. |

For every case, verify exact expected disposition, schema validity, citation
resolution for each non-abstained proposition, no invented factual content, and
no agent-issued approval. Rerun one clear-regression case and compare
disposition, cited evidence roles, and routing rather than brittle wording.

## 12. Usability and impact evidence

Run an exploratory reviewer walkthrough using the same fictional source pack:

1. Ask a reviewer to decide from the raw documents.
2. Ask the reviewer to decide from the generated review package.
3. Record time-to-disposition, decisive evidence found, and whether the outcome
   matched the known test label.

If there is only one tester, call this an exploratory walkthrough, not user
research. Any impact claim must be a bounded forecast based on observed
evidence, for example: reducing evidence assembly during policy-configuration
review. Do not claim enterprise savings or legal-compliance outcomes.

## 13. Suggested repository bootstrap

Create the new repository only after its name, owner, visibility, and initial
license are chosen. Start with:

```text
AGENTS.md
README.md
docs/
  PROJECT_BRIEF.md
  ARCHITECTURE.md
  DATA_RIGHTS.md
  EVALUATION_PLAN.md
  HANDOFF.md (copy this document, then maintain it in-repo)
data/
  synthetic/
tests/
src/
```

The new root `AGENTS.md` should preserve these non-negotiables: source-rights
provenance, untrusted source text, deterministic validation first, typed agent
handoffs, no automatic approval, synthetic-only first slice, and evidence-backed
claims.

## 14. Settled versus open decisions

### Agreed direction

- Start a separate repository rather than expanding the existing Trusted
  Knowledge Intake repository.
- Use an original, fictional source pack.
- Build the Policy-to-Configuration Regression Tribunal vertical slice.
- Keep the first taxonomy to the three smells in section 4.
- Use multi-agent orchestration only for distinct evidence mapping,
  regression-hypothesis, and skeptical-review work.
- Treat monitoring and evaluation as demonstrated product evidence.

### Still open

- New repository name, owner, visibility, and license.
- Exact fictional domain vocabulary and organization names.
- Whether existing Foundry resources/agents may be reused or a new project and
  deployment are needed; do not assume permission, cost, or data-handling terms.
- Precise agent contracts and selected model/deployment.
- Whether an original generated PDF belongs in the final demo.
- What the competition's full official rules say beyond the already verified
  public submission guidance; do not claim the unparsed rules PDF was reviewed.

## 15. Immediate next action

Before implementation, review this handoff and choose the repository identity.
Then create the repository, copy this document into `docs/HANDOFF.md`, and make
the first reviewable change: define the four original source artifacts and the
six-case evaluation matrix without calling a model.

## 16. Source context

- Microsoft Agent-a-thon transcript captured locally on 2026-09-17:
  `D:\ai-engineering\FrontierWeekTrustedKnowledgeIntake\docs\Agentathon_transcript.md`
- Legal Tech Debt taxonomy (inspiration only):
  <https://github.com/Dorian-Klingenberg/legal-tech-debt/blob/main/legal_code_smell_taxonomy.md>
  <https://github.com/Dorian-Klingenberg/legal-tech-debt/blob/main/insurance_policy_smells.md>
  <https://github.com/Dorian-Klingenberg/legal-tech-debt/blob/main/insurance_claims_smells.md>
