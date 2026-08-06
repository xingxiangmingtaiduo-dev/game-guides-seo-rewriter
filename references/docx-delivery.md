# DOCX Delivery

Use this reference when the user wants the rewritten article as a Word document.

## Default behavior

- Treat the SEO article package as the source of truth.
- Build a `.docx` unless the user explicitly prefers Markdown only.
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
7. Require the builder's post-save structural verification to pass before delivery.
8. For English, Spanish, or Portuguese output, set `Output Language` in `SEO Metadata` before building so the helper headings and captions stay consistent.

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
- Converts the `Image Plan` into a table.
- Inserts source screenshots exactly where their `SOURCE_IMAGE` markers appear.
- Rejects missing, duplicated, swapped, or out-of-range source-image markers.
- Applies mapped image-plan alt text to the corresponding Word image metadata.
- Reopens the generated `.docx` and verifies its image count and image binary order before reporting success.

## Guardrails

- Preserve every source image unless the user explicitly requests that specific images be removed.
- Never reorder images during rewriting. Keep markers in the exact original sequence `1, 2, 3, ...`.
- Never distribute images evenly by section and never place unmatched images in an appendix.
- Use the source text surrounding each marker to determine the matching rewritten section; do not map images from filenames alone.
- If the new SEO structure conflicts with the source image order, revise or merge sections so topic relevance and image order are both preserved.
- If the article package does not parse cleanly, fix the package instead of hand-editing the script output in Word.
- Treat any post-save structural verification failure as a build failure and fix the article package or builder before delivery.
