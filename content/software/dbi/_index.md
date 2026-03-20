---
color: '#9A4665'
description: A database interface (DBI) definition for communication between R and
  RDBMSs
github: r-dbi/DBI
image: logo.svg
languages:
- R
latest_release: '2026-02-24T17:22:15+00:00'
people:
- Hadley Wickham
- Charlie Gao
title: DBI
website: https://dbi.r-dbi.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: A database interface (DBI) definition for communication between R and
    RDBMSs
  first_commit: '2013-10-16T05:17:38+00:00'
  forks: 79
  languages:
  - R
  last_updated: '2026-03-20T10:27:58.941427+00:00'
  latest_release: '2026-02-24T17:22:15+00:00'
  license: LGPL-2.1
  people:
  - Hadley Wickham
  - Charlie Gao
  - Jeroen Janssens
  repo: r-dbi/DBI
  stars: 316
  title: DBI
  website: https://dbi.r-dbi.org
---

DBI is a database interface package for R that provides a standardized front-end API for connecting to and working with database management systems. It defines a common set of methods that work across different databases through backend-specific packages like RPostgres, RMariaDB, RSQLite, and odbc.

The package solves the problem of database-specific code by providing a unified interface inspired by similar systems in other languages (Perl's DBI, Java's JDBC, Python's DB-API). It supports essential database operations including connections, query execution, result extraction, transaction management, and metadata retrieval. This means you can write R code that works with multiple database systems by only changing the backend driver, not your application logic.
