# Porting TODO

Track specific issues found while porting posts. Address these after bulk porting is complete.

## Major remaining tasks

Now that all legacy blogs have been ported (in some form), these major items need attention:

### Link checking

- [ ] Run comprehensive link check across all ported blogs (tidyverse, education, ai, rstudio, shiny, great-tables, pointblank, plotnine, quarto)
- [ ] Fix or document broken external links
- [ ] Update cross-blog links to use internal paths (see "Cross-blog links" section below)

### Taxonomy cleanup

- [ ] Audit, consolidate and separate: `tags`, `categories`, and `ported_from`. Decide on a consistent scheme
- [ ] Populate `software` taxonomy to link posts to `/software/` pages
- [ ] Consider whether to keep or migrate blog-specific taxonomies (e.g., `blogcategories` from rstudio.com)

### People/authors

- [ ] Audit `people` entries - find entries that aren't linking to `/people/` pages
- [ ] Decide policy for former employees (keep page? different treatment?)
- [ ] Decide policy for external contributors/guest authors
- [ ] Handle combined author names that weren't split correctly
- [ ] Consider whether to import author URLs from education posts

### Hero images

- [ ] Audit hero image quality - many ported images are low resolution
- [ ] Decide minimum resolution/quality standards
- [ ] Identify posts needing new/better hero images
- [ ] Consider whether to generate placeholder images for posts without heroes

### New post guide and templates

- [ ] Create contributor guide for writing new blog posts
- [ ] Document frontmatter fields and when to use them
- [ ] Create archetypes

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

## Draft posts (blank on legacy blog)

| Source | Post | Notes |
|--------|------|-------|
| ai | 2018-07-17-activity-detection | Legacy blog page exists but is blank. Marked as draft. |

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
## Quarto video shortcodes render as links

Quarto's `{{< video URL >}}` shortcode gets converted to bare URLs (e.g., `<https://youtu.be/ID>`) during hugo-md rendering. Hugo renders these as clickable links, not embedded video players.

**To fix later:** Create a Hugo `video` shortcode and post-process rendered `.md` files to convert bare video URLs to shortcode calls.

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

## AI blog: failed ports

All initially failed posts have been fixed:
- 2018-07-17-activity-detection - Used HTML extraction (no `.Rmd` source)
- 2019-07-09-feature-columns - Added `emo` package to renv
- 2020-07-30-state-of-the-art-nlp-models-from-r - Rendered manually

## AI blog: missing References heading

Posts with bibliographies don't get a "References" heading before the bibliography entries. The `_metadata.yml` approach didn't work (needs full Quarto project context).

**Options to fix later:**
1. Add `## References` during post-processing
2. Create a Quarto project in `content/blog/ai/`
3. Add manually during review

## Broken external images

Some legacy posts reference external images that are now dead. These are broken on the original blogs too.

| Post | Image URL |
|------|-----------|
| ai/2017-09-06-keras-for-r | `https://keras.rstudio.com/images/training_history_ggplot2.png` |

## Shiny posts: tabsets/panels not rendering

Posts using Quarto tabsets (`::: {.panel-tabset}`) don't render as tabs in Hugo. Example: `shinyswatch-0.7.0` makes heavy use of these.

**Options to investigate:**
- Hugo built-in tab shortcodes or partials
- Lua filter to convert Quarto tabsets to Hugo-compatible HTML
- CSS/JS solution for tab styling

## Shiny posts: broken links sweep

**Status:** ✅ Complete. Updated all cross-references from `https://shiny.posit.co/blog/posts/<slug>/` to `/blog/shiny/<slug>/` in both `.md` and `.qmd` files.

## Shiny posts: `engine: markdown` added

These posts needed `engine: markdown` to prevent Quarto from attempting code execution. This shouldn't normally be necessary — investigate why.

| Post | Reason |
|------|--------|
| shiny-vscode-1.0.0 | Had it in original, preserved during port |

