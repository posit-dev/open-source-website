---
title: overviewR
image: page-1.png
resource_type: cheatsheet
by: community
date: '2022-09-01'
description: Generate tables and plots summarizing the time and scope conditions of a panel dataset.
download_url: overviewR.pdf
people:
- Cosima Meyer
- Dennis Hammerschmidt
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

The overviewR package helps researchers inspect the temporal and cross-sectional coverage of panel datasets. It produces summary tables (`overview_tab()`), cross-tabulations (`overview_crosstab()`), ggplot2-based sample and NA plots, and LaTeX-ready output compatible with knitr and flextable.

## What's covered
- `overview_tab()` – collapse time conditions by unit ID, including complex date columns
- `overview_crosstab()` – cross-tabulate units by two threshold-based conditions
- `overview_na()` – horizontal ggplot2 bar chart of missing values per variable
- `overview_plot()` – ggplot2 graphic of sample coverage over time
- `overview_crossplot()` – visualize cross-tabulation conditions as a scatter plot
- Export tables – `overview_latex()` for LaTeX output with `save_out` and `file_path` options
- Workflows – tidyverse pipe integration and compatibility with knitr `kable()` and ggplot2 `ggsave()`
