---
color: '#72994E'
description: Docker images for R
github: rstudio/r-docker
image: logo.svg
languages:
- Dockerfile
title: r-docker
website: https://hub.docker.com/r/rstudio/r-base

external:  # updated automatically, do not edit
  description: Docker images for R
  first_commit: '2019-02-27T22:14:56+00:00'
  forks: 25
  languages:
  - Dockerfile
  last_updated: '2026-03-20T10:27:35.283300+00:00'
  license: GPL-3.0
  repo: rstudio/r-docker
  stars: 140
  title: r-docker
  website: https://hub.docker.com/r/rstudio/r-base
---

Posit provides Docker images built on their opinionated R binary distributions for various Linux platforms. These images are intentionally minimal and designed to serve as base images for building custom Docker containers that require R.

The images support multiple Linux distributions (Ubuntu, Debian, Rocky Linux, openSUSE) on both x86_64 and arm64 architectures, with all R minor versions since 4.0. They offer flexible tagging patterns that let you pin to specific R patch versions or float to the latest patch within a minor version, making it easier to build reproducible environments or stay current with R updates. The images only include R and its system dependencies, leaving you to add packages and tools as needed for your specific use case.
