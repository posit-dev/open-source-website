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
  contributors:
  - gaborcsardi
  - hannes
  - yutannihilation
  - jeroenjanssens
  - Mytherin
  - eitsupi
  description: R package to read and write Parquet files
  first_commit: '2024-03-30T15:40:31+00:00'
  forks: 6
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.703402+00:00'
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

nanoparquet is a lightweight R package that enables efficient reading and writing of Parquet files without requiring any external dependencies. Parquet is a columnar storage format widely used in data engineering and analytics workflows for its excellent compression and performance characteristics. With nanoparquet, you can seamlessly integrate Parquet files into your R data pipelines while maintaining competitive speed, memory efficiency, and file sizes compared to other tools. The package supports essential features like selective column reading, multiple compression methods (Snappy, Gzip, and Zstd), and proper preservation of R-specific data types including factors and temporal types.

What makes nanoparquet particularly valuable is its zero-dependency architecture and practical focus on flat tabular data. Unlike heavier alternatives, it provides a streamlined solution that's easy to deploy in any R environment without dependency conflicts or complex setup. The package also offers append functionality, allowing you to add data to existing Parquet files without reprocessing entire datasets—a feature that streamlines iterative analysis and incremental data workflows. Whether you're exchanging data with other analytics platforms, optimizing storage for large datasets, or building reproducible data pipelines, nanoparquet delivers a reliable, self-contained tool that fits naturally into data science and development workflows.
