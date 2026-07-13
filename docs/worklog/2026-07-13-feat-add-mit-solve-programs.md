---
title: feat(programs): add MIT Solve pages
date: 2026-07-13
branch: feat/add-mit-solve-programs
request-source: "Slack, 2026-07-13"
---

## Request

Add the newly verified MIT Solve program pages, mark the Verizon Disaster Resilience Prize 2025 entry as closed, and keep closed programs hidden from the home page while still showing them in the catalog list.

## Changes

- Added Hugo bundles for three verified MIT Solve programs:
  - Amazon Sustainability Pilot Program
  - Verizon Disaster Resilience Prize 2025
  - Truist Foundation Inspire Awards Year 4
- Updated the Verizon entry from `Active` to `Closed` after user confirmation that the challenge has ended.
- Changed the home-page program selection so entries with `status: Closed` or `status: 종료` are excluded from the featured home cards.
- Kept the catalog list visible for closed entries, since the user wanted closed items to remain discoverable there.
- Chose a conventional-commit-style PR title so the branch metadata matches the repository's PR convention.

## Verification

- Confirmed the three program slugs were not already present under `content/programs/` before adding them.
- Verified the newly added Markdown front matter parses cleanly with a local Python check.
- Confirmed the repo's home template now excludes closed programs, while the list template still includes them.
- Verified the current branch is clean after commit and push.
