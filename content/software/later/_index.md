---
color: '#447099'
description: Schedule an R function or formula to run after a specified period of
  time
github: r-lib/later
image: logo.svg
languages:
- C++
latest_release: '2026-03-05T12:53:35+00:00'
people:
- Winston Chang
- Joe Cheng
- Charlie Gao
- Barret Schloerke
- Carson Sievert
- Jeroen Janssens
- Jeroen Ooms
title: later
website: https://later.r-lib.org/

external:  # updated automatically, do not edit
  description: Schedule an R function or formula to run after a specified period of
    time
  first_commit: '2017-03-17T21:11:40+00:00'
  forks: 31
  languages:
  - C++
  last_updated: '2026-03-05T16:27:06.581632+00:00'
  latest_release: '2026-03-05T12:53:35+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Joe Cheng
  - Charlie Gao
  - Barret Schloerke
  - Carson Sievert
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/later
  stars: 148
  title: later
  website: https://later.r-lib.org/
---

The later package enables scheduling of R functions to execute after a specified delay, similar to JavaScript's setTimeout function. Since R is single-threaded, scheduled operations run when control returns to the top-level prompt to avoid reentrancy issues.

The package provides both R and C++ interfaces for deferred execution, supports file descriptor monitoring for asynchronous I/O operations like reading from TCP sockets, and includes a BackgroundTask C++ class for safely executing computationally expensive work on background threads. This makes it useful for building responsive applications that need to handle time-delayed callbacks or non-blocking I/O without freezing the R session.
