---
color: '#31A459'
description: A fresh approach to string manipulation in R
github: tidyverse/stringr
image: logo.png
languages:
- R
latest_release: '2025-11-03T22:09:36+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Gábor Csárdi
- Tomasz Kalinowski
- Christophe Dervieux
- Garrick Aden-Buie
- Jeroen Janssens
- Joe Cheng
tags:
- tidyverse
title: stringr
website: https://stringr.tidyverse.org

external:  # updated automatically, do not edit
  description: A fresh approach to string manipulation in R
  first_commit: '2009-11-08T22:20:08+00:00'
  forks: 195
  languages:
  - R
  last_updated: '2026-03-20T10:27:40.579897+00:00'
  latest_release: '2025-11-03T22:09:36+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Gábor Csárdi
  - Tomasz Kalinowski
  - Christophe Dervieux
  - Garrick Aden-Buie
  - Jeroen Janssens
  - Joe Cheng
  readme_image: man/figures/logo.png
  repo: tidyverse/stringr
  stars: 658
  title: stringr
  website: https://stringr.tidyverse.org
---

stringr is an R package that provides a cohesive set of functions for working with strings, built on top of the stringi package which uses the ICU C library for fast, correct string manipulation. It focuses on the most common string operations with a consistent interface where all functions start with `str_` and take a vector of strings as the first argument.

The package simplifies string manipulation through consistent function naming and behavior that works well with pipes and tidyverse workflows. It provides seven main pattern-matching verbs (detect, count, subset, locate, extract, match, replace, split) that work with regular expressions by default, plus support for fixed bytes, human letter collation, and boundary matching. Compared to base R string functions, stringr offers more predictable behavior where missing inputs produce missing outputs and zero-length inputs produce zero-length outputs.
