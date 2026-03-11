---
description: R binding for NNG (Nanomsg Next Gen)
github: r-lib/nanonext
image: logo.png
color: "#4AA1BF"
languages:
- C
latest_release: '2026-02-09T19:24:09+00:00'
people:
- Charlie Gao
- Joe Cheng
- Jeroen Janssens
title: nanonext
website: https://nanonext.r-lib.org/

external:  # updated automatically, do not edit
  description: R binding for NNG (Nanomsg Next Gen)
  first_commit: '2022-01-23T12:59:16+00:00'
  forks: 11
  languages:
  - C
  last_updated: '2026-03-05T16:30:04.638668+00:00'
  latest_release: '2026-02-09T19:24:09+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  - Joe Cheng
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/nanonext
  stars: 79
  title: nanonext
  website: https://nanonext.r-lib.org/
---

nanonext is a fast, lightweight R package for messaging, concurrency, and web communications built on NNG (Nanomsg Next Gen) with a C implementation. It provides scalable networking protocols like pub/sub, request/reply, and push/pull patterns with support for multiple transports including TCP, IPC, WebSocket, and TLS.

The package enables non-blocking async I/O operations that resolve automatically, making it suitable for concurrent programming in R. It includes a unified web toolkit that handles HTTP, WebSocket, and streaming protocols on a single port with built-in TLS support. The cross-language compatibility allows R to exchange data with Python, C++, Go, and Rust applications using standard messaging protocols.
