---
color: '#9A4665'
description: Higher Level API for torch
github: mlverse/luz
image: luz.png
languages:
- R
latest_release: '2026-04-28T10:41:56+00:00'
people:
- Daniel Falbel
title: luz
website: https://mlverse.github.io/luz/

external:  # updated automatically, do not edit
  description: Higher Level API for torch
  first_commit: '2021-04-23T20:32:24+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-09-18T14:18:39.415964+00:00'
  latest_release: '2026-04-28T10:41:56+00:00'
  license: NOASSERTION
  people:
  - Daniel Falbel
  repo: mlverse/luz
  stars: 101
  title: luz
  website: https://mlverse.github.io/luz/
---

Luz is a higher-level API for torch in R that reduces the verbosity of deep learning training loops. It lets you take a torch `nn_module` definition and fit it to a dataloader with a concise `setup() %>% fit()` interface, handling device placement, weight updates, progress tracking, and metrics automatically.

Luz draws on ideas from FastAI, Keras, PyTorch Lightning, and HuggingFace Accelerate. It provides a callbacks API for customizing training behavior and treats `luz_module` as a subclass of `nn_module`, so existing torch models work with minimal changes. It currently supports CPU and single-GPU training.
