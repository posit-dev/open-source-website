---
title: Time Series
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-10-01'
description: Simulate, filter, and forecast ARMA time series models using base R functions.
download_url: time-series.pdf
people:
- Yunjun Xia
- Shuyu Huang
thumbnails:
- page-1.png
languages:
- R
source_files:
- file: time-series.key
  format: Keynote
---

This cheat sheet covers the key steps of time series analysis in R using base functions:
plotting time series, applying linear and differencing filters, fitting AR and ARMA models,
and forecasting future observations with confidence intervals.

## What's covered
- Plot time series – `tsplot`, `plot(ts(...))`, `ts.plot`
- Linear filter – `filter` with convolution method
- Differencing filter – `diff` with lag and differences arguments
- Simulation – `arima.sim` for AR(p), MA(q), and ARMA(p,q) models
- Auto-correlation – ACF with `acf`, PACF with `pacf`
- Parameter estimation – `ar` for AR models, `arima` for ARMA models
- Model comparison – `AICc` for comparing fitted models
- Forecasting – `predict` and plotting predicted values with confidence intervals
