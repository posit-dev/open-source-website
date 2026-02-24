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

external:  # updated automatically, do not edit
  description: Read excel files (.xls and .xlsx) into R 🖇
  first_commit: '2015-03-13T14:50:20+00:00'
  forks: 196
  languages:
  - C++
  last_updated: '2026-02-24T09:26:23.360012+00:00'
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

The readxl package imports Excel data into R, supporting both `.xls` and `.xlsx` formats. It reads tabular data from Excel files without requiring external dependencies like Java or Perl, making it easy to install across all operating systems.

The package automatically handles common Excel quirks like date specifications (Windows 1900 and Mac 1904), re-encodes non-ASCII characters to UTF-8, and detects the minimal data rectangle to import. Users can control which cells to read through flexible range specification, skip rows, limit the number of rows read, and customize column names and types. Returns are tibbles for better integration with tidyverse workflows.
