---
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
title: ellmer
website: https://ellmer.tidyverse.org/

external:
  contributors:
  - hadley
  - gadenbuie
  - jcheng5
  - atheriel
  - lindbrook
  - howardbaik
  - simonpcouch
  - shikokuchuo
  - cpsievert
  - DavisVaughan
  - maciekbanas
  - michaelgrund
  - adisarid
  - SokolovAnatoliy
  - schloerke
  - bgreenwell
  - D-M4rk
  - elnelson575
  - etiennebacher
  - flaviaerius
  - gavinsimpson
  - hfrick
  - cortinah
  - jsowder
  - JamesHWade
  - netique
  - jeroenjanssens
  - jtrecenti
  - kbenoit
  - walkerke
  - maurolepore
  - thisisnic
  - pedrobtz
  - AdaemmerP
  - rplsmn
  - robert-norberg
  - hafen
  - ryjohnson09
  - salim-b
  - stephhazlitt
  - stevegbrooks
  - t-kalinowski
  - benyake
  - billsanto
  - cherylisabella
  - dcomputing
  - frankiethull
  - naltmann
  - xx02al
  description: Call LLM APIs from R
  first_commit: '2024-08-27T21:55:59+00:00'
  forks: 119
  languages:
  - R
  last_updated: '2026-02-13T14:17:09.022980+00:00'
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
  stars: 581
  title: ellmer
  website: https://ellmer.tidyverse.org/
---

ellmer provides a unified interface for working with large language models directly from R, making it easy to integrate AI capabilities into your data science workflows. Whether you need to generate code, analyze text, extract structured data, or build interactive applications, ellmer connects you to over 20 LLM providers including Claude, OpenAI, Google Gemini, Groq, and Mistral. The package handles the complexity of different provider APIs while giving you the flexibility to choose the right model for your needs—from cost-effective options for experimentation to high-performing models for production work.

Key features include streaming outputs for real-time interaction, tool calling for extending model capabilities, image analysis support, and intelligent credential management that works seamlessly with cloud authentication systems. For teams working in enterprise environments, ellmer supports routing through Azure, AWS, or Databricks to meet organizational policies, while individual developers can run models locally using Ollama for complete privacy. The package's stateful chat objects maintain conversation context across interactions, enabling sophisticated multi-turn dialogues that remember previous exchanges and build on prior results.
