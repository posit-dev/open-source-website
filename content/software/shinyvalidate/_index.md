---
description: Input validation package for the Shiny web framework
github: rstudio/shinyvalidate
image: demo.gif
languages:
- JavaScript
latest_release: '2023-10-05T22:06:32+00:00'
people:
- Rich Iannone
- Joe Cheng
- Carson Sievert
- Barret Schloerke
title: shinyvalidate
website: https://rstudio.github.io/shinyvalidate/

external:
  description: Input validation package for the Shiny web framework
  first_commit: '2020-07-23T00:20:44+00:00'
  forks: 10
  languages:
  - JavaScript
  last_updated: '2026-02-17T11:23:41.880636+00:00'
  latest_release: '2023-10-05T22:06:32+00:00'
  license: NOASSERTION
  people:
  - Rich Iannone
  - Joe Cheng
  - Carson Sievert
  - Barret Schloerke
  readme_image: man/figures/demo.gif
  repo: rstudio/shinyvalidate
  stars: 116
  title: shinyvalidate
  website: https://rstudio.github.io/shinyvalidate/
---

shinyvalidate adds input validation capabilities to Shiny applications. It allows developers to define validation rules for user inputs and display error messages directly next to the relevant input fields.

The package uses an InputValidator object to manage validation rules, with built-in validators for common requirements like required fields and email addresses. It works with all standard Shiny inputs and most custom inputs following Bootstrap conventions. Unlike Shiny's built-in validation which only shows errors in downstream outputs, shinyvalidate displays feedback next to the incorrect input where users expect it.
