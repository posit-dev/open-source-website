---
description: R package to read and write Parquet files
github: r-lib/nanoparquet
languages:
- C++
latest_release: '2025-12-16T21:21:31+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: nanoparquet
website: https://nanoparquet.r-lib.org/

external:
  description: R package to read and write Parquet files
  first_commit: '2024-03-30T15:40:31+00:00'
  forks: 6
  languages:
  - C++
  last_updated: '2026-02-17T11:37:01.497507+00:00'
  latest_release: '2025-12-16T21:21:31+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/nanoparquet
  stars: 79
  title: nanoparquet
  website: https://nanoparquet.r-lib.org/
---

`nanoparquet` is an R package that reads and writes flat (non-nested) Parquet files. It provides a lightweight, dependency-free solution for working with a common subset of the Parquet format.

The package supports most Parquet data types and compression methods (Snappy, Gzip, Zstd). It can read column subsets and append data to existing files without rewriting the entire file. It offers competitive performance on speed, memory use, and file size compared to other tools, though it requires reading data into memory rather than supporting out-of-memory operations.
