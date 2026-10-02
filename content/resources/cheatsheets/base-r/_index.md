---
title: Base R
image: page-1.png
resource_type: cheatsheet
by: community
date: '2015-03-01'
description: Core R syntax and functions covering help, packages, vectors, data I/O, programming structures, and probability distributions.
download_url: base-r.pdf
people:
- Mhairi McNeill
thumbnails:
- page-1.png
- page-2.png
languages:
- R
source_files:
- url: https://github.com/posit-dev/open-source-website/tree/main/content/resources/cheatsheets/base-r/source/base-r
  format: LaTeX
translations:
- language: Chinese (Simplified)
  lang: zh-Hans
  file: base-r_zh.pdf
  added: 2021-09
  people:
  - Fu Yongchao
  source: base-r_zh.pptx
- language: German
  lang: de
  file: base-r_de.pdf
  added: 2020-04
  people:
  - Annika Kies
  - Martin Kies
- language: Greek
  lang: el
  file: base-r_el.pdf
  updated: 2015-03
  people:
  - Kleanthis Koupidis
- language: Japanese
  lang: ja
  file: base-r_ja.pdf
  updated: 2015-03
- language: Korean
  lang: ko
  file: base-r_ko.pdf
  updated: 2015-03
  people:
  - Taeho Kim
  source: https://github.com/posit-dev/open-source-website/tree/main/content/resources/cheatsheets/base-r/source/base-r_ko
- language: Portuguese (Brazil)
  lang: pt-BR
  file: base-r_pt_br.pdf
  updated: 2015-03
  people:
  - Samuel Carleial
  source: https://github.com/posit-dev/open-source-website/tree/main/content/resources/cheatsheets/base-r/source/base-r_pt_br
- language: Spanish
  lang: es
  file: base-r_es.pdf
  updated: 2015-03
  people:
  - Anthony Romero-Cerdán
  - Thatiane Ramírez Porras
  source: base-r_es.pptx
- language: Turkish
  lang: tr
  file: base-r_tr.pdf
  updated: 2015-03
  people:
  - Elif Kartal
- language: Vietnamese
  lang: vi
  file: base-r_vi.pdf
  added: 2018-05
---

This cheat sheet covers the built-in R language and functions available without loading any external packages. It spans the building blocks of R programming, from interactive help and package management to vectors, data frames, control flow, and statistical distributions.

## What's covered
- Getting help – `?`, `help.search()`, `help(package=)`
- Working directory – `getwd()`, `setwd()`
- Using packages – `install.packages()`, `library()`
- Creating vectors – `c()`, `:`, `seq()`, `rep()`
- Vector functions – `sort()`, `rev()`, `table()`, `unique()`
- Selecting vector elements – by position and by value
- Reading and writing data – `read.table()`, `read.csv()`, `write.csv()`
- Programming – for loops, while loops, if/else statements, functions
- Distributions – density, distribution, quantile, and random functions
