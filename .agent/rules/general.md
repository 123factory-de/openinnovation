# Antigravity Agent Instructions

This file provides specific context and operational rules for the Antigravity AI assistant.

## Core Directives
- **Source of Truth**: Always refer to the following documents for workflow rules:
    - [branching-strategy.md](docs/git-workflow/branching-strategy.md)
    - [commit-convention.md](docs/git-workflow/commit-convention.md)
    - [pr-convention.md](docs/git-workflow/pr-convention.md)
- **Branching**: Follow GitHub Flow. Use `feat/`, `fix/`, `docs/`, etc. Never commit to `main`.
- **Commits**: Use Conventional Commits as defined in [commit-convention.md](docs/git-workflow/commit-convention.md).
- **Pull Requests**: Follow the template and standards defined in [pr-convention.md](docs/git-workflow/pr-convention.md).

- **Language**: All communication, documentation, and code comments must be in **English**.

## Project Mission
- **Project**: `open-innovation-directory`
- **Objective**: Build and maintain an open innovation program and resources collection/aggregator website.


## Security & Data Protection (MANDATORY)
- **Never commit secrets or personal data.** This includes API keys, tokens, passwords, credentials, and PII such as email addresses, phone numbers, and resident registration numbers — in file contents, file names, and commit messages alike.
- **One-time setup per clone**: run `git config core.hooksPath .githooks` so the pre-commit secret scan is active. `gitleaks` must be installed (`brew install gitleaks` on macOS).
- **Before every commit**, the pre-commit hook runs gitleaks against `.gitleaks.toml`. If it fails, remove the flagged data — do not bypass with `--no-verify`, do not edit the scanning config.
- **Protected paths — never modify**: `.github/`, `.gitleaks.toml`, `.githooks/`, `.agent/`, `.gitmodules`. CI rejects agent PRs touching these. If a change there seems necessary, describe it in the PR body and let a human maintainer make it.
- **Publishing a contact address**: if a program page genuinely needs a public contact email, do not add it directly. Open the PR without it and note the address in the PR description; a human will review and extend the allowlist in `.gitleaks.toml` if appropriate.

## Operational Preferences
- Be concise and technical.
- Proactively suggest best practices for Agentic systems.
