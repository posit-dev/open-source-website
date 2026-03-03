---
date: '2022-06-13'
description: "00:00 Introduction\n00:18 sub_missing()\n03:51 Markdown formatting in sub_missing()\n04:51 sub_zero()\n07:34 sub_small_vals()\n13:08 sub_large_vals()\n16:25 final thoughts\n\nA new version of the R package {gt} has been released! We are now at version `0.6.0` and there are now even more features that'll make your display/summary tables look and work much, much better. Let's run through some of the bigger changes and see the benefits they can bring!\n\nNew functions for substituting cell data\nWe now have four new functions that allow you to make precise substitutions of cell values with perhaps something more meaningful. They all begin with `sub_` and that's short for substitution!\n\nsub_missing() (formerly known as fmt_missing())\nHere's something that's both old and new. The sub_missing() function (for replacing NAs with... something) is new, but it's essentially replacing a function that is old (fmt_missing()).\n\nThe missing_text replacement of \"---\" is actually an em dash (the longest of the dash family). This can be downgraded to an en dash with \"--\" or we can go further with \"-\", giving us a hyphen replacement. Or, you can use another piece of text. \n\nIf you're using and loving fmt_missing(), it's okay! You'll probably receive a warning about it when you upgrade to {gt} 0.6.0 though. Best to just substitute fmt_missing() with sub_missing() anyway!\n\nsub_zero()\nThe sub_zero() function allows for substituting zero values in the table body. \n\nsub_small_vals()\nNext up is the sub_small_vals() function. Ever have really, really small values and really just want to say they are small? \n\nWith sub_small_vals() we can reformat smaller numbers using the default threshold of 0.01.\n\nSmall and negative values can also be handled but they are handled specially by the sign\nparameter. Setting that to \"-\" will format only the small, negative values.\n\nYou don't have to settle with the default threshold value or the default replacement pattern\n(in small_pattern). This can be changed and the \"x\" in small_pattern (which uses the\nthreshold value) can even be omitted.\n\nsub_large_vals()\nOkay, there's one more substitution function to cover, and this one's for all the large values in your table: sub_large_vals(). With this you can substitute what you might consider as too large values in the table body.\n\nLarge negative values can also be handled but they are handled specially by the sign parameter. Setting that to \"-\" will format only the large values that are negative. \nYou don't have to settle with the default threshold value or the default replacement pattern (in large_pattern). This can be changed and the \"x\" in large_pattern (which uses the threshold value) can even be omitted.\n\nFinal thoughts\nWe are always trying to improve the gt package with a mix of big features (some examples: improving rendering, adding new families of functions) and numerous tiny features (like improving existing functions, clarifying documentation, etc.). It's hoped that the things delivered in gt 0.6.0 lead to improvements in how you create and present summary tables in R. If there are features you *really* want, always feel free to: \n\nFile an issue: https://github.com/rstudio/gt/issues) \nTalk about your ideas on the Discussions page: https://github.com/rstudio/gt/discussions\n\nLearn more about the gt package here: \nhttps://gt.rstudio.com/\n\nGot questions? The RStudio Community site is a great place to get assistance:\nhttps://community.rstudio.com/\n\nContent: Rich Iannone (@riannone) \nMotion Design & editing: Jesse Mostipak \nMusic: Nu Fornacis by Blue Dot Sessions https://app.sessions.blue/browse/track/98983"
people:
- Rich Iannone
resource_type: video
resources: []
software:
- design
- gt
- here
- markdown
- probably
- rstudio
title: Rich Iannone || New features in {gt} 0.6.0! || RStudio

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 10
  date: '2022-06-13T16:00:56Z'
  definition: hd
  description: "00:00 Introduction\n00:18 sub_missing()\n03:51 Markdown formatting in sub_missing()\n04:51 sub_zero()\n07:34 sub_small_vals()\n13:08 sub_large_vals()\n16:25 final thoughts\n\nA new version of the R package {gt} has been released! We are now at version `0.6.0` and there are now even more features that'll make your display/summary tables look and work much, much better. Let's run through some of the bigger changes and see the benefits they can bring!\n\nNew functions for substituting cell data\nWe now have four new functions that allow you to make precise substitutions of cell values with perhaps something more meaningful. They all begin with `sub_` and that's short for substitution!\n\nsub_missing() (formerly known as fmt_missing())\nHere's something that's both old and new. The sub_missing() function (for replacing NAs with... something) is new, but it's essentially replacing a function that is old (fmt_missing()).\n\nThe missing_text replacement of \"---\" is actually an em dash (the longest of the dash family). This can be downgraded to an en dash with \"--\" or we can go further with \"-\", giving us a hyphen replacement. Or, you can use another piece of text. \n\nIf you're using and loving fmt_missing(), it's okay! You'll probably receive a warning about it when you upgrade to {gt} 0.6.0 though. Best to just substitute fmt_missing() with sub_missing() anyway!\n\nsub_zero()\nThe sub_zero() function allows for substituting zero values in the table body. \n\nsub_small_vals()\nNext up is the sub_small_vals() function. Ever have really, really small values and really just want to say they are small? \n\nWith sub_small_vals() we can reformat smaller numbers using the default threshold of 0.01.\n\nSmall and negative values can also be handled but they are handled specially by the sign\nparameter. Setting that to \"-\" will format only the small, negative values.\n\nYou don't have to settle with the default threshold value or the default replacement pattern\n(in small_pattern). This can be changed and the \"x\" in small_pattern (which uses the\nthreshold value) can even be omitted.\n\nsub_large_vals()\nOkay, there's one more substitution function to cover, and this one's for all the large values in your table: sub_large_vals(). With this you can substitute what you might consider as too large values in the table body.\n\nLarge negative values can also be handled but they are handled specially by the sign parameter. Setting that to \"-\" will format only the large values that are negative. \nYou don't have to settle with the default threshold value or the default replacement pattern (in large_pattern). This can be changed and the \"x\" in large_pattern (which uses the threshold value) can even be omitted.\n\nFinal thoughts\nWe are always trying to improve the gt package with a mix of big features (some examples: improving rendering, adding new families of functions) and numerous tiny features (like improving existing functions, clarifying documentation, etc.). It's hoped that the things delivered in gt 0.6.0 lead to improvements in how you create and present summary tables in R. If there are features you *really* want, always feel free to: \n\nFile an issue: https://github.com/rstudio/gt/issues) \nTalk about your ideas on the Discussions page: https://github.com/rstudio/gt/discussions\n\nLearn more about the gt package here: \nhttps://gt.rstudio.com/\n\nGot questions? The RStudio Community site is a great place to get assistance:\nhttps://community.rstudio.com/\n\nContent: Rich Iannone (@riannone) \nMotion Design & editing: Jesse Mostipak \nMusic: Nu Fornacis by Blue Dot Sessions https://app.sessions.blue/browse/track/98983"
  duration: 1043
  has_captions: true
  language: en
  last_updated: '2026-03-02T20:54:21.349201+00:00'
  like_count: 0
  people:
  - Rich Iannone
  playlist: ''
  software:
  - design
  - gt
  - here
  - markdown
  - probably
  - rstudio
  tags:
  - rstudio
  - data science
  - machine learning
  - python
  - stats
  - tidyverse
  - data visualization
  - data viz
  - ggplot
  - coding
  - server pro
  - shiny
  - rmarkdown
  - CRAN
  - interoperability
  - dplyr
  - forcats
  - ggplot2
  - tibble
  - readr
  - stringr
  - tidyr
  - purrr
  - github
  - data wrangling
  - tidy data
  - odbc
  - plumber
  - blogdown
  - gt
  - lazy evaluation
  - tidymodels
  - statistics
  - debugging
  - programming education
  - rstats
  - open source
  - OSS
  - reticulate
  - gt 0.6.0
  - rich iannone
  - gt update
  - sub_missing
  - sub_small_vals
  - sub_large_vals
  - sub_zero
  - tables
  thumbnail: https://i.ytimg.com/vi/F5TV9uWCJps/maxresdefault.jpg
  title: Rich Iannone || New features in {gt} 0.6.0! || RStudio
  url: https://www.youtube.com/watch?v=F5TV9uWCJps
  view_count: 2670
---

