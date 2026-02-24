---
description: A complete toolkit for connecting R and LLMs
github: posit-dev/btw
image: logo.png
languages:
- R
latest_release: '2025-12-23T13:00:45+00:00'
people:
- Garrick Aden-Buie
- Simon Couch
- Charlie Gao
title: btw
website: https://posit-dev.github.io/btw/

external:  # updated automatically, do not edit
  description: A complete toolkit for connecting R and LLMs
  first_commit: '2025-02-06T23:25:06+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-02-24T09:25:57.961613+00:00'
  latest_release: '2025-12-23T13:00:45+00:00'
  license: NOASSERTION
  people:
  - Garrick Aden-Buie
  - Simon Couch
  - Charlie Gao
  readme_image: man/figures/logo.png
  repo: posit-dev/btw
  stars: 110
  title: btw
  website: https://posit-dev.github.io/btw/
---

btw is a toolkit for connecting R with Large Language Models (LLMs) across different workflows. It helps R users provide context about their environment—data structures, packages, and documentation—to AI assistants, whether pasting into ChatGPT, chatting in an IDE, or building LLM-powered applications.

The package offers three main capabilities: a `btw()` function that gathers R session context and copies it to your clipboard for external LLMs, an interactive chat interface (`btw_app()`) that runs directly in your IDE with access to your R environment, and tools for building custom LLM applications through integration with the ellmer package or the Model Context Protocol. It solves the problem of LLMs lacking context about your R session by providing flexible tools to share environment data, documentation, and files with AI assistants.
