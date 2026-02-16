---
description: HTML 5 Websockets implementation for R
github: rstudio/R-Websockets
languages:
- R
people:
- Joe Cheng
title: R-Websockets
website: http://illposed.net/websockets.html

external:
  contributors:
  - bwlewis
  - jcheng5
  - jeffreyhorner
  - jaryan
  description: HTML 5 Websockets implementation for R
  first_commit: '2011-04-17T20:01:50+00:00'
  forks: 36
  languages:
  - R
  last_updated: '2026-02-13T14:17:00.979791+00:00'
  people:
  - Joe Cheng
  repo: rstudio/R-Websockets
  stars: 73
  title: R-Websockets
  website: http://illposed.net/websockets.html
---

R-Websockets provides native HTML5 WebSocket functionality for R, enabling real-time, bidirectional communication between R and web clients. This portable implementation supports both WebSocket client and server capabilities, allowing you to build interactive web applications with R backends that communicate efficiently with JavaScript and other web technologies. By replacing traditional Ajax-based HTTP request-response patterns with persistent WebSocket connections, R-Websockets delivers more efficient network utilization and lower latency for data-intensive applications.

The package handles multiple simultaneous WebSocket connections and supports the draft IETF protocols used by modern web browsers. Written mostly in R with minimal external dependencies, R-Websockets is easily portable across platforms and ideal for developers building real-time data visualizations, collaborative analytical tools, or interactive dashboards. Whether you're streaming live data updates to a web interface or enabling multiple users to share an R session, R-Websockets provides the infrastructure for modern, responsive web applications powered by R. Note that for new projects, you may also want to explore the httpuv package, which offers an alternative approach to WebSocket server implementation.