## Shiny posts: code block syntax fixed

Hugo can't parse ```` ``` {python} ```` (with space) — expects ```` ```python ````. Fixed manually with sed after rendering.

| Post | Fix applied |
|------|-------------|
| shiny-side-of-llms-part-3 | `sed 's/``` {python}/```python/g; s/``` {r}/```r/g'` |

**Root cause:** Quarto outputs code blocks with cell options (`#| eval: false` etc.) using ```` ``` {lang} ```` syntax. Consider adding post-processing to the porting script if this is common.

## Shiny posts: shinylive code blocks need manual rendering

`shiny-r-1.8.0` uses `{shinylive-r}` code blocks that require the shinylive Quarto extension. The extension's Lua filter spawns a separate Rscript process that doesn't pick up the renv from the parent directory, causing "no package called 'shinylive'" errors.

**Workaround:** Render manually outside the renv environment (e.g., with global shinylive installed).

**Status:** `shiny-r-1.8.0` was rendered manually, but shinylive components show no output — the extension is optimized for HTML output and doesn't work with hugo-md format.

## Shiny posts: shinylive embeds need CSS styling

`introducing-component-layouts` has shinylive components that render but don't get enough space — often end up with scrollbars.

**To investigate:** Add site-level CSS for shinylive iframes/embeds to ensure adequate height/width.

## Shiny posts: code-fold show/hide

`shiny-side-of-llms-part-3` uses Quarto's `#| code-fold: true` and `#| code-summary: "Show output"` to show/hide code output.

**Status:** Fixed by removing `engine: markdown` and re-rendering with knitr execution. The code-fold features now work correctly.
- Manual conversion during review

## Shiny posts: `# <<` line-highlight markers

