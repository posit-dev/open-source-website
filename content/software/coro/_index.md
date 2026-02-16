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
  contributors:
  - lionel-
  - hadley
  - dfalbel
  - shikokuchuo
  - jeroenjanssens
  - t-kalinowski
  - brookslogan
  - olivroy
  description: Coroutines for R
  first_commit: '2017-09-27T08:37:42+00:00'
  forks: 12
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.586578+00:00'
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

Coro brings coroutines to R, enabling functions that can suspend and resume execution. This powerful capability unlocks two essential programming patterns: async functions for concurrent operations and generators for elegant iteration over complex sequences. Instead of wrestling with nested callbacks and promise chains, you can write asynchronous code that reads naturally while remaining non-blocking, making it ideal for handling multiple data streams, API calls, or long-running computations without freezing your R session.

The package integrates seamlessly with R's ecosystem, supporting suspension within loops, conditionals, and error handlers while maintaining full debuggability with browser() and step-through debugging. Coro works harmoniously with the promises package for asynchronous operations, the future package for parallel computing, and reticulate for Python interoperability. Whether you're building responsive Shiny applications, orchestrating complex data pipelines, or working with streaming data, coro provides the tools to write cleaner, more maintainable concurrent code without sacrificing R's interactive development experience.
