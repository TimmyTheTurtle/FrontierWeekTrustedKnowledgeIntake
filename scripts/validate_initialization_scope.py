"""Validate the file-level scope of the repository-initialization change."""

from __future__ import annotations

import subprocess
import sys
from pathlib import PurePosixPath


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

ALLOWED_PREFIXES = (
    "data/samples/",
    "data/README.md",
    "docs/",
    "evaluations/",
    "src/contextual_knowledge/",
    "tests/",
)


def changed_files(revision: str) -> list[str]:
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
    return path in ALLOWED_FILES or any(path.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def main() -> int:
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
