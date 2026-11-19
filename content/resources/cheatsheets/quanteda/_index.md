---
title: quanteda
image: page-1.png
resource_type: cheatsheet
by: community
date: '2017-09-01'
description: Quantitative text analysis in R using corpus management, tokenization, document-feature matrices, text statistics, and text models.
download_url: quanteda.pdf
people:
- Stefan Müller
- Kenneth Benoit
thumbnails:
- page-1.png
- page-2.png
languages:
- R
translations:
- language: French
  lang: fr
  file: quanteda_fr.pdf
  added: 2019-09
  people:
  - Ahmadou Dicko
---

The quanteda package provides a framework for quantitative text analysis in R. Its consistent grammar uses `corpus_*` functions for text management, `tokens_*` for tokenization, `dfm_*` for document-feature matrices, `textstat_*` for statistics, `textmodel_*` for supervised and unsupervised models, and `textplot_*` for visualization.

## What's covered
- General syntax – object-specific prefixes and companion packages (readtext, spacyr, stopwords)
- Create a corpus – `corpus()`, `corpus_subset()`, `corpus_reshape()`, `corpus_segment()`, `docvars()`
- Tokenize texts – `tokens()`, `tokens_compound()`, `tokens_ngrams()`, `tokens_skipgrams()`, `tokens_lookup()` with dictionaries
- Extract features – `dfm()`, `dfm_select()`, `dfm_weight()`, `dfm_group()`, `dfm_compress()`, `fcm()`
- Text statistics – `textstat_frequency()`, `textstat_collocations()`, `textstat_readability()`, `kwic()`
- Text models – `textmodel_nb()` (Naïve Bayes), `textmodel_svm()`, `textmodel_wordscores()`, `textmodel_wordfish()`
- Visualizations – `textplot_wordcloud()` and other `textplot_*` functions
