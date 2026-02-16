---
description: Install R packages from GitHub, GitLab, Bitbucket, git, svn repositories,
  URLs
github: r-lib/remotes
languages:
- R
latest_release: '2024-03-17T12:41:28+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
- Christophe Dervieux
- Hannah Frick
- Lionel Henry
- Hadley Wickham
- Jeroen Janssens
- Jeroen Ooms
title: remotes
website: https://remotes.r-lib.org/

external:
  contributors:
  - gaborcsardi
  - jimhester
  - krlmlr
  - maksymiuks
  - overmar
  - tylermorganwall
  - muschellij2
  - jennybc
  - Bisaloo
  - heavywatal
  - riccardoporreca
  - kevinushey
  - niheaven
  - dpprdan
  - cderv
  - antoine-sachet
  - eeholmes
  - bbimber
  - stufield
  - maelle
  - batpigandme
  - HenrikBengtsson
  - hfrick
  - ateucher
  - aornugent
  - ankane
  - Neil-Schneider
  - pommedeterresautee
  - mkearney
  - siyangli32
  - MichaelChirico
  - MyKo101
  - MatthieuStigler
  - ms609
  - LiNk-NY
  - malcolmbarrett
  - lionel-
  - kirillseva
  - achimgaedke
  - flying-sheep
  - rnorberg
  - robertdj
  - rcannood
  - salim-b
  - timtrice
  - ttriche
  - tmelliott
  - wibeasley
  - hadley
  - jjchern
  - musvaage
  - infotroph
  - dagola
  - danhalligan
  - djnavarro
  - Dasonk
  - davidchall
  - mdneuzerling
  - DivadNojnarg
  - dgkf
  - dmurdoch
  - QuLogic
  - jefferis
  - yutannihilation
  - jakubkovac
  - JamesCuster
  - coatless
  - jan-glx
  - jeroenjanssens
  - jeroen
  - jesse-ross
  - jgabry
  - joshuaulrich
  - jsilve24
  - kenahoo
  description: Install R packages from GitHub, GitLab, Bitbucket, git, svn repositories,
    URLs
  first_commit: '2016-01-02T10:24:31+00:00'
  forks: 155
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.953673+00:00'
  latest_release: '2024-03-17T12:41:28+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jenny Bryan
  - Christophe Dervieux
  - Hannah Frick
  - Lionel Henry
  - Hadley Wickham
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/remotes
  stars: 356
  title: remotes
  website: https://remotes.r-lib.org/
---

The remotes package provides a lightweight, flexible solution for installing R packages from diverse repositories beyond CRAN. Whether you need to install development versions from GitHub, access packages from GitLab or Bitbucket, or pull code from git and subversion repositories, remotes makes it straightforward. As a standalone replacement for the install_* functions in devtools, it requires no compiler or external dependencies for most use cases, making it faster to install and easier to use in any environment.

With remotes, you can install packages from specific versions, branches, commits, tags, or even pull requests, giving you precise control over your dependencies. The package automatically handles dependency resolution and supports the Remotes field in package descriptions, allowing package authors to specify non-standard dependencies that point directly to development repositories. This flexibility is invaluable for data scientists and developers who need to work with cutting-edge features, collaborate on pre-release code, or maintain reproducible environments with exact package versions.
