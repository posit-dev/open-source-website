---
image: logo.svg
color: "#E7B10A"
description: An interface to Google's BigQuery from R.
github: r-dbi/bigrquery
languages:
- R
latest_release: '2025-09-10T12:43:44+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Joe Cheng
- Jeroen Janssens
- Edgar Ruiz
- Davis Vaughan
title: bigrquery
website: https://bigrquery.r-dbi.org

external:  # updated automatically, do not edit
  description: An interface to Google's BigQuery from R.
  first_commit: '2013-05-22T14:04:16+00:00'
  forks: 191
  languages:
  - R
  last_updated: '2026-03-05T16:31:21.523329+00:00'
  latest_release: '2025-09-10T12:43:44+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Joe Cheng
  - Jeroen Janssens
  - Edgar Ruiz
  - Davis Vaughan
  repo: r-dbi/bigrquery
  stars: 525
  title: bigrquery
  website: https://bigrquery.r-dbi.org
---

The bigrquery package provides R interfaces for working with Google BigQuery, allowing you to query tables and manage BigQuery resources like projects, datasets, and jobs. It offers three levels of interaction: low-level REST API wrappers, a DBI interface for standard database operations, and a dplyr interface for working with BigQuery tables like in-memory data frames.

The package solves the problem of choosing the right abstraction level for your workflow. The low-level API gives you full control for advanced use cases, the DBI interface lets you write SQL queries and upload data under 100 MB like any other database, and the dplyr interface automatically generates SQL from R code so you don't need to write queries manually. This flexibility makes it suitable whether you're familiar with BigQuery's REST API or prefer working with standard R database tools.
