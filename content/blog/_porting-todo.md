# Porting TODO

Track specific issues found while porting posts. Address these after bulk porting is complete.

## Responsive image processing disabled

**File:** `layouts/_default/_markup/render-image.html`

The responsive image processing (webp conversion, multiple sizes) was disabled due to memory errors when building with 700+ rstudio.com images. The CI environment ran out of memory during the webp conversion step.

**What changed:** Markdown images (`![alt](image.png)`) now render as simple `<img>` tags instead of `<picture>` elements with multiple srcset sizes and webp variants.

**What still works:** Hero images and other images processed via templates (not the markdown render hook) still get responsive processing.

**To re-enable later:**
1. Consider processing only images under a size threshold
2. Or reduce the number of responsive sizes (was: 320, 640, 960, 1280, 1600, 1920)
3. Or add caching/incremental builds
4. Test on CI before merging

**Original template:** Based on https://www.brycewray.com/posts/2023/05/better-code-image-processing-hugo-render-hook-edition/

## Cross-blog links

Links between legacy blogs that need updating once both posts are ported.

| Post | Link | Target |
|------|------|--------|
| plumber2-0-2-0 | `https://shiny.posit.co/blog/posts/shiny-r-1.12/` | Shiny blog |
| dplyr-performance | `https://tidyverse.org/blog/2026/02/dplyr-1-2-0/` | tidyverse blog (ported as dplyr-1-2-0) |
| shiny-python-1.0 | `https://shiny.posit.co/blog/posts/shiny-python-general-availability/` | Shiny blog |
| shiny-python-1.0 | `https://shiny.posit.co/blog/posts/shiny-express/` | Shiny blog |

## Broken legacy links

Posts where slug doesn't match original - investigate when porting that blog:

| Post | Issue |
|------|-------|
| sparklyr-updates-q1-2024 | AI blog original slug is `sparklyr-updates` not `sparklyr-updates-q1-2024` |

## Missing metadata

To address in bulk after porting:

- [ ] Add `image-alt` to all ported posts
- [ ] Populate `software` taxonomy to link posts to software pages
- [ ] Consider adding `photo` attribution to templates (tidyverse posts have `photo.author` and `photo.url`)
- [ ] Consider using `author:` URLs from education posts (preserved markdown links with author websites)

## Issues fixed during bulk port

These were fixed to unblock the build. Please verify manually.

### Education blog fixes

**Tags as string instead of array:**
- `2020-04-08-announcing-2020-interns` - changed `tags: internship` to `tags: [internship]`
- `2020-02-24-applications-for-2020-intern-program-are-now-open` - changed `tags: internship` to `tags: [internship]`

### Duplicate YAML keys
- `2019/dplyr-0-8-1/index.markdown` - had duplicate `tags:` key, removed duplicate

### Malformed frontmatter
- `2023/pak-0-6-0/index.md` - had orphaned `hugodown::md_document` line, removed

### Invalid image files
- `2018/tibble-1-4-1/index.png` - was text file not PNG, deleted

### R Markdown code chunks in `.markdown` files
Converted `{r, ...}` code blocks to plain `r` blocks:
- `2019/roxygen2-7-0-0/index.markdown`
- `2019/odbc-1-2-0/index.markdown`
- `2020/roxygen2-7.1.0/index.markdown`

### Tweet shortcode
- `2019/tidy-dev-day-toulouse/index.markdown` - replaced `{{% tweet %}}` with comment (shortcode format changed)

### Combined author names
Split "Name1 and Name2" or "Name1, Name2, and Name3" into separate `people` entries using `scripts/fix-people.sh`:
- `2020/stacks-0-1-0`
- `2022/tidyselect-1-2-0`
- `2024/postprocessing-preview`
- `2024/s7-0-2-0`
- `2020/broom-0-7-0`
- `2025/air`
- `2025/air-0-7-0`
- `2025/purrr-1-1-0-parallel`
- `2025/duckplyr-1-1-0`
- `2025/tune-2`
- `2025/three-new-tidymodels-packages`
- `2020/corrr-0-4-3`
- `2020/dplyr-1-0-0-last-minute-additions`
- `2023/data-trail`

## Missing shortcodes

Created stub shortcodes in `layouts/shortcodes/` (need implementation):
- `test-drive-cloud.html` - used by `2023/purrr-walk-this-way`
- `webr-init.html` / `webr-editor.html` - used by webr posts

### .markdown files not processed by porting script

83 `.markdown` files (2017-2020) were copied but not transformed. Fixed with `scripts/fix-markdown-files.sh` which:

### .html files not processed by porting script

41 `index.html` files (2017-2019) had YAML frontmatter but weren't transformed. Fixed with `scripts/fix-html-files.sh` which:
- Converted `author:` to `people:`
- Added `image: thumbnail-wd.jpg`
- Added `ported_from: tidyverse` and `port_status: raw`

## Posts to evaluate for porting

Some posts may be too blog-specific to port (e.g., welcome posts, blog announcements):

| Source | Post | Issue |
|--------|------|-------|
| education | 2019-09-24-welcome | "Welcome to education.rstudio.com" - very blog-specific |

### Draft posts

Some source posts have `draft: true` and won't appear on the site. Evaluate whether to skip or publish.

| Source | Post | Notes |
|--------|------|-------|
| education | 2019-08-26-learner-personas | Was draft in source |

Check for drafts with:
```bash
grep -l "draft: true" content/blog/education/*/index.markdown
```

## rstudio.com blog fields to evaluate

The rstudio.com blog has additional frontmatter fields preserved during porting:

- `blogcategories` - broader category groupings (e.g., "Products and Technology", "Open Source", "Company News and Events")
- `events: blog` - appears on most posts, unclear purpose
- `categories` / `tags` - topic tags (e.g., "Shiny", "Packages")

Evaluate whether to:
1. Map `blogcategories` to site categories
2. Keep/remove `events` field
3. Migrate `categories`/`tags` to site taxonomies

## Other observations

Record any issues or notes discovered during porting here.
