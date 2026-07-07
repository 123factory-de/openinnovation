---
title: "docs: add worklog convention for agent PRs"
date: 2026-07-07
branch: docs/add-worklog-convention
request-source: "repo-maintenance, 2026-07-07"
---

## Request

Keep a permanent, in-repository record of each PR's title and description.
Rather than copying PR metadata into the repo after the fact (which
duplicates what GitHub already stores and drifts when the PR is edited),
adopt the inverse: a worklog file committed with each change is the source
of truth, and the PR title/description are generated from it.

## Changes

- Added `docs/worklog/_template.md` defining the worklog format: a
  frontmatter `title` (becomes the PR title) plus Request / Changes /
  Verification sections (become the PR description).
- Added a mandatory "Worklog" section to `.agent/rules/general.md`:
  every PR must include one worklog file named
  `docs/worklog/YYYY-MM-DD-<branch-slug>.md`, created before the PR is
  opened; scope changes update the file first, then the PR description.
- Worklog files fall under the existing Security & Data Protection rules
  and are scanned by gitleaks; requesters are referenced by channel and
  date, never by name or handle.
- This file is the first worklog, serving as a filled-in example of the
  convention it introduces.

## Verification

- gitleaks pre-commit hook passed on this branch.
- `docs/` is outside Hugo's `content/`, so nothing is rendered to the
  public site; confirmed no layout references `docs/`.
