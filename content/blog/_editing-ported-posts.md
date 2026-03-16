# Editing Ported Posts

Guidelines for modifying blog posts that were ported from legacy blogs.

## Identifying ported posts

Ported posts have `ported_from` in their frontmatter:

```yaml
ported_from: tidyverse  # or: education, ai, shiny, etc.
```

## Source vs. rendered files

Many ported posts have both:
- **Source file**: `.Rmd`, `.Rmarkdown`, `.qmd`, or `.ipynb`
- **Rendered file**: `.md` or `.markdown`

Hugo uses the rendered file. The source file is kept for potential re-rendering.

## Before re-rendering a post

**Don't assume metadata will propagate.** During porting, we updated frontmatter in the rendered file but often not the source. If you re-render without updating the source first, you'll lose:

- `people` (source may have `author` instead)
- `image` (source may have `preview` instead)
- `image-alt`
- `ported_from`
- `port_status`

**Before rendering, copy these fields from the `.md` to the source file.**

### Field mappings by blog

| Blog | Source field | Rendered field |
|------|--------------|----------------|
| ai | `author` (with name/affiliation) | `people` (names only) |
| ai | `preview` | `image` |
| ai | `date: MM-DD-YYYY` | `date: YYYY-MM-DD` |
| tidyverse | `author` | `people` |
| shiny | `imagealt` | `image-alt` |

### Fields to remove from source before rendering

These are rendering config that shouldn't be in the final output:

- `output: hugodown::hugo_document`
- `rmd_hash`
- `editor`, `editor_options`

## Simple text edits

For typo fixes or minor text changes, edit the `.md` file directly. No need to re-render.

If you also want to keep the source in sync, make the same edit there — but this is optional for small fixes.

## Adding/changing metadata

Edit the `.md` file. Update the source file too if you want to keep them in sync.

## Fixing links

For quick fixes, edit the `.md` file directly. If you plan to re-render, fix the source file too.

**Link guidelines:**

- Use **absolute URLs** for external sites: `https://shiny.posit.co/r/getstarted/`
- Use **site-root paths** for internal blog links: `/blog/shiny/foo/`
- Never use `https://posit.co/blog/...` for internal links — that's a different site
- In source files, avoid relative paths like `../` — they break when posts move

See `_link-checks.md` for common patterns to fix and how to run link checking.

## Virtual environments

Some blogs have shared virtual environments for rendering posts with executable code. **Check for these files before re-rendering:**

| File | Tool | Activate |
|------|------|----------|
| `renv.lock` | renv (R) | `renv::restore()` from blog directory |
| `pyproject.toml` | uv (Python) | `uv sync` from blog directory |

**Blogs with environments:**

| Blog | R (renv) | Python (uv) |
|------|----------|-------------|
| `content/blog/ai/` | Yes | — |
| `content/blog/shiny/` | Yes | Yes |
| `content/blog/great-tables/` | — | Yes |
| `content/blog/pointblank/` | — | Yes |
| `content/blog/plotnine/` | — | Yes |

**To render with the environment:**

```bash
# Python (uv)
cd content/blog/<blog>
uv sync
uv run quarto render <post>/index.qmd --to hugo-md

# R (renv) - start R from the blog directory
cd content/blog/<blog>
R
# then in R: renv::restore()
```

## Re-rendering a post

1. Open the rendered `.md` and note the current frontmatter
2. Update the source file's frontmatter to match (see field mappings above)
3. Activate the virtual environment if one exists (see above)
4. Render: `quarto render <file> --to hugo-md` (or knit for R Markdown)
5. Verify the rendered file's frontmatter is correct
6. Commit both source and rendered files

## Blog-specific notes

### AI blog (`content/blog/ai/`)

The AI blog has the biggest gap between source and rendered frontmatter. Source files typically have:
- `author:` with name/affiliation/url structure
- `preview:` instead of `image:`
- `date:` in MM-DD-YYYY format
- `bibliography:` reference

**If re-rendering:** Posts with bibliographies won't get a "References" heading without a full Quarto project setup.

### Tidyverse blog (`content/blog/tidyverse/`)

Source `.Rmd` files have `output: hugodown::hugo_document`. Remove this before rendering with Quarto.

### Education blog (`content/blog/education/`)

Uses `.Rmarkdown` (source) and `.markdown` (rendered). These are usually well-synced.

### Shiny blog (`content/blog/shiny/`)

`.qmd` and `.md` files are usually in sync. Watch for `imagealt` vs `image-alt`.

**If re-rendering:**

- **Nested HTML gets stripped** — Quarto/Pandoc strips nested `<div>` elements. Wrap complex HTML (like video embeds) in `` ```{=html} `` blocks.
- **Bootstrap classes** — A Lua filter (`strip-bootstrap`) removes Bootstrap classes during rendering. Posts with heavy Bootstrap usage may lose styling.
- **Shinylive blocks** — `{shinylive-r}` and `{shinylive-python}` blocks don't work with `hugo-md` output.
- **Don't mix `code-fold` and `engine: markdown`** — If a post uses `#| code-fold: true`, don't add `engine: markdown` to frontmatter; it breaks code folding.

### Great Tables, Pointblank, Plotnine blogs

**If re-rendering:** Watch for `{{` in code blocks (e.g., `{{%NO3%}}` for units). Hugo interprets `{{` as shortcode delimiters. Escape as `&#123;&#123;` in both source and rendered files.
