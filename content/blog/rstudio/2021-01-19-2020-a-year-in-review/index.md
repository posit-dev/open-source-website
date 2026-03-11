---
title: '2020 at RStudio: A Year in Review'
people:
  - Lou Bajuk
date: '2021-01-19'
slug: 2020-a-year-in-review
categories:
  - Company News & Events
tags:
  - Python
  - RStudio
  - RStudio Cloud
  - RStudio Desktop Pro
  - RStudio IDE
  - RStudio Package Manager
  - Connect
description: In this blog post, I take a look back at some of the many announcements, product releases, etc. that RStudio did in 2020. It was an exciting year, despite the challenges that 2020 presented to everyone, and we were pleased to continue to support and deliver value to the R and Python data science community.
resources:
- name:  "calendar"
  src:   "calendar.jpg"
  title: "Calendar flipping to 2021"
blogcategories:
  - Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---

<sup>Photo by<a href="https://unsplash.com/@kellysikkema?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer"> Kelly Sikkema</a> on<a href="https://unsplash.com/s/photos/year-in-review?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer"> Unsplash</a></sup>

We at RStudio are excited to host our first fully virtual conference this week, <a href="/conference/">rstudio::global</a>. We were so pleased to have so many of you join us this week, and while we wish we could see you all in person again, we were happy to have this opportunity to come together with the open source data science community. We will share a recap of the conference in after it concludes this Friday.

Before we dive back into our projects, I thought it would be a good time to look back at what kept us busy in 2020. While the year presented many challenges for everyone, we were pleased to continue to support and deliver value to the R and Python data science community. Below, I list some of the many highlights of the past year. No doubt I have missed a few, but these are some of the things I am particularly proud we were able to accomplish last year.

### RStudio the Company

Our company grew significantly this year, despite the many challenges posed by COVID-19. As part of that growth, we:

-   Started out 2020 with rstudio::conf, with thousands of attendees from around the world, both in person and virtually. You can watch all the <a href="/resources/rstudioconf-2020/">talks from the conference here</a>.
-   Announced that RStudio is now a Public Benefit Corporation, with our open source mission codified into our corporate charter. Check out <a href="https://blog.rstudio.com/2020/01/29/rstudio-pbc/" target="_blank" rel="noopener noreferrer">JJ Allaire's rstudio::conf keynote</a> for the full story. We also wrote about <a href="/about/what-makes-rstudio-different/">What Makes RStudio Different</a>.
-   Were honored to be named a <a href="https://blog.rstudio.com/2020/09/25/forrester-wave/" target="_blank" rel="noopener noreferrer">Strong Performer</a> in the Forrester Wave™: Notebook-Based Predictive Analytics and Machine Learning, Q3 2020.
-   Wrote and spoke about the importance of <a href="https://blog.rstudio.com/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">Serious Data Science</a>, <a href="https://blog.rstudio.com/2020/11/17/an-interview-with-lou-bajuk/" target="_blank" rel="noopener noreferrer">why we focus on a code-based approach</a> to data science, how <a href="https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/" target="_blank" rel="noopener noreferrer">Interoperability</a> helps you leverage your entire analytic ecosystem, and how we provide a single home for <a href="/solutions/r-and-python/">R and Python Data Science</a>.
-   Delivered <a href="/resources/webinars/">several webinars</a>, many featuring our customers and partners, and were privileged to share <a href="/about/customer-stories/">several customer stories</a>, featuring the great work our customers are doing. We were also thrilled and humbled by the <a href="https://www.trustradius.com/products/rstudio/reviews" target="_blank" rel="noopener noreferrer">many great reviews</a> our customers provided on TrustRadius.

### RStudio Products
On the product side, we significantly enhanced the capabilities of both our commercial and open source products. Specifically, we:

-   Created and delivered new releases of the RStudio IDE, making it <a href="https://blog.rstudio.com/2020/05/27/rstudio-1-3-release/" target="_blank" rel="noopener noreferrer">more accessible</a>, as well as delivering <a href="https://blog.rstudio.com/2020/09/30/rstudio-v1-4-preview-visual-markdown-editing/" target="_blank" rel="noopener noreferrer">many other enhancements</a>, including the surprisingly popular <a href="https://blog.rstudio.com/2020/11/04/rstudio-1-4-preview-rainbow-parentheses/" target="_blank" rel="noopener noreferrer">rainbow parentheses</a>. We also greatly expanded capabilities for <a href="https://blog.rstudio.com/2020/10/07/rstudio-v1-4-preview-python-support/" target="_blank" rel="noopener noreferrer">native Python coding in the RStudio IDE</a>, including a Python environment and object explorer.
-   Expanded the capabilities of <a href="/products/connect/">RStudio Connect</a>, our centralized platform for sharing the work data science teams create in R and Python, including support for a full suite of interactive Python applications based on Dash, Bokeh and Streamlit. (See the announcements for <a href="https://blog.rstudio.com/2020/07/14/rstudio-connect-1-8-4/" target="_blank" rel="noopener noreferrer">Connect 1.8.4</a> and <a href="https://blog.rstudio.com/2020/12/16/rstudio-connect-1-8-6-python-update/" target="_blank" rel="noopener noreferrer">1.8.6</a>.) We also added the ability to share Python APIs (via Flask) in <a href="https://blog.rstudio.com/2020/04/02/rstudio-connect-1-8-2/" target="_blank" rel="noopener noreferrer">Connect 1.8.2</a>.
-   Updated <a href="/products/package-manager/">RStudio Package Manager</a>, introducing support for Windows binaries, bioconductor, and beta support for PyPI packages. We also<a href="https://blog.rstudio.com/2020/07/01/announcing-public-package-manager/" target="_blank" rel="noopener noreferrer"> introduced Public Package Manager </a>as a free service.
-   Officially <a href="https://blog.rstudio.com/2020/08/05/rstudio-cloud-announcement/" target="_blank" rel="noopener noreferrer">launched RStudio Cloud</a>, our cloud-based platform for doing, teaching, and learning data science using only a browser--and promised we will always offer a free plan for casual users. We were gratified to <a href="https://blog.rstudio.com/2020/09/17/rstudio-cloud-a-student-perspective/" target="_blank" rel="noopener noreferrer">hear great responses </a>from the many people using RStudio Cloud to teach and learn data science.

