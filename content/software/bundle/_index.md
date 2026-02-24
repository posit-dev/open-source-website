---
description: Prepare objects for serialization with a consistent interface
github: rstudio/bundle
image: diagram_04.png
languages:
- R
latest_release: '2025-12-10T20:15:43+00:00'
people:
- Simon Couch
- Julia Silge
- Emil Hvitfeldt
- Daniel Falbel
title: bundle
website: https://rstudio.github.io/bundle/

external:  # updated automatically, do not edit
  description: Prepare objects for serialization with a consistent interface
  first_commit: '2022-06-23T19:15:20+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-02-24T09:26:20.065909+00:00'
  latest_release: '2025-12-10T20:15:43+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Julia Silge
  - Emil Hvitfeldt
  - Daniel Falbel
  readme_image: man/figures/diagram_04.png
  repo: rstudio/bundle
  stars: 31
  title: bundle
  website: https://rstudio.github.io/bundle/
---

The bundle package provides a common interface for saving and reloading R model objects that rely on external references, such as pointers or server connections, which aren't preserved by standard `save()` or `saveRDS()` functions. It allows you to bundle these models with their references so they can be safely transferred between R sessions and deployed in production environments.

The package solves the problem of model objects that break when saved and reloaded because they depend on information outside the object itself. Bundle works with various model types, including XGBoost, that store pointers or other external references that get disrupted during serialization. The workflow is straightforward: call `bundle()` before saving your model and `unbundle()` after loading it in a new session to restore full functionality.
