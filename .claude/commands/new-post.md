---
name: new-post
description: Scaffold a new blog post with inferred frontmatter, branch, and optional environment setup
---

Help the user create a new blog post for the Posit open-source website. Work through these steps in order.

## Step 0: Preflight check

Description: "Checking whether you're working from a direct clone or a fork"

```sh
git remote get-url origin
```

If the remote URL does not contain `posit-dev/open-source-website`, note to the user:

> Looks like you're working from a fork. That's supported — you'll just need to comment `/deploy-preview` on your PR once to trigger the preview build (fork PRs can't auto-deploy because the workflow runs with a read-only token). If you're a member of the `posit-dev` org, the smoother path is to clone `posit-dev/open-source-website` directly so branch PRs get auto-deploy.

Then ask whether they'd like to continue from the fork or stop to re-clone.

## Step 1: Gather information

Ask the user for anything not already provided via arguments: `$ARGUMENTS`

- **Title** — the post title
- **Topic** — a brief description of what the post is about (use this to infer frontmatter)
- **Author(s)** — full name(s) of the people writing the post
- **Executable code?** — ask "Will this post include executable code chunks (R or Python)?" rather than asking about file format directly:
  - Yes → `.qmd`; also ask whether the code is R, Python, or both
  - No → `.md` (unless they specifically want `.ipynb`, which is fine to offer)

## Step 2: Infer frontmatter

From the title and topic, reason about:

- **slug** — only needed if it should differ from the folder name; otherwise the folder name is used automatically
- **software** — folder names from `content/software/` that the post is about (e.g. `ggplot2`, `quarto`, `great-tables`)
- **languages** — programming languages featured (R, Python, etc.)
- **topics** — one or more from the fixed set in `data/topics.yaml`: Machine Learning, Artificial Intelligence, Visualization, Interactive Apps, Publishing, MLOps and Admin, Data Wrangling, Best Practices, Community
- **source** — set if the post belongs to one of the projects with its own blog listing page, so it appears there (e.g. `source: tidyverse` → `/blog/q/tidyverse/`). Older project blog URLs (e.g. `tidyverse.org/blog/`) redirect to these listing pages, so this is how a new post stays visible to those readers. Valid values: `positron`, `tidyverse`, `ai`, `shiny`, `great_tables`, `plotnine`, `pointblank`, `quarto`. Infer from the inferred `software`/topic (e.g. dplyr/ggplot2 → `tidyverse`, Positron → `positron`); confirm with the user. Omit only if the post genuinely doesn't belong to any of these projects.
- **description** — a draft 1–2 sentence description of the post

Present your inferences clearly and ask the user to confirm or correct before proceeding.

For every shell command below, use a description that explains *why* this step is needed in the context of creating the blog post — not just what the command does. This text appears in the permission prompt and helps the author understand what's happening.

## Step 3: Create a branch

Description: "Creating a dedicated branch for this post so it can be reviewed as a PR before going live"

```sh
git checkout -b blog/<slug>
```

## Step 4: Scaffold the post

Description: "Scaffolding the post folder and frontmatter from the blog archetype"

```sh
hugo new blog/<slug>/index.md
```

If the format is `.qmd`, rename the file:

Description: "Renaming to .qmd so Quarto will render this post to Markdown before Hugo builds it"

```sh
mv content/blog/<path>/index.md content/blog/<path>/index.qmd
```

## Step 5: Fill in the frontmatter

Edit the created file to replace the archetype defaults with the confirmed values:

- Set `title`, `date` (today), `people`, `description`
- Set `topics` to only the relevant values (remove the rest)
- Set `source` if confirmed in step 2; otherwise omit it entirely
- Set `software` and `languages` to only the relevant values; remove empty `-` entries
- Remove empty `tags` entries
- Leave `image` and `image-alt` empty for the author to fill in

## Step 6: Open the file

Report the full path to the created file so the user can open it themselves, along with the predicted permalink the post will live at: `/blog/<date>_<slug-or-folder>/` (e.g. `/blog/2026-04-07_my-post/`).

## Step 7: Offer to set up local preview

Local preview is recommended for fast iteration but optional — the author can also rely on the Netlify preview that gets built on the PR. Mention this up front, then offer the local-preview setup as something they can opt into.

Detect which preview tools the user already has on `PATH`:

```sh
for t in just hugo node quarto; do command -v "$t" >/dev/null 2>&1 && echo "$t: present" || echo "$t: missing"; done
```

For any that are missing, list them and offer to install them. Don't run the install yourself unprompted — the author may prefer their own setup.

- macOS: `brew install just`, `brew install hugo node`; install Quarto from [quarto.org](https://quarto.org/docs/get-started/)
- Other platforms: point at the [Prerequisites](../../README.md#prerequisites) section of the README

If `node_modules/` doesn't exist at the repo root, offer to run `just install` to pick up the Node dependencies.

Then offer to start a local preview in the background:

- `just dev` for Hugo + Tailwind
- For `.qmd` posts, additionally offer `quarto preview index.qmd` from the post directory so Quarto re-renders on save while Hugo live-reloads

Skip any of these if the author declines or already has a preview running.

## Step 8: Hand off

Finish with a short next-steps list:

- Add `image` (1920×1080 PNG or JPG recommended) and `image-alt` to the frontmatter.
- Once frontmatter is filled in, run `/check-post` to validate it.
- Once the draft is ready, run `/review-post` for a content review before opening a PR.
- Open a PR against `main` to get a Netlify preview and a human review.
