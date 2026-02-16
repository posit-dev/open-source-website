---
description: WebSocket client for R
github: rstudio/websocket
image: logo.svg
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

external:
  contributors:
  - wch
  - alandipert
  - jcheng5
  - schloerke
  - bborgesr
  - trestletech
  - shikokuchuo
  - jeroen
  - kalibera
  description: WebSocket client for R
  first_commit: '2018-02-21T18:29:48+00:00'
  forks: 19
  languages:
  - C++
  last_updated: '2026-02-13T14:17:03.240972+00:00'
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

The websocket package brings real-time, bidirectional communication to R through a robust WebSocket client implementation. Built on the battle-tested websocketpp C++ library, it enables R users to connect to WebSocket servers for live data streams, interactive applications, and event-driven workflows. Whether you're building responsive Shiny dashboards that update in real-time, consuming streaming data from APIs, or creating middleware that processes message traffic on the fly, websocket provides the foundation for modern, connected R applications.

With its event-driven architecture and asynchronous I/O running on a separate thread, websocket keeps your R session responsive while handling network communication in the background. The package supports both text and binary messages, custom headers for authentication, and a straightforward callback-based API for handling connection events, incoming messages, and errors. This makes it particularly valuable for data scientists who need to integrate live data sources into their analytical workflows and developers building real-time features into R-based applications.
