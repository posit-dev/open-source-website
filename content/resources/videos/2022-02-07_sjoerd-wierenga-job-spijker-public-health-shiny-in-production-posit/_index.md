---
date: '2022-02-07'
description: 'R in Public Sector: Organizational & Technical Aspects of Shiny in Production with the Dutch National Institute for Public Health and the Environment.


  00:00 - Introductions

  2:47 - Organizational aspects of Shiny in production

  32:52 - Technical aspects of Shiny in production

  52:33 - Ask us everything / Open Discussion


  Questions:

  29:00 - When you first introduced Shiny, what other tools were you comparing it to? How did you explain the difference to your leaders?

  30:00 - What were the most important aspects of your prototype app to create buy-in?

  52:33 - As Clusterbuster began to be used by more people, did you face any performance issues? How did you adjust your app to deal with more concurrent users?

  56:10 - Can you say anything about the update frequency of the data?

  57:15 - Which model was used to define the clusters?

  58:23 - Did you ever consider not using a database?

  1:01:50 - What''s the communication with the data engineering team?

  1:03:51 - How often do you collect feedback from users and update your app?

  1:05:10 - Was your data loaded into Docker in a form of some aggregates? How did you create them?

  1:06:26 - What is the main advantage of keeping it all in R with Shiny? Did you feel at any point you were sacrificing simplicity?

  1:08:14 - Did you use any specific methods to increase the performance of your app? Did you scope your data, or load it all in the global file?

  1:12:03 - How did you make sure regions and users felt comfortable using your app?

  1:13:25 - What types of businesses are hotbeds for covid clusters? Has this info informed policy changes?

  1:14:50 - How did the data quality issues improve over the rollout?

  1:16:47 - Did you use CI/CD?

  1:17:38 - Did you have any functionality within your apps to send individual-level data to municipalities?

  1:19:47 - For huge amounts of data, have you tested out different file types to store your data set within your containers?

  1:20:54 - For people just starting to use Shiny, what is one piece of advice you would give them?


  Proof on Concept with fictitious data: https://rivm.shinyapps.io/clusterbuster/

  Blog post from the team as well! https://www.rstudio.com/blog/how-the-clusterbuster-shiny-app-helps-battle-covid-19-in-the-netherlands/

  Code-first blog post mentioned: https://www.rstudio.com/blog/code-first-data-science-for-the-enterprise2/


  How the "Clusterbuster" app provides actionable information to 300 health professionals

  Presented by: Sjoerd Wierenga


  In this talk we want to give an overview of what it took to create the Clusterbuster from an organizational perspective. We will go into detail on how we got from an abstract question to an application that is user-friendly, safe, and valuable. Furthermore, we will offer a glimpse of what is yet to come, and where we see possibilities to turbocharge a more data-driven public policy approach.


  How to build a production shiny app within the context of public health governance.

  Presented by: Job Spijker


  This presentation goes into the more technical details about the production environment of the Clusterbuster application. We will show how we deployed the application, how we ensured security and mitigated the risks in case of a security breach, and how we organized our code for maintainability and refactoring.


  Presenter Biographies:


  Sjoerd Wieringa: As the son of two healthcare professionals, with a background in Public Administration, and a passion for technology, it is no surprise that Sjoerd Wierenga now works at the National Institute for Public Health and the Environment leading a team of highly skilled Data Scientists that created an application to support the battle against COVID-19. After having worked as a healthcare manager for several years, he decided he wanted to learn how to program. Which he has been doing now since 2016 in different capacities.


  Job Spijker: Job Spijker is a senior research and data scientist at the Dutch National Institute of Public Health and the Environment. He has a PhD in Earth Sciences with a focus on computational and statistical methods of spatial data. He is currently involved in projects about how the institute’s environmental and health data can be leveraged to create insightful actionable information to assist policy makers at local, regional, and national level.'
image: thumbnail.jpg
people: []
resource_type: video
resources: []
software:
- rstudio
- Shiny
- shinyapps
tags: []
title: Sjoerd Wierenga & Job Spijker | Public Health | Shiny in Production | Posit

