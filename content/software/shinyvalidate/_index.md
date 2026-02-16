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
  contributors:
  - rich-iannone
  - jcheng5
  - cpsievert
  - schloerke
  - daattali
  - dependabot[bot]
  description: Input validation package for the Shiny web framework
  first_commit: '2020-07-23T00:20:44+00:00'
  forks: 10
  languages:
  - JavaScript
  last_updated: '2026-02-13T14:17:04.797939+00:00'
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

Building reliable Shiny applications means ensuring that user inputs are valid before they're processed. shinyvalidate provides a comprehensive framework for adding input validation to your Shiny apps, displaying clear, contextual error messages directly adjacent to problematic inputs where users naturally expect feedback. Unlike Shiny's built-in validation which only shows errors in downstream outputs, shinyvalidate catches issues at the source, making it immediately obvious to users what needs to be corrected.

The package offers a flexible validation system through its InputValidator object, supporting everything from simple required field checks to complex custom validation rules. Whether you need to validate email formats, numeric ranges, conditional requirements, or create entirely custom validators, shinyvalidate handles it with an intuitive R API. It works seamlessly with standard Shiny inputs, supports validation within Shiny modules, and provides programmatic access to validation results, giving you complete control over when and how validation occurs in your application workflow.
