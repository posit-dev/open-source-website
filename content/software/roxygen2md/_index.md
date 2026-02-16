---
description: Convert elements of roxygen documentation to markdown
github: r-lib/roxygen2md
languages:
- R
latest_release: '2024-02-18T17:50:05+00:00'
title: roxygen2md
website: https://roxygen2md.r-lib.org/

external:
  contributors:
  - krlmlr
  - IndrajeetPatil
  - alexpghayes
  - batpigandme
  - aviator-app[bot]
  description: Convert elements of roxygen documentation to markdown
  first_commit: '2016-11-24T14:25:44+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.237672+00:00'
  latest_release: '2024-02-18T17:50:05+00:00'
  repo: r-lib/roxygen2md
  stars: 68
  title: roxygen2md
  website: https://roxygen2md.r-lib.org/
---

roxygen2md is an R package that modernizes documentation in roxygen2-based projects by automatically converting legacy Rd (R documentation) markup syntax into clean, readable Markdown format. If you maintain R packages, you know that older documentation often contains verbose Rd markup like `\emph{}`, `\code{}`, `\href{}`, and `\url{}` that can make your roxygen2 comments harder to read and maintain. roxygen2md streamlines this by automating the conversion to Markdown equivalents, updating your `DESCRIPTION` file to enable Markdown support, and providing diagnostic tools to identify any remaining unconverted elements.

What makes roxygen2md particularly valuable for package developers is its staged workflow approach. Rather than attempting to convert everything at once, the package offers "none," "simple," "full," and "unlink" scopes that let you tackle the modernization incrementally. This methodical approach isolates automated changes from those requiring careful human review, reducing risk in large legacy codebases. Whether you're maintaining a mature package with years of accumulated documentation or starting fresh with modern standards, roxygen2md helps ensure your documentation is consistent, readable, and ready for enhanced rendering with tools like pkgdown.