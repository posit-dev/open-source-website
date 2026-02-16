---
description: A promise library for R
github: rstudio/promises
image: logo.svg
languages:
- R
latest_release: '2025-11-05T18:06:35+00:00'
people:
- Joe Cheng
- Barret Schloerke
- Winston Chang
- Charlie Gao
- Garrick Aden-Buie
- Carson Sievert
- Christophe Dervieux
title: promises
website: https://rstudio.github.io/promises/

external:
  contributors:
  - jcheng5
  - schloerke
  - wch
  - shikokuchuo
  - gadenbuie
  - Copilot
  - yihui
  - HenrikBengtsson
  - cpsievert
  - cderv
  - daattali
  - rpodcast
  - maxheld83
  - pawelru
  description: A promise library for R
  first_commit: '2017-04-11T18:52:38+00:00'
  forks: 17
  languages:
  - R
  last_updated: '2026-02-13T14:17:02.734850+00:00'
  latest_release: '2025-11-05T18:06:35+00:00'
  license: NOASSERTION
  people:
  - Joe Cheng
  - Barret Schloerke
  - Winston Chang
  - Charlie Gao
  - Garrick Aden-Buie
  - Carson Sievert
  - Christophe Dervieux
  readme_image: man/figures/logo.svg
  repo: rstudio/promises
  stars: 210
  title: promises
  website: https://rstudio.github.io/promises/
---

The promises package brings asynchronous programming capabilities to R, enabling developers to write non-blocking code that keeps applications responsive during long-running operations. By implementing promise-based patterns familiar to developers from other languages, promises allows you to handle multiple concurrent operations without freezing the user interface. This is particularly valuable for building scalable Shiny applications where database queries, API calls, or complex computations would otherwise block the entire app while waiting for results.

With seamless integration with task launchers like future and mirai, promises makes it straightforward to execute code asynchronously and coordinate the results. The library provides intuitive APIs for combining multiple promises, handling errors, and managing complex async workflows. Whether you're building interactive dashboards that need to remain responsive or data pipelines that benefit from concurrent processing, promises helps you write cleaner, more efficient R code that scales to meet the demands of modern web applications and data science workflows.
