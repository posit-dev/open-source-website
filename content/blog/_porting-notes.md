# Blog Porting Notes

Reference information about the blog porting project. For guidance on editing ported posts, see `_editing-ported-posts.md`.

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

Posts may contain links to other legacy blogs (e.g., a tidyverse post linking to a Shiny blog post). These need updating to point to the new locations on this site. See `_porting-todo.md` for status.

## Thumbnail and hero use the same image

Both the post thumbnail (on list pages) and the hero banner (on the post page) use the same image, discovered via `layouts/partials/blog/thumbnail.html`.

Some legacy blogs had separate thumbnail and hero images. If this becomes an issue, we may need to add support for distinct `thumbnail` and `image` fields.

## Image alt text

We use `image-alt` (with hyphen) for hero image alt text. This matches the Quarto standard.

See `content/blog/CLAUDE.md` for full frontmatter documentation.

## Link checking

See `_link-checks.md` for instructions on running lychee and interpreting results.

## Known limitations (blog only)

These limitations apply only to the blog section to avoid memory issues from processing ~16,000 images.

### Image processing disabled for blog list pages and markdown images

Hugo's WASM-based image processor crashes with memory errors when processing many images at once (e.g., blog list pages). Blog list item thumbnails and markdown images in blog posts are served as-is without responsive srcsets or WebP conversion.

Blog hero images and related post thumbnails still get full responsive/WebP processing (these render one post at a time, not in bulk).

**Files affected:**
- `layouts/partials/item.html` — skips `responsive_image_container.html` for blog items
- `layouts/_default/_markup/render-image.html` — simplified for blog section

## Archived porting scripts

The original porting scripts are in `scripts/archive/`. These were used for bulk porting and are kept for reference only.
