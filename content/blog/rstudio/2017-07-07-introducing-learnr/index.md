---
title: Introducing learnr
description: "Introducing learnr: create interactive R tutorials with exercises, quizzes, and videos."
auto-description: true
people:
  - Garrett Grolemund
date: '2017-07-11'
categories:
  - Publishing
tags:
  - Shiny
  - Tutorial
  - Packages
  - R Markdown
  - RStudio
slug: introducing-learnr
blogcategories:
  - Products and Technology
  - Open Source
ported_from: rstudio
port_status: in-progress
software: ["shiny-r"]
languages: ["R"]
ported_categories:
  - Packages
  - R Markdown
---


We're pleased to introduce the [learnr](https://rstudio.github.io/learnr/) package, now available on CRAN. The learnr package makes it easy to turn any R Markdown document into an interactive tutorial. Tutorials consist of content along with interactive components for checking and reinforcing understanding. Tutorials can include any or all of the following:

  * Narrative, figures, illustrations, and equations.

  * Code exercises (R code chunks that users can edit and execute directly).

  * Multiple choice quizzes.

  * Videos (supported services include YouTube and Vimeo).

  * Interactive Shiny components.

[![learnr-blog-1](https://rstudioblog.files.wordpress.com/2017/06/learnr-blog-1.png)](https://tutorials.shinyapps.io/04-Programming-Basics/)

Each learnr tutorial is a Shiny interactive document, which means that tutorials can be deployed all of the same ways that Shiny applications can, including locally on an end-user’s machine, on a Shiny or RStudio Connect Server, or on a hosting service like [shinyapps.io](http://shinyapps.io).

### Getting Started

To create a learnr tutorial, install the learnr package with

```r
install.packages("learnr")
```

Then select the Interactive Tutorial template from the **New R Markdown** dialog in the RStudio IDE (v1.0.136 or later).

![learnr-blog-2](https://rstudioblog.files.wordpress.com/2017/06/learnr-blog-2.png)

### Exercises

Exercises are interactive R code chunks that allow readers to directly execute R code and see it's results:

To add an exercise, add `exercise = TRUE` to the chunk options of an R Markdown code chunk. R Markdown will preload the chunk with the code that you supply.

    ```r ex1, exercise = TRUE
    head(mtcars, n = 5)
    ```

becomes

![learnr-blog-3](https://rstudioblog.files.wordpress.com/2017/06/learnr-blog-3.png)

Exercises can include hints or solutions as well as custom checking code to provide feedback on user answers. The [learnr Exercises page](https://rstudio.github.io/learnr/exercises.html) includes a more in depth discussion of exercises and their various available options and behaviors.

### Questions

You can include one or more [multiple-choice quiz questions](https://rstudio.github.io/learnr/questions.html) within a tutorial to help verify that readers understand the concepts presented. Questions can have a single or multiple correct answers.

Include a question by calling the `question()` function within an R code chunk:

    ```r letter-a, echo=FALSE
    question("What number is the letter A in the English alphabet?",
      answer("8"),
      answer("14"),
      answer("1", correct = TRUE),
      answer("23")
    )
    ```

![learnr-blog-4](https://rstudioblog.files.wordpress.com/2017/06/learnr-blog-4.png)

### Videos

You can include videos published on either YouTube or Vimeo within a tutorial using the standard markdown image syntax. Note that any valid YouTube or Vimeo URL will work. For example, the following are all valid examples of video embedding:

    ![](https://youtu.be/zNzZ1PfUDNk)
    ![](https://www.youtube.com/watch?v=zNzZ1PfUDNk)

    ![](https://vimeo.com/142172484)
    ![](https://player.vimeo.com/video/142172484)

### Code checking

learnr works with external code checking packages to let you evaluate student answers and provide targeted, automated feedback, like the message below.

![learnr-blog-5](https://rstudioblog.files.wordpress.com/2017/06/learnr-blog-5.png)

You can use any package that provides a learnr compatible [checker function](https://rstudio.github.io/learnr/exercises.html#exercise_checking) to do code checking (the [checkr](https://github.com/dtkaplan/checkr) package provides a working prototype of a compatible code checker).

### Navigation and progress tracking

Each learnr tutorial includes a Table of Contents that tracks student progress. learnr remembers which sections of a tutorial a student completes, and returns a student to where they left off when they reopen a tutorial.

![learnr-blog-6](https://rstudioblog.files.wordpress.com/2017/06/learnr-blog-6.png)

### Progressive Reveal

learnr optionally reveals content one sub-section at a time. You can use this feature to let students set their own pace, or to hide information that would spoil an exercise or question that appears just before it.

To use progressive reveal, set the `progressive` field to true in the yaml header.

```yaml
---
title: "Programming basics"
output:
  learnr::tutorial:
    progressive: true
    allow_skip: true
runtime: shiny_prerendered
---
```

Visit [rstudio.github.io/learnr/](https://rstudio.github.io/learnr/) to learn more about creating interactive tutorials with learnr.

