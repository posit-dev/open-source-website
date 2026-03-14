---
color: '#D44000'
description: HTML widget to visually compare files
github: r-lib/diffviewer
image: logo.svg
languages:
- JavaScript
latest_release: '2024-06-12T16:12:44+00:00'
people:
- Hadley Wickham
- Winston Chang
title: diffviewer
website: http://diffviewer.r-lib.org

external:  # updated automatically, do not edit
  description: HTML widget to visually compare files
  first_commit: '2020-07-26T13:18:02+00:00'
  forks: 7
  languages:
  - JavaScript
  last_updated: '2026-03-05T16:29:28.655634+00:00'
  latest_release: '2024-06-12T16:12:44+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  repo: r-lib/diffviewer
  stars: 66
  title: diffviewer
  website: http://diffviewer.r-lib.org
---

diffviewer provides an HTML widget for visually comparing files in R. It wraps three JavaScript libraries to handle different file types: resemble.js for images, daff.js for data frames, and jsdiff for text files.

The package extracts common comparison UI functionality from shinytest and vdiffr, making it useful for testing and validation workflows. It provides a unified interface for visual diff operations across different data types. The widget displays differences in an interactive HTML format that's easy to inspect and understand.
