---
title: 'R vs. Python: What''s the best language for Data Science?'
description: We will briefly examine the debates over R vs. Python, and then share
people:
  - Lou Bajuk
date: '2019-12-17'
slug: r-vs-python-what-s-the-best-for-language-for-data-science
categories:
- News
- Data Science Leadership
tags:
- Python
- R
blogcategories:
- Data Science Leadership
- Company News and Events
events: blog
ported_from: rstudio
port_status: raw
---

This is a question that we at RStudio hear a lot. With the tremendous growth in both languages, and in the application of data science in general, there is a lot of interest and debate over which is the “best” language for data science. 

![R and Python](https://rstudio.github.io/reticulate/images/reticulated_python.png)

From our founding, RStudio has been dedicated to a couple of key ideas: that it’s better for everyone if the tools used for data science are free and open, and that we love and support coding as the most powerful path to tackle data science. Coding gives current and aspiring data scientists superpowers to tackle the most complex problems, because code is flexible, reusable, inspectable, and reproducible. 

With that in mind, at RStudio we don’t judge which language you prefer. We just care that you feel enabled to do great data science. As RStudio’s Chief Data Scientist Hadley Wickham expressed in a [recent interview with Dan Kopf](https://qz.com/1661487/hadley-wickham-on-the-future-of-r-python-and-the-tidyverse/): *Use whatever makes you happy.*

We will talk more about the benefits of coding for data science in a future blog post, but in this post we will briefly examine the debates over R vs. Python, and then share why we believe R and Python can, should and do work beautifully together. 

## R or Python for Data Science?

There is a lot of heated discussion over the topic, but there are some  great, thoughtful articles as well. Some suggest Python is preferable as a general-purpose programming language, while others suggest data science is better served by a dedicated language and toolchain. The origins and development arcs of the two languages are compared and contrasted, often to support differing conclusions. 

For individual data scientists, some common points to consider:

* Python is a great general programming language, with many libraries dedicated to data science. 
* Many (if not most) general introductory programming courses start teaching with Python now.
* Python is the go-to language for many ETL and Machine Learning workflows. 
* Many (if not most) introductory courses to statistics and data science teach R now.
* R has become the world's largest repository of statistical knowledge with reference implementations for thousands, if not tens of thousands, of algorithms that have been vetted by experts. The documentation for many R packages includes links to the primary literature on the subject.
* R has a very low barrier to entry for doing exploratory analysis, and converting that work into a great report, dashboard, or API.
* R with RStudio is often considered the best place to do exploratory data analysis. 
 
For organizations with Data Science teams, some additional points to keep in mind:

* For some organizations, Python is easier to deploy, integrate and scale than R, because Python tooling already exists within the organization. On the other hand, we at RStudio have worked with thousands of data teams successfully solving these problems with our open-source and [professional products](https://rstudio.com/products/team/), including in multi-language environments. 
* R has a great community of supportive data scientists from diverse backgrounds. For example, [R-Ladies](https://rladies.org/about-us/) is a global organization dedicated to promoting gender diversity in the R Community.   
* Most interfaces for novel machine learning tools are first written and supported in Python, while many new methods in statistics are first written in R. 
* Trying to enforce one language to the exclusion of the other, perhaps out of vague fears of complexity or costs to support both, risks excluding a huge potential pool of Data Scientist candidates either way. 
* Advice on building Data Science teams often stresses the importance of having a diverse team bringing a variety of viewpoints and complementary skills to the table, to make it more likely to efficiently find the “best” solution for a given problem. In this vein, R users tend to come from a much more diverse range of domain expertise (ecology, economics, psychology, bioinformatics, policy analysis, etc.). 
 
Thus, the focus on “R or Python?” risks missing the advantages that having both can bring to individual data scientists and data science teams. Because of this, many of these articles end up with fairly nuanced conclusions, along the lines of “You need both” or “It depends.” A great example of this view can be found in the above-referenced interview with Hadley Wickham:

*Generally, there are a lot of people who talk about R versus Python like it’s a war that either R or Python is going to win. I think that is not helpful because it is not actually a battle. These things exist independently and are both awesome in different ways.*

## R and Python for Data Science!

And so the reality is that both languages are valuable, and both are here to stay. This is borne out by our experience. In talking to our customers, we’ve found that many Data Science teams today are bilingual, leveraging both R and Python in their work. In the spirit of Hadley’s *Use whatever makes you happy*, we’ve worked to make this sometime-rocky relationship a much happier one. We give individual Data Scientists, and the Data Science teams and organizations they are a part of, a smoother path to using both languages side by side, and to address the concerns around complexity or cost that IT teams might have about supporting both. 

For example:

* Our open source [reticulate](https://rstudio.github.io/reticulate/) package and the RStudio IDE makes it easy to combine R and Python in a single data science project. 
* Our [professional products](https://rstudio.com/products/team/) make it easier to manage and collaborate across bilingual Data Science environments. E.g., RStudio Server Pro launches and manages Jupyter Notebooks and JupyterLab, and RStudio Connect makes it easy to share Jupyter Notebooks with stakeholders, alongside your work in R and your mixed R and Python projects.
* As a longer term investment in improving cross-language collaboration, we are incubating Ursa Labs, providing operational support and infrastructure for this industry-funded development group specializing in open source data science tools. Wes McKinney, the author of the pandas package for Python is the Director, and talks a lot  with Hadley Wickham. The [goal of the Ursa Labs project](https://blog.rstudio.com/2018/04/19/arrow-and-beyond/) is nothing less than creating a modern data science runtime environment that takes advantage of the computational advances of the last 20 years, and can be used from many languages, including R and Python. 

To learn more about how RStudio supports using R and Python on the same Data Science teams, check out our [R and Python Love Story](https://rstudio.com/solutions/r-and-python/), where we provide information and resources for Data Scientists, Data Science Leaders, and DevOps/IT Leaders grappling with mixed R & Python environments. Or, you check out our recent [R and Python Love Story Webinar](https://resources.rstudio.com/webinars/r-and-python-a-data-science-love-story), where you can watch the recording or download the slides. In future blog posts, we will also talk more about what we’ve seen in real life Data Science teams using R and Python side by side. 