Some shiny posts have `# <<` markers at the end of code lines. These were used by the `line-highlight` Quarto extension to highlight specific lines in HTML output. The extension was removed during porting (doesn't work in Hugo).

**Affected posts:**
- introducing-component-layouts
- shinyswatch-0.7.0

**To fix:** Manually remove `# <<` markers from code blocks, or leave them as-is if they serve as useful annotations.

## Shiny posts: Bootstrap classes stripped

A Lua filter (`content/blog/shiny/_extensions/strip-bootstrap/`) strips Bootstrap classes during rendering. This filter was also copied to `content/blog/quarto/_extensions/strip-bootstrap/` for the Quarto blog. These posts had Bootstrap-dependent HTML (buttons, icons, layout) that may need manual review:

| Post | Class count | Notes |
|------|-------------|-------|
| shiny-r-1.8.0 | 57 | Heavy Bootstrap usage |
| bslib-dashboards | 20 | |
| bslib-tooltips | 18 | |
| introducing-component-layouts | 17 | |
| shiny-side-of-llms-part-3 | 12 | |
| conf-2025-shinytalks | 9 | |
| announcing-new-r-shiny-ui-components | 8 | Also has Wistia embed (fixed) |
| shiny-express | 4 | |
| shiny-at-scipy-2025 | 4 | |
| introducing-shiny-templates | 3 | |
| shiny-vscode-1.0.0 | 2 | |
| shinychat-tool-ui | 1 | |
| shiny-r-1.8.1 | 1 | |
| shiny-python-1.0 | 1 | |
| conf-2023-recap-andrew-holz | 1 | |

**What was stripped:**
- Button styling (`btn btn-primary` → plain `<a>`)
- Icons (`bi bi-*`, `fas fa-*` → empty `<i>`)
- Spacing/layout utilities (`my-4`, `d-flex`, etc.)
- Jekyll code classes (`language-plaintext highlighter-rouge`)

**To verify:** Check these posts render acceptably without Bootstrap styling. Consider adding Bootstrap Icons CDN if icons are important.

## Frontmatter mismatch: source vs rendered files

Some ported blogs transformed frontmatter only in the rendered file (`.md`, `.markdown`), not the source (`.Rmd`, `.Rmarkdown`, `.qmd`). Re-rendering would lose changes like:
- `author` → `people` conversion
- Added `ported_from`, `port_status`
- Added `image`, `image-alt`

**Affected blogs:**
- tidyverse (`.Rmd` source, `.md` rendered)
- education (`.Rmarkdown` source, `.markdown` rendered)
- ai (`.Rmd` source, `.md` rendered)

**Shiny blog is OK** — script transforms `.qmd` first, then renders.

**To fix:** Update source files to match rendered frontmatter, or accept that re-rendering requires re-applying transformations.

## Shiny posts: shinychat-tool-ui iframe removed

The original post had an iframe embedding `feature/index.html` with complex scaling. This didn't render well in Hugo, so the iframe was removed and the post now relies on the hero image.

The `feature/` folder with the interactive HTML demo is still present if needed later. Added `'shinychat-tool-ui/feature/'` to `ignoreFiles` in `hugo.toml` to prevent Hugo from rendering it as a page.

## Shiny posts: broken external links

Discovered via `lychee --base http://localhost:1313 content/blog/shiny/*/index.md`

**404 - Dead links:**
| URL | Post |
|-----|------|
| https://www1.ncdc.noaa.gov/pub/data/normals/1981-2010/... | weather-lookup-about |
| https://www.ncdc.noaa.gov/data-access/land-based-station-data/... | weather-lookup-about |
| https://rstudio.github.io/bslib/articles/layouts.html | bslib-dashboards |
| https://rstudio.github.io/shinyuieditor/articles/ui-editor-live-demo.html | shinyuieditor-out-of-alpha |
| https://shinyconf.appsilon.com/state-of-shiny-2023/ | shiny-python-0.6.1 |
| https://github.com/rstudio/bslib/tree/main/inst/examples/flights | bslib-dashboards |
| https://github.com/rstudio/otel | shiny-r-1.12 |
| https://shiny.posit.co/py/api/express.ui.layout_columns.html | responsive-shiny-layouts |
| https://shiny.posit.co/py/docs/workflow-server.html | shiny-on-hugging-face |
| https://shiny.posit.co/py/api/ExTooltip.html | shiny-python-0.5.0 |
| https://shiny.posit.co/py/docs/r-quickstart.html | shiny-python-general-availability |
| https://shiny.posit.co/r/articles/build/bookmarking-state/ | shinychat-tool-ui |

**Connection errors (may be temporary or blocking bots):**
- `https://reg.conf.posit.co/flow/posit/positconf23/...` (conf-2023 posts)

**GitHub user 404s (accounts deleted/renamed):**
- kangjf1943, KRRLP-PL, MalteSteinCytel, oozbeker-onemagnify, jonathanmburns, ngoodkindGSI, bioinformzhang, howardbaek, MartinBaumga, TopBottomTau, toxintoxin, dependabot[bot]

## great-tables: interlinks filter

**Location:** `content/blog/great-tables/remove-interlinks.lua` and `_metadata.yml`

The great-tables blog used Quarto's interlinks feature to create backtick-style links to API docs (e.g., `` [`cols_width()`](`~great_tables.GT.cols_width`) ``). These rendered as URL-encoded links like `%60great_tables.GT.cols_width%60` in the output.

**Solution:** Added `remove-interlinks.lua` Lua filter that strips these during rendering. Re-render any posts that have `%60great_tables` in the output.

**Note:** This only handles backtick-style interlinks. Regular reference paths (like `../../../../reference/google_font.qmd`) must be manually converted to full URLs (e.g., `https://posit-dev.github.io/great-tables/reference/google_font.html`).

## great-tables: broken external links

| Post | URL | Notes |
|------|-----|-------|
| introduction-0.4.0 | `https://docs.pola.rs/user-guide/expressions/lists/` | 404 - page may have moved |
| polars-dot-style | `https://fastht.ml/gallery/split_view?category=visualizations&project=great_tables_tables` | 404 - FastHTML gallery link |

## great-tables, pointblank, plotnine: relative links

These posts have relative links to docs/examples that need fixing:

**great-tables:**
- introduction-0.2.0
- introduction-0.13.0
- polars-styling (links to `../../../../get-started/...`)
- bring-your-own-df
- polars-dot-style
- septa-timetables

**pointblank:**
- lets-workshop-together
- overhauled-user-guide

**Pattern:** Links like `../../../../get-started/basic-styling.qmd` should become `https://posit-dev.github.io/great-tables/get-started/basic-styling.html`

## Link checking for other blogs

Run link checking on other ported blogs:
- [ ] tidyverse
- [ ] education
- [ ] ai
- [ ] rstudio
- [x] great-tables
- [x] pointblank
- [x] plotnine

## Quarto blog: manual attention needed

**`2024-07-02-beautiful-tables-in-typst`** - Has complex freeze structure with embedded examples in subdirectories rather than a main index freeze. Needs manual porting/rendering.

## Quarto blog: relative links to quarto.org docs

**Status:** ✅ Fixed. Converted `../docs/` and `/docs/` links to `https://quarto.org/docs/...` and changed `.qmd` extensions to `.html`. Fixes applied to both `.qmd` source files and include files (`_quarto-1.3-feature.qmd`, `_quarto-1.9-feature.qmd`, `docs/authoring/_brand-example.qmd`) so they persist through re-renders.

## Quarto blog: broken external links

Discovered via `lychee --base http://localhost:1313 content/blog/quarto/*/index.md`

**404 - Dead links:**
| URL | Post |
|-----|------|
| https://www.r-consortium.org/r-medicine-quarto-for-reproducible-medical-manuscripts | 2022-07-28-rstudio-conf-2022-quarto |

**Connection errors (may be blocking bots):**
- `https://reg.conf.posit.co/flow/posit/positconf24/...` (conf-2024 posts)

**Malformed links (fixed manually):**
- `2023-12-07-quarto-dashboards-demo` - YouTube link had incorrect format

**Lychee false positives:**
Running `lychee --base http://localhost:1313` against the `.md` files reports many image 404s (e.g., `/callouts.png`, `/2023-03-13-code-annotation/annotation.png`). These are false positives - lychee doesn't account for Hugo's `/blog/quarto/` URL prefix. The relative image paths resolve correctly when pages are rendered. Verify by checking actual URLs like `http://localhost:1313/blog/quarto/2023-03-13-code-annotation/annotation.png`.

## Quarto blog: dark-content images

Posts with light/dark image pairs (`.dark-content` / `.light-content` classes) have the dark versions removed during rendering. The strip-bootstrap Lua filter removes elements with `dark-content` class entirely since we don't support dark mode.

**Affected posts:**
- 2025-10-13-1.8-release
- 2025-10-20-quarto-wizard-1-0-0
- 2025-05-19-quarto-codespaces

## Quarto blog: shortcodes

### Solved: Examples in code blocks

Hugo parses `{{<` even inside fenced code blocks. Fixed with a Lua filter that escapes shortcodes during `hugo-md` render.

**Filter:** `content/blog/quarto/_extensions/escape-shortcodes/escape-shortcodes.lua`

Converts `{{< shortcode >}}` to `{{</* shortcode */>}}` in code blocks so Hugo displays them as literal text.

### Stub shortcode: `prerelease-docs-url`

**Post:** `2026-03-05-pdf-accessibility-and-standards` (5 uses)

**Original behavior:** `{{< prerelease-docs-url 1.9 >}}` outputs `prerelease.` to create URLs like `https://prerelease.quarto.org/...`

**Current fix:** Empty stub shortcode at `layouts/shortcodes/prerelease-docs-url.html` outputs nothing. Links point to `https://quarto.org/...` instead of prerelease docs.

**To implement properly:** Output version prefix like `prerelease.` based on argument.



## Other observations

Record any issues or notes discovered during porting here.
