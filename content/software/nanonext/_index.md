---
description: R binding for NNG (Nanomsg Next Gen)
github: r-lib/nanonext
image: logo.png
languages:
- C
latest_release: '2026-02-09T19:24:09+00:00'
people:
- Charlie Gao
- Joe Cheng
- Jeroen Janssens
title: nanonext
website: https://nanonext.r-lib.org/

external:
  contributors:
  - shikokuchuo
  - jcheng5
  - jeroenjanssens
  description: R binding for NNG (Nanomsg Next Gen)
  first_commit: '2022-01-23T12:59:16+00:00'
  forks: 11
  languages:
  - C
  last_updated: '2026-02-13T14:17:20.603465+00:00'
  latest_release: '2026-02-09T19:24:09+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  - Joe Cheng
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/nanonext
  stars: 76
  title: nanonext
  website: https://nanonext.r-lib.org/
---

nanonext is a fast, lightweight toolkit for messaging, concurrency, and web services in R, built on NNG (Nanomsg Next Gen) and implemented almost entirely in C for exceptional performance. It provides robust inter-process and network communication capabilities through multiple messaging patterns including publish/subscribe, request/reply, and push/pull, while supporting diverse transport options like TCP, WebSocket, and TLS. With non-blocking asynchronous operations, nanonext enables developers to build scalable, concurrent applications that handle I/O efficiently without blocking execution.

What makes nanonext particularly valuable for data scientists and developers is its unified web toolkit that can serve HTTP endpoints, WebSocket connections, and data streaming on a single port with built-in HTTPS/WSS encryption. Beyond its web capabilities, nanonext facilitates seamless cross-language interoperability, enabling R applications to exchange data with Python, C++, Go, and Rust. Whether you're building microservices, real-time data pipelines, or distributed computing systems, nanonext provides the essential infrastructure for reliable, high-performance communication without the complexity of managing multiple servers or protocols.
