# Blog Porting Notes

Reference information about the blog porting project. For guidance on editing ported posts, see `_editing-ported-posts.md`.

## Notes for future taxonomy work

The rstudio blog posts (557 files) have a `blogcategories` field with values like "Products and Technology", "Company News and Events", "Open Source", "Training and Education". This could inform a `categories` scheme.

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
| Great Tables | [Blog](https://posit-dev.github.io/great-tables/blog/) | Quarto w/ some freeze | [GitHub](https://github.com/posit-dev/great-tables/tree/main/docs/blog) |
| plotnine | [Blog](https://plotnine.org/blog.html) | Quarto w/ some freeze | [GitHub](https://github.com/has2k1/plotnine.org/tree/main/source/blog) |
| pointblank | [Blog](https://posit-dev.github.io/pointblank/blog/) | Quarto w/o freeze | [GitHub](https://github.com/posit-dev/pointblank/tree/main/docs/blog) |
| Quarto | [Blog](https://quarto.org/docs/blog/) | Quarto w/ freeze | [GitHub](https://github.com/quarto-dev/quarto-web) |
| Education blog | [Blog](https://education.rstudio.com/blog/) | blogdown | [GitHub](https://github.com/rstudio/education.rstudio.com) |
| RStudio blog | Some on <https://posit.co/blog/> | hugo | [GitHub](https://github.com/gregswinehart/rstudio.com) |

## Folder structure

Posts are organized by source blog:

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

This preserves original folder structures and makes it easy to track porting progress.

## Cross-blog links

Posts may contain links to other legacy blogs (e.g., a tidyverse post linking to a Shiny blog post). These need updating to point to the new locations on this site. See "Related issues" above.

## Thumbnail and hero use the same image

Both the post thumbnail (on list pages) and the hero banner (on the post page) use the same image, discovered via `layouts/partials/blog/thumbnail.html`.

Some legacy blogs had separate thumbnail and hero images. If this becomes an issue, we may need to add support for distinct `thumbnail` and `image` fields.

## Image alt text

We use `image-alt` (with hyphen) for hero image alt text. This matches the Quarto standard.

See `content/blog/CLAUDE.md` for full frontmatter documentation.

## Link checking

See `_link-checks.md` for instructions on running lychee and interpreting results.

## Known limitations

### Responsive images disabled for blog

Hugo's WASM-based image processor crashes with memory errors when processing many images at once (e.g., blog list pages). Blog list item thumbnails and markdown images in blog posts are served as-is without responsive srcsets or WebP conversion.

Blog hero images and related post thumbnails still get full responsive/WebP processing (these render one post at a time, not in bulk).

**Files affected:**
- `layouts/partials/item.html` — skips `responsive_image_container.html` for blog items
- `layouts/_default/_markup/render-image.html` — simplified for blog section

See https://github.com/posit-dev/open-source-website/issues/44

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

## Posts needing manual review

| Post | Issue |
|------|-------|
| quarto/2024-07-02-beautiful-tables-in-typst | Complex freeze structure, needs manual porting |
| education/2019-09-24-welcome | Very blog-specific ("Welcome to education.rstudio.com") |
| education/2019-08-26-learner-personas | Was draft in source |
| ai/2018-07-17-activity-detection | Blank on legacy blog, marked as draft |
| ai/2017-09-06-keras-for-r | Broken external image (keras.rstudio.com) |

## Archived porting scripts

The original porting scripts are in `scripts/archive/`. These were used for bulk porting and are kept for reference only.

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