### R and Python Packages
RStudio also expanded its wealth of free and open-source packages available to the larger data science community in 2020. Some of the significant development included:

-   <a href="https://blog.rstudio.com/2020/01/29/sparklyr-1-1/" target="_blank" rel="noopener noreferrer">Announcing in January</a> that sparklyr is available on CRAN, enabling R users to scale datasets across computing clusters running Apache Spark. We later <a href="https://blog.rstudio.com/2020/07/16/sparklyr-1-3/" target="_blank" rel="noopener noreferrer">announced support for Apache Avro</a> in sparklyr.
-   <a href="https://blog.rstudio.com/2020/09/29/torch/" target="_blank" rel="noopener noreferrer">Providing native access to Torch</a>, making one of the most widely used deep learning frameworks available to R users.
-   <a href="https://blog.rstudio.com/2020/04/08/great-looking-tables-gt-0-2/" target="_blank" rel="noopener noreferrer">Introducing the gt package</a> (short for "grammar of tables"), to help R users reliably and efficiently create beautiful customized display tables. We also had a great response to our <a href="https://blog.rstudio.com/2020/12/23/winners-of-the-2020-rstudio-table-contest/" target="_blank" rel="noopener noreferrer">RStudio Table contest</a>.

And of course, the tidyverse team was as productive as always this year, releasing (among other things) upgrades to:

- <a href="https://www.tidyverse.org/blog/2020/03/forcats-0-5-0/" target="_blank" rel="noopener noreferrer">forcats</a>,
- <a href="https://www.tidyverse.org/blog/2020/03/ggplot2-3-3-0/" target="_blank" rel="noopener noreferrer">ggplot2</a>,
- <a href="https://www.tidyverse.org/blog/2020/04/tibble-3-0-0/" target="_blank" rel="noopener noreferrer">tibble</a>, and
- <a href="https://www.tidyverse.org/blog/2020/06/dplyr-1-0-0/" target="_blank" rel="noopener noreferrer">dplyr</a>, which received a massive update as part of its official 1.0 release.

There were also significant updates to:

- <a href="https://www.tidyverse.org/blog/2020/09/pkgdown-1-6-0/" target="_blank" rel="noopener noreferrer">pkgdown</a>,
- <a href="https://www.tidyverse.org/blog/2020/10/readr-1-4-0/" target="_blank" rel="noopener noreferrer">readr</a>,
- <a href="https://www.tidyverse.org/blog/2020/10/testthat-3-0-0/" target="_blank" rel="noopener noreferrer">testthat</a>,
- <a href="https://www.tidyverse.org/blog/2020/11/dbplyr-2-0-0/" target="_blank" rel="noopener noreferrer">dbplyr</a>,
- <a href="https://www.tidyverse.org/blog/2020/12/usethis-2-0-0/" target="_blank" rel="noopener noreferrer">usethis</a>, and
- <a href="https://www.tidyverse.org/blog/2020/11/magrittr-2-0-is-here/" target="_blank" rel="noopener noreferrer">magrittr</a>.

The team also <a href="https://www.tidyverse.org/blog/2020/04/tidymodels-org/" target="_blank" rel="noopener noreferrer">launched tidymodels.org</a>, a central location for learning and using the `tidymodels` packages.

Finally, in support of online scientific and technical communication, we <a href="https://blog.rstudio.com/2020/12/07/distill/" target="_blank" rel="noopener noreferrer">introduced the 1.0 version of the distill package</a>, as well as real-time <a href="https://blog.rstudio.com/2020/09/30/rstudio-v1-4-preview-visual-markdown-editing/" target="_blank" rel="noopener noreferrer">visual editing of R Markdown documents</a>. We also introduced <a href="https://blog.rstudio.com/2020/12/21/rmd-news/" target="_blank" rel="noopener noreferrer">many other updates and enhancements</a> to R Markdown.

## To Learn More
2020 was a busy year, and I am sure there are still a dozen things I missed. I know it's difficult to keep up with everything RStudio is doing, but hopefully the links I've included above will help. If you'd like to learn more about any of the professional products, please drop a line to <a href="mailto:sales@rstudio.com">sales@rstudio.com</a>, or book at time talk with us <a href="https://rstudio.chilipiper.com/book/rst-demo" target="_blank" rel="noopener noreferrer">using this link</a>.

If you'd particularly like to learn more about the many ways that RStudio provides a single home for data science teams using R and Python, we encourage you to <a href="https://pages.rstudio.net/RStudio_R_Python.html" target="_blank" rel="noopener noreferrer">register for our upcoming webinar</a> on February 3rd.

Here's to a happy, healthy, and productive 2021 for all of us!

  
  
