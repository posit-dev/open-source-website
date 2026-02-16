---
description: Data table backend for dplyr
github: tidyverse/dtplyr
image: logo.png
languages:
- R
latest_release: '2026-02-10T17:24:35+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Davis Vaughan
- Jeroen Janssens
title: dtplyr
website: https://dtplyr.tidyverse.org

external:
  contributors:
  - hadley
  - markfairbanks
  - romainfrancois
  - mgirlich
  - eutwt
  - lionel-
  - christophsax
  - krlmlr
  - batpigandme
  - hannes
  - MichaelChirico
  - kevinushey
  - jimhester
  - arunsrinivasan
  - lindbrook
  - DavisVaughan
  - uribo
  - smingerson
  - ilarischeinin
  - pimentel
  - earino
  - leondutoit
  - hs3180
  - xiaodaigh
  - tmastny
  - JoshuaSturm
  - cosinequanon
  - richpauloo
  - psanker
  - jonthegeek
  - jeroenjanssens
  - jl5000
  - eibanez
  - craigcitro
  - alyst
  description: Data table backend for dplyr
  first_commit: '2016-03-07T23:28:16+00:00'
  forks: 60
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.638975+00:00'
  latest_release: '2026-02-10T17:24:35+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Davis Vaughan
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/dtplyr
  stars: 673
  title: dtplyr
  website: https://dtplyr.tidyverse.org
---

dtplyr bridges two powerful R data manipulation ecosystems by providing a translation layer between dplyr and data.table. It enables you to write code using dplyr's intuitive and expressive syntax while automatically gaining the exceptional speed and computational efficiency of data.table under the hood. This approach is particularly valuable when working with large datasets where performance matters, allowing you to maintain readable, familiar dplyr code while achieving significantly faster execution times.

The package works through a simple lazy evaluation workflow: wrap your data with lazy_dt(), chain together standard dplyr verbs like filter(), mutate(), group_by(), and summarise(), then materialize the result when needed. This seamless integration means you can leverage your existing dplyr knowledge without learning data.table's different syntax, while still benefiting from its performance advantages. With minimal translation overhead of under 1ms per operation, dtplyr makes it easy to optimize your data pipelines for speed without sacrificing code clarity or readability.
