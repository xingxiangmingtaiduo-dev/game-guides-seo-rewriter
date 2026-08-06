from __future__ import annotations

import argparse
import math
import json
import re
import sys
import unicodedata
from pathlib import Path


def parse_article_package(md_text: str):
    lines = md_text.splitlines()
    metadata = {}
    image_plan = []
    article_title = ""
    article_lines = []
    h2s = []
    mode = None
    i = 0

    while i < len(lines):
        stripped = lines[i].strip()

        if stripped == "## SEO Metadata":
            mode = "metadata"
            i += 1
            continue
        if stripped == "## Article Body":
            mode = "article"
            i += 1
            continue
        if stripped == "## Image Plan":
            mode = "image_plan"
            i += 1
            continue

        if mode == "metadata":
            if stripped.startswith("- ") and ":" in stripped:
                key, value = stripped[2:].split(":", 1)
                metadata[key.strip()] = value.strip().strip("`")
            i += 1
            continue

        if mode == "article":
            article_lines.append(lines[i])
            if stripped.startswith("# "):
                article_title = stripped[2:].strip()
            elif stripped.startswith("## "):
                h2s.append(stripped[3:].strip())
            i += 1
            continue

        if mode == "image_plan":
            if re.match(r"^\d+\.\s+", stripped):
                title = re.sub(r"^\d+\.\s+", "", stripped)
                alt = ""
                purpose = ""
                j = i + 1
                while j < len(lines) and lines[j].startswith("   - "):
                    detail = lines[j].strip()[2:].strip()
                    if detail.startswith("Alt:"):
                        alt = detail.split(":", 1)[1].strip().strip("`")
                    elif detail.startswith("\u7528\u9014:") or detail.startswith("用途:"):
                        purpose = detail.split(":", 1)[1].strip()
                    j += 1
                image_plan.append({"title": title, "alt": alt, "purpose": purpose})
                i = j
                continue
            i += 1
            continue

        i += 1

    article_text = "\n".join(article_lines)
    plain_text = re.sub(r"^[#>\-\d\.\*\s`]+", "", article_text, flags=re.M)
    plain_text = re.sub(r"`([^`]+)`", r"\1", plain_text)
    paragraphs = [p.strip() for p in article_text.split("\n\n") if p.strip()]
    intro = ""
    conclusion = ""
    if paragraphs:
        intro = paragraphs[1] if paragraphs and paragraphs[0].startswith("# ") and len(paragraphs) > 1 else paragraphs[0]
    conclusion_match = re.search(
        r"^##\s+(?:Conclusion(?:\s*\+\s*CTA)?|结语(?:与\s*CTA)?|結語(?:與\s*CTA)?|结论(?:与\s*CTA)?|結論(?:與\s*CTA)?)\s*$",
        article_text,
        re.IGNORECASE | re.MULTILINE,
    )
    if conclusion_match:
        conclusion = article_text[conclusion_match.end():].strip()

    return {
        "metadata": metadata,
        "article_title": article_title,
        "article_text": article_text,
        "plain_text": plain_text,
        "h2s": h2s,
        "image_plan": image_plan,
        "intro": intro,
        "conclusion": conclusion,
    }


def count_cjk(text: str) -> int:
    return len(re.findall(r"[\u4e00-\u9fff]", text))


