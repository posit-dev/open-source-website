---
description: Serverless R message queue using SQLite
github: r-lib/liteq
languages:
- R
people:
- Gábor Csárdi
title: liteq
website: ''

external:
  contributors:
  - gaborcsardi
  - Enchufa2
  - wlandau
  - eddelbuettel
  - krlmlr
  - rentrop
  - wlandau-lilly
  description: Serverless R message queue using SQLite
  first_commit: '2017-01-07T22:29:26+00:00'
  forks: 9
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.287025+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  repo: r-lib/liteq
  stars: 57
  title: liteq
  website: ''
---

liteq is a lightweight, serverless message queue system for R that uses SQLite as its backend. Perfect for coordinating parallel workflows and managing asynchronous tasks, liteq provides a portable alternative to heavyweight message brokers like RabbitMQ or Redis. Since it requires only SQLite, you can use it anywhere R runs without setting up external infrastructure or managing additional services.

The package excels at building resilient data processing pipelines. It automatically detects crashed workers and returns unacknowledged messages to the queue, ensuring no work is lost when processes fail unexpectedly. With support for multiple databases and queues, race-condition-safe operations, and flexible message handling, liteq makes it straightforward to build robust job processing systems for everything from batch data transformations to distributed computing workflows.
