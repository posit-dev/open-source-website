# Blog Authoring Guide

All blog posts should be submitted as a pull request against `main` — don't push directly to the branch. This ensures every post gets a Netlify preview before it goes live.

If you're using Claude Code, the `/new-post` skill will handle scaffolding, frontmatter, branch creation, and environment setup interactively.

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

## Choosing a format

- **`index.md`** — prose only; no code execution needed
- **`index.qmd`** — executable R or Python code, or Quarto features like callouts, tabsets, cross-references, and video shortcodes
- **`index.ipynb`** — if you're primarily working in Jupyter

When in doubt, use `.md`.

## Frontmatter

See `CLAUDE.md` in this directory for the full metadata schema. A few things worth noting:

- **Authors** — list individuals by full name in the `people` field; don't use team names like "Shiny Team"
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

The preview URL looks like `https://<hash>--posit-open-source.netlify.app`. Your post's path within it follows the folder structure:

| Post location | Preview path |
|---|---|
| `content/blog/my-post/` | `/blog/my-post/` |
| `content/blog/tidyverse/my-post/` | `/blog/tidyverse/my-post/` |
| `content/blog/tidyverse/my-post/` with `slug: original-post` | `/blog/tidyverse/original-post/` |

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

## Quarto features (`.qmd` posts)

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

### Callouts

```markdown
::: {.callout-note}
This is a note without a custom title.
:::

::: {.callout-tip}
## Custom Title

This tip has a custom title.
:::

::: {.callout-warning collapse="true"}
## Expandable Warning

This callout starts collapsed — the reader clicks to expand it.
:::
```

Five types are available: `note`, `tip`, `warning`, `caution`, `important`. Each has a distinct color and icon. If you omit the heading inside the callout, the type name is used as the title.

Add `collapse="true"` to make the callout collapsible (requires a title).

### Code block filenames

Label a code block with a filename to show the reader which file the code belongs to:

````markdown
```{.python filename="app.py"}
from shiny.express import input, ui
```
````

This renders a styled filename header attached to the top of the code block. Works for any language (`.python`, `.yaml`, `.bash`, etc.) and for non-language labels like `filename="Terminal"`.

This also works in `.md` posts — use Goldmark attribute syntax:

````markdown
``` python { filename="app.py" }
from shiny.express import input, ui
```
````

**Note:** This works on non-executable code blocks only (`` ```{.python} `` with the dot). Executable code cells (`` ```{python} ``) do not support `filename` — Quarto's execution engines don't preserve the attribute through rendering.

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

### Other Hugo shortcodes

Hugo shortcodes pass through Quarto's rendering unchanged, so the `{{< columns >}}` and `{{< button >}}` shortcodes documented below also work in `.qmd` posts.

## Math

To use LaTeX math in a post, add `math: true` to the frontmatter:

```yaml
math: true
```

Then use `$...$` for inline math and `$$...$$` for display math:

```markdown
The loss is $L = -\sum y_i \log \hat{y}_i$.

$$
\nabla_\theta J(\theta) = \mathbb{E}[\nabla_\theta \log \pi_\theta(a|s) \cdot R]
$$
```

Math rendering uses MathJax 3 and is only loaded on posts that set `math: true`, so there's no performance cost for other pages.

**Important:** If your post uses a literal `$` sign (e.g. currency) outside of backticks or code blocks, escape it as `\$` to prevent it from being interpreted as a math delimiter. This applies to all posts, not just those with `math: true`.

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
