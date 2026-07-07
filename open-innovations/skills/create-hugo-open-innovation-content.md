---
name: create-hugo-open-innovation-content
description: Convert an open innovation research report into Hugo content/programs Markdown entries with normalized frontmatter, PitchBook-based industry and vertical classification, body sections, and source links.
---

# Create Hugo Open Innovation Content

Use this skill when the user wants to turn an open innovation research report, especially a report under `open-innovations/reports/`, into Hugo content files under `content/programs/`.

This skill is for content generation after research has already been done. If the user still needs discovery or verification, use `collect-open-innovation` first.

## Input

Default input report:

```text
open-innovations/reports/2026-06-08-global-open-innovation-programs.md
```

The report should contain:

- A `## Shortlist` table with `Program`, `Sponsor`, `Status`, `Focus Areas`, and `Official Link`
- A `## Program Details` section with one heading per program
- Detail fields such as `Region`, `Country`, `Sector`, `Eligibility`, `Benefits`, `Application path`, `Official source`, and `Notes`

## Output

Create one Hugo leaf bundle per included program:

```text
content/programs/<program-slug>/index.md
content/programs/<program-slug>/index.ko.md
content/programs/<program-slug>/feature.<ext>
```

Do not create content for rows under `## Excluded Or Uncertain Leads` unless the user explicitly asks.

Default language rule:

- Unless the user explicitly asks for English-only output, create both `index.md` and `index.ko.md` for every new program bundle.
- Treat Korean content as required, not optional.
- If an English file already exists but the Korean file is missing, create only the missing `index.ko.md` unless the user asks to refresh English too.

## Conversion Workflow

1. Read the full report and identify the `## Program Details` entries.
2. For each program, extract the sponsor, source URL, status, deadline, eligibility, focus areas, benefits, application path, and notes.
3. Generate a stable slug.
4. Check whether `content/programs/<slug>/index.md` already exists.
5. Also check for an existing program by comparing the official URL and normalized title across existing `content/programs/*/index.md` files.
6. If an existing bundle already represents the same program, skip it.
7. If the bundle exists, do not overwrite it unless the user asks to refresh or replace existing content.
8. Create only missing entries with valid Hugo YAML frontmatter and a concise body.
9. Create the Korean companion file for each new entry.
10. Add a small representative image when a suitable official image can be found.
11. Run a quick validation pass:
   - Every file has frontmatter bounded by `---`.
   - `draft` is `false`.
   - `industry` is a non-empty YAML list, and every entry exactly matches one of the seven canonical PitchBook sectors.
   - `verticals` is a non-empty YAML list, and every entry exactly matches a canonical PitchBook Industry Vertical name.
   - `externalUrl` is non-empty.
   - If `featureimage` is used, it points to an existing bundle-local image.
   - Otherwise, any representative image is named `feature.<ext>`, `cover.<ext>`, or `thumbnail.<ext>` inside the same bundle.
   - `verticals` and `eligibility` are YAML lists.
   - Body includes `## Overview`, `## Focus Areas`, `## Collaboration & Benefits`, `## How to Apply`, and `## Sources`.
   - Both `index.md` and `index.ko.md` exist for each newly created bundle unless the user explicitly requested otherwise.

## Slug Rules

Use lowercase ASCII slugs:

- Convert `Program - Sponsor` into a slug when the program name is generic.
- Use only the program name when it is distinctive.
- Replace `+` with `plus`.
- Replace `&` with `and`.
- Remove apostrophes, periods, commas, parentheses, trademark symbols, and slashes.
- Replace spaces and remaining punctuation with single hyphens.
- Collapse duplicate hyphens.

Examples:

- `Connect + Develop` -> `pg-connect-plus-develop`
- `Open Innovation - AstraZeneca` -> `astrazeneca-open-innovation`
- `Startup Garage - BMW Group` -> `bmw-group-startup-garage`
- `Open Innovation Platform - IMDA Singapore` -> `imda-open-innovation-platform`
- `NASA Prizes, Challenges, and Crowdsourcing` -> `nasa-prizes-challenges-crowdsourcing`

