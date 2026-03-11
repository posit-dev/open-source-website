---
image: logo.svg
color: "#72994E"
description: Open System Files, URLs, Anything
github: r-lib/xopen
languages:
- Shell
latest_release: '2024-04-25T08:48:47+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: xopen
website: https://r-lib.github.io/xopen/

external:  # updated automatically, do not edit
  description: Open System Files, URLs, Anything
  first_commit: '2018-09-10T08:11:47+00:00'
  forks: 3
  languages:
  - Shell
  last_updated: '2026-03-05T16:28:15.174786+00:00'
  latest_release: '2024-04-25T08:48:47+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/xopen
  stars: 34
  title: xopen
  website: https://r-lib.github.io/xopen/
---

xopen is a cross-platform R package that opens files, directories, or URLs using their associated system applications. It works consistently across Windows, macOS, and Linux, similar to R's `shell.exec()` but with better platform support.

The package handles platform differences automatically, removing the need to write OS-specific code for opening external resources. You can open items with their default applications or specify a particular application to use. It also supports passing command-line arguments to applications, making it useful for launching programs with specific configurations or parameters.
