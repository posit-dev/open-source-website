---
description: Tools to make an R developer's life easier
github: r-lib/devtools
image: logo.png
languages:
- R
latest_release: '2025-10-02T01:44:51+00:00'
people:
- Hadley Wickham
- Winston Chang
- Jenny Bryan
- Gábor Csárdi
- Jeroen Ooms
- Lionel Henry
- Thomas Lin Pedersen
- JJ Allaire
- Joe Cheng
- Julia Silge
- Jeroen Janssens
title: devtools
website: https://devtools.r-lib.org

external:
  contributors:
  - hadley
  - jimhester
  - wch
  - jennybc
  - rmflight
  - malcolmbarrett
  - krlmlr
  - kevinushey
  - gaborcsardi
  - lev-kuznetsov
  - kohske
  - Geoff99
  - jeroen
  - ashander
  - yoni
  - lionel-
  - robertzk
  - bpbond
  - ateucher
  - yihui
  - HenrikBengtsson
  - brentonk
  - hmalmedal
  - imanuelcostigan
  - jiho
  - ncarchedi
  - richfitz
  - craigcitro
  - klmr
  - jonthegeek
  - maelle
  - mbjones
  - karthik
  - fmichonneau
  - bquast
  - amcdavid
  - flying-sheep
  - philliplab
  - randy3k
  - rcannood
  - kiwiroy
  - AmundsenJunior
  - StevenMMortimer
  - stevensurgnier
  - tklebel
  - thomasp85
  - plantarum
  - hrbrmstr
  - nbenn
  - seankross
  - theGreatWhiteShark
  - BrianDiggs
  - renozao
  - karawoo
  - pavel-filatov
  - az0
  - daattali
  - adrtod
  - ianmcook
  - ijlyttle
  - jjallaire
  - jrnold
  - jimvine
  - jcheng5
  - jdblischak
  - muschellij2
  - jmcphers
  - juliangehring
  - karl-forner-quartz-bio
  - batpigandme
  - npjc
  - mnel
  - martinstuder
  - mcol
  - pranayaryal
  - rmsharp
  - ricardo-bion
  - romainfrancois
  - rorynolan
  - seaaan
  - uribo
  - shabbychef
  - yui-knk
  - philchalmers
  - peterdesmet
  - Paxanator
  - pkq
  - pbreheny
  - niranjv
  - nparley
  - ntdef
  - nfrerebeau
  - IndrajeetPatil
  - statwonk
  - orgadish
  - olivroy
  - musvaage
  - lindbrook
  - kiendang
  - jlburkhead
  - tappek
  - dmurdoch
  - catalamarti
  - bbolker
  - WilDoane
  - wibeasley
  - heavywatal
  - wleoncio
  - vspinu
  - twolodzko
  - kalibera
  - t-gibson
  - leeper
  - gitter-badger
  - Bisaloo
  - HughParsonage
  - hansharhoff
  - gavinsimpson
  - florisvdh
  - emilsjoerup
  - edwindj
  - eibanez
  - DillonHammill
  - dlebauer
  - djnavarro
  - ChrisMuir
  - infotroph
  - arcresu
  - brendan-r
  - billdenney
  - bborgesr
  - tonytonov
  - Anirban166
  - adamhsparks
  - mikldk
  - mikemahoney218
  - MichaelChirico
  - m-muecke
  - matthew-brett
  - mattmalin
  - wamserma
  - luisDVA
  - lbusett
  - lmullen
  - kornl
  - Kevin-Jin
  - katrinleinweber
  - juliasilge
  - jgabry
  - joesho112358
  - jeroenjanssens
  - jayhesselberth
  - jameslamb
  - james-atkins
  - moonboots
  description: Tools to make an R developer's life easier
  first_commit: '2010-05-03T04:08:49+00:00'
  forks: 761
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.421345+00:00'
  latest_release: '2025-10-02T01:44:51+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  - Jenny Bryan
  - Gábor Csárdi
  - Jeroen Ooms
  - Lionel Henry
  - Thomas Lin Pedersen
  - JJ Allaire
  - Joe Cheng
  - Julia Silge
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/devtools
  stars: 2495
  title: devtools
  website: https://devtools.r-lib.org
---

devtools is an essential R package that streamlines the entire package development workflow by automating and simplifying common tasks. Whether you're building your first R package or maintaining a suite of production tools, devtools provides intuitive functions that make the iterative cycle of writing, documenting, testing, and checking code significantly more efficient. Instead of manually rebuilding and reinstalling your package after every change, functions like load_all() simulate installation instantly, while document() automatically generates documentation from your code comments, and test() runs your test suite with a single command.

What makes devtools particularly valuable for data scientists and developers is its modular architecture that coordinates specialized tools while keeping the interface simple. It seamlessly integrates with the broader R development ecosystem, delegating tasks to focused packages like testthat for testing, roxygen2 for documentation, and pak for installation. Beyond local development, devtools extends its reach to quality assurance with check() for package validation and specialized functions for testing on remote Windows and macOS builders. Whether you're installing packages directly from GitHub, building from local sources, or preparing for CRAN submission, devtools provides a unified, developer-friendly interface that lets you focus on solving problems rather than wrestling with development infrastructure.
