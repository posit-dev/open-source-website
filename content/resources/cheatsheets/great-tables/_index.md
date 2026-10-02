---
title: Great Tables
image: page-1.png
resource_type: cheatsheet
by: posit
date: '2026-08-01'
description: Make display tables from Python DataFrames (Polars, Pandas, and Arrow) with formatting, styling, and output to HTML or LaTeX.
download_url: great-tables.pdf
people:
- Mine Çetinkaya-Rundel
- Rich Iannone
thumbnails:
- page-1.png
software:
- great-tables
languages:
- Python
source_files:
- file: great-tables.key
  format: Keynote
---

Great Tables is a Python package for building display tables from Polars, Pandas, or Arrow DataFrames. It mirrors the gt API closely and is designed for use in notebooks and Quarto documents, with options to save table images or export HTML and LaTeX.

## What's covered
- Introduction – package overview and sample datasets
- Creating a GT Table – `GT()`, basic workflow, and Polars style property
- Adding Structure – `tab_header()`, `tab_source_note()`, stub and row groups, column spanners
- Formatting Data Values – `fmt_number()`, `fmt_integer()`, `fmt_percent()`, `fmt_scientific()`, `fmt_date()`, `fmt_time()`, `fmt_datetime()`, `fmt_image()`, `fmt_icon()`, `fmt_flag()`
- Colorizing Body Cells – `data_color()` with domain, palette, and NA color options
- Adding Nanoplots – `fmt_nanoplot()` for inline sparklines
- Styling the Table – `tab_style()` with `style.fill()`, `style.text()`, `style.borders()`, and `loc.*` location helpers
- Table-wide options – `tab_options()`, `opt_stylize()`, `opt_table_font()`
