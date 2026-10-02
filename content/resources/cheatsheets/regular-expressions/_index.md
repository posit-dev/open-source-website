---
title: Regular expressions
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-07-01'
description: Reference for regex syntax and base R and stringr functions for detecting, locating, extracting, and replacing string patterns.
download_url: regex.pdf
people:
- Ian Kopacka
thumbnails:
- page-1.png
software:
- stringr
languages:
- R
source_files:
- file: regex.pptx
  format: PowerPoint
translations:
- language: French
  lang: fr
  file: regex_fr.pdf
  added: 2019-08
  people:
  - Ahmadou Dicko
  source: regex_fr.pptx
- language: Turkish
  lang: tr
  file: regex_tr.pdf
  updated: 2016-09
  people:
  - Zeki Özen
---

This cheat sheet covers regular expression syntax for use in R, including character classes, anchors, quantifiers, and lookaheads, alongside the main base R functions (`grep()`, `grepl()`, `sub()`, `gsub()`, `regexpr()`) and their stringr equivalents (`str_detect()`, `str_extract()`, `str_replace()`). It also explains POSIX classes, PCRE-only features, greedy versus lazy matching, and case-insensitive mode.

## What's covered
- Character classes – POSIX classes (`[[:digit:]]`, `[[:alpha:]]`), `\\d`, `\\w`, `\\s` and complements
- Special characters – escape sequences `\n`, `\t`, `\r`, `\v`, `\f`
- Anchors and word boundaries – `^`, `$`, `\\b`, `\\B`, `\\<`, `\\>`
- Quantifiers – `*`, `+`, `?`, `{n}`, `{n,m}`; greedy vs. lazy with `?` and `(?U)`
- Grouping and alternation – `(…)`, `|`, `[…]`, `[^…]`, back references
- Lookahead and lookbehind – `(?=)`, `(?!)`, `(?<=)`, `(?<!)` (PCRE, requires `perl = TRUE`)
- Detect and locate – `grep()`, `grepl()`, `regexpr()`, `gregexpr()`, `str_detect()`, `str_locate()`
- Extract and replace – `regmatches()`, `str_extract()`, `str_match()`, `sub()`, `gsub()`, `str_replace()`
