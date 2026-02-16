---
description: Make HTTP requests and process their responses. A modern reimagining
  of httr.
github: r-lib/httr2
image: logo.png
languages:
- R
latest_release: '2025-12-05T17:45:53+00:00'
people:
- Hadley Wickham
- Charlie Gao
- Jeroen Ooms
- Jenny Bryan
- Joe Cheng
- Neal Richardson
- Gábor Csárdi
- Jeroen Janssens
title: httr2
website: https://httr2.r-lib.org

external:
  contributors:
  - hadley
  - mgirlich
  - jonthegeek
  - atheriel
  - shikokuchuo
  - jeroen
  - jennybc
  - salim-b
  - maelle
  - jcheng5
  - jameslairdsmith
  - jl5000
  - MichaelChirico
  - flahn
  - boshek
  - romainfrancois
  - pedrobtz
  - nealrichardson
  - cgiachalis
  - gergness
  - gaborcsardi
  - jchrom
  - fh-mthomson
  - m-muecke
  - arnaudgallou
  - DyfanJones
  - MSHelm
  - feinleib
  - maxheld83
  - casa-henrym
  - mdsumner
  - mthomas-ketchbrook
  - Nelson-Gon
  - owenjonesuob
  - plietar
  - ramiromagno
  - marberts
  - tanho63
  - taerwin
  - denskh
  - jeffreyzuber
  - olivroy
  - verhovsky
  - botan
  - arcresu
  - DMerch
  - dpprdan
  - DavidRLovell
  - elipousson
  - burgerga
  - gvelasq
  - yutannihilation
  - hongooi73
  - howardbaik
  - jansim
  - jeroenjanssens
  - jimbrig
  - judith-bourque
  - Kevanness
  - KoderKow
  description: Make HTTP requests and process their responses. A modern reimagining
    of httr.
  first_commit: '2018-11-22T15:32:29+00:00'
  forks: 85
  languages:
  - R
  last_updated: '2026-02-13T14:17:19.995833+00:00'
  latest_release: '2025-12-05T17:45:53+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Charlie Gao
  - Jeroen Ooms
  - Jenny Bryan
  - Joe Cheng
  - Neal Richardson
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/httr2
  stars: 258
  title: httr2
  website: https://httr2.r-lib.org
---

httr2 is a modern HTTP client for R that makes working with web APIs elegant and reliable. Whether you're retrieving data from REST APIs, building integrations with web services, or automating HTTP workflows, httr2 provides a clean, chainable interface that lets you compose requests step-by-step and handle responses with confidence. Built as a reimagining of its predecessor httr, it brings contemporary design patterns to R's HTTP toolkit while maintaining the stability of proven libraries like curl and openssl.

The package excels at making API interactions robust and developer-friendly. It includes automatic retry logic for handling transient failures and rate limiting, built-in response caching for improved performance, and comprehensive OAuth support for modern authentication flows. Security features like credential management and secret obfuscation help you write code that's safe to share publicly. With explicit request objects and powerful helper functions for extracting response data—whether JSON, HTML, headers, or status codes—httr2 gives data scientists and developers the tools they need to work seamlessly with any HTTP-based service.