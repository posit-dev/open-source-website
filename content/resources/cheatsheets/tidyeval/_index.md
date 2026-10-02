---
title: Tidy evaluation with rlang
image: page-1.png
resource_type: cheatsheet
by: posit
date: '2018-11-01'
description: Use the rlang package to write functions that work with tidyverse-style non-standard evaluation, quosures, and quasiquotation.
download_url: tidyeval.pdf
people:
- Garrett Grolemund
- Mine Çetinkaya-Rundel
thumbnails:
- page-1.png
- page-2.png
software:
- rlang
languages:
- R
source_files:
- file: tidyeval.key
  format: Keynote
- file: tidyeval.pptx
  format: PowerPoint
translations:
- language: Spanish
  lang: es
  file: tidyeval_es.pdf
  edition: rlang 0.3.0
  updated: 2019-10
  source: tidyeval_es.pptx
---

Tidy evaluation is a framework for non-standard (delayed) evaluation in R that makes it easier to program with tidyverse functions. This cheat sheet covers the key vocabulary and the rlang functions used to quote, unquote, and evaluate code.

## What's covered
- Vocabulary – symbols, environments, constants, call objects, expressions, quosures, and expression vectors
- Quoting Code – `quo()`, `enquo()`, `quos()`, `enquos()` for quosures; `expr()`, `enexpr()`, `exprs()`, `enexprs()` for expressions; `ensym()` for symbols
- Parsing and Deparsing – `parse_expr()`, `expr_text()`, `quo_name()`
- Building Calls – `call2()`, `exec()` for constructing and evaluating calls
- Evaluation – `eval_bare()`, `eval_tidy()`, data masks, and the `.data$` pronoun
- Quasiquotation – `!!` (unquote), `!!!` (unquote-splice), `:=` (unquote in LHS)
- Programming Recipes – writing functions that recognize quasiquotation operators
