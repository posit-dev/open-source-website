---
description: https://rstudio.github.io/connections/
github: rstudio/connections
image: connection-1.png
languages:
- R
latest_release: '2023-12-18T23:41:21+00:00'
people:
- Edgar Ruiz
- Hadley Wickham
title: connections
website: https://rstudio.github.io/connections/

external:
  contributors:
  - edgararuiz-zz
  - edgararuiz
  - javierluraschi
  - hadley
  description: https://rstudio.github.io/connections/
  first_commit: '2019-09-06T12:49:39+00:00'
  forks: 4
  languages:
  - R
  last_updated: '2026-02-13T14:17:04.322092+00:00'
  latest_release: '2023-12-18T23:41:21+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  - Hadley Wickham
  readme_image: man/figures/connection-1.png
  repo: rstudio/connections
  stars: 58
  title: connections
  website: https://rstudio.github.io/connections/
---

The connections package bridges the gap between DBI-compliant database packages and RStudio's Connection Pane, streamlining database workflows for data scientists working with R. By providing seamless integration with popular backends like PostgreSQL, SQLite, BigQuery, and MariaDB, connections eliminates the manual overhead of database management and brings database objects directly into your IDE where they're easily discoverable and actionable. The package also extends support to the pins package, enabling you to persistently store and share both connection code and analytical queries across your team.

Key features include connection_open() for launching database connections with automatic pane integration, copy_to() for uploading R data to databases, and tbl() for creating dplyr-compatible table references. The package emphasizes reproducibility by recording connection code rather than storing connection objects, and it preserves your dplyr transformation logic without materializing results prematurely. Whether you're exploring database schemas, running complex queries, or collaborating on data pipelines, connections provides the infrastructure to work efficiently with databases directly from RStudio.
