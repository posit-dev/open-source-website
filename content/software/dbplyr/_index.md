---
description: Database (DBI) backend for dplyr
github: tidyverse/dbplyr
image: logo.png
languages:
- R
latest_release: '2025-09-09T16:38:02+00:00'
people:
- Hadley Wickham
- Lionel Henry
- Edgar Ruiz
- Simon Couch
- Christophe Dervieux
- Mine Çetinkaya-Rundel
- Davis Vaughan
- Carson Sievert
- Joe Cheng
- Jeroen Janssens
- Garrick Aden-Buie
title: dbplyr
website: https://dbplyr.tidyverse.org

external:
  contributors:
  - hadley
  - romainfrancois
  - mgirlich
  - krlmlr
  - lionel-
  - edgararuiz
  - colearendt
  - lindbrook
  - jimhester
  - batpigandme
  - hannes
  - edward-burn
  - kevinushey
  - ejneer
  - ilarischeinin
  - javierluraschi
  - sfirke
  - cosinequanon
  - MichaelChirico
  - simonpcouch
  - leondutoit
  - dpprdan
  - zeehio
  - pimentel
  - eibanez
  - cderv
  - arunsrinivasan
  - DavidPatShuiFong
  - austenhead
  - fh-afrachioni
  - shosaco
  - fh-mthomson
  - imanuelcostigan
  - rbdixon
  - okhoma
  - shabbybanks
  - erikvona
  - zacdav-db
  - xiaodaigh
  - thomashulst
  - mtoto
  - uribo
  - rsund
  - owenjonesuob
  - NicolasCOUTIN
  - ablack3
  - derekmorr
  - earino
  - alistaire47
  - edwindj
  - hdplsa
  - ianmcook
  - kevinykuo
  - justmarkham
  - zozlak
  - mkuhn
  - mkearney
  - nathanhaigh
  - nhanitvn
  - noamross
  - OssiLehtinen
  - paulstaab
  - PauloJhonny
  - rplsmn
  - robertzk
  - overmar
  - Robinlovelace
  - russellpierce
  - mine-cetinkaya-rundel
  - MikeJohnPage
  - mtreadwell
  - mdsumner
  - mkuehn10
  - mnel
  - maelle
  - matthewjnield
  - mattle24
  - washcycle
  - sandan
  - mungojam
  - yutannihilation
  - teramonagi
  - shearerp
  - shea-parkes
  - mnfn
  - klmedeiros
  - hs3180
  - hoxo-m
  - harrismcgehee
  - agable-vt
  - fh-kpikhart
  - eitsupi
  - eipi10
  - edgararuiz-zz
  - pachevalier
  - avsdev-cw
  - zachary-foster
  - sverchkov
  - wibeasley
  - tdsmith
  - tcarnus
  - StevenMMortimer
  - salim-b
  - aguynamedryan
  - FvD
  - saurfang
  - ethanwhite
  - espinielli
  - cb4ds
  - DavisVaughan
  - dgrtwo
  - davidkretch
  - davidchall
  - gorcha
  - denismaciel
  - craigcitro
  - chrmongeau
  - cwarden
  - chris-billingham
  - NoRaincheck
  - cjyetman
  - rehbbea
  - bbolker
  - ajdamico
  - cpsievert
  - ateucher
  - alexkyllo
  - aaronwolen
  - lorenzwalthert
  - LluisRamon
  - liudvikasakelis
  - kirillseva
  - karldw
  - jentjr
  - casallas
  - jrandall
  - joranE
  - jonkeane
  - jonassundman
  - jcheng5
  - jeroenjanssens
  - JeremyPasco
  - jrnold
  - bairdj
  - bkkkk
  - jsowder
  - itcarroll
  - gregrahn
  - gergness
  - nachti
  - gadenbuie
  - garrettgman
  description: Database (DBI) backend for dplyr
  first_commit: '2017-03-28T20:29:16+00:00'
  forks: 187
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.783667+00:00'
  latest_release: '2025-09-09T16:38:02+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Lionel Henry
  - Edgar Ruiz
  - Simon Couch
  - Christophe Dervieux
  - Mine Çetinkaya-Rundel
  - Davis Vaughan
  - Carson Sievert
  - Joe Cheng
  - Jeroen Janssens
  - Garrick Aden-Buie
  readme_image: man/figures/logo.png
  repo: tidyverse/dbplyr
  stars: 504
  title: dbplyr
  website: https://dbplyr.tidyverse.org
---

dbplyr is the database backend for dplyr, enabling you to work with remote database tables as if they were in-memory data frames. It automatically translates your familiar dplyr code into optimized SQL queries, eliminating the need to write raw SQL while maintaining the efficiency of database-side processing. With lazy evaluation at its core, dbplyr generates queries that only execute when you explicitly request results, allowing you to build complex data pipelines that process large datasets remotely without overwhelming your local memory.

What makes dbplyr particularly valuable for data scientists and developers is its seamless integration with the dplyr ecosystem. You can use the same intuitive grammar for filtering, grouping, summarizing, and joining data whether working with local data frames or massive database tables. This consistency means you can prototype analyses on small local datasets and scale them to production databases without rewriting code. dbplyr supports a wide range of database systems through the DBI interface and even provides tools to inspect the generated SQL, giving you both the convenience of high-level syntax and the transparency to understand and optimize your database operations.
