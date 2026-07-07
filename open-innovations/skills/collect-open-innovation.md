---
name: collect-open-innovation
description: Discover active corporate open innovation programs worldwide, verify official sources, and summarize them into Markdown reports or Hugo program entries.
---

# Collect Open Innovation Programs

Use this skill when the user wants to search for open innovation programs, challenge portals, startup collaboration calls, corporate venture/client pilot programs, or R&D partnership opportunities and organize the results in Markdown.

Before writing any report or Hugo entry, first check whether the candidate program already exists in `content/programs/` (or is otherwise already represented in the repository). Treat existing programs as duplicates and do not count them as newly discovered.

The main output can be either:

- A research report under `open-innovations/` that records only newly discovered programs not already present in the repository.
- Individual Hugo entries under `content/programs/` for selected new programs.

You may use aggregator sites, directories, innovation platform listings, newsletters, and database-style roundups as discovery inputs, but never as the final authority for program facts.

Reference file:

- `open-innovations/references/open-innovation-lead-sources.md`

## Definition

Open innovation programs are initiatives where corporations, universities, research institutes, accelerators, public agencies, or consortiums invite external partners to submit technologies, startup solutions, research proposals, pilots, or commercialization ideas.

Include programs that clearly accept external participation from one or more of these groups:

- Startups and scaleups
- Researchers, universities, and labs
- Inventors and entrepreneurs
- Suppliers, technology vendors, and solution providers
- SMEs or industry partners

Exclude:

- Generic VC portfolio pages with no external application or collaboration path
- Expired challenge pages unless the user specifically asks for historical examples
- Pure job postings, grants with no innovation or collaboration focus, and procurement-only tenders
- Blog posts that mention innovation but do not link to an official program, challenge, or application path

Treat these as `lead sources only`, not final evidence:

- Aggregator sites that list many programs
- Innovation directories or scouting databases
- Newsletters, media roundups, and blog compilations
- Third-party challenge platforms unless the platform page is clearly the official application destination for the sponsor

## Research Workflow

1. Confirm the scope if needed.
   - Default scope: worldwide, currently active or always-open programs.
   - Default languages: English plus local-language sources when search results indicate useful regional coverage.
   - Default minimum result count: 20 high-confidence programs, unless the user requests another number.

2. Search broadly, then verify from official sources.
   - Use web search for discovery.
   - Review `open-innovations/references/open-innovation-lead-sources.md` when you want a faster starting list of aggregator sites and challenge marketplaces.
   - Use aggregator sites and directory-style pages to accelerate discovery when they expose many relevant candidate programs.
   - Treat aggregator pages as lead generation only.
   - Prefer official corporate, university, government, or challenge platform pages as sources.
   - Use secondary sources only to discover leads, not as the final authority.
   - Before collecting a candidate, check whether it already exists in `content/programs/` or is otherwise already represented in the repository; if so, exclude it from the new-program count and do not include it in the report's main shortlist.
   - Every included program must have at least one official source URL.
   - If a candidate is first discovered on an aggregator, click through and verify the current status on the official sponsor page, official challenge page, official application page, or official press release before including it.

3. Use source hierarchy.
   Rank evidence in this order:
   - Official application page or official challenge portal
   - Official program landing page on the sponsor or operating partner site
   - Official press release or official news post announcing the current cohort, call, or application round
   - Official PDF or terms page tied to the program
   - Third-party listing or aggregator page, for discovery only

   If only a third-party listing exists and no official source can be verified, do not include the program in the main list. Put it under `Excluded Or Uncertain Leads` instead.

4. Use diversified search queries.
   Combine global and regional queries such as:
   - `"open innovation" startup challenge apply`
   - `"open innovation portal" corporation`
   - `"startup collaboration" "open innovation"`
   - `"innovation challenge" startup corporate`
   - `"technology scouting" "submit your solution"`
   - `"partner with us" "open innovation"`
   - `"external innovation" "submit"`
   - `"R&D collaboration" startup challenge`
   - `"open innovation" site:.com`
   - `"open innovation" site:.eu`
   - `"open innovation" Japan startup challenge`
   - `"open innovation" Korea startup challenge`
   - `"open innovation" Singapore startup challenge`
   - `"open innovation" India startup challenge`
   - `"open innovation" Middle East startup challenge`
   - `"open innovation" Latin America startup challenge`
   - `site:f6s.com corporate startup challenge`
   - `site:innovationexchange.org open innovation`
   - `site:herox.com company challenge startup`
   - `site:innocentive.com challenge company`
   - `site:yet2.com open innovation`
   - `site:plugandplaytechcenter.com innovation program corporate`
   - `site:enterpriseeuropeanetwork.ec.europa.eu open call innovation`

5. Prioritize diversity.
   Aim to cover multiple regions and sectors:
   - Regions: North America, Europe, East Asia, Southeast Asia, India, Middle East, Latin America, Africa, Oceania
   - Sectors: consumer goods, healthcare, pharma, chemicals, mobility, energy, manufacturing, food/agri, finance, telecom, software, sustainability

6. Verify current status.
   - Mark as `Always Open` when the official page accepts ongoing submissions.
   - Mark as `Active` when there is a currently open challenge or visible application window.
   - Record `deadline: YYYY-MM-DD` when a deadline is published.
   - Keep `status` for non-date labels such as `Always Open`, `Active`, `Closed`, or `Unknown`.
   - Mark as `Closed` only when useful to include and clearly labeled closed.
   - If current status is not explicit, write `Unknown` and explain the uncertainty in notes.
   - Never infer `Active` only because an aggregator says a program is open. Confirm from the official source.

