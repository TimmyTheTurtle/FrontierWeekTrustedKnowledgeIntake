# Firebreak Decision Lab — Project Handoff

**Status:** concept handoff; no implementation or repository has been created.  
**Created:** 2026-09-17  
**Intended use:** a possible new, user-selected repository for the Microsoft
Agent-a-thon Level 3: Architect competition.

## 1. Product in one sentence

Build a fictional, deterministic wildfire-containment simulation that tests an
agent's proposed actions for unintended consequences, then uses trace-informed,
evaluation-gated improvement under an explicit human promotion gate.

This is a decision-assurance demonstration, **not** a real emergency-response
system, dispatch tool, or public-safety recommendation engine.

## 2. Why this theme

The wildfire metaphor is legible in a short demo: fire spread, wind direction,
fuel, protected assets, limited crews, and constrained actions make both a good
plan and a dangerous shortcut easy to see. It also preserves *Watershed* as its
own future puzzle-game project.

This project may borrow only the broad inspiration of a constrained simulation
with visible consequences. It must not copy Watershed code, scenarios, names,
mechanics, assets, prompts, screenshots, fixture text, or narrative framing.

## 3. Core review question

> Given a fictional scenario, can an agent's proposed containment plan meet
> its stated objective without breaching protected-zone or crew-safety
> constraints?

The deterministic simulator is the authority on outcomes. Agents may interpret
evidence and propose actions, but cannot create actions, change rules, or claim
an outcome that the simulator did not produce.

## 4. Bounded first vertical slice

Create one original toy grid with:

- a fire origin, fuel map, and fixed wind state;
- a small number of protected zones and limited response resources;
- an explicit objective, such as prevent fire from reaching one protected zone
  within a fixed number of turns;
- a finite action grammar: `BUILD_FIREBREAK`, `PROTECT_ASSET`,
  `REPOSITION_CREW`, `MONITOR`, `PASS`, and `ESCALATE`;
- deterministic spread and deterministic action preconditions; and
- a factual event log containing state before/after each action.

Use fictional places, synthetic scenario records, and deliberately invented
parameters. Do not make claims about real fire behavior, operational doctrine,
or emergency-management effectiveness.

## 5. The safety smells to detect

The challenger is not looking for generic bad writing. It looks for specific,
testable planning failures:

- **Asset tunnel vision:** protects the most visible asset while another
  protected zone becomes exposed.
- **Wind-shift fragility:** a plan succeeds only under an unexamined wind
  assumption.
- **Resource starvation:** commits scarce crews or actions early and leaves no
  viable recovery path.
- **Local-success / global-harm:** slows spread near the origin while violating
  a protected-zone or crew-safety constraint elsewhere.
- **Unjustified certainty:** recommends a high-impact action when simulator
  evidence is insufficient; the correct action is `MONITOR` or `ESCALATE`.

## 6. Minimum multi-agent workflow

```text
Validated fictional scenario
        |
        v
Planner Agent ── constrained action proposal + stated assumptions
        |
        v
Deterministic Simulator ── legal execution + factual trace + outcome metrics
        |
        v
Safety Challenger ── identifies smell, counterexample, or uncertainty
        |
        v
Recovery Agent ── revised legal plan, abstention, or escalation
        |
        v
Deterministic Simulator ── comparative replay
        |
        v
Human Control Gate ── approve, reject, or request a revision
```

The orchestrator passes structured packets between roles and records every
handoff. It rejects invalid action names, missing evidence references, and
attempts to override the simulator.

## 7. Human control gate

This is the project’s key trust boundary. The system can observe traces,
diagnose recurring failure patterns, and propose an improvement. It cannot
silently change its own behavior or redefine success.

Only a human may:

- approve or reject a proposed policy, prompt, threshold, or routing change;
- promote a newly discovered failure scenario into the regression suite; and
- promote a candidate agent version after it passes evaluation.

Every decision includes the candidate version, linked trace/evaluation evidence,
human disposition, and rationale.

## 8. Trace-informed, evaluation-gated improvement

Use the phrase **trace-informed, evaluation-gated improvement**, not continual
learning or autonomous self-training.

```text
simulation run
  -> immutable trace and deterministic outcome labels
  -> failure-pattern analysis
  -> bounded candidate improvement
  -> fixed regression suite + held-out scenarios
  -> human promotion decision
  -> versioned candidate, if approved
```

Candidate improvements may change a planner instruction, a confidence threshold,
or an orchestration route. They must not alter simulator truth, overwrite prior
traces, or enter production/demo behavior before human approval.

## 9. Monitoring and evaluation

Record at least:

- objective success rate;
- protected-zone breach rate;
- resource/crew constraint violation rate;
- challenger catch rate on seeded unsafe plans;
- recovery improvement rate versus the initial plan;
- abstention/escalation appropriateness on ambiguous scenarios;
- invalid-action rejection rate; and
- human approval, rejection, and override counts.

Build a small, wholly original evaluation set before the demo: clear safe plan,
asset-tunnel-vision failure, wind-shift failure, resource-starvation failure,
and a deliberately ambiguous escalation case. Keep one or more scenarios
held out from tuning to demonstrate that a candidate improvement did not merely
memorize the visible cases.

## 10. Data and intellectual-property boundary

- Use only original synthetic scenario data, code, visual assets, and prompts.
- Never use real incident reports, agency maps, private dispatch data,
  proprietary wildfire models, or personal information.
- Do not imply validation for real-world fire response.
- Treat every competition artefact—video, trace, screenshot, prompt, supporting
  document, and shared activity page—as a disclosure surface.

## 11. A three-minute demonstration arc

1. Show a compact fictional map and the objective/constraints.
2. The Planner proposes an apparently sensible plan.
3. Deterministic replay exposes a protected-zone breach after a wind change.
4. The Challenger cites the evidence; Recovery produces a revised plan or
   escalates.
5. Replay shows the comparison and the metrics.
6. Show a trace-derived candidate improvement being evaluated, then stopped at
   the Human Control Gate for approval.

The visual center is the evidence loop, not a claim of autonomous crisis
management.

## 12. Recommended first implementation order

1. Write the action schema, simulator rules, fixtures, and deterministic tests.
2. Add trace records and a replay view.
3. Add Planner, Challenger, and Recovery roles through Foundry orchestration.
4. Add fixed evaluations, metrics, and the human-promotion record.
5. Prepare the short demo using synthetic scenarios only.

## 13. Open decisions before a new repository is started

- Confirm this theme instead of the neutral Intervention Wind Tunnel.
- Select the actual Foundry project/model and decide whether a narrowly scoped
  optional structured-decision service is worth the dependency.
- Define the exact human approval interface: JSON record first, then minimal UI
  only if time permits.
- Recheck the competition’s final rules and submission requirements immediately
  before any external upload or submission.
