---
title: Class agnostic time series with tsbox
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-04-01'
description: Convert, combine, and transform time series across all major R time series classes using tsbox.
download_url: tsbox.pdf
people:
- Christoph Sax
thumbnails:
- page-1.png
languages:
- R
---

tsbox provides a class-agnostic toolkit that works identically with ts, xts, zoo, data.frame,
tibble, data.table, tsibble, and other time series classes. All functions start with `ts_` and
return an object of the same class as the input, handling both regular and irregular frequencies.

## What's covered
- Basics – the `ts_` prefix convention and combining time series with `ts_c` and `ts_bind`
- Class conversion – `ts_ts`, `ts_df`, `ts_xts`, `ts_tbl`, `ts_zoo`, `ts_tsibble`, `ts_tslist`
- Helper functions – `ts_trend`, `ts_pc`, `ts_pcy`, `ts_scale`, `ts_index`, `ts_seas`, `ts_lag`
- Span and frequency operations
- Time series in data frames – long structure and auto-detect column names
