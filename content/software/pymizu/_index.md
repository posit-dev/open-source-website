---
color: '#1b66f8'
description: Async and parallel Python at thread speed over shared memory
github: shikokuchuo/pymizu
image: logo.svg
languages:
- Python
people:
- Charlie Gao
title: pymizu
topics:
- Data Wrangling
- Interactive Apps
website: https://shikokuchuo.net/pymizu/

external:  # updated automatically, do not edit
  description: Async and parallel Python at thread speed over shared memory
  first_commit: '2026-08-21T09:24:40+00:00'
  forks: 0
  languages:
  - Python
  last_updated: '2026-11-02T14:24:06.438482+00:00'
  license: MIT
  people:
  - Charlie Gao
  readme_image: https://raw.githubusercontent.com/shikokuchuo/pymizu/main/docs/assets/logo.svg
  repo: shikokuchuo/pymizu
  stars: 3
  title: pymizu
  website: https://shikokuchuo.net/pymizu/
---

pymizu is a Python package for async and parallel computing that communicates over shared memory instead of sockets. A task round trip drops from ~100 µs over sockets to under 1 µs, so work can be divided as finely as it would be across threads.

pymizu is built on libmizu, a C library for lock-free shared-memory IPC, and mizu binds the same core for R, so pool workers can be R processes and lists, dicts, NumPy arrays, and Arrow tables cross between Python and R as zero-copy views. Pools provide a drop-in `concurrent.futures.Executor` with real `Future` objects, and tasks, maps, and channels can be awaited directly in asyncio without polling threads. Parallel random numbers are reproducible for any worker count, and a task can map over its own pool without deadlock.
