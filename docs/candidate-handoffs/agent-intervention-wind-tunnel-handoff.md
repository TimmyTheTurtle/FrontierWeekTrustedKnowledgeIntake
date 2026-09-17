# Agent Intervention Wind Tunnel — Project Handoff

**Status:** planning handoff; no new repository created yet  
**Created:** 2026-09-17  
**Intended use:** seed a brand-new, user-selected repository for the Microsoft Agent-a-thon Level 3: Architect competition.

## 1. Product in one sentence

Build an evidence-first test harness that runs agent-proposed operational
interventions through a small deterministic simulator, exposes unintended
consequences, and requires human review before any recommendation is accepted.

The working metaphor is a **wind tunnel for intervention agents**: test plans
against a known, inspectable world before trusting them in a real one.

## 2. Competition rationale

The strongest Agent-a-thon examples are more than chat experiences: they make a
consequential decision visible, give agents specialized roles, demonstrate that
the system works, and show impact. This concept provides all four:

- a visible proposed intervention;
- deterministic proof of both intended and collateral effects;
- an adversarial agent role that is rewarded for finding failure;
- a recovery role that must improve the plan; and
- measurable safety and reliability outcomes.

The project is inspired by the *pattern* in `Dorian-Klingenberg/watershed`:
hidden-system scenarios, constrained actions, factual evidence capture,
role-differentiated testing, and human adjudication. It must not copy Watershed
code, lore, scenarios, assets, prompts, tester identities, screenshots, or
wording. It is not a game and it is not a flood-response digital twin.

## 3. Core review question

> Can an AI-proposed intervention achieve the stated objective without causing
> unacceptable collateral effects when tested against a deterministic scenario?

The system advises. It never applies an intervention to a real system.

## 4. Differentiated competition position

Do **not** position this as disaster response, flood allocation, a digital twin
for emergency management, or a fantasy/game adaptation. A previous competition
winner already demonstrated a crisis-response digital twin.

Position it as an **agent safety and evaluation harness** for any action-taking
agent that must reason about partially observed systems. The first fictional
scenario is only a legible controlled experiment, not the product domain.

## 5. First scenario: original controlled intervention exercise

Implement one small, wholly fictional, grid or graph-based resource-routing
scenario. It needs:

- one explicit objective, such as deliver a resource to a target zone;
- one hidden dependency that makes a naive high-throughput plan unsafe;
- two observable collateral dimensions, such as protected-zone overload and
  route instability;
- a finite, explicit action grammar; and
- deterministic reset, state transition, and result calculation.

Use original neutral names such as `source`, `target_zone`, `protected_zone`,
and `stability_path`. Do not reuse Watershed location names, mechanics, action
names, story details, or source data.

### Candidate truth model

The simulator owns all world truth:

- nodes, connections, capacities, and hidden dependency;
- legal actions and preconditions;
- flow/routing transitions;
- objective completion and collateral thresholds; and
- an event log with factual before/after state.

No LLM can modify simulator truth or invent a legal action.

## 6. Minimum multi-agent architecture

```text
Validated scenario packet + objective
        |
        v
Planner Agent
proposes one constrained action sequence and states assumptions
        |
        v
Deterministic simulator
executes only legal actions and returns factual outcome/evidence
        |
        v
Safety Challenger Agent
uses the plan, outcome, and evidence to identify unsafe assumptions,
counterexamples, or insufficient observability
        |
        v
Recovery Agent
proposes a revised, safety-constrained action sequence or abstains
        |
        v
Deterministic simulator rerun + validation
        |
        v
Human reviewer
accept | reject | request revision | quarantine
```

### Why multi-agent orchestration is necessary

The agents have conflicting, measurable jobs:

- **Planner:** reach the objective efficiently.
- **Safety Challenger:** find an unsafe consequence, failed assumption, or
  unknown that invalidates confidence in the plan.
- **Recovery Agent:** improve the plan under the safety constraints discovered
  by the Challenger.

The deterministic simulator is the independent referee. It prevents the agents
from awarding themselves success and lets evaluation distinguish a safe plan
from persuasive narration.

Do not add a fourth presentation agent. Use deterministic rendering/templates
for the human-review package.

## 7. Deterministic versus LLM boundary

### Deterministic system owns

