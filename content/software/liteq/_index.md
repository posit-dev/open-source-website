---
color: '#E7B10A'
description: Serverless R message queue using SQLite
github: r-lib/liteq
image: logo.svg
languages:
- R
people:
- Gábor Csárdi
title: liteq
website: ''

external:  # updated automatically, do not edit
  description: Serverless R message queue using SQLite
  first_commit: '2017-01-07T22:29:26+00:00'
  forks: 9
  languages:
  - R
  last_updated: '2026-03-20T10:27:53.312583+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  repo: r-lib/liteq
  stars: 57
  title: liteq
  website: ''
---

liteq is a lightweight message queue system for R that uses SQLite databases to store and manage job queues. It enables asynchronous task processing with support for multiple databases and multiple queues per database, requiring no separate server infrastructure.

The package provides automatic handling of crashed workers through SQLite's locking mechanism, which can detect when a worker process dies and automatically requeue or mark failed messages. Messages can be acknowledged (ack) when successfully processed or negatively acknowledged (nack) when processing fails, giving precise control over job state management. The SQLite-based implementation makes queues portable and persistent across R sessions while maintaining process safety through built-in locking.
