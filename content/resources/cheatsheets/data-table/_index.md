---
title: data.table
image: page-1.png
resource_type: cheatsheet
by: community
date: '2026-07-01'
description: Transform data in R with concise `dt[i, j, by]` syntax for fast in-memory subsetting, column operations, and grouped aggregation.
download_url: datatable.pdf
people:
- Erik Petrovski
- Mara Destefanis
- Tyson Barrett
thumbnails:
- page-1.png
- page-2.png
languages:
- R
source_files:
- file: datatable.pptx
  format: PowerPoint
translations:
- language: French
  lang: fr
  file: datatable_fr.pdf
  added: 2025-09
  people:
  - Christian Wiat
  source: datatable_fr.pptx
- language: Portuguese (Brazil)
  lang: pt-BR
  file: datatable_pt_br.pdf
  edition: data.table 1.11.8
  updated: 2019-01
  people:
  - Samuel Carleial
  source: datatable_pt_br.pptx
---

data.table extends R's native data frame with an extremely fast and memory-efficient syntax built around `dt[i, j, by]`. It supports in-place column creation and modification with `:=`, avoiding copies, and is fully compatible with functions that work on data frames.

## What's covered
- Basics – `data.table()`, `setDT()`, `as.data.table()`
- Subset rows using i – row numbers, column values, logical operators
- Extract and summarize columns with j – `.(cols)`, summary functions
- Compute and delete columns – `:=` operator, type conversion
- Group according to by – `by`, `keyby`, common grouped operations
- Chaining – `dt[...][...]`
- Functions for data.tables – `setorder()`, `rbind()`, `cbind()`, `setnames()`, `unique()`, `uniqueN()`
- Apply a function to multiple columns – `lapply(.SD, fun)` with `.SDcols`
