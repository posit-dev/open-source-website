---
description: Easy and Powerful Webservers in R
github: posit-dev/plumber2
image: logo.png
languages:
- R
latest_release: '2026-01-20T09:21:21+00:00'
people:
- Thomas Lin Pedersen
- Barret Schloerke
title: plumber2
website: http://plumber2.posit.co/

external:
  contributors:
  - thomasp85
  - schloerke
  - andreranza
  - LiNk-NY
  - yutannihilation
  - JosephBARBIERDARNAL
  - maelle
  - hrbrmstr
  - bowerth
  description: Easy and Powerful Webservers in R
  first_commit: '2025-02-27T14:17:04+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:16:46.435620+00:00'
  latest_release: '2026-01-20T09:21:21+00:00'
  license: NOASSERTION
  people:
  - Thomas Lin Pedersen
  - Barret Schloerke
  readme_image: man/figures/logo.png
  repo: posit-dev/plumber2
  stars: 110
  title: plumber2
  website: http://plumber2.posit.co/
---

plumber2 is a modern R package that makes it easy to transform your R code into production-ready RESTful APIs. Built as a complete rewrite of the original plumber package, it enables data scientists and developers to expose R functions as web endpoints without requiring deep web development expertise. With plumber2, you can share your analytical models, data processing pipelines, and statistical computations as HTTP services that integrate seamlessly with web applications, dashboards, and other systems.

What distinguishes plumber2 is its refined approach to API development, incorporating lessons learned from years of real-world use. The package features improved parameter handling with clear separation of path, query, and body parameters, reducing common sources of confusion and errors. Enhanced documentation built on roxygen2 conventions provides automatic type checking for inputs and outputs, while advanced content negotiation allows clients to request their preferred response formats. For performance-critical applications, built-in async support simplifies the creation of non-blocking handlers that can efficiently manage longer-running requests, making plumber2 an excellent choice for deploying R-based services at scale.