## Duplicate Detection Rules

Treat a program as already existing and skip creation when any of these is true:

- `content/programs/<slug>/index.md` already exists for the generated slug.
- Another existing bundle has the same `externalUrl`.
- Another existing bundle has the same normalized program title after lowercasing and removing minor punctuation differences.

When a duplicate is found:

- Do not create a new bundle for the same program.
- Do not rename or overwrite the existing bundle unless the user explicitly asks for a refresh, merge, or replacement.
- Prefer reporting which existing path was matched so the user can decide whether to update it later.

## Frontmatter Schema

Use the existing project schema:

```yaml
---
title: "Program Name"
date: YYYY-MM-DD
draft: false
company: "Sponsor Name"
industry:
  - "Information Technology"
externalUrl: "https://official.example/path"
verticals:
  - "Artificial Intelligence & Machine Learning (AI/ML)"
  - "Cybersecurity"
eligibility:
  - "Startups"
  - "Researchers"
status: "Always Open"
deadline: ""
summary: "One sentence describing the program, sponsor, and collaboration opportunity."
---
```

Use the same schema for `index.ko.md`. Translate `summary` into natural Korean while keeping names, brands, URLs, dates, and status values faithful to the source report.

Rules:

- `industry` is required and is a YAML list of one or more of the seven PitchBook Primary Industry Sectors (see `## Industry Classification`). List the primary sector first. Most programs have a single entry; add a second (or third) only when the program genuinely spans multiple sectors. Every entry drives the industry filter bar on the home and programs list pages, so each must match a canonical value character-for-character.
- `verticals` is required and is a YAML list of one to four canonical PitchBook Industry Verticals (see `## Vertical Classification`). These are the thematic, tech-driven niches derived from the report's focus areas, and they render as the chips on each program card. List the most representative vertical first. Each entry must match a canonical vertical name character-for-character. Replaces the old free-text `focusAreas` field.
- Use the report `Last checked` date as `date`.
- Use `status` only for non-date labels such as `Always Open`, `Active`, `Closed`, or `Unknown`.
- If the report has a published cutoff date, store it in `deadline` using `YYYY-MM-DD`.
- Do not write `Deadline: YYYY-MM-DD` into `status`.
- Map the report's semicolon-separated `Focus areas` onto canonical verticals for the `verticals` field, and keep the original phrasing as descriptive bullets in the body `## Focus Areas` section.
- Convert semicolon-separated `Eligibility` into list items.
- If eligibility is vague, use conservative values such as `"Startups"`, `"Researchers"`, `"Companies"`, `"Solution Providers"`, or `"Innovators"` only when supported by the report.
- Keep `summary` under 220 characters.
- Do not add `featureimage` when the image is stored in the same bundle as `feature.<ext>`, `cover.<ext>`, or `thumbnail.<ext>`.
- Add `featureimage` only if a non-standard bundle-local image filename is necessary.
- Avoid adding frontmatter fields not used by the project unless the user asks.
- `status` may be omitted when `deadline` alone is enough to describe the program state.
- Keep `status` values machine-stable across languages. Use the same canonical value in `index.md` and `index.ko.md`, such as `Always Open`, `Active`, `Closed`, or `Unknown`.

## Industry Classification

The `industry` field is a controlled vocabulary, not a free-text label. Use the PitchBook Primary Industry Sector taxonomy as the source of truth: [`docs/references/pitchbook-industry-taxonomy.md`](../../docs/references/pitchbook-industry-taxonomy.md).

Each program carries a **YAML list** of one or more of these seven canonical values, with the primary sector first. Copy each string verbatim — the filter bar matches a card when any of its sector entries equals the selected tag.

