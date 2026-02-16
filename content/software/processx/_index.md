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
  contributors:
  - gaborcsardi
  - wch
  - lionel-
  - infotroph
  - rschuchmann
  - hadley
  - domq
  - smu-ggl
  - MichaelChirico
  - dominik-handler
  - salim-b
  - maelle
  - IronistM
  - kevinushey
  - kendonB
  - jdblischak
  - jeroen
  - jeroenjanssens
  - hugomflavio
  - davechilders
  description: Execute and Control Subprocesses from R
  first_commit: '2016-08-19T13:18:57+00:00'
  forks: 43
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.104774+00:00'
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

processx is an R package that enables you to launch, control, and monitor system processes in the background without blocking your R session. Whether you're running long computations, calling external command-line tools, or orchestrating complex data pipelines, processx gives you fine-grained control over subprocess execution while keeping your interactive R environment responsive. The package provides sophisticated mechanisms for capturing standard output and error streams in real-time, managing process lifecycles, and handling multiple concurrent processes through its polling system.

Key features include non-blocking process execution that prevents R from freezing, the ability to read output line-by-line or in chunks with callback functions, support for writing to standard input, and cross-platform compatibility across Linux, macOS, and Windows. For data scientists and developers building tools that interact with external programs or need to manage complex computational workflows, processx offers the reliability and flexibility to implement timeouts, responsive termination, and real-time output processing with minimal dependencies.