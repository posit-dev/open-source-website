# Blog Post Instructions

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
| `description` | Summary for list pages and SEO (keep under 160 chars) |
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
| `ported_from` | Source blog (e.g., "tidyverse", "shiny", "quarto", "posit") |
| `port_status` | Porting progress: `raw`, `in-progress`, `review`, `complete` |

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
- `categories` — Topical only: news, education, releases, programming
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

For `.ipynb` files, include frontmatter (including `image-alt`) in the first cell as a raw cell with YAML between `---` delimiters.
