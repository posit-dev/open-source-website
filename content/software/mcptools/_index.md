---
description: Model Context Protocol For R
github: posit-dev/mcptools
image: logo.png
languages:
- R
latest_release: '2025-10-29T20:23:51+00:00'
people:
- Simon Couch
- Charlie Gao
- Winston Chang
- Garrick Aden-Buie
- Hannah Frick
- Tomasz Kalinowski
title: mcptools
website: https://posit-dev.github.io/mcptools/

external:
  contributors:
  - simonpcouch
  - shikokuchuo
  - wch
  - galachad
  - gadenbuie
  - hfrick
  - t-kalinowski
  description: Model Context Protocol For R
  first_commit: '2025-03-26T21:10:12+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-13T14:16:46.467671+00:00'
  latest_release: '2025-10-29T20:23:51+00:00'
  license: NOASSERTION
  people:
  - Simon Couch
  - Charlie Gao
  - Winston Chang
  - Garrick Aden-Buie
  - Hannah Frick
  - Tomasz Kalinowski
  readme_image: man/figures/logo.png
  repo: posit-dev/mcptools
  stars: 153
  title: mcptools
  website: https://posit-dev.github.io/mcptools/
---

mcptools brings the Model Context Protocol to R, enabling seamless bidirectional communication between AI assistants and R environments. This powerful integration allows AI tools like Claude Desktop and VS Code Copilot to execute R code, access data in active R sessions, and leverage package documentation without requiring direct access to your environment. Whether you're exploring data interactively with AI assistance or building context-aware applications, mcptools serves as the bridge that makes intelligent collaboration possible.

As both an MCP server and client, mcptools offers flexible workflows for data scientists and developers. When functioning as a server, it integrates with the btw package to provide AI assistants with rich context about your R session, including object inspection and metadata retrieval. As a client, mcptools connects your R applications to third-party MCP services like GitHub, Confluence, and Google Drive, enabling you to build AI-enhanced tools with shinychat and querychat. By automating tool discovery and routing requests between R and AI models, mcptools opens up new possibilities for interactive data science and intelligent application development.
