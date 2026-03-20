---
color: '#9A4665'
description: A DBI-compliant interface to PostgreSQL
github: r-dbi/RPostgres
image: logo.svg
languages:
- R
latest_release: '2026-02-15T18:53:30+00:00'
people:
- Hadley Wickham
- Jeroen Ooms
title: RPostgres
website: https://rpostgres.r-dbi.org

external:  # updated automatically, do not edit
  description: A DBI-compliant interface to PostgreSQL
  first_commit: '2015-01-05T17:43:02+00:00'
  forks: 79
  languages:
  - R
  last_updated: '2026-03-20T10:27:58.969153+00:00'
  latest_release: '2026-02-15T18:53:30+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jeroen Ooms
  repo: r-dbi/RPostgres
  stars: 337
  title: RPostgres
  website: https://rpostgres.r-dbi.org
---

RPostgres is a DBI-compliant R interface for connecting to and querying PostgreSQL databases. It provides a modern implementation built with C++ that allows R users to interact with PostgreSQL through standard DBI methods.

The package offers several technical advantages including full support for parameterized queries to prevent SQL injection, automatic cleanup of connections and result sets to prevent memory leaks, and performance improvements that reduce query overhead by approximately 5ms compared to the older RPostgreSQL package. It relies on the system libpq library for a simplified build process and provides complete DBI compatibility for standard database operations like reading, writing, and querying data.
