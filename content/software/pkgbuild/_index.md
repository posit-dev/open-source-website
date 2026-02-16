---
description: Find tools needed to build R packages
github: r-lib/pkgbuild
languages:
- R
latest_release: '2025-05-26T10:36:19+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jeroen Ooms
- Lionel Henry
- Jeroen Janssens
- Christophe Dervieux
title: pkgbuild
website: https://pkgbuild.r-lib.org

external:
  contributors:
  - gaborcsardi
  - jimhester
  - hadley
  - krlmlr
  - ateucher
  - dgkf
  - jeroen
  - remlapmot
  - richierocks
  - MichaelChirico
  - batpigandme
  - paleolimbot
  - dpastoor
  - theGreatWhiteShark
  - musvaage
  - const-ae
  - sangeetabhatia03
  - richfitz
  - njtierney
  - m-muecke
  - mcol
  - lorenzwalthert
  - lionel-
  - jeroenjanssens
  - burgerga
  - dpprdan
  - cderv
  description: Find tools needed to build R packages
  first_commit: '2016-11-10T14:16:37+00:00'
  forks: 38
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.204782+00:00'
  latest_release: '2025-05-26T10:36:19+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jeroen Ooms
  - Lionel Henry
  - Jeroen Janssens
  - Christophe Dervieux
  repo: r-lib/pkgbuild
  stars: 77
  title: pkgbuild
  website: https://pkgbuild.r-lib.org
---

pkgbuild streamlines the development of R packages that include compiled code by automatically handling the complexity of build tool configuration and verification. For R package developers working with C, C++, or Fortran code, pkgbuild eliminates the friction of ensuring that compilation tools are properly installed and configured. The package provides simple functions to check build prerequisites, compile packages from source, and execute code in environments where build tools are available, making it an essential utility for anyone developing packages with performance-critical compiled components.

Beyond basic compilation support, pkgbuild offers extensive customization options through DESCRIPTION entries, R options, and environment variables. Developers can fine-tune build behavior including documentation handling, file copying strategies for large directories, compiler flags, and recompilation detection. By automating these often-tedious setup tasks, pkgbuild allows package developers to focus on writing code rather than troubleshooting compilation environments, whether they're building locally or setting up continuous integration pipelines.
