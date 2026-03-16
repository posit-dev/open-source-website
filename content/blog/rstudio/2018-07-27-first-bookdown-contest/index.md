---
title: Announcing the 1st Bookdown Contest
people:
  - Yihui Xie
date: '2018-07-27'
slug: first-bookdown-contest
categories:
- News
tags:
- bookdown
- R Markdown
- contest
blogcategories:
- Company News and Events
- Open Source
events: blog
ported_from: rstudio
port_status: in-progress
---


Since the release of [the **bookdown** package](https://github.com/rstudio/bookdown) in 2016, there have been a large number of books written and published with **bookdown**. Currently there are about 200 books (including tutorials and notes) listed on [bookdown.org](https://bookdown.org) alone! We have also heard about other applications of **bookdown** based on custom templates (e.g., dissertations).

As popular as **bookdown** is becoming, especially with teachers, researchers, and students, we know it can take a lot of time to tailor **bookdown** to meet the special typesetting requirements of your institution or publisher. As it is today, future graduate students will have to spend many hours reinventing a thesis template, instead of focusing on writing content in R Markdown! Fortunately, we are sure that there are already elegant and reusable **bookdown** applications, which would greatly benefit future users.

With that in mind, we are happy to announce the first contest to recognize outstanding **bookdown** applications!

![The first bookdown contest](https://user-images.githubusercontent.com/163582/43284090-651365f8-90e0-11e8-8092-a9b10775fda0.png)

## Criteria

There are no hard judging criteria for this contest, but in general, we'd prefer these types of applications:

- Publicly and freely accessible (both source documents and the output). If the full source and output cannot be shared publicly, we expect at least a full demo that can be shared (the demo could contain only placeholder content).
- Not tightly tied to a particular output format, which means you should use as fewer raw LaTeX commands or HTML tags as possible in the body of the book (using the `includes` options is totally fine, e.g., including custom LaTeX content in the preamble). An exception can be made for dissertations, since they are typically in the PDF format.
- Has some minimal examples or clear instructions for other users to easily create similar applications.
- Uses new output formats based on **bookdown**'s built-in output formats (such as `bookdown::html_book` or `bookdown::pdf_document2`).
- Has creative and elegant styling for HTML and/or PDF output based on either the default templates in **bookdown** or completely new custom templates.

We'd also like to see non-English applications, such as books written in CJK (Chinese, Japanese, Korean), right-to-left, or other languages, since there are additional challenges in typesetting with these languages.

Note that the applications do not have to be technical books or even books at all. They could be novels, diaries, collections of poems/essays, course notes, or data analysis reports.

## Awards

Honorable Mention Prizes (ten):

- One signed copy of "[bookdown: Authoring Books and Technical Documents with R Markdown](https://www.crcpress.com/product/isbn/9781138700109)".
- One RStudio t-shirt.

Runner Up Prizes (two): All awards above, plus

- All hex/RStudio stickers we can find.
- Any number of [RStudio t-shirts and mugs](https://www.rstudio.com/about/gear/) (within $200).

Grand Prize (one): All awards above, with three more signed books related to R Markdown

- [R Markdown: The Definitive Guide](https://www.crcpress.com/p/book/9781138359338)
- [Dynamic Documents with knitr, 2nd edition](https://www.crcpress.com/p/book/9781498716963)
- [blogdown: Creating Websites with R Markdown](https://www.crcpress.com/p/book/9780815363729)

The names and work of all winners will be highlighted in a gallery on the [bookdown.org](https://bookdown.org) website and we will announce them on RStudio’s social platforms, including [community.rstudio.com](https://community.rstudio.com) (unless the winner prefers not to be mentioned).

Of course, the main reward is knowing that you’ve helped future writers!

## Submission

To participate this contest, please follow the link http://rstd.io/bookdown-contest to create a new post in RStudio Community (you will be asked to sign up if you don't have an account). The post title should start with "Bookdown contest submission:", followed by a short title to describe your application (e.g., "a PhD thesis template for Iowa State"). The post may describe features and highlights of the application, include screenshots and links to live examples and source repositories, and briefly explain key technical details (how the customization or extension was achieved). 

There is no limit on the number of entries one participant can submit. Please submit as many as you wish!

The deadline for the submission is October 1st, 2018. You are welcome to either submit your existing **bookdown** applications (even like a PhD thesis you wrote two years ago), or create one in two months! We will announce winners and their submissions in this blog, RStudio Community, and also on Twitter before Oct 15th, 2018.

I (Yihui) will be the main judge this year. Winners of this year will be invited to serve as judges next year. I'll consider both the above criteria and the feedback/reaction of other users in the submission posts in RStudio Community (such as the number of likes that a post receives).

Looking forward to your submissions!

