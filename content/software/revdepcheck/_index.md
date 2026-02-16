---
description: R package reverse dependency checking
github: r-lib/revdepcheck
languages:
- R
people:
- Gábor Csárdi
- Hadley Wickham
- Jenny Bryan
- Lionel Henry
- Davis Vaughan
- Christophe Dervieux
title: revdepcheck
website: https://revdepcheck.r-lib.org

external:
  contributors:
  - gaborcsardi
  - hadley
  - jimhester
  - krlmlr
  - jennybc
  - ateucher
  - lionel-
  - maksymiuks
  - HenrikBengtsson
  - DavisVaughan
  - romainfrancois
  - cderv
  - adamhsparks
  - fmichonneau
  - warnes
  - llrs
  - lbergelson
  - bertcarnell
  - stevenolen
  - vspinu
  description: R package reverse dependency checking
  first_commit: '2016-08-06T20:40:42+00:00'
  forks: 33
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.087436+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Hadley Wickham
  - Jenny Bryan
  - Lionel Henry
  - Davis Vaughan
  - Christophe Dervieux
  repo: r-lib/revdepcheck
  stars: 103
  title: revdepcheck
  website: https://revdepcheck.r-lib.org
---

revdepcheck is an essential R package for maintainers who need to ensure their package updates don't break downstream dependencies. When you're preparing to release a new version of your package, revdepcheck automates the critical but time-consuming task of testing all reverse dependencies—the packages that depend on yours. It runs comparative checks using both the CRAN and development versions of your package, highlighting exactly what changed so you can identify and address breaking changes before they affect the broader R community.

What makes revdepcheck particularly powerful for package developers is its intelligent workflow designed for real-world development scenarios. The tool leverages parallel processing and smart caching to speed up testing, automatically resumes interrupted runs, and provides clear status indicators so you can prioritize which package failures need investigation. An elegant progress bar keeps you informed while checks run in the background, and you can use separate R processes to monitor status or investigate specific failures in real time. Whether you maintain a widely-used package with hundreds of reverse dependencies or are preparing your first CRAN release, revdepcheck streamlines the testing workflow and gives you confidence that your updates won't introduce unexpected breaking changes.
