---
description: Glue strings to data in R. Small, fast, dependency free interpreted string
  literals.
github: tidyverse/glue
image: logo.png
languages:
- R
latest_release: '2024-09-27T15:59:19+00:00'
people:
- Jenny Bryan
- Hadley Wickham
- Gábor Csárdi
- Lionel Henry
- Davis Vaughan
- Mine Çetinkaya-Rundel
- Jeroen Janssens
title: glue
website: https://glue.tidyverse.org

external:
  contributors:
  - jimhester
  - jennybc
  - hadley
  - batpigandme
  - gaborcsardi
  - foundinblank
  - shrektan
  - dpprdan
  - egnha
  - lionel-
  - mgirlich
  - krlmlr
  - MichaelChirico
  - DavisVaughan
  - salim-b
  - alandipert
  - mitchelloharawild
  - pnacht
  - zeehio
  - Shelmith-Kariuki
  - stephhazlitt
  - laderast
  - tstev
  - BroVic
  - wibeasley
  - baptiste
  - dmurdoch
  - eitsupi
  - landesbergn
  - moodymudskipper
  - mine-cetinkaya-rundel
  - maelle
  - kendonB
  - jeroenjanssens
  - Moohan
  - ijlyttle
  - echasnovski
  - alistaire47
  - davidchall
  - cdhowe
  - BrennanAntone
  - billdenney
  - md0u80c9
  description: Glue strings to data in R. Small, fast, dependency free interpreted
    string literals.
  first_commit: '2016-12-23T21:07:25+00:00'
  forks: 64
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.750844+00:00'
  latest_release: '2024-09-27T15:59:19+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Hadley Wickham
  - Gábor Csárdi
  - Lionel Henry
  - Davis Vaughan
  - Mine Çetinkaya-Rundel
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidyverse/glue
  stars: 742
  title: glue
  website: https://glue.tidyverse.org
---

Glue provides interpreted string literals for R, making it easy to seamlessly interpolate data into strings. Unlike traditional methods like `paste()` or `sprintf()`, glue lets you embed R expressions directly within curly braces, creating readable and maintainable string templates where the final output format is immediately apparent. The package is small, fast, and dependency-free, designed to minimize syntactic noise while maximizing code clarity.

The package offers several powerful functions to suit different use cases. The core `glue()` function interpolates values from your environment or named arguments, while `glue_data()` works naturally with data frames and pipes for batch processing. For data scientists working with databases, `glue_sql()` provides safe SQL statement generation with automatic quoting. All functions support vectorization over data, automatic whitespace trimming, and arbitrary R expressions within interpolation brackets, making glue an essential tool for anyone who needs to generate formatted strings efficiently in R.
