---
color: '#143641'
description: Async and parallel R at thread speed over shared memory
github: shikokuchuo/mizu
image: logo.svg
languages:
- R
people:
- Charlie Gao
title: mizu
topics:
- Data Wrangling
- Interactive Apps
website: https://shikokuchuo.net/mizu/

external:  # updated automatically, do not edit
  description: Async and parallel R at thread speed over shared memory
  first_commit: '2026-08-21T09:26:17+00:00'
  forks: 0
  languages:
  - R
  last_updated: '2026-11-02T14:09:48.089169+00:00'
  license: NOASSERTION
  people:
  - Charlie Gao
  readme_image: man/figures/logo.svg
  repo: shikokuchuo/mizu
  stars: 23
  title: mizu
  website: https://shikokuchuo.net/mizu/
---

mizu is an R package for async and parallel computing that communicates over shared memory instead of sockets. A task round trip takes under a microsecond rather than around 100 µs, so work can be divided as finely as it would be across threads.

mizu is built on libmizu, a C library for lock-free shared-memory IPC, and pymizu binds the same core for Python, so pool workers can be Python processes and vectors, data frames, and Arrow tables cross between R and Python as zero-copy views. Messages stream into a `later` event loop without polling, and channels, tasks, and parallel maps plug into `promises` pipelines for use in Shiny. Parallel random numbers are reproducible for any worker count, and a task can map over its own pool without deadlock.
