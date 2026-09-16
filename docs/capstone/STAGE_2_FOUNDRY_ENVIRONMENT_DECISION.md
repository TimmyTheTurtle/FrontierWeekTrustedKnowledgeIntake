# Stage 2: Foundry environment decision and approval gate

**Founderz lesson:** [Agent Architect - Set up your Foundry environment](https://learn.founderz.com/lesson/agent-architect-set-up-your-foundry-environment/356bb23b-0d31-48c3-b4e0-c35142d02f5f)
**Issue:** #20
**Status:** human-approved environment plan; no model deployment, agent, or connector has been created by this work

## Lesson-aligned boundary

The repository is the code workspace for deterministic intake, tests, and
reviewable documentation. Microsoft Foundry is a later environment for the
agent runtime, observability, and evaluation. These surfaces have distinct
credentials, costs, data-handling requirements, and verification evidence.

## Resolved Stage 2 decisions

| Decision | Agreed value | Verification/status |
| --- | --- | --- |
| Subscription | Pay-As-You-Go (`d73a2af6-1ff7-42c1-91e7-a6bcc3d6f930`) | Verified read-only through Azure CLI and Resource Graph. |
| Resource group | `rg-trusted-knowledge-intake-capstone-eus2` | Created by the human reviewer; verified read-only through Resource Graph. |
| Foundry account | `trusted-knowledge-intake-capstone-resource` | Verified read-only through Resource Graph. |
| Foundry project | `trusted-knowledge-intake-capstone` | Reachable through Foundry MCP; no agents exist. |
| Region | `eastus2` | Verified read-only through Resource Graph. |
| Baseline model deployment | `capstone-gpt-5-mini`: `gpt-5-mini`, version `2025-08-07`, Global Standard pay-as-you-go, 1K TPM | Created by the human reviewer; Foundry MCP verified `Succeeded`. The default `Microsoft.DefaultV2` RAI policy applies. The previously proposed `gpt-4o-mini` version `2024-07-18` was rejected by the portal as deprecating. |
| Budget boundary | CA$10 monthly resource-group budget, with actual-cost alerts at 50%, 80%, and 100% | Verified through Azure CLI. Alerts send to the human reviewer's email. A budget is an alert threshold, not a guaranteed hard spend stop. |
| Temporary notification exception | The existing Claims action group remains attached to the capstone budget alerts until the human reviewer deletes the separate Claims resource group. | Intentional human decision; do not modify either resource as part of this capstone. |
| Data boundary | Synthetic or openly redistributable Markdown/plain text only; no private content or secrets. | Approved. |
| Access boundary | Human reviewer identity only; no service principals, external connectors, or shared access. | Approved. |
| Evidence boundary | Preserve safe configuration screenshots, deployment details, test inputs, trace IDs, and evaluation outputs. | Approved. |

## Current decision

For Issue #20, adopt a **local-first, Foundry-deferred** environment posture:

- Keep the existing deterministic Markdown intake implementation local and
  dependency-free.
- The human reviewer created a dedicated Foundry account and project for this
  capstone; it is distinct from other projects and learning exercises.
- Do not create, modify, or use a model deployment, agent, external connector,
  or other billable service until the human reviewer performs the portal action
  and asks for verification.
- Treat the Stage 3 architecture as a design artifact until a model deployment
  and a thin workflow are verified. Do not describe either as implemented yet.

This is a deliberate environment decision, not a setup failure. It preserves
the capstone's verified local evidence while preventing accidental cost, data,
or scope expansion.

## Explicit approval gate for any Foundry use

Before any model deployment, agent, connector, or other billable Foundry
capability is created or used, the human reviewer must approve all of the
following in writing:

| Required decision | What must be specified |
| --- | --- |
| Project and subscription | Exact Foundry project and Azure subscription; whether it is new or existing. |
| Region | Intended Azure region and the reason it meets data/residency needs. |
| Model and deployment | Exact model/version, SKU or capacity, deployment name, and whether use is billable. |
| Cost control | Expected cost, maximum spend or duration, and stop/cleanup owner. |
| Data handling | Permitted source data, classification, retention, telemetry redaction, and prohibited data. |
| Identity and access | Intended user/service identity, minimum roles, and any tool/connector access. |
| Evidence plan | The trace, evaluation, screenshots, and configuration facts that will be captured without exposing secrets. |

No approval is inferred from account access, a prior lab, a course lesson, or a
general request to work on the capstone. If any field changes, the gate must be
reviewed again before use.

## What may proceed without this approval

- Deterministic parser increments and local unit tests.
- Foundry-compatible architecture, schemas, tool contracts, and evaluation
  design that do not call external services.
- Synthetic and clearly redistributable test fixtures.
- Documentation that clearly labels plans versus verified implementation.

## Evidence required after approval, before claiming an environment works

1. Read-only confirmation of the selected tenant/subscription and project.
2. Visible confirmation of the exact project, region, model/deployment, and
   applicable cost controls.
3. A minimal non-sensitive run with correlation identifiers and its resulting
   trace or structured execution evidence.
4. A separately documented evaluation run with observed results.

## Stage 2 review checklist

- [x] Human reviewer accepts the dedicated-capstone environment and the local-first implementation posture.
- [x] The budget, data, access, and evidence boundaries are approved.
- [x] The human reviewer created the CA$10 resource-group budget and confirmed actual-cost alert thresholds of 50%, 80%, and 100%.
- [x] The human reviewer accepts no forecast alert for this capstone and temporarily retains the Claims action group until its separate resource group is deleted.
- [ ] Stage 2 is checked in Issue #20 only after the human confirms the recorded decisions and budget configuration. This advances one course stage; it does not close Issue #20.
