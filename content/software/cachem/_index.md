---
color: '#419599'
description: Key-value caches for R
github: r-lib/cachem
image: logo.svg
languages:
- R
latest_release: '2024-05-15T15:53:45+00:00'
people:
- Winston Chang
- Barret Schloerke
- Jeroen Janssens
title: cachem
website: https://cachem.r-lib.org

external:  # updated automatically, do not edit
  description: Key-value caches for R
  first_commit: '2018-05-04T15:50:05+00:00'
  forks: 16
  languages:
  - R
  last_updated: '2026-03-05T16:27:59.403596+00:00'
  latest_release: '2024-05-15T15:53:45+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Barret Schloerke
  - Jeroen Janssens
  repo: r-lib/cachem
  stars: 64
  title: cachem
  website: https://cachem.r-lib.org
---

cachem provides R objects for creating and managing key-value caches with automatic memory and age-based pruning to prevent unbounded growth. It offers both in-memory and disk-based storage options that can be used interchangeably through a consistent API.

The package handles cache misses by returning a sentinel value rather than NULL or throwing exceptions, which simplifies error handling and prevents race conditions in multi-process scenarios. It supports automatic eviction policies (LRU and FIFO), customizable size and age limits, and can layer multiple caches together to create multi-level storage hierarchies. Memory caches avoid serialization overhead and preserve object references, while disk caches enable larger storage capacity and can be shared across multiple R processes using the same directory.
