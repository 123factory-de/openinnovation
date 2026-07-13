---
title: fix(programs): normalize industry values
date: 2026-07-13
branch: feat/add-mit-solve-programs
request-source: "Slack, 2026-07-13"
---

## Request

Normalize the `industry` field for the newly added MIT Solve program pages so it follows the repository's PitchBook taxonomy rules instead of translated Korean labels.

## Changes

- Kept `industry` values in English PitchBook primary sector form on the Korean pages.
- Corrected the Verizon and Truist Korean pages to use `Public Safety` and `Social Impact` respectively.
- Confirmed that no other `index.ko.md` files in `content/programs/` contain out-of-taxonomy `industry` values.
- Updated the open-innovation skill to explicitly note that `industry` must use the repository's English PitchBook taxonomy in both English and Korean markdown files.

## Verification

- Searched all `index.ko.md` program pages for `industry` values and found no remaining taxonomy violations.
- Read the PitchBook taxonomy references under `docs/references/` to confirm the correct controlled vocabulary.
- Verified the affected Korean pages now use the expected English sector values.