- scenario schema, input validation, hashing, and reset;
- world state, legal actions, preconditions, and state transitions;
- action execution and objective/collateral scoring;
- source/provenance checks, JSON schema validation, and human decision state;
- trace correlation IDs and event recording.

### Agents may do

- select among legal actions;
- explain assumptions based on supplied scenario evidence;
- identify a plausible unsafe interaction or missing observation;
- propose a safety-constrained revision; and
- abstain when the packet does not support a safe recommendation.

### Agents must not do

- invent actions, targets, simulator state, or successful outcomes;
- override a simulator result;
- claim a real-world safety guarantee; or
- make the terminal human decision.

## 8. First evaluation suite

Create six original, deterministic test cases:

| Case | Expected result | What it evaluates |
| --- | --- | --- |
| Naive high-throughput plan | objective may progress; collateral failure | Planner-only safety weakness |
| Mitigation-first plan | objective succeeds; no collateral failure | Safe recovery path |
| Hidden dependency not inspected | `insufficient` or explicit risk | Uncertainty handling |
| Illegal action proposal | blocked before simulation | Action-boundary enforcement |
| Challenger catches unsafe plan | challenger flags factual collateral risk | Adversarial handoff value |
| Recovery cannot safely improve | abstention/escalation | No fabricated remedy |

Metrics must be derived from simulator truth:

- objective-success rate;
- collateral-damage rate;
- Safety Challenger catch rate for unsafe plans;
- Recovery success rate after a caught unsafe plan;
- illegal-action rejection rate;
- citation/evidence-reference validity; and
- human override or rejection rate.

Run a Planner-only baseline and the complete Planner → Challenger → Recovery
workflow against the same cases. Only claim improvement after observed results
exist.

## 9. Monitoring and trace evidence

Generate a deterministic `workflow_id` and carry it through every request,
response, simulator event, validation gate, trace, and human review package.

Record:

- scenario ID/version/hash and evaluator version;
- agent, prompt, model/deployment version, and trace ID;
- proposed action sequence and each action-validation outcome;
- simulator event log, objective score, and each collateral metric;
- Challenger finding, evidence references, and confidence/uncertainty;
- Recovery proposal, rerun outcome, duration, token count, and retry count;
- human disposition, edits, and override reason.

The primary review view should be a timeline that makes the causal chain
legible: proposed action → factual simulation event → safety challenge →
recovery action → verified rerun. Do not claim distributed tracing until it is
directly verified.

## 10. Demo narrative

Within three minutes:

1. State the risk: an action-taking AI can optimize the visible goal while
   damaging a hidden dependency.
2. Show the Planner's superficially successful plan.
3. Show the deterministic simulator's collateral evidence.
4. Show the Challenger turning that evidence into a specific safety objection.
5. Show the Recovery plan and the simulator-confirmed safer outcome.
6. Close with the monitoring timeline, evaluation metrics, limitations, and
   human-review boundary.

Do not present planned capability as implemented. Do not claim the simulator
proves real-world safety or generalizes beyond the fictional test cases.

## 11. Source-material and data policy

All source artifacts, scenario state, test cases, labels, actions, diagrams,
and demo assets must be newly authored for this project or have a separately
recorded reuse license. Keep the first slice fully fictional and non-sensitive.

Treat prompts, model traces, screenshots, video, supporting files, source
control, and competition activity pages as disclosure surfaces. Do not submit
confidential, personal, employer-owned, client-owned, proprietary, or otherwise
restricted content.

## 12. Non-goals

- Do not build a real operational digital twin, disaster-response tool, or
  water-management product.
- Do not copy/rebuild Watershed or its D3D12 simulation.
- Do not add real-world control-system integrations, external connectors,
  RAG, customer data, authentication, or production deployment.
- Do not claim that an LLM can validate physical safety.
- Do not make a general multi-agent society or open-ended autonomous loop.

## 13. Suggested repository bootstrap

Create the new repository only after its name, owner, visibility, and license
are deliberately chosen. Start with:

```text
AGENTS.md
README.md
docs/
  PROJECT_BRIEF.md
  ARCHITECTURE.md
  DATA_RIGHTS.md
  EVALUATION_PLAN.md
  HANDOFF.md
data/
  synthetic/
src/
tests/
```

