---
description: Classes and functions to create and summarize resampling objects
github: tidymodels/rsample
image: logo.png
languages:
- R
latest_release: '2026-01-30T11:52:49+00:00'
people:
- Hannah Frick
- Max Kuhn
- Julia Silge
- Davis Vaughan
- Emil Hvitfeldt
- Simon Couch
- Jeroen Janssens
- Gábor Csárdi
title: rsample
website: https://rsample.tidymodels.org

external:
  contributors:
  - hfrick
  - topepo
  - juliasilge
  - DavisVaughan
  - fbchow
  - mikemahoney218
  - PriKalra
  - Dpananos
  - ClaytonJY
  - EmilHvitfeldt
  - JamesHWade
  - mdancho84
  - agmurray
  - nmercadeb
  - simonpcouch
  - batpigandme
  - seb09
  - bjornkallerud
  - rkb965
  - laurabrianna
  - brshallo
  - ZWael
  - timtrice
  - MichaelChirico
  - mattwarkentin
  - LluisRamon
  - liamblake
  - krlmlr
  - duju211
  - jonkeane
  - jeroenjanssens
  - jamesm131
  - issactoast
  - hlynurhallgrims
  - gaborcsardi
  - erictleung
  - EdwinTh
  - dpastling
  - brian-j-smith
  - abichat
  - AngelFelizR
  - alvindev0
  description: Classes and functions to create and summarize resampling objects
  first_commit: '2017-04-22T19:19:58+00:00'
  forks: 68
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.066790+00:00'
  latest_release: '2026-01-30T11:52:49+00:00'
  license: NOASSERTION
  people:
  - Hannah Frick
  - Max Kuhn
  - Julia Silge
  - Davis Vaughan
  - Emil Hvitfeldt
  - Simon Couch
  - Jeroen Janssens
  - Gábor Csárdi
  readme_image: man/figures/logo.png
  repo: tidymodels/rsample
  stars: 340
  title: rsample
  website: https://rsample.tidymodels.org
---

rsample is a foundational R package within the tidymodels ecosystem that provides efficient tools for creating and analyzing resampled datasets. Whether you're estimating sampling distributions to understand statistical properties or evaluating model performance with holdout sets, rsample offers a comprehensive suite of resampling methods including bootstrap, cross-validation, Monte Carlo splits, and more. The package focuses on delivering the essential building blocks for resampling workflows, integrating seamlessly with other tidymodels packages for end-to-end machine learning pipelines.

What makes rsample particularly valuable for data scientists working with large datasets is its remarkable memory efficiency. Rather than creating full copies of your data for each resample, rsample uses intelligent indexing to reference the original dataset. This approach means that creating 50 bootstrap samples increases memory usage by only 2-3 times instead of 50 times, making extensive resampling workflows practical even with substantial datasets. Combined with its consistent, tidy interface and modular design, rsample enables you to conduct rigorous model evaluation and statistical analysis without worrying about computational overhead or memory constraints.
