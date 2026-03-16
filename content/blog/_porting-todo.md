# Porting TODO

## Priority 1: Before launch

### Link checking

See `_link-checks.md` for workflow.

- [ ] Fix rstudio blog localhost errors (after content cull)
- [ ] Find links to legacy blog URLs (e.g., `https://shiny.posit.co/blog/posts/...`) that now point to posts on this site — convert to internal links

### Taxonomy cleanup

- [ ] Audit `tags`, `categories`, `ported_from` — decide on consistent scheme
- [ ] Populate `software` taxonomy to link posts to `/software/` pages
- [ ] Evaluate rstudio.com `blogcategories` field — map to site categories or remove?

### Frontmatter sync

Source files (`.Rmd`, `.Rmarkdown`) don't have the same frontmatter as rendered files (`.md`, `.markdown`). Re-rendering would lose `people`, `ported_from`, `image`, etc.

- [x] ~~Sync source frontmatter for: tidyverse, education, ai blogs~~ — Created `_editing-ported-posts.md` guide instead. Syncing all posts upfront isn't worth the effort; guide documents what to do before re-rendering.

## Priority 2: Should do

### People/authors

- [ ] Audit `people` entries not linking to `/people/` pages
- [ ] Policy for former employees and external contributors
- [ ] Fix remaining combined author names (e.g., "Name1 and Name2")

### Missing metadata

- [ ] Add `image-alt` to ported posts (accessibility)
- [ ] Consider `photo` attribution in templates (tidyverse has `photo.author`, `photo.url`)

## Priority 3: Nice to have

### Hero images

- [ ] Audit quality — many are low resolution
- [ ] Decide minimum standards
- [ ] Generate placeholders for posts without heroes?

### New post guide

- [ ] Contributor guide for new blog posts
- [ ] Document frontmatter fields
- [ ] Create archetypes

### Rendering improvements

- [ ] Quarto video shortcodes render as links — create Hugo `video` shortcode
- [ ] Quarto tabsets don't render as tabs — investigate Hugo/CSS solution
- [ ] Shinylive embeds need CSS for adequate height/width
- [ ] `# <<` line-highlight markers left in some posts (cosmetic)

## Known limitations

### Responsive images disabled

Memory errors on CI with 700+ images. Markdown images now render as simple `<img>` tags. Hero images still get responsive processing.

**File:** `layouts/_default/_markup/render-image.html`

### Bootstrap classes stripped

A Lua filter strips Bootstrap classes during rendering. Posts with heavy Bootstrap usage may have degraded styling (missing icons, button styles, layout utilities).

**Heaviest usage:** shiny-r-1.8.0 (57 classes), bslib-dashboards (20), bslib-tooltips (18)

### Shinylive components

- `shiny-r-1.8.0`: shinylive extension doesn't work with hugo-md format
- `introducing-component-layouts`: components render but need CSS for sizing

### Dark mode images

Posts with `.dark-content` / `.light-content` image pairs have dark versions removed (we don't support dark mode).

**Affected:** 2025-10-13-1.8-release, 2025-10-20-quarto-wizard-1-0-0, 2025-05-19-quarto-codespaces

### AI blog bibliographies

Posts with bibliographies don't get a "References" heading. Would need post-processing or full Quarto project.

### Stub shortcodes

These exist but need implementation:
- `test-drive-cloud.html` — used by `2023/purrr-walk-this-way`
- `webr-init.html` / `webr-editor.html` — used by webr posts
- `prerelease-docs-url.html` — outputs nothing, links go to main docs instead of prerelease

## Reference: Issues fixed during porting

<details>
<summary>Click to expand historical fixes</summary>

### Build-blocking fixes

| Issue | Posts |
|-------|-------|
| Tags as string instead of array | education: 2020-04-08-announcing-2020-interns, 2020-02-24-applications-for-2020-intern-program-are-now-open |
| Duplicate YAML keys | tidyverse: 2019/dplyr-0-8-1 |
| Malformed frontmatter | tidyverse: 2023/pak-0-6-0 |
| Invalid image file (text, not PNG) | tidyverse: 2018/tibble-1-4-1 |
| R Markdown chunks in .markdown | tidyverse: roxygen2-7-0-0, odbc-1-2-0, roxygen2-7.1.0 |
| Tweet shortcode format | tidyverse: 2019/tidy-dev-day-toulouse |

### Combined author names split

Used `scripts/fix-people.sh`: stacks-0-1-0, tidyselect-1-2-0, postprocessing-preview, s7-0-2-0, broom-0-7-0, air, air-0-7-0, purrr-1-1-0-parallel, duckplyr-1-1-0, tune-2, three-new-tidymodels-packages, corrr-0-4-3, dplyr-1-0-0-last-minute-additions, data-trail

### AI blog manual renders

- 2018-07-17-activity-detection — HTML extraction (no source)
- 2019-07-09-feature-columns — added `emo` package
- 2020-07-30-state-of-the-art-nlp-models-from-r — manual render

### Shiny blog fixes

- Code block syntax: ```` ``` {python} ```` → ```` ```python ```` (shiny-side-of-llms-part-3)
- shinychat-tool-ui iframe removed (didn't render well)
- code-fold fixed by removing `engine: markdown`

### Lua filters created

- `escape-shortcodes` — escapes `{{<` in code blocks
- `remove-interlinks` — strips great-tables API interlinks
- `strip-bootstrap` — removes Bootstrap classes

</details>

## Posts needing manual review

| Post | Issue |
|------|-------|
| quarto/2024-07-02-beautiful-tables-in-typst | Complex freeze structure, needs manual porting |
| education/2019-09-24-welcome | Very blog-specific ("Welcome to education.rstudio.com") |
| education/2019-08-26-learner-personas | Was draft in source |
| ai/2018-07-17-activity-detection | Blank on legacy blog, marked as draft |
| ai/2017-09-06-keras-for-r | Broken external image (keras.rstudio.com) |
