---
description: Syntax Highlighting and Automatic Linking
github: r-lib/downlit
languages:
- R
latest_release: '2025-11-13T22:37:02+00:00'
people:
- Hadley Wickham
- Davis Vaughan
- Christophe Dervieux
- Garrick Aden-Buie
- Jeroen Janssens
title: downlit
website: https://downlit.r-lib.org

external:  # updated automatically, do not edit
  description: Syntax Highlighting and Automatic Linking
  first_commit: '2020-05-28T18:00:36+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-02-24T09:26:36.293738+00:00'
  latest_release: '2025-11-13T22:37:02+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Davis Vaughan
  - Christophe Dervieux
  - Garrick Aden-Buie
  - Jeroen Janssens
  repo: r-lib/downlit
  stars: 90
  title: downlit
  website: https://downlit.r-lib.org
---

downlit provides syntax highlighting and automatic linking for R code in documentation. It's designed to work with RMarkdown packages like pkgdown, bookdown, and hugodown to turn code references into clickable links to documentation.

The package automatically links function calls, help topics, vignettes, and package names to their documentation, either on pkgdown sites or fallback sources like rdrr.io. It handles both multiline code blocks (with syntax highlighting and comment styling) and inline code references. Cross-package linking works by discovering pkgdown metadata, making it easy to create interconnected documentation across R packages.
