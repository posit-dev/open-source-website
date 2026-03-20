---
color: '#9A4665'
description: Fast map implementation for R
github: r-lib/fastmap
image: logo.svg
languages:
- C++
latest_release: '2024-05-14T17:53:33+00:00'
people:
- Winston Chang
- Barret Schloerke
- Jenny Bryan
title: fastmap
website: https://r-lib.github.io/fastmap/

external:  # updated automatically, do not edit
  description: Fast map implementation for R
  first_commit: '2019-04-18T18:07:06+00:00'
  forks: 8
  languages:
  - C++
  last_updated: '2026-03-20T10:27:55.393961+00:00'
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

The fastmap package provides fast key-value maps, stacks, and queues for R. Unlike R's standard environment-based maps, fastmap avoids memory leaks and performance degradation that occur when using large numbers of keys.

Standard R environments intern every key as a symbol in R's global symbol table, which is never garbage-collected and slows down all GC operations as it grows. fastmap stores keys as C++ strings instead, preventing memory leaks and maintaining consistent performance even with millions of random keys. This makes it suitable for long-running processes or applications that use dynamically-generated keys.
