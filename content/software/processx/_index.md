---
description: Execute and Control Subprocesses from R
github: r-lib/processx
languages:
- R
latest_release: '2025-02-19T21:20:17+00:00'
people:
- Gábor Csárdi
- Winston Chang
- Lionel Henry
- Hadley Wickham
- Jeroen Ooms
- Jeroen Janssens
title: processx
website: https://processx.r-lib.org/

external:
  description: Execute and Control Subprocesses from R
  first_commit: '2016-08-19T13:18:57+00:00'
  forks: 43
  languages:
  - R
  last_updated: '2026-02-17T11:33:27.010584+00:00'
  latest_release: '2025-02-19T21:20:17+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Winston Chang
  - Lionel Henry
  - Hadley Wickham
  - Jeroen Ooms
  - Jeroen Janssens
  repo: r-lib/processx
  stars: 244
  title: processx
  website: https://processx.r-lib.org/
---

processx is an R package for executing and controlling system processes in the background. It lets you start external programs, read their standard output and error streams, and manage their lifecycle including killing processes when needed.

The package provides non-blocking I/O with efficient polling across single or multiple processes using OS-level facilities. It handles process cleanup automatically through garbage collection, supports callbacks for real-time output processing, and works consistently across Linux, macOS, and Windows. The package is lightweight with minimal dependencies (only R6 and ps packages).
