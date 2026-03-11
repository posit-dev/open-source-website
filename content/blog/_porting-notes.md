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
