---
description: Fast map implementation for R
github: r-lib/fastmap
languages:
- C++
latest_release: '2024-05-14T17:53:33+00:00'
people:
- Winston Chang
- Barret Schloerke
- Jenny Bryan
title: fastmap
website: https://r-lib.github.io/fastmap/

external:
  contributors:
  - wch
  - schloerke
  - jennybc
  - tracykteal
  description: Fast map implementation for R
  first_commit: '2019-04-18T18:07:06+00:00'
  forks: 8
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.094204+00:00'
  latest_release: '2024-05-14T17:53:33+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Barret Schloerke
  - Jenny Bryan
  repo: r-lib/fastmap
  stars: 135
  title: fastmap
  website: https://r-lib.github.io/fastmap/
---

Fastmap provides high-performance data structures for R developers who need efficient key-value stores, stacks, and queues in their applications. Built with C++, it addresses a critical performance limitation in R's native environments: when storing or accessing keys, traditional R environments intern every key into R's symbol table, which never gets garbage collected. For long-running processes with dynamically generated keys, this creates memory leakage and progressively degrades performance as the symbol table expands. Fastmap eliminates this problem entirely by storing keys as C++ strings, ensuring consistent memory usage and performance even under heavy workloads.

The package is particularly valuable for data scientists and developers building production systems, interactive applications, or long-running analytics pipelines where memory efficiency and predictable performance are essential. Fastmap implements a hopscotch hash map internally for fast lookups while maintaining compatibility with R's serialization capabilities. Whether you're caching computation results, managing session state, or implementing custom data structures, fastmap delivers the speed and reliability needed for demanding R applications without the hidden costs of symbol table pollution.
