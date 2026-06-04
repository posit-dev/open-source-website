---
color: '#FA00C3'
description: Make awesome display tables using Python
github: posit-dev/great-tables
image: great-tables.svg
languages:
- Python
latest_release: '2026-03-02T20:52:39+00:00'
people:
- Rich Iannone
- Michael Chow
- Jules Walzer-Goldfeld
- Isabel Zimmerman
- Carlos Scheidegger
title: Great Tables
topics:
- Best Practices
- Publishing
- Visualization
website: https://posit-dev.github.io/great-tables/

override:
  title: Great Tables

external:  # updated automatically, do not edit
  description: Make awesome display tables using Python
  first_commit: '2022-05-06T20:11:05+00:00'
  forks: 127
  languages:
  - Python
  last_updated: '2026-05-20T08:05:14.879339+00:00'
  latest_release: '2026-03-02T20:52:39+00:00'
  license: MIT
  people:
  - Rich Iannone
  - Michael Chow
  - Jules Walzer-Goldfeld
  - Isabel Zimmerman
  - Carlos Scheidegger
  readme_image: https://posit-dev.github.io/great-tables/assets/GT_logo.svg
  repo: posit-dev/great-tables
  stars: 2658
  title: great-tables
  website: https://posit-dev.github.io/great-tables/
---

Great Tables is a Python package for creating publication-quality tables from Pandas or Polars DataFrames. It provides a composable system of table components (headers, footers, stubs, spanners, column labels) that you can mix and match to build display tables for notebooks, Quarto documents, or HTML/image output.

The package emphasizes simplicity for common tasks while offering power for complex formatting needs. It includes built-in methods for formatting currency, dates, and numbers, along with extensive customization options for styling and layout. The package includes 16 sample datasets for testing and learning, and it's designed specifically for display tables rather than interactive data exploration.

## Try it

{{< pyodide packages="great_tables,polars,pandas" >}}
from great_tables import GT, md
from great_tables.data import countrypops
import polars as pl

pop = (
    pl.from_pandas(countrypops)
    .filter(
        pl.col("country_code_3").is_in(["USA", "BRA", "JPN", "DEU", "IND"]),
        pl.col("year").is_in([2000, 2005, 2010, 2015, 2020])
    )
    .pivot(on="year", index="country_name", values="population")
)

(
    GT(pop, rowname_col="country_name")
    .tab_header(
        title="Population Growth by Country",
        subtitle=md("In millions, *2000-2020*")
    )
    .fmt_number(columns=pop.columns[1:], compact=True, decimals=1)
    .data_color(palette="Blues")
)
{{< /pyodide >}}
