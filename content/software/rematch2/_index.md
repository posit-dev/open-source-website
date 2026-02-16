---
description: Tidy output from regular expression matches
github: r-lib/rematch2
languages:
- R
latest_release: '2020-04-30T10:30:07+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
title: rematch2
website: ''

external:
  contributors:
  - gaborcsardi
  - krlmlr
  - maelle
  - wibeasley
  - brodieG
  - jennybc
  description: Tidy output from regular expression matches
  first_commit: '2017-06-20T15:18:28+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.520261+00:00'
  latest_release: '2020-04-30T10:30:07+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jenny Bryan
  repo: r-lib/rematch2
  stars: 46
  title: rematch2
  website: ''
---

Regular expressions are powerful, but R's base regex functions return complex nested lists that can be difficult to work with. rematch2 transforms this experience by wrapping `regexpr` and `gregexpr` to deliver results as tidy tibbles instead. Whether you're extracting the first match with `re_match()` or finding all occurrences with `re_match_all()`, you get clean data frames where named capture groups automatically become intuitive column names.

This approach makes pattern matching accessible for data scientists who need to parse structured text—like dates, URLs, or identifiers—without wrestling with unwieldy list structures. rematch2 also tracks exact character positions where matches occur, making it invaluable for text manipulation pipelines. By prioritizing usability and seamless integration with tidyverse workflows, rematch2 helps you spend less time debugging regex output and more time analyzing your data.
