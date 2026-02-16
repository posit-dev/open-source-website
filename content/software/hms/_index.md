---
description: A simple class for storing time-of-day values
github: tidyverse/hms
image: logo.png
languages:
- R
latest_release: '2025-10-16T19:10:13+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Jeroen Ooms
title: hms
website: https://hms.tidyverse.org/

external:
  contributors:
  - krlmlr
  - github-actions[bot]
  - IndrajeetPatil
  - batpigandme
  - qgeissmann
  - hadley
  - moodymudskipper
  - lionel-
  - DivadNojnarg
  - schochastics
  - hglanz
  - jeroen
  - jimhester
  - joethorley
  - romainfrancois
  - vspinu
  - eitsupi
  - evanhaldane
  description: A simple class for storing time-of-day values
  first_commit: '2016-03-31T09:05:58+00:00'
  forks: 29
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.654655+00:00'
  latest_release: '2025-10-16T19:10:13+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Jeroen Ooms
  readme_image: man/figures/logo.png
  repo: tidyverse/hms
  stars: 143
  title: hms
  website: https://hms.tidyverse.org/
---

hms is a lightweight R package that provides a simple yet robust class for storing and displaying time-of-day values in the familiar hh:mm:ss format. Built on R's difftime foundation, it stores times internally as seconds elapsed since midnight, making it ideal for seamless data exchange with databases and spreadsheets. The package supports flexible construction from hours, minutes, or seconds, and handles edge cases elegantly, including times that extend beyond 24 hours or negative durations, while maintaining precision up to microseconds.

What makes hms particularly valuable for data scientists is its seamless integration with data frames and compatibility with various time formats, including POSIXt objects. Whether you're importing time data from external sources, performing time-based calculations, or preparing datasets for analysis, hms eliminates common friction points in time representation. Its focused design ensures that time-of-day values are handled consistently and accurately throughout your data pipeline, letting you concentrate on analysis rather than wrestling with time format conversions.
