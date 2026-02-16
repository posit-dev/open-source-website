---
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

external:
  contributors:
  - glin
  - gaborcsardi
  - jonyoder
  - pat-s
  - colearendt
  - michaelmayer2
  - schloerke
  - pepijn-devries
  - eyk801
  - jeroen
  - tylfin
  - thomasp85
  - jimhester
  - dependabot[bot]
  - r-ash
  - raphaelbetschart
  - rdinnager
  - Aariq
  - edavidaja
  - bogdanoancea
  - stupidpupil
  - theAeon
  - aja08379
  - dfalbel
  - louisaslett
  - mikemahoney218
  - rtobar
  - salim-b
  - caiohamamura
  - mns-nordicals
  - snyk-bot
  description: System requirements for R packages
  first_commit: '2019-02-11T21:01:15+00:00'
  forks: 31
  languages:
  - Shell
  last_updated: '2026-02-13T14:17:03.942359+00:00'
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

r-system-requirements is a comprehensive catalog that automatically identifies and resolves system-level dependencies for R packages across multiple Linux distributions and Windows. Instead of manually figuring out which system libraries your R packages need, this tool uses intelligent pattern-matching rules to scan the SystemRequirements field in package metadata and translate those informal descriptions into platform-specific installation commands. This eliminates the frustration of cryptic installation errors caused by missing system dependencies, making it easier to set up reproducible R environments.

The catalog supports a wide range of platforms including Ubuntu, CentOS, Rocky Linux, RHEL, openSUSE, SUSE Linux Enterprise, Debian, Fedora, and Windows, with distribution-appropriate package manager commands for each. It powers tools like Posit Package Manager and integrates with the pak R package for automated dependency resolution. Whether you're deploying R applications in production, setting up development environments, or managing container images, r-system-requirements provides the foundation for smooth, reliable package installations without the manual detective work of identifying missing system libraries.
