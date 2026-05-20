---
name: review-post
description: Review a blog post's content against its frontmatter and the authoring guide
---

Review a blog post's content the way a reviewer would — checking that the content lines up with its frontmatter, surfacing things authors commonly miss, and flagging accessibility issues. Complements `/check-post`, which validates frontmatter mechanically; this skill reads the actual post text.

This skill **does not check writing style**. At the end, remind the author to get a human review for tone, clarity, and flow.

## Step 1: Identify the post

If the user provided a path via `$ARGUMENTS`, use that. Otherwise, look for blog posts changed on the current branch:

```sh
git diff --name-only --diff-filter=d origin/main...HEAD -- 'content/blog/**/index.md' 'content/blog/**/index.qmd'
```

If no changed posts are found, ask the user which post to review.

## Step 2: Read the post

For each post, read both the frontmatter and the body. If an `index.qmd` exists, prefer it as the source of truth; otherwise read `index.md`. You need the actual prose, not just the metadata.

## Step 3: Content vs. frontmatter consistency

Compare what the post actually says to what its frontmatter claims. Flag mismatches:

- **`description` drift** — does the description still summarize the post accurately? Descriptions written at `/new-post` time often stop matching the finished draft.
- **`software` / `languages` / `topics`** — do the values reflect what the post is actually about? If the post discusses ggplot2 but `software` only lists dplyr, flag it. If the inferred topics no longer fit, flag it. Suggest the values that *would* match.
- **`source`** — if the post is clearly about one of the projects with a blog listing page (`positron`, `tidyverse`, `ai`, `shiny`, `great_tables`, `plotnine`, `pointblank`, `quarto`) and `source` isn't set, flag it. See `content/blog/_authoring-guide.md` for the rule.
- **`title`** — does it match the post's actual focus, or has the angle shifted during writing?

## Step 4: Things authors miss

- **Placeholders left in the draft** — search the body for `TODO`, `TBD`, `XXX`, `FIXME`, `lorem ipsum`, `[insert ...]`, `[link]`, etc. List each occurrence with line context.
- **Internal blog links use the permalink pattern** — flag any links that look like `/blog/<source>/<year>/<slug>/` or other content-directory paths instead of `/blog/YYYY-MM-DD_slug/`. (See "Linking to other blog posts" in the authoring guide.)
- **Code blocks have a language tag** — fenced code blocks should open with a language (` ```r `, ` ```python `, ` ```sh `, etc.), not bare ` ``` `.
- **`.qmd` images use `fig-alt`** — alt text in `.qmd` should be `![](path){fig-alt="..."}`, not `![alt](path)` (the bracket text becomes a caption in Quarto).

## Step 5: Accessibility and structure

- **Image alt text on body images** — for every image in the post body, check that alt text is descriptive ("Bar chart showing ...") not generic ("screenshot", "logo", "image"). Empty alt is only acceptable for purely decorative images.
- **Heading hierarchy** — the post body should have **no `#` (H1) headings** — the page H1 is rendered from frontmatter `title`. Top-level body sections should start at `##` (H2), and lower-level headings shouldn't skip levels (don't jump `##` → `####`).

## Step 6: Predicted permalink

From the frontmatter `date` and `slug` (or folder name), report the URL the post will live at:

```
/blog/{date}_{slug-or-folder}/
```

This lets the author sanity-check the slug before publishing and copy the URL for cross-linking from other posts.

## Step 7: Report findings

Summarize results grouped by severity:

- **Must fix** — placeholders, broken permalink-format links, missing code-block languages, generic/missing alt text, bracket-alt on `.qmd` images, heading hierarchy violations.
- **Consider** — frontmatter drift (`description`, `software`, `languages`, `topics`, `source`, `title`), title-vs-content focus shifts.

For each item, quote the relevant line(s) and explain what to change.

If there are no findings, say so.

## Step 8: Offer to fix

Ask whether to apply the fixes. For accepted items:

- If the post has an `index.qmd`, edit the `.qmd` (source of truth), then re-render to update `index.md`.
- Otherwise, edit `index.md` directly.

## Step 9: Re-run /check-post

After any frontmatter edits, run `/check-post` (or the underlying script) on the post so the author sees a clean mechanical-validation pass before moving on.

## Step 10: Remind about human review

Finish with a one-line reminder: this skill doesn't check writing style, tone, or flow — ask a teammate to read the draft before merging.
