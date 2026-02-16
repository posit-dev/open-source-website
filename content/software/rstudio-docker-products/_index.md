---
description: Docker images for RStudio Professional Products
github: rstudio/rstudio-docker-products
languages:
- Shell
people:
- Neal Richardson
title: rstudio-docker-products
website: https://hub.docker.com/u/rstudio

external:
  contributors:
  - colearendt
  - ianpittwood
  - bschwedler
  - nahara7
  - zachhannum
  - aronatkins
  - skyeturriff
  - edavidaja
  - dbkegley
  - jonyoder
  - tylfin
  - melissa-barca
  - danielfrg
  - cm421
  - jforest
  - glin
  - Lytol
  - bdeitte
  - sagerb
  - dkasabovn
  - blairj09
  - nodivbyzero
  - koverholt
  - nunyunuymi
  - zackverham
  - marcosnav
  - plascaray
  - lucasrod16
  - alessap
  - github-actions[bot]
  - jeffvroom
  - ssinnott
  - GCRev
  - starlightromero
  - samcofer
  - jmwoliver
  - mmarchetti
  - atheriel
  - adamhigerd
  - nihara-thomas
  - dethmasque
  - tdstein
  - zfouts
  - shepherdjerred
  - vivas89
  - christierney
  - mconflitti-pbc
  - CDRayn
  - kfeinauer
  - michaelmayer2
  - scottmmjackson
  - sharon-wang
  - kevinushey
  - kelli-rstudio
  - joshfrench
  - gtritchie
  - costrouc
  - AndrewMcClain
  - jstruzik
  - fh-mthomson
  - nealrichardson
  - timtmok
  - trestletech
  - dotNomad
  - gbrlsnchs
  - karawoo
  - dpastoor
  - alexkgold
  - eduardocfalcao
  - MariaSemple
  - m--
  - msarahan
  - rstub
  - Trevor-Reid
  - AshleyHenry15
  description: Docker images for RStudio Professional Products
  first_commit: '2019-06-06T18:31:12+00:00'
  forks: 58
  languages:
  - Shell
  last_updated: '2026-02-13T14:17:04.195954+00:00'
  license: MIT
  people:
  - Neal Richardson
  repo: rstudio/rstudio-docker-products
  stars: 71
  title: rstudio-docker-products
  website: https://hub.docker.com/u/rstudio
---

RStudio Docker Products provides pre-built, containerized images of RStudio's professional analytics platform, making it easier for teams to deploy and scale their data science infrastructure. The repository includes Docker containers for RStudio Workbench (a collaborative development environment), RStudio Connect (a publishing and sharing platform for analytics), and RStudio Package Manager (a repository management system for R packages). Whether you're setting up a complete analytics stack locally for development or deploying to production, these images provide a flexible foundation that can be customized to meet your organization's specific needs.

Rather than manually installing and configuring each component, teams can use docker-compose to orchestrate a complete RStudio Team deployment with all products working together seamlessly. The images are designed as starting points that organizations can fork and customize with their own security scanning, base OS preferences, and CVE management standards. With configurable dependency versions and validation testing built in, these Docker images reduce operational overhead while giving teams the flexibility to control Python, R, Quarto, and other component versions to match their workflow requirements.
