---
description: Extra recipes for predictor embeddings
github: tidymodels/embed
image: logo.png
languages:
- R
latest_release: '2026-01-29T21:24:25+00:00'
people:
- Emil Hvitfeldt
- Max Kuhn
- Julia Silge
- Hannah Frick
- Daniel Falbel
- Simon Couch
- Davis Vaughan
- Gábor Csárdi
- Jeroen Janssens
title: embed
website: https://embed.tidymodels.org

external:
  contributors:
  - EmilHvitfeldt
  - topepo
  - juliasilge
  - hfrick
  - konradsemsch
  - dfalbel
  - simonpcouch
  - JamesHWade
  - klahrich
  - Athospd
  - corybrunson
  - DavisVaughan
  - eddelbuettel
  - focardozom
  - gaborcsardi
  - jeroenjanssens
  - ndjrt
  - smingerson
  - tmastny
  - asiripanich
  description: Extra recipes for predictor embeddings
  first_commit: '2018-05-16T18:28:10+00:00'
  forks: 22
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.182746+00:00'
  latest_release: '2026-01-29T21:24:25+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Max Kuhn
  - Julia Silge
  - Hannah Frick
  - Daniel Falbel
  - Simon Couch
  - Davis Vaughan
  - Gábor Csárdi
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: tidymodels/embed
  stars: 144
  title: embed
  website: https://embed.tidymodels.org
---

embed is a specialized R package that extends the recipes framework with advanced techniques for transforming categorical and numeric predictors into more informative numeric embeddings. Unlike traditional one-hot encoding, embed provides supervised preprocessing methods that leverage outcome information to create features with stronger predictive power. The package offers a rich toolkit including likelihood encodings via generalized linear models, Bayesian approaches, neural network embeddings through Keras, and sophisticated techniques like weight of evidence encodings and feature hashing for high-cardinality categorical data.

For numeric predictors, embed brings powerful dimensionality reduction and binning capabilities to your tidymodels workflow. It integrates UMAP for nonlinear dimensionality reduction, supervised tree-based binning using XGBoost and CART, and sparse principal component analysis with optional Bayesian refinement. Whether you're dealing with high-cardinality features that would explode into thousands of indicator variables or seeking to create more meaningful numeric representations for downstream modeling, embed provides the preprocessing steps you need while maintaining the familiar recipes syntax and seamless integration with the broader tidymodels ecosystem.
