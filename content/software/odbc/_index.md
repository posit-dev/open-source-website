---
description: Connect to ODBC databases (using the DBI interface)
github: r-dbi/odbc
image: logo.png
color: "#8BABDB"
languages:
- C++
latest_release: '2025-12-08T14:40:41+00:00'
people:
- Simon Couch
- Hadley Wickham
- Edgar Ruiz
- Jeroen Ooms
- Gábor Csárdi
- Jeroen Janssens
title: odbc
website: https://odbc.r-dbi.org/

external:  # updated automatically, do not edit
  description: Connect to ODBC databases (using the DBI interface)
  first_commit: '2016-07-13T19:32:07+00:00'
  forks: 116
  languages:
  - C++
  last_updated: '2026-03-05T16:31:37.488227+00:00'
  latest_release: '2025-12-08T14:40:41+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Hadley Wickham
  - Edgar Ruiz
  - Jeroen Ooms
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-dbi/odbc
  stars: 408
  title: odbc
  website: https://odbc.r-dbi.org/
---

The odbc package provides a DBI-compliant interface to ODBC drivers, allowing R users to connect to databases like SQL Server, Oracle, Databricks, and Snowflake.

This package offers a faster alternative to RODBC and RODBCDBI packages, built on the nanodbc C++ library for performance. It works seamlessly with DBI functions for common database operations (reading/writing tables, executing queries) and integrates with dbplyr for automatic SQL generation from dplyr code. The package handles the communication between R and database driver managers, supporting both named data sources and direct driver connections.
