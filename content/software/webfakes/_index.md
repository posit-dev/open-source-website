---
description: Fake web apps for HTTP testing R packages
github: r-lib/webfakes
languages:
- C
latest_release: '2025-06-24T17:53:05+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: webfakes
website: https://webfakes.r-lib.org

external:
  contributors:
  - gaborcsardi
  - maelle
  - gergness
  - jeroenjanssens
  - Zopolis4
  description: Fake web apps for HTTP testing R packages
  first_commit: '2020-03-30T15:34:05+00:00'
  forks: 6
  languages:
  - C
  last_updated: '2026-02-13T14:17:20.241737+00:00'
  latest_release: '2025-06-24T17:53:05+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/webfakes
  stars: 63
  title: webfakes
  website: https://webfakes.r-lib.org
---

webfakes is a lightweight R package that lets you create fake web servers for testing HTTP clients and API interactions. Built on the embedded civetweb server, it provides a complete web application framework that runs directly in your R process, eliminating issues with local firewalls and external dependencies. You can define custom HTTP handlers in R, use flexible path matching with parameters and regular expressions, and leverage built-in middleware for parsing JSON, multipart, and URL-encoded request bodies.

Whether you're testing an HTTP client package or need to simulate specific API behavior, webfakes makes it easy to spin up realistic web services for your test suites. The package includes a ready-to-use httpbin-style app for common testing scenarios, supports concurrent requests through its multi-threaded server, and even allows you to simulate low bandwidth conditions. Since web apps are just R objects, you can save them to disk, copy them between processes, extend them with new routes and middleware, and interact with them from your browser or command line for easy debugging.
