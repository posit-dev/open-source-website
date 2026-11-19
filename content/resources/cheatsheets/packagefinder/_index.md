---
title: Searching CRAN with packagefinder
image: page-1.png
resource_type: cheatsheet
by: community
date: '2021-03-01'
description: Search CRAN for R packages by keyword using the console or an RStudio add-in with ranking and filtering options.
download_url: packagefinder.pdf
people:
- Joachim Zuckarelli
thumbnails:
- page-1.png
languages:
- R
---

The packagefinder package provides `findPackage()` for full-text keyword searches across CRAN package names, titles, and descriptions, with results displayed in the console, RStudio viewer, or browser. It ships with an RStudio add-in for graphical searches and helper functions for viewing package details and tracking new CRAN releases.

## What's covered
- `findPackage()` – `keywords`, `mode` ("and"/"or"), `case.sensitive`, `limit.results`, `display`, `return.df`, `clipboard` arguments
- Output options – console, viewer, and browser display; dataframe return; clipboard copy
- RStudio add-in – graphical interface to `findPackage()` and `whatsNew()` with install and review features
- Additional functions – `whatsNew()`, `packageDetails()`, `lastResults()`, `go()`, `fp()` shorthand
