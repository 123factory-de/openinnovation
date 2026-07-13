#!/usr/bin/env python3
"""Lint content/programs frontmatter.

Rules:
1. `status` and `deadline` are mutually exclusive — a program with a deadline
   must leave `status` empty (static markdown cannot flip Active -> Closed
   when the deadline passes; templates derive the state from `deadline`).
2. `industry` values must be one of the 7 PitchBook primary industry sectors
   (docs/references/pitchbook-industry-taxonomy.md).
3. `verticals` values must be official PitchBook industry verticals
   (docs/references/pitchbook-industry-verticals.md). Korean files use the
   same English taxonomy terms as the English files.
"""

import glob
import re
import sys

VALID_INDUSTRIES = {
    "Business Products and Services (B2B)",
    "Consumer Products and Services (B2C)",
    "Energy",
    "Financial Services",
    "Healthcare",
    "Information Technology (IT)",
    "Materials and Resources",
}

VALID_VERTICALS = {
    "3D Printing", "Adtech", "Advanced Manufacturing", "Agtech",
    "Artificial Intelligence & Machine Learning (AI/ML)", "Audiotech",
    "Augmented Reality (AR)", "Autonomous Cars", "B2B Payments", "Beauty",
    "Big Data", "Cannabis", "Carsharing", "Cleantech", "Climate Tech",
    "Cloudtech & DevOps", "Construction Technology",
    "Cryptocurrency & Blockchain", "Cybersecurity", "Digital Health",
    "Ecommerce", "Edtech", "Ephemeral Content", "eSports", "Femtech",
    "Fintech", "Foodtech", "Gaming", "Healthtech", "HRtech",
    "Impact Investing", "Industrials", "Infrastructure", "Insurtech",
    "Internet of Things (IoT)", "Legal Tech", "Life Sciences",
    "Lifestyles of Health and Sustainability (LOHAS) & Wellness",
    "Manufacturing", "Marketing Tech", "Micro-Mobility", "Mobile",
    "Mobile Commerce", "Mobility Tech", "Mortgage Tech", "Nanotechnology",
    "Oil and Gas", "Oncology", "Pet Tech", "Real Estate Tech",
    "Restaurant Tech", "Ridesharing", "Robotics & Drones",
    "Software as a Service (SaaS)", "Space Tech", "Supply Chain Technology",
    "Technology, Media & Telecommunications (TMT)", "Virtual Reality (VR)",
    "Wearables & Quantified Self",
}


def frontmatter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    return m.group(1) if m else None


def scalar(fm, key):
    m = re.search(rf'^{key}:\s*"?([^"\n]*?)"?\s*$', fm, re.M)
    return m.group(1).strip() if m else ""


def string_list(fm, key):
    m = re.search(rf"^{key}:\s*\n((?:[ \t]*-[^\n]*\n)*)", fm, re.M)
    if not m:
        return []
    return re.findall(r'-\s*"?([^"\n]+?)"?\s*$', m.group(1), re.M)


def main():
    errors = []
    paths = sorted(
        glob.glob("content/programs/*/index.md")
        + glob.glob("content/programs/*/index.ko.md")
    )
    if not paths:
        errors.append("no program files found — run from the repo root")

    for path in paths:
        fm = frontmatter(path)
        if fm is None:
            errors.append(f"{path}: missing frontmatter")
            continue

        status = scalar(fm, "status")
        deadline = scalar(fm, "deadline")
        if status and deadline:
            errors.append(
                f"{path}: status ({status!r}) and deadline ({deadline!r}) are "
                'both set — programs with a deadline must use status: ""'
            )

        for value in string_list(fm, "industry"):
            if value not in VALID_INDUSTRIES:
                errors.append(f"{path}: unknown industry {value!r}")

        for value in string_list(fm, "verticals"):
            if value not in VALID_VERTICALS:
                errors.append(f"{path}: unknown vertical {value!r}")

    if errors:
        print(f"{len(errors)} problem(s) in {len(paths)} program files:\n")
        for e in errors:
            print(f"  {e}")
        return 1

    print(f"OK: {len(paths)} program files pass all checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
