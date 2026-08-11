---
name: game-guides-seo-rewriter
description: Rewrite source notes, drafts, briefs, outlines, research, or existing documents into natural, editor-quality UgPhone SEO articles that avoid formulaic AI prose. Use when Codex must turn game reviews, game guides, product explainers, feature tutorials, cloud-phone how-to articles, troubleshooting notes, or other product-tech materials into publish-ready SEO content with a human voice, keyword planning, SEO metadata, structured H1/H2 sections, natural UgPhone integration, FAQ or tutorial sections, CTA, image suggestions, reader-facing Markdown with preserved formatting and image assets, or a paired Word `.docx` and `.md` delivery that preserves source images, including multilingual output.
---

# Game Guides SEO Rewriter

## Overview

Turn raw source material into a player-first SEO game guide that solves a real player problem before introducing UgPhone as the technical solution. Produce a clean article package, not just body copy: include metadata, keyword framing, structure, and publishing notes when needed.

Always read [references/human-writing-style.md](references/human-writing-style.md) before drafting or revising an article. Read [references/sop-distilled.md](references/sop-distilled.md) when you need the detailed game-guide rules, title formulas, topic taxonomy, or QA checklist for game content. Read [references/product-tech-seo.md](references/product-tech-seo.md) when the source material is about UgPhone, cloud phones, product features, tutorials, use cases, troubleshooting, or other technology topics. Read [references/checklist-enforcement.md](references/checklist-enforcement.md) when you need to enforce the final article checklist or diagnose why a draft failed. Read [references/backend-publishing.md](references/backend-publishing.md) only when the user wants UgPhone CMS publishing notes. Read [references/docx-delivery.md](references/docx-delivery.md) and [references/markdown-delivery.md](references/markdown-delivery.md) when the user wants a `.docx`, a Markdown deliverable, or source screenshots carried into the rewritten output.

## Run The Workflow

### 1. Distill the source

- Extract the topic, platform or product context, target language, reader pain point, and any factual claims that must be preserved.
- If the source language and output language differ, preserve the meaning and SEO intent rather than translating line by line.
- Identify the article mode before drafting:
  - `game-guide` for game reviews, gameplay notes, leveling, AFK, events, codes, or game FAQs.
  - `product-tech` for UgPhone features, cloud phone tutorials, use cases, troubleshooting articles, product workflows, or technology explainers.
- Identify the search intent within that mode.
- Keep source-supported facts. Do not invent patch details, rates, or mechanics that the source does not support.
- Ask for a missing detail only when that gap would materially change the article.

### 2. Lock the SEO angle

- Choose exactly one primary keyword for the page.
- Add 2 to 5 tightly aligned secondary or long-tail keywords.
- If the user provides many candidate keywords, collapse them into 1 primary keyword plus supporting keywords.
- Use keywords in the output language unless the user explicitly wants bilingual or mixed-language SEO.
- Prefer titles that combine the core topic, high-intent keyword, year when useful, and a concrete benefit.
- Avoid vague low-intent titles such as `Game Introduction` or `Play XXX`.

### 3. Draft the article

- Write an H1 that contains the primary keyword.
- Use Markdown formatting deliberately: keep the H1/H2 hierarchy, use lists for real steps or choices, and apply `**bold emphasis**` to a small number of key actions, interface labels, or warnings.
- Write an introduction of about 200 words that explains the topic, the reader problem, and what the article will solve. Do not lead with hard selling.
- For `game-guide` mode:
  - Add `## What is [Game Name]?`
  - Add one main `## How to ...` gameplay section.
  - Add `## Common Problems` or `## FAQ`.
  - Add `## How UgPhone Helps` or `## Why Choose UgPhone for [Game Name] AFK Farming?`.
  - Add `## How to Use UgPhone with [Game Name]`.
- For `product-tech` mode:
  - Add `## What is [Feature/Product/Workflow]?` or `## Why [Topic] Matters?`
  - Add `## Key Features`, `## How It Works`, or `## Main Use Cases` depending on the topic.
  - Add `## Common Problems`, `## FAQ`, or `## Troubleshooting` when useful.
  - Add `## How to Use UgPhone for [Task]` or `## Step-by-Step Setup` when the topic is procedural.
  - Add `## Why Use UgPhone for [Scenario]?` when the topic is value-led rather than procedural.
