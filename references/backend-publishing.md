# UgPhone Backend Publishing Notes

Use this reference only when the user wants output that is ready for the current UgPhone blog backend.

## Prepare the article package

Return these fields alongside the article body:

- `Type`
- `Language or version`
- `English name / slug`
- `Tags`
- `Title`
- `Keywords`
- `Description`
- `Publish date`
- `Author`
- `Read count suggestion`
- `Thumbnail suggestion`

## Fill the backend fields this way

- Set the content type according to the article family:
  - game-guide category for game-guide content
  - cloud-phone, product-news, or product-tutorial category for product-tech content, following the current editorial taxonomy
- Match the language or version field to the article language.
- Write the `English name` as lowercase words joined by hyphens because it becomes part of the URL.
- Keep tags aligned with the article topic plus the usual UgPhone categories.
- Use the article title as the backend title.
- Use the SEO keyword cluster as backend keywords.
- Use the meta description as backend description.
- Use the current publish time unless the editorial calendar says otherwise.
- Use `ugphone` as the author unless the team provides another name.
- Treat read count as a seed number, not a performance metric.

## Respect current CMS formatting constraints

- Write links in the CMS-safe Markdown format `*++[text](url)++*`.
- Avoid regular tables in article body copy because the CMS may render them poorly.
- Convert tables into bullets, screenshots, or styled images when the content must stay tabular.
- Leave a blank line before embedded video code if the surrounding text starts rendering incorrectly.
- Avoid emojis and unsupported special characters because they can trigger publishing errors.

## Use these guardrails for publishing status

- Do not set a future publish date unless the user explicitly wants scheduled publishing.
- If the post returns to draft after publish, re-check the publish date first.
- Treat any weekday cadence from an older SOP as a default editorial rule, not as a timeless truth. Follow newer team guidance if it exists.

## Remember what the skill should output

When backend-ready output is requested, include:

- The article body in CMS-safe Markdown.
- A field-by-field metadata block.
- Notes for image placement and thumbnail choice.
- Any backend risk notes, such as a table that should become an image.
