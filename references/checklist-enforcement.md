# Checklist Enforcement

Use this reference when the draft needs to satisfy the final SEO article checklist before delivery.

The skill supports two main profiles:

- `game-guide`
- `product-tech`

## Required checks

The final package should pass these shared rules unless the user explicitly asks for an exception:

- One primary keyword for the full page.
- H1 and SEO title both contain the primary keyword.
- SEO title stays within 60 characters when possible.
- Use 4 to 6 clear H2 sections in the article body.
- Total body length should stay in the configured target band.
- If `SEO Metadata` contains `Body Length Target`, use that range instead of the default.
- If no explicit range is set, use the `1500-1800` target band by default.
- If `SEO Metadata` contains `Output Language`, the validator should use the matching length metric automatically.
- Supported delivery languages are Traditional Chinese, English, Portuguese, Spanish, Thai, Indonesian, and Vietnamese. Traditional Chinese uses CJK-character length, Thai uses Thai-script character length, and the other supported Latin-script languages use Unicode-aware word length.
- Introduction and conclusion should both be substantial. For Chinese, roughly 150-260 CJK characters is a useful validation band. For Thai, use a shorter 90-260 Thai-script-character band when the total requested article is only 500-600 Thai characters so the opening and closing do not consume the whole brief.
- Plan 6 to 10 images by default. A source document with more than 10 required images may exceed this range only when the plan maps every preserved image as one complete consecutive `Source Image: 1..N` sequence.
- Every image alt text should describe the image and be unique. Only one or two relevant alt texts should normally contain the exact primary keyword.
- Include UgPhone pain-point analysis and at least one practical value or step-by-step section.
- End with a clear CTA.
- Keep the conclusion heading clean: use `Conclusion`, `结语`, `結語`, or the natural output-language equivalent without adding `CTA` to the heading.
- Slug should be lowercase with hyphens.
- Meta description should stay in the `120-160` character band.
- Avoid competitor comparisons and price mentions.
- Keep the Markdown structure valid and predictable.
- Avoid stock AI phrases, duplicated sentences, repetitive section previews and recaps, excessive exact-match keywords, and mechanical transition chains.
- Do not fabricate first-person experience or anecdotes as a shortcut to sounding human.
- Deliver a reader-facing Markdown copy with preserved headings, emphasis, lists, and image positions. Keep Image Plan and source markers private.
- Keep the editorial CTA in the conclusion, then let the public builders append the localized Discord invitation after it. This generated block is excluded from body-length validation.

## Profile-specific expectations

### `game-guide`

- Keep game search intent explicit.
- Include a gameplay or progression H2.
- Include a UgPhone use or AFK workflow section.

### `product-tech`

- Keep the article anchored in a real workflow, feature, troubleshooting case, or use case.
- Include either a `How to Use UgPhone...` section or a strong `Why Use UgPhone...` section.
- Do not force gameplay-specific sections such as `What is [Game Name]?`.

## Validation workflow

1. Draft the article package.
2. Run:

```bash
python scripts/validate_article_package.py --article-package article.md --profile auto
```

3. Read the failing checks first.
4. Revise the draft.
5. Re-run until the required checks pass.

## How to fix common failures

### Body too long

- Cut repeated explanations before cutting unique strategy.
- Shorten the introduction first if it is bloated.
- Compress FAQ answers to direct, practical responses.
- Remove duplicated UgPhone framing if the same point appears in multiple sections.
- If the brief asked you to stay close to the source length, add `Body Length Target` to metadata and validate against that narrower range.

### Body too short

- Add more actionable gameplay or workflow detail in the main guide section.
- Expand FAQ only with real search-intent questions.
- Strengthen the UgPhone tutorial with concrete steps instead of generic benefits.

### Primary keyword missing from H1 or SEO title

- Rewrite the H1 and title immediately.
- Do not rely on close variants when the exact primary keyword was already chosen.

### Too many or too few H2 sections

- Merge overlapping H2 sections or split overloaded ones.
- Keep the structure easy to scan instead of adding decorative headings.

### Image plan failure

- Expand the image plan to 6 to 10 entries unless the user approved another range.
- Describe each image accurately and keep alt text unique.
- Put the exact primary keyword into only one or two relevant alt texts; use natural variants elsewhere.

### Human-style failure

- Replace flagged stock phrases with a concrete fact, action, constraint, or consequence.
- Delete repeated introductions to sections and summary sentences that add no new information.
- Break a repeated paragraph pattern by combining connected ideas, shortening obvious points, or expanding only the useful detail.
- Reduce exact-match keyword repetition after the topic is established.
- Remove duplicate sentences and repeated UgPhone benefit statements.

### Final DOCX contains an Image Plan

- Keep Image Plan entries in the intermediate Markdown package for validation, alt text, and source-image mapping.
- Do not render the Image Plan heading or table in the final Word document unless the user explicitly requests it.

### Final Markdown exposes internal data or loses formatting

- Build the public file with `scripts/build_markdown.py`; do not copy the internal article package directly.
- Preserve H1/H2, meaningful `**bold emphasis**`, lists, and links.
- Confirm that the public Markdown includes language-appropriate introduction and conclusion headings.
- Replace every source marker with a relative image link and extract images to the paired assets folder.
- Reject output containing `Image Plan`, `SOURCE_IMAGE`, missing image links, or altered image order.
- Confirm that the final Markdown invitation uses `FhSaQfq6rJ` only for Portuguese and Spanish, and `Agkk96vcfA` for the other supported languages.

### Description too short or too long

- Keep the description focused on what the reader gets from the article.
- Remove filler adjectives before cutting practical nouns and verbs.

### Wrong profile assumptions

- If the article is about a product feature, tutorial, workflow, or troubleshooting topic, validate it with `product-tech`.
- If the article is about a game's progression, events, AFK farming, beginner help, or FAQs, validate it with `game-guide`.

### Wrong language assumptions

- If the source is Chinese but the requested output is English, Spanish, or another language, write the article in the requested language rather than translating section by section mechanically.
- Add `Output Language` to metadata so the validator can use word-based checks for Latin-script outputs.
- Localize the introduction and conclusion headings, SEO document labels, image captions, keywords, and CTA in the requested language. Do not leave English interface text around an otherwise translated article.

## Notes on metrics

- The validator measures Chinese-heavy drafts by CJK character count in the article body as the closest deterministic proxy to the `1500-1800` requirement.
- If `Body Length Target` is present, the validator uses that range as the deterministic proxy instead.
- If the user asks for a very different article size, treat that request as an intentional override and record it in metadata.