- End with a conclusion whose heading is only `Conclusion` or the natural equivalent in the output language. Put a clear CTA in the final paragraph, never in the heading.

### 4. Run a human-voice revision

- Treat the first draft as raw material. Revise it once for editorial voice before validation.
- Ground paragraphs in source-supported details, actual player decisions, concrete workflow friction, or observable outcomes.
- Delete meta-writing such as `in this comprehensive guide`, `this article will explore`, and repeated section previews.
- Vary sentence and paragraph rhythm. Do not make every paragraph follow the same claim-explanation-summary pattern.
- Use direct transitions or no transition when the logic is already clear. Avoid chains of `Furthermore`, `Moreover`, `Additionally`, or their translated equivalents.
- Keep useful nuance and limitations. Do not make every feature sound effortless, revolutionary, seamless, or suitable for everyone.
- Never invent first-person testing, personal experience, quotations, community consensus, or anecdotes to simulate authenticity.
- Use the exact primary keyword selectively. Prefer pronouns, game or feature names, and natural variants once the topic is clear.
- Write image alt text for the actual image. Use the exact primary keyword in only a small number of relevant alt texts instead of every entry.
- Make the conclusion short and decisive. Do not repeat every H2 in summary form before the CTA.

### 5. Keep the brand insertion natural

- Lead with player value, not product marketing.
- For game articles, use UgPhone to solve concrete pain points such as heat, battery drain, disconnects, device limits, or multi-instance farming.
- For product-tech articles, use UgPhone to solve concrete workflow pains such as device constraints, multi-tasking limits, remote access, automation friction, or account management overhead.
- Avoid unsupported superlatives such as `best`, `number one`, or `strongest`.
- Do not mention competitors or pricing unless the user explicitly asks and provides approved language.

### 6. Package the deliverable

- Obey the user's requested body-length range first.
- If the user gives a target range, include `Body Length Target` in `SEO Metadata` so the validator can enforce it.
- If the user asks for a different output language, include `Output Language` in `SEO Metadata`.
- If the user wants the rewrite to stay close to the source article's scale, preserve that scale instead of expanding automatically.
- If no length guidance exists, default to 1500 to 1800 words for long-form SEO pieces.
- Provide SEO metadata: slug or URL, SEO title, primary and long-tail keywords, meta description, and tags.
- Suggest image placements with descriptive, non-duplicated alt text. Use the exact primary keyword in one or two high-value alt texts when relevant; use natural variants elsewhere.
- If the output is meant for the UgPhone CMS, follow [references/backend-publishing.md](references/backend-publishing.md) for link syntax and upload field rules.
- Always keep the validated article package as the internal Markdown source of truth.
- Build a reader-facing Markdown copy with `scripts/build_markdown.py`; preserve headings, emphasis, lists, image placement, and SEO metadata while removing internal Image Plan data.
- If the user asks for a Word document, deliver paired `.docx` and `.md` files by default unless the user explicitly requests Word only.

### 7. Build `.docx` and reader-facing Markdown output