external:  # updated automatically, do not edit
  channel: Posit PBC
  comment_count: 2
  date: '2022-02-07T20:21:53Z'
  definition: hd
  description: 'R in Public Sector: Organizational & Technical Aspects of Shiny in Production with the Dutch National Institute for Public Health and the Environment.


    00:00 - Introductions

    2:47 - Organizational aspects of Shiny in production

    32:52 - Technical aspects of Shiny in production

    52:33 - Ask us everything / Open Discussion


    Questions:

    29:00 - When you first introduced Shiny, what other tools were you comparing it to? How did you explain the difference to your leaders?

    30:00 - What were the most important aspects of your prototype app to create buy-in?

    52:33 - As Clusterbuster began to be used by more people, did you face any performance issues? How did you adjust your app to deal with more concurrent users?

    56:10 - Can you say anything about the update frequency of the data?

    57:15 - Which model was used to define the clusters?

    58:23 - Did you ever consider not using a database?

    1:01:50 - What''s the communication with the data engineering team?

    1:03:51 - How often do you collect feedback from users and update your app?

    1:05:10 - Was your data loaded into Docker in a form of some aggregates? How did you create them?

    1:06:26 - What is the main advantage of keeping it all in R with Shiny? Did you feel at any point you were sacrificing simplicity?

    1:08:14 - Did you use any specific methods to increase the performance of your app? Did you scope your data, or load it all in the global file?

    1:12:03 - How did you make sure regions and users felt comfortable using your app?

    1:13:25 - What types of businesses are hotbeds for covid clusters? Has this info informed policy changes?

    1:14:50 - How did the data quality issues improve over the rollout?

    1:16:47 - Did you use CI/CD?

    1:17:38 - Did you have any functionality within your apps to send individual-level data to municipalities?

    1:19:47 - For huge amounts of data, have you tested out different file types to store your data set within your containers?

    1:20:54 - For people just starting to use Shiny, what is one piece of advice you would give them?


    Proof on Concept with fictitious data: https://rivm.shinyapps.io/clusterbuster/

    Blog post from the team as well! https://www.rstudio.com/blog/how-the-clusterbuster-shiny-app-helps-battle-covid-19-in-the-netherlands/

    Code-first blog post mentioned: https://www.rstudio.com/blog/code-first-data-science-for-the-enterprise2/


    How the "Clusterbuster" app provides actionable information to 300 health professionals

    Presented by: Sjoerd Wierenga


    In this talk we want to give an overview of what it took to create the Clusterbuster from an organizational perspective. We will go into detail on how we got from an abstract question to an application that is user-friendly, safe, and valuable. Furthermore, we will offer a glimpse of what is yet to come, and where we see possibilities to turbocharge a more data-driven public policy approach.


    How to build a production shiny app within the context of public health governance.

    Presented by: Job Spijker


    This presentation goes into the more technical details about the production environment of the Clusterbuster application. We will show how we deployed the application, how we ensured security and mitigated the risks in case of a security breach, and how we organized our code for maintainability and refactoring.


    Presenter Biographies:


    Sjoerd Wieringa: As the son of two healthcare professionals, with a background in Public Administration, and a passion for technology, it is no surprise that Sjoerd Wierenga now works at the National Institute for Public Health and the Environment leading a team of highly skilled Data Scientists that created an application to support the battle against COVID-19. After having worked as a healthcare manager for several years, he decided he wanted to learn how to program. Which he has been doing now since 2016 in different capacities.


    Job Spijker: Job Spijker is a senior research and data scientist at the Dutch National Institute of Public Health and the Environment. He has a PhD in Earth Sciences with a focus on computational and statistical methods of spatial data. He is currently involved in projects about how the institute’s environmental and health data can be leveraged to create insightful actionable information to assist policy makers at local, regional, and national level.'
  duration: 5047
  has_captions: false
  language: en
  last_updated: '2026-03-04T14:51:27.561238+00:00'
  like_count: 36
  playlist: ''
  software:
  - rstudio
  - Shiny
  - shinyapps
  tags: []
  thumbnail: https://i.ytimg.com/vi/9Nn9yjpivlE/hqdefault.jpg
  title: Sjoerd Wierenga & Job Spijker | Public Health | Shiny in Production | Posit
  url: https://www.youtube.com/watch?v=9Nn9yjpivlE
  view_count: 1319
---
image: thumbnail.jpg

