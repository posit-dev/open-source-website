---
image: logo.svg
color: "#EE6331"
description: Source of tidyverse.org
github: tidyverse/tidyverse.org
languages:
- HTML
people:
- Hadley Wickham
- Max Kuhn
- Jenny Bryan
- Lionel Henry
- Davis Vaughan
- Thomas Lin Pedersen
- Simon Couch
- Julia Silge
- Emil Hvitfeldt
- Mine Çetinkaya-Rundel
- Gábor Csárdi
- Hannah Frick
- Teun Van den Brand
- George Stagg
- Charlie Gao
- Tomasz Kalinowski
- Edgar Ruiz
- Garrick Aden-Buie
title: tidyverse.org
website: https://tidyverse.org

external:  # updated automatically, do not edit
  description: Source of tidyverse.org
  first_commit: '2017-07-27T12:34:02+00:00'
  forks: 117
  languages:
  - HTML
  last_updated: '2026-03-05T16:21:25.943325+00:00'
  license: CC-BY-SA-4.0
  people:
  - Hadley Wickham
  - Max Kuhn
  - Jenny Bryan
  - Lionel Henry
  - Davis Vaughan
  - Thomas Lin Pedersen
  - Simon Couch
  - Julia Silge
  - Emil Hvitfeldt
  - Mine Çetinkaya-Rundel
  - Gábor Csárdi
  - Hannah Frick
  - Teun Van den Brand
  - George Stagg
  - Charlie Gao
  - Tomasz Kalinowski
  - Edgar Ruiz
  - Garrick Aden-Buie
  repo: tidyverse/tidyverse.org
  stars: 210
  title: tidyverse.org
  website: https://tidyverse.org
---

The tidyverse.org repository contains the source code for the tidyverse website, built using hugodown (not blogdown) and Hugo. It allows contributors to create and publish blog posts and event announcements through a two-step rendering process: hugodown converts R Markdown files to Markdown, then Hugo generates the final HTML.

The repository provides a structured workflow for content creation with helper functions like `hugodown::use_tidy_post()` for blog posts and automatic live previews via Netlify for every pull request. The hugodown approach cleanly separates R Markdown rendering from site generation, meaning `.Rmd` files are only rendered when explicitly knitted rather than automatically rebuilt. Contributors can fix small issues directly through pull requests and are encouraged to open issues for larger changes.
