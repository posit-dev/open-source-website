---
description: Static Code Analysis for R
github: r-lib/lintr
image: logo.png
languages:
- R
latest_release: '2025-11-27T15:14:26+00:00'
people:
- Gábor Csárdi
- Barret Schloerke
- Jenny Bryan
- Hadley Wickham
- Hannah Frick
- JJ Allaire
title: lintr
website: https://lintr.r-lib.org

external:
  contributors:
  - MichaelChirico
  - jimhester
  - AshesITR
  - IndrajeetPatil
  - fangly
  - renkun-ken
  - russHyde
  - Bisaloo
  - dependabot[bot]
  - dragosmg
  - gaborcsardi
  - saurfang
  - michaelquinn32
  - MEO265
  - mcol
  - schloerke
  - salim-b
  - jrnold
  - krlmlr
  - jennybc
  - olivroy
  - huisman
  - jonkeane
  - JhossePaul
  - etiennebacher
  - eitsupi
  - LaurentGatto
  - kpagacz
  - fabian-s
  - F-Noelle
  - emmanuel-ferdman
  - dpprdan
  - f-ritter
  - yu-iskw
  - infotroph
  - bfgray3
  - dmurdoch
  - mwaldstein
  - maelle
  - klmr
  - jabranham
  - ashbaldry
  - dankessler
  - dchiu911
  - karawoo
  - Enchufa2
  - hadley
  - gdequeiroz
  - batpigandme
  - mschilli87
  - lschneiderbauer
  - prosoitos
  - alessandro-gentilini
  - markromanmiller
  - mattyb
  - thisisnic
  - nicholas-masel
  - pdil
  - paulkaefer
  - paulstaab
  - randy3k
  - shaopeng-gh
  - StefanBRas
  - marberts
  - stufield
  - gitter-badger
  - TimTaylor
  - tonyk7440
  - wesleyburr
  - wlandau
  - arekbee
  - bahadzie
  - clerousset
  - jeffwong-nflx
  - jmaspons
  - ttriche
  - ax42
  - andrewychoi
  - andyquinterom
  - 1beb
  - cdiener
  - rundel
  - danielinteractive
  - dave-lovell
  - ellisvalentiner
  - fdlk
  - fkohrt
  - FvD
  - frederic-mahe
  - Guillawme
  - hfrick
  - ha0ye
  - hedsnz
  - HenningLorenzen-ext-bayer
  - yutannihilation
  - jjallaire
  - jcken95
  - bairdj
  - jamieRowen
  - jmwerner
  - jonthegeek
  - joshkgold
  - Arcanemagus
  - leogama
  description: Static Code Analysis for R
  first_commit: '2014-09-28T02:48:15+00:00'
  forks: 196
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.687937+00:00'
  latest_release: '2025-11-27T15:14:26+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Barret Schloerke
  - Jenny Bryan
  - Hadley Wickham
  - Hannah Frick
  - JJ Allaire
  readme_image: man/figures/logo.png
  repo: r-lib/lintr
  stars: 1270
  title: lintr
  website: https://lintr.r-lib.org
---

lintr is an essential static code analysis tool that helps R developers maintain high code quality by automatically checking for style adherence, syntax errors, and potential semantic issues. Acting as a vigilant code reviewer, lintr analyzes your R scripts and packages to identify problems that need attention, from inconsistent formatting to problematic coding patterns. It supports multiple coding standards including the tidyverse style guide and integrates seamlessly with GitHub Actions for continuous integration, making it invaluable for teams maintaining shared codebases.

What makes lintr particularly powerful is its flexibility and extensive customization options. With over 100 built-in linters covering everything from function naming conventions to whitespace usage, you can configure lintr to enforce the exact standards your project requires through simple configuration files. The tool works alongside the styler package in a complementary way: while styler automatically reformats code, lintr focuses on detection and analysis, helping you understand code quality issues before taking corrective action. Whether you're working on individual scripts with lint_dir() or entire R packages with lint_package(), lintr provides the automated code review that helps catch problems early and maintain consistent, readable code across your data science projects.
