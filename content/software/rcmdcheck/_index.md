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

external:
  contributors:
  - gaborcsardi
  - hadley
  - jimhester
  - ateucher
  - pawelru
  - kevinushey
  - dpprdan
  - krlmlr
  - jennybc
  - fweber144
  - jeroenjanssens
  - lionel-
  - m-muecke
  - MichaelChirico
  - rorynolan
  - salim-b
  - tdhock
  - pat-s
  - tappek
  description: Run R CMD check from R and collect the results
  first_commit: '2016-02-25T12:45:25+00:00'
  forks: 34
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.004594+00:00'
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
  stars: 121
  title: rcmdcheck
  website: https://rcmdcheck.r-lib.org
---

The rcmdcheck package streamlines quality assurance for R package developers by enabling programmatic execution of R CMD check directly from within R. Instead of running checks manually from the command line, rcmdcheck allows you to automate package validation, capture structured results, and integrate quality checks seamlessly into your development workflow. This is especially valuable for continuous integration pipelines, automated testing, and maintaining high-quality R packages at scale.

With rcmdcheck, you can run comprehensive package checks on local source packages or .tar.gz files, receiving organized results with errors, warnings, and notes neatly categorized for easy analysis. The package also provides powerful features for comparing check results across different versions, retrieving and parsing CRAN check results across all testing platforms, and executing checks as background processes for concurrent testing. Whether you're developing a single package or maintaining a suite of R tools, rcmdcheck simplifies the quality assurance process and helps you catch issues before they reach users.
