# Retirement of the initialization gates

The repository-initialization workflow and its companion scope-check script were
retired after the initialization flow completed and issue #1 was closed.

They are intentionally removed from the active workflow set because they were
hard-coded to issue #1 and blocked ordinary pull requests that used GitHub's
normal `Fixes #<number>` closing convention. Their source remains recoverable in
Git history, and the recovered initialization brief and handoff remain attached
to issue #1.

The replacement is the manual, human-reviewed delivery workflow in
`docs/DELIVERY_WORKFLOW.md`; it is not a generalized automation framework.
