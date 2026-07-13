---
title: fix(programs): normalize taxonomy values
date: 2026-07-13
branch: feat/add-mit-solve-programs
request-source: "Slack, 2026-07-13"
---

## Request

Normalize the recently added MIT Solve program metadata so it follows the repository's PitchBook taxonomy rules for both `industry` and `verticals`.

## Changes

- Kept `industry` values in English PitchBook primary sector form on the Korean pages.
- Corrected the Amazon page to use `Consumer Products and Services` with valid verticals (`Cleantech`, `Climate Tech`).
- Corrected the Verizon page to use `Information Technology` with a valid vertical (`Infrastructure`).
- Corrected the Truist page to use `Financial Services` with a valid vertical (`Impact Investing`).
- Confirmed that the newly added MIT Solve pages no longer contain out-of-taxonomy `industry` or `verticals` values.

## Verification

- Read the PitchBook taxonomy references under `docs/references/` to confirm the controlled vocabulary.
- Re-checked the affected program pages after editing to ensure the new values are valid taxonomy entries.
