---
title: gt
image: page-1.png
resource_type: cheatsheet
by: posit
date: '2026-08-01'
description: Create display tables from R data frames with formatting, styling, and output to HTML, PDF, LaTeX, and Word.
download_url: gt.pdf
people:
- Mine Çetinkaya-Rundel
- Rich Iannone
thumbnails:
- page-1.png
software:
- gt
languages:
- R
source_files:
- file: gt.key
  format: Keynote
---

The gt package lets you turn R data frames into display tables by structuring, formatting, and styling every element. It is well-suited for Shiny apps, Quarto documents, and standalone HTML or PDF reports. All formatting is done through a consistent, pipeable API.

## What's covered
- Introduction – package overview and sample datasets
- Creating a gt Table – `gt()`, basic workflow, and `exibble` example
- Adding Structure – `tab_header()`, `tab_source_note()`, `tab_footnote()`, stub and row groups, column spanners, `row_group_order()`
- Formatting Data Values – `fmt_number()`, `fmt_integer()`, `fmt_percent()`, `fmt_scientific()`, `fmt_date()`, `fmt_time()`, `fmt_datetime()`, `fmt_image()`, `fmt_icon()`, `fmt_flag()`
- Colorizing Body Cells – `data_color()` with domain and palette options
- Adding Nanoplots – `cols_nanoplot()` for inline sparklines
- Styling the Table – `tab_style()` with `cell_fill()`, `cell_text()`, `cell_borders()`, and location helpers
- Table-wide options – `tab_options()`, `opt_stylize()`, `opt_table_font()`
