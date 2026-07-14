# AGENTS.md

Operating instructions for AI coding agents (Antigravity, Claude Code, and any other AGENTS.md-compatible agent) working in this repository. This is the canonical, tool-agnostic source of truth. Tool-specific files (`CLAUDE.md`, `.agent/rules/general.md`) defer to this document.

**Read this file fully before making any change.**

---

## 🚦 Guardrails — non-negotiable

These rules are hard limits. If a task appears to require breaking one, **stop and ask a human** instead of proceeding.

1. **Never commit to `main`.** Always work on a branch and open a Pull Request. `main` is protected and deploys to production on merge.
2. **Never commit secrets or personal data.** No API keys, tokens, credentials, Korean resident registration numbers (주민등록번호), personal phone numbers, or private email addresses — in file contents, file names, and commit messages alike. Commits are scanned by gitleaks locally (`.githooks/pre-commit`) and in CI (`.github/workflows/pr-checks.yml`). Do not disable, bypass (`--no-verify`), or edit these scans.
3. **Never modify protected paths.** The following may only be changed by a trusted human maintainer via a reviewed PR — an agent must not touch them:
   - `.github/` (CI workflows)
   - `.gitleaks.toml` (secret/PII scan rules)
   - `.githooks/` (git hooks)
   - `.agent/` (agent rules)
   - `.gitmodules` (submodule config)

   CI enforces this (`protected-paths` job); a PR from a non-maintainer that touches these paths will fail. If a change there seems necessary, describe it in the PR body and let a human maintainer make it.
4. **Never edit generated or vendored files.** Do not hand-edit `public/`, `resources/`, or the `themes/blowfish/` submodule.
5. **Keep changes atomic and in scope.** One task per branch/PR. If you discover unrelated work, note it — do not bundle it in.
6. **When uncertain about a destructive or irreversible action, ask.** Deleting content, force operations, history rewrites, and dependency changes warrant a human check.

---

## Project

- **Name**: `open-innovation-directory`
- **Owner**: 123 Factory
- **Objective**: Build and maintain a curated directory and aggregator for open innovation programs, challenges, and resources.
- **Live site**: https://openinnovation.123factory.de/
- **Stack**: [Hugo](https://gohugo.io/) (extended) static site generator with the [Blowfish](https://github.com/nunocoracao/blowfish) theme (git submodule at `themes/blowfish`).
- **Languages**: Bilingual site — English (default) and Korean (`ko`).

## Repository layout

| Path | Purpose |
| :--- | :--- |
| `config/_default/` | Hugo configuration (`hugo.toml`, `params.toml`, `menus.*.toml`, `languages.*.toml`, `markup.toml`, `module.toml`) |
| `content/programs/` | Program pages — one folder per program with `index.md` / `index.ko.md` and a `feature.*` image |
| `layouts/` | Custom Hugo templates overriding the theme |
| `assets/`, `static/` | Site assets and static files |
| `data/` | Hugo data files |
| `i18n/` | Translation strings |
| `themes/blowfish/` | Theme (git submodule — do not edit) |
| `scripts/` | Repo tooling (`check_programs.py` — program frontmatter linter, run in CI) |
| `docs/` | Git workflow, reference taxonomies, and PR worklogs |
| `open-innovations/` | Research workspace — collection reports, source references, worklogs, and reusable skills |
| `.githooks/`, `.gitleaks.toml`, `.github/`, `.agent/` | Safety guardrails and agent rules (protected — see above) |
| `public/`, `resources/` | Generated output — do not edit |

## Setup & common commands

Requires Hugo **extended** (developed against `v0.153.x`), Python 3 (for the frontmatter linter), and `gitleaks` (for the commit hook).

```bash
git submodule update --init --recursive   # fetch the Blowfish theme
git config core.hooksPath .githooks       # enable the local secret-scan hook (once per clone)
brew install gitleaks                     # macOS; other platforms: gitleaks.io

hugo server -D                            # local dev server with drafts at http://localhost:1313
hugo --gc --minify                        # production build into ./public
python3 scripts/check_programs.py         # lint program frontmatter (matches the CI check)
```

Deployment is automated via GitHub Actions (`.github/workflows/hugo.yml`) on push to `main`. Do not commit changes to the generated `public/` directory as part of feature work.

## Git workflow — source of truth

Follow these documents exactly. They are authoritative:

- [docs/git-workflow/branching-strategy.md](docs/git-workflow/branching-strategy.md)
- [docs/git-workflow/commit-convention.md](docs/git-workflow/commit-convention.md)
- [docs/git-workflow/pr-convention.md](docs/git-workflow/pr-convention.md)

Key rules:

- **GitHub Flow.** Branch from `main` using prefixes: `feat/`, `fix/`, `docs/`, `refactor/`, `test/`, `chore/`.
- **Conventional Commits.** Format `<type>[scope]: <description>`; imperative mood; subject ≤ 50 chars; no trailing period.
- **Pull Requests** follow the template and process in the PR convention doc; keep PRs atomic. All PR checks (program frontmatter lint, secret scan, protected paths) must pass before merge.
- Delete feature branches after merge.

## Worklog — mandatory for every PR

- Every PR must include exactly one branch-specific worklog file named `docs/worklog/YYYY-MM-DD-<branch-slug>.md` (this count excludes [docs/worklog/_template.md](docs/worklog/_template.md)).
- Create the worklog on the same branch as the change and commit it **before opening the PR**.
- **The worklog file is the source of truth for the PR**: PR title = the worklog `title` field; PR description = the worklog body (from `## Request` down). Generate the PR from the file, never the other way around. If scope changes during review, update the worklog first, then sync the PR description.
- Record: the original request (e.g. a Slack instruction, summarized), what changed and why, and how it was verified.
- The Security & Data Protection rules apply to worklog files too — no personal names, handles, emails, or other personal data; refer to request sources by channel/system and date, not by name.
- Never modify another branch's worklog file.

## Content authoring

- Program entries live in `content/programs/<slug>/` as Markdown with front matter. Each entry has an English file (`index.md`) and a Korean counterpart (`index.ko.md`). Keep both language versions in sync when adding or editing content.
- **`status` and `deadline` are mutually exclusive** — if a program has an open `deadline`, leave `status` empty, and vice versa. This is a static-Markdown convention (no automatic transition) enforced by `scripts/check_programs.py`.
- **`industry` and `verticals`** must match the PitchBook taxonomy references in `docs/references/` ([taxonomy](docs/references/pitchbook-industry-taxonomy.md), [verticals](docs/references/pitchbook-industry-verticals.md)); the frontmatter linter checks this.
- Do not publish personal data. Only use approved public contact addresses (see the allowlist in `.gitleaks.toml`); adding a new one requires a human-reviewed change to that protected file. If a page genuinely needs a new contact address, open the PR without it and note the address in the PR description for a human to review.
- Research and reusable workflows live under `open-innovations/`:
  - `open-innovations/skills/` — reusable skills, e.g. `collect-open-innovation.md` (source collection) and `create-hugo-open-innovation-content.md` (author a program page). Prefer these over ad-hoc edits when they apply.
  - `open-innovations/references/`, `open-innovations/reports/`, `open-innovations/worklogs/` — lead sources, collection reports, and research worklogs.

## Conventions

- **Language**: All documentation, code comments, commit messages, and PR text in **English**.
- **Style**: Be concise and technical.
- Proactively suggest best practices, but keep changes focused and atomic.
