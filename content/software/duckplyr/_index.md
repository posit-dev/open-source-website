---
description: A drop-in replacement for dplyr, powered by DuckDB for speed.
github: tidyverse/duckplyr
image: logo.png
languages:
- R
latest_release: '2025-11-03T23:28:28+00:00'
people:
- Davis Vaughan
- Hadley Wickham
- Jeroen Janssens
- Mine Çetinkaya-Rundel
title: duckplyr
website: https://duckplyr.tidyverse.org/

external:
  contributors:
  - krlmlr
  - github-actions[bot]
  - maelle
  - Tmonster
  - Copilot
  - toppyy
  - hannes
  - andreranza
  - TimTaylor
  - joakimlinde
  - DavisVaughan
  - wibeasley
  - stefanlinner
  - hadley
  - jeroenjanssens
  - luisDVA
  - mine-cetinkaya-rundel
  description: A drop-in replacement for dplyr, powered by DuckDB for speed.
  first_commit: '2022-11-29T08:20:48+00:00'
  forks: 25
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.991153+00:00'
  latest_release: '2025-11-03T23:28:28+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Hadley Wickham
  - Jeroen Janssens
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: tidyverse/duckplyr
  stars: 372
  title: duckplyr
  website: https://duckplyr.tidyverse.org/
---

duckplyr is a high-performance alternative to dplyr that seamlessly integrates DuckDB's powerful analytical engine into your existing data analysis workflows. It serves as a drop-in replacement for dplyr, meaning you can run your existing dplyr code without any modifications while benefiting from dramatic speed improvements and the ability to analyze datasets that exceed your system's memory. By automatically overwriting dplyr methods for your entire session, duckplyr intelligently routes operations through DuckDB when possible, falling back to standard dplyr when needed to ensure consistent results every time.

What makes duckplyr particularly valuable for data scientists and developers is its ability to handle modern data challenges effortlessly. You can query remote Parquet, CSV, and JSON files directly from disk or web sources without downloading them first, leverage lazy evaluation to optimize query execution, and work with larger-than-memory datasets using familiar tidyverse syntax. The package combines dplyr's intuitive data manipulation interface with DuckDB's columnar processing efficiency, giving you the best of both worlds: a comfortable development experience with production-grade performance, all while maintaining the standard tibble outputs you expect from the tidyverse ecosystem.
