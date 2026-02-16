---
description: Key-value caches for R
github: r-lib/cachem
languages:
- R
latest_release: '2024-05-15T15:53:45+00:00'
people:
- Winston Chang
- Barret Schloerke
- Jeroen Janssens
title: cachem
website: https://cachem.r-lib.org

external:
  contributors:
  - wch
  - schloerke
  - jimhester
  - lanceupton
  - briandconnelly
  - jeroenjanssens
  - maelle
  - tracykteal
  - bart1
  description: Key-value caches for R
  first_commit: '2018-05-04T15:50:05+00:00'
  forks: 16
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.730604+00:00'
  latest_release: '2024-05-15T15:53:45+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Barret Schloerke
  - Jeroen Janssens
  repo: r-lib/cachem
  stars: 63
  title: cachem
  website: https://cachem.r-lib.org
---

Cachem provides intelligent key-value storage for R with built-in resource management that prevents unbounded memory growth. Unlike standard caching approaches, cachem automatically handles cache eviction through configurable memory limits, age constraints, and flexible policies like least-recently-used (LRU) or first-in-first-out (FIFO). Whether you're optimizing data processing pipelines or building responsive applications, cachem eliminates manual cache management while ensuring predictable resource usage.

The package offers both memory-based and disk-based caching options, each optimized for different use cases. Memory caches provide lightning-fast access and can even store non-serializable R objects, while disk caches enable persistent storage for larger datasets. Cachem's unique sentinel value system for missing keys streamlines error handling, and its support for layered, multi-level cache hierarchies lets you combine the speed of memory with the capacity of disk storage for sophisticated caching strategies.
