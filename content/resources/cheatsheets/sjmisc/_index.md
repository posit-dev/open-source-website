---
title: sjmisc
image: page-1.png
resource_type: cheatsheet
by: community
date: '2017-08-01'
description: Transform and recode variables in data frames using sjmisc alongside dplyr and pipes.
download_url: sjmisc.pdf
people:
- Daniel Lüdecke
thumbnails:
- page-1.png
languages:
- R
---

sjmisc complements dplyr with functions for data transformation and variable recoding, designed
to work with pipes and labelled data. Functions follow the tidyverse convention of
taking the data as the first argument and returning the same type as the input.

## What's covered
- Design philosophy – vector and data frame input, ellipsis argument for variable selection
- Frequency tables – `frq`, `flat_table`, `count_na`
- Descriptive summary – `descr`
- Finding variables in a data frame – `find_var`
- Recode and transform variables – `rec`, `dicho`, `split_var`, `group_var`, `std`, `recode_to`
- Summarise variables and cases – `row_sums`, `row_means`, `row_count`
- Other useful functions – `add_columns`, `set_na`, `remove_var`, `group_str`, `to_long`, `merge_df`
