---
description: Sass compiler package for R
github: rstudio/sass
image: logo.svg
languages:
- C++
latest_release: '2025-04-11T20:21:04+00:00'
people:
- Carson Sievert
- Winston Chang
- Rich Iannone
- Barret Schloerke
- Joe Cheng
- Charlie Gao
- Christophe Dervieux
- George Stagg
- Hadley Wickham
- Jeroen Ooms
title: sass
website: https://rstudio.github.io/sass/

external:
  contributors:
  - cpsievert
  - wch
  - tmastny
  - rich-iannone
  - schloerke
  - jcheng5
  - shikokuchuo
  - paleolimbot
  - abichat
  - cderv
  - georgestagg
  - hadley
  - jeroen
  - maelle
  - salim-b
  description: Sass compiler package for R
  first_commit: '2018-08-14T17:02:58+00:00'
  forks: 19
  languages:
  - C++
  last_updated: '2026-02-13T14:17:03.607937+00:00'
  latest_release: '2025-04-11T20:21:04+00:00'
  license: NOASSERTION
  people:
  - Carson Sievert
  - Winston Chang
  - Rich Iannone
  - Barret Schloerke
  - Joe Cheng
  - Charlie Gao
  - Christophe Dervieux
  - George Stagg
  - Hadley Wickham
  - Jeroen Ooms
  readme_image: man/figures/logo.svg
  repo: rstudio/sass
  stars: 101
  title: sass
  website: https://rstudio.github.io/sass/
---

The sass package brings the power of Sass (Syntactically Awesome Style Sheets) to R, providing native bindings to LibSass for compiling Sass into CSS. Sass is a mature CSS extension language that makes styling modern websites less complex and more maintainable through features like variables, nesting, mixins, and mathematical operations. Rather than writing repetitive CSS manually, you can use Sass to create dynamic, reusable stylesheets that are easier to understand and modify.

This package is particularly valuable for R developers building web applications, interactive documents, or R packages that require customizable styling systems. The sass package accepts input in multiple flexible formats including raw R strings, named lists for defining variables, file references, and nested structures combining all these methods. With its fast C++-based compiler, sass seamlessly integrates Sass preprocessing capabilities into R workflows, enabling programmatic stylesheet generation and making it simpler to maintain consistent, sophisticated designs across your projects.
