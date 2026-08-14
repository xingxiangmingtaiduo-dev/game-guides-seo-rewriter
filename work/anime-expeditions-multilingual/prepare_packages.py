from __future__ import annotations

import re
from pathlib import Path


SOURCE_DIR = Path(r"C:\Users\Og\Desktop\已SEO文章\Anime Expeditions七语言SEO")
OUTPUT_DIR = Path(r"C:\Users\Og\.codex\skills\game-guides-seo-rewriter\work\anime-expeditions-multilingual\packages")

LANGUAGES = {
    "Traditional-Chinese": "繁體中文",
    "English": "English",
    "Portuguese": "Português",
    "Spanish": "Español",
    "Thai": "ภาษาไทย",
    "Indonesian": "Bahasa-Indonesia",
    "Vietnamese": "Tiếng-Việt",
}

KEY_MAP = {
    "slug": "Slug",
    "seo_title": "SEO Title",
    "primary_keyword": "Primary Keyword",
    "secondary_keywords": "Secondary Keywords",
    "meta_description": "Meta Description",
    "tags": "Tags",
    "body_length_target": "Body Length Target",
    "output_language": "Output Language",
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    match = re.match(r"^---\n(.*?)\n---\n\n(.*)$", text, re.DOTALL)
    if not match:
        raise ValueError("Missing frontmatter")
    values = {}
    for line in match.group(1).splitlines():
        key, value = line.split(":", 1)
        values[key] = value.strip().strip('"')
    return values, match.group(2)


def make_package(stem: str, old_stem: str) -> None:
    source = SOURCE_DIR / f"Anime Expeditions_SEO_{old_stem}_500-600.md"
    values, body = parse_frontmatter(source.read_text(encoding="utf-8"))
    alts: list[str] = []

    def replace_image(match: re.Match[str]) -> str:
        alts.append(match.group(1))
        return f"<!-- SOURCE_IMAGE:{len(alts)} -->"

    body = re.sub(r"!\[(.*?)\]\(<[^>]*source-image-\d+\.[^>]+>\)", replace_image, body)
    body = re.sub(
        r"^(##\s+(?:Introduction|Introdução|Introducción|前言|บทนำ|Pendahuluan|Giới thiệu)\s*\n\n)",
        "",
        body,
        flags=re.MULTILINE,
    )
    if len(alts) != 19:
        raise ValueError(f"{stem}: expected 19 source images, found {len(alts)}")
    metadata = "\n".join(f"- {KEY_MAP[key]}: {values[key]}" for key in KEY_MAP)
    plan = []
    for index, alt in enumerate(alts, 1):
        plan.extend(
            [
                f"{index}. Source image {index}",
                f"   - Alt: {alt}",
                "   - Purpose: Preserve the matching source visual in its original article context.",
                f"   - Source Image: {index}",
            ]
        )
    package = f"# {values['title']}\n\n## SEO Metadata\n\n{metadata}\n\n## Article Body\n\n{body.strip()}\n\n## Image Plan\n\n" + "\n".join(plan) + "\n"
    (OUTPUT_DIR / f"{stem}.md").write_text(package, encoding="utf-8", newline="\n")


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
for stem, old_stem in LANGUAGES.items():
    make_package(stem, old_stem)
