---
description: write YAML for R Markdown, bookdown, blogdown, and more
github: r-lib/ymlthis
languages:
- R
latest_release: '2022-08-04T13:16:24+00:00'
people:
- Carson Sievert
- Rich Iannone
title: ymlthis
website: https://ymlthis.r-lib.org/

external:
  contributors:
  - malcolmbarrett
  - cpsievert
  - rich-iannone
  - katrinleinweber
  - lquayle88
  description: write YAML for R Markdown, bookdown, blogdown, and more
  first_commit: '2019-06-03T20:45:14+00:00'
  forks: 10
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.110459+00:00'
  latest_release: '2022-08-04T13:16:24+00:00'
  license: NOASSERTION
  people:
  - Carson Sievert
  - Rich Iannone
  repo: r-lib/ymlthis
  stars: 168
  title: ymlthis
  website: https://ymlthis.r-lib.org/
---

ymlthis streamlines the creation of YAML front matter for R Markdown documents and related formats like bookdown and blogdown. Rather than manually writing YAML syntax with its strict indentation rules and easy-to-miss colons, ymlthis lets you build YAML configurations using intuitive R functions. The package provides a comprehensive set of yml_*() functions that cover everything from basic author and date information to complex configurations like output formats, bibliography management, and custom parameters. With its pipe-friendly design, you can chain together multiple YAML elements in a readable, discoverable way that integrates naturally with modern R workflows.

What makes ymlthis particularly valuable is how it reduces friction in the R Markdown ecosystem. The function-based approach means you can use R's built-in help system to explore available options, eliminating the need to memorize YAML syntax or constantly reference documentation. An integrated RStudio add-in provides a graphical interface for interactive YAML generation, while use_*() functions make it easy to write your configurations directly to files or copy them to your clipboard. Whether you're setting up a simple document or configuring complex bookdown projects with custom output formats and citations, ymlthis transforms YAML creation from a tedious technical detail into a smooth, error-free experience.
