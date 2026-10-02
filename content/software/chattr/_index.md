---
color: '#419599'
description: ''
github: mlverse/chattr
image: chattr.png
languages:
- R
latest_release: '2025-08-18T17:15:54+00:00'
people:
- Edgar Ruiz
- Hadley Wickham
title: chattr
website: https://mlverse.github.io/chattr/

external:  # updated automatically, do not edit
  description: ''
  first_commit: '2023-03-22T14:58:30+00:00'
  forks: 26
  languages:
  - R
  last_updated: '2026-09-18T14:19:16.010919+00:00'
  latest_release: '2025-08-18T17:15:54+00:00'
  license: NOASSERTION
  people:
  - Edgar Ruiz
  - Hadley Wickham
  readme_image: https://www.r-pkg.org/badges/version/chattr
  repo: mlverse/chattr
  stars: 249
  title: chattr
  website: https://mlverse.github.io/chattr/
---

`chattr` is an R package that provides an interface to large language models (LLMs) directly from RStudio and Positron. It lets you send prompts to an LLM from your script or through a built-in Shiny Gadget app, with a focus on assisting exploratory data analysis tasks.

The package connects to a wide range of LLM providers — including OpenAI, Anthropic, Databricks, Ollama, and many others — through the `ellmer` package. It automatically enriches your prompts with context about your current R environment, such as data frame structures and working directory file paths, which helps the model produce responses that follow recommended R best practices. Code returned by the LLM can be copied to your clipboard, pasted into your current script, or opened in a new script, all from within the chat interface.
