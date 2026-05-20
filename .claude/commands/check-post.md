---
name: check-post
description: Validate blog post frontmatter and placement
---

Run the blog post validation script and help the user fix any issues found.

## Step 1: Identify the post

If the user provided a path via `$ARGUMENTS`, use that. Otherwise, look for blog posts changed on the current branch:

```sh
git diff --name-only --diff-filter=d origin/main...HEAD -- 'content/blog/**/index.md' 'content/blog/**/index.qmd'
```

If no changed posts are found, ask the user which post to check.

## Step 2: Check for unrendered `.qmd` files

For each post directory found, check if an `index.qmd` exists. If it does, check whether `index.md` also exists and is newer than `index.qmd`:

```sh
# For each post directory
if [ -f index.qmd ] && { [ ! -f index.md ] || [ index.qmd -nt index.md ]; }; then
  echo "index.qmd has not been rendered to index.md (or is out of date)"
fi
```

If any `.qmd` files need rendering, warn the user and always offer to re-render — even if there is no computational environment setup. To render:

```sh
quarto render <path>/index.qmd
```

`.qmd` posts may need to render through a specific environment — check the post folder for a `pyproject.toml`, `renv.lock`, or similar, and use whatever tool the author set up. See the "Setting up an environment" section of `content/blog/_authoring-guide.md` for context.

Do not proceed with validation until `index.md` exists and is up to date for all posts.

## Step 3: Run validation

The validation script reads `index.md` files (not `.qmd`):

```sh
uv run scripts/validate-blog-posts.py <paths to index.md>
```

## Step 4: Report results

If all checks pass, say so and stop.

If there are issues, summarize them clearly grouped by severity:

- **Errors** need fixing before the post can be published.
- **Warnings** are worth reviewing but won't block publishing — and some are reasonable to leave alone (see below).

For each error, explain what's wrong and suggest a concrete fix. For example:

- Missing `topics` → suggest values from `data/topics.yaml` that fit the post content
- Unknown `software` → check if there's a close match in `content/software/`. If there isn't one, offer to create a new software page using `scripts/create-new-software.py`.
- Unknown `people` → check if there's a close match in `content/people/`. If there isn't one, offer to create a new people page.
- Missing `source` on a ported post → suggest setting it to match `ported_from`
- `categories` present → replace with `topics`

For warnings, distinguish two groups:

**Sometimes intentional — ask before fixing.** These warnings flag fields that can be legitimately omitted when the post genuinely doesn't have that dimension:

- **`software` missing** — may be intentional for general best-practices, community, or company-news posts that aren't about a specific project. Ask before suggesting a value.
- **`languages` missing** — may be intentional for posts that aren't about a particular programming language. Ask before suggesting a value.
- **Can't find people page for `<name>`** — may be intentional if the contributor doesn't want a `content/people/` profile. Ask before offering to create one.

**Should normally be acted on.**

- **`date` is in the past** — confirm whether the author wants the post to publish on merge; if not, suggest a future date.
- **`<name>` looks like a team name** — suggest replacing with the individual contributors.

## Step 5: Offer to fix

For errors and the "should normally be acted on" warnings, ask the user if they'd like you to fix them directly. For the "sometimes intentional" warnings, ask first whether the absence is intentional — only fix if the user confirms a value should be set.

If they accept any fixes:

- If the post has an `index.qmd`, edit the **`.qmd`** file (that's the source of truth), then re-render to update `index.md`.
- If the post is plain Markdown, edit `index.md` directly.

Re-run validation to confirm the fixes worked.
