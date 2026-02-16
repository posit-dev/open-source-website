---
description: Tools for load testing Shiny applications
github: rstudio/shinyloadtest
image: slt_report_screenshot.png
languages:
- HTML
latest_release: '2026-02-09T14:55:05+00:00'
people:
- Barret Schloerke
- Joe Cheng
- Winston Chang
- Davis Vaughan
- Hadley Wickham
title: shinyloadtest
website: https://rstudio.github.io/shinyloadtest/

external:
  contributors:
  - alandipert
  - schloerke
  - bborgesr
  - jcheng5
  - wch
  - ajwtech
  - DavisVaughan
  - rpodcast
  - hadley
  - kota7
  - ColinFay
  description: Tools for load testing Shiny applications
  first_commit: '2017-02-14T06:46:53+00:00'
  forks: 22
  languages:
  - HTML
  last_updated: '2026-02-13T14:17:02.671127+00:00'
  latest_release: '2026-02-09T14:55:05+00:00'
  people:
  - Barret Schloerke
  - Joe Cheng
  - Winston Chang
  - Davis Vaughan
  - Hadley Wickham
  readme_image: man/figures/slt_report_screenshot.png
  repo: rstudio/shinyloadtest
  stars: 112
  title: shinyloadtest
  website: https://rstudio.github.io/shinyloadtest/
---

shinyloadtest provides a scientific approach to evaluating how your Shiny applications perform under real-world traffic conditions. Instead of guessing whether your app can handle dozens or thousands of concurrent users, shinyloadtest enables you to conduct rigorous load tests that reveal your application's true capacity and identify performance bottlenecks before they impact users. The toolkit works through a straightforward three-step process: record a typical user session, replay it in parallel to simulate multiple simultaneous users with the shinycannon command-line tool, and analyze the results through detailed HTML reports that highlight performance patterns.

Whether you're preparing for a product launch, scaling existing applications, or optimizing infrastructure costs, shinyloadtest transforms capacity planning from speculation into data-driven decision making. The framework helps you estimate maximum concurrent user capacity, pinpoint whether bottlenecks exist in your code or infrastructure, and make informed optimization choices. By enabling developers and administrators to horizontally scale applications to handle tens of thousands of users, shinyloadtest addresses common misconceptions about Shiny's scalability and empowers teams to deploy production-ready applications with confidence.
