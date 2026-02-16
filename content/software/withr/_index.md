---
description: Methods For Temporarily Modifying Global State
github: r-lib/withr
image: logo.png
languages:
- R
latest_release: '2024-10-28T10:59:02+00:00'
people:
- Lionel Henry
- Hadley Wickham
- Jenny Bryan
- Gábor Csárdi
- Jeroen Janssens
- Davis Vaughan
title: withr
website: http://withr.r-lib.org

external:
  contributors:
  - jimhester
  - lionel-
  - hadley
  - krlmlr
  - jennybc
  - gaborcsardi
  - MichaelChirico
  - ellessenne
  - alexcipro
  - kyleam
  - lauracion
  - MLopez-Ibanez
  - batpigandme
  - malfaro2
  - mpaulacaldas
  - mtmorgan
  - multimeric
  - romainfrancois
  - zkamvar
  - orichters
  - wendtke
  - jonkeane
  - jeroenjanssens
  - javierluraschi
  - czeildi
  - meta00
  - dragosmg
  - dskard
  - DavisVaughan
  - AshesITR
  - angelinepro
  description: Methods For Temporarily Modifying Global State
  first_commit: '2015-04-21T19:18:28+00:00'
  forks: 44
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.804540+00:00'
  latest_release: '2024-10-28T10:59:02+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Hadley Wickham
  - Jenny Bryan
  - Gábor Csárdi
  - Jeroen Janssens
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: r-lib/withr
  stars: 177
  title: withr
  website: http://withr.r-lib.org
---

withr is an essential R package for safely managing side effects by temporarily modifying global state during code execution. It provides a clean, reliable way to run code with altered environmental conditions such as working directories, environment variables, random seeds, graphics parameters, or library paths, and then automatically restore the original state when execution completes. This makes your code more predictable and prevents unintended side effects from leaking into other parts of your program.

The package offers two complementary sets of functions: `with_*()` functions that reset state immediately after code execution, and `local_*()` functions that reset state at the end of their scope. This design is particularly valuable for package developers writing robust tests, data scientists working with sensitive credentials or specific configurations, and anyone who needs to ensure their code doesn't inadvertently alter the global environment. Originally developed as part of the devtools project, withr has matured into a lightweight, standalone tool that has become a foundational dependency in the R ecosystem.