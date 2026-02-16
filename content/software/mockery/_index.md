---
description: A mocking library for R.
github: r-lib/mockery
languages:
- R
latest_release: '2025-09-03T20:06:59+00:00'
people:
- Hadley Wickham
title: mockery
website: ''

external:
  contributors:
  - n-s-f
  - jimhester
  - lbartnik
  - hadley
  - lbartnikmsft
  - nsfinkelstein
  - damianooldoni
  - dbast
  - frbl
  - MichaelChirico
  - sambrightman
  - kjohnsen
  description: A mocking library for R.
  first_commit: '2016-07-18T18:54:06+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.054364+00:00'
  latest_release: '2025-09-03T20:06:59+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  repo: r-lib/mockery
  stars: 104
  title: mockery
  website: ''
---

Mockery is a testing library for R that makes it easy to replace functions with substitutes during testing. When writing unit tests, you often need to isolate the code you're testing from external dependencies like database connections, API calls, or even base R functions. Mockery's stub function lets you temporarily replace these dependencies with fixed return values or alternative implementations, while mock objects let you verify exactly how functions were called and what arguments they received. This is particularly valuable for testing code that depends on external resources or for mocking R primitives that other tools can't handle.

Note that mockery is now superseded by testthat's built-in mocking functionality. For new test suites, developers should use testthat::local_mocked_bindings() instead, which provides similar capabilities with better integration into the testthat framework.
