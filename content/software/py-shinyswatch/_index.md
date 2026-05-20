---
color: '#404041'
description: Bootswatch themes for py-shiny
github: posit-dev/py-shinyswatch
image: logo.svg
languages:
- Python
latest_release: '2026-03-20T20:44:16+00:00'
people:
- Barret Schloerke
- Garrick Aden-Buie
- Michael Chow
- Winston Chang
title: py-shinyswatch
topics:
- Best Practices
- Interactive Apps
- Visualization
website: https://posit-dev.github.io/py-shinyswatch/

external:  # updated automatically, do not edit
  description: Bootswatch themes for py-shiny
  first_commit: '2023-03-27T20:11:42+00:00'
  forks: 4
  languages:
  - Python
  last_updated: '2026-05-20T08:05:15.003150+00:00'
  latest_release: '2026-03-20T20:44:16+00:00'
  license: MIT
  people:
  - Barret Schloerke
  - Garrick Aden-Buie
  - Michael Chow
  - Winston Chang
  repo: posit-dev/py-shinyswatch
  stars: 37
  title: py-shinyswatch
  website: https://posit-dev.github.io/py-shinyswatch/
---

Shinyswatch provides Bootswatch + Bootstrap 5 themes for Python Shiny applications, offering 25 pre-built visual themes that can be applied to Shiny apps with a single line of code. Simply add a theme object (like `shinyswatch.theme.darkly`) to your app's UI definition to completely change its appearance.

The package includes a theme picker component for runtime theme switching, making it easy for users to customize app appearance without code changes. Each theme also exposes a `.colors` attribute that can be used to consistently style plots and other output elements to match the app's theme. This solves the problem of maintaining visual consistency across UI components and data visualizations.
