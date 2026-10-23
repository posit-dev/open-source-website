---
title: vegan
image: page-1.png
resource_type: cheatsheet
by: community
date: '2020-04-01'
description: Analyze ecological community data with ordination, diversity indices, and dissimilarity measures.
download_url: vegan.pdf
people:
- Bruna Luiza Silva
thumbnails:
- page-1.png
languages:
- R
---

The vegan package provides tools for descriptive community ecology, including ordination methods,
diversity analysis, and dissimilarity indices. Most multivariate tools can also be applied to
non-ecological data types.

## What's covered
- Unconstrained ordination – `metaMDS`, `plot`, `ordihull`, `ordiellipse`, `ordispider`
- Constrained ordination – `cca`, `rda`, `capscale`
- Analysis of constraints – `anova.cca` permutation test
- Diversity analysis – `diversity` (Shannon, Simpson, Fisher), `renyi`, `rarefy`
- Taxonomic diversity – `taxondive`, `taxa2dist`
- Ranked abundance distribution – `radfit`, `rad.null`
- Beta diversity – `betadiver`
- Analysis of diversity in groups – `anosim`
- Dissimilarity analysis – `vegdist` with multiple index options
- Other features – `vegemite`, `tabasco`, `beals`
