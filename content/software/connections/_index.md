---
color: '#213245'
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

external:  # updated automatically, do not edit
  description: https://rstudio.github.io/connections/
  first_commit: '2019-09-06T12:49:39+00:00'
  forks: 4
  languages:
  - R
  last_updated: '2026-03-05T16:15:19.258118+00:00'
  latest_release: '2023-12-18T23:41:21+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  - Hadley Wickham
  readme_image: man/figures/connection-1.png
  repo: rstudio/connections
  stars: 59
  title: connections
  website: https://rstudio.github.io/connections/
---

The `connections` package integrates DBI-compliant database packages (like RPostgres, RSQLite, RMariaDB, and bigrquery) with the RStudio IDE's Connection Pane. It provides `connection_open()` and `connection_close()` functions that work like `dbConnect()` but automatically display database connections, tables, and views in RStudio's interface.

The package solves the problem of managing database connections and queries by providing visual integration with RStudio and persistence through the `pins` package. It supports `dplyr` operations like `tbl()` and `copy_to()` that automatically update the Connections pane when tables change. You can pin both database connections and dplyr queries, storing the code needed to recreate them rather than the data itself, which enables reproducible database workflows across sessions.
