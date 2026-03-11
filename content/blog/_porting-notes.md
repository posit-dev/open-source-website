# Blog Porting Notes

Decisions made while porting legacy blog posts to this Hugo site.

## Image alt text: use `image-alt`

**Decision:** Use `image-alt` (with hyphen) for image alt text in frontmatter.

**Rationale:** This is the standard Quarto parameter name, which makes posts more portable between Quarto and Hugo contexts.

**Changes made:**
- Updated all blog templates to read `image-alt` instead of `alttext`
- Updated `archetypes/blog.md` to use `image-alt`
- Documented in `content/blog/CLAUDE.md`

**Migration:** Existing posts using `image_alt` (underscore) need to be updated to `image-alt` (hyphen).

**Note for `.ipynb` files:** Frontmatter (including `image-alt`) must be set in the first cell of the notebook as a raw cell with YAML between `---` delimiters. This needs to be edited in addition to any rendered `.md` file.

## Thumbnail and hero use the same image

Currently, both the post thumbnail (on list pages) and the hero banner (on the post page) use the same image, discovered via `layouts/partials/blog/thumbnail.html`.

**Potential issue:** Some legacy blogs have two separate images — one for the thumbnail and one for the hero banner. May need to add support for distinct `thumbnail` and `image` (hero) fields if this is common.