def count_words(text: str) -> int:
    return len(re.findall(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9]+(?:['’-][A-Za-zÀ-ÖØ-öø-ÿ0-9]+)*", text))


def normalize_output_language(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii").strip().lower()
    aliases = {
        "en": "english",
        "eng": "english",
        "english": "english",
        "es": "spanish",
        "espanol": "spanish",
        "spanish": "spanish",
        "pt": "portuguese",
        "portuguese": "portuguese",
        "portugues": "portuguese",
        "fr": "french",
        "french": "french",
        "de": "german",
        "german": "german",
        "it": "italian",
        "italian": "italian",
        "zh": "chinese",
        "chinese": "chinese",
        "simplified chinese": "chinese",
        "traditional chinese": "chinese",
        "ja": "japanese",
        "japanese": "japanese",
        "ko": "korean",
        "korean": "korean",
    }
    return aliases.get(normalized, normalized or "chinese")


def choose_length_metric(language: str) -> str:
    return "word" if language in {"english", "spanish", "portuguese", "french", "german", "italian"} else "cjk"


def count_length_units(text: str, metric: str) -> int:
    return count_words(text) if metric == "word" else count_cjk(text)


def normalize_match_text(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", normalized).strip().lower()


def heading_matches_any(h2s: list[str], patterns: list[str]) -> bool:
    normalized_h2s = [normalize_match_text(h2) for h2 in h2s]
    normalized_patterns = [normalize_match_text(pattern) for pattern in patterns]
    return any(pattern in h2 for h2 in normalized_h2s for pattern in normalized_patterns)


def parse_length_target(value: str) -> tuple[int, int] | None:
    matches = re.findall(r"\d+", value)
    if len(matches) < 2:
        return None
    lower, upper = int(matches[0]), int(matches[1])
    if lower <= 0 or upper <= 0 or lower > upper:
        return None
    return lower, upper


def contains_price_reference(text: str) -> bool:
    patterns = [
        r"\bprice\b",
        r"\bpricing\b",
        r"\bprecio\b",
        r"\bcosto\b",
        r"\bcoste\b",
        r"\bpreco\b",
        r"\bpreço\b",
        r"\bprix\b",
        r"\bpreis\b",
        r"\$\s*\d",
        r"\d+\s*\u5143",
        r"\d+\s*\u5757",
        r"\u8d39\u7528",
        r"\u552e\u4ef7",
        r"\u4ef7\u683c",
    ]
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def contains_competitor_reference(text: str) -> bool:
    patterns = [
        r"\u7ade\u54c1",
        r"\u5bf9\u6bd4",
        r"\bcompetitor\b",
        r"\bcomparison with\b",
        r"\bcompare with\b",
        r"\bcomparativa con\b",
        r"\bcomparacion con\b",
        r"\bcomparación con\b",
        r"vs\.?",
        r"versus",
        r"better than",
        r"stronger than",
    ]
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)


def find_stock_ai_phrases(text: str) -> list[str]:
    patterns = [
        ("in today's fast-paced world", r"\bin today['’]s fast-paced (?:digital )?world\b"),
        ("in this comprehensive guide", r"\bin this comprehensive guide\b"),
        ("this article will explore", r"\bthis article will (?:explore|examine|delve into|walk you through)\b"),
        ("whether you are a beginner or...", r"\bwhether you(?:'re| are) (?:a )?(?:beginner|new player|seasoned player|experienced user).{0,80}\bor\b"),
        ("unlock the full potential", r"\bunlock (?:its|the|your) full potential\b"),
        ("take ... to the next level", r"\btake .{0,45} to the next level\b"),
        ("game-changer", r"\bgame[- ]changer\b"),
        ("seamless experience", r"\bseamless experience\b"),
        ("在当今……时代", r"在当今.{0,16}(?:时代|世界|环境)"),
        ("本文将……", r"本文将(?:深入)?(?:探讨|介绍|解析|带你了解)"),
        ("无论你是……还是……", r"无论你是.{0,24}还是"),
        ("随着……不断发展", r"随着.{0,24}不断(?:发展|变化|普及)"),
        ("en esta guía completa", r"\ben esta gu[ií]a completa\b"),
        ("este artículo explorará", r"\beste art[ií]culo (?:explorar[aá]|analizar[aá])\b"),
        ("neste guia completo", r"\bneste guia completo\b"),
        ("este artigo explorará", r"\beste artigo (?:explorar[aá]|analisar[aá])\b"),
    ]
    return [label for label, pattern in patterns if re.search(pattern, text, re.IGNORECASE | re.DOTALL)]


def find_routine_transition_starts(text: str) -> list[str]:
    pattern = re.compile(
        r"^(Furthermore|Moreover|Additionally|In addition|Besides|此外|另外|而且|不仅如此|"
        r"Además|Asimismo|Adicionalmente|Por otra parte|Além disso|Ademais)[,，:]?\s*",
        re.IGNORECASE | re.MULTILINE,
    )
    return [match.group(1) for match in pattern.finditer(text)]


def find_duplicate_sentences(text: str) -> list[str]:
    cleaned = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    cleaned = re.sub(r"^#{1,6}\s+.*$", " ", cleaned, flags=re.MULTILINE)
    sentences = re.split(r"(?<=[.!?。！？])\s+|[\r\n]+", cleaned)
    seen = {}
    duplicates = []
    for sentence in sentences:
        normalized = re.sub(r"\s+", " ", sentence).strip(" -*`\t\r\n").casefold()
        if count_words(normalized) < 8 and count_cjk(normalized) < 16:
            continue
        key = re.sub(r"[^\w\u4e00-\u9fff]+", "", normalized)
        if not key:
            continue
        if key in seen and seen[key] == 1:
            duplicates.append(sentence.strip())
        seen[key] = seen.get(key, 0) + 1
    return duplicates


def detect_profile(data: dict) -> str:
    text = data["article_text"]
    title = data["article_title"]
    primary = data["metadata"].get("Primary Keyword", "")
    combined = f"{title}\n{primary}\n{text}"
    lead_signal = f"{title}\n{primary}".lower()
    explicit_game_signals = [
        "guide",
        "walkthrough",
        "tier list",
        "codes",
        "afk",
        "\u653b\u7565",
        "\u6e38\u620f",
        "\u6302\u673a",
        "\u65b0\u624b",
        "\u5237",
        "\u5956\u676f",
        "\u5173\u5361",
        "\u9635\u5bb9",
    ]
    if any(signal in lead_signal for signal in explicit_game_signals):
        return "game-guide"

    explicit_product_signals = [
        "cloud phone",
        "feature",
        "tutorial",
        "workflow",
        "troubleshooting",
        "\u4e91\u624b\u673a",
        "\u529f\u80fd",
        "\u6559\u7a0b",
        "\u4ea7\u54c1",
        "\u8fdc\u7a0b",
        "\u591a\u5f00",
    ]
    if any(signal in lead_signal for signal in explicit_product_signals):
        return "product-tech"

    game_markers = [
        "AFK",
        "tier list",
        "beginner guide",
        "event guide",
        "codes",
        "\u5956\u676f",
        "\u6302\u673a",
        "\u5173\u5361",
        "\u9635\u5bb9",
        "\u65b0\u624b\u653b\u7565",
    ]
    product_markers = [
        "cloud phone",
        "UgPhone",
        "feature",
        "workflow",
        "tutorial",
        "troubleshooting",
        "\u4e91\u624b\u673a",
        "\u529f\u80fd",
        "\u6559\u7a0b",
        "\u4ea7\u54c1",
        "\u8fdc\u7a0b",
        "\u591a\u5f00",
    ]
    game_score = sum(marker.lower() in combined.lower() for marker in game_markers)
    product_score = sum(marker.lower() in combined.lower() for marker in product_markers)
    return "product-tech" if product_score > game_score else "game-guide"


def validate(data: dict, profile: str):
    metadata = data["metadata"]
    article_title = data["article_title"]
    article_text = data["article_text"]
    plain_text = data["plain_text"]
    primary = metadata.get("Primary Keyword", "")
    slug = metadata.get("Slug", "")
    seo_title = metadata.get("SEO Title", "")
    meta_desc = metadata.get("Meta Description", "")
    body_length_target = metadata.get("Body Length Target", "")
    output_language = normalize_output_language(metadata.get("Output Language", "chinese"))
    image_plan = data["image_plan"]
    h2s = data["h2s"]
    effective_profile = detect_profile(data) if profile == "auto" else profile
    length_metric = choose_length_metric(output_language)

    checks = []

    def add_check(name: str, passed: bool, details: str):
        checks.append({"name": name, "passed": passed, "details": details})

    primary_occurrences = len(re.findall(re.escape(primary), plain_text, re.IGNORECASE)) if primary else 0
    add_check("profile", True, f"Profile: {effective_profile}")
    add_check("primary_keyword_present", bool(primary), f"Primary keyword: {primary or 'missing'}")
    add_check("h1_contains_primary", bool(primary) and primary in article_title, f"H1: {article_title}")
    add_check("seo_title_contains_primary", bool(primary) and primary in seo_title, f"SEO title: {seo_title}")
    add_check("seo_title_length", len(seo_title) <= 60, f"SEO title length: {len(seo_title)}")
    add_check("h2_count", 4 <= len(h2s) <= 6, f"H2 count: {len(h2s)}")
    conclusion_h2s = [
        h2
        for h2 in h2s
        if re.fullmatch(
            r"(?:Conclusion(?:\s*\+\s*CTA)?|结语(?:与\s*CTA)?|結語(?:與\s*CTA)?|结论(?:与\s*CTA)?|結論(?:與\s*CTA)?)",
            h2,
            re.IGNORECASE,
        )
    ]
    add_check(
        "conclusion_heading_without_cta",
        bool(conclusion_h2s) and all("cta" not in h2.casefold() for h2 in conclusion_h2s),
        f"Conclusion heading: {conclusion_h2s[0] if conclusion_h2s else 'missing'}",
    )
    add_check("output_language", True, f"Output language: {output_language}; metric: {length_metric}")

    body_count = count_length_units(plain_text, length_metric)
    body_target = parse_length_target(body_length_target) if body_length_target else None
    if body_target is None:
        body_target = (1500, 1800) if length_metric == "cjk" else (1500, 1800)
        body_target_label = f"{body_target[0]}-{body_target[1]} (default {length_metric}s)"
    else:
        body_target_label = f"{body_target[0]}-{body_target[1]}"
    add_check(
        "body_length_target",
        body_target[0] <= body_count <= body_target[1],
        f"Body {length_metric} count: {body_count}; target: {body_target_label}",
    )

    intro_count = count_length_units(data["intro"], length_metric)
    intro_lower, intro_upper = (70, 220) if length_metric == "word" else (150, 260)
    add_check("intro_substantial", intro_lower <= intro_count <= intro_upper, f"Intro {length_metric} count: {intro_count}")

    conclusion_count = count_length_units(data["conclusion"], length_metric)
    conclusion_lower, conclusion_upper = (70, 220) if length_metric == "word" else (150, 260)
    add_check(
        "conclusion_substantial",
        conclusion_lower <= conclusion_count <= conclusion_upper,
        f"Conclusion {length_metric} count: {conclusion_count}",
    )

    add_check("image_plan_count", 6 <= len(image_plan) <= 10, f"Image plan count: {len(image_plan)}")
    normalized_alts = [re.sub(r"\s+", " ", item["alt"]).strip().casefold() for item in image_plan]
    unique_alts = bool(normalized_alts) and all(normalized_alts) and len(normalized_alts) == len(set(normalized_alts))
    primary_alt_count = (
        sum(primary.casefold() in item["alt"].casefold() for item in image_plan) if primary and image_plan else 0
    )
    max_primary_alts = min(2, len(image_plan))
    add_check("image_alt_unique", unique_alts, f"Unique non-empty alt texts: {len(set(normalized_alts))}/{len(normalized_alts)}")
    add_check(
        "image_alt_keyword_balance",
        bool(image_plan) and 1 <= primary_alt_count <= max_primary_alts,
        f"Exact primary keyword appears in {primary_alt_count} alt texts; target: 1-{max_primary_alts}",
    )

    stock_phrases = find_stock_ai_phrases(article_text)
    add_check(
        "no_stock_ai_phrases",
        not stock_phrases,
        "No stock AI phrases found" if not stock_phrases else f"Flagged: {', '.join(stock_phrases)}",
    )
    transition_starts = find_routine_transition_starts(article_text)
    add_check(
        "transition_variety",
        len(transition_starts) <= 2,
        f"Routine transition paragraph starts: {len(transition_starts)}"
        + (f" ({', '.join(transition_starts[:6])})" if transition_starts else ""),
    )
    duplicate_sentences = find_duplicate_sentences(article_text)
    add_check(
        "no_duplicate_sentences",
        not duplicate_sentences,
        "No repeated substantial sentences found"
        if not duplicate_sentences
        else f"Repeated sentence samples: {' | '.join(duplicate_sentences[:3])}",
    )
    keyword_frequency_limit = max(8, math.ceil(body_count / (120 if length_metric == "word" else 150)))
    add_check(
        "primary_keyword_natural_frequency",
        primary_occurrences <= keyword_frequency_limit,
        f"Primary keyword occurrences: {primary_occurrences}; maximum natural-use threshold: {keyword_frequency_limit}",
    )

    has_ugphone_value = heading_matches_any(
        h2s,
        [
            "How UgPhone Helps",
            "Why Choose UgPhone",
            "Why Use UgPhone",
            "为什么使用 UgPhone",
            "為什麼使用 UgPhone",
            "UgPhone 如何帮助",
            "UgPhone 如何幫助",
            "使用 UgPhone 的理由",
        ],
    )
    add_check("ugphone_value_section", has_ugphone_value, "UgPhone value section scan")

    if effective_profile == "game-guide":
        add_check(
            "core_topic_section",
            heading_matches_any(h2s, ["What is", "Que es", "Qué es", "O que e", "What Is", "什么是", "什麼是"]),
            "Game topic section scan",
        )
        add_check(
            "main_action_section",
            heading_matches_any(h2s, ["How to", "Guide", "Tips", "AFK", "Farm", "Como", "Cómo", "Guia", "Guía", "攻略", "挂机", "掛機", "如何", "教学", "教學"]),
            "Gameplay or action section scan",
        )
        add_check(
            "ugphone_tutorial_or_flow",
            heading_matches_any(h2s, ["UgPhone", "How to Use UgPhone", "Como usar UgPhone", "Cómo usar UgPhone", "使用 UgPhone", "使用UgPhone", "如何使用 UgPhone"]),
            "UgPhone game workflow scan",
        )
    else:
        add_check(
            "core_topic_section",
            heading_matches_any(h2s, ["What is", "Why", "Que es", "Qué es", "Por que", "Por qué", "为什么", "為什麼"]),
            "Product-tech topic section scan",
        )
        add_check(
            "main_action_section",
            heading_matches_any(h2s, ["Key Features", "How It Works", "Main Use Cases", "Step-by-Step Setup", "How to Use", "Caracteristicas", "Características", "Como funciona", "Cómo funciona", "Casos de uso", "使用方法"]),
            "Feature or workflow section scan",
        )
        add_check(
            "ugphone_tutorial_or_flow",
            heading_matches_any(h2s, ["UgPhone", "How to Use UgPhone", "Step-by-Step Setup", "Why Use UgPhone", "Como usar UgPhone", "Cómo usar UgPhone", "Por que usar UgPhone", "Por qué usar UgPhone", "使用 UgPhone"]),
            "UgPhone product-tech workflow scan",
        )

    add_check(
        "cta_present",
        bool(
            re.search(
                r"try ugphone|download|free|free trial|descarga|descargar|prueba gratis|prueba gratuita|baixar|teste gratis|teste gratuito|\u514d\u8d39\u4f53\u9a8c|\u514d\u8cbb\u8a66\u7528|\u7acb\u5373\u4e0b\u8f7d|\u7acb\u5373\u4e0b\u8f09|\u9a6c\u4e0a\u8bd5\u7528|\u99ac\u4e0a\u8a66\u7528",
                article_text,
                re.IGNORECASE,
            )
        ),
        "CTA phrase scan",
    )
    add_check("slug_format", bool(re.fullmatch(r"[a-z0-9-]+", slug)), f"Slug: {slug}")
    add_check("meta_description_length", 120 <= len(meta_desc) <= 160, f"Meta description length: {len(meta_desc)}")
    add_check("no_price_mentions", not contains_price_reference(article_text), "Price wording scan")
    add_check("no_competitor_mentions", not contains_competitor_reference(article_text), "Competitor wording scan")
    add_check("primary_occurrence_scan", primary_occurrences > 0, f"Primary keyword occurrences in body: {primary_occurrences}")

    return checks


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Validate an SEO article package against the selected checklist profile.")
    parser.add_argument("--article-package", required=True, type=Path, help="Markdown article package to validate.")
    parser.add_argument("--profile", choices=["auto", "game-guide", "product-tech"], default="auto", help="Validation profile.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of plain text.")
    args = parser.parse_args()

    data = parse_article_package(args.article_package.read_text(encoding="utf-8"))
    checks = validate(data, args.profile)
    passed = all(check["passed"] for check in checks)

    if args.json:
        print(json.dumps({"passed": passed, "checks": checks}, ensure_ascii=False, indent=2))
    else:
        print("PASS" if passed else "FAIL")
        for check in checks:
            status = "OK" if check["passed"] else "FAIL"
            print(f"[{status}] {check['name']}: {check['details']}")

    sys.exit(0 if passed else 1)


if __name__ == "__main__":
    main()
