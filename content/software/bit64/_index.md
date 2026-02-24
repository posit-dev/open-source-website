---
description: An R package with an S3 Class for Vectors of 64bit Integers
github: r-lib/bit64
languages:
- R
latest_release: '2025-01-17T04:42:06+00:00'
people:
- Jeroen Janssens
- Jeroen Ooms
title: bit64
website: https://bit64.r-lib.org

external:  # updated automatically, do not edit
  description: An R package with an S3 Class for Vectors of 64bit Integers
  first_commit: '2020-04-12T17:33:29+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-24T09:26:36.232511+00:00'
  latest_release: '2025-01-17T04:42:06+00:00'
  people:
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/bit64
  stars: 39
  title: bit64
  website: https://bit64.r-lib.org
---

The bit64 package provides an S3 class for working with 64-bit integers in R. This addresses R's lack of native support for 64-bit integer types, which is needed when working with large identifiers, timestamps, or data that exceeds the 32-bit integer range.

The package enables efficient storage and manipulation of integers that would otherwise require floating-point representation, which can lose precision for large values. It provides arithmetic operations, comparisons, and coercion methods specifically designed for 64-bit integers. This is particularly useful when interfacing with databases, working with large datasets, or handling Unix timestamps and other identifiers that require the full 64-bit integer range.