| `industry` value | Use for |
|---|---|
| `Business Products and Services` | Programs whose primary customers are other businesses — industrial equipment, logistics, B2B commercial products and services, aerospace and defense |
| `Consumer Products and Services` | Programs centered on individual end consumers — FMCG, apparel, consumer durables, automotive, retail, media, consumer mobility, hospitality |
| `Energy` | Energy production, infrastructure, and services — utilities, oil and gas, renewables, energy storage |
| `Financial Services` | Banking, capital markets, insurance, and fintech-led financial programs |
| `Healthcare` | Health outcomes — medical devices, healthcare services, health IT, pharmaceuticals and biotech |
| `Information Technology` | Software, computer hardware, semiconductors, communications/networking, and IT services |
| `Materials and Resources` | Physical material extraction and processing — chemicals, agriculture, metals and mining, construction materials, packaging |

Classification rules:

- Choose the **primary sector** that best matches the program's main focus, judged by who the program ultimately serves and what it produces, and list it first. When in doubt, follow the "primary customer" test in the taxonomy doc (business customer → `Business Products and Services`; end consumer → `Consumer Products and Services`).
- Add a **second (or third) sector** only when the program genuinely operates across sectors — for example a sponsor with two core businesses (ZEISS → `Business Products and Services` + `Healthcare`) or a program whose focus straddles sectors (a sustainability accelerator run by a consumer brand → `Consumer Products and Services` + `Materials and Resources`). Do not list more than is true; a single sector is the norm. Never list all seven as a substitute for "any sector" — for sector-agnostic programs use the single sponsor-anchored sector below.
- The seven sectors have **no "Cross-Industry" or "Sustainability" bucket**. For a sector-agnostic accelerator or corporate venture program, classify by the **sponsor's primary business sector** (e.g. an automaker's open-innovation arm → `Consumer Products and Services`; an industrial conglomerate's startup gateway → `Business Products and Services`).
- Map sustainability/climate programs by their underlying activity: clean power and grid → `Energy`; circular materials, recycling, and chemicals → `Materials and Resources`.
- Do not invent new sector strings, abbreviations, or parentheticals (`IT`, `ICT`, `FMCG`, `Cross-Industry` are **not** valid values).

When normalizing existing free-text values, use this mapping as a starting point and confirm against the program's actual focus:

| Legacy free-text value | Canonical sector |
|---|---|
| `ICT` | `Information Technology` |
| `Manufacturing` | `Business Products and Services` |
| `FMCG` | `Consumer Products and Services` |
| `Automotive` | `Consumer Products and Services` |
| `Mobility` | `Consumer Products and Services` |
| `Logistics` | `Business Products and Services` |
| `Aerospace` | `Business Products and Services` |
| `Healthcare` | `Healthcare` |
| `Energy` | `Energy` |
| `Sustainability` | `Energy` or `Materials and Resources` (by activity) |
| `Cross-Industry` | Sponsor's primary sector (decide per program) |

## Vertical Classification

The `verticals` field is a controlled vocabulary that complements `industry`. Where `industry` answers "which of the seven broad sectors," `verticals` captures the **thematic, tech-driven niches** a program targets — these can cross sectors. Use the PitchBook Industry Verticals taxonomy as the source of truth: [`docs/references/pitchbook-industry-verticals.md`](../../docs/references/pitchbook-industry-verticals.md).

Each program carries a **YAML list of one to four** of these verticals. Copy each name verbatim from the verticals doc, including casing, ampersands, and parentheticals — for example `"Artificial Intelligence & Machine Learning (AI/ML)"`, `"Climate Tech"`, `"Digital Health"`, `"Cybersecurity"`. The verticals render as the chips on each program card, so the most representative vertical comes first.

Classification rules:

- Derive verticals from the report's **focus areas, sector, and program description** — not from the sponsor's name alone. Pick the verticals that best describe what the program actually invites startups to work on.
- A program belongs to **one industry but may carry multiple verticals**. It is normal for a `Healthcare` program to carry `"Digital Health"` and `"Life Sciences"`, or for an `Energy` program to carry `"Cleantech"` and `"Climate Tech"`.
- Keep the list focused: **one to four** verticals. Do not pad the list to cover every loosely related theme. If a program is broad and sector-agnostic, pick the two or three verticals that most define it (often `"Advanced Manufacturing"`, `"SaaS"`, or `"Artificial Intelligence & Machine Learning (AI/ML)"` for generic corporate accelerators).
- Prefer a **specific vertical over an aggregate** one. `"Industrials"`, `"Manufacturing"`, and `"Technology, Media & Telecommunications (TMT)"` are intentionally broad — use a sharper vertical (e.g. `"Advanced Manufacturing"`, `"Robotics & Drones"`, `"Construction Technology"`) when the focus supports it.
- Do not invent vertical names, abbreviations, or new parentheticals. If a focus area has no matching vertical, choose the closest canonical vertical rather than coining a new string.

