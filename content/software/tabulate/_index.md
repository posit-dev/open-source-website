---
description: Pretty Console Output for Tables
github: mlverse/tabulate
languages:
- C++
latest_release: '2022-02-15T17:58:52+00:00'
people:
- Daniel Falbel
title: tabulate
website: https://mlverse.github.io/tabulate/
external:
  description: Pretty Console Output for Tables
  first_commit: '2022-02-05T12:28:11+00:00'
  forks: 2
  languages:
  - C++
  last_updated: '2026-09-18T14:19:00.295508+00:00'
  latest_release: '2022-02-15T17:58:52+00:00'
  license: NOASSERTION
  people:
  - Daniel Falbel
  readme_image: man/figures/README-/demo.svg
  repo: mlverse/tabulate
  stars: 39
  title: tabulate
  website: https://mlverse.github.io/tabulate/
image: demo.svg
color: "#282D35"
---

tabulate is an R package that wraps the tabulate C++ library to pretty-print formatted tables in the console. It supports custom font styles, colors, borders, multi-byte characters, and nested tables.

The package gives R users fine-grained control over console table output — you can style individual columns or cells with font color, alignment, and bold/italic formatting using a pipe-friendly API. It handles multi-line cell content and allows embedding one table inside another, which is useful for hierarchical data display. Output relies on ANSI escape codes, so styled rendering works in terminals and environments that support ANSI strings.
