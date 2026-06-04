---
color: '#0363BD'
description: An implementation of the Grammar of Graphics in R
github: tidyverse/ggplot2
image: ggplot2.png
languages:
- R
latest_release: '2026-04-21T12:44:21+00:00'
people:
- Hadley Wickham
- Winston Chang
- Teun Van den Brand
- Thomas Lin Pedersen
- Lionel Henry
- Max Kuhn
- Hassan Kibirige
- Carson Sievert
- Mine Çetinkaya-Rundel
- Barret Schloerke
- Charlotte Wickham
- Christophe Dervieux
- Davis Vaughan
- Julia Silge
- Gábor Csárdi
- Jeroen Ooms
tags:
- tidyverse
- data visualization
title: ggplot2
topics:
- Visualization
website: https://ggplot2.tidyverse.org

exclude:
  people:
  - Jeroen Janssens

external:  # updated automatically, do not edit
  description: An implementation of the Grammar of Graphics in R
  first_commit: '2008-05-25T01:21:32+00:00'
  forks: 2134
  languages:
  - R
  last_updated: '2026-05-20T08:05:43.888124+00:00'
  latest_release: '2026-04-21T12:44:21+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Winston Chang
  - Teun Van den Brand
  - Thomas Lin Pedersen
  - Lionel Henry
  - Max Kuhn
  - Hassan Kibirige
  - Carson Sievert
  - Mine Çetinkaya-Rundel
  - Barret Schloerke
  - Charlotte Wickham
  - Christophe Dervieux
  - Davis Vaughan
  - Julia Silge
  - Gábor Csárdi
  - Jeroen Janssens
  - Jeroen Ooms
  readme_image: man/figures/logo.png
  repo: tidyverse/ggplot2
  stars: 6933
  title: ggplot2
  website: https://ggplot2.tidyverse.org
---

ggplot2 is an R package for creating graphics using a declarative system based on The Grammar of Graphics. You provide data and specify how variables map to visual properties, then add layers like points or histograms to build complete visualizations.

The package handles low-level plotting details automatically, letting you focus on the structure of your visualization. It supports layered graphics construction through composable components (geometries, scales, facets, coordinate systems). The package is mature and stable, with a large ecosystem of extensions for specialized plot types and customizations.

## Try it

{{< webr packages="ggplot2" >}}
library(ggplot2)

ggplot(diamonds[sample(nrow(diamonds), 2000), ],
       aes(carat, price, color = cut)) +
  geom_point(alpha = 0.6, size = 1.5) +
  scale_color_brewer(palette = "Spectral") +
  scale_y_continuous(labels = scales::dollar) +
  facet_wrap(vars(cut), nrow = 1) +
  labs(title = "Diamond Price vs Carat by Cut Quality",
       x = "Carat", y = "Price") +
  theme_minimal(base_size = 11) +
  theme(legend.position = "none")
{{< /webr >}}
