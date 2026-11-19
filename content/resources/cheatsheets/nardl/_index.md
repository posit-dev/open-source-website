---
title: nardl
image: page-1.png
resource_type: cheatsheet
by: community
date: '2018-10-01'
description: Estimate nonlinear cointegrating ARDL models and run bounds tests, serial correlation, and heteroscedasticity diagnostics.
download_url: nardl.pdf
people:
- Taha Zaghdoudi
thumbnails:
- page-1.png
languages:
- R
---

The nardl package fits nonlinear autoregressive distributed lag (NARDL) cointegration models in R, supporting automatic or fixed lag selection via information criteria. It provides Cusum and CusumQ stability plots, Pesaran-Shin-Smith bounds tests, serial correlation tests, and dynamic multiplier plots for asymmetric long-run relationships.

## What's covered
- Specifying the model – `nardl()` with fixed (`p`, `q`) or automatic (`maxlags = TRUE`) lag selection
- Cusum and CusumQ plot – parameter stability visualization with `graph = TRUE`
- Cointegration bounds test – `pssbounds()` with Pesaran, Shin & Smith (2001) critical values
- LM test for serial correlation – `bp2()` Breusch-Pagan test
- Lagrange multiplier test – `ArchTest()` for ARCH conditional heteroscedasticity (Engle 1982)
- Dynamic multipliers plot – `plotmplier()` for short- and long-run multiplier visualization
