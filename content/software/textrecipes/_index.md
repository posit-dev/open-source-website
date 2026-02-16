---
description: Extra recipes for Text Processing
github: tidymodels/textrecipes
image: logo.png
languages:
- R
latest_release: '2025-03-18T15:37:10+00:00'
people:
- Emil Hvitfeldt
- Julia Silge
- Max Kuhn
- Davis Vaughan
- Hannah Frick
- Hadley Wickham
title: textrecipes
website: https://textrecipes.tidymodels.org/

external:
  contributors:
  - EmilHvitfeldt
  - juliasilge
  - topepo
  - jonthegeek
  - joranE
  - DavisVaughan
  - hfrick
  - kanishkamisra
  - aluxh
  - duttashi
  - kant
  - hadley
  description: Extra recipes for Text Processing
  first_commit: '2018-09-10T23:15:56+00:00'
  forks: 17
  languages:
  - R
  last_updated: '2026-02-13T14:17:12.247046+00:00'
  latest_release: '2025-03-18T15:37:10+00:00'
  license: NOASSERTION
  people:
  - Emil Hvitfeldt
  - Julia Silge
  - Max Kuhn
  - Davis Vaughan
  - Hannah Frick
  - Hadley Wickham
  readme_image: man/figures/logo.png
  repo: tidymodels/textrecipes
  stars: 164
  title: textrecipes
  website: https://textrecipes.tidymodels.org/
---

textrecipes extends the recipes framework with specialized preprocessing steps designed specifically for text data, enabling seamless integration of natural language processing into tidymodels machine learning workflows. When working with unstructured text data, data scientists face the challenge of transforming words and documents into numerical features that models can understand. textrecipes solves this by providing a comprehensive toolkit of text-specific preprocessing steps that work within the familiar recipes pipeline, ensuring reproducible transformations and consistent handling of both training and test data.

The package offers essential text processing capabilities including tokenization, stopword removal, token filtering, TF-IDF transformation, and even advanced techniques like Latent Dirichlet Allocation for topic modeling. By operating within the recipes framework, textrecipes allows you to chain multiple text preprocessing steps together, combine them with other feature engineering operations, and apply the entire pipeline consistently across your dataset. This makes it invaluable for anyone building text classification models, sentiment analysis systems, or any machine learning application that needs to extract meaningful features from text.
