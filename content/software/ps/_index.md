---
description: R package to query, list, manipulate system processes
github: r-lib/ps
languages:
- C
latest_release: '2025-04-12T09:22:49+00:00'
people:
- Gábor Csárdi
- Lionel Henry
- George Stagg
- Jeroen Janssens
title: ps
website: https://ps.r-lib.org/

external:
  contributors:
  - gaborcsardi
  - dansmith01
  - QuLogic
  - okhoma
  - barracuda156
  - francisbarton
  - lionel-
  - batpigandme
  - MichaelChirico
  - brendanf
  - georgestagg
  - JFormoso
  - jeroenjanssens
  - ruarai
  - reikoch
  description: R package to query, list, manipulate system processes
  first_commit: '2018-06-15T12:19:35+00:00'
  forks: 22
  languages:
  - C
  last_updated: '2026-02-13T14:17:19.780192+00:00'
  latest_release: '2025-04-12T09:22:49+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Lionel Henry
  - George Stagg
  - Jeroen Janssens
  repo: r-lib/ps
  stars: 82
  title: ps
  website: https://ps.r-lib.org/
---

ps is a cross-platform R package that provides programmatic access to system processes on Windows, macOS, and Linux. It enables developers to query comprehensive process information including process IDs, parent-child relationships, executable paths, command-line arguments, memory consumption, CPU usage, and file descriptors. Beyond simple queries, ps offers robust process manipulation capabilities such as suspending and resuming processes, sending signals, and terminating execution, all while handling platform-specific differences seamlessly.

What makes ps particularly valuable for data scientists and developers is its sophisticated handling of common process management challenges. The package includes built-in safeguards against pid reuse scenarios where operating systems recycle process IDs, ensuring your queries always target the correct process. Whether you're monitoring long-running computations, managing parallel workflows, cleaning up zombie processes, or analyzing system resource usage, ps integrates smoothly with tidyverse tools for filtering and analyzing process data. Based on the proven psutil Python package, ps brings enterprise-grade process management capabilities to R environments with a clean, consistent API.
