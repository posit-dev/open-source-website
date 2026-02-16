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

external:
  contributors:
  - wch
  - jcheng5
  - schloerke
  - gadenbuie
  - cpsievert
  - nealrichardson
  - hcorrada
  - jeroen
  - alandipert
  - shikokuchuo
  - yihui
  - atheriel
  - gifi
  - MattSandy
  - PromyLOPh
  - LHaferkamp
  - rundel
  - QuLogic
  - gtritchie
  - nstrayer
  - salim-b
  - sebastian-c
  - ZainRizvi
  - hadley
  - ismirsehregal
  description: HTTP and WebSocket server package for R
  first_commit: '2013-02-01T16:17:25+00:00'
  forks: 87
  languages:
  - C
  last_updated: '2026-02-13T14:17:01.209807+00:00'
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

httpuv provides low-level socket and protocol support for handling HTTP and WebSocket requests directly from within R. Built on the robust libuv and http-parser C libraries, httpuv enables developers to create performant web servers and handle real-time bidirectional communication without blocking R's main computational thread. Its multithreaded architecture ensures that network I/O operations run separately from R callback functions, making it an essential foundation for building responsive web applications and APIs.

While httpuv functions primarily as an infrastructure component for higher-level packages like Shiny and plumber, it offers powerful capabilities for developers who need fine-grained control over HTTP server behavior. Key features include customizable request handling through callback functions, efficient static file serving that operates entirely within its I/O thread, and comprehensive WebSocket support for event-driven applications. Whether you're building interactive dashboards, REST APIs, or real-time data streaming applications, httpuv provides the reliable networking foundation that keeps your R-based web services running smoothly.
