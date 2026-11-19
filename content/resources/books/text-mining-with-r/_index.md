---
title: Text Mining with R
subtitle: A Tidy Approach
date: '2017-06-01'
description: Analyze text by treating it as tidy data with the tidytext package, covering sentiment analysis, tf-idf, n-grams, word networks, and topic modeling, with several case studies.
image: cover.jpg
color: '#B4293E'
resource_type: book
edition: 1
publisher: O'Reilly Media
isbn: '9781491981658'
pages: 191
people:
- Julia Silge
- David Robinson
website: https://www.tidytextmining.com/
read_url: https://www.tidytextmining.com/
buy_url: https://www.oreilly.com/library/view/text-mining-with/9781491981641/
github: juliasilge/tidy-text-mining
software:
- dplyr
- ggplot2
languages:
- R
topics:
- Data Wrangling
---

Much of today's data is unstructured text, which can be hard to analyze with the usual data wrangling and visualization tools.
Julia Silge and David Robinson created the `tidytext` package to apply tidy data principles to text, treating it as data frames of individual words so that it can be manipulated, summarized, and visualized with familiar tools like `dplyr` and `tidyr`.

This book introduces text mining with `tidytext` and related tidy tools in R.
The package's functions are simple, so the focus is on applications: practical code examples work through real text from literature, news, and social media.
It is a good fit for analysts and data scientists who are comfortable with tidy data tools and want to fold natural language processing into workflows they already use.

You will learn how to:

- Convert text into the tidy text format with `unnest_tokens()`
- Use sentiment analysis to measure the emotional content of text
- Identify the most important terms in a document with tf-idf
- Explore relationships between words with n-grams, `ggraph`, and `widyr`
- Convert between tidy text and document-term matrices or corpus objects from `tm` and `quanteda`
- Use topic modeling to group documents into natural clusters
- Apply these methods in case studies on Twitter archives, NASA metadata, and Usenet messages

The full book is free to read online.
