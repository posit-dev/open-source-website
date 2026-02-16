---
description: '🐈🐈🐈🐈: tools for working with categorical variables (factors)'
github: tidyverse/forcats
image: logo.png
languages:
- R
latest_release: '2025-09-24T17:08:08+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Lionel Henry
- Mine Çetinkaya-Rundel
- Jeroen Janssens
title: forcats
website: https://forcats.tidyverse.org/

external:
  contributors:
  - hadley
  - batpigandme
  - robinsones
  - krlmlr
  - jennybc
  - gtm19
  - lionel-
  - kbodwin
  - zhiiiyang
  - yimingli
  - PursuitOfDataScience
  - rtaph
  - jtr13
  - jonocarroll
  - yeedle
  - luisDVA
  - lwjohnst86
  - mahjabinoyshi
  - malcolmbarrett
  - mine-cetinkaya-rundel
  - mitchelloharawild
  - monicagerber
  - njspix
  - riinuots
  - Ryo-N7
  - salim-b
  - 808sAndBR
  - sinarueeger
  - tklebel
  - tslumley
  - eipi10
  - mgacc0
  - VincentGuyader
  - yutannihilation
  - Adam-AKong
  - alberthkcheng
  - AmeliaMN
  - AndrewKinsman
  - billdenney
  - BarkleyBG
  - ismayc
  - colinbrislawn
  - dpprdan
  - davidchall
  - wilkox
  - sellisd
  - math-mcshane
  - alistaire47
  - gregrs-uk
  - jeroenjanssens
  - jimhester
  - johngoldin
  - khusmann
  description: '🐈🐈🐈🐈: tools for working with categorical variables (factors)'
  first_commit: '2016-08-08T18:07:47+00:00'
  forks: 134
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.686863+00:00'
  latest_release: '2025-09-24T17:08:08+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Lionel Henry
  - Mine Çetinkaya-Rundel
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/forcats
  stars: 552
  title: forcats
  website: https://forcats.tidyverse.org/
---

forcats is an essential R package designed to simplify working with categorical variables, known as factors in R. Factors represent data with a fixed set of possible values and are fundamental to statistical modeling and data visualization. forcats provides a comprehensive suite of tools to solve common challenges data scientists face when handling categorical data, including reordering factor levels by frequency or by another variable, manually adjusting level order for clearer visualizations, and consolidating infrequent categories into an "other" group to reduce noise in your analysis.

What makes forcats particularly valuable is its focus on improving data visualization workflows. With intuitive functions like fct_reorder() for ordering levels by another variable, fct_infreq() for frequency-based sorting, fct_relevel() for manual reordering, and fct_lump() for grouping rare values, forcats transforms messy categorical data into well-organized factors that produce clearer, more informative plots. Whether you're creating bar charts that need proper ordering, building predictive models that require specific factor level arrangements, or simply cleaning up survey data with dozens of response categories, forcats streamlines the process and lets you focus on extracting insights rather than wrestling with factor manipulation.
