# DOCX Delivery

Use this reference when the user wants the rewritten article as a Word document.

## Default behavior

- Treat the SEO article package as the source of truth.
- Build a `.docx` plus a reader-facing `.md` unless the user explicitly prefers one format only.
- Preserve source screenshots when a source `.docx` is available.
- Keep every source image in its corresponding rewritten section and preserve the original image order exactly.
- Prefer stable inline image placement over floating layouts.
- Generate and verify `.docx` files entirely with the bundled Python scripts.
- If `SEO Metadata` includes `Output Language`, keep helper labels and document chrome aligned with that language when practical.

## Workflow

1. Generate the normal article package in Markdown with these sections:
   - `Title`
   - `SEO Metadata`
   - `Article Body`
   - `Image Plan`
2. Save that package to a temporary `.md` file.
3. If the source contains images, inspect its exact text-image order first:

```bash
python scripts/inspect_source_docx.py --source-docx source.docx --out source-sequence.md
```

4. Use the surrounding source text in `source-sequence.md` to place standalone markers in the rewritten `Article Body`:

```markdown
## Matching rewritten section

Paragraph explaining the same feature or step shown by the source image.

<!-- SOURCE_IMAGE:1 -->
```

5. Include `Source Image: 1` in the matching `Image Plan` item so its alt text is written into the Word image metadata.
6. Run `scripts/build_docx.py`. If the source contains images, pass `--source-docx`.
7. Run `scripts/build_markdown.py` with the same article package. Pass `--source-docx` so the Markdown copy receives extracted image assets and relative links.
8. Require both builders' post-save structural verification to pass before delivery.
9. For Traditional Chinese, English, Portuguese, Spanish, Thai, Indonesian, or Vietnamese output, set `Output Language` in `SEO Metadata` before building so headings, metadata labels, and captions stay consistent.

Keep `Image Plan` internal throughout this workflow. The builder reads it for validation and image metadata but does not place it in the final Word document.

Follow [markdown-delivery.md](markdown-delivery.md) for the paired Markdown file. Do not give the internal article package to the user as a substitute for the reader-facing Markdown output.

## Script usage

Text-only:

```bash
python scripts/build_docx.py --article-package article.md --out article.docx
```

Preserve source screenshots:

```bash
python scripts/build_docx.py --article-package article.md --source-docx source.docx --out article.docx
```

## What the script does

- Applies a compact, guide-friendly Word layout.
- Writes a title block and SEO metadata table.
- Converts the `Article Body` Markdown into headings, paragraphs, bullets, and numbered steps.
- Reads the `Image Plan` for validation, source-image mapping, and alt text without rendering it in the final document.
- Inserts source screenshots exactly where their `SOURCE_IMAGE` markers appear.
- Rejects missing, duplicated, swapped, or out-of-range source-image markers.
- Applies mapped image-plan alt text to the corresponding Word image metadata.
- Normalizes a conclusion heading such as `Conclusion + CTA`, `结语与 CTA`, or `結語與 CTA` to a clean language-appropriate conclusion title while keeping the CTA paragraph.
- Reopens the generated `.docx` and verifies its image count and image binary order before reporting success.

## Guardrails

- Preserve every source image unless the user explicitly requests that specific images be removed.
- Never reorder images during rewriting. Keep markers in the exact original sequence `1, 2, 3, ...`.
- Never distribute images evenly by section and never place unmatched images in an appendix.
- Use the source text surrounding each marker to determine the matching rewritten section; do not map images from filenames alone.
- If the new SEO structure conflicts with the source image order, revise or merge sections so topic relevance and image order are both preserved.
- If the article package does not parse cleanly, fix the package instead of hand-editing the script output in Word.
- Treat any post-save structural verification failure as a build failure and fix the article package or builder before delivery.
- Never append an Image Plan heading, table, checklist, or image-rule block to the final `.docx` unless the user explicitly requests that internal data.
