---
description: Call R from R
github: r-lib/callr
image: simple.svg
languages:
- R
latest_release: '2024-03-25T12:09:25+00:00'
people:
- Gábor Csárdi
- Daniel Falbel
- Jenny Bryan
- Lionel Henry
- Hadley Wickham
- Winston Chang
- Jeroen Ooms
- Jeroen Janssens
title: callr
website: https://callr.r-lib.org/

external:
  contributors:
  - gaborcsardi
  - klmr
  - krlmlr
  - dfalbel
  - jdblischak
  - jennybc
  - lionel-
  - hadley
  - shrektan
  - wch
  - pkq
  - mihaiconstantin
  - multimeric
  - karawoo
  - jimhester
  - jeroen
  - jeroenjanssens
  - giocomai
  - daattali
  - djnavarro
  - nuest
  - ChrisMuir
  description: Call R from R
  first_commit: '2016-05-13T10:26:09+00:00'
  forks: 40
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.037986+00:00'
  latest_release: '2024-03-25T12:09:25+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Daniel Falbel
  - Jenny Bryan
  - Lionel Henry
  - Hadley Wickham
  - Winston Chang
  - Jeroen Ooms
  - Jeroen Janssens
  readme_image: man/figures/simple.svg
  repo: r-lib/callr
  stars: 304
  title: callr
  website: https://callr.r-lib.org/
---

callr is an essential R package that enables you to execute R functions in separate, isolated R processes. This capability is invaluable when you need to run computations without affecting your current R environment, test code in a clean session, or manage resource-intensive operations that might otherwise interfere with your interactive workflow. By seamlessly transferring function arguments to subprocesses and returning results back to your main session, callr provides a robust foundation for reliable and reproducible R development.

What makes callr particularly powerful is its flexibility in handling different execution patterns. Whether you need a quick one-off computation with the r() function, a background process running asynchronously with r_bg(), or a persistent R session for repeated function calls with r_session, callr adapts to your workflow. The package handles all the complexity of process management while preserving error stack traces, managing output streams, and ensuring that your results transfer back safely. For data scientists and developers working on package development, testing workflows, or complex analytical pipelines, callr delivers the isolation and control needed to build robust, maintainable R code.