The first committed increment should be model-free: scenario schema, original
scenario fixture, legal-action validator, deterministic simulator, expected
outcomes, and tests. Add Foundry agents only after the simulator can prove the
baseline safe and unsafe paths.

## 14. Settled versus open decisions

### Agreed direction

- This is a separate candidate project and deserves its own handoff.
- Watershed is conceptual inspiration only, not a code/content source.
- The first product is a deterministic intervention-test harness, not a game
  or digital twin.
- The LLM roles are Planner, Safety Challenger, and Recovery Agent.
- A deterministic simulator is the source of truth and evaluation oracle.
- Human review remains the terminal authority.

### Still open

- Whether this becomes the final Agent-a-thon direction rather than the
  Policy-to-Configuration Regression Tribunal.
- New repository name, owner, visibility, and license.
- Exact fictional scenario mechanics, legal action grammar, and success/
  collateral thresholds.
- Whether existing Foundry resources/agents may be reused or whether a new
  project/deployment is needed; do not assume permission, cost, or data terms.
- Exact agent JSON contracts and selected model/deployment.
- Presentation style and any original visual assets.

## 15. Immediate next action

Compare this handoff with `policy-to-configuration-regression-tribunal-handoff.md`
and make one project-direction decision before creating a repository. If this
option wins, define the fictional scenario schema and six expected simulation
outcomes before implementing any agent call.

## 16. Research context and reading list

This is a focused competition prototype in an active agent-safety evaluation
research area. It is not a claim of novel research, a real-world safety
certificate, or a reproduction of any work below. Use the papers to inform
evaluation design and to cite the problem space; do not copy their datasets,
scenarios, prompts, code, figures, or text without separately checking their
license and reuse terms.

### Closest research patterns

- [ToolEmu: Identifying the Risks of LM Agents with an LM-Emulated Sandbox](https://arxiv.org/abs/2309.15817)
  — sandboxed evaluation and automatic safety assessment for tool-using
  language-model agents. Our deliberate difference: the first slice uses a
  small deterministic simulator as the source of truth rather than an
  LLM-emulated environment.
- [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)
  — extensible tasks, adversarial untrusted data, and measurable defenses for
  agents that call tools. Relevant to the scenario’s hostile/irrelevant input
  and the requirement that all scenario content remain data, never instruction.
- [R-Judge: Benchmarking Safety Risk Awareness for LLM Agents](https://aclanthology.org/2024.findings-emnlp.79/)
  — evaluates whether a model can identify safety risks from multi-turn agent
  records. This supports making the Safety Challenger an independently
  evaluated role rather than decorative multi-agent orchestration.

### Practice and evaluation infrastructure

- [UK AI Security Institute: ControlArena](https://control-arena.aisi.org.uk/)
  — controlled evaluation environments with explicit tasks, side effects, and
  measurable outcomes. Useful inspiration for separating objective completion
  from collateral-impact scoring.

### Implications for this project

1. The simulator must emit the authoritative state transition and score; no
   agent may narrate or override it.
2. Score objective completion and collateral effects separately. A plan that
   succeeds on the main objective may still fail the safety evaluation.
3. Keep a planner-only baseline, then test whether Challenger plus Recovery
   measurably improves safe completion and catches unsafe apparent success.
4. Record scenario version/hash, legal-action validation, simulator events,
   model/prompt identifiers, agent outputs, and human disposition for every
   run.
5. Include adversarial and uncertainty cases, but use wholly original,
   fictional fixtures and do not reuse benchmark task content.

### Useful search labels

Use these labels for independent research: **AI agent safety evaluation**,
**LLM agent safety evaluation**, **simulation-based evaluation for tool-using
agents**, **agentic AI assurance**, **sandboxed agent evaluation**,
**behavioral safety of LLM agents**, **adversarial evaluation/red-teaming of
AI agents**, **counterfactual testing for AI agents**, and **multi-agent
critique and recovery**.

The concise label for this project is: **deterministic simulation-based safety
evaluation for tool-using AI agents**.

## 17. Source context

- Watershed inspiration only: <https://github.com/Dorian-Klingenberg/watershed>
- Agent-a-thon winner/criteria transcript captured locally on 2026-09-17:
  `D:\ai-engineering\FrontierWeekTrustedKnowledgeIntake\docs\Agentathon_transcript.md`
