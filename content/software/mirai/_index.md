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
  contributors:
  - shikokuchuo
  - jcheng5
  - cgiachalis
  - jeroenjanssens
  - karangattu
  - mcol
  - boshek
  - sebffischer
  - wlandau
  - VincentGuyader
  description: Minimalist Async Evaluation Framework for R
  first_commit: '2022-02-14T22:11:55+00:00'
  forks: 17
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.620449+00:00'
  latest_release: '2026-02-13T11:36:25+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  - Joe Cheng
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/mirai
  stars: 298
  title: mirai
  website: https://mirai.r-lib.org/
---

mirai is a minimalist async evaluation framework that brings high-performance parallel computing to R. It enables you to send computational tasks to background processes without blocking your main session, delivering microsecond-level response times through an event-driven architecture built on NNG and nanonext. By supporting dynamic scaling from local laptops to HPC clusters and cloud platforms, mirai makes it easy to write code that runs efficiently whether you're prototyping on your machine or deploying to production infrastructure.

What makes mirai essential for modern R development is its deep integration across the R ecosystem. It powers the official R parallel backend, purrr's parallel mapping functions, Shiny's async task execution, and tidymodels' parallel infrastructure. With features like distributed tracing, OpenTelemetry observability, and cross-language data support for torch, Arrow, and Polars, mirai provides production-grade capabilities while maintaining a clean, minimalist design. Whether you're building responsive Shiny applications, running large-scale data science pipelines with targets, or orchestrating complex parallel workflows, mirai delivers the scalability and reliability needed for professional data science work.