When migrating existing free-text `focusAreas` values, map each phrase to the closest canonical vertical and confirm against the program's actual focus. Common mappings:

| Legacy free-text focus area | Canonical vertical |
|---|---|
| `AI`, `Artificial Intelligence`, `Machine Learning`, `Data Analytics` | `Artificial Intelligence & Machine Learning (AI/ML)` |
| `Sustainability`, `Decarbonization`, `Net Zero`, `Climate` | `Climate Tech` |
| `Clean Energy`, `Renewables`, `Energy Storage`, `Cleantech` | `Cleantech` |
| `Digital Health`, `Telehealth`, `Health IT`, `Medtech` | `Digital Health` |
| `Biotech`, `Pharma`, `Drug Discovery`, `Life Sciences` | `Life Sciences` |
| `Mobility`, `Automotive`, `EV` | `Mobility Tech` |
| `Logistics`, `Supply Chain` | `Supply Chain Technology` |
| `IoT`, `Connected Devices`, `Sensors` | `Internet of Things (IoT)` |
| `Cybersecurity`, `Security` | `Cybersecurity` |
| `Fintech`, `Payments`, `Banking` | `Fintech` |
| `Insurance`, `Insurtech` | `Insurtech` |
| `Manufacturing`, `Industry 4.0`, `Smart Factory`, `Robotics`, `Automation` | `Advanced Manufacturing` or `Robotics & Drones` (by focus) |
| `Agriculture`, `Farming`, `Food`, `Agrifood` | `Agtech` or `Foodtech` (by focus) |
| `Circular Packaging`, `Recycling`, `Materials`, `Chemicals` | `Cleantech` (or `Advanced Manufacturing` for process tech) |
| `Cloud`, `DevOps`, `Infrastructure software` | `Cloudtech & DevOps` |
| `SaaS`, `Enterprise Software`, `B2B Software` | `Software as a Service (SaaS)` |
| `Blockchain`, `Crypto`, `Web3` | `Cryptocurrency & Blockchain` |
| `Space`, `Satellite`, `Aerospace` | `Space Tech` |
| `Construction`, `PropTech` real estate build | `Construction Technology` or `Real Estate Tech` |
| `Retail`, `Commerce`, `D2C` | `Ecommerce` |
| `Marketing`, `Adtech` | `Marketing Tech` or `Adtech` |
| `Education`, `Learning` | `Edtech` |
| `Gaming`, `Esports` | `Gaming` or `eSports` |
| `AR/VR`, `Metaverse`, `Immersive` | `Augmented Reality (AR)` or `Virtual Reality (VR)` |

## Representative Image Workflow

Cards on the home page can show a small representative image from the program leaf bundle.

Preferred structure:

```text
content/programs/<program-slug>/
  index.md
  feature.<ext>
```

Use this workflow when creating or refreshing a program entry:

1. Look for an official image source.
   - Prefer the official program page's Open Graph image (`og:image`) or Twitter card image.
   - If `og:image` or Twitter card image is missing, inspect the official page body before deciding there is no image.
     - Search the fetched HTML for `<img src=...>`, `srcset=...`, `data-src=...`, `data-lazy=...`, `background-image: url(...)`, and image-like links ending in `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`, or `.svg`.
     - Also inspect obvious official CSS/asset paths when the page uses a CMS and references site assets, for example `/images/`, `/assets/images/`, `/ResourcePackages/.../assets/images/`, `/media/`, `/uploads/`, `/wp-content/uploads/`, or `/_next/image`.
     - Convert root-relative URLs such as `/images/default-source/.../oin-banners.gif?sfvrsn=...` into absolute URLs using the official page origin.
     - Keep query strings when they appear to be required by the CMS or CDN.
   - Prefer page-body images in this order:
     1. Hero/banner images near the program title, main headline, or first viewport.
     2. Program or platform logo images from the official page.
     3. Challenge-card or success-story thumbnails only when they represent the same official platform and no broader program image is available.
   - If no suitable program/platform image exists, use an official sponsor logo only when it is publicly served by the sponsor and suitable as a small editorial thumbnail.
   - Do not use random stock images, search-result thumbnails, third-party logos, or images from unrelated news/blog pages.
   - Do not reject official page-body images just because no `og:image` exists.

