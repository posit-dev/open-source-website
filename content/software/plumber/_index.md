---
description: Turn your R code into a web API.
github: rstudio/plumber
image: logo.svg
languages:
- R
latest_release: '2026-02-09T15:06:24+00:00'
people:
- Barret Schloerke
- Thomas Lin Pedersen
- Joe Cheng
- Garrick Aden-Buie
- Charlie Gao
- Carson Sievert
title: plumber
website: https://www.rplumber.io

external:
  contributors:
  - trestletech
  - schloerke
  - meztez
  - blairj09
  - FvD
  - thomasp85
  - antoine-sachet
  - shrektan
  - wkmor1
  - shapenaji
  - JosiahParry
  - muschellij2
  - jcheng5
  - sambaala
  - m-muecke
  - mhairi
  - pachadotdev
  - randyzwitch
  - robertdj
  - scottmmjackson
  - s-fleck
  - mtoto
  - thiyagu-p
  - TylerGrantSmith
  - vfulco
  - vspinu
  - eitsupi
  - olivroy
  - r2evans
  - svdwoude
  - maxheld83
  - jdtrat
  - howardbaik
  - yutannihilation
  - gtritchie
  - gadenbuie
  - etiennebr
  - pinduzera
  - ColinFay
  - chris-dudley
  - shikokuchuo
  - cpsievert
  - cgiachalis
  - aronatkins
  - atheriel
  description: Turn your R code into a web API.
  first_commit: '2015-06-04T05:09:10+00:00'
  forks: 260
  languages:
  - R
  last_updated: '2026-02-13T14:17:01.863877+00:00'
  latest_release: '2026-02-09T15:06:24+00:00'
  license: NOASSERTION
  people:
  - Barret Schloerke
  - Thomas Lin Pedersen
  - Joe Cheng
  - Garrick Aden-Buie
  - Charlie Gao
  - Carson Sievert
  readme_image: man/figures/logo.svg
  repo: rstudio/plumber
  stars: 1433
  title: plumber
  website: https://www.rplumber.io
---

Plumber transforms your existing R code into production-ready web APIs with minimal effort. By simply adding special comment decorations to your R functions, you can expose them as HTTP endpoints without learning web development frameworks or restructuring your code. Whether you need to share analytical models, create data pipelines, or integrate R with other applications, Plumber handles the complexities of request routing, parameter parsing, and response formatting across multiple data formats including JSON, XML, and even custom outputs like PNG images.

What makes Plumber particularly powerful for data scientists and developers is its seamless integration with the R ecosystem and modern deployment workflows. Using familiar roxygen2-style annotations, you can define API routes, specify HTTP methods, and document your endpoints directly in your R source files. Plumber supports flexible deployment options ranging from local development servers for rapid testing to enterprise platforms like Posit Connect, Docker containers, and cloud services. This makes it ideal for teams looking to operationalize their R analytics, build microservices architectures, or provide programmatic access to R-powered insights without sacrificing the interactive development experience that makes R so productive.
