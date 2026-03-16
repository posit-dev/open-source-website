# Blog Porting Notes

Decisions made while porting legacy blog posts to this Hugo site.

## Tracking Progress

Use `/blog/all/` to monitor porting progress. The table shows:
- Metadata completeness (image, image-alt, people)
- Whether authors have pages in `/people/`
- Source blog and porting status

## Legacy Blogs

Shallow clones of all legacy blog repos are in `/_external-sources/` (ignored by git and Hugo).

| Blog | Live | Current Tech | Source |
|------|------|--------------|--------|
| positron | [Blog](https://positron.posit.co/blog/) | Quarto | [GitHub](https://github.com/posit-dev/positron-website) |
| tidyverse.org | [Blog](https://www.tidyverse.org/blog/) | hugodown | [GitHub](https://github.com/tidyverse/tidyverse.org) |
| AI blog | [Blog](https://blogs.rstudio.com/ai/) | Distill for R Markdown | [GitHub](https://github.com/rstudio/ai-blog) |
| Shiny | [Blog](https://shiny.posit.co/blog/) | Quarto w/ freeze | [GitHub](https://github.com/rstudio/shiny-dev-center/) |
| Great Tables | [Blog](https://posit-dev.g ithub.io/great-tables/blog/) | Quarto w/ some freeze | [GitHub](https://github.com/posit-dev/great-tables/tree/main/doc s/blog) |
| plotnine | [Blog](https://plotnine.org/blog.html) | Quarto w/ some freeze | [GitHub](https://github.com/has2k1/plotnine.org/tree/main/source/blog) |
| pointblank | [Blog](https://posit-dev.github.io/pointblank/blog/) | Quarto w/o freeze | [GitHub](https://github.com/posit-dev/pointblank/tree/main/docs/blog) |
| Quarto | [Blog](https://quarto.org/docs/blog/) | Quarto w/ freeze | [GitHub](https://github.com/quarto-dev/quarto-web) |
| Education blog | [Blog](https://education.rstudio.com/blog/) | blogdown | [GitHub](https://github.com/rstudio/education.rstudio.com) |
| RStudio blog | Some on <https://posit.co/blog/> | hugo | [GitHub](https://github.com/gregswinehart/rstudio.com) |

### Content file types

Blogs with pre-rendered static files (.md, .markdown, .html) are easier to port than those requiring code execution (.qmd, .Rmd, .ipynb).

| Blog | Posts path | Static files | Needs rendering |
|------|------------|--------------|-----------------|
| positron-website | blog/posts | - | 1 qmd (static, no code) |
| education.rstudio.com | content/blog | 85 markdown + 5 md | 85 Rmarkdown (have rendered .markdown) |
| ai-blog | _posts | 97 html | 140 Rmd |
| shiny-dev-center | blog/posts | 1 html | 46 qmd |
| quarto-web | docs/blog/posts | - | 37 qmd |
| great-tables | docs/blog | - | 22 qmd |
| pointblank | docs/blog | - | 6 qmd |
| plotnine.org | source/blog | - | 3 qmd |
| rstudio.com | content/blog | 544 md + 21 html | - (all pre-rendered) |

## Image alt text: use `image-alt`

**Decision:** Use `image-alt` (with hyphen) for image alt text in frontmatter.

**Rationale:** This is the standard Quarto parameter name, which makes posts more portable between Quarto and Hugo contexts.

**Changes made:**
- Updated all blog templates to read `image-alt` instead of `alttext`
- Updated `archetypes/blog.md` to use `image-alt`
- Documented in `content/blog/CLAUDE.md`

**Migration:** Existing posts using `image_alt` (underscore) need to be updated to `image-alt` (hyphen).

**Note for `.ipynb` files:** Frontmatter (including `image-alt`) must be set in the first cell of the notebook as a raw cell with YAML between `---` delimiters. This needs to be edited in addition to any rendered `.md` file.

## Cross-blog links

Posts may contain links to other legacy blogs (e.g., a tidyverse post linking to a Shiny blog post). These links will need updating once both posts are ported.

**Strategy:** Port all posts first, then do a sweep to update cross-references. Record specific instances in `_porting-todo.md`.

## Thumbnail and hero use the same image

Currently, both the post thumbnail (on list pages) and the hero banner (on the post page) use the same image, discovered via `layouts/partials/blog/thumbnail.html`.

**Potential issue:** Some legacy blogs have two separate images — one for the thumbnail and one for the hero banner. May need to add support for distinct `thumbnail` and `image` (hero) fields if this is common.

## Folder structure

During porting, posts are organized by source blog:

```
content/blog/
├── tidyverse/       # tidyverse.org posts
│   ├── 2017/
│   ├── 2018/
│   └── ...
├── education/       # education.rstudio.com posts
│   ├── 2019-09-24-welcome/
│   └── ...
└── ...              # other posts (not ported)
```

This preserves original folder structures and makes it easy to track porting progress. Folder structure can be flattened later if desired.

---

## tidyverse.org

Blog source: `_external-sources/tidyverse.org/content/blog`
Destination: `content/blog/tidyverse/`

Already uses Hugo (via hugodown). Posts have both `index.Rmd` (source) and `index.md` (rendered).

**Script:** `scripts/port-tidyverse-post.sh <path>`

```bash
./scripts/port-tidyverse-post.sh dplyr-performance
./scripts/port-tidyverse-post.sh 2022/roxygen2-7-2-0
```

Posts in year subfolders are ported preserving the folder structure.

The script:
1. Copies post folder to `content/blog/tidyverse/`
2. Updates frontmatter in both `.md` and `.Rmd`:
   - Changes `author` → `people`
   - Adds `image: thumbnail-wd.jpg`
   - Adds `ported_from: tidyverse` and `port_status: raw`
3. In `.md` only: removes hugodown fields (`output`, `rmd_hash`, `editor`, `editor_options`)
4. In `.Rmd`: keeps all fields needed for re-rendering

**Config:** `.Rmd` files are ignored by Hugo via `ignoreFiles` in `hugo.toml`.

**After porting:** Check for cross-blog links or other issues and record in `_porting-todo.md`.

**Fix combined authors:** If `people` has names joined by "and" or commas, run:
```bash
./scripts/fix-people.sh content/blog/tidyverse/<path>/index.md
./scripts/fix-people.sh content/blog/tidyverse/<path>/index.Rmd
```

## education.rstudio.com

Blog source: `_external-sources/education.rstudio.com/content/blog`
Destination: `content/blog/education/`

Uses blogdown (similar to hugodown). Posts have both `index.Rmarkdown` (source) and `index.markdown` (rendered).

**Script:** `scripts/port-education-post.sh <folder-name>`

```bash
./scripts/port-education-post.sh 2019-09-24-welcome
./scripts/port-education-post.sh 2020-05-19-learnr-for-remote
```

The script:
1. Copies post folder to `content/blog/education/`
2. Updates frontmatter in both `.markdown` and `.Rmarkdown`:
   - Changes `author` → `people`
   - Adds `ported_from: education` and `port_status: raw`

**Config:** `.Rmarkdown` files are ignored by Hugo via `ignoreFiles` in `hugo.toml`.

**Note on author names:** Education posts often use first names only (e.g., "Alison" instead of "Alison Hill"). After porting, expand to full names for consistency with `/people/` pages.

**Markdown author links:** Some education posts have author names as markdown links (e.g., `[Dewey Dunnington](https://fishandwhistle.net/)`). These are preserved in an `author:` field while `people:` contains just the name. Posts without markdown links only have `people:`.

```yaml
# Post with markdown author link:
author:
  - "[Dewey Dunnington](https://fishandwhistle.net/)"
people:
  - Dewey Dunnington

# Post with plain text author:
people:
  - Alison
```

## rstudio.com

Blog source: `_external-sources/rstudio.com/content/blog`
Destination: `content/blog/rstudio/`

Uses Hugo. Mix of flat `.md` files and folder-based posts (`index.md` or `index.html`).

**Script:** `scripts/port-rstudio-post.sh <path>`

```bash
./scripts/port-rstudio-post.sh 2011-02-27-about-the-rstudio-project
./scripts/port-rstudio-post.sh 2012-11-08-introducing-shiny.md
```

The script handles both folder-based posts and flat `.md` files (converting flat files to folders).

The script:
1. Copies/creates post folder to `content/blog/rstudio/`
2. Updates frontmatter:
   - Changes `authors` → `people`
   - Removes `authormeta` (internal linking slug)
   - Preserves `categories`, `blogcategories`, `tags`, `events`
   - Adds `image: thumbnail.png` if present
   - Adds `ported_from: rstudio` and `port_status: raw`

**Note:** Posts with `index.html` (rendered R Markdown) need the same frontmatter transformation - handled separately after bulk import.

**Fixes applied during import:**
- Created stub shortcode `layouts/shortcodes/conf-form.html`
- Fixed duplicate `date:` key in `2021-08-23-pins-0-4-0-versioning`

## ai-blog (blogs.rstudio.com/ai)

Blog source: `_external-sources/ai-blog/_posts`
Destination: `content/blog/ai/`

Uses Distill for R Markdown. Posts have `*.Rmd` source and `*.html` pre-rendered output (96 posts have both, 44 have Rmd only, 1 has HTML only).

### Approach 1: HTML extraction (script: `port-ai-post.sh`)

Extracts rendered content from the HTML file and converts to markdown via pandoc.

**Script:** `scripts/port-ai-post.sh <folder-name>`

```bash
./scripts/port-ai-post.sh 2017-09-06-keras-for-r
```

**How it works:**
1. Extracts content from `<div class="d-article">` in HTML
2. Converts to markdown using pandoc
3. Transforms frontmatter from Rmd
4. Copies images and source files

**Automatic cleanups:**
- Citations: `[(Author [year](#ref)...)]{.citation cites="id"}` → `[@id]`
- Figure anchors: `[]{#fig:...}` removed
- Empty code blocks and layout divs removed

**Manual fixes still needed:**
- Twitter embeds → Hugo shortcode
- Footnotes: content lost in conversion, copy from `.Rmd`
- Code input vs output: no visual distinction after conversion
- References section: may be out of order

**Limitation:** Distill uses JavaScript to transform footnotes, references, and other elements. Static HTML extraction misses these transformations.

### Approach 2: Quarto rendering (script: `port-ai-post-quarto.sh`)

Renders the `.Rmd` with Quarto to `hugo-md` format. This produces clean markdown with proper footnotes, citations, and code block handling.

**Script:** `scripts/port-ai-post-quarto.sh <folder-name>`

```bash
./scripts/port-ai-post-quarto.sh 2017-09-06-keras-for-r
```

**How it works:**
1. Copies `.Rmd` and all supporting files to `content/blog/ai/<folder>/`
2. Renders with `quarto render <file>.Rmd --to hugo-md`
3. Transforms frontmatter (date format, author → people, etc.)
4. Copies preview image as thumbnail
5. Cleans up intermediate files (.html, *_files/)

**Output:** Files are renamed to `index.md` and `index.Rmd` for Hugo page bundles.

**Shared renv environment:**

Posts in `content/blog/ai/` share an renv environment with common packages (keras, tensorflow, torch, tidyverse, etc.). Files:
- `content/blog/ai/renv.lock` - Package lockfile
- `content/blog/ai/.Rprofile` - Activates renv
- `content/blog/ai/renv/` - Library (gitignored)

To restore the environment:
```r
setwd("content/blog/ai")
renv::restore(exclude = c("gert", "usethis", "devtools", "credentials", "gitcreds", "gh"))
```

The excludes bypass packages requiring libgit2.

**Advantages over Approach 1:**
- Footnotes and citations render correctly
- Code input vs output visually distinct
- No pandoc conversion artifacts

**Known limitation:** The `_metadata.yml` with `reference-section-title: References` doesn't take effect without a full Quarto project. Posts with bibliographies won't have an explicit "References" heading. See `_porting-todo.md` for options.

### Common setup

**Frontmatter transformation:**
- `title`, `description`, `categories` → keep as-is
- `author:` with name/url/affiliation → preserve in `author:`, extract name to `people:`
- `date: MM-DD-YYYY` → `date: YYYY-MM-DD` (ISO format)
- `preview: <path>` → `image: thumbnail.png`
- Add `image-alt`, `ported_from: ai`, `port_status: raw`

**Files to copy:**
- Preview image → `thumbnail.png`
- `images/` folder if present
- Source `.Rmd` for reference

**Config:** `.Rmd` files are ignored by Hugo via `ignoreFiles` in `hugo.toml`.

**Posts without HTML:** 44 posts have only `.Rmd`. List with:
```bash
for d in _external-sources/ai-blog/_posts/*/; do
  [ -z "$(find "$d" -maxdepth 1 -name "*.html")" ] && echo "$(basename $d)"
done
```

---

## shiny.posit.co (Shiny blog)

Blog source: `_external-sources/shiny-dev-center/blog/posts`
Destination: `content/blog/shiny/`

Uses Quarto website/blog format with `.qmd` files. Has a `_freeze` directory at project level.

### Structure

- **47 posts** total (all `.qmd`)
- **38 posts are fully static** (no executable code)
- **9 posts have R code chunks**
- **2 posts have Python code chunks** (shiny-side-of-llms-part-2, part-3)
- **Only 4 posts have freeze files** (bslib-tooltips, shiny-r-1.8.0, shiny-r-1.8.1, shinychat-tool-ui)

### Posts with executable code

| Post | R chunks | Python chunks | Has freeze? |
|------|----------|---------------|-------------|
| bslib-0.9.0 | 3 | 0 | No |
| bslib-dashboards | 1 | 0 | No |
| bslib-tooltips | 1 | 0 | Yes |
| chromote-0.5.0 | 1 | 0 | No |
| shiny-r-1.8.0 | 6 | 0 | Yes |
| shiny-r-1.8.1 | 2 | 0 | Yes |
| shiny-side-of-llms-part-2 | 11 | 16 | No |
| shiny-side-of-llms-part-3 | 2 | 2 | No |
| shinychat-tool-ui | 13 | 0 | Yes |

### Porting approach

**Static posts (38):** Render with `quarto render index.qmd --to hugo-md`, transform frontmatter.

**Posts with freeze (4):** Can use pre-rendered output from freeze files.

**Posts with code but no freeze (5):** Need R/Python environment to render, or convert code to static display.

### Script

**Script:** `scripts/port-shiny-post.sh <folder-name>`

```bash
./scripts/port-shiny-post.sh shiny-on-hugging-face
```

The script:
1. Copies post folder to `content/blog/shiny/`
2. Transforms frontmatter in `.qmd` first:
   - `author` → `people` (as list)
   - `imagealt` → `image-alt`
   - Removes `twitter-card`, `open-graph`, `format` blocks
   - Adds `ported_from: shiny`, `port_status: raw`
3. Renders from `content/blog/shiny/` with `quarto render <post>/index.qmd --to hugo-md`
4. Warns about broken links (site-relative or relative paths that need fixing)

**After porting:** Fix any flagged links in the `.qmd`, then re-render to update `.md`.

### Shared environments

Posts in `content/blog/shiny/` share renv (R) and uv (Python) environments. Render from within `content/blog/shiny/` to use them.

Files:
- `content/blog/shiny/renv.lock` - R package lockfile
- `content/blog/shiny/.Rprofile` - Activates renv
- `content/blog/shiny/pyproject.toml` - Python dependencies

### Watch for: Quarto stripping nested HTML

**Problem:** When rendering `.qmd` to `hugo-md`, Quarto/Pandoc strips nested `<div>` elements from inline HTML. This breaks embeds like Wistia videos.

**Solution:** Wrap complex HTML in a raw HTML block:

```qmd
```{=html}
<script src="..."></script>
<div class="wrapper"><div class="inner">...</div></div>
```
```

**Example:** The `announcing-new-r-shiny-ui-components` post had a Wistia embed that was stripped. Fixed by wrapping in `{=html}` block.

### Watch for: Bootstrap-dependent HTML

Some Shiny blog posts contain HTML designed for Bootstrap (the CSS framework used by Quarto sites). These won't render correctly on the Hugo/Tailwind site.

**Bootstrap classes to strip:**

| Category | Classes | Action |
|----------|---------|--------|
| Buttons | `btn`, `btn-primary`, `btn-outline-*` | Strip (becomes plain link) |
| Icons | `bi bi-*`, `fas fa-*` | Strip (icon won't show) |
| Spacing | `my-*`, `mx-*`, `mb-*`, `mt-*`, `me-*`, `ms-*`, `px-*`, `py-*`, `p-*`, `pt-*` | Strip |
| Layout | `d-flex`, `align-items-*` | Strip |
| Text | `text-muted`, `text-end`, `fw-bold` | Strip |
| Images | `img-fluid`, `shadow`, `img-shadow` | Strip |
| Nav | `nav-item`, `nav-link`, `tab-pane` | Strip (may break tabs) |
| Code | `language-plaintext highlighter-rouge` | Strip (Jekyll artifact) |

**Affected posts (15 of 47):**

| Post | Bootstrap class count |
|------|----------------------|
| shiny-r-1.8.0 | 57 |
| bslib-dashboards | 20 |
| bslib-tooltips | 18 |
| introducing-component-layouts | 17 |
| shiny-side-of-llms-part-3 | 12 |
| conf-2025-shinytalks | 9 |
| announcing-new-r-shiny-ui-components | 8 |
| shiny-express | 4 |
| shiny-at-scipy-2025 | 4 |
| introducing-shiny-templates | 3 |
| shiny-vscode-1.0.0 | 2 |
| shinychat-tool-ui | 1 |
| shiny-r-1.8.1 | 1 |
| shiny-python-1.0 | 1 |
| conf-2023-recap-andrew-holz | 1 |

**Solution:** Use a Quarto Lua filter (`_extensions/strip-bootstrap/strip-bootstrap.lua`) to remove these classes during rendering. See `content/blog/shiny/_quarto.yml` for usage.

### Watch for: shinylive code blocks

Posts using `{shinylive-r}` or `{shinylive-python}` code blocks (interactive Shiny apps in the browser) won't work with `hugo-md` output. The shinylive extension is optimized for HTML output.

**Additional issue:** The shinylive Lua filter spawns a separate Rscript process that doesn't pick up the renv from the parent directory. May need to render these posts manually with global shinylive installed.

**Example:** `shiny-r-1.8.0` was rendered manually.

### Watch for: code-fold and engine: markdown

If a post uses `#| code-fold: true` for collapsible code blocks, **do not** add `engine: markdown` to the frontmatter. The code-fold feature requires knitr execution to work.

**What happened:** Initially added `engine: markdown` to `shiny-side-of-llms-part-3` to prevent execution of `{.python}` display blocks. This broke code-fold. Removing it and re-rendering fixed the issue.

**Note:** `{.python}` (with dot) are display-only blocks that don't execute anyway.

### Watch for: embedded HTML files (iframes)

Some posts embed interactive HTML demos via iframes. These may need adjustment:

1. **Complex scaling** - Original blog CSS/transforms may not work. Simplify or remove.
2. **Subfolder rendering** - If the iframe points to a subfolder like `feature/index.html`, add the folder to `ignoreFiles` in `hugo.toml` to prevent Hugo from rendering it as a page:
   ```toml
   ignoreFiles = [..., 'shinychat-tool-ui/feature/']
   ```
3. **Consider removing** - If the iframe doesn't render well, rely on the hero image instead.

---

## positron.posit.co (Positron blog)

Blog source: `_external-sources/positron-website/blog/posts`
Destination: `content/blog/positron/`

Uses Quarto website/blog format with `.qmd` files. Currently has 1 post.

### Structure

- **1 post** (static, no executable code)
- No freeze files needed

### Porting approach

Simple static posts render directly with `quarto render index.qmd --to hugo-md`.

**Manual porting steps:**
1. Create post folder in `content/blog/positron/<slug>/`
2. Copy `index.qmd`, transform frontmatter:
   - `author` → `people` (as list)
   - Convert site-relative links (`/page.qmd`) to absolute URLs (`https://positron.posit.co/page.html`)
   - Add `ported_from: positron`, `port_status: raw`
3. Render: `cd content/blog/positron && quarto render <slug>/index.qmd --to hugo-md`

**Config:** `content/blog/positron/_quarto.yml` scopes the Quarto project to avoid interference from other blog projects.

### Watch for: video shortcodes

Quarto's `{{< video URL >}}` shortcode renders as a bare URL link (e.g., `<https://youtu.be/ID>`). See "Quarto video shortcodes render as links" in `_porting-todo.md`.

---

## Link checking

Use [lychee](https://github.com/lycheeverse/lychee) to check links in ported posts.

### Running lychee

**Against live dev server (recommended):**
```bash
# Start Hugo dev server first: hugo server
lychee --base-url http://localhost:1313 content/blog/shiny/*/index.md
```

**Offline mode (limited):**
```bash
lychee --offline content/blog/shiny/*/index.md
```

### Interpreting results

**False positives to ignore:**
- **Relative image paths** (e.g., `[500] http://localhost:1313/image.png`) - lychee misresolves relative paths like `![](image.png)` to site root instead of post folder. These work correctly in Hugo.
- **429 Too Many Requests** - GitHub rate limiting. Not broken, just throttled.
- **403 Forbidden** - Some sites block automated requests (NOAA, academic journals).

**Actual issues to fix:**
- **404 Not Found** - Dead external links
- **Relative paths to other site sections** - e.g., `../r/getstarted/` should be `https://shiny.posit.co/r/getstarted/`
- **Root-relative blog links** - e.g., `../blog/posts/foo/` should be `/blog/shiny/foo/`
- **Malformed URLs** - e.g., `../../https://` from sed replacement gone wrong

### Link types to fix during porting

| Pattern | Fix |
|---------|-----|
| `https://shiny.posit.co/blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `../blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `../r/...` or `../py/...` | `https://shiny.posit.co/r/...` or `https://shiny.posit.co/py/...` |
| `https://connect.rstudioservices.com/...` | `https://connect.posit.it/...` |

### After porting each blog

Run lychee and record broken external links in `_porting-todo.md`. Some links may have been broken on the legacy blog too.

---

## great-tables, pointblank, plotnine

These three Python blogs are similar enough to port together using a shared approach.

### Overview

| Blog | Posts | With Python code | Static | Source path |
|------|-------|-----------------|--------|-------------|
| great-tables | 21 | 19 | 2 | `docs/blog/<slug>/` |
| pointblank | 5 | 4 | 1 | `docs/blog/<slug>/` |
| plotnine | 3 | 2 | 1 | `source/blog/<year>/<mo>/<slug>/` |

**Total: 29 posts, 25 need Python execution, none have freeze files.**

### Static posts (no code execution needed)

- great-tables: `marimo-and-great-tables`, `pycon-2024-great-tables-are-possible`
- pointblank: `lets-workshop-together`
- plotnine: `about-plotnine` (in `2017/04/`)

### Similarities

1. All Quarto `.qmd` files with `jupyter: python3`
2. Similar frontmatter: `title`, `author`, `date`
3. No freeze directories — all need fresh rendering
4. Same workflow: copy → transform frontmatter → render hugo-md

### Frontmatter differences

| Aspect | great-tables | pointblank | plotnine |
|--------|-------------|------------|----------|
| Author field | `author: Name` | `author: Name` | Often missing |
| Extra fields | `html-table-processing: none`, `freeze: true` | same | `format:` block |

### Python environments

Each blog has a separate uv environment in `content/blog/<blog>/`:

| Blog | Key dependencies |
|------|-----------------|
| great-tables | `great_tables`, `polars`, `pandas` |
| pointblank | `pointblank`, `polars`, `pandas`, `ibis[duckdb]` |
| plotnine | `plotnine`, `mizani`, `pandas` |

Note: pointblank depends on great_tables internally.

### Porting scripts

Each blog has its own script due to different source paths:

```bash
./scripts/port-great-tables-post.sh design-philosophy
./scripts/port-pointblank-post.sh intro-pointblank
./scripts/port-plotnine-post.sh 2024/11/version-0.14.0
```

Key transformations:
1. `author` → `people` (as list, splits on " and ")
2. Remove `freeze`, `html-table-processing`, `jupyter`, `format`, `aliases` blocks
3. Add `ported_from: <blog>`, `port_status: raw`
4. Render with `uv run quarto render <post>/index.qmd --to hugo-md`

No Bootstrap class stripping needed (unlike Shiny posts).

### Watch for: shortcode-like text in code blocks

Great Tables uses `{{%...%}}` notation for units/chemistry formatting. Hugo interprets `{{%` as a shortcode delimiter, even inside fenced code blocks.

**Fix:** Replace `{{` with `&#123;&#123;` (HTML entities) in both `.qmd` and `.md` files.

**Example:** `tables-for-scientific-publishing` has `{{%NO3%}}` which needed escaping.

---

## WebP processing disabled

Hugo's WASM-based WebP image processor crashes with memory allocation errors when building this site:

```
Error allocating memory for blob data
Error parsing JSON line
panic: call with ID 0 not found
```

The site has ~16,000+ images across ~1,000 blog posts. Processing all of these through the WASM WebP converter exhausts memory.

**Workaround:** Disabled WebP processing in all templates by commenting out `<source type="image/webp">` blocks. The site still serves responsive images via JPEG srcsets.

### Files modified

| File | Changes |
|------|---------|
| `layouts/partials/blog/hero.html` | Commented out WebP source; added GIF exclusion |
| `layouts/partials/blog/related.html` | Commented out WebP source; added GIF exclusion |
| `layouts/categories/list.html` | Commented out 2 WebP sources; added GIF exclusions |
| `layouts/events/term.html` | Commented out WebP processing loop and sources |
| `layouts/resources/term.html` | Commented out WebP processing loop and source |
| `layouts/partials/block/image.html` | Commented out WebP source |
| `layouts/partials/responsive_image_container.html` | Commented out WebP processing |
| `layouts/partials/responsive_image_fixed.html` | Commented out WebP processing |

### To re-enable WebP

If Hugo fixes the WASM memory issue in a future version:

1. Search for `WebP disabled due to Hugo WASM memory issues` in templates
2. Uncomment the `<source type="image/webp">` blocks
3. Uncomment the WebP processing loops (in events/term.html and resources/term.html)
4. Test with a full build: `hugo`
