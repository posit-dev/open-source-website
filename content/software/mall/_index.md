---
color: '#404041'
description: Run multiple LLM predictions against a data frame with R and Python
github: mlverse/mall
image: mall.png
languages:
- R
latest_release: '2025-08-18T21:07:21+00:00'
people:
- Edgar Ruiz
title: mall
website: https://mlverse.github.io/mall/

external:  # updated automatically, do not edit
  description: Run multiple LLM predictions against a data frame with R and Python
  first_commit: '2024-08-30T16:00:49+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-09-18T14:19:32.094905+00:00'
  latest_release: '2025-08-18T21:07:21+00:00'
  people:
  - Edgar Ruiz
  readme_image: site/images/favicon/apple-touch-icon-180x180.png
  repo: mlverse/mall
  stars: 129
  title: mall
  website: https://mlverse.github.io/mall/
---

mall is a package for R and Python that runs LLM predictions against a data frame, processing each row of a specified column using a one-shot prompt. It enables batch LLM operations directly within tabular data workflows.

The package integrates LLM calls into familiar data frame operations, making it straightforward to apply tasks like classification, sentiment analysis, or text extraction across an entire column without writing manual loops or API boilerplate. It works row-wise, pairing a pre-determined prompt with each row's content, so results stay aligned with the source data.
