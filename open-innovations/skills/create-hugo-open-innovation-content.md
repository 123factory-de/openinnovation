---
name: create-hugo-open-innovation-content
description: Convert an open innovation research report into Hugo content/programs Markdown entries with normalized frontmatter, body sections, and source links.
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
content/programs/<program-slug>/feature.<ext>
```

Do not create content for rows under `## Excluded Or Uncertain Leads` unless the user explicitly asks.

## Conversion Workflow

1. Read the full report and identify the `## Program Details` entries.
2. For each program, extract the sponsor, source URL, status, eligibility, focus areas, benefits, application path, and notes.
3. Generate a stable slug.
4. Check whether `content/programs/<slug>/index.md` already exists.
5. If the bundle exists, do not overwrite it unless the user asks to refresh or replace existing content.
6. Create missing entries with valid Hugo YAML frontmatter and a concise body.
7. Add a small representative image when a suitable official image can be found.
8. Run a quick validation pass:
   - Every file has frontmatter bounded by `---`.
   - `draft` is `false`.
   - `externalUrl` is non-empty.
   - If `featureimage` is used, it points to an existing bundle-local image.
   - Otherwise, any representative image is named `feature.<ext>`, `cover.<ext>`, or `thumbnail.<ext>` inside the same bundle.
   - `focusAreas` and `eligibility` are YAML lists.
   - Body includes `## Overview`, `## Focus Areas`, `## Collaboration & Benefits`, `## How to Apply`, and `## Sources`.

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

## Frontmatter Schema

Use the existing project schema:

```yaml
---
title: "Program Name"
date: YYYY-MM-DD
draft: false
company: "Sponsor Name"
externalUrl: "https://official.example/path"
focusAreas:
  - "Area 1"
  - "Area 2"
eligibility:
  - "Startups"
  - "Researchers"
status: "Always Open"
summary: "One sentence describing the program, sponsor, and collaboration opportunity."
---
```

Rules:

- Use the report `Last checked` date as `date`.
- Use the report `Status` value exactly, including `Deadline: YYYY-MM-DD`.
- Convert semicolon-separated `Focus areas` into title-cased list items where appropriate.
- Convert semicolon-separated `Eligibility` into list items.
- If eligibility is vague, use conservative values such as `"Startups"`, `"Researchers"`, `"Companies"`, `"Solution Providers"`, or `"Innovators"` only when supported by the report.
- Keep `summary` under 220 characters.
- Do not add `featureimage` when the image is stored in the same bundle as `feature.<ext>`, `cover.<ext>`, or `thumbnail.<ext>`.
- Add `featureimage` only if a non-standard bundle-local image filename is necessary.
- Avoid adding frontmatter fields not used by the project unless the user asks.

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

Explain the application path, deadline if any, and link to the official program page.

## Sources

- [Official program page](https://official.example/path)
- [Representative image source](https://official.example/image-or-page)
```

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

If an older standalone file exists, such as `content/programs/henkel-spark.md`, do not silently create a duplicate bundle. Ask the user whether to migrate it, unless the user explicitly asked for migration.

When duplicate or near-duplicate entries are possible:

- Prefer the more specific program name over a generic one.
- Avoid creating both `bosch-corporate-innovation-gateway/index.md` and `open-bosch/index.md` only if the report clearly describes them as the same program. If the report presents them as separate collaboration paths, create separate entries.
- For generic titles such as `Open Innovation`, prefix the sponsor in the slug and use a title like `"AstraZeneca Open Innovation"` if that improves browsing clarity.

## Image Validation Checklist

Before finishing a content-generation task with images:

- Confirm `content/programs/<slug>/index.md` exists.
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
