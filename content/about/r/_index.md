---
title: "Our R work"
layout: single
---

Whether you've been with us since the first version of RStudio or you're just starting your first script, we're here to support you.

At Posit, we believe R is one of the most powerful languages for statistical communication and data exploration. Our commitment to the R community includes the maintenance of hundreds of open-source packages designed to ensure reproducible research and scalable statistical computing.

\[[Browse all R packages](/software/?lang=R&filters=show) \-\>\] \[[Explore learning resources](/resources) \-\>\]

## Choose your own adventuRe

{{< columns >}}

### Work with tools for data science

We recommend starting with the tidyverse, a collection of packages designed for data science that share an underlying philosophy and grammar. Use these tools to clean, transform, and visualize your data with consistent, readable code.

---

{{< insert-items cols="2" format="tile" hide-badge=true >}}
- software/ggplot2
- software/dplyr
- software/tidyr
- software/purrr
- software/readr
- software/tidyverse
{{< /insert-items>}}

{{< /columns >}}


\[Visit [tidyverse.org](http://tidyverse.org)\] \[[Read R for Data Science](https://r4ds.hadley.nz/) \-\>\]

<br>

{{< columns >}}

### Deepen your expertise

Already comfortable with dplyr and ggplot2? Take your work to the next level.

---

{{< insert-items cols="2" format="tile" hide-badge=true >}}
- software/shiny
- software/quarto
- software/rvest
- software/gt
- software/tidymodels
- software/plumber
{{< /insert-items>}}

{{< /columns >}}

\[Visit [tidymodels.org](https://tidymodels.org) \] \[Visit [shiny.org](https://shiny.posit.co/)\] \[Visit [quarto.org](https://quarto.org)\]

<br>

{{< columns >}}

### Develop your own packages

Ready to create your own R package? We maintain foundational tools used by thousands of R users to create and distribute packages.

---

{{< insert-items cols="2" format="tile" hide-badge=true >}}
- software/devtools
- software/usethis
- software/roxygen2
- software/testthat
- software/pkgdown
- software/cli
{{< /insert-items>}}

{{< /columns >}}

\[[Read R Packages book](https://r-pkgs.org/) \-\>\]

<br>

{{< columns >}}

### Enhance your workflows

Streamline your R development experience with modern tools for package management, version control, and code editing.

---

{{< insert-items cols="2" format="tile" hide-badge=true >}}
- software/pak
- software/rig
- software/air
- software/renv
{{< /insert-items>}}

{{< /columns >}}

## Read the latest on the blog

Stay up to date with the latest R developments, package releases, and best practices from the Posit team.

{{< query-items path="/blog/.*" filter=`{"contains_any": [{"var": "languages"}, ["R"]]}` sort-by="date" limit="3" cols="3" format="card" >}}

\[[Read R blog posts](/blog) \-\>\]

## Join us at an upcoming event

Learn about the latest developments in the R ecosystem through our workshops and conferences. We have hex stickers\!

{{< query-items path="^/events/.*" filter=`{"and": [{"contains_any": [{"var": "languages"}, ["R"]]}, {">": [{"var": "start_date"}, "$today"]}]}` sort-by="start_date" sort-direction="ascending" limit="3" cols="3" format="card" hide-badge=true >}}

\[[View all events](/events) \-\>\]
