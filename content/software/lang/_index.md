---
description: Uses LLMs to translate R help docs on the fly
github: mlverse/lang
languages:
- R
latest_release: '2026-06-11T13:27:18+00:00'
people:
- Edgar Ruiz
title: lang
website: https://mlverse.github.io/lang/
external:
  description: Uses LLMs to translate R help docs on the fly
  first_commit: '2024-11-14T20:00:01+00:00'
  forks: 4
  languages:
  - R
  last_updated: '2026-09-18T14:19:34.465377+00:00'
  latest_release: '2026-06-11T13:27:18+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  readme_image: man/figures/logo.png
  repo: mlverse/lang
  stars: 32
  title: lang
  website: https://mlverse.github.io/lang/
image: logo.png
color: "#34476C"
---

lang is an R package that uses a large language model to translate R function help pages into other languages on the fly. It overrides the `?` and `help()` functions so that translated documentation appears directly in the Help pane of RStudio or Positron.

The package supports both cloud LLMs via ellmer (e.g., OpenAI's GPT-4o) and local models through Ollama, and it automatically detects the target language from your locale environment variables. Translations are cached within a session to avoid redundant API calls, and the cache location can be fixed to persist across sessions. To handle translation quality, lang summarizes the full help page first and uses that summary as context when translating individual sections, which helps the LLM produce more consistent results.
