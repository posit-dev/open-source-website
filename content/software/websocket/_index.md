---
description: WebSocket client for R
github: rstudio/websocket
image: logo.svg
color: "#CC6699"
languages:
- C++
latest_release: '2025-04-10T10:24:20+00:00'
people:
- Winston Chang
- Joe Cheng
- Barret Schloerke
- Charlie Gao
- Jeroen Ooms
title: websocket
website: https://rstudio.github.io/websocket/

external:  # updated automatically, do not edit
  description: WebSocket client for R
  first_commit: '2018-02-21T18:29:48+00:00'
  forks: 19
  languages:
  - C++
  last_updated: '2026-03-05T16:12:54.232431+00:00'
  latest_release: '2025-04-10T10:24:20+00:00'
  license: NOASSERTION
  people:
  - Winston Chang
  - Joe Cheng
  - Barret Schloerke
  - Charlie Gao
  - Jeroen Ooms
  readme_image: man/figures/logo.svg
  repo: rstudio/websocket
  stars: 94
  title: websocket
  website: https://rstudio.github.io/websocket/
---

The websocket package is an R WebSocket client library backed by the websocketpp C++ library that handles WebSocket I/O on a separate thread from R. It provides a client for establishing WebSocket connections, sending and receiving messages, and managing connection lifecycle events.

The package uses an event-driven callback system (onOpen, onMessage, onClose, onError) that makes it straightforward to handle asynchronous WebSocket communication in R. It supports both text and binary messages, can be used within Shiny applications, and works with WebSocket servers to implement patterns like proxies for logging or modifying traffic. The threaded I/O design prevents WebSocket operations from blocking R's main execution thread.
