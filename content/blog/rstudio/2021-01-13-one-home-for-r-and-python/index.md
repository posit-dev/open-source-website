---
title: 'RStudio: A Single Home for R and Python Data Science'
people:
  - Lou Bajuk
date: '2021-01-13'
slug: one-home-for-r-and-python
categories:
  - Data Science Leadership
tags:
  - Python
  - R
description: "Over the past year, RStudio has invested in making our pro and open source offerings the best common home for both R- and Python-based Data Science. In this blog post, we explain why we support both Python and R, review these recent features, and encourage readers to attend our upcoming webinar."
resources:
- name: "randpython"
  src: "rstudioandpython-15.png"
  title: "R and Python logo"
blogcategories:
- Data Science Leadership
events: blog
image: thumbnail.png
ported_from: rstudio
port_status: in-progress
---

## Why R AND Python?

From the very beginning, two key ideas have driven the work we do at RStudio:

-   **It's better for everyone if the tools used for data science are free and open.** This enhances the production and consumption of knowledge and facilitates collaboration and reproducible research in science, education and industry.
-   **Coding is the most powerful and efficient path to tackle complex, real-world data science challenges.** It gives data scientists superpowers to tackle the hardest problems because code is flexible, reusable, inspectable, and reproducible.

Some data scientists, and even some organizations, believe they have to pick between R or Python. However, this turns out to be a false choice. In talking to our many customers and others in the data science field, as well as in <a href="https://blog.rstudio.com/2020/10/30/why-rstudio-supports-python/" target="_blank" rel="noopener noreferrer">the surveys we've done of the data science community</a>, we've seen that many data science teams today are bilingual, leveraging both R and Python in their work. And while both languages have unique strengths, these teams frequently struggle to use them together.

## Common Objections to using R and Python Together

We've heard three common criticisms from data science teams about using R and Python together:

1.  Data science leaders are often concerned that multilingual teams will have a harder time collaborating and sharing work than a team standardized on one language.
2.  Individual data scientists may worry that using two languages together will incur a higher cost of project organization and maintenance.
3.  IT organizations are often concerned that enabling two languages will mean doubling their effort, requiring they maintain, manage, and scale separate environments for R and Python.

Contrary to these concerns, in talking with many data science teams, we've found that:

-   Modern tooling allows R and Python programmers to seamlessly share and build off of one another. Additionally, data science team leads find it easier to hire and recruit talent when they are able to reach into both R and Python communities.
-   Many data scientists find that combining R and Python allows them to use each language for their best strengths, and improvements in data science tools like RStudio eliminate additional overhead.
-   IT organizations find that common infrastructure and best practices can support both languages, enabling all the benefits without additional cost. One example of this common infrastructure is <a href="https://rstudio.com/products/team/" target="_blank" rel="noopener noreferrer">RStudio Team</a>, a single centralized infrastructure for bilingual teams using R and Python.

As you can see, many of the potential concerns of using two languages are addressed through better tooling. In line with our ongoing mission to support the open source data science ecosystem, we've invested heavily in creating the best platform for data science using both R AND Python. This effort includes many features in the products that comprise RStudio Team. We have also made significant investments in our open source offerings to make it easier than ever to combine R and Python in a single data science project.

## New Python Features in RStudio products

In our open source products, we improved and invested in a number of different features over the past year, including:

-   <a href="https://rstudio.github.io/reticulate/" target="_blank" rel="noopener noreferrer">Continuing to invest in the reticulate package</a> to make it easy for R users to access Python capabilities.
-   <a href="https://blog.rstudio.com/2020/09/29/torch/" target="_blank" rel="noopener noreferrer">Providing native access from R to `torch`</a>, one of the most widely used deep learning frameworks.
-   <a href="https://ursalabs.org/" target="_blank" rel="noopener noreferrer">Investing in Ursa Labs</a> for the development of cross language capabilities.
-   <a href="https://blog.rstudio.com/2020/10/07/rstudio-v1-4-preview-python-support/" target="_blank" rel="noopener noreferrer">Expanding capabilities for native Python coding in the RStudio IDE</a>, including a Python environment and object explorer.

