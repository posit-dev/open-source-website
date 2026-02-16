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

external:
  contributors:
  - hadley
  - maelle
  - IndrajeetPatil
  - krlmlr
  - dmurdoch
  - DavisVaughan
  - ARawles
  - cderv
  - davidchall
  - mdneuzerling
  - gadenbuie
  - jeroenjanssens
  - strazto
  - salim-b
  - zeehio
  - zkamvar
  description: Syntax Highlighting and Automatic Linking
  first_commit: '2020-05-28T18:00:36+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.322854+00:00'
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

downlit is an essential R package that enhances code documentation by providing sophisticated syntax highlighting and automatic linking capabilities. Designed to work seamlessly with popular R Markdown documentation tools like pkgdown, bookdown, and hugodown, downlit uses R's own parser to provide accurate syntax highlighting while intelligently linking function calls to their documentation. Whether you're working with multi-line code blocks or inline code snippets, downlit automatically recognizes function references, help system calls, vignettes, and package names, transforming them into properly formatted and linked elements.

What makes downlit particularly valuable for developers and data scientists is its smart cross-package linking system. When documenting code that references functions from other packages, downlit automatically discovers their pkgdown sites and creates direct links to the appropriate documentation, falling back to rdrr.io or CRAN when needed. This creates a connected documentation ecosystem where readers can easily navigate from your code examples to the detailed documentation of any function you reference. While primarily designed for integration into documentation generation workflows, downlit's powerful transformation functions help ensure that your R documentation is both visually appealing and functionally rich with helpful references.
