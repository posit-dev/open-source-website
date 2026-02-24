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

external:  # updated automatically, do not edit
  description: Tools for load testing Shiny applications
  first_commit: '2017-02-14T06:46:53+00:00'
  forks: 22
  languages:
  - HTML
  last_updated: '2026-02-24T09:26:16.214430+00:00'
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

The `shinyloadtest` package, along with the `shinycannon` command-line tool, enables load testing of deployed Shiny applications to estimate how many concurrent users an application can support. It helps developers and administrators determine if their app can handle expected traffic levels.

Load testing with `shinyloadtest` identifies performance bottlenecks and guides infrastructure, configuration, or code improvements. The workflow involves recording a typical user session, replaying it in parallel to simulate multiple simultaneous users, and analyzing the results through automated reports. This approach provides concrete evidence that Shiny applications can scale to handle large numbers of users when properly configured.
