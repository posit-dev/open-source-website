---
description: Simulate installing and loading a package
github: r-lib/pkgload
languages:
- R
latest_release: '2025-09-23T10:17:36+00:00'
people:
- Hadley Wickham
- Winston Chang
- Lionel Henry
- Gábor Csárdi
- Jenny Bryan
- JJ Allaire
- Daniel Falbel
- Tomasz Kalinowski
- Charlie Gao
- Jeroen Janssens
title: pkgload
website: http://pkgload.r-lib.org

external:
  contributors:
  - hadley
  - wch
  - lionel-
  - jimhester
  - Geoff99
  - yoni
  - krlmlr
  - robertzk
  - yiufung
  - gaborcsardi
  - kohske
  - klmr
  - MichaelChirico
  - jennybc
  - HenrikBengtsson
  - jiho
  - bpbond
  - kevinushey
  - ncarchedi
  - TimTaylor
  - olivroy
  - pitakakariki
  - craigcitro
  - neshvig10
  - rmflight
  - karl-forner-quartz-bio
  - jjallaire
  - ethanplunkett
  - adrtod
  - dfalbel
  - mtkerbeR
  - philchalmers
  - riccardoporreca
  - richfitz
  - romainfrancois
  - sebffischer
  - shabbychef
  - kalibera
  - t-kalinowski
  - vspinu
  - heavywatal
  - yihui
  - jlburkhead
  - lev-kuznetsov
  - musvaage
  - tylermorganwall
  - AlexAxthelm
  - assaron
  - benmarwick
  - BrianDiggs
  - shikokuchuo
  - edwindj
  - imanuelcostigan
  - isteves
  - ashander
  - jrnold
  - jeroenjanssens
  - lorenzwalthert
  - lgaborini
  - malcolmbarrett
  - mcol
  - mdequeljoe
  - mgirlich
  description: Simulate installing and loading a package
  first_commit: '2016-11-07T21:45:48+00:00'
  forks: 53
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.187851+00:00'
  latest_release: '2025-09-23T10:17:36+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  - Lionel Henry
  - Gábor Csárdi
  - Jenny Bryan
  - JJ Allaire
  - Daniel Falbel
  - Tomasz Kalinowski
  - Charlie Gao
  - Jeroen Janssens
  repo: r-lib/pkgload
  stars: 59
  title: pkgload
  website: http://pkgload.r-lib.org
---

pkgload is an essential development tool for R package developers that simulates the process of installing and loading a package without performing the complete installation procedure. This dramatically speeds up the development workflow, allowing you to test changes and iterate on your package rapidly without the overhead of full reinstallation. Originally part of the popular devtools package, pkgload was extracted as a standalone tool during the restructuring of the devtools ecosystem to provide focused, efficient functionality.

Most developers interact with pkgload through the familiar `devtools::load_all()` function, which leverages pkgload's capabilities behind the scenes. By loading your package's code, data, and compiled components directly into your R session, pkgload enables you to experiment with modifications and immediately see results. This seamless integration makes package development more productive and enjoyable, eliminating the friction of constant reinstallation cycles while maintaining the reliability you need to build robust R packages.
