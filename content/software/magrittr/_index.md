---
description: Improve the readability of R code with the pipe
github: tidyverse/magrittr
image: logo.png
languages:
- R
latest_release: '2025-09-11T16:42:35+00:00'
people:
- Lionel Henry
- Hadley Wickham
- Jeroen Janssens
- Gábor Csárdi
- Davis Vaughan
title: magrittr
website: https://magrittr.tidyverse.org

external:
  contributors:
  - smbache
  - lionel-
  - hadley
  - tonytonov
  - casallas
  - batpigandme
  - dlebauer
  - prosoitos
  - rsaporta
  - pkq
  - robertzk
  - romainfrancois
  - salim-b
  - steromano
  - trevorld
  - wibeasley
  - isomorphisms
  - jonazose
  - leerssej
  - mpadge
  - kevinushey
  - jimhester
  - jeroenjanssens
  - jdnewmil
  - HughParsonage
  - gaborcsardi
  - DavisVaughan
  - dchudz
  - cathblatter
  - bfgray3
  - ajschumacher
  description: Improve the readability of R code with the pipe
  first_commit: '2014-01-01T13:30:01+00:00'
  forks: 161
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.479406+00:00'
  latest_release: '2025-09-11T16:42:35+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Hadley Wickham
  - Jeroen Janssens
  - Gábor Csárdi
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: tidyverse/magrittr
  stars: 965
  title: magrittr
  website: https://magrittr.tidyverse.org
---

magrittr transforms how you write R code by introducing the pipe operator (`%>%`), which enables you to chain operations together in a natural, left-to-right flow. Instead of dealing with deeply nested function calls or cluttering your workspace with temporary variables, magrittr lets you express complex data transformations as clear, sequential steps that mirror how you think about the problem. This approach dramatically improves code readability and makes it easier to modify your analysis by simply inserting or removing steps in the pipeline.

Beyond the basic pipe operator, magrittr provides a suite of powerful features including flexible placeholder positioning with the dot (`.`) operator, the exposition pipe (`%$%`) for working with functions that don't support data arguments natively, and the ability to build reusable function pipelines. Whether you're performing data transformations, building statistical models, or conducting exploratory analysis, magrittr helps you write cleaner, more maintainable R code that's easier for both you and your collaborators to understand and modify.
