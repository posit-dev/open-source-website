---
color: '#EE6331'
description: A simpler way to find your files
github: r-lib/here
image: logo.svg
languages:
- R
latest_release: '2025-09-14T18:48:48+00:00'
people:
- Jenny Bryan
title: here
website: https://here.r-lib.org/

external:  # updated automatically, do not edit
  description: A simpler way to find your files
  first_commit: '2016-07-19T14:47:19+00:00'
  forks: 46
  languages:
  - R
  last_updated: '2026-03-20T10:27:52.704150+00:00'
  latest_release: '2025-09-14T18:48:48+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  repo: r-lib/here
  stars: 430
  title: here
  website: https://here.r-lib.org/
---

The `here` package enables easy file referencing in project-oriented R workflows by building paths relative to the project's top-level directory. Instead of using `setwd()`, which breaks when files are reorganized or shared across different systems, `here` automatically finds the project root and constructs file paths from there.

This approach solves the problem of fragile, hard-coded file paths that fail when code is moved or run on different machines. Paths built with `here()` work regardless of where your script lives within the project directory structure, making it particularly useful for projects with data, scripts, and reports in different subdirectories. The package eliminates path-related errors when collaborating or running code from different locations within a project.
