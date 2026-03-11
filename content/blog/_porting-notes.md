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
| tidyverse.org | [Blog](https://www.tidyverse.org/blog/) | hugodown | [GitHub](https://github.com/tidyverse/tidyverse.org) |
| AI blog | [Blog](https://blogs.rstudio.com/ai/) | Distill for R Markdown | [GitHub](https://github.com/rstudio/ai-blog) |
| Shiny | [Blog](https://shiny.posit.co/blog/) | Quarto w/ freeze | [GitHub](https://github.com/rstudio/shiny-dev-center/) |
| Great Tables | [Blog](https://posit-dev.github.io/great-tables/blog/) | Quarto w/ some freeze | [GitHub](https://github.com/posit-dev/great-tables/tree/main/docs/blog) |
| plotnine | [Blog](https://plotnine.org/blog.html) | Quarto w/ some freeze | [GitHub](https://github.com/has2k1/plotnine.org/tree/main/source/blog) |
| pointblank | [Blog](https://posit-dev.github.io/pointblank/blog/) | Quarto w/o freeze | [GitHub](https://github.com/posit-dev/pointblank/tree/main/docs/blog) |
| Quarto | [Blog](https://quarto.org/docs/blog/) | Quarto w/ freeze | [GitHub](https://github.com/quarto-dev/quarto-web) |
| Education blog | [Blog](https://education.rstudio.com/blog/) | blogdown | [GitHub](https://github.com/rstudio/education.rstudio.com) |

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


## tidyverse.org

Blog source: `_external-sources/tidyverse.org/content/blog`

Already uses Hugo (via hugodown). Posts have both `index.Rmd` (source) and `index.md` (rendered).

**Script:** `scripts/port-tidyverse-post.sh <path>`

```bash
./scripts/port-tidyverse-post.sh dplyr-performance
./scripts/port-tidyverse-post.sh 2022/roxygen2-7-2-0
```

Posts in year subfolders are ported preserving the folder structure.

The script:
1. Copies post folder to `content/blog/`
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
./scripts/fix-people.sh content/blog/<path>/index.md
./scripts/fix-people.sh content/blog/<path>/index.Rmd
```
