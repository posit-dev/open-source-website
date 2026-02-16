---
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

external:
  contributors:
  - gaborcsardi
  - jeroenjanssens
  description: Open System Files, URLs, Anything
  first_commit: '2018-09-10T08:11:47+00:00'
  forks: 3
  languages:
  - Shell
  last_updated: '2026-02-13T14:17:19.846710+00:00'
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

xopen provides a unified interface for opening files, directories, and URLs across different operating systems. Rather than writing platform-specific code using `shell.exec()` on Windows, `open` on macOS, or `xdg-open` on Linux, xopen lets you use a single R function that works consistently everywhere. It automatically launches resources with their associated default applications, making it simple to open files in their native editors, launch URLs in web browsers, or trigger any system-registered application.

The package is particularly valuable when building cross-platform R scripts and packages that need to interact with the user's desktop environment. You can open help documentation in a browser, launch data files in Excel or another spreadsheet application, or even specify which particular program should handle a resource. xopen also supports passing command-line arguments to applications, giving you fine-grained control over how resources are opened while maintaining the simplicity and portability that makes your code work seamlessly across all major operating systems.
