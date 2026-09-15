"""Validate the file-level scope of the repository-initialization change.

The GitHub Actions workflow calls this script on a pull request. The script
does not judge whether a document or design is good; it provides a simple,
deterministic first check that changed paths stay inside the initialization
boundary.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import PurePosixPath


# These individual files are explicitly allowed during initialization.
# Keeping the list visible makes the guardrail easy for a beginner to inspect.
ALLOWED_FILES = {
    ".env.example",
    ".gitignore",
    "AGENTS.md",
    "LICENSE",
    "README.md",
    "pyproject.toml",
    ".github/copilot-instructions.md",
    ".github/workflows/validate.yml",
    "scripts/validate_agent_context.py",
}

# These folders contain the documentation, schemas, tests, and small helpers
# that the initialization issue may create.
ALLOWED_PREFIXES = (
    "data/samples/",
    "data/README.md",
    "docs/",
    "evaluations/",
    "src/contextual_knowledge/",
    "tests/",
)


def changed_files(revision: str) -> list[str]:
    """Return paths changed from the supplied Git revision expression."""
    result = subprocess.run(
        ["git", "diff", "--name-only", revision],
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        print(result.stderr.strip(), file=sys.stderr)
        raise SystemExit(result.returncode)
    return [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]


def is_allowed(path: str) -> bool:
    """Return True when a changed path belongs to the initialization scope."""
    return path in ALLOWED_FILES or any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def main() -> int:
    """Print a Markdown report and return a process exit code for GitHub Actions."""
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_initialization_scope.py REVISION", file=sys.stderr)
        return 2

    files = changed_files(sys.argv[1])
    unauthorized = [path for path in files if not is_allowed(path)]

    print("## Initialization scope report")
    print()
    print(f"Changed files: {len(files)}")
    for path in files:
        print(f"- `{path}`")
    print()

    if not files:
        print("Result: **fail** — no changed files were found.")
        return 1

    if unauthorized:
        print("Result: **fail** — these paths are outside the initialization boundary:")
        for path in unauthorized:
            print(f"- `{path}`")
        return 1

    print("Result: **pass** — all changed paths are within the initialization boundary.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# Beginner references:
# - This repository's initialization issue:
#   https://github.com/TimmyTheTurtle/FrontierWeekTrustedKnowledgeIntake/issues/1
# - Canonical repository instructions:
#   https://github.com/TimmyTheTurtle/FrontierWeekTrustedKnowledgeIntake/blob/main/AGENTS.md
# - Project handoff:
#   https://github.com/TimmyTheTurtle/FrontierWeekTrustedKnowledgeIntake/blob/main/docs/history/initial-chat.md
# - Initialization brief:
#   https://github.com/TimmyTheTurtle/FrontierWeekTrustedKnowledgeIntake/blob/main/docs/history/foundry-knowledge-platform-agent-init.md
# - GitHub Actions learning path:
#   https://learn.microsoft.com/training/paths/github-actions/
# - Implement GitHub Actions:
#   https://learn.microsoft.com/training/modules/implement-github-actions/
# - GH-600 study guide:
#   https://learn.microsoft.com/credentials/certifications/resources/study-guides/gh-600
# - Foundations of Agentic AI in GitHub:
#   https://learn.microsoft.com/en-us/training/modules/foundations-agentic-ai/
# - Designing Agent Architecture and SDLC Integration:
#   https://learn.microsoft.com/en-us/training/modules/design-agent-architecture-integration/
# - Tooling, MCP, and Agent Execution Environments:
#   https://learn.microsoft.com/en-us/training/modules/agent-tooling-mcp-execution-environments/
# - GitHub Copilot agent mode:
#   https://learn.microsoft.com/training/modules/github-copilot-agent-mode/
# - GitHub Script in Actions:
#   https://learn.microsoft.com/training/modules/automate-github-using-github-script/
