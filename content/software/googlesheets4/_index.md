---
description: Google Spreadsheets R API (reboot of the googlesheets package)
github: tidyverse/googlesheets4
image: logo.png
languages:
- R
latest_release: '2025-09-03T23:00:17+00:00'
people:
- Jenny Bryan
- Joe Cheng
- Mine Çetinkaya-Rundel
title: googlesheets4
website: https://googlesheets4.tidyverse.org

external:
  contributors:
  - jennybc
  - robitalec
  - averiperny
  - csnardi
  - chrowe
  - florisvdh
  - Moohan
  - jcheng5
  - batpigandme
  - MonkmanMH
  - MichaelChirico
  - mine-cetinkaya-rundel
  - mitchelloharawild
  description: Google Spreadsheets R API (reboot of the googlesheets package)
  first_commit: '2017-04-28T02:03:33+00:00'
  forks: 53
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.816725+00:00'
  latest_release: '2025-09-03T23:00:17+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  - Joe Cheng
  - Mine Çetinkaya-Rundel
  readme_image: man/figures/logo.png
  repo: tidyverse/googlesheets4
  stars: 372
  title: googlesheets4
  website: https://googlesheets4.tidyverse.org
---

googlesheets4 is an R package that provides a modern, programmatic interface to Google Sheets through the Sheets API v4. It enables data scientists and R developers to read from and write to Google Sheets directly from their R workflows, eliminating the need for manual CSV exports or copy-pasting. With intuitive functions like read_sheet() for importing data and sheet_write() for exporting results, googlesheets4 makes it effortless to integrate spreadsheet-based collaboration into your data analysis pipelines. The package includes built-in authentication support and works seamlessly with both private and public sheets.

Designed as a complete reboot of the original googlesheets package, googlesheets4 brings the full power of the modern Sheets API to R users while maintaining consistency with tidyverse conventions. Beyond simple reading and writing, the package offers sophisticated operations like range_write() for targeted cell updates, sheet_append() for incremental data additions, and gs4_create() for programmatically generating new spreadsheets. Whether you're building automated reporting dashboards, collaborating with non-technical stakeholders through shared spreadsheets, or managing survey data collection, googlesheets4 provides a robust and pipe-friendly interface that fits naturally into tidyverse workflows.
