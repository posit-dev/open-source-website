# Blog Post Instructions

For full authoring guidance — post placement, format choice, environments, previewing — see `_authoring-guide.md` in this directory.

## Creating Blog Posts

Each blog post lives in its own folder under `content/blog/`:
```
content/blog/my-post-slug/
├── index.md          # Post content (or .qmd, .ipynb)
├── thumbnail.jpg     # Hero/thumbnail image
└── other-assets/     # Additional images, videos, etc.
```

Create new posts with: `hugo new blog/my-post-slug/index.md`

## Required Metadata

```yaml
---
title: "Post title"
date: '2025-01-15'
people:
  - Author Name
---
```

## Optional Metadata

### Content fields
| Field | Purpose |
|-------|---------|
| `description` | 1-2 sentences shown in card listings and under the post hero; also used for social previews |
| `image` | Thumbnail/hero image filename |
| `image-alt` | Alt text for image (Quarto standard) |

**Always set `image` and `image-alt` explicitly.** The site can auto-discover images (files with "thumbnail" in the name, or the first image alphabetically), but auto-discovered images fall back to the post title for alt text, which is poor for accessibility.
| `hero_video` | Video file for hero section |
| `photo.author` / `photo.url` | Stock photo attribution |
| `slug` | Override URL (use to preserve URLs when reorganizing folders) |
| `nohero` | Boolean, hides hero image |
| `hidesubscription` | Boolean, hides subscription CTA |

### Porting metadata

| Field | Purpose |
|-------|---------|
| `ported_from` | Source blog |
| `port_status` | Porting progress: `raw`, `in-progress`, `review`, `complete` |

**Valid `ported_from` values:** positron, tidyverse, ai, shiny, great_tables, plotnine, pointblank, quarto, education, rstudio

**Tracking page:** Use `/blog/all/` to monitor porting progress and metadata completeness.

### Taxonomies (for cross-linking)

Use these to connect posts to other site content:

```yaml
software:
  - plotnine         # Links to /software/plotnine/
  - shiny
languages:
  - python           # Links to /languages/python/
  - r
categories:
  - releases         # Topical groupings only
events:
  - posit-conf-2025  # Links to /events/posit-conf-2025/
resources:
  - tutorials        # Links to /resources/tutorials/
tags:
  - additional-tags
```

**Guidelines:**
- `software` — Which projects the post is about (not categories!)
- `languages` — Programming languages (R, Python, etc.)
- `categories` — Use the fixed set: Machine Learning, Artificial Intelligence, Visualization, Interactive Apps, Publishing, MLOps and Admin, Data Wrangling, Best Practices, Community
- `events` — Related conferences/events
- `resources` — Related resource types (tutorials, videos, cheatsheets, webinars)
- `people` — Post authors

## URL Structure

By default, the folder name becomes the URL: `blog/my-post/` → `/blog/my-post/`

To override (e.g., when organizing into subfolders without changing URLs):
```yaml
slug: original-post-slug
```

## Supported Formats

- `index.md` — Standard Markdown
- `index.qmd` — Quarto (with executable code)
- `index.ipynb` — Jupyter notebook (frontmatter goes in first raw cell as YAML)

**Notes:**
- For `.ipynb` files, include frontmatter (including `image-alt`) in the first cell as a raw cell with YAML between `---` delimiters.
- When a post has both `.qmd` and `.md` files, edit both to keep them in sync (avoids needing to re-render).

## Embedding Videos

Use Quarto's video shortcode in `.qmd` files:

```
{{< video my-video.mp4 >}}
{{< video https://www.youtube.com/watch?v=VIDEO_ID >}}
{{< video my-video.mp4 title="Description for accessibility" >}}
```

**Supported sources:** YouTube, Vimeo, local files (.mp4, .webm, .ogg)

**Optional parameters:** `title`, `width`, `height`, `start` (YouTube only), `aspect-ratio` (1x1, 4x3, 16x9, 21x9)

A Lua filter automatically converts these to Hugo's `video` shortcode when rendering to `hugo-md`. No `resources:` frontmatter needed for local video files.
