---
description: 'renv: Project environments for R.'
github: rstudio/renv
image: logo.svg
languages:
- R
latest_release: '2025-07-24T22:49:27+00:00'
people:
- Hadley Wickham
- Christophe Dervieux
- JJ Allaire
- Jenny Bryan
- Garrick Aden-Buie
- Neal Richardson
title: renv
website: https://rstudio.github.io/renv/

external:
  contributors:
  - kevinushey
  - hadley
  - cderv
  - aronatkins
  - jrdnbradford
  - salim-b
  - jjallaire
  - jennybc
  - krlmlr
  - edavidaja
  - toph-allen
  - fh-mthomson
  - fkohrt
  - gadenbuie
  - zkamvar
  - remlapmot
  - ratnanil
  - mcanouil
  - klmr
  - khughitt
  - JosiahParry
  - jonkeane
  - blairj09
  - Felixmil
  - vandenman
  - cstepper
  - kiwiroy
  - robbfitzsimmons
  - StatsRhian
  - randy3k
  - NikNakk
  - njtierney
  - nealrichardson
  - MiguelRodo
  - mthomas-ketchbrook
  - mkuehn10
  - strazto
  - r-suzuki
  - swt30
  - beansrowning
  - zeehio
  - shannonpileggi
  - uribo
  - wenjie2wang
  - shrektan
  - alasdair-breasley
  - arbelt
  - bartekch
  - Shitao5
  - galachad
  - adamrobinson361
  - Ahschreyer
  - alex-wenzel
  - ateucher
  - drmowinckels
  - cokelly
  - collinberke
  - damonbayer
  - dbast
  - benkeser
  - DivadNojnarg
  - fdetsch
  - guslipkin
  - HenningLorenzen-ext-bayer
  - HenrikBengtsson
  - Bisaloo
  - jfunction
  - jimhester
  - JorisGoosen
  - Jollywatt
  - marcosnav
  - mtheiss
  description: 'renv: Project environments for R.'
  first_commit: '2018-11-28T20:25:39+00:00'
  forks: 163
  languages:
  - R
  last_updated: '2026-02-13T14:17:03.751275+00:00'
  latest_release: '2025-07-24T22:49:27+00:00'
  license: MIT
  people:
  - Hadley Wickham
  - Christophe Dervieux
  - JJ Allaire
  - Jenny Bryan
  - Garrick Aden-Buie
  - Neal Richardson
  readme_image: man/figures/logo.svg
  repo: rstudio/renv
  stars: 1131
  title: renv
  website: https://rstudio.github.io/renv/
---

renv is an R package designed to create reproducible environments for your projects by managing package dependencies with precision and isolation. Every R project using renv maintains its own private library of packages, ensuring that updates or changes in one project never affect another. By capturing exact package versions in a lockfile, renv guarantees that your code runs identically across different computers, team members, and deployment environments, solving one of the most persistent challenges in collaborative data science work.

What makes renv essential for data scientists and developers is its elegant workflow that fits naturally into existing R development practices. Initialize a project with renv, develop using standard R package installation functions, and periodically snapshot your dependencies to record their versions. When sharing your work or setting up on a new machine, renv automatically installs the exact package versions your project needs, eliminating the friction of dependency conflicts and "works on my machine" problems. Whether you're collaborating on long-term research projects, deploying production analytics, or simply want to ensure your analyses remain reproducible years into the future, renv provides the foundation for reliable, portable R environments.
