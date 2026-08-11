# Markdown Delivery

Use this reference when the user wants Markdown or whenever a `.docx` article is delivered. The default DOCX workflow now produces a paired reader-facing `.md` file.

## Output rules

- Preserve the article's Markdown structure: H1, H2, H3, numbered steps, bullets, links, and meaningful `**bold emphasis**`.
- Keep SEO metadata as YAML frontmatter.
- Include the reader-facing article body only. Never expose `Image Plan`, `SOURCE_IMAGE` markers, internal QA notes, or image rules.
- Add the introduction heading and keep both introduction and conclusion headings natural for the output language, such as `Introdução` and `Conclusão` in Portuguese.
- When a source DOCX contains images, extract every image to a sibling `<markdown-stem>_assets` folder and replace each source marker with a relative Markdown image link.
- Preserve source image count, binary content, semantic placement, and original order exactly.
- Use descriptive image alt text from `Image Plan`; do not repeat the exact primary keyword in every alt.

## Script usage

Text-only Markdown:

```bash
python scripts/build_markdown.py --article-package article.md --out article-public.md
```

Markdown with source images:

```bash
python scripts/build_markdown.py --article-package article.md --source-docx source.docx --out article-public.md
```

The script creates `<article-public>_assets` beside the Markdown file unless `--assets-dir` is provided.

## Verification

Require the script's post-save verification to pass. Confirm that:

- the Markdown file contains an H1, a language-appropriate introduction H2, and the expected article H2 structure;
- Markdown emphasis such as `**key action**` remains intact;
- no internal Image Plan or source markers remain;
- image links equal the source image count;
- extracted image hashes match the source images in exact order.

Deliver the `.md` file together with its assets folder. When a DOCX was requested, deliver both `.docx` and `.md` unless the user explicitly asks for Word only.
