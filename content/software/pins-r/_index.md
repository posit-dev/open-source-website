---
color: '#F1C7A0'
description: Pin, discover, and share resources
github: rstudio/pins-r
image: logo.png
languages:
- R
latest_release: '2025-04-30T12:56:12+00:00'
people:
- Hadley Wickham
- Julia Silge
- Neal Richardson
- Edgar Ruiz
- Christophe Dervieux
- Daniel Falbel
- Gábor Csárdi
- Jenny Bryan
- Joe Cheng
- Michael Chow
title: pins-r
website: https://pins.rstudio.com

external:  # updated automatically, do not edit
  description: Pin, discover, and share resources
  first_commit: '2019-03-22T16:06:23+00:00'
  forks: 67
  languages:
  - R
  last_updated: '2026-03-05T16:14:45.038961+00:00'
  latest_release: '2025-04-30T12:56:12+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Julia Silge
  - Neal Richardson
  - Edgar Ruiz
  - Christophe Dervieux
  - Daniel Falbel
  - Gábor Csárdi
  - Jenny Bryan
  - Joe Cheng
  - Michael Chow
  readme_image: man/figures/logo.png
  repo: rstudio/pins-r
  stars: 333
  title: pins-r
  website: https://pins.rstudio.com
---

The pins package enables publishing and sharing of R objects (data, models, etc.) across projects and collaborators. It supports various storage backends including local folders, Posit Connect, Databricks, Amazon S3, Google Cloud Storage, Azure, and Microsoft 365, with automatic versioning for tracking changes and reproducing historical analyses.

Pins simplifies collaborative data workflows by providing a consistent API (`pin_write()` and `pin_read()`) regardless of storage backend. It supports multiple file formats (RDS, Parquet, Arrow, CSV, JSON) and integrates with Posit Connect's permission system for access control. The package also offers cross-language compatibility, allowing Python users to read pins created in R and vice versa.
