---
description: Schedule an R function or formula to run after a specified period of
  time
github: r-lib/later
languages:
- C++
latest_release: '2026-01-08T08:06:53+00:00'
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

external:
  contributors:
  - wch
  - jcheng5
  - shikokuchuo
  - schloerke
  - cpsievert
  - MichaelChirico
  - batpigandme
  - jeroenjanssens
  - jeroen
  - mingwandroid
  - tracykteal
  description: Schedule an R function or formula to run after a specified period of
    time
  first_commit: '2017-03-17T21:11:40+00:00'
  forks: 31
  languages:
  - C++
  last_updated: '2026-02-13T14:17:19.370547+00:00'
  latest_release: '2026-01-08T08:06:53+00:00'
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

The later package brings asynchronous programming capabilities to R by enabling you to schedule functions or formulas to execute after a specified delay. Similar to JavaScript's `setTimeout` function, later allows you to defer operations, create responsive applications, and handle background tasks without blocking your interactive R session. This is particularly valuable for building Shiny applications that need to perform long-running computations, scheduled updates, or asynchronous I/O operations while maintaining a responsive user interface.

Beyond basic delayed execution, later provides advanced features like file descriptor monitoring for asynchronous I/O operations with TCP sockets and other resources, making it a foundation for building scalable network-enabled applications in R. The package includes built-in reentrancy protection to prevent overlapping code execution and offers C++ integration through its API, allowing package developers to schedule callbacks from both the main R thread and background threads. When combined with the promises package, later enables sophisticated asynchronous workflows that can transform how you handle time-consuming operations in data analysis pipelines and interactive applications.