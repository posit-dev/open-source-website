---
description: Read flat files (csv, tsv, fwf) into R
github: tidyverse/readr
image: logo.png
languages:
- R
latest_release: '2025-11-14T17:31:10+00:00'
people:
- Hadley Wickham
- Jenny Bryan
- Christophe Dervieux
- Lionel Henry
- Jeroen Ooms
- Mine Çetinkaya-Rundel
- Davis Vaughan
- Jeroen Janssens
- Emil Hvitfeldt
title: readr
website: https://readr.tidyverse.org

external:
  contributors:
  - jimhester
  - hadley
  - jennybc
  - romainfrancois
  - npjc
  - jrnold
  - batpigandme
  - sbearrows
  - krlmlr
  - edwindj
  - yutannihilation
  - Ironholds
  - asnr
  - wibeasley
  - bearloga
  - jdblischak
  - cderv
  - yeedle
  - gergness
  - michaelquinn32
  - mkearney
  - sambrady3
  - dmurdoch
  - dmurdoch
  - dewittpe
  - kmillar
  - boshek
  - ellessenne
  - MichaelChirico
  - lionel-
  - kbenoit
  - jeroen
  - QuLogic
  - mawds
  - brianrice2
  - md0u80c9
  - zeehio
  - bastistician
  - salim-b
  - rgknight
  - RomeroBarata
  - pralitp
  - peterdesmet
  - olgamie
  - noamross
  - mine-cetinkaya-rundel
  - mikmart
  - MikeJohnPage
  - maelle
  - malcolmbarrett
  - tarheel
  - LluisRamon
  - spaette
  - ryanatanner
  - keesdeschepper
  - jangorecki
  - ifendo
  - hidekoji
  - ghaarsma
  - dgromer
  - blakeboswell
  - antoine-lizee
  - zekiakyol
  - shrektan
  - GegznaV
  - thays42
  - tvedebrink
  - TonyLadson
  - leeper
  - uribo
  - nacnudus
  - drvictorvs
  - cb4ds
  - daattali
  - DavisVaughan
  - dpprdan
  - christophergandrud
  - cdhowe
  - cboettig
  - bbrewington
  - billdenney
  - benmarwick
  - pierucci
  - ajdamico
  - alyst
  - dickoa
  - adamroyjones
  - lambdamoses
  - kwstat
  - KKulma
  - jmbarbone
  - namelessjon
  - johnmcdonnell
  - jdeboer
  - jesse-ross
  - jeroenjanssens
  - violetcereza
  - izahn
  - ijlyttle
  - gregrs-uk
  - briatte
  - fpinter
  - erictleung
  - EmilHvitfeldt
  description: Read flat files (csv, tsv, fwf) into R
  first_commit: '2013-07-25T15:28:22+00:00'
  forks: 291
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.462085+00:00'
  latest_release: '2025-11-14T17:31:10+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Jenny Bryan
  - Christophe Dervieux
  - Lionel Henry
  - Jeroen Ooms
  - Mine Çetinkaya-Rundel
  - Davis Vaughan
  - Jeroen Janssens
  - Emil Hvitfeldt
  readme_image: man/figures/logo.png
  repo: tidyverse/readr
  stars: 1024
  title: readr
  website: https://readr.tidyverse.org
---

readr is a fast and user-friendly R package designed to streamline the process of importing rectangular data from delimited files. Whether you're working with CSV, TSV, fixed-width files, or other common data formats, readr offers a dramatic speed improvement over base R functions, delivering performance gains of up to 10-100x depending on your dataset. The package intelligently detects column types during import while providing informative feedback when parsing encounters unexpected results, making it easier to diagnose and resolve data quality issues quickly.

What makes readr particularly valuable for data scientists is its thoughtful design that grows with your workflow. During exploratory analysis, automatic type detection gets you started immediately, while mature production pipelines benefit from explicit column specifications for robust, reproducible imports. As part of the tidyverse, readr follows consistent naming conventions and returns tibbles by default, ensuring seamless integration with your data analysis pipeline. The package handles strings without unwanted modifications, automatically parses common date and time formats, and displays progress bars for lengthy imports, creating a smooth and predictable experience from initial exploration through production deployment.