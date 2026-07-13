---
title: "fix(programs): align IT industry taxonomy and update deadline logic"
date: 2026-07-13
branch: docs/fix-pitchbook-verticals
request-source: "direct-user-request, 2026-07-13"
---

## Request

- Correct PitchBook industry verticals reference and align all program content frontmatter accordingly.
- Refactor the deadline and status display logic to prioritize deadlines.
- Set up a dynamic client-side mechanism to update and display the program closed status.

## Changes

- Renamed primary industry `"Information Technology"` to `"Information Technology (IT)"` in [pitchbook-industry-verticals.md](file:///Users/123f/Workspaces/Github/openinnovation/docs/references/pitchbook-industry-verticals.md) and all program markdown files.
- Refactored [single.html](file:///Users/123f/Workspaces/Github/openinnovation/layouts/programs/single.html) and [list.html](file:///Users/123f/Workspaces/Github/openinnovation/layouts/programs/list.html) templates to prioritize the `deadline` field over `status`.
- Created [deadline-refresh.html](file:///Users/123f/Workspaces/Github/openinnovation/layouts/partials/programs/deadline-refresh.html) partial to dynamically compute and update program open/closed status badge on the client side.
- Added translation values in [en.toml](file:///Users/123f/Workspaces/Github/openinnovation/i18n/en.toml) and [ko.toml](file:///Users/123f/Workspaces/Github/openinnovation/i18n/ko.toml) for "closed" and "official_site".
- Created program taxonomy checker script [check_programs.py](file:///Users/123f/Workspaces/Github/openinnovation/scripts/check_programs.py).

## Verification

- Verified pages and status transitions locally by running the Hugo server.
- Validated layout behaviors for dynamic client-side updates.
- Passed local git commit pre-commit hooks (including Gitleaks secret scanning).