Official CMS example:

- `https://www.openinnovationnetwork.gov.sg/` has no `og:image`, but the official HTML includes image assets such as:
  - `/images/default-source/default-album/homepage/oin-logo.png?sfvrsn=...`
  - `/images/default-source/default-album/oin-banners.gif?sfvrsn=...`
  - `/images/default-source/default-album/homepage/share-and-divide.jpg?sfvrsn=...`
- For this case, use the official hero/banner or logo image after converting it to an absolute URL, for example:
  - `https://www.openinnovationnetwork.gov.sg/images/default-source/default-album/oin-banners.gif?sfvrsn=...`

2. Download the image locally.
   - Store the image inside the program bundle:

```text
content/programs/<program-slug>/feature.<ext>
```

   - Use `feature.<ext>` as the default filename.
   - `cover.<ext>` or `thumbnail.<ext>` are acceptable alternatives.
   - Prefer `.jpg`, `.png`, or `.webp` based on the original file type.
   - If the source URL has a query string, infer the extension from the path before the query string.
   - If the image is a GIF but it is used as a static representative card image, save it as `feature.gif` only when Hugo and the theme render it correctly. Otherwise prefer another official static image from the same page, such as a PNG logo or JPEG hero/card image.
   - Keep images small. Aim for a final width of 320-640 px and a file size under 150 KB when practical.

3. Resize when needed.
   - On macOS, `sips -Z 640 content/programs/<program-slug>/feature.<ext>` is acceptable for JPEG/PNG images.
   - Preserve aspect ratio.
   - Avoid huge screenshots or full-size hero images.

4. Wire the image into the page.
   - If the image is named `feature.<ext>`, `cover.<ext>`, or `thumbnail.<ext>` inside the bundle, do not add a frontmatter image field.
   - If a non-standard image filename is necessary, set `featureimage` to the filename relative to the bundle.
   - Correct:

```yaml
featureimage: "program-logo.jpg"
```

   - Incorrect:

```yaml
featureimage: "assets/images/programs/pg-connect-plus-develop.jpg"
```

5. Track image provenance.
   - Add the official source page under `## Sources`.
   - If the image URL is different from the program page, add a second source line such as:

```markdown
- [Representative image source](https://official.example/image-or-page)
```

6. If no suitable official image is available:
   - Omit `featureimage`.
   - Do not invent or generate a logo unless the user explicitly asks for generated placeholder artwork.
   - The card should still render without an image.
   - Before reporting no image found, state which official-image checks were attempted: metadata image, body `<img>`, lazy image attributes, CSS/background URLs, and official asset paths.

## Body Template

Each generated file should use this body:

```markdown
## Overview

Short paragraph describing the sponsor, program purpose, target collaborators, and current status.

## Focus Areas

- Area 1
- Area 2

## Collaboration & Benefits

- Benefit or collaboration pathway
- Benefit or collaboration pathway

## How to Apply

- Explain the application path in a short sentence.
```

Create a Korean companion body in `index.ko.md` using the same section structure:

```markdown
## Overview

짧은 한국어 문단으로 프로그램 목적, 운영 주체, 대상 협업 파트너, 현재 상태를 설명한다.

## Focus Areas

- 항목 1
- 항목 2

## Collaboration & Benefits

- 협업 방식 또는 기대 효과
- 협업 방식 또는 기대 효과

## How to Apply

지원 경로를 한 문장으로 설명한다.
```

