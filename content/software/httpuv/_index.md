---
description: HTTP and WebSocket server package for R
github: rstudio/httpuv
languages:
- C
latest_release: '2025-04-16T08:39:59+00:00'
people:
- Winston Chang
- Joe Cheng
- Barret Schloerke
- Garrick Aden-Buie
- Carson Sievert
- Neal Richardson
- Jeroen Ooms
- Charlie Gao
- Nick Strayer
- Hadley Wickham
title: httpuv
website: https://rstudio.github.io/httpuv/

external:  # updated automatically, do not edit
  description: HTTP and WebSocket server package for R
  first_commit: '2013-02-01T16:17:25+00:00'
  forks: 88
  languages:
  - C
  last_updated: '2026-02-24T09:26:14.399256+00:00'
  latest_release: '2025-04-16T08:39:59+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Joe Cheng
  - Barret Schloerke
  - Garrick Aden-Buie
  - Carson Sievert
  - Neal Richardson
  - Jeroen Ooms
  - Charlie Gao
  - Nick Strayer
  - Hadley Wickham
  repo: rstudio/httpuv
  stars: 248
  title: httpuv
  website: https://rstudio.github.io/httpuv/
---

httpuv provides low-level socket and protocol support for handling HTTP and WebSocket requests directly from within R. It uses a multithreaded architecture where I/O is handled on one thread and R callbacks are handled on another.

This package is primarily intended as a building block for other packages rather than for creating complete web applications directly. It can serve static files entirely within the I/O thread without blocking R, and it supports WebSocket connections in addition to standard HTTP requests. httpuv is built on top of the libuv and http-parser C libraries for reliable, high-performance network communication.
