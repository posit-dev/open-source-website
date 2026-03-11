---
description: Markdown Parser and Renderer for R Graphics
github: r-lib/marquee
image: logo.png
color: "#8E896E"
languages:
- C
latest_release: '2025-09-15T13:31:09+00:00'
people:
- Thomas Lin Pedersen
- Teun Van den Brand
title: marquee
website: https://marquee.r-lib.org

external:  # updated automatically, do not edit
  description: Markdown Parser and Renderer for R Graphics
  first_commit: '2024-04-16T20:01:24+00:00'
  forks: 10
  languages:
  - C
  last_updated: '2026-03-05T16:30:21.016785+00:00'
  latest_release: '2025-09-15T13:31:09+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Teun Van den Brand
  readme_image: man/figures/logo.png
  repo: r-lib/marquee
  stars: 98
  title: marquee
  website: https://marquee.r-lib.org
---

Marquee is a markdown parser and renderer designed specifically for R's graphics engine, allowing you to render rich text formatted as markdown inside R graphics like ggplot2 or grid-based visualizations. The core function `marquee_grob()` creates a grid graphical object (grob) from markdown text that can be styled and drawn.

The package fully supports the CommonMark specification and uses a powerful textshaping backend to render text with customizable fonts, colors, and backgrounds. Unlike similar tools that parse HTML, marquee focuses exclusively on markdown syntax, making it a cleaner option for developers who want markdown-native text rendering in R graphics. It provides a straightforward way to add formatted documentation, labels, or annotations directly into plots without dealing with HTML or CSS complexity.
