from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path

from build_docx import (
    extract_source_images,
    get_language_pack,
    metadata_to_dict,
    parse_article_package,
)


ARTICLE_BODY_RE = re.compile(
    r"^## Article Body\s*$\n(?P<body>.*?)(?=^## Image Plan\s*$|\Z)",
    re.MULTILINE | re.DOTALL,
)
SOURCE_IMAGE_RE = re.compile(
    r"^\s*<!--\s*SOURCE_IMAGE\s*:\s*(\d+)\s*-->\s*$",
    re.IGNORECASE,
)
CONCLUSION_RE = re.compile(
    r"^##\s+(?:Conclusion(?:\s*\+\s*CTA)?|Conclusão|Conclusión|结语(?:与\s*CTA)?|結語(?:與\s*CTA)?|结论(?:与\s*CTA)?|結論(?:與\s*CTA)?|สรุป|Kesimpulan|Kết luận)\s*$",
    re.IGNORECASE,
)


def metadata_key(value: str) -> str:
    key = re.sub(r"[^a-z0-9]+", "_", value.strip().lower()).strip("_")
    return key or "field"


def yaml_value(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def markdown_alt(value: str) -> str:
    return value.replace("\\", "\\\\").replace("]", "\\]")


def extract_article_body(md_text: str) -> str:
    match = ARTICLE_BODY_RE.search(md_text)
    if not match:
        raise ValueError("Article package is missing a readable '## Article Body' section.")
    return match.group("body").strip()


def add_introduction_heading(article_body: str, heading_text: str) -> str:
    lines = article_body.splitlines()
    h1_index = next((index for index, line in enumerate(lines) if re.fullmatch(r"#\s+\S.*", line.strip())), None)
    if h1_index is None:
        raise ValueError("Article Body contains no H1 heading.")

    first_content_index = h1_index + 1
    while first_content_index < len(lines) and not lines[first_content_index].strip():
        first_content_index += 1
    if first_content_index < len(lines) and lines[first_content_index].strip().casefold() == f"## {heading_text}".casefold():
        return article_body

    return "\n".join(lines[: h1_index + 1] + ["", f"## {heading_text}"] + lines[h1_index + 1 :])


def marker_sequence(article_body: str) -> list[int]:
    markers = []
    for line in article_body.splitlines():
        match = SOURCE_IMAGE_RE.fullmatch(line)
        if match:
            markers.append(int(match.group(1)))
    return markers


def render_frontmatter(article_title: str, metadata) -> str:
    rows = [("title", article_title)]
    seen = {"title"}
    for key, value in metadata:
        normalized = metadata_key(key)
        if normalized in seen:
            suffix = 2
            candidate = f"{normalized}_{suffix}"
            while candidate in seen:
                suffix += 1
                candidate = f"{normalized}_{suffix}"
            normalized = candidate
        seen.add(normalized)
        rows.append((normalized, value))
    return "---\n" + "\n".join(f"{key}: {yaml_value(value)}" for key, value in rows) + "\n---"


def build_markdown(
    article_package: Path,
    output_path: Path,
    source_docx: Path | None = None,
    assets_dir: Path | None = None,
) -> tuple[Path, Path | None]:
    md_text = article_package.read_text(encoding="utf-8")
    article_title, metadata, _, image_plan = parse_article_package(md_text)
    if not article_title:
        raise ValueError("Article package is missing the Article Body H1 title.")

    body = extract_article_body(md_text)
    metadata_map = metadata_to_dict(metadata)
    labels = get_language_pack(metadata_map.get("Output Language", "english"))
    body = add_introduction_heading(body, labels["introduction"])
    body = "\n".join(
        f"## {labels['conclusion']}" if CONCLUSION_RE.fullmatch(line.strip()) else line
        for line in body.splitlines()
    )

    source_images = extract_source_images(source_docx) if source_docx else []
    markers = marker_sequence(body)
    if source_images:
        expected = list(range(1, len(source_images) + 1))
        if markers != expected:
            raise ValueError(
                "Markdown source image placement must preserve every image exactly once and in order. "
                f"Expected markers {expected}, found {markers}."
            )
    elif markers:
        raise ValueError("Article package contains SOURCE_IMAGE markers, but no source DOCX was provided.")

    image_alt_by_index = {
        item["source_image"]: item["alt"]
        for item in image_plan
        if item["source_image"] is not None and item["alt"]
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    resolved_assets_dir = None
    image_links = {}
    if source_images:
        resolved_assets_dir = assets_dir or output_path.parent / f"{output_path.stem}_assets"
        resolved_assets_dir.mkdir(parents=True, exist_ok=True)
        for image in source_images:
            suffix = Path(image["name"]).suffix.lower() or ".png"
            target = resolved_assets_dir / f"source-image-{image['index']:02d}{suffix}"
            target.write_bytes(image["blob"])
            relative = Path(os.path.relpath(target, output_path.parent)).as_posix()
            alt = image_alt_by_index.get(image["index"], f"Source image {image['index']}")
            image_links[image["index"]] = f"![{markdown_alt(alt)}](<{relative}>)"

    rendered_lines = []
    for line in body.splitlines():
        marker = SOURCE_IMAGE_RE.fullmatch(line)
        if marker:
            rendered_lines.append(image_links[int(marker.group(1))])
        else:
            rendered_lines.append(line)
    rendered_body = "\n".join(rendered_lines).strip()

    output = f"{render_frontmatter(article_title, metadata)}\n\n{rendered_body}\n"
    output_path.write_text(output, encoding="utf-8", newline="\n")
    verify_markdown(output_path, source_images, resolved_assets_dir, labels)
    return output_path, resolved_assets_dir


def verify_markdown(output_path: Path, source_images, assets_dir: Path | None, labels: dict) -> None:
    if not output_path.exists() or output_path.stat().st_size == 0:
        raise ValueError(f"Generated Markdown is missing or empty: {output_path}")
    text = output_path.read_text(encoding="utf-8")
    if "## Image Plan" in text or "SOURCE_IMAGE" in text:
        raise ValueError("Generated Markdown exposes internal Image Plan data or source markers.")
    if not re.search(r"^#\s+\S", text, re.MULTILINE):
        raise ValueError("Generated Markdown contains no H1 heading.")
    if not re.search(rf"^##\s+{re.escape(labels['introduction'])}\s*$", text, re.MULTILINE):
        raise ValueError("Generated Markdown is missing the language-appropriate introduction heading.")
    if not re.search(rf"^##\s+{re.escape(labels['conclusion'])}\s*$", text, re.MULTILINE):
        raise ValueError("Generated Markdown is missing the language-appropriate conclusion heading.")
    if source_images:
        if assets_dir is None:
            raise ValueError("Generated Markdown is missing its image assets directory.")
        linked_images = re.findall(r"^!\[.*?\]\(<(.+?)>\)\s*$", text, re.MULTILINE)
        if len(linked_images) != len(source_images):
            raise ValueError(
                "Generated Markdown image link count does not match the source image count. "
                f"Expected {len(source_images)}, found {len(linked_images)}."
            )
        expected_hashes = [hashlib.sha256(image["blob"]).hexdigest() for image in source_images]
        built_hashes = []
        for link in linked_images:
            asset_path = (output_path.parent / Path(link)).resolve()
            if not asset_path.exists():
                raise ValueError(f"Generated Markdown image asset is missing: {asset_path}")
            built_hashes.append(hashlib.sha256(asset_path.read_bytes()).hexdigest())
        if built_hashes != expected_hashes:
            raise ValueError("Markdown image assets are missing, altered, or out of order.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build a reader-facing Markdown article and optional image assets from an SEO article package."
    )
    parser.add_argument("--article-package", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--source-docx", type=Path)
    parser.add_argument("--assets-dir", type=Path)
    args = parser.parse_args()

    output_path, assets_dir = build_markdown(
        args.article_package,
        args.out,
        source_docx=args.source_docx,
        assets_dir=args.assets_dir,
    )
    print(output_path)
    if assets_dir:
        print(assets_dir)


if __name__ == "__main__":
    main()
