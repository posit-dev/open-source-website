# Blog Authoring Guide

All blog posts should be submitted as a pull request against `main` — don't push directly to the branch. This ensures every post gets a Netlify preview before it goes live.

**Posit org members:** Clone the repo directly — don't fork it. As a member of the Everyone team you have Write access to `posit-dev/open-source-website`, so you can push branches straight to the main repo and open a PR from there. This is the smoothest path because branch PRs get a Netlify preview automatically.

If you already work from a fork (your own preference, or a personal-fork-first workflow), that's fine too — you'll just need to comment `/deploy-preview` on your PR once to trigger the preview build. Fork PRs can't auto-deploy because GitHub gives the workflow a read-only token with no access to our Netlify secrets.

If you're using Claude Code, the `/new-post` skill will handle scaffolding, frontmatter, branch creation, and environment setup interactively.

## Where to place your post

New posts go at the top level: `content/blog/my-post-slug/`.

The subfolders (`quarto/`, `tidyverse/`, `shiny/`, `ai/`, etc.) contain ported legacy content — don't use them for new posts.

Create a new post with:

```sh
hugo new blog/my-post-slug/index.md
```

For a Quarto post, create as `index.md` then rename to `index.qmd` — Hugo doesn't recognise `.qmd` as a content format, so `hugo new` won't work directly with that extension.

## Choosing a format

- **`index.md`** — prose only; no code execution needed
- **`index.qmd`** — executable R or Python code, or Quarto features like callouts, tabsets, and cross-references.
- **`index.ipynb`** — if you're primarily working in Jupyter

When in doubt, use `.md`.

## Frontmatter

See `CLAUDE.md` in this directory for the full metadata schema. A few things worth noting:

- **Authors** — use `people`, not `author`. List individuals by full name; don't use team names like "Shiny Team"
- **Image** — 1920×1080 PNG or JPG recommended (16:9); GIF is supported and animation will play in the hero and listings
- **Alt text** — describe what the image shows; "screenshot" or "logo" alone isn't enough
- **Project blog listing** — if your post belongs to one of the projects below, set `source` so it appears on that project's blog listing page (e.g. `source: tidyverse` → `/blog/q/tidyverse/`). Older project blog URLs (e.g. `tidyverse.org/blog/`) will redirect to these listing pages, so posts about these projects should set `source` to stay visible to those readers. Valid values for new posts: `positron`, `tidyverse`, `ai`, `shiny`, `great_tables`, `plotnine`, `pointblank`, `quarto`. (`education` and `rstudio` are reserved for ported posts — those blogs aren't actively published to.)

## Setting up an environment

For `.qmd` posts with executable code, you may want to record the environment in the post's folder so others can reproduce it later. This is optional — pick the approach that fits how you usually work, including not pinning at all.

Common options:

- **Python** — `uv` or a plain `requirements.txt`
- **R** — `renv` or a `DESCRIPTION` file with `pak`

If you do pin:

- Commit the environment definition and lockfile(s) (e.g. `pyproject.toml` + `uv.lock`, or `renv.lock` + `.Rprofile` + `renv/activate.R` + `renv/settings.json`) alongside the post.
- Don't commit the package library or virtual environment — `.venv/` and `renv/library/` are gitignored.
- Render the post from within the environment (e.g. `uv run quarto render index.qmd`, or with `renv` activated).

## Rendering and committing

Quarto renders `index.qmd` to `index.md` (Hugo-flavored Markdown) via the project's `_quarto.yml` setting. No freeze configuration is needed.

Always commit:
- `index.qmd` — the source
- `index.md` — the rendered output
- Any generated output files (plots, notebooks, data) in the post folder

Reviewers and CI can build the site without re-executing your code.

## Previewing your post

### Option 1: PR preview (simplest)

Open a pull request against `main`. GitHub Actions will build the site and post a Netlify preview URL as a comment on the PR — no local setup required.

If your PR is from a fork, auto-deploy is disabled (fork workflows run with a read-only token). A member — including you, if you have member access — can comment `/deploy-preview` on the PR to trigger the build.

The preview URL looks like `https://<hash>--posit-open-source.netlify.app`. All posts use the format `/blog/YYYY-MM-DD_slug/`, where date and slug come from frontmatter:

