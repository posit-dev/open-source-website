---
title: Avoid Irrelevancy and Fire Drills in Data Science Teams
people:
  - Sean Lopp
date: '2020-04-28'
slug: avoid-irrelevancy-and-fire-drills-in-data-science-teams
categories:
- Data Science Leadership
resources:
- name: irrelevancy-and-fire-drills
  src: irrelevancy-and-fire-drills.png
  title: A visualization of a computer thrown away and a fire
blogcategories:
- Data Science Leadership
events: blog
ported_from: rstudio
port_status: raw
---


## Balancing the twin threats of data science development 

Data science leaders naturally want to maximize the value their teams deliver to their organization, and that often means helping them navigate between two possible extremes. On the one hand, a team can easily become an expensive R&D department, detached from actual business decisions, slowly chipping away only to end up answering stale questions. On the other hand, teams can be overwhelmed with requests, spending all of their time on labor intensive, manual fire-drills,  always creating one more “Just in Time” Powerpoint slide. 

How do you avoid these threats, of either irrelevancy or constant fire drills?  As we touched on in a recent blog post, [Getting to the Right Question](https://blog.rstudio.com/2020/04/22/getting-to-the-right-question/), it turns out the answer is pretty straightforward: use iterative, code-based development to share your content early and often, to help overcome the communications gap with your stakeholders.

Data science ecosystems can be complex and full of jargon, so before we dive into specifics let's consider a similar balancing act. Imagine you are forming a band that wants to share new music with the world. To do so, it is critical to get music out to your fans quickly, to iterate on ideas rapidly. You don’t want to get bogged down in the details of a recording studio on day 1.  At the same time, you want to be able to capture and repeat what works - perhaps as sheet music, perhaps as a video, or even as a simple recording. 

## Share your data science work early and often

For data scientists, the key is creating the right types of outputs so that decision makers can iterate with you on questions and understand your results. Luckily, like a musician, the modern data science team has many ways to share their initial vision:

  * They can quickly create notebooks, through tools like R Markdown or Jupyter, that are driven by reproducible code and can be shared, scheduled, and viewed without your audience needing to understand code. 
  * They can build interactive web applications using tools like Shiny, Flask, or Dash to help non-coders test questions and explore data. 
  * Sometimes, data science teams even create APIs, which act as a realistic preview of their final work with a much lower cost of creation.

Sharing early and often enables data science teams to solve impactful problems. For example, perhaps a data scientist is tasked with forecasting sales by county. They might share their initial exploratory analysis sales leadership and tap into their domain expertise to help explain outlier counties. Or imagine a data scientist working to support biologists doing drug discovery research. Instead of responding to hundreds of requests for statistical analysis,  the data scientist could build an interactive application to allow biologists to run their own analysis on different inputs and experiments. By sharing the application early and often, the biologist and data scientist can empower each other to complete far more experiments.

These types of outputs all share a few characteristics:

  1. **The outputs are easy to create.** The sign that your team has the right set of tools is if a data scientist can create and share an output from scratch in days, not months. They shouldn’t have to learn a new framework or technology stack.

  2. **The outputs are reproducible.** It can be tempting, in a desire to move quickly, to take shortcuts. However, these shortcuts can undermine your work almost immediately. Data scientists are responsible for informing critical decisions with data. This responsibility is serious, and it means results can not exist only on one person’s laptop, or require manual tweaking to recreate. A lack of reproducibility can undermine credibility in the minds of your stakeholders, which may lead them to dismiss or ignore your analyses if the answer conflicts with their intuition.

  3. **Finally, and most importantly: the outputs must be shared.** All of these examples: notebooks, interactive apps and dashboards, and even APIs, are geared towards interacting with decision makers as quickly as possible to be sure the right questions are being answered.

## Benefits of sharing for data science teams

Luckily, tools exist to ensure data science teams can create artifacts that share these three characteristics. At RStudio, we’ve built [RStudio Team](https://rstudio.com/products/team/) with all 3 of these goals in mind.

Great data science teams talk about the happy result of this approach. For examples: 

> *“RStudio Connect is critical, the way you can deploy flexdashboards, R Markdown… I use web apps as a way to convey a model in a very succinct fashion... because I don’t know what the user will do, I can create an app where the user’s interactions with the model can imply it, I don’t have to come up with all the finite outcomes ahead of time”* - Moody Hadi at S&P

> *“One of the key focuses for us was the method of delivery ... actually taking your insights and getting business impact. How are non analytic people digesting your work.”* - Aymen Waqar at Astellas (check out our last blog post, [Getting to the Right Question](https://blog.rstudio.com/2020/04/22/getting-to-the-right-question/), to see Aymen discussing the analytics communication gap)

<div align="center" style="padding: 35px 0 35px 0;">
<script src="https://fast.wistia.com/embed/medias/58qjn34mxy.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_58qjn34mxy videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/58qjn34mxy/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>
</div>

## It’s not just about production

We often see data science teams make a common mistake that prevents them from achieving this delicate balancing act. A tempting trap is to focus exclusively on complex tooling oriented towards putting models in production. Because data science teams are trying to strike a balance between repeatability, robustness, and speed, and because they are working with code, they often turn to their software engineering counterparts for guidance on adopting “agile” processes. Unfortunately, many teams end up focusing on the wrong parts of the agile playbook. Instead of copying the concept - rapid iterations towards a useful goal - teams get caught up in the technologies, introducing complex workflows instead of focusing on results. This mistake leads to a different version of the expensive R&D department - the band stuck in a recording studio with the wrong song.

Eduardo Arina de la Rubio, head of a large data team at Facebook, lays out an important reminder [in his recent talk at rstudio::conf 2020](https://resources.rstudio.com/rstudio-conf-2020/value-in-data-science-beyond-models-in-production-eduardo-arino-de-la-rubia). Data science teams are not machine learning engineers. While growth of the two are related, ML models will ultimately become commoditized, mastered by engineers and available in off-the-shelf offerings. Data scientists, on the other hand, have a broader mandate: to enable critical business decisions. Often, in the teams we work with at RStudio, many projects are resolved and decisions made based on the rapid iteration of an app or a notebook. Only on occasion does the result need to be codified into a model at scale - and usually engineers are involved at that stage. 


To wrap up, at RStudio we get to interact with hundreds of data science teams of all shapes and sizes from all types of industries. The best of these teams have all mastered the same balancing act: they use powerful tools to help them share results quickly, earning them a fanbase among their business stakeholders and helping their companies make great decisions. 

We developed RStudio Team with this balancing act in mind, and to make it easy for data science teams to create, reproduce and share their work. To learn more, please visit the [RStudio Team page](https://rstudio.com/products/team/).

<div style="padding: 25px 0 25px 0;"></div>

