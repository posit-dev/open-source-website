---
description: Manipulate DESCRIPTION files
github: r-lib/desc
languages:
- R
latest_release: '2023-12-10T11:07:16+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
- Hadley Wickham
- Jeroen Janssens
- Jeroen Ooms
title: desc
website: https://desc.r-lib.org/

external:
  contributors:
  - gaborcsardi
  - ateucher
  - maelle
  - dpprdan
  - malcolmbarrett
  - jennybc
  - jimhester
  - salim-b
  - niceume
  - kevinushey
  - krlmlr
  - massarin
  - dpastoor
  - hadley
  - jeroenjanssens
  - jeroen
  - muschellij2
  - llrs
  - lorenzwalthert
  - lwjohnst86
  - mvkorpel
  - richfitz
  - seankross
  description: Manipulate DESCRIPTION files
  first_commit: '2015-09-07T22:01:43+00:00'
  forks: 35
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.887814+00:00'
  latest_release: '2023-12-10T11:07:16+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jenny Bryan
  - Hadley Wickham
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/desc
  stars: 124
  title: desc
  website: https://desc.r-lib.org/
---

desc is an essential R package for developers who work with R packages, providing comprehensive tools to programmatically read, manipulate, and reformat DESCRIPTION files. Every R package relies on a DESCRIPTION file to specify metadata, dependencies, authors, and licensing information. Rather than manually editing these files or using fragile text processing approaches, desc offers a robust API that understands the structure and conventions of DESCRIPTION files, making it easy to query fields, update package dependencies, manage author information, and ensure proper formatting.

The package offers both object-oriented and procedural interfaces to accommodate different workflow preferences. The R6-based API is perfect for complex operations requiring multiple modifications, while the procedural functions allow quick, one-off changes directly to files on disk. Whether you're building tools that generate or modify R packages, automating package maintenance tasks, or developing infrastructure for package development workflows, desc provides the reliable foundation you need to work confidently with DESCRIPTION files without worrying about parsing edge cases or maintaining proper formatting conventions.
