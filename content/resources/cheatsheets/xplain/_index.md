---
title: xplain
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-05-01'
description: Write XML-based interpretation texts for statistical functions that adapt to the user's actual results.
download_url: xplain.pdf
people:
- Joachim Zuckarelli
thumbnails:
- page-1.png
languages:
- R
---

xplain lets analysts write XML files containing explanation and interpretation texts for R
statistical functions, with embedded R code that reacts to the user's actual output values.
Explanations can be layered by language and complexity level, and can iterate over elements
of a function's return object.

## What's covered
- Purpose and application – wrapping functions with adaptive contextual explanations
- xplain XML structure – `<xplain>`, `<package>`, `<function>`, `<result>`, `<title>`, `<text>` elements
- Main attributes – `name`, `lang`, `level`
- Attribute inheritance and necessity
- Including R code – `!%% ... %%!` delimiter tags with access to the return object via `@` and `##`
- Using placeholders – `<define>` elements and `!** ... **!` tags
- Iterating through return objects – `foreach` attribute for matrices, vectors, and lists
- Calling `xplain` – direct call and wrapper function using `xplain.getcall`
