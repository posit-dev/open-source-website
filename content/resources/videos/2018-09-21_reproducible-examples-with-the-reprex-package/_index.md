---
date: '2018-09-21'
description: "Reproducible Examples and the `reprex` package. \nhttps://speakerdeck.com/jennybc/reprex-reproducible-examples-with-r\n\nJump to: \n0:08 Intro\n0:40 Basic usage of reprex\n3:35 Motivation, why use reprex? \"Help me help you\"\n\n4:08 Define `reprex`? \nThree commons ways to use the term. \n1. noun, a reproducible example\n2. the reprex package. a tool to build R `reprex`s\n3. reprex::reprex(), a function in `reprex` to  make a reprex. \n\n5:26 When should you use a reprex? \n\n6:14 reprex installation and setup. \nHow do you actually get repex on your machine? \n7:59 Advanced setup and discussion. \n9:45 Please use advanced features responsibly. \n\n11:02 Why does the reprex package exist? \nAnyone who has helped teach R or dealt with github issues, twitter, stack overflow & RStudio community questions knows that helping people diagnose their coding problems can be hard.\nThis tool comes from hard-won experience. It’s aim to is help people ask well formed questions and increase the chances of getting well formed answers quickly. \n\n12:52  philosophy behind reprex\n1. code that I can run\n2. code that I don't need to run\n3. code that I can easily run\n\n13:52 code that I can run. \n\n17:25  Tips on writing good `reprex`s. Dos and don'ts. \n\n18:52  How do I get my data into my reprex?\nGetting small data and CSV type data into your reprex is easy.  \n“I have a big hairy data object and I can only show their problem by using it”, but that's not always the case. \n\n21:02  code that I don't need to run\nreprex gives your reader the code and reveals the output being produced by that code. For experienced coders, that might be enough to help you. \n\n22:44  code that I can easily run\nDon't copy and paste from the R console. This is usually annoying for your reader. \nWorse than console copy-pasta is the screenshot. (Many people think screenshots of code are downright offensive.)\n\n25:03 reprex_clean\nIf you copy someone else's reprex into your consolve, it may include their output, making your new reprex a untidy. \nHere are tips for taking someone else's reprex code and output, and create a clean reprex reply. \n\n\n25:54 shock and awe\nMore interesting features of the reprex package. \n- 26:29 What about figures and plots in your reprex? So happy you asked about that. reprex will automatically upload your images to imgur.com. \n- 28:23 Create a reprex by explicitly providing your code in the reprex call. \n- 29:00 when you need your reprex to work in the current working directory. \n- 30:45 Differently flavored markdown. Optimize your reprex markdown output for github, stack overflow, or the RStudio community. \n- 30:31 Make your reprex create an R script, with your reprex outputs as comments. This is handy for pasting into an email or slack-type-app. \n- 32:25 Rich text format, rtf output. (currently experimental feature as of this video)\n- 33:06 supress the reprex add at the bottom of your reprex\n- 33:19 Include session info. \n- 33:54 Auto styling of your code. Good if you're dealing with poorly formatting code.\n- 34:25 Change your comments string. \n- 34:32 Silence Tidyverse startup messages. \n- 35:00 Capture a reprex that sends messages to standard output and standard input (e.g. package installation compilation messages). \n\n36:13  Set up personal defaults for your reprex usage. \n\n36:54 reprex RStudio addins; render reprex and reprex selection. These accelerate your use of reprex. \n\n39:01 The human side of reproducible examples. \nHow to ask questions in ways that are most likely to get answered. \nSorry for the tough love, but this is important. Why are you always asked to give a reprex? \n- Experts try to use reproducible examples to ensure their advice works. \n- Making a good reprex is hard. But, you are asking them to solve a problem for you, so meet them halfway. \n- Creating reprexes is good coding practice. \n- Making a good reprex is often a good way to debug your issue in the embarrassment-free privacy of your own home. \n- reprexes lead to discussions more likely to help people in the future. \n\n44:34 Behind the scenes of reprex\n\n44:44 Thanks for those that helped make reprex possible. \n\nQuestions and Answers\n- 46:05 can reprex capture variables and objects in the current environment? (not yet, maybe in development)\n- 47:25 does reprex actually check that the code is self contained? (self contained)\n- 48:08 does readr::read_csv support the text argument? (yep, just read the help manual for readr)"
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software:
- readr
- reprex
- rstudio
- tidyverse
tags:
- reprex
- reproducible examples
- r-coding
- r-software
- r-stats
- statistics
- coding
- data science
title: Reproducible Examples with the reprex package

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 1
  date: '2018-09-21T14:22:14Z'
  definition: hd
  description: "Reproducible Examples and the `reprex` package. \nhttps://speakerdeck.com/jennybc/reprex-reproducible-examples-with-r\n\nJump to: \n0:08 Intro\n0:40 Basic usage of reprex\n3:35 Motivation, why use reprex? \"Help me help you\"\n\n4:08 Define `reprex`? \nThree commons ways to use the term. \n1. noun, a reproducible example\n2. the reprex package. a tool to build R `reprex`s\n3. reprex::reprex(), a function in `reprex` to  make a reprex. \n\n5:26 When should you use a reprex? \n\n6:14 reprex installation and setup. \nHow do you actually get repex on your machine? \n7:59 Advanced setup and discussion. \n9:45 Please use advanced features responsibly. \n\n11:02 Why does the reprex package exist? \nAnyone who has helped teach R or dealt with github issues, twitter, stack overflow & RStudio community questions knows that helping people diagnose their coding problems can be hard.\nThis tool comes from hard-won experience. It’s aim to is help people ask well formed questions and increase the chances of getting well formed answers quickly. \n\n12:52  philosophy behind reprex\n1. code that I can run\n2. code that I don't need to run\n3. code that I can easily run\n\n13:52 code that I can run. \n\n17:25  Tips on writing good `reprex`s. Dos and don'ts. \n\n18:52  How do I get my data into my reprex?\nGetting small data and CSV type data into your reprex is easy.  \n“I have a big hairy data object and I can only show their problem by using it”, but that's not always the case. \n\n21:02  code that I don't need to run\nreprex gives your reader the code and reveals the output being produced by that code. For experienced coders, that might be enough to help you. \n\n22:44  code that I can easily run\nDon't copy and paste from the R console. This is usually annoying for your reader. \nWorse than console copy-pasta is the screenshot. (Many people think screenshots of code are downright offensive.)\n\n25:03 reprex_clean\nIf you copy someone else's reprex into your consolve, it may include their output, making your new reprex a untidy. \nHere are tips for taking someone else's reprex code and output, and create a clean reprex reply. \n\n\n25:54 shock and awe\nMore interesting features of the reprex package. \n- 26:29 What about figures and plots in your reprex? So happy you asked about that. reprex will automatically upload your images to imgur.com. \n- 28:23 Create a reprex by explicitly providing your code in the reprex call. \n- 29:00 when you need your reprex to work in the current working directory. \n- 30:45 Differently flavored markdown. Optimize your reprex markdown output for github, stack overflow, or the RStudio community. \n- 30:31 Make your reprex create an R script, with your reprex outputs as comments. This is handy for pasting into an email or slack-type-app. \n- 32:25 Rich text format, rtf output. (currently experimental feature as of this video)\n- 33:06 supress the reprex add at the bottom of your reprex\n- 33:19 Include session info. \n- 33:54 Auto styling of your code. Good if you're dealing with poorly formatting code.\n- 34:25 Change your comments string. \n- 34:32 Silence Tidyverse startup messages. \n- 35:00 Capture a reprex that sends messages to standard output and standard input (e.g. package installation compilation messages). \n\n36:13  Set up personal defaults for your reprex usage. \n\n36:54 reprex RStudio addins; render reprex and reprex selection. These accelerate your use of reprex. \n\n39:01 The human side of reproducible examples. \nHow to ask questions in ways that are most likely to get answered. \nSorry for the tough love, but this is important. Why are you always asked to give a reprex? \n- Experts try to use reproducible examples to ensure their advice works. \n- Making a good reprex is hard. But, you are asking them to solve a problem for you, so meet them halfway. \n- Creating reprexes is good coding practice. \n- Making a good reprex is often a good way to debug your issue in the embarrassment-free privacy of your own home. \n- reprexes lead to discussions more likely to help people in the future. \n\n44:34 Behind the scenes of reprex\n\n44:44 Thanks for those that helped make reprex possible. \n\nQuestions and Answers\n- 46:05 can reprex capture variables and objects in the current environment? (not yet, maybe in development)\n- 47:25 does reprex actually check that the code is self contained? (self contained)\n- 48:08 does readr::read_csv support the text argument? (yep, just read the help manual for readr)"
  duration: 3087
  has_captions: true
  language: en
  last_updated: '2026-03-20T11:32:56.700400+00:00'
  like_count: 0
  playlist: ''
  software:
  - readr
  - reprex
  - rstudio
  - tidyverse
  tags:
  - reprex
  - reproducible examples
  - r-coding
  - r-software
  - r-stats
  - statistics
  - coding
  - data science
  thumbnail: https://i.ytimg.com/vi/MmTPhGQWPUo/maxresdefault.jpg
  title: Reproducible Examples with the reprex package
  url: https://www.youtube.com/watch?v=MmTPhGQWPUo
  view_count: 1354
---
image: thumbnail.jpg

