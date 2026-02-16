---
description: A Date-Time Library for R
github: r-lib/clock
image: logo.png
languages:
- R
latest_release: '2026-01-13T16:12:36+00:00'
people:
- Davis Vaughan
- Jenny Bryan
- Jeroen Janssens
- Lionel Henry
title: clock
website: https://clock.r-lib.org

external:
  contributors:
  - DavisVaughan
  - jennybc
  - jeroenjanssens
  - lionel-
  - martaalcalde
  - MichaelChirico
  - trevorld
  description: A Date-Time Library for R
  first_commit: '2020-10-26T19:27:27+00:00'
  forks: 7
  languages:
  - R
  last_updated: '2026-02-13T14:17:20.471902+00:00'
  latest_release: '2026-01-13T16:12:36+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Jenny Bryan
  - Jeroen Janssens
  - Lionel Henry
  readme_image: man/figures/logo.png
  repo: r-lib/clock
  stars: 110
  title: clock
  website: https://clock.r-lib.org
---

clock is a comprehensive date-time library for R that brings clarity and precision to temporal calculations. Built on Howard Hinnant's highly regarded C++ date library, clock provides a powerful toolkit for parsing, formatting, and manipulating dates and times. Unlike traditional approaches that force all temporal data into a single class, clock introduces four specialized types—durations, time points, zoned-times, and calendars—each designed for specific aspects of date-time work. This architecture allows you to work with time zones only when necessary, handle irregular periods like months and years with ease, and perform date arithmetic with confidence.

What makes clock particularly valuable for data scientists and R developers is its explicit handling of the complexities that often cause silent errors in date-time code. The package forces you to consciously address invalid dates and daylight saving time ambiguities, reducing the risk of subtle bugs in your analyses. Whether you're working with financial time series, scheduling data, or temporal experiments, clock offers both high-level functions for everyday tasks and low-level tools for advanced manipulations. Its dual API approach means you can leverage clock's capabilities with native R date classes while having access to more sophisticated features when your work demands them.
