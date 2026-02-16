---
description: Platform independent zip compression via miniz
github: r-lib/zip
languages:
- C
latest_release: '2025-05-13T13:31:24+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
- Jeroen Ooms
title: zip
website: https://r-lib.github.io/zip/

external:
  contributors:
  - gaborcsardi
  - jefferis
  - jimhester
  - m-muecke
  - zeehio
  - QuLogic
  - weshinsley
  - chainsawriot
  - AshesITR
  - daattali
  - jeroenjanssens
  - jeroen
  - batpigandme
  - wibeasley
  - bart1
  - jbfagotfede39
  description: Platform independent zip compression via miniz
  first_commit: '2017-04-09T01:06:13+00:00'
  forks: 23
  languages:
  - C
  last_updated: '2026-02-13T14:17:19.404428+00:00'
  latest_release: '2025-05-13T13:31:24+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/zip
  stars: 93
  title: zip
  website: https://r-lib.github.io/zip/
---

The **zip** package provides cross-platform ZIP compression capabilities for R, making it easy to create, manage, and extract compressed archives directly from your R workflows. Built on the lightweight miniz library, it delivers reliable compression functionality that works consistently across Windows, macOS, and Linux without requiring external system tools. Whether you're packaging datasets for sharing, archiving project outputs, or managing large collections of files, zip offers a straightforward interface that integrates seamlessly into your data pipelines.

Key features include recursive directory compression, the ability to list and inspect archive contents as data frames, and support for background processing to handle large files without blocking your R session. The package automatically handles file permissions, timestamps, and metadata, giving you fine-grained control over your compressed archives. For data scientists distributing reproducible research or developers building packages that need to bundle resources, zip provides a dependable solution for all your compression needs within the R ecosystem.
