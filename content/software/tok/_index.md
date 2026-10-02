---
image: logo.svg
color: "#419599"
description: Tokenizers from HuggingFace
github: mlverse/tok
languages:
- R
latest_release: '2026-04-21T19:01:00+00:00'
people:
- Daniel Falbel
- Tomasz Kalinowski
title: tok
website: ''

external:  # updated automatically, do not edit
  description: Tokenizers from HuggingFace
  first_commit: '2023-04-20T20:25:27+00:00'
  forks: 2
  languages:
  - R
  last_updated: '2026-09-18T14:19:18.461686+00:00'
  latest_release: '2026-04-21T19:01:00+00:00'
  license: NOASSERTION
  people:
  - Daniel Falbel
  - Tomasz Kalinowski
  repo: mlverse/tok
  stars: 48
  title: tok
  website: ''
---

tok is an R package that provides bindings to the Hugging Face tokenizers library, letting you tokenize and detokenize text directly in R using the same Rust backend that powers the Python implementation.

The package can load pretrained tokenizers from JSON files or pull them directly from the Hugging Face Hub using `from_pretrained`. It supports encoding text into token IDs and decoding them back, making it useful for preparing inputs to transformer models. Because it relies on Rust via extendr rather than a pure-R implementation, it offers performance comparable to the Python tokenizers library.