7. Deduplicate.
   - Merge duplicate portals for the same sponsor and program.
   - Keep separate entries when a corporation has distinct challenge portals by business unit, region, or technology domain.
   - If multiple aggregators point to the same official program, retain only one program entry and optionally note the discovery source in `leadSource`.

## Data Fields

Extract these fields for each program:

- `program`: Public program or challenge name
- `company`: Sponsoring organization
- `region`: Primary geography or `Global`
- `country`: Sponsor country or main program country, if clear
- `sector`: Main industry sector
- `leadSource`: Where the program was first discovered, if relevant
- `externalUrl`: Direct official URL
- `focusAreas`: Technologies, industries, challenge themes, or problem statements
- `eligibility`: Who can apply
- `status`: `Always Open`, `Active`, `Closed`, or `Unknown`
- `deadline`: ISO date when available, otherwise blank
- `benefits`: Pilot, funding, mentoring, lab access, commercial partnership, procurement, investment, etc.
- `applicationPath`: How to apply or submit
- `sourceNotes`: Short note about where the data came from and any ambiguity
- `lastChecked`: Today's date in `YYYY-MM-DD`

Rules for `leadSource`:

- Use this only when a third-party site materially helped discovery.
- Format as a short label plus URL when helpful, for example `F6S - https://www.f6s.com/...`
- Do not use `leadSource` as the evidence field for status, deadline, or benefits. Those must still come from official pages.

## Markdown Research Report

When the user asks to collect or search open innovation programs globally, create a Markdown report in:

```text
open-innovations/reports/YYYY-MM-DD-global-open-innovation-programs.md
```

Filename collision rule:

- If no report exists yet for that date, use `open-innovations/reports/YYYY-MM-DD-global-open-innovation-programs.md`.
- If a report for that date already exists, create a new file with a time suffix:
  `open-innovations/reports/YYYY-MM-DD-global-open-innovation-programs-HHMM.md`
- Use 24-hour time in the local workspace timezone.
- Do not overwrite an existing same-day report unless the user explicitly asks to update that exact file.

Use this structure:

```markdown
# Global Open Innovation Programs

Last checked: YYYY-MM-DD
Scope: Worldwide active and always-open open innovation programs

## Summary

- Total programs reviewed: N
- Included high-confidence programs: N
- Regions covered: ...
- Sectors covered: ...

## Shortlist

| Program | Sponsor | Region | Sector | Status | Focus Areas | Official Link |
|---|---|---|---|---|---|---|
| Program Name | Company | Global | Chemicals | Always Open | Sustainability; Packaging | https://... |

## Program Details

### Program Name - Company

- Region: Global
- Country: Germany
- Sector: Consumer goods
- Status: Always Open
- Deadline:
- Lead source: F6S - https://...
- Eligibility: Startups; researchers; suppliers
- Focus areas: Sustainability; packaging; ingredients
- Benefits: Pilot collaboration; R&D access
- Application path: Submit via the official portal
- Official source: https://...
- Notes: Any ambiguity or evidence quality comments.

## Excluded Or Uncertain Leads

| Lead | Reason | URL |
|---|---|---|
| Example | Expired challenge, no active application path | https://... |
```

Keep the report concise but evidence-based. Do not overstate status, eligibility, benefits, or deadlines beyond what official sources support.
When a lead came from a third-party site, it is fine to mention that in the details, but keep the official URL as the primary link in the table and narrative.

## Hugo Program Entry

When the user wants selected programs added to the Hugo site, create files under:

```text
content/programs/<program-slug>.md
```

Use `hugo new content programs/<program-slug>.md` when possible. Otherwise create the file manually with this frontmatter:

```yaml
---
title: "Program Name"
date: YYYY-MM-DD
draft: false
company: "Sponsor Name"
externalUrl: "https://example.com/open-innovation"
focusAreas:
  - "Area 1"
  - "Area 2"
eligibility:
  - "Startups"
  - "Researchers"
status: "Always Open"
deadline: ""
summary: "A brief one or two-sentence description of the program and its goals."
---
```

Rules:

- Use `deadline` for date-based closing information in `YYYY-MM-DD` format.
- Do not encode dates inside `status`.
- Omit `status` when the only meaningful state is the deadline and there is no separate label such as `Active` or `Always Open`.

Use this body structure:

```markdown
## Overview

Describe the program, sponsor, and collaboration goal.

## Focus Areas

- Specific technology or problem area
- Specific industry or business unit

## Collaboration & Benefits

- Pilot, R&D, lab, funding, mentoring, commercial, procurement, or investment benefits

## How to Apply

Explain the submission path, timeline, and official link.

## Sources

- [Official program page](https://...)
```

## Quality Bar

- Use official source URLs for all included programs.
- Use aggregator and directory pages for discovery only, then re-verify against official sources.
- Prefer current pages with clear application or contact paths.
- Use ISO dates for deadlines and `lastChecked`.
- Preserve uncertainty instead of guessing.
- Avoid copying long source text. Summarize in original words.
- Keep each report row scannable; put detailed nuance in the program detail section.
- When using web research, cite or link sources in the Markdown output itself.

## Example Mapping: Henkel Spark

Source: `https://www.henkel.com/our-businesses/henkel-consumer-brands/open-innovation`

- `program`: Henkel Spark
- `company`: Henkel
- `region`: Global
- `country`: Germany
- `sector`: Consumer goods
- `externalUrl`: `https://www.henkel.com/our-businesses/henkel-consumer-brands/open-innovation`
- `focusAreas`: Sustainability; Laundry & Home Care; Beauty & Hair Care; Active Ingredients; Packaging
- `eligibility`: Startups; researchers; suppliers
- `status`: Always Open
- `benefits`: R&D partnership, pilot opportunities, access to Henkel expertise
- `applicationPath`: Submit through the official Henkel Spark portal
