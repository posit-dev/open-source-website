# Blog Authoring Guide

Guidelines for creating new blog posts.

## Images

### Post images

Every post should have an `image` and `image-alt` in the frontmatter:

```yaml
---
title: My Post Title
image: featured.png
image-alt: A descriptive alt text for the image
---
```

The image is used in:
- **Hero banner** on the post page
- **Cards** in blog listings
- **Social previews** (OG/Twitter images)

If no `image` is set:
- Hero: no image shown
- Listings: falls back to parent section's image (if set), otherwise empty
- Social: falls back to generic blog placeholder

### Subsection default images

Blog subsections (e.g., `content/blog/great-tables/`) can set a default image for posts that don't have their own. Add to the subsection's `_index.md`:

```yaml
---
title: Great Tables
image: default-image.png
image-alt: Great Tables logo
---
```

Posts in that folder without an `image` will use this in listings. The `image-alt` is also inherited.

### Image recommendations

- **Format**: PNG, JPG, or WebP (Hugo will generate responsive sizes)
- **Aspect ratio**: 16:9 works well for hero banners
- **Minimum width**: 1200px recommended for sharp display on large screens
- **File location**: Place in the post's folder (same directory as `index.md`)

### Alt text

Always provide meaningful `image-alt` text:
- Describe what the image shows, not just "screenshot" or "logo"
- Keep it concise but informative
- If the image is decorative, you can use the post title as alt text (this is the fallback)
