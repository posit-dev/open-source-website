---
color: '#1b66f8'
description: Lock-free shared memory IPC at thread speed in C11
github: shikokuchuo/libmizu
image: logo.svg
languages:
- C
people:
- Charlie Gao
title: libmizu
website: https://shikokuchuo.net/libmizu/

external:  # updated automatically, do not edit
  description: Lock-free shared memory IPC at thread speed in C11
  first_commit: '2026-08-21T09:24:37+00:00'
  forks: 0
  languages:
  - C
  last_updated: '2026-11-02T14:09:54.105049+00:00'
  license: MIT
  people:
  - Charlie Gao
  readme_image: https://raw.githubusercontent.com/shikokuchuo/libmizu/main/docs/assets/logo.svg
  repo: shikokuchuo/libmizu
  stars: 5
  title: libmizu
  website: https://shikokuchuo.net/libmizu/
---

libmizu is a C11 library for lock-free shared-memory IPC between processes. It is built for runtimes that parallelize with processes rather than threads, cutting a message round trip from tens of microseconds over sockets to under 1 µs so that work can be divided as finely as it would be with threads.

Channels and work-stealing task pools run over POSIX shared memory on Linux and macOS or Win32 file mappings on Windows, using lock-free single-producer single-consumer rings with batched publication and spin-then-park waiting that stays out of the kernel on the hot path. Peer death is detected by OS notification and confirmed by a kernel-released lock, with no heartbeats or polling, and crash-atomic claims mean a dead peer never leaves a queue stuck. All bindings share one wire format, so processes in different languages can exchange data over the same channel — the first-party bindings are mizu for R and pymizu for Python.
