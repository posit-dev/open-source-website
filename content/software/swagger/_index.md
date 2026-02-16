---
description: Swagger is a collection of HTML, Javascript, and CSS assets that dynamically
  generate beautiful documentation from a Swagger-compliant API.
github: rstudio/swagger
image: browse_swagger.png
languages:
- HTML
latest_release: '2024-06-29T17:13:31+00:00'
people:
- Barret Schloerke
title: swagger
website: https://swagger.io/swagger-ui/

external:
  contributors:
  - schloerke
  - javierluraschi
  - meztez
  - dselivanov
  description: Swagger is a collection of HTML, Javascript, and CSS assets that dynamically
    generate beautiful documentation from a Swagger-compliant API.
  first_commit: '2017-10-25T21:02:12+00:00'
  forks: 10
  languages:
  - HTML
  last_updated: '2026-02-13T14:17:03.129792+00:00'
  latest_release: '2024-06-29T17:13:31+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  readme_image: man/figures/browse_swagger.png
  repo: rstudio/swagger
  stars: 54
  title: swagger
  website: https://swagger.io/swagger-ui/
---

Swagger is an R package that bundles a collection of HTML, JavaScript, and CSS assets to dynamically generate beautiful, interactive documentation from Swagger-compliant APIs. By providing a standardized way to describe RESTful APIs, Swagger makes it easy for developers and data scientists to understand and interact with API endpoints without diving into source code. The package automatically creates visual documentation that displays available routes, parameters, request/response formats, and even includes an interactive interface for testing API calls directly from the browser.

The primary purpose of this package is to enable R package authors to create APIs that are fully compatible with the Swagger and OpenAPI ecosystems. Whether you're building data science APIs with plumber, creating web services for analytical workflows, or developing tools that need to expose programmatic interfaces, the swagger package provides the static assets you need to serve professional-grade API documentation. Package authors can easily integrate these assets into their web applications using httpuv or fiery, giving users immediate access to comprehensive, interactive documentation that improves API discoverability and reduces integration time.
