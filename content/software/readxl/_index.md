---
description: Read excel files (.xls and .xlsx) into R 🖇
github: tidyverse/readxl
image: logo.png
languages:
- C++
latest_release: '2025-03-07T07:25:18+00:00'
people:
- Jenny Bryan
- Hadley Wickham
- Jeroen Ooms
- Gábor Csárdi
- Davis Vaughan
title: readxl
website: https://readxl.tidyverse.org

external:
  contributors:
  - jennybc
  - hadley
  - jeroen
  - jirkalewandowski
  - batpigandme
  - jimhester
  - gaborcsardi
  - bquast
  - zeehio
  - sbearrows
  - nacnudus
  - MichaelChirico
  - DavisVaughan
  - SokolovAnatoliy
  - KaiAragaki
  - kevinushey
  - kwstat
  - krlmlr
  - twopatek
  - mkuhn
  - PedramNavid
  - rohan-shah
  - boshek
  - stephenc
  - tklebel
  - olivroy
  - struckma
  - JakeRuss
  - gergness
  - gl-eb
  - FvD
  - fontikar
  - fermumen
  - eringrand
  - dchiu911
  - benmarwick
  - averiperny
  - apjanke
  - apreshill
  - elgabbas
  description: Read excel files (.xls and .xlsx) into R 🖇
  first_commit: '2015-03-13T14:50:20+00:00'
  forks: 196
  languages:
  - C++
  last_updated: '2026-02-13T14:17:08.575442+00:00'
  latest_release: '2025-03-07T07:25:18+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Hadley Wickham
  - Jeroen Ooms
  - Gábor Csárdi
  - Davis Vaughan
  readme_image: man/figures/logo.png
  repo: tidyverse/readxl
  stars: 751
  title: readxl
  website: https://readxl.tidyverse.org
---

readxl makes it easy to get data out of Excel and into R. The package supports both legacy `.xls` files and modern `.xlsx` formats, with the major advantage of having no external dependencies—no Java, no Perl, just pure R. This means it's straightforward to install and works reliably across all operating systems. Whether you're wrangling data from colleagues who live in Excel or integrating spreadsheet data into reproducible analysis pipelines, readxl provides a fast and dependable solution.

The package handles the messy realities of Excel files with grace. It automatically detects file formats, converts character encodings to UTF-8, manages datetime values across different Excel date systems, and returns data as tibbles for seamless integration with tidyverse workflows. With intuitive functions like `read_excel()` for imports and `excel_sheets()` for exploring workbook contents, plus flexible options for selecting cell ranges and specifying column types, readxl gives data scientists the tools they need to efficiently bridge the gap between Excel and R.
