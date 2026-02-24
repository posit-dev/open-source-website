---
description: Legacy DBI interface for MySQL
github: r-dbi/RMySQL
languages:
- C
latest_release: '2022-12-05T23:01:14+00:00'
people:
- Jeroen Ooms
- Hadley Wickham
- Gábor Csárdi
title: RMySQL
website: http://cran.r-project.org/package=RMySQL

external:  # updated automatically, do not edit
  description: Legacy DBI interface for MySQL
  first_commit: '2012-01-12T17:27:03+00:00'
  forks: 108
  languages:
  - C
  last_updated: '2026-02-24T09:26:38.171070+00:00'
  latest_release: '2022-12-05T23:01:14+00:00'
  people:
  - Jeroen Ooms
  - Hadley Wickham
  - Gábor Csárdi
  repo: r-dbi/RMySQL
  stars: 209
  title: RMySQL
  website: http://cran.r-project.org/package=RMySQL
---

RMySQL is a database interface and MySQL driver for R that implements the DBI specification, allowing R users to connect to MySQL databases and execute SQL queries. This package is being phased out in favor of the newer RMariaDB package.

The package provides a complete implementation of the DBI interface for MySQL, enabling standard database operations like connecting to databases, reading and writing tables, executing queries, and fetching results in chunks. It supports MySQL configuration files for secure credential management and works across multiple platforms including Linux, macOS, and Windows. The implementation offers better compatibility when linked against MariaDB Connector/C rather than Oracle's legacy libmysqlclient driver.
