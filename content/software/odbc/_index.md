---
color: '#8BABDB'
description: Connect to ODBC databases (using the DBI interface)
github: r-dbi/odbc
image: logo.png
languages:
- C++
latest_release: '2026-09-16T13:52:35+00:00'
people:
- Simon Couch
- Hadley Wickham
- Jonathan McPherson
- Jeroen Ooms
- Edgar Ruiz
- Gábor Csárdi
- Kevin Ushey
title: odbc
topics:
- Data Wrangling
- MLOps and Admin
website: https://odbc.r-dbi.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Connect to ODBC databases (using the DBI interface)
  first_commit: '2016-07-13T19:32:07+00:00'
  forks: 118
  languages:
  - C++
  last_updated: '2026-09-18T14:32:22.109194+00:00'
  latest_release: '2026-09-16T13:52:35+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Hadley Wickham
  - Jonathan McPherson
  - Jeroen Ooms
  - Edgar Ruiz
  - Gábor Csárdi
  - Kevin Ushey
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-dbi/odbc
  stars: 416
  title: odbc
  website: https://odbc.r-dbi.org/
---

The odbc package provides a DBI-compliant interface to ODBC drivers, allowing R users to connect to databases like SQL Server, Oracle, Databricks, and Snowflake.

This package offers a faster alternative to RODBC and RODBCDBI packages, built on the nanodbc C++ library for performance. It works seamlessly with DBI functions for common database operations (reading/writing tables, executing queries) and integrates with dbplyr for automatic SQL generation from dplyr code. The package handles the communication between R and database driver managers, supporting both named data sources and direct driver connections.
