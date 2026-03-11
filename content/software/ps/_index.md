---
color: '#404041'
description: R package to query, list, manipulate system processes
github: r-lib/ps
image: logo.svg
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

external:  # updated automatically, do not edit
  description: R package to query, list, manipulate system processes
  first_commit: '2018-06-15T12:19:35+00:00'
  forks: 22
  languages:
  - C
  last_updated: '2026-03-05T16:28:06.611715+00:00'
  latest_release: '2025-04-12T09:22:49+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Lionel Henry
  - George Stagg
  - Jeroen Janssens
  repo: r-lib/ps
  stars: 83
  title: ps
  website: https://ps.r-lib.org/
---

The ps package provides an API for querying and manipulating system processes in R. It allows you to list all running processes, get detailed information about specific processes, and perform operations like suspending, resuming, or terminating them.

The package handles process identification safely by tracking both process IDs and creation times to avoid issues with PID reuse. It works across Windows, macOS, and Linux and provides robust handling of finished and zombie processes. The implementation is based on the Python psutil library and includes functions for accessing process attributes like memory usage, CPU time, open files, environment variables, and parent-child relationships.
