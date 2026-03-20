---
color: '#F8B13B'
description: A lightweight svg graphics device for R
github: r-lib/svglite
image: logo.png
languages:
- C++
latest_release: '2025-10-20T15:57:02+00:00'
people:
- Hadley Wickham
- Thomas Lin Pedersen
- Lionel Henry
- Jeroen Ooms
- Gábor Csárdi
title: svglite
website: https://svglite.r-lib.org

external:  # updated automatically, do not edit
  description: A lightweight svg graphics device for R
  first_commit: '2012-11-27T14:29:49+00:00'
  forks: 40
  languages:
  - C++
  last_updated: '2026-03-20T10:27:51.623491+00:00'
  latest_release: '2025-10-20T15:57:02+00:00'
  people:
  - Hadley Wickham
  - Thomas Lin Pedersen
  - Lionel Henry
  - Jeroen Ooms
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: r-lib/svglite
  stars: 199
  title: svglite
  website: https://svglite.r-lib.org
---

svglite is an R graphics device that generates clean, web-ready SVG output with text preserved as editable elements rather than converted to polygons.

The package produces significantly smaller files and renders faster than R's built-in svg() device, making it suitable for dynamic web applications. It supports advanced typography features through systemfonts integration, including font discovery, webfont embedding, OpenType features, and custom font registration. The output prioritizes editability, allowing users to open and modify the resulting SVG files in vector graphics editors like Inkscape or Illustrator.
