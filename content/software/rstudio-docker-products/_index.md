---
description: Docker images for RStudio Professional Products
github: rstudio/rstudio-docker-products
languages:
- Shell
people:
- Neal Richardson
title: rstudio-docker-products
website: https://hub.docker.com/u/rstudio

external:
  description: Docker images for RStudio Professional Products
  first_commit: '2019-06-06T18:31:12+00:00'
  forks: 58
  languages:
  - Shell
  last_updated: '2026-02-17T11:22:23.731964+00:00'
  license: MIT
  people:
  - Neal Richardson
  repo: rstudio/rstudio-docker-products
  stars: 71
  title: rstudio-docker-products
  website: https://hub.docker.com/u/rstudio
---

This repository provides Docker images for RStudio's professional products: Workbench, Connect, and Package Manager. It includes both the main product images and supporting session images for running R content.

The images are designed as starting points that organizations should customize and rebuild to meet their security requirements. Key features include a hierarchical image structure with base images and product-specific layers, orchestrated builds using docker buildx bake, and validation testing with Goss. The repository uses a Justfile-based build system that allows building individual images or groups, with all dependency versions centrally defined in docker-bake.hcl for easy customization.
