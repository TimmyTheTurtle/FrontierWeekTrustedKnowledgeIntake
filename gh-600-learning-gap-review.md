# GH-600 learning-gap review

Status: separate working review; not part of the canonical Agent-a-Thon learning-links record.

Reviewed: September 14, 2026

## Purpose

This document identifies Microsoft Learn material that appears relevant to the GH-600 direction and to the GitHub issue/workflow experiment in this repository.

Keep this file separate from `foundry-agentathon-learning-links.md`. It is intentionally removable. Do not copy its recommendations into the main learning-links record until completion status has been confirmed against the Microsoft Learn profile.

## Current-file comparison

The current learning-links record marks these GitHub items as content completed but assessment still due:

- Introduction to GitHub's Products
- Introduction to GitHub Copilot

It does not currently record the following GH-600 or GitHub Actions material. “Not recorded” does not prove that a module is incomplete; verify each item against the Microsoft Learn transcript before marking it complete.

## Highest-priority recommendations

### 1. Foundations of Agentic AI in GitHub

Official module: <https://learn.microsoft.com/en-us/training/modules/foundations-agentic-ai/>

Why it matters here:

- explains the plan -> act -> evaluate lifecycle;
- treats GitHub as the system of record and control plane;
- covers responsibilities, risks, anti-patterns, and traceability;
- gives the conceptual model for using an issue as durable agent state.

This is the best first GH-600 module for understanding why the issue-driven approach works.

### 2. Designing Agent Architecture and SDLC Integration

Official module: <https://learn.microsoft.com/en-us/training/modules/design-agent-architecture-integration/>

Why it matters here:

- separates planning, reasoning, and execution;
- defines inputs, outputs, and success criteria;
- covers pull-request governance, checks, rules, and environments;
- explains triggers, contexts, outputs, and cross-job handoffs;
- addresses observability, tool governance, secrets, and reliability.

This is the closest match to the guardrail concern that led us to replace a one-shot initialization prompt with staged approvals.

### 3. Automate your workflow with GitHub Actions — Part 1 of 2

Official learning path: <https://learn.microsoft.com/training/paths/github-actions/>

The most relevant modules for this repository are:

- [Automate development tasks by using GitHub Actions](https://learn.microsoft.com/training/modules/github-actions-automate-tasks/) — workflow components, triggers, and a basic action;
- [Build continuous integration workflows by using GitHub Actions](https://learn.microsoft.com/training/modules/github-actions-ci/) — workflow checks, logs, debugging, and customization;
- [Automate GitHub by using GitHub Script](https://learn.microsoft.com/training/modules/automate-github-using-github-script/) — issue comments through Octokit and expression-based job filtering.

The GitHub Script module is especially relevant because our workflow uses `actions/github-script` to post and update checkpoint comments.

Do not prioritize the Azure deployment module in Part 1 for this experiment; Azure deployment is intentionally outside the current initialization scope.

### 4. Tooling, MCP, and Agent Execution Environments

Official module: <https://learn.microsoft.com/en-us/training/modules/agent-tooling-mcp-execution-environments/>

Why it matters here:

- explains how agents interact with GitHub APIs and workflows;
- covers MCP servers, registries, and allow lists;
- defines repository, branch, and workflow execution boundaries;
- covers protections such as pull-request review and environment safeguards;
- includes an exercise using GitHub Agentic Workflows.

This is the module to study after the basic Actions model is comfortable.

### 5. Building applications with GitHub Copilot agent mode

Official module: <https://learn.microsoft.com/training/modules/github-copilot-agent-mode/>

Why it matters here:

- explains how to prompt an autonomous coding agent;
- uses documentation files to guide agent behavior;
- shows how agent mode iterates over a codebase.

This covers the agent side of the experiment. The Actions modules cover the workflow side.

## Useful foundation if the mechanics still feel unfamiliar

### Implement GitHub Actions

Official module: <https://learn.microsoft.com/training/modules/implement-github-actions/>

Use this before or alongside the Actions path if triggers, jobs, steps, variables, contexts, expressions, or workflow execution are still unclear. Its exercise creates a workflow that validates code on a pull request, which is close to the validation half of our initialization workflow.

### Manage repository changes by using pull requests on GitHub

Official module: <https://learn.microsoft.com/training/modules/manage-changes-pull-requests-github/>

Use this if the branch -> pull request -> review -> merge lifecycle needs reinforcement. It is foundational rather than specifically GH-600, but the issue workflow eventually hands work into that lifecycle.

## Recommended study order for this experiment

1. Finish or confirm the assessment for Introduction to GitHub Copilot, already listed in the main learning-links file.
2. Complete [Automate development tasks by using GitHub Actions](https://learn.microsoft.com/training/modules/github-actions-automate-tasks/).
3. Complete [Implement GitHub Actions](https://learn.microsoft.com/training/modules/implement-github-actions/) if workflow syntax, contexts, or permissions remain unclear.
4. Complete [Automate GitHub by using GitHub Script](https://learn.microsoft.com/training/modules/automate-github-using-github-script/).
5. Study [Foundations of Agentic AI in GitHub](https://learn.microsoft.com/en-us/training/modules/foundations-agentic-ai/).
6. Study [Designing Agent Architecture and SDLC Integration](https://learn.microsoft.com/en-us/training/modules/design-agent-architecture-integration/).
7. Study [Building applications with GitHub Copilot agent mode](https://learn.microsoft.com/training/modules/github-copilot-agent-mode/).
8. Study [Tooling, MCP, and Agent Execution Environments](https://learn.microsoft.com/en-us/training/modules/agent-tooling-mcp-execution-environments/).

This order builds the workflow foundation before asking GH-600 material to make architectural sense.

## Lower priority for the current experiment

- [Automate your workflow with GitHub Actions Part 2 of 2](https://learn.microsoft.com/training/paths/github-actions-2/) — custom actions, GitHub Packages, and enterprise administration; useful later, not needed for issue #1.
- [Using advanced GitHub Copilot features](https://learn.microsoft.com/training/modules/advanced-github-copilot/) — useful for local Copilot fluency, but less directly connected to the issue/workflow control loop.
- GitHub Actions deployment modules — defer until Azure deployment is deliberately in scope.

## GH-600 alignment

The official GH-600 study guide names three self-paced resources directly:

- [Foundations of Agentic AI in GitHub](https://learn.microsoft.com/en-us/training/modules/foundations-agentic-ai/);
- [Designing Agent Architecture and SDLC Integration](https://learn.microsoft.com/en-us/training/modules/design-agent-architecture-integration/);
- [Tooling, MCP, and Agent Execution Environments](https://learn.microsoft.com/en-us/training/modules/agent-tooling-mcp-execution-environments/).

The study guide also explicitly measures planning/execution boundaries, validated plans, human intervention, agent tools, GitHub workflow invocation, durable state, traceability, and guardrails. Those are the concepts this issue experiment is making concrete.

## Verification note

The recommendations above were checked against the official Microsoft Learn pages and the GH-600 study guide on the review date. Completion status remains a personal-profile fact and should be updated only after checking the Microsoft Learn transcript.
