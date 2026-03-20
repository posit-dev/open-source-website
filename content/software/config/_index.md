---
description: config package for R
github: rstudio/config
image: logo.svg
languages:
- R
people:
- JJ Allaire
title: config
website: https://rstudio.github.io/config/

external:  # updated automatically, do not edit
  description: config package for R
  first_commit: '2016-05-29T01:48:59+00:00'
  forks: 31
  languages:
  - R
  last_updated: '2026-03-20T10:27:33.086412+00:00'
  people:
  - JJ Allaire
  readme_image: man/figures/logo.svg
  repo: rstudio/config
  stars: 261
  title: config
  website: https://rstudio.github.io/config/
---

The `config` package manages environment-specific configuration values in R using YAML files. It allows you to define different settings for development, testing, and production environments and switch between them programmatically.

The package uses a simple YAML file structure with named configurations like "default" and "production" that contain key-value pairs. You access configuration values by calling `config::get()` to retrieve either the entire configuration list or specific values. The package supports inheritance between configurations and R expressions in config files, making it practical for deploying code across different environments without hardcoding values.
