---
name: game-guides-seo-rewriter
description: Rewrite game guides, reviews, and UgPhone-related source documents into clear, publish-ready SEO articles. Use for multilingual Markdown or Word output when source images and article structure must be preserved.
---

# Game Guides SEO Rewriter

Use the source as factual material and produce a reader-first article. Keep the writing direct, the layout simple, and one search intent per article.

## Required format confirmation

For every new request to generate an SEO article from a source document, ask this question first and stop:

```text
是否按照以下默认格式生成？

请用 SEO Docx Rewriter 处理这篇文档：

1. 输出 SEO 版 DOCX，同时输出为繁体中文、英语、葡萄牙语、西班牙语、泰语、印尼语和越南语，每种语言分别生成 DOCX
2. 保留原文图片
3. 正文控制在 500-600 字
4. 主关键词为“XXX”（可以不写）
5. 结尾保留 CTA

如果是，请回复“继续”；如果不是，请告诉我你想要生成的格式。
```

Do not inspect the source document, draft, translate, validate, or create files before the user replies. Treat `继续` as approval of all five defaults. Treat any other response that specifies languages, format, length, image policy, keyword, or CTA as the approved custom format and proceed without asking the same confirmation again. Ask this confirmation again only when the user starts a new source-article generation request.

Do not use this confirmation for questions, status checks, existing-output reviews, bug reports, or requests to update this Skill.

## Before drafting

- Read `references/human-writing-style.md` and `references/sop-distilled.md` for game articles.
- Read `references/product-tech-seo.md` for product or cloud-phone topics.
- Read `references/docx-delivery.md` when a Word document or source screenshots are requested.
- Read `references/markdown-delivery.md` when Markdown is requested or paired with Word output.
- Distill the topic, audience, search intent, supported facts, primary keyword, and 2-5 related keywords.
- Do not invent mechanics, rates, testing experience, quotes, or community claims.

## Article package

Create one internal Markdown package with exactly these sections:

```markdown
# Title

## SEO Metadata
- Slug: ...
- SEO Title: ...
- Primary Keyword: ...
- Long-tail Keywords: ...
- Meta Description: ...
- Tags: ...
- Output Language: ...
- Body Length Target: ...

## Article Body
# H1

## Introduction or the natural localized equivalent

正文段落。

## What is [Game Name]? or the natural localized equivalent

正文段落。
```

For game guides, include the game introduction, the main gameplay/resource section, common problems or FAQ, a natural UgPhone value section, a UgPhone setup section, and a short conclusion with the CTA in the final paragraph.

## Markdown invariants

These are hard requirements. If any fails, stop and repair the package before building files:

- Every heading occupies its own line. Leave one blank line after every heading.
- Every paragraph occupies its own block. Never concatenate a translated heading and the following paragraph.
- Preserve Markdown markers such as `#`, `##`, numbered lists, bold text, and links.
- Never translate or rewrite the package by replacing text in a way that can remove line breaks. If an external translation step is used, normalize and inspect the resulting Markdown before continuing.
- A source-image marker is standalone and appears exactly once: `<!-- SOURCE_IMAGE:1 -->`.
- Place each marker immediately after the paragraph describing that screenshot. Preserve source order, but do not collect markers at the end of a section or append them after the conclusion.
- Keep the `Image Plan` internal. It must not appear in the public Markdown or the visible Word article.
- Use localized title, metadata, headings, captions, CTA, and community text. Do not fall back to English or Chinese in another language's public article.

## Source images

When the source is a `.docx`:

1. Run `scripts/inspect_source_docx.py` and read the text-image sequence.
2. Put all source-image markers into the matching rewritten sections in the same order.
3. Add `Source Image: N` to each matching Image Plan entry.
4. Build with `scripts/build_docx.py --source-docx ...` and `scripts/build_markdown.py --source-docx ...`.
5. Require both builders' post-save checks to pass. If an image is misplaced, fix the package; do not append an image appendix as a workaround.

## Validation and delivery

- Run `scripts/validate_article_package.py` before building.
- Reject packages with merged heading/body lines, missing blank lines, mixed-language public text, duplicate or out-of-order source markers, or markers grouped away from their related text.
- Deliver the requested `.docx` and a reader-facing `.md` by default when Word output is requested. Include the extracted image assets beside the Markdown file.
- Keep the final response concise and link the actual output files.

Do not modify this Skill during ordinary article generation. Change it only when a reproducible workflow defect is identified, then validate the change before using it for a new article.
