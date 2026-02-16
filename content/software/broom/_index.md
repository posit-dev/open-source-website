---
description: Convert statistical analysis objects from R into tidy format
github: tidymodels/broom
image: logo.png
languages:
- R
latest_release: '2025-12-03T20:26:24+00:00'
people:
- Simon Couch
- Max Kuhn
- Emil Hvitfeldt
- Hadley Wickham
- Julia Silge
- Davis Vaughan
- Hannah Frick
- Jenny Bryan
- Jeroen Janssens
title: broom
website: https://broom.tidymodels.org

external:
  contributors:
  - simonpcouch
  - alexpghayes
  - grantmcdermott
  - dchiu911
  - dgrtwo
  - mdlincoln
  - hughjonesd
  - jgabry
  - bbolker
  - vincentarelbundock
  - gregmacfarlane
  - karldw
  - ddsjoberg
  - MatthieuStigler
  - IndrajeetPatil
  - lilymedina
  - nutterb
  - bwiernik
  - mkuehn10
  - topepo
  - briatte
  - larmarange
  - thisisnic
  - LukasWallrich
  - tappek
  - jiho
  - leejasme
  - mattle24
  - mbojan
  - olivroy
  - petrhrobar
  - jayhesselberth
  - tavareshugo
  - EmilHvitfeldt
  - PirateGrunt
  - jrnold
  - capnrefsmmat
  - crsh
  - hmalmedal
  - malcolmbarrett
  - tarensanders
  - hadley
  - cwang23
  - pkq
  - mariusbarth
  - bschneidr
  - corybrunson
  - atheriel
  - dmenne
  - jenzopr
  - jimhester
  - juliasilge
  - lukesonnet
  - batpigandme
  - zeehio
  - adibender
  - bfgray3
  - jyuu
  - x249wang
  - junkka
  - ilapros
  - rudeboybert
  - DavisVaughan
  - hfrick
  - lwjohnst86
  - PursuitOfDataScience
  - GegznaV
  - kuriwaki
  - MichaelChirico
  - ankrauska
  - erleholgersen
  - bensoltoff
  - brunaw
  - lepennec
  - gavinsimpson
  - haozhu233
  - KZARCA
  - paul-buerkner
  - mjskay
  - nt-williams
  - pjpaulpj
  - ste-tuf
  - ShreyasSingh
  - serina-robinson
  - rsbivand
  - riinuots
  - rtaph
  - nmjakobsen
  - milanwiedemann
  - zietzm
  - michaelweylandt
  - m-sostero
  - MarcusWalz
  - lselzer
  - ellessenne
  - AntoniosBarotsis
  - tylerlittlefield
  - drvictorvs
  - weiyangtham
  - cassws
  - smith-abby
  - anniew
  - gravesti
  - jarvisc1
  - jsr-p
  - karissawhiting
  - khailper
  - puterleat
  - shabbybanks
  - wilsonfreitas
  - asbates
  - andrewjlm
  - angusmoore
  - billdenney
  - bmannakee
  - softloud
  - tripartio
  - stillmatic
  - ChuliangXiao
  - drsimonj
  - atyre2
  - Edild
  - ethchr
  - focardozom
  - HenrikBengtsson
  - hideaki
  - yutannihilation
  - hongooi73
  - jrob95
  - jwilber
  - jmuhlenkamp
  - jaspercooper
  - jennybc
  - jbiesanz
  - jeroenjanssens
  - cimentadaj
  - josue-rodriguez
  - JanLauGe
  - lmullen
  - llendway
  description: Convert statistical analysis objects from R into tidy format
  first_commit: '2014-09-11T19:17:04+00:00'
  forks: 305
  languages:
  - R
  last_updated: '2026-02-13T14:17:11.980273+00:00'
  latest_release: '2025-12-03T20:26:24+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Max Kuhn
  - Emil Hvitfeldt
  - Hadley Wickham
  - Julia Silge
  - Davis Vaughan
  - Hannah Frick
  - Jenny Bryan
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/broom
  stars: 1512
  title: broom
  website: https://broom.tidymodels.org
---

broom is an essential R package that transforms complex statistical model outputs into tidy data structures, making them easy to work with in modern data analysis workflows. Instead of dealing with messy, inconsistent model objects, broom provides three core functions that standardize how you interact with statistical results: tidy() extracts model components like regression coefficients into a clean format perfect for visualization and further analysis, glance() returns a single-row summary with goodness-of-fit metrics for quick model comparison, and augment() enriches your original data with model-derived predictions and residuals. With support for over 100 models from popular packages, broom seamlessly integrates with the tidyverse ecosystem and tidy data principles.

What makes broom particularly valuable for data scientists and developers is how it streamlines the entire modeling workflow. Whether you're exploring a single model, comparing multiple competing models, or building reproducible analysis pipelines, broom eliminates the friction of extracting information from diverse model objects. This consistency enables you to spend less time wrestling with data structures and more time on the analytical work that matters, from creating custom visualizations of model results to efficiently documenting your findings in reports and presentations.
