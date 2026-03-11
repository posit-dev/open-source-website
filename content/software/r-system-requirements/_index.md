---
image: logo.svg
color: "#EE6331"
description: System requirements for R packages
github: rstudio/r-system-requirements
languages:
- Shell
people:
- Gábor Csárdi
- Barret Schloerke
- Jeroen Ooms
- Thomas Lin Pedersen
- Daniel Falbel
title: r-system-requirements
website: ''

external:  # updated automatically, do not edit
  description: System requirements for R packages
  first_commit: '2019-02-11T21:01:15+00:00'
  forks: 32
  languages:
  - Shell
  last_updated: '2026-03-05T16:14:27.655449+00:00'
  license: MIT
  people:
  - Gábor Csárdi
  - Barret Schloerke
  - Jeroen Ooms
  - Thomas Lin Pedersen
  - Daniel Falbel
  repo: rstudio/r-system-requirements
  stars: 136
  title: r-system-requirements
  website: ''
---

This repository provides a catalog of rules that automatically map the free-form `SystemRequirements` field in R package DESCRIPTION files to specific system installation commands for different Linux distributions. It solves the problem of translating vague requirements like "libcurl" into concrete commands like `apt install libcurl4-openssl-dev`.

The rules cover major Linux distributions including Ubuntu, Debian, CentOS, RHEL, Rocky Linux, openSUSE, and Fedora. Rather than maintaining a massive table mapping every R package to its dependencies, this approach uses regular expressions to pattern-match requirements and generate OS-specific installation commands. The catalog powers Posit Package Manager and is also used by the `pak` package to automatically install system dependencies when installing R packages.
