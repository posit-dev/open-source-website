---
color: '#447099'
description: Install R packages from GitHub, GitLab, Bitbucket, git, svn repositories,
  URLs
github: r-lib/remotes
image: logo.svg
languages:
- R
latest_release: '2024-03-17T12:41:28+00:00'
people:
- Gábor Csárdi
- Jenny Bryan
- Christophe Dervieux
- Hannah Frick
- Lionel Henry
- Hadley Wickham
- Jeroen Ooms
title: remotes
topics:
- Best Practices
website: https://remotes.r-lib.org/

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: Install R packages from GitHub, GitLab, Bitbucket, git, svn repositories,
    URLs
  first_commit: '2016-01-02T10:24:31+00:00'
  forks: 157
  languages:
  - R
  last_updated: '2026-05-20T08:05:55.253291+00:00'
  latest_release: '2024-03-17T12:41:28+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jenny Bryan
  - Christophe Dervieux
  - Hannah Frick
  - Lionel Henry
  - Hadley Wickham
  - Jeroen Janssens
  - Jeroen Ooms
  repo: r-lib/remotes
  stars: 357
  title: remotes
  website: https://remotes.r-lib.org/
---

The remotes package provides functions to install R packages from various remote and local sources, including GitHub, GitLab, Bitbucket, Bioconductor, git/SVN repositories, local directories, and URLs. It serves as a lightweight, standalone alternative to the installation functions previously found in the devtools package.

The package handles dependency resolution automatically, supports installing specific versions, branches, commits, tags, and pull requests, and requires no compiled code or external software for most operations. It recognizes and respects the `Remotes` field in DESCRIPTION files for specifying non-CRAN dependencies and can operate in standalone mode without relying on other R packages. The package supports both source and binary installations across different repository types while providing flexible configuration through R options and environment variables.
