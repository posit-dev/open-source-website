---
title: Advanced and Fast Data Transformation with collapse
image: page-1.png
resource_type: cheatsheet
by: community
date: '2023-10-01'
description: Perform fast grouped, weighted, and panel-data statistical operations on R vectors, matrices, and data frames using C/C++.
download_url: collapse.pdf
people:
- Sebastian Krantz
thumbnails:
- page-1.png
- page-2.png
languages:
- R
---

collapse is a C/C++ based R package for advanced data transformation that is class-agnostic and compatible with base R, dplyr, data.table, and panel data classes. It provides fast statistical functions, flexible grouping objects, and efficient in-place data manipulation with minimal memory overhead and support for multithreading.

## What's covered
- Introduction – design philosophy and compatibility
- Fast statistical functions – `fmean()`, `fmedian()`, `fsum()`, `fsd()`, `fnth()`, and more
- Grouping and ordering – `GRP()`, `fgroup_by()`, `qF()`, `radixorder()`
- Fast data manipulation – `fselect()`, `fsubset()`, `fmutate()`, `fsummarise()`, `join()`, `pivot()`
- Row/column arithmetic by reference – `%cr%`, `%r+%`, `setop()`
