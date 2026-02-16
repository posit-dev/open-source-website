---
description: Pipeable steps for feature engineering and data preprocessing to prepare
  for modeling
github: tidymodels/recipes
image: logo.png
languages:
- R
latest_release: '2025-05-21T17:05:49+00:00'
people:
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Davis Vaughan
- Hannah Frick
- Simon Couch
- Daniel Falbel
- Lionel Henry
- Garrick Aden-Buie
- Gábor Csárdi
title: recipes
website: https://recipes.tidymodels.org

external:
  contributors:
  - EmilHvitfeldt
  - topepo
  - juliasilge
  - DavisVaughan
  - hfrick
  - EdwinTh
  - simonpcouch
  - alexpghayes
  - HolyMiracle
  - AshesITR
  - jkennel
  - terrytangyuan
  - dajmcdon
  - RaymondBalise
  - jrnold
  - Edgar-Zamora
  - seb09
  - olivroy
  - gregdenay
  - mastoffel
  - dfalbel
  - ewv88
  - lawwu
  - lionel-
  - MichaelChirico
  - smingerson
  - klahrich
  - jakubkovac
  - ttzhou
  - tmastny
  - rorynolan
  - batpigandme
  - gadenbuie
  - gdequeiroz
  - erictleung
  - dimagor
  - meztez
  - brunocarlin
  - atsyplenkov
  - lorenzwalthert
  - lgaborini
  - perluna
  - msberends
  - mikemc
  - monicagerber
  - schoonees
  - stufield
  - VictorSuarezL
  - asmae-toumi
  - fxdlmatt
  - jyuu
  - karissawhiting
  - laurabrianna
  - rudeboybert
  - tareefk
  - abichat
  - balthasars
  - bcjaeger
  - collinberke
  - dlependorf
  - dshemetov
  - doug-friedman
  - gaborcsardi
  - hnagaty
  - jameslairdsmith
  - jaredlander
  - corybrunson
  - jrwinget
  - GoldbergData
  - zecojls
  - liamblake
  description: Pipeable steps for feature engineering and data preprocessing to prepare
    for modeling
  first_commit: '2016-12-16T02:40:24+00:00'
  forks: 123
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.030334+00:00'
  latest_release: '2025-05-21T17:05:49+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Davis Vaughan
  - Hannah Frick
  - Simon Couch
  - Daniel Falbel
  - Lionel Henry
  - Garrick Aden-Buie
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: tidymodels/recipes
  stars: 612
  title: recipes
  website: https://recipes.tidymodels.org
---

recipes is a powerful R package designed to streamline the data preprocessing and feature engineering workflow in machine learning projects. Built as part of the tidymodels ecosystem, it provides a dplyr-like, pipeable interface for creating reproducible sequences of data transformation steps. recipes addresses the limitations of traditional R preprocessing approaches by offering a flexible framework that can handle complex feature engineering pipelines, from simple operations like centering and scaling to sophisticated transformations for categorical variables, missing data imputation, and dimensionality reduction.

What makes recipes particularly valuable for data scientists is its emphasis on workflow consistency and reproducibility. Instead of ad-hoc preprocessing code scattered throughout your analysis, recipes lets you define a structured specification that can be applied uniformly across training and test datasets, ensuring that the same transformations are executed in the correct order every time. The package integrates seamlessly with other tidymodels tools, making it an essential component for building end-to-end machine learning workflows in R. With its extensive library of built-in preprocessing steps and the ability to create custom transformations, recipes provides both accessibility for common tasks and extensibility for specialized requirements.
