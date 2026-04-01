# Blog Authoring Guide

Guidelines for creating new blog posts.

## Images

### Post images

Every post should have an `image` and `image-alt` in the frontmatter:

```yaml
---
title: My Post Title
image: featured.png
image-alt: A descriptive alt text for the image
---
```

The image is used in:
- **Hero banner** on the post page
- **Cards** in blog listings
- **Social previews** (OG/Twitter images)

If no `image` is set:
- Hero: no image shown
- Listings: falls back to parent section's image (if set), otherwise empty
- Social: falls back to generic blog placeholder

### Subsection default images

Blog subsections (e.g., `content/blog/great-tables/`) can set a default image for posts that don't have their own. Add to the subsection's `_index.md`:

```yaml
---
title: Great Tables
image: default-image.png
image-alt: Great Tables logo
---
```

Posts in that folder without an `image` will use this in listings. The `image-alt` is also inherited.

### Image recommendations

- **Format**: PNG or JPG; GIF is also supported and animation will play in the hero and card listings — useful for demo-heavy posts
- **Aspect ratio**: 16:9 (e.g. 1920×1080)
- **Size**: 1920×1080 recommended — this is the standard used across the blog
- **File location**: Place in the post's folder (same directory as `index.md`)

### Alt text

Always provide meaningful `image-alt` text:
- Describe what the image shows, not just "screenshot" or "logo"
- Keep it concise but informative
- If the image is decorative, you can use the post title as alt text (this is the fallback)

## Where to place your post

Posts live under `content/blog/`. Posts about a specific project should go in that project's subfolder:

| Subfolder | Use for |
|-----------|---------|
| `positron/` | Positron IDE |
| `tidyverse/` | tidyverse packages |
| `shiny/` | Shiny (R and Python) |
| `quarto/` | Quarto |
| `great-tables/` | Great Tables |
| `plotnine/` | plotnine |
| `pointblank/` | pointblank |

Everything else — general news, cross-cutting topics, AI posts, posts about projects without a dedicated subfolder — goes at the top level `content/blog/my-post/`.

The `ai/`, `rstudio/`, and `education/` subfolders contain ported legacy content; don't use them for new posts.

Create a new post with:

```sh
# Top level
hugo new blog/my-post-slug/index.md

# In a project subfolder
hugo new blog/tidyverse/my-post-slug/index.md
```

For a Quarto post, create as `index.md` then rename to `index.qmd` — Hugo doesn't recognise `.qmd` as a content format, so `hugo new` won't work directly with that extension.

## Authors

The `people` field lists post authors. Use each person's full name, one per line:

```yaml
people:
  - Jane Smith
  - Alex Johnson
```

Don't use team names like "Shiny Team" — list individuals.

## Choosing a format

- **`index.md`** — prose only; no code execution needed
- **`index.qmd`** — executable R or Python code, or Quarto features like callouts, tabsets, cross-references, and video shortcodes
- **`index.ipynb`** — if you're primarily working in Jupyter

When in doubt, use `.md`.

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

## Quarto features (`.qmd` posts)

### Callouts

```markdown
::: callout-note
Note text here.
:::

::: {.callout-tip title="Custom title" collapse="true"}
Collapsible tip.
:::
```

Types: `callout-note`, `callout-tip`, `callout-warning`, `callout-important`, `callout-caution`

### Tabsets

```markdown
::: {.panel-tabset}
## R

R code here.

## Python

Python code here.
:::
```

Add a `group="my-group"` attribute to sync multiple tabsets on the page.

### Code folding

Set in frontmatter to fold all code blocks by default:

```yaml
format:
  hugo-md:
    code-fold: true
    code-summary: "Show the code"
```

Or per-chunk with `#| code-fold: true`.

### Videos

```markdown
{{< video https://www.youtube.com/watch?v=VIDEO_ID >}}
{{< video my-video.mp4 title="Description for accessibility" >}}
```

Supported sources: YouTube, Vimeo, local files (`.mp4`, `.webm`, `.ogg`). A Lua filter converts the Quarto `{{< video >}}` shortcode to Hugo's format automatically.

Optional parameters: `title`, `width`, `height`, `start` (YouTube only), `aspect-ratio` (`16x9`, `4x3`, `1x1`, `21x9`).

## Hugo shortcodes (`.md` posts)

### Videos

Same syntax as Quarto:

```markdown
{{< video src="https://www.youtube.com/watch?v=VIDEO_ID" >}}
{{< video src="my-video.mp4" title="Description" >}}
```

### Columns

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

### Button

```markdown
{{< button url="https://example.com" text="Click here" >}}
```

Optional parameters: `icon`, `icon-left`, `icon-right`, `size` (`small`, `medium`, `large`).

## Previewing your post

**Locally:** run `hugo server` from the project root and open `http://localhost:1313`.

**In a PR:** GitHub Actions builds the site on every PR and posts a Netlify preview URL as a comment. All posts should go through a PR — don't push directly to `main`.
