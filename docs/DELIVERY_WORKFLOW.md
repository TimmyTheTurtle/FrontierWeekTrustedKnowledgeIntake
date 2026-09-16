# Delivery workflow

GitHub is the operational system of record for planned and active delivery work.
Repository documents remain the source of truth for product facts, architecture,
and accepted decisions.

## Working records

- A GitHub Issue records one bounded outcome, question, defect, or discovery.
- The **Trusted Knowledge Intake Delivery** GitHub Project prioritizes Issues and
  pull requests. Its Project number is `8` under `TimmyTheTurtle`.
- A pull request is the reviewable implementation artifact. It links to its Issue
  with `Fixes #<number>` only when merging it should close that Issue.
- A decision that changes architecture or scope is captured in the appropriate
  canonical document or ADR after review; a Project field is not a substitute for
  that record.

## Project conventions

Use the built-in Status field as `Todo`, `In Progress`, or `Done`. Use the
custom fields as follows:

- **Work type:** Discovery, Spike, Feature, Technical debt, or Bug.
- **Priority:** P0/Critical through P3/Low; leave it unset until a human has
  deliberately prioritized the work.
- **Product stage:** the stage the work supports.
- **Evidence:** a durable link to the report, test result, ADR, or other evidence
  that justifies the item.
- **Start date** and **Target date:** set only when a human establishes a delivery
  window. They provide date planning without pretending an iteration cadence has
  already been chosen.

Repository labels provide lightweight filtering. In particular,
`type:discovery` means that an Issue gathers evidence and does not itself
authorize implementation.

## Intake and delivery loop

1. Turn a verified observation, decision, or problem into an Issue using the
   relevant template. State the expected outcome, evidence, acceptance criteria,
   non-goals, and dependencies.
2. Add the Issue to the Project. Keep it in `Todo` until a human selects it for
   work. Do not create duplicates when an existing Issue already owns the topic.
3. Before implementation, refine the Issue until its acceptance criteria and
   product-stage boundary are clear. Discovery output remains untrusted design
   evidence until a human accepts a bounded follow-up.
4. Implement on a branch, run the relevant deterministic checks, and open a PR
   that links the Issue. Include the verification evidence and any unresolved
   questions in the PR description.
5. A human reviews the actual diff and evidence. After the review approves the
   change, merge the PR and move the item to `Done`.

This is a manual, review-centered workflow. It intentionally does not add
issue-to-PR orchestration, automatic merging, releases, or agents that change
planning state without human authority.
