# Blog Post Instructions

For full authoring guidance — post placement, format choice, environments, previewing — see `_authoring-guide.md` in this directory.

For porting guidance, see `_porting-notes.md` (how to port) and `_editing-ported-posts.md` (working with ported posts).

## Required Metadata

Every post must have:

| Field | Purpose |
|-------|---------|
| `title` | Post title |
| `date` | Publication date (`YYYY-MM-DD`) |
| `people` | Author full names (list) |
| `description` | 1-2 sentences; shown in card listings, under the post hero, and in social previews |
| `image` | Thumbnail/hero image filename |
| `image-alt` | Alt text for the image — describe what it shows, not just "screenshot" |
| `categories` | Fixed set — see below |
| `software` | Projects the post is about; use folder names from `content/software/` |
| `languages` | Programming languages (R, Python, etc.) |

**On `image` and `image-alt`:** The site can auto-discover images but falls back to the post title for alt text, which is poor for accessibility. Always set both explicitly.

## Taxonomies

### `categories` (required)

Use the fixed set — these power the blog filter UI:

Machine Learning, Artificial Intelligence, Visualization, Interactive Apps, Publishing, MLOps and Admin, Data Wrangling, Best Practices, Community

### `software` (required)

Which projects the post is about (not a category substitute). Use the folder name from `content/software/`, e.g. `ggplot2`, `quarto`, `great-tables`. Links to `/software/<name>/`.

### `languages` (required)

R, Python, etc. Links to `/languages/<name>/`.

### `events` (optional)

Related conferences/events, e.g. `posit-conf-2025`. Links to `/events/<name>/`.

### `resources` (optional)

Related resource types: tutorials, videos, cheatsheets, webinars. Links to `/resources/<name>/`.

### `tags` (optional)

Freeform. Avoid duplicating `software` or `categories` values.

## Optional Metadata

| Field | Purpose |
|-------|---------|
| `slug` | Override URL — use to preserve URLs when reorganizing folders |
| `nohero` | Boolean, hides the hero image |
| `hidesubscription` | Boolean, hides the subscription CTA |
| `photo.url` / `photo.author` | Stock photo attribution |

## Porting Metadata

Used to identify and track posts ported from legacy blogs. Do not add to new posts.

| Field | Purpose |
|-------|---------|
| `ported_from` | Source blog: positron, tidyverse, ai, shiny, great_tables, plotnine, pointblank, quarto, education, rstudio |
| `port_status` | Progress: `raw`, `in-progress`, `review`, `complete` |

**Tracking page:** `/blog/all/` shows porting progress and metadata completeness.

## URL Structure

By default, the folder name becomes the URL: `blog/my-post/` → `/blog/my-post/`

To override (e.g., when organizing into subfolders without changing URLs):
```yaml
slug: original-post-slug
```

## Exploring Post Metadata

`scripts/extract-blog-metadata.R` extracts frontmatter from all blog posts to JSON, which is useful for bulk queries across the post corpus.

```sh
Rscript scripts/extract-blog-metadata.R > posts.json
```

**Don't leave `posts.json` inside `content/` — Hugo will try to process it and fail.** Write it outside the content tree, or delete it when done.

Each entry in the JSON array has:

```json
{
  "md_path": "content/blog/tidyverse/my-post/index.md",
  "source_path": "content/blog/tidyverse/my-post/index.qmd",  // null if no source file
  "frontmatter": {
    "title": "My Post",
    "date": "2025-01-15",
    "people": ["Jane Smith"],
    "categories": ["Visualization"],
    "software": ["ggplot2"],
    ...
  }
}
```

`source_path` is populated if a `.qmd`, `.Rmd`, `.Rmarkdown`, or `.ipynb` file exists alongside the rendered `.md`. It is `null` for posts with no source file.

Pipe through Python for quick queries, e.g. to find posts missing a description:

```sh
Rscript scripts/extract-blog-metadata.R | python3 -c "
import json, sys
for p in json.load(sys.stdin):
    if not p['frontmatter'].get('description'):
        print(p['md_path'])
"
```
