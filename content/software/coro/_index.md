---
description: Coroutines for R
github: r-lib/coro
languages:
- R
latest_release: '2024-11-05T09:52:00+00:00'
people:
- Lionel Henry
- Hadley Wickham
- Daniel Falbel
- Charlie Gao
- Jeroen Janssens
- Tomasz Kalinowski
title: coro
website: https://coro.r-lib.org/

external:
  description: Coroutines for R
  first_commit: '2017-09-27T08:37:42+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-17T11:34:35.335449+00:00'
  latest_release: '2024-11-05T09:52:00+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Hadley Wickham
  - Daniel Falbel
  - Charlie Gao
  - Jeroen Janssens
  - Tomasz Kalinowski
  repo: r-lib/coro
  stars: 181
  title: coro
  website: https://coro.r-lib.org/
---

The coro package implements coroutines for R, which are functions that can be suspended and resumed. It provides two main types: async functions for concurrent programming and generators for iterating over complex sequences.

This package simplifies asynchronous code by using async/await syntax instead of nested promise callbacks, making concurrent operations more readable and maintainable. It supports suspending within loops, conditionals, and error handling blocks, includes debugging capabilities, and integrates with existing R packages like promises, future, and reticulate. The package works by transforming user code into state machines while preserving source references for debugging.
