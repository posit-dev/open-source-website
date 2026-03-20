---
color: '#E14825'
description: Call LLM APIs from R
github: tidyverse/ellmer
image: logo.png
languages:
- R
latest_release: '2025-11-14T20:30:45+00:00'
people:
- Hadley Wickham
- Garrick Aden-Buie
- Joe Cheng
- Simon Couch
- Charlie Gao
- Carson Sievert
- Davis Vaughan
- Barret Schloerke
- Liz Nelson
- Hannah Frick
- Jeroen Janssens
- Tomasz Kalinowski
tags:
- AI
title: ellmer
website: https://ellmer.tidyverse.org/

external:  # updated automatically, do not edit
  description: Call LLM APIs from R
  first_commit: '2024-08-27T21:55:59+00:00'
  forks: 124
  languages:
  - R
  last_updated: '2026-03-20T10:27:41.346436+00:00'
  latest_release: '2025-11-14T20:30:45+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Garrick Aden-Buie
  - Joe Cheng
  - Simon Couch
  - Charlie Gao
  - Carson Sievert
  - Davis Vaughan
  - Barret Schloerke
  - Liz Nelson
  - Hannah Frick
  - Jeroen Janssens
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: tidyverse/ellmer
  stars: 587
  title: ellmer
  website: https://ellmer.tidyverse.org/
---

ellmer is an R package for working with large language models from multiple providers including OpenAI, Anthropic, Google, AWS, Azure, and many others. It provides a unified interface for chat-based interactions with LLMs, supporting streaming outputs, tool calling, and structured data extraction.

The package uses stateful R6 objects that maintain conversation context across multiple queries, making it straightforward to build interactive chat applications or programmatic workflows. It handles authentication automatically for major cloud providers and offers flexible interaction modes—from interactive console chat sessions to capturing responses as strings for downstream processing. Key features include support for multimodal inputs (text and images), control over streaming behavior, and integration with other Posit LLM tools for RAG, evaluation, and chatbot interfaces.
