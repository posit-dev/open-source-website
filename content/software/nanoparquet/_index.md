---
color: '#447099'
description: R package to read and write Parquet files
github: r-lib/nanoparquet
image: logo.svg
languages:
- C++
latest_release: '2026-09-15T19:12:37+00:00'
people:
- Gábor Csárdi
title: nanoparquet
topics:
- Data Wrangling
website: https://nanoparquet.r-lib.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: R package to read and write Parquet files
  first_commit: '2024-03-30T15:40:31+00:00'
  forks: 8
  languages:
  - C++
  last_updated: '2026-09-18T14:31:03.759026+00:00'
  latest_release: '2026-09-15T19:12:37+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/nanoparquet
  stars: 85
  title: nanoparquet
  website: https://nanoparquet.r-lib.org/
---

`nanoparquet` is an R package that reads and writes flat (non-nested) Parquet files. It provides a lightweight, dependency-free solution for working with a common subset of the Parquet format.

The package supports most Parquet data types and compression methods (Snappy, Gzip, Zstd). It can read column subsets and append data to existing files without rewriting the entire file. It offers competitive performance on speed, memory use, and file size compared to other tools, though it requires reading data into memory rather than supporting out-of-memory operations.
