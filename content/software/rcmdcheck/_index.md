---
description: Run R CMD check from R and collect the results
github: r-lib/rcmdcheck
image: rcmdcheck.svg
languages:
- R
latest_release: '2021-09-23T11:00:56+00:00'
people:
- Gábor Csárdi
- Hadley Wickham
- Jenny Bryan
- Jeroen Janssens
- Lionel Henry
title: rcmdcheck
website: https://rcmdcheck.r-lib.org

external:  # updated automatically, do not edit
  description: Run R CMD check from R and collect the results
  first_commit: '2016-02-25T12:45:25+00:00'
  forks: 34
  languages:
  - R
  last_updated: '2026-02-24T09:26:34.663599+00:00'
  latest_release: '2021-09-23T11:00:56+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jenny Bryan
  - Jeroen Janssens
  - Lionel Henry
  readme_image: https://cdn.jsdelivr.net/gh/r-lib/rcmdcheck@main/tools/rcmdcheck.svg
  repo: r-lib/rcmdcheck
  stars: 122
  title: rcmdcheck
  website: https://rcmdcheck.r-lib.org
---

rcmdcheck provides programmatic access to R's package checking system by running `R CMD check` from within R and capturing the results. It works on package folders or `.tar.gz` files and returns structured output with errors, warnings, and notes as separate character vectors.

The package enables automated quality checks in CI/CD pipelines and supports background processes for running multiple checks concurrently. It includes functions for parsing check output from files or URLs, accessing CRAN check results across platforms, and comparing check results between different versions or against CRAN. The structured output makes it straightforward to integrate package validation into automated workflows.
