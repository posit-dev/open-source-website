# Blog Authoring Guide

All blog posts should be submitted as a pull request against `main` — don't push directly to the branch. This ensures every post gets a Netlify preview before it goes live.

**Posit org members:** Clone the repo directly — don't fork it. You have Write access to `posit-dev/open-source-website`, so you can push branches straight to the main repo and open a PR from there.

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

## Setting up an environment

For `.qmd` posts with executable code, record the environment in the post's folder so others can reproduce it.

### Python (uv)

```sh
cd content/blog/my-post/
uv init --no-workspace
uv add package1 package2
```

Optionally pin dependency resolution to a date for long-term reproducibility:

```toml
[tool.uv]
exclude-newer = "2025-01-01T00:00:00Z"
```

Commit `pyproject.toml` and `uv.lock`. The `.venv/` folder is gitignored.

Render using the environment:

```sh
uv run quarto render index.qmd
```

### R (renv)

```r
# With your R working directory set to the post folder
renv::init()
# install packages, write your post...
renv::snapshot()
```

Commit `renv.lock`, `.Rprofile`, `renv/activate.R`, and `renv/settings.json`. The `renv/library/` folder is gitignored.

If you prefer, a `DESCRIPTION` file with `pak` for dependency declaration also works, though it's less established for posts.

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

The preview URL looks like `https://<hash>--posit-open-source.netlify.app`. All posts use the format `/blog/YYYY-MM-DD_slug/`, where date and slug come from frontmatter:

| Frontmatter | Preview path |
|---|---|
| `date: 2026-04-07`, folder `my-post` (no slug set) | `/blog/2026-04-07_my-post/` |
| `date: 2026-04-07`, `slug: custom-slug` | `/blog/2026-04-07-custom-slug/` |

The URL slug defaults to the folder name, so you only need to set `slug` in frontmatter if you want something different.

### Option 2: Build locally

For faster iteration, you can preview locally. You'll need:

- [just](https://github.com/casey/just)
- Node.js v20+
- Hugo Extended v0.158.0+
- Quarto (if rendering `.qmd` or `.ipynb` files)

First-time setup:

```sh
just install   # Install Node.js dependencies
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

#### Linking to other blog posts

Use the **permalink URL** — the `/blog/YYYY-MM-DD_slug/` path you see in the browser:

```markdown
Check out the [dplyr 1.0.0 post](/blog/2020-06-01_dplyr-1-0-0/).
```

Don't use content directory paths like `/blog/tidyverse/2020/dplyr-1-0-0/`. Those depend on how files are organized on disk and would break if we ever reorganize.

To find a post's permalink, check its `date` and `slug` (or folder name) in frontmatter. The pattern is `/blog/{date}_{slug}/`, e.g. `date: 2020-06-01` + `slug: dplyr-1-0-0` → `/blog/2020-06-01_dplyr-1-0-0/`. Or just find the post on the site and copy the URL.

### `.md` posts

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
