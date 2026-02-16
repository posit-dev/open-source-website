---
description: Finding files in project subdirectories
github: r-lib/rprojroot
languages:
- R
latest_release: '2025-08-26T15:22:36+00:00'
people:
- Jenny Bryan
- Garrick Aden-Buie
title: rprojroot
website: https://rprojroot.r-lib.org/

external:
  contributors:
  - krlmlr
  - aviator-app[bot]
  - github-actions[bot]
  - IndrajeetPatil
  - salim-b
  - BarkleyBG
  - jennybc
  - batpigandme
  - karldw
  - olivroy
  - gadenbuie
  - mitchelloharawild
  - bastistician
  - uribo
  description: Finding files in project subdirectories
  first_commit: '2015-05-19T02:10:40+00:00'
  forks: 23
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.821028+00:00'
  latest_release: '2025-08-26T15:22:36+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Garrick Aden-Buie
  repo: r-lib/rprojroot
  stars: 149
  title: rprojroot
  website: https://rprojroot.r-lib.org/
---

rprojroot is a lightweight R package that solves a common frustration in data science workflows: the brittleness of file paths that break when scripts are run from different locations. By automatically identifying your project's root directory and enabling file access relative to that anchor point, rprojroot eliminates the notorious "working directory insanity" that plagues collaborative projects. The package intelligently locates your project root by searching for markers like DESCRIPTION files in R packages or other customizable criteria, allowing you to reference data files, scripts, and outputs consistently regardless of where your code executes from.

What makes rprojroot particularly valuable for developers and data scientists is its ability to make your code more portable and robust. Instead of relying on fragile absolute paths or assumptions about working directories, you can construct file paths that work seamlessly whether you're running code interactively, from a subdirectory, or within automated pipelines. The package handles both relative and absolute paths gracefully, serving as the foundational infrastructure for higher-level tools like the popular here package while remaining powerful enough to use directly in any R project or package development workflow.
