---
title: labelled
image: page-1.png
resource_type: cheatsheet
by: community
date: '2020-06-01'
description: Manipulate labelled data imported from Stata, SAS, or SPSS, including variable labels, value labels, and user-defined missing values.
download_url: labelled.pdf
people:
- Joseph Larmarange
thumbnails:
- page-1.png
- page-2.png
software:
- haven
languages:
- R
source_files:
- file: labelled.pptx
  format: PowerPoint
---

The labelled package provides functions to handle labelled data structures common in Stata, SAS, and SPSS. It manages variable labels (`var_label()`), value labels (`val_labels()`), SPSS-style user-defined missing values, and Stata/SAS-style tagged NAs, and supports converting labelled vectors to factors or plain R types.

## What's covered
- Basics – labelled data structure and its three attribute types
- Variable labels – `var_label()` and `set_variable_labels()` for reading and setting labels on vectors and data frames
- Value labels – `val_labels()`, `val_label()`, `add_value_labels()`, and `set_value_labels()`
- Missing values – SPSS-style `na_values()` / `na_range()` and Stata/SAS tagged NAs (`tagged_na()`, `na_tag()`)
- When using labelled data? – guidance on converting to factors or numeric vectors before analysis
- Conversion – `to_factor()`, `to_character()`, `remove_val_labels()`, `to_labelled()`
