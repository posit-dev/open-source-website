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

external:  # updated automatically, do not edit
  description: Easy and Powerful Webservers in R
  first_commit: '2025-02-27T14:17:04+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-24T09:25:58.020845+00:00'
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

plumber2 is a complete rewrite of the plumber package for creating HTTP APIs in R. It maintains similar functionality to the original but makes breaking changes to improve the API design based on lessons learned from the original package's development.

The package separates path parameters from query and body parameters for clearer request handling, adds extensive type checking and validation for inputs and outputs (including nested objects, enums, and default values), supports content negotiation with multiple serializers per endpoint, and provides simplified async handler creation. The documentation system is rebuilt on roxygen2 for better parsing and follows modern API documentation conventions.