| Frontmatter | Preview path |
|---|---|
| `date: 2026-04-07`, folder `my-post` (no slug set) | `/blog/2026-04-07_my-post/` |
| `date: 2026-04-07`, `slug: custom-slug` | `/blog/2026-04-07-custom-slug/` |

The URL slug defaults to the folder name, so you only need to set `slug` in frontmatter if you want something different.

### Option 2: Build locally

For faster iteration, you can preview locally. You'll need [just](https://github.com/casey/just), Node.js v20+, Hugo Extended v0.158.0+, and Quarto (if rendering `.qmd` or `.ipynb` files). On macOS:

```sh
brew install just         # command runner — needed for `just dev`
brew install hugo node    # Hugo Extended + Node.js
```

Install Quarto from [quarto.org](https://quarto.org/docs/get-started/) if rendering `.qmd` or `.ipynb`. See [Prerequisites](../../README.md#prerequisites) in the README for other platforms.

First-time setup (Node dependencies):

```sh
just install
```

Then start the dev server:

```sh
just dev
```

This runs Hugo and the Tailwind CSS watcher in parallel. The site will be available at `http://localhost:1313` with live reload.

**For `.qmd` posts:** Hugo serves the rendered `index.md`, not the source `.qmd`, so you need to run Quarto separately. Two options:

- Re-render on demand (from the post directory):
  ```sh
  quarto render index.qmd
  ```
- Watch for changes in a second terminal — Quarto will re-render to `index.md` on each save, which Hugo will then pick up automatically:
  ```sh
  quarto preview index.qmd
  ```

## Getting published

Once your post is written, follow these steps to get it live.

### Open a pull request

Push your branch and open a PR against `main`. A bot will post a publishing checklist on your PR to help you track the remaining steps.

### Get a review

Request at least one reviewer — they can check content, frontmatter, and the rendered preview.

### Check the preview

After the deploy workflow finishes, a bot comment will appear with direct links to your post's preview and the blog listing. Use these to:

1. **Read through your post** — check formatting, images, links, and code blocks
2. **Check the blog listing** — confirm your post appears at `/blog/` with the right title, thumbnail, and description

These links update automatically when you push new commits.

### Merge

Once you have an approving review and the preview looks good, merge the PR to `main`. The site deploys automatically — your post will be live within a few minutes.

### Scheduling a post for the future

To publish a post on a specific future date, set `date` in frontmatter to that date and merge the PR whenever it's ready. Hugo won't include future-dated posts in production builds, so the post stays hidden until its date arrives.

A scheduled build runs daily at 8 AM UTC (3 AM EST / 4 AM EDT), so your post will go live automatically on the morning of its publish date. No manual action needed.

PR previews always use `--buildFuture`, so reviewers can see and check future-dated posts before they go live.

## Validating your post

A validation script checks frontmatter for required fields, valid taxonomy values, image existence, and other common issues.

### Automatically on PRs

Any PR that touches `content/blog/**` triggers a GitHub Actions workflow that validates changed posts and posts results as a comment on the PR. Errors block the check; warnings are advisory.

### Locally

Run the script against specific posts:

```sh
uv run scripts/validate-blog-posts.py content/blog/my-post/index.md
```

Or check all posts (skips the past-date warning since every published post would trigger it):

```sh
uv run scripts/validate-blog-posts.py --no-date-check
```

Other flags:

- `--strict` — treat warnings as errors
- `--format markdown` — output markdown (used by CI for PR comments)

### With Claude Code

The `/check-post` skill runs validation interactively and can offer to fix issues it finds.

## Content reference

### `.qmd` posts

#### Tabsets

```markdown
::: {.panel-tabset}
## R

R code here.

## Python

Python code here.
:::
```

Add a `group="my-group"` attribute to sync multiple tabsets on the page.

#### Code folding

Set in frontmatter to fold all code blocks by default:

```yaml
format:
  hugo-md:
    code-fold: true
    code-summary: "Show the code"
```

Or per-chunk with `#| code-fold: true`.

#### Code line numbers

Off by default. Set `code-line-numbers: true` at the top level of frontmatter to turn line numbers on for every code block on the page:

```yaml
code-line-numbers: true
```

Quarto's per-cell (`#| code-line-numbers: true`) and per-block (`{code-line-numbers="true"}`) variants are stripped during the GFM render, so page-level is currently the only form that works.

#### Videos

```markdown
{{< video https://www.youtube.com/watch?v=VIDEO_ID >}}
{{< video my-video.mp4 title="Description for accessibility" >}}
```

Supported sources: YouTube, Vimeo, local files (`.mp4`, `.webm`, `.ogg`). A Lua filter converts the Quarto `{{< video >}}` shortcode to Hugo's format automatically.

Optional parameters: `title`, `width`, `height`, `start` (YouTube only), `aspect-ratio` (`16x9`, `4x3`, `1x1`, `21x9`).

#### Button

Hugo's `{{< button >}}` shortcode passes through Quarto's rendering unchanged:

```markdown
{{< button url="https://example.com" text="Click here" >}}
```

Optional parameters: `icon`, `icon-left`, `icon-right`, `size` (`small`, `medium`, `large`).

#### Images

Always include alt text — it's required for accessibility. Use the `fig-alt` attribute:

```markdown
![Optional caption](my-image.png){fig-alt="Alt text describing the image"}
```

#### Multi-column layouts

Place content side-by-side with `layout-ncol`. Each child `:::` div becomes one column:

```markdown
::: {layout-ncol=2}

::: {}
Left column content — markdown, code blocks, images all work here.
:::

::: {}
Right column content.
:::

:::
```

A Lua filter converts these to CSS grid at render time, so code blocks (including those with `filename=` attributes) render correctly.

#### Linking to other blog posts

Use the **permalink URL** — the `/blog/YYYY-MM-DD_slug/` path you see in the browser:

```markdown
Check out the [dplyr 1.0.0 post](/blog/2020-06-01_dplyr-1-0-0/).
```

Don't use content directory paths like `/blog/tidyverse/2020/dplyr-1-0-0/`. Those depend on how files are organized on disk and would break if we ever reorganize.

To find a post's permalink, check its `date` and `slug` (or folder name) in frontmatter. The pattern is `/blog/{date}_{slug}/`, e.g. `date: 2020-06-01` + `slug: dplyr-1-0-0` → `/blog/2020-06-01_dplyr-1-0-0/`. Or just find the post on the site and copy the URL.

### `.md` posts

#### Code line numbers

Off by default. Set `code-line-numbers: true` at the top level of frontmatter to turn line numbers on for every code block on the page:

```yaml
code-line-numbers: true
```

#### Videos

```markdown
{{< video src="https://www.youtube.com/watch?v=VIDEO_ID" >}}
{{< video src="my-video.mp4" title="Description" >}}
```

Supported sources: YouTube, Vimeo, local files (`.mp4`, `.webm`, `.ogg`).

Optional parameters: `title`, `width`, `height`, `start` (YouTube only), `aspect-ratio` (`16x9`, `4x3`, `1x1`, `21x9`).

#### Columns

Split content into responsive columns (stacks on mobile):

```markdown
{{< columns >}}
Left column content.

---

Right column content.
{{< /columns >}}
```

Control column widths with `split` (comma-separated `fr` values):

```markdown
{{< columns split="2,1" >}}
Wider left column.

---

Narrower right column.
{{< /columns >}}
```

#### Button

```markdown
{{< button url="https://example.com" text="Click here" >}}
```

Optional parameters: `icon`, `icon-left`, `icon-right`, `size` (`small`, `medium`, `large`).

#### Images

Always include alt text — it's required for accessibility. Set it inside `[]`. To add a visible caption, use a title string in quotes after the URL:

```markdown
![Alt text describing the image](my-image.png)
![Alt text describing the image](my-image.png "Caption shown below the image")
```

#### Linking to other blog posts

Use the **permalink URL** — the `/blog/YYYY-MM-DD_slug/` path you see in the browser:

```markdown
Check out the [dplyr 1.0.0 post](/blog/2020-06-01_dplyr-1-0-0/).
```

Don't use content directory paths like `/blog/tidyverse/2020/dplyr-1-0-0/`. Those depend on how files are organized on disk and would break if we ever reorganize.

To find a post's permalink, check its `date` and `slug` (or folder name) in frontmatter. The pattern is `/blog/{date}_{slug}/`, e.g. `date: 2020-06-01` + `slug: dplyr-1-0-0` → `/blog/2020-06-01_dplyr-1-0-0/`. Or just find the post on the site and copy the URL.
