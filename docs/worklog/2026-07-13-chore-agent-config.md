---
title: "chore: add unified agent configuration files"
date: 2026-07-13
branch: chore/agent-config
request-source: "IDE chat, 2026-07-13"
---

## Request

Set up unified agent configuration for the repository so that all
AGENTS.md-compatible coding agents (Antigravity, Claude Code, etc.) share
a single, canonical source of operating rules.

## Changes

- **`AGENTS.md` (new)**: Created the root-level `AGENTS.md` as the canonical,
  tool-agnostic source of truth for all AI coding agents. Consolidates
  guardrails, project context, repository layout, setup commands, git
  workflow references, worklog requirements, content authoring rules, and
  conventions into one document.
- **`CLAUDE.md` (new)**: Added a one-line pointer (`@AGENTS.md`) so Claude
  Code defers to the shared rules file instead of maintaining a separate
  config.
- **`.agent/rules/general.md` (modified)**: Trimmed the Antigravity-specific
  rules file to reference `AGENTS.md` for shared rules, removing duplicated
  content.
- **`.gitignore` (modified)**: Added `.claude/` to ignore the local-only
  Claude Code settings directory (contains machine-specific permission
  grants).
- **`.github/workflows/pr-checks.yml` (modified)**: Removed `123factory`
  from the `TRUSTED_MAINTAINERS` list, leaving only the active maintainer
  account.

## Verification

- `gitleaks` pre-commit hook passed on all commits (no leaks found).
- Confirmed no secrets or personal data in any changed file.
- Branch contains exactly one worklog file (this file) excluding `_template.md`.
