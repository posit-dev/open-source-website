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

external:  # updated automatically, do not edit
  description: Model Context Protocol For R
  first_commit: '2025-03-26T21:10:12+00:00'
  forks: 13
  languages:
  - R
  last_updated: '2026-02-24T09:25:58.059616+00:00'
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
  stars: 156
  title: mcptools
  website: https://posit-dev.github.io/mcptools/
---

mcptools implements the Model Context Protocol (MCP) in R, enabling bidirectional integration between R and MCP-enabled AI tools. It allows R to function as both an MCP server (letting AI assistants like Claude Desktop, Claude Code, and VS Code Copilot run R code in your active R sessions) and as an MCP client (connecting third-party MCP servers to R-based chat applications).

The package solves the problem of AI assistants being unable to access or interact with your live R sessions and data. When used as a server, it enables models to run R code directly in your working sessions to answer questions about your data and environment. When used as a client, it integrates external tools (like GitHub, Confluence, or Google Drive) into R chat applications through the ellmer package, providing additional context for AI-powered workflows.
