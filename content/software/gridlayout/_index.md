---
description: Package for setting up CSS grid layouts in Shiny apps or RMarkdown documents
github: rstudio/gridlayout
image: geyser_demo.png
languages:
- HTML
people:
- Nick Strayer
title: gridlayout
website: https://rstudio.github.io/gridlayout

external:
  contributors:
  - nstrayer
  description: Package for setting up CSS grid layouts in Shiny apps or RMarkdown
    documents
  first_commit: '2021-02-17T21:57:27+00:00'
  forks: 4
  languages:
  - HTML
  last_updated: '2026-02-13T14:17:05.105405+00:00'
  license: NOASSERTION
  people:
  - Nick Strayer
  readme_image: man/figures/geyser_demo.png
  repo: rstudio/gridlayout
  stars: 44
  title: gridlayout
  website: https://rstudio.github.io/gridlayout
---

Building dashboard-style layouts for Shiny applications and RMarkdown documents traditionally requires wrestling with complex CSS or HTML positioning code. gridlayout simplifies this process by leveraging modern CSS Grid technology through an intuitive, visual syntax. Instead of writing intricate layout logic, you define your dashboard structure using character vectors where elements are visually aligned, making the overall design immediately apparent in your code.

The package offers flexible implementation options to match your needs: `grid_page()` for full-page layouts, `grid_container()` for custom-sized grids, and `grid_nested()` for hierarchical structures. Built-in responsive design ensures your dashboards adapt seamlessly across different screen sizes, while RMarkdown integration through `use_gridlayout_rmd()` enables grid layouts by matching section headers to layout elements. Whether you're a data scientist building interactive applications or a developer creating polished reports, gridlayout democratizes professional dashboard creation without requiring deep CSS expertise.
