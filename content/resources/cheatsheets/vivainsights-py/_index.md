---
title: vivainsights (Python)
image: page-1.png
resource_type: cheatsheet
by: community
date: '2025-01-01'
description: Analyze and visualize Microsoft Viva Insights data using the vivainsights Python package.
download_url: vivainsights_py.pdf
people:
- Martin Chan
thumbnails:
- page-1.png
languages:
- Python
---

The vivainsights Python package provides tools for importing, validating, and visualizing
Microsoft Viva Insights query data. It mirrors the R package's design with functions for
flexible metric analysis, network visualization, and inequality measurement.

## What's covered
- Basics and setup – installation via pip and example workflow
- Data import and export – `import_query`, `export`
- Inbuilt datasets – `load_pq_data`, `load_mt_data`, `load_g2g_data`, `p2p_data_sim`
- Data validation – `identify_holidayweeks`, `identify_inactiveweeks`, `identify_nkw`
- Flexible analysis – `create_bar`, `create_boxplot`, `create_inc`, `create_line`, `create_sankey`
- Network analysis – `network_g2g`, `network_p2p`
- Exploratory analysis – `keymetrics_scan`, `create_rank`
- Other analysis – `create_IV`, `p_test`, `compute_gini`, `create_lorenz`
