# Stage 4: monitoring and trace evidence

**Founderz lesson:** [Agent Architect - Monitor and trace agent behavior](https://learn.founderz.com/lesson/agent-architect-monitor-and-trace-agent-behavior/1c92f4fe-496b-4e18-b21b-1a3ee91ffc2c)
**Issue:** #20
**Status:** real server-side traces verified for both prompt agents; manual correlation only

## Observability configuration

| Element | Verified configuration |
| --- | --- |
| Foundry project | `trusted-knowledge-intake-capstone` |
| Application Insights | `trusted-knowledge-intake-capstone-appinsights-4955` |
| Project connection | App Insights connection `trusted-knowledge-intake-capstone-appinsights-4955` |
| Connection type | ApiKey, created through the Foundry tracing connection flow |
| Trace scope | Server-side Foundry tracing for prompt agents |
| Data-handling boundary | Synthetic, non-sensitive prompts only; traces can capture instructions, inputs, and outputs |

Foundry automatically enables server-side tracing after the Application Insights
connection is created. No client-side code instrumentation was added.

## Verified execution evidence

| Agent | Version | Result | Spans / model calls | Duration | Tokens |
| --- | --- | --- | --- | --- | --- |
| Intake Analyst | `intake-analyst:4` | succeeded | 2 spans / 1 chat call | 13.2 seconds | approximately 1.5K |
| Knowledge Steward | `knowledge-steward:5` | succeeded | 2 spans / 1 chat call | 8.8 seconds | approximately 1.9K |

The Foundry Traces UI visibly showed the agent version, successful status, span
tree, duration, token activity, and captured agent instructions for both runs.

## Manual correlation boundary

The Stage 4 test used a synthetic source marker,
`source_stage4_trace_001`, and passed the Analyst proposal to the Steward
with a manual handoff marker, `stage4-handoff-001`.

This is **manual correlation evidence**, not a distributed-trace claim. The
current prompt-agent calls are separate Foundry invocations and do not share an
automatically propagated trace ID. A later deterministic orchestrator can
propagate a stable correlation ID across agent calls and record it in the
review package.

## Observed behavior

- The Intake Analyst returned a source-cited candidate proposal and preserved
  uncertainty for the untrusted source.
- The Knowledge Steward returned `review`, counted supported eligible claims,
  reported risks and uncertainties, and retained the human terminal decision.
- Earlier synthetic prompt-injection tests showed the Analyst excluding an
  embedded directive from candidate claims and the Steward flagging it as an
  integrity risk.

## Query limitation

The project connection exists, but authenticated Azure management and
Application Insights queries from this local environment are forcibly reset
before Azure returns a response. The failure was reproduced with Azure CLI,
PowerShell, and curl. Unauthenticated HTTPS connectivity to
`management.azure.com` succeeds, so this is treated as a local/network
authenticated-transport limitation rather than absent trace data.

The Foundry Traces UI remains the verified evidence source for this stage. No
KQL result, trace query, or automated trace correlation is claimed.

## Stage 4 review checklist

- [x] A dedicated Application Insights resource is connected to the capstone Foundry project.
- [x] Server-side Intake Analyst trace is visibly verified.
- [x] Server-side Knowledge Steward trace is visibly verified.
- [x] Manual source/handoff markers establish reviewable paired execution evidence.
- [x] Trace privacy boundary and local query limitation are documented.
- [ ] Human reviewer approves this Stage 4 evidence and checks Stage 4 in Issue #20.