Korean writing rules:

- Write natural Korean, not word-for-word translation.
- Keep brand names, program names, URLs, and ISO dates unchanged unless there is a widely used Korean rendering.
- Translate descriptive text, benefits, and application instructions into concise Korean.
- It is acceptable to keep the section headings in English if that matches the existing project pattern.
- Preserve uncertainty in Korean too. If status is `Unknown`, explain why the current application state is unclear.

If the report has multiple official sources, include them all under `## Sources`.

## Content Rules

- Base content on the report. Do not invent benefits, deadlines, or eligibility.
- Preserve uncertainty. If status is `Unknown`, say why in the overview or `How to Apply`.
- Keep body text concise and useful for browsing.
- Avoid copying long source text. Write summaries in original words.
- Prefer hyphen bullets, not `*` bullets.
- Use ASCII punctuation unless source names require otherwise.
- Use local representative images only; do not hotlink image URLs in `featureimage`.
- Prefer leaf bundles over standalone Markdown files so each program's content and image stay together.

## Existing Content Handling

If `content/programs/henkel-spark/index.md` already exists, leave it unchanged by default.

If `content/programs/henkel-spark/index.md` exists but `content/programs/henkel-spark/index.ko.md` does not, create the missing Korean file by default.

If `content/programs/henkel-spark/index.ko.md` exists but the English file does not, create the missing English file by default.

If an older standalone file exists, such as `content/programs/henkel-spark.md`, do not silently create a duplicate bundle. Ask the user whether to migrate it, unless the user explicitly asked for migration.

When duplicate or near-duplicate entries are possible:

- Prefer the more specific program name over a generic one.
- Avoid creating both `bosch-corporate-innovation-gateway/index.md` and `open-bosch/index.md` only if the report clearly describes them as the same program. If the report presents them as separate collaboration paths, create separate entries.
- For generic titles such as `Open Innovation`, prefix the sponsor in the slug and use a title like `"AstraZeneca Open Innovation"` if that improves browsing clarity.

## Image Validation Checklist

Before finishing a content-generation task with images:

- Confirm `content/programs/<slug>/index.md` exists.
- Confirm `content/programs/<slug>/index.ko.md` exists.
- Confirm any representative image exists in the same bundle as `feature.<ext>`, `cover.<ext>`, or `thumbnail.<ext>`.
- If `featureimage` is used, confirm it points to a real bundle-local image filename.
- Run `hugo` and confirm the build succeeds.
- Check the generated home page HTML for the image path or inspect the local site visually if a server is running.
- Report any program entries that were created without images because no suitable official image was found.

## Recommended Batch From 2026-06-08 Report

For `open-innovations/reports/2026-06-08-global-open-innovation-programs.md`, create missing entries for the 20 included shortlist rows:

- `pg-connect-plus-develop/index.md`
- `henkel-spark/index.md` if it does not already exist
- `enel-open-innovability/index.md`
- `shell-gamechanger/index.md`
- `astrazeneca-open-innovation/index.md`
- `johnson-and-johnson-innovation-challenges-jlabs/index.md`
- `bayer-open-innovation-and-collaboration/index.md`
- `nestle-rd-accelerator-open-innovation/index.md`
- `corbion-open-innovation/index.md`
- `bosch-corporate-innovation-gateway/index.md`
- `open-bosch/index.md`
- `bmw-group-startup-garage/index.md`
- `siemens-collaborations-and-open-innovation/index.md`
- `imda-open-innovation-platform/index.md`
- `singapore-open-innovation-network/index.md`
- `k-startup-grand-challenge-2026/index.md`
- `ship-sdgs-holistic-innovation-platform/index.md`
- `xprize-active-competitions/index.md`
- `mit-solve-open-challenges/index.md`
- `nasa-prizes-challenges-crowdsourcing/index.md`

After generation, report which files were created and which existing files were skipped.

When reporting results, separate:

- Bundles created in both languages
- English files created
- Korean files created
- Existing bundles skipped
- Existing English or Korean companion files that were already present
