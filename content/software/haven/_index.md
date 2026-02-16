---
description: Read SPSS, Stata and SAS files from R
github: tidyverse/haven
image: logo.png
languages:
- C
latest_release: '2025-05-30T13:08:26+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Jeroen Ooms
- Jeroen Janssens
- JJ Allaire
title: haven
website: https://haven.tidyverse.org

external:
  contributors:
  - hadley
  - gorcha
  - jimhester
  - evanmiller
  - batpigandme
  - lionel-
  - jeroen
  - markriseley
  - mikmart
  - larmarange
  - edwindj
  - gergness
  - krlmlr
  - aghaynes
  - jmobrien
  - bquast
  - urswilke
  - rkb965
  - oscardssmith
  - oliverbock
  - dsteuer
  - zkamvar
  - thays42
  - tklebel
  - sbae
  - szimmer
  - rubenarslan
  - pkq
  - maxheld83
  - BioStatMatt
  - lwjohnst86
  - lorenzwalthert
  - kwenzig
  - huftis
  - jmbarbone
  - ehrlinger
  - jeroenjanssens
  - jjallaire
  - HughParsonage
  - ecortens
  - diogocp
  - ajdamico
  description: Read SPSS, Stata and SAS files from R
  first_commit: '2015-02-04T16:28:17+00:00'
  forks: 116
  languages:
  - C
  last_updated: '2026-02-13T14:17:08.559571+00:00'
  latest_release: '2025-05-30T13:08:26+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Jeroen Ooms
  - Jeroen Janssens
  - JJ Allaire
  readme_image: man/figures/logo.png
  repo: tidyverse/haven
  stars: 446
  title: haven
  website: https://haven.tidyverse.org
---

haven is an essential R package that bridges the gap between statistical software ecosystems by enabling seamless data interchange with SAS, SPSS, and Stata. It provides a unified interface for reading and writing multiple proprietary formats, eliminating the friction that typically arises when collaborating across research teams using different statistical tools. Built on the robust ReadStat C library, haven handles the technical complexity of format specifications behind the scenes, allowing you to focus on your analysis rather than data conversion logistics.

What makes haven particularly valuable for data scientists is its intelligent handling of data semantics through a specialized labelled() class that preserves value labels and special missing values from the original files. Unlike other tools that force automatic factor conversion or lose important metadata, haven maintains the rich context encoded in your data while converting date/time values to native R classes and keeping character vectors intact. This semantic preservation is crucial for interdisciplinary projects where maintaining the original meaning of coded variables can make the difference between accurate analysis and costly misinterpretation.
