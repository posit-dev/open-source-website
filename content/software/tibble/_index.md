---
description: A modern re-imagining of the data frame
github: tidyverse/tibble
image: logo.png
languages:
- R
latest_release: '2026-01-10T18:28:34+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Lionel Henry
- Davis Vaughan
- Tomasz Kalinowski
- Max Kuhn
- Jeroen Janssens
- Christophe Dervieux
title: tibble
website: https://tibble.tidyverse.org/

external:
  contributors:
  - krlmlr
  - hadley
  - romainfrancois
  - jennybc
  - lionel-
  - DavisVaughan
  - github-actions[bot]
  - jimhester
  - zhilongjia
  - kevinushey
  - batpigandme
  - anhqle
  - olivroy
  - IndrajeetPatil
  - hannes
  - patperry
  - ilarischeinin
  - maelle
  - ncarchedi
  - rbjanis
  - mgirlich
  - lindbrook
  - kevinykuo
  - jeffreyhanson
  - echasnovski
  - TimTaylor
  - stufield
  - MichaelChirico
  - gdequeiroz
  - dholstius
  - Copilot
  - t-kalinowski
  - tappek
  - earowang
  - uribo
  - cosinequanon
  - maxheld83
  - topepo
  - Enchufa2
  - earino
  - imanuelcostigan
  - jeroenjanssens
  - kwstat
  - Layalchristine24
  - lorenzwalthert
  - luisDVA
  - michaelweylandt
  - pat-s
  - sharlagelfand
  - mundl
  - heavywatal
  - xiaodaigh
  - anabbott
  - eitsupi
  - hs3180
  - vinhtantran
  - web-flow
  - etiennebr
  - QuLogic
  - edwindj
  - eibanez
  - daviddalpiaz
  - craigcitro
  - csgillespie
  - cderv
  - BrianDiggs
  - bhive01
  - bgreenwell
  - arunsrinivasan
  - andreranza
  - alexwhan
  description: A modern re-imagining of the data frame
  first_commit: '2015-10-28T23:57:00+00:00'
  forks: 135
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.607674+00:00'
  latest_release: '2026-01-10T18:28:34+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Lionel Henry
  - Davis Vaughan
  - Tomasz Kalinowski
  - Max Kuhn
  - Jeroen Janssens
  - Christophe Dervieux
  readme_image: man/figures/logo.png
  repo: tidyverse/tibble
  stars: 737
  title: tibble
  website: https://tibble.tidyverse.org/
---

Tibbles are a modern reimagining of R's data frames, designed to make data manipulation more reliable and user-friendly. While maintaining compatibility with the broader R ecosystem, tibbles take a stricter approach that prevents common pitfalls: they never silently change variable names or types, don't perform partial matching on column names, and only recycle vectors of length 1. This deliberate pickiness helps you catch errors early and write cleaner, more maintainable code.

The enhanced printing methods make working with large datasets a pleasure, displaying column types upfront and intelligently truncating output for readability. Tibbles also provide first-class support for list columns, making it natural to work with complex, nested data structures. By making implicit assumptions explicit and refusing to guess what you meant, tibbles reduce debugging time and help data scientists and developers build more robust data pipelines.
