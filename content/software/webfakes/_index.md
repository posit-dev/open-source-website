---
image: logo.svg
color: "#404041"
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

external:  # updated automatically, do not edit
  description: Fake web apps for HTTP testing R packages
  first_commit: '2020-03-30T15:34:05+00:00'
  forks: 6
  languages:
  - C
  last_updated: '2026-03-05T16:29:13.247324+00:00'
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

webfakes is an R package that provides a lightweight framework for creating fake web servers to test HTTP-related code. It uses the embedded civetweb server to run web apps directly in your R process.

The package solves the problem of testing HTTP clients and APIs without relying on external services. It includes a complete web framework for defining custom handlers in R, comes with a built-in httpbin-like app for common testing scenarios, and supports concurrent requests through multi-threading. Since the server runs in-process, it avoids firewall issues and allows you to test network code reliably and quickly.
