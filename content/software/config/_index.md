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

external:
  contributors:
  - andrie
  - jjallaire
  - dermcnor
  - kevinykuo
  - jimhester
  - wibeasley
  - edavidaja
  - shrektan
  description: config package for R
  first_commit: '2016-05-29T01:48:59+00:00'
  forks: 31
  languages:
  - R
  last_updated: '2026-02-13T14:17:02.357272+00:00'
  people:
  - JJ Allaire
  readme_image: man/figures/logo.svg
  repo: rstudio/config
  stars: 261
  title: config
  website: https://rstudio.github.io/config/
---

config is a lightweight R package that simplifies managing environment-specific configuration values across development, testing, and production environments. By centralizing all your settings in a single config.yml file, it eliminates the need to hardcode environment-specific values like database credentials, API endpoints, or file paths throughout your codebase. You can define configurations for different deployment stages and retrieve them programmatically using the simple config::get() function, making your R projects more maintainable and deployment-ready.

The package is particularly valuable for data scientists and developers working with complex workflows that span multiple environments. Whether you're managing different dataset paths for local development versus production, handling varied database connections across testing and deployment stages, or deploying applications on platforms like Posit Connect that require flexible configuration, config provides an elegant solution. It supports advanced features like inheritance patterns and R expressions within configuration files, giving you the flexibility to build sophisticated configuration hierarchies while keeping your code clean and environment-agnostic.
