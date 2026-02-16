---
description: Connect to ODBC databases (using the DBI interface)
github: r-dbi/odbc
image: logo.png
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

external:
  contributors:
  - jimhester
  - detule
  - simonpcouch
  - hadley
  - devbww
  - krlmlr
  - devjgm
  - jmcphers
  - atheriel
  - shrektan
  - edgararuiz
  - blairj09
  - javierluraschi
  - jeroen
  - khotilov
  - vkapartzianis
  - wibeasley
  - gaborcsardi
  - meztez
  - rnorberg
  - hoxo-m
  - sharon-wang
  - vh-d
  - stevecondylios
  - s-fleck
  - barracuda156
  - mnel
  - schuemie
  - lberki
  - kevinushey
  - jonmcalder
  - jeroenjanssens
  - jschelbert
  - aryoda
  - davidchall
  - But2ene
  - bschwedler
  - she3o
  - alexkowa
  description: Connect to ODBC databases (using the DBI interface)
  first_commit: '2016-07-13T19:32:07+00:00'
  forks: 116
  languages:
  - C++
  last_updated: '2026-02-13T14:17:21.970424+00:00'
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
  stars: 407
  title: odbc
  website: https://odbc.r-dbi.org/
---

odbc is a high-performance R package that provides a DBI-compliant interface for connecting to major database systems including SQL Server, Oracle, Databricks, and Snowflake. Built on the nanodbc C++ library, it offers a faster alternative to older ODBC packages while providing a standardized, consistent API for database operations. Whether you're reading tables, executing queries, or writing data back to your database, odbc delivers the speed and reliability that data scientists need when working with enterprise data sources.

What makes odbc particularly powerful is its seamless integration with modern R workflows. The package provides familiar DBI methods like dbReadTable, dbWriteTable, and dbGetQuery for straightforward database operations, while also supporting memory-efficient iteration over large result sets. When combined with dbplyr, odbc enables you to write dplyr code that automatically translates to optimized SQL, allowing you to work with databases using the same syntax you use for local data frames. This abstraction lets you focus on analysis rather than the complexities of driver configuration and low-level database communication.
