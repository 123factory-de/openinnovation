---
title: "docs: unwrap hard-wrapped lines in AGENTS.md and template"
date: 2026-07-14
branch: docs/fix-agents-hard-wrap
request-source: "repo-maintenance, 2026-07-14"
---

## Request

Fix manual line wrapping in `AGENTS.md` and other documentation files (like `docs/worklog/_template.md`) to use soft wrapping, improving readability and editing ease.

## Changes

- Unwrapped all manually broken paragraph lines in `AGENTS.md` into single-line paragraphs.
- Unwrapped manually broken lines in `docs/worklog/_template.md` to use soft wrapping.

## Verification

- Verified the file content formatting.
- Checked `git diff` to confirm that no instructions or rules were altered, only their wrapping/formatting.