- Default to a `.docx` deliverable when the user explicitly asks for Word output, a downloadable document, or a file they can review visually.
- When building a `.docx`, also build a reader-facing `.md` version by default.
- Keep the article package as an intermediate artifact: `Title`, `SEO Metadata`, `Article Body`, and `Image Plan`.
- Treat `Image Plan` as internal build and validation data. Never render the Image Plan heading, table, or entries in the final `.docx` unless the user explicitly asks to see them.
- If a source `.docx` exists and contains screenshots, preserve those screenshots in the new document unless the user asks for a clean text-only version.
- Before rewriting a source `.docx` with images, run `scripts/inspect_source_docx.py --source-docx <input.docx> --out <source-sequence.md>` and use the report to understand which text and section surrounds each image.
- Insert every preserved image into `Article Body` with a standalone marker such as `<!-- SOURCE_IMAGE:1 -->` at the exact semantic position where it belongs in the rewritten section.
- Preserve the source image sequence exactly. Markers must appear once each as `1, 2, 3, ...` with no omissions, duplicates, swaps, or appendix fallback.
- Keep related source content and its image together when restructuring headings. If a proposed section order would reverse the original image order, adjust the article structure instead of moving the images out of sequence.
- Use `scripts/build_docx.py --article-package <package.md> --out <output.docx>` for text-only output.
- Add `--source-docx <input.docx>` to carry source images into the new document.
- Use `scripts/build_markdown.py --article-package <package.md> --out <output.md>` for reader-facing Markdown.
- Add `--source-docx <input.docx>` to the Markdown command to extract all source images into a sibling `<output-stem>_assets` folder and replace source markers with relative image links.
- In each matching `Image Plan` entry, add `Source Image: <number>` so the builder can apply the planned alt text to that source image.
- Treat image-marker validation failures as rewrite failures. Fix the article package instead of allowing automatic distribution or moving unused images to an appendix.
- Treat the script output as the default Word deliverable.
- Keep the Word deliverable reader-facing: include the title block, SEO metadata, article body, inline source images, and captions; omit the internal Image Plan section entirely.
- Keep the Markdown deliverable reader-facing: use YAML frontmatter for SEO metadata, add the language-appropriate introduction heading, preserve the remaining H1/H2 structure, `**bold emphasis**`, lists, and links, and omit the internal Image Plan entirely.
- Use only the bundled Python DOCX and Markdown scripts for generation and verification.
- Require both builders' post-save structural verification to pass before delivery.

### 8. Enforce the final checklist before shipping

- Save the article package to a temporary `.md` file before final delivery.
- Run `scripts/validate_article_package.py --article-package <package.md> --profile <game-guide|product-tech|auto>`.
- If `SEO Metadata` includes `Body Length Target`, expect the validator to use that range instead of the long-form default.
- If `SEO Metadata` includes `Output Language`, expect the validator to switch between Chinese-style length checks and word-based checks automatically.
- If the validator reports failures, revise the article and run it again until all required checks pass or until the user explicitly accepts an exception.
- Treat a length failure as a rewrite task, not as a reporting-only task. Compress the introduction, repeated explanations, and FAQ answers first before cutting the main actionable guide.
- Treat human-style failures as rewrite tasks. Remove flagged stock phrases, duplicate sentences, keyword stuffing, repetitive transitions, and empty recap paragraphs before delivery.
- Treat image-count failures as planning failures. Add or remove planned images so the package lands in the target range.
- Before delivery, confirm that source-image markers match the complete source sequence and that each marker sits inside the section discussing the same topic as its surrounding source text.
- Reopen the generated Markdown and confirm that it contains no `Image Plan` or `SOURCE_IMAGE`, that formatting markers remain intact, and that every extracted image hash matches the source in exact order.
- Do not claim compliance from memory. Use the validator output.

## Return The Result In This Format

- `Title`
- `SEO Metadata`
- `Article Body`
- `Image Plan` as an internal artifact; omit it from the final `.docx` and user-facing response unless requested.
- `Publishing Notes` only when the user asks for backend-ready output.
- `Docx Deliverable` when the user asks for a Word file.
- `Markdown Deliverable` for every article delivery unless the user explicitly declines it.

## Watch For Common Failure Modes

- Fix keyword drift. Do not let multiple unrelated primary intents compete on one page.
- Fix hard-sell openings. The first section must satisfy search intent before product mention.
- Replace tables with bullets, screenshots, or image instructions when the destination is the UgPhone CMS.
- Remove emojis or unsupported special characters if the article is going into the current CMS.
- Do not expand a concise source into a longer article unless the brief actually asks for expansion.
- Do not keep Chinese keywords as the primary keyword when the requested output is English, Spanish, or another target language.
- Resolve source conflicts explicitly. The source SOP mentions both `3-5` and `6-10` images; default to `3-5` high-value horizontal images unless the brief or publishing team asks for a denser guide.
- Do not claim pixel-level visual inspection. Report only the structural checks actually performed by the bundled DOCX workflow.
- Do not deliver the internal article package as the public Markdown file. Build the reader-facing copy so Image Plan and QA markers remain private.
