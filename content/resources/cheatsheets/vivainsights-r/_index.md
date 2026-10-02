---
title: vivainsights (R)
image: page-1.png
resource_type: cheatsheet
by: community
date: '2024-11-01'
description: Analyze and visualize Microsoft Viva Insights data using the vivainsights R package.
download_url: vivainsights_r.pdf
people:
- Martin Chan
thumbnails:
- page-1.png
- page-2.png
languages:
- R
source_files:
- file: vivainsights-r-py.pptx
  format: PowerPoint
---

The vivainsights R package provides functions for importing, validating, and visualizing
Microsoft Viva Insights query data. Metric analysis functions combine a prefix (e.g., `collab_`,
`email_`) with a plot type suffix (e.g., `_summary`, `_dist`) for rapid exploratory analysis.

## What's covered
- Basics and setup – installation, companion tidyverse workflow
- Data import and export – `import_query`, `export`
- Inbuilt datasets – `pq_data`, `mt_data`, `p2p_data`, `p2p_data_sim`
- Data validation – `validation_report`, `hrvar_count`, `identify_holidayweeks`, `identify_nkw`, `identify_outlier`
- Basic analysis – metric prefix functions (`*_summary`, `*_dist`, `*_fizz`, `*_line`, `*_trend`, `*_rank`)
- Exploratory analysis – `keymetrics_scan`, `create_rank`
- Distribution – `create_boxplot`, `create_density`, `create_hist`
- Flexible analysis – `create_bar`, `create_fizz`, `create_scatter`, `create_bubble`, `create_dist`, `create_inc`
- Flexible analysis over time – `create_line`, `create_period_scatter`, `create_trend`, `create_tracking`
- Network analysis – `network_g2g`, `network_p2p`, `network_summary`
- Other analysis – `create_IV`, `create_lorenz`, `maxmin`
- Helper functions – `anonymise`, `totals_bind`, `tstamp`, `wrap_text`
