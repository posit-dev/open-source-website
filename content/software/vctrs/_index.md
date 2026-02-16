---
description: Generic programming with typed R vectors
github: r-lib/vctrs
image: logo.png
languages:
- C
latest_release: '2026-01-27T14:09:03+00:00'
people:
- Lionel Henry
- Davis Vaughan
- Hadley Wickham
- Jenny Bryan
- George Stagg
- Jeroen Janssens
title: vctrs
website: https://vctrs.r-lib.org

external:
  contributors:
  - lionel-
  - DavisVaughan
  - hadley
  - krlmlr
  - romainfrancois
  - jennybc
  - maxheld83
  - batpigandme
  - lbm364dl
  - earowang
  - echasnovski
  - yutannihilation
  - ijlyttle
  - jimhester
  - fenguoerbian
  - dpprdan
  - gorcha
  - paleolimbot
  - QuLogic
  - etiennebacher
  - georgestagg
  - gergness
  - IndrajeetPatil
  - jameslairdsmith
  - JamesCuster
  - jeroenjanssens
  - jessesadler
  - JosiahParry
  - jtlandis
  - mgirlich
  - MichaelChirico
  - mdsumner
  - Akirathan
  - salim-b
  - 808sAndBR
  - zachary-foster
  - chsafouane
  - coreyyanofsky-zz
  - juangomezduaso
  - olivroy
  description: Generic programming with typed R vectors
  first_commit: '2016-09-06T21:32:53+00:00'
  forks: 73
  languages:
  - C
  last_updated: '2026-02-13T14:17:19.121114+00:00'
  latest_release: '2026-01-27T14:09:03+00:00'
  license: NOASSERTION
  people:
  - Lionel Henry
  - Davis Vaughan
  - Hadley Wickham
  - Jenny Bryan
  - George Stagg
  - Jeroen Janssens
  readme_image: man/figures/logo.png
  repo: r-lib/vctrs
  stars: 300
  title: vctrs
  website: https://vctrs.r-lib.org
---

vctrs provides the foundational tools for creating consistent and predictable S3 vector classes in R. It addresses longstanding inconsistencies in how base R handles vectorization, type coercion, and recycling by establishing a unified theory and framework. The package introduces key primitives like `vec_size()` and `vec_ptype()` that provide more reliable alternatives to `length()` and `class()`, along with size-stable and type-stable operations that make function behavior more predictable across different data types.

For R package developers, vctrs dramatically simplifies the creation of custom vector types that work seamlessly across the tidyverse ecosystem. By building on vctrs' base class infrastructure, developers can implement new vector classes with far fewer methods than building from scratch, while automatically gaining consistent behavior for common operations like combining, subsetting, and coercion. The package's minimal dependencies and lightweight design make it ideal as foundational infrastructure, enabling robust data structures that provide users with more intuitive and reliable data manipulation experiences.