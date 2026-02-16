---
description: Minimalistic GitHub API client in R
github: r-lib/gh
languages:
- R
latest_release: '2025-05-26T09:31:40+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
- Hadley Wickham
- Garrick Aden-Buie
- Christophe Dervieux
- Jeroen Janssens
- Jeroen Ooms
- Lionel Henry
title: gh
website: https://gh.r-lib.org

external:
  contributors:
  - gaborcsardi
  - jennybc
  - hadley
  - rundel
  - gadenbuie
  - maelle
  - krlmlr
  - noamross
  - cderv
  - gdequeiroz
  - jimhester
  - batpigandme
  - statnmap
  - tanho63
  - atheriel
  - fmichonneau
  - coatless
  - jvstein
  - jeroenjanssens
  - jeroen
  - jsta
  - lionel-
  - RodDalBen
  - realAkhmed
  - FMKerckhof
  description: Minimalistic GitHub API client in R
  first_commit: '2015-06-08T03:00:11+00:00'
  forks: 56
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.870914+00:00'
  latest_release: '2025-05-26T09:31:40+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jenny Bryan
  - Hadley Wickham
  - Garrick Aden-Buie
  - Christophe Dervieux
  - Jeroen Janssens
  - Jeroen Ooms
  - Lionel Henry
  repo: r-lib/gh
  stars: 231
  title: gh
  website: https://gh.r-lib.org
---

gh is a minimalistic R package that provides seamless access to GitHub's REST and GraphQL APIs directly from your R environment. It enables data scientists and developers to programmatically interact with GitHub repositories, issues, pull requests, and other resources without needing deep knowledge of API mechanics. The package handles all the complexity of authentication, request formatting, and JSON parsing, allowing you to copy endpoint paths straight from GitHub's documentation and use them in your R code with minimal adaptation.

What makes gh particularly valuable for data-driven workflows is its intelligent handling of authentication through multiple methods including git credential stores and environment variables, automatic pagination for retrieving large datasets, and support for all standard HTTP methods. Whether you're analyzing repository metrics, automating issue management, querying collaborative coding patterns, or building data pipelines that depend on GitHub data, gh provides a low-friction interface that integrates naturally with the R ecosystem while keeping your credentials secure and your code clean.
