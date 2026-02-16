---
description: Record and expose Shiny app logic using metaprogramming
github: rstudio/shinymeta
languages:
- R
latest_release: '2021-11-17T15:48:16+00:00'
people:
- Carson Sievert
- Joe Cheng
- Barret Schloerke
- Lionel Henry
title: shinymeta
website: https://rstudio.github.io/shinymeta

external:
  contributors:
  - cpsievert
  - jcheng5
  - schloerke
  - DavidBarke
  - daattali
  - giocomai
  - lionel-
  description: Record and expose Shiny app logic using metaprogramming
  first_commit: '2019-05-09T06:00:50+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-13T14:17:04.132733+00:00'
  latest_release: '2021-11-17T15:48:16+00:00'
  people:
  - Carson Sievert
  - Joe Cheng
  - Barret Schloerke
  - Lionel Henry
  readme_image: https://i.imgur.com/5gNquPE.gif
  repo: rstudio/shinymeta
  stars: 226
  title: shinymeta
  website: https://rstudio.github.io/shinymeta
---

shinymeta transforms your Shiny applications from interactive black boxes into transparent, reproducible workflows by capturing the logic behind your app and exposing it as standalone R code. Using metaprogramming techniques, shinymeta provides special counterparts to Shiny's reactive building blocks (like `metaReactive()` and `metaRender()`) that automatically generate code to recreate what users see in your app, enabling them to reproduce results outside the Shiny runtime.

This capability unlocks powerful possibilities for data science workflows: users can automate analyses with the latest data, download reproducible reports with embedded code, and extend your app's logic in ways you never anticipated. Whether you're building educational tools that help students understand statistical concepts through code, creating exploratory analysis apps where users need permanent records of their work, or developing data dashboards where transparency and reproducibility are essential, shinymeta bridges the gap between interactive exploration and reproducible research. The package makes complex analyses more transparent, helps build user trust through code visibility, and empowers your audience to take ownership of the insights they discover.
