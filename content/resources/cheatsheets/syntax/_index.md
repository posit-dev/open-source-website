---
title: R syntax comparison
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-01-01'
description: Compare dollar sign, formula, and tidyverse syntax styles for common R operations side by side.
download_url: syntax.pdf
people:
- Amelia McNamara
thumbnails:
- page-1.png
- page-2.png
software:
- ggplot2
- dplyr
languages:
- R
translations:
- language: Korean
  lang: ko
  file: syntax_ko.pdf
  updated: 2018-02
  people:
  - Kwangchun Lee
- language: Spanish
  lang: es
  file: syntax_es.pdf
  updated: 2018-01
  people:
  - Riva Quiroga
---

R allows package developers to define their own syntax, resulting in three widely used styles
that express the same operations differently. This cheat sheet shows how base R (dollar sign),
formula (tilde), and tidyverse (pipe) syntax approach summary statistics, plotting, and data
wrangling using the `mtcars` dataset.

## What's covered
- Dollar sign syntax – `dataset$variable` notation and square bracket subsetting
- Formula syntax – tilde-based syntax used by `lm`, lattice, and mosaic
- Tidyverse syntax – pipe-based syntax using dplyr and ggplot2
- Summary statistics – one and two variable summaries, categorical and continuous
- Plotting – histogram, boxplot, scatter plot, bar chart, mosaic plot
- Data wrangling – subsetting rows and creating new variables
- Variations within ggplot2 – `qplot`, `ggplot`, and ggformula
