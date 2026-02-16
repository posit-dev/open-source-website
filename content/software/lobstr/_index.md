---
description: Understanding complex R objects with tools similar to str()
github: r-lib/lobstr
image: logo.png
languages:
- C
latest_release: '2025-11-14T13:22:25+00:00'
people:
- Hadley Wickham
- Nick Strayer
- Lionel Henry
- Jeroen Janssens
title: lobstr
website: https://lobstr.r-lib.org/

external:
  contributors:
  - hadley
  - nstrayer
  - lionel-
  - jimhester
  - batpigandme
  - yutannihilation
  - Bisaloo
  - jeroenjanssens
  - jmcphers
  - krlmlr
  - samrickman
  - terrytangyuan
  description: Understanding complex R objects with tools similar to str()
  first_commit: '2015-03-20T20:57:44+00:00'
  forks: 30
  languages:
  - C
  last_updated: '2026-02-13T14:17:18.770140+00:00'
  latest_release: '2025-11-14T13:22:25+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Nick Strayer
  - Lionel Henry
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/lobstr
  stars: 312
  title: lobstr
  website: https://lobstr.r-lib.org/
---

lobstr is a diagnostic toolkit designed to help R developers inspect and understand the internal structure of objects with unprecedented clarity. Building on the foundation of R's familiar str() function, lobstr provides specialized tools that reveal how R actually works under the hood. Whether you're debugging complex code, optimizing memory usage, or simply trying to understand how R evaluates your expressions, lobstr transforms abstract concepts about R's internals into visual, comprehensible representations that make troubleshooting and learning intuitive.

The package offers four powerful diagnostic tools that each address a specific aspect of R's behavior. The ast() function visualizes abstract syntax trees to show exactly how R parses your code, while ref() reveals how objects share memory across data structures, helping you identify when variables point to the same data rather than holding copies. The obj_size() function provides accurate memory footprint analysis by accounting for shared references, and cst() displays call stack relationships to help you trace function execution flow. Together, these tools give data scientists and developers the insights they need to write more efficient code, understand performance characteristics, and master R's evaluation model.