In <a href="https://rstudio.com/products/rstudio-server-pro/" target="_blank" rel="noopener noreferrer">RStudio Server Pro</a>, which provides collaboration, centralized management, and security for data science teams developing in R and Python, we've <a href="https://blog.rstudio.com/2020/11/16/rstudio-1-4-preview-server-pro/" target="_blank" rel="noopener noreferrer">added beta support for the VSCode IDE</a>. This work is in addition to our existing support for Jupyter Notebooks and JupyterLab. These enhancements make RStudio Server Pro a true workbench for open source data science.

<a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a> provides a centralized platform where data science teams can operationalize the works they create in R and Python. We've solved the same challenges for Python users that have made Connect so popular with R users including:

-   <a href="https://blog.rstudio.com/2020/01/22/rstudio-connect-1-8-0/#python-support" target="_blank" rel="noopener noreferrer">Publishing enhancements</a> in Connect 1.8.0 that make it easier to share Jupyter Notebooks and mixed R and Python content.
-   Support for Dash, Bokeh and Streamlit, allowing users to share a full suite of Python applications. See the announcements for <a href="https://blog.rstudio.com/2020/07/14/rstudio-connect-1-8-4/" target="_blank" rel="noopener noreferrer">Connect 1.8.4</a> and <a href="https://blog.rstudio.com/2020/12/16/rstudio-connect-1-8-6-python-update/" target="_blank" rel="noopener noreferrer">1.8.6</a> for more details.
-   The ability to use Flask to share Python APIs in <a href="https://blog.rstudio.com/2020/04/02/rstudio-connect-1-8-2/" target="_blank" rel="noopener noreferrer">Connect 1.8.2</a>.

Finally, in <a href="https://rstudio.com/products/package-manager/" target="_blank" rel="noopener noreferrer">RStudio Package Manager</a>, which helps organize, manage and centralize packages across a team or an entire organization, we recently <a href="https://blog.rstudio.com/2020/12/07/package-manager-1-2-0/" target="_blank" rel="noopener noreferrer">added beta support for PyPI</a>, giving users access to full documentation, automatic syncs, and historic snapshots of Python packages.

## To Learn More

If you'd like to learn more about the many ways that RStudio provides a single home for teams using both R and Python, we encourage you to <a href="https://pages.rstudio.net/RStudio_R_Python.html" target="_blank" rel="noopener noreferrer">register for our upcoming webinar</a> on February 3rd and explore the information at <a href="https://rstudio.com/solutions/r-and-python/" target="_blank" rel="noopener noreferrer">R & Python: A Love Story.</a>

We've also discussed R & Python in several previous blog posts, including:

-   <a href="https://blog.rstudio.com/2020/10/30/why-rstudio-supports-python/" target="_blank" rel="noopener noreferrer">Why RStudio supports Python</a>, which reviewed survey data from the data science community about the use of R and Python for data science.
-   <a href="https://blog.rstudio.com/2020/09/10/dispelling-r-and-python-myths-qanda/" target="_blank" rel="noopener noreferrer">Debunking R and Python Myths</a>, which answered questions from a recent joint webinar with our partner, Lander Analytics.
-   <a href="https://blog.rstudio.com/2020/08/13/how-to-deliver-maximum-value-using-r-python/" target="_blank" rel="noopener noreferrer">Delivering Maximum value using R and Python</a>, which provided multilingual best practices from Dan Chen of Lander Analytics.
-   <a href="https://blog.rstudio.com/2020/07/28/practical-interoperability/" target="_blank" rel="noopener noreferrer">Wild-caught R and Python applications</a>, which highlighted several bilingual applications suggested by the data science community.
-   <a href="https://blog.rstudio.com/2020/11/17/an-interview-with-lou-bajuk/" target="_blank" rel="noopener noreferrer">Why RStudio focuses on code-based data science</a>, which recapped a recent podcast featuring RStudio's Lou Bajuk and the Outcast's Michael Lippis.
