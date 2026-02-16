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

external:
  contributors:
  - gadenbuie
  - simonpcouch
  - jeanchristophe13v
  - shikokuchuo
  - Copilot
  description: A complete toolkit for connecting R and LLMs
  first_commit: '2025-02-06T23:25:06+00:00'
  forks: 6
  languages:
  - R
  last_updated: '2026-02-13T14:16:46.387072+00:00'
  latest_release: '2025-12-23T13:00:45+00:00'
  license: NOASSERTION
  people:
  - Garrick Aden-Buie
  - Simon Couch
  - Charlie Gao
  readme_image: man/figures/logo.png
  repo: posit-dev/btw
  stars: 107
  title: btw
  website: https://posit-dev.github.io/btw/
---

btw is a comprehensive R package that bridges the gap between your R environment and Large Language Models. It addresses a fundamental challenge when working with AI assistants: LLMs need context about your data structures, packages, and relevant documentation to provide meaningful help. Rather than manually gathering and formatting this information, btw automates the entire process, making it effortless to get AI assistance that's actually useful for your specific R workflow.

The package supports three distinct workflows to fit different preferences and use cases. For quick interactions, the `btw()` function compiles relevant context from your R environment that you can paste directly into ChatGPT or Claude. If you prefer working within your IDE, `btw_app()` launches a built-in AI assistant that can explore your local environment and access documentation without leaving R. For developers building LLM-powered applications, functions like `btw_client()` and `btw_tools()` provide the building blocks to integrate AI capabilities into custom tools and connect with external coding agents via the Model Context Protocol.
