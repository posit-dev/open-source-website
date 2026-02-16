---
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

external:
  contributors:
  - hadley
  - thomasp85
  - lionel-
  - yixuan
  - timelyportfolio
  - davidgohel
  - trevorld
  - jeroen
  - mdecorde
  - MichaelChirico
  - vandenman
  - hmalmedal
  - ilia-kats
  - nx10
  - gaborcsardi
  - tjake
  - jimhester
  - pmur002
  description: A lightweight svg graphics device for R
  first_commit: '2012-11-27T14:29:49+00:00'
  forks: 40
  languages:
  - C++
  last_updated: '2026-02-13T14:17:18.573837+00:00'
  latest_release: '2025-10-20T15:57:02+00:00'
  people:
  - Hadley Wickham
  - Thomas Lin Pedersen
  - Lionel Henry
  - Jeroen Ooms
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: r-lib/svglite
  stars: 200
  title: svglite
  website: https://svglite.r-lib.org
---

svglite provides a fast, lightweight graphics device for creating high-quality SVG output from R. Designed as a drop-in replacement for R's built-in `svg()` function, svglite delivers substantially better performance—roughly twice as fast—while producing dramatically smaller file sizes. The package leverages systemfonts to give you access to all installed fonts on your system and supports web font embedding, making it easy to create publication-ready graphics with custom typography. With built-in compression support for `.svgz` files, svglite is ideal for generating web-ready visualizations that need to load quickly.

What sets svglite apart is its focus on editability and real-world workflows. Unlike standard SVG output that converts text to polygons, svglite preserves text as editable `<text>` elements, making it simple to refine your visualizations in design tools like Inkscape or Illustrator. Whether you're rendering dynamic graphics for web delivery, creating figures that need post-production polish, or optimizing bandwidth for interactive dashboards, svglite gives you clean, efficient SVG output without sacrificing the ability to make last-minute adjustments outside of R.
