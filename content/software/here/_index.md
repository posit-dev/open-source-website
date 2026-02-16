---
description: A simpler way to find your files
github: r-lib/here
languages:
- R
latest_release: '2025-09-14T18:48:48+00:00'
people:
- Jenny Bryan
title: here
website: https://here.r-lib.org/

external:
  contributors:
  - krlmlr
  - github-actions[bot]
  - IndrajeetPatil
  - batpigandme
  - wael-sadek
  - web-flow
  - Bisaloo
  - jack-davison
  - jennybc
  - maelle
  - Masterxilo
  - rajanand
  - sharlagelfand
  - aviator-app[bot]
  - nzgwynn
  - t-gummer
  description: A simpler way to find your files
  first_commit: '2016-07-19T14:47:19+00:00'
  forks: 46
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.071028+00:00'
  latest_release: '2025-09-14T18:48:48+00:00'
  license: NOASSERTION
  people:
  - Jenny Bryan
  repo: r-lib/here
  stars: 431
  title: here
  website: https://here.r-lib.org/
---

The here package solves one of the most common pain points in R development: managing file paths across different project structures and team environments. Instead of relying on fragile approaches like `setwd()` that break when files are moved or shared, here automatically detects your project's root directory and builds reliable, portable paths from that anchor point. With intuitive syntax like `here("data", "analysis.csv")`, you can reference files consistently regardless of where your script lives within the project, making your code work seamlessly whether it's in the top-level directory or nested several folders deep.

This project-oriented approach delivers substantial benefits for data scientists and analysts working in complex repositories. Your paths remain valid when collaborating with teammates who have different directory structures, when reorganizing your project layout, or when running scripts from different locations. By eliminating context-dependent path failures, here enhances reproducibility and maintainability, letting you focus on analysis rather than wrestling with file system navigation.
