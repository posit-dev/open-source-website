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

external:
  contributors:
  - MichaelChirico
  - truecluster
  - hcirellu
  - ben-schwen
  - dipterix
  - QuLogic
  - jeroenjanssens
  - jeroen
  description: An R package with an S3 Class for Vectors of 64bit Integers
  first_commit: '2020-04-12T17:33:29+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.274531+00:00'
  latest_release: '2025-01-17T04:42:06+00:00'
  people:
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/bit64
  stars: 39
  title: bit64
  website: https://bit64.r-lib.org
---

bit64 extends R's integer handling capabilities by providing a specialized S3 class for working with 64-bit integers. While R's standard integer type is limited to 32-bit values (roughly -2 billion to +2 billion), bit64 enables you to work with much larger integer values that are essential for modern data science workflows. This is particularly valuable when interfacing with databases that use 64-bit integer primary keys, processing large-scale identifiers, handling high-precision timestamps, or maintaining data integrity with external systems that rely on 64-bit integer standards.

What makes bit64 indispensable for many data practitioners is its seamless integration into R's existing ecosystem. The package provides familiar vector operations and methods, allowing you to perform arithmetic, comparisons, and data manipulation on 64-bit integers without sacrificing the intuitive R syntax you already know. Whether you're working with financial data requiring precise integer calculations, managing datasets with identifiers that exceed 32-bit limits, or connecting to enterprise databases, bit64 ensures your integer data remains accurate and efficient throughout your analytical pipeline.
