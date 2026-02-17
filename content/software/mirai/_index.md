---
description: Minimalist Async Evaluation Framework for R
github: r-lib/mirai
image: logo.png
languages:
- R
latest_release: '2026-02-13T11:36:25+00:00'
people:
- Charlie Gao
- Joe Cheng
- Jeroen Janssens
title: mirai
website: https://mirai.r-lib.org/

external:
  description: Minimalist Async Evaluation Framework for R
  first_commit: '2022-02-14T22:11:55+00:00'
  forks: 17
  languages:
  - R
  last_updated: '2026-02-17T11:36:51.527345+00:00'
  latest_release: '2026-02-13T11:36:25+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  - Joe Cheng
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/mirai
  stars: 299
  title: mirai
  website: https://mirai.r-lib.org/
---

mirai is an async evaluation framework for R that enables parallel processing through background daemons (persistent worker processes). It provides a simple interface where `mirai()` evaluates expressions asynchronously and `daemons()` manages the worker pool.

The package uses a hub architecture where daemons connect to a host, allowing dynamic scaling from local machines to HPC clusters and cloud platforms. It features microsecond-level performance through NNG networking, supports custom serialization for torch tensors and Arrow/Polars data formats, and includes distributed tracing via OpenTelemetry. mirai serves as the parallel backend for major R packages including Shiny, purrr, tidymodels, and targets.
