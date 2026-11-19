---
title: Advanced R
date: '2019-05-24'
description: Learn how R works under the hood, from names and values, functions, and environments to functional programming, object-oriented programming with S3, S4, and R6, metaprogramming, and performance.
image: cover.jpg
color: '#F49525'
resource_type: book
edition: 2
publisher: CRC Press
isbn: '9780815384571'
pages: 604
people:
- Hadley Wickham
website: https://adv-r.hadley.nz/
read_url: https://adv-r.hadley.nz/
buy_url: https://www.routledge.com/Advanced-R-Second-Edition/Wickham/p/book/9780815384571
github: hadley/adv-r
software:
- rlang
- lobstr
- r6
languages:
- R
topics:
- Best Practices
---

Hadley Wickham's guide to R as a programming language is written for two audiences: intermediate R users who want to understand how the language really works, and programmers coming from other languages who want to know why R behaves the way it does.
Rather than teaching data analysis, it explains the ideas and techniques behind well-designed R code, including those used to build the tidyverse.

The second edition is a major revision.
It adds new foundational chapters on names and values, control flow, and conditions; expands object-oriented programming into separate chapters on S3, R6, and S4 and how to choose among them; and greatly deepens the coverage of metaprogramming, including the tidy evaluation framework.
Examples use newer packages such as `rlang` for low-level operations and `purrr` for functional programming, and code and figures are printed in color.
Chapters include quizzes and exercises, with worked answers available in the companion book *Advanced R Solutions*.

Readers will learn:

- How objects differ from the names bound to them, and when R makes copies
- How vectors, subsetting, functions, environments, and the condition system work
- Functional programming techniques that can replace many for loops
- The S3, S4, and R6 object-oriented systems and their trade-offs
- Metaprogramming with expressions, quasiquotation, and tidy evaluation
- Debugging strategies that work wherever your code runs
- How to find performance bottlenecks and rewrite slow functions in C++ with `Rcpp`

The complete book is free to read online under a Creative Commons license.
