---
description: Generate R package documentation from inline R comments
github: r-lib/roxygen2
image: logo.png
languages:
- R
latest_release: '2025-09-03T20:12:14+00:00'
people:
- Hadley Wickham
- Gábor Csárdi
- Lionel Henry
- Jenny Bryan
- Thomas Lin Pedersen
- Davis Vaughan
- Christophe Dervieux
- Neal Richardson
- Jeroen Ooms
- Simon Couch
title: roxygen2
website: https://roxygen2.r-lib.org

external:
  contributors:
  - hadley
  - klutometis
  - gaborcsardi
  - yihui
  - jimhester
  - krlmlr
  - briandk
  - MichaelChirico
  - Geoff99
  - kevinushey
  - dougmitarotonda
  - ateucher
  - jranke
  - lionel-
  - maelle
  - wibeasley
  - jennybc
  - maxheld83
  - salim-b
  - olivroy
  - jdmanton
  - egnha
  - batpigandme
  - thomasp85
  - DavisVaughan
  - HenrikBengtsson
  - gustavdelius
  - fmichonneau
  - brodieG
  - billdenney
  - msberends
  - tobiaskley
  - mikefc
  - lindbrook
  - bastistician
  - cderv
  - nealrichardson
  - mikldk
  - eibanez
  - mikemc
  - jeroen
  - yutannihilation
  - romainfrancois
  - flying-sheep
  - PeteHaitch
  - peterdesmet
  - pat-s
  - pkq
  - Ironholds
  - mikmart
  - michaelquinn32
  - mccarthy-m-g
  - mikemahoney218
  - mnazarov
  - maurolepore
  - mjskay
  - mcol
  - ximeg
  - musvaage
  - martin-mfg
  - mpadge
  - lorenzwalthert
  - monkeywithacupcake
  - d-sci
  - bahadzie
  - shrektan
  - tpbilton
  - tbates
  - takluyver
  - ThierryO
  - simonpcouch
  - sgibb
  - russHyde
  - samuel-rosa
  - akersting
  - arilamstein
  - AugustT
  - bwiernik
  - BarkleyBG
  - DanChaltiel
  - halldc
  - hughjonesd
  - dlebauer
  - dieghernan
  - eddelbuettel
  - QuLogic
  - crsh
  - jefferis
  - HenningLorenzen-ext-bayer
  - Bisaloo
  - ijlyttle
  - IndrajeetPatil
  - jakob-r
  - jameslamb
  - johnbaums
  - jeis2497052
  - jonthegeek
  - jmbarbone
  - jhchou
  - JoshOBrien
  - kellijohnson-NOAA
  - klmr
  - Lucaweihs
  - mjaeugster
  - LiNk-NY
  description: Generate R package documentation from inline R comments
  first_commit: '2011-05-18T08:23:27+00:00'
  forks: 238
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.489638+00:00'
  latest_release: '2025-09-03T20:12:14+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Gábor Csárdi
  - Lionel Henry
  - Jenny Bryan
  - Thomas Lin Pedersen
  - Davis Vaughan
  - Christophe Dervieux
  - Neal Richardson
  - Jeroen Ooms
  - Simon Couch
  readme_image: man/figures/logo.png
  repo: r-lib/roxygen2
  stars: 626
  title: roxygen2
  website: https://roxygen2.r-lib.org
---

roxygen2 is an essential R package that streamlines documentation for R package developers by automatically generating documentation files from inline code comments. Instead of manually creating and maintaining separate .Rd files, you write special roxygen2 comments (marked with `#'`) directly above your function definitions, and the package transforms them into proper R documentation. This approach keeps documentation and code together, reducing duplication and the risk of outdated documentation while making package development more efficient and maintainable.

Beyond just function documentation, roxygen2 manages critical package infrastructure including your NAMESPACE file, which controls what functions are exported and imported in your package. It can also handle the Collate field in your DESCRIPTION file to manage source file loading order. Whether you're documenting functions, datasets, S3/S4/R6 objects, or entire packages, roxygen2 provides a comprehensive solution that has become the de facto standard in the R community. By automating tedious documentation tasks and keeping your docs close to your code, roxygen2 lets you focus on building great packages rather than wrestling with documentation mechanics.
