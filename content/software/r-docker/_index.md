---
description: Docker images for R
github: rstudio/r-docker
languages:
- Dockerfile
title: r-docker
website: https://hub.docker.com/r/rstudio/r-base

external:
  contributors:
  - glin
  - jonyoder
  - jforest
  - jmwoliver
  description: Docker images for R
  first_commit: '2019-02-27T22:14:56+00:00'
  forks: 25
  languages:
  - Dockerfile
  last_updated: '2026-02-13T14:17:04.005193+00:00'
  license: GPL-3.0
  repo: rstudio/r-docker
  stars: 140
  title: r-docker
  website: https://hub.docker.com/r/rstudio/r-base
---

r-docker provides lightweight, production-ready Docker images for R that serve as a minimal foundation for building containerized data science applications. These images support all minor R versions since 4.0 across ten different Linux distributions, including Ubuntu, Debian, Rocky Linux, CentOS, and openSUSE, with compatibility for both x86_64 and arm64 architectures. By maintaining intentionally minimal environments with only essential system libraries, r-docker enables data scientists and developers to create reproducible, consistent R environments across teams while keeping image sizes lean.

What makes r-docker particularly valuable is its comprehensive version coverage and flexible tagging system, allowing you to pin specific R patch versions for maximum reproducibility or track the latest patches within a version line for automatic security updates. The images are designed as foundation layers for custom Docker builds, making them ideal for teams that need to standardize their R infrastructure, deploy applications in cloud environments, or ensure consistent computational environments across development, testing, and production. Whether you're packaging Shiny applications, building data pipelines, or creating custom analytical environments, r-docker provides the minimal, reliable base you need to get started quickly.