---
title: 'BI and Data Science: Deliver Insights Through Embedded Analytics'
people:
  - Daniel Petzold
date: '2021-04-01'
slug: bi-and-data-science-deliver-insights-through-embedded-analytics
categories:
  - Data Science Leadership
tags:
  - BI tools
description: Continuing our series on self-service BI tools and code-first, open source data science, we explore embedded analytics and why they are a critical way for a data science team to deliver insights. We also discuss the unique needs that will be demanded of data science teams as they deliver insights that are secure, scalable, and flexible to multiple end user’s needs.
resources:
  - name:  "climbing"
    src:   "climbing.jpg"
    title: "Mountain climbing tools"
blogcategories:
- Data Science Leadership
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---
<sup>
Photo by <a href="https://unsplash.com/@omidarmin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Omid Armin</a> on <a href="https://unsplash.com/" target="_blank" rel="noopener noreferrer">Unsplash</a>
</sup>

Data Scientists are trailblazers. They look for value inside of data and seek to ask the right questions, disseminating insights to their stakeholders. In the world of business intelligence, those “on the ground” need more than just static reports. They need access to clear reproducible insights for exploration, feedback, and action, all in the right place at the right time. This may seem daunting but fortunately, BI and analytics have been tackling these challenges for some time. <b>Embedded analytics</b> integrates data analysis inside workflows, applications, and processes that people use every day, helping move the point of discovery to the point of decision.

In this post, we are going to dive into how the data scientist can integrate insights, increase adoption, and effectively empower end-users to make better decisions. With a code-first approach, data science is perfectly suited to rapidly integrate organizational insights with everyday systems. Our last post covered practical ways that BI and Data Science <a href="https://blog.rstudio.com/2021/03/25/bi-and-data-science-the-handoff/" target="_blank" rel="noopener noreferrer">collaborate with data handoffs</a>. Now let’s look further at how analysts, decision-makers, and end-users can benefit from “tightly tying the rope” between embedded analytics and data science in a secure, scalable, and flexible way.

> *With a code-first approach, data science is perfectly suited to rapidly integrate organizational insights with everyday systems.*
>

## Security and authentication: Overcoming the first roadblock

For an enterprise, data security is regularly a top concern across the entire organization. Security must be front and center as you plan your path forward and coordinate sharing across stakeholders. Not everyone will likely require (or should have) access to the same data. This is where having a system in place that customizes security and permissions for various predetermined roles, often at the data and row-level, will be critical. You need to define which of your stakeholders can view and collaborate on various data products. For example, will only internal users have access, or will outside stakeholders and/or customers also be consuming information as a service? Will you need to integrate with existing services?

No matter the answer to these questions, considerable work will be involved to ensure that proper security is enforced and organizational standards are met. This is one of the major reasons that <a href="https://www.rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a> is considered, to simplify the deployment of data products for multiple users, integrating directly with existing security protocols like LDAP/Active Directory, OAuth, PAM, SAML, and more.

## Scalability and communication: Expanding the horizon

As your user base grows, effective communication of results often requires access to the right tools for scheduling and alerts. Your team will likely need automated systems for updates and emails at critical times. No one wants to constantly monitor dashboards or receive non-relevant alerts. Having a system that helps you to administer alerts and scheduling will not only make your life easier but will make working and communicating across multiple teams and stakeholders over the long run more effective. Learn about how RStudio Connect makes this easy in our “Avoid Dashboard Fatigue” webinar <a href="https://www.rstudio.com/resources/webinars/avoid-dashboard-fatigue/" target="_blank" rel="noopener noreferrer">here</a>.

Embedded analytics runs on scalable platforms, particularly with software as a service (SaaS) to manage cost and capacity over time. As a data scientist, you can plug into these, allowing end-users to utilize models and increase adoption. The <a href="https://www.rplumber.io/index.html" target="_blank" rel="noopener noreferrer">Plumber API</a> (R-based) and <a href="https://flask.palletsprojects.com/en/1.1.x/" target="_blank" rel="noopener noreferrer">Flask API</a> (Python-based) both work alongside each other with RStudio Connect to provide the perfect combination of organizational access and integration. This in turn provides access without requiring R or Python knowledge for users. In addition, you can integrate work from both these languages, giving data science teams a clear point of collaboration. This is perfect for data science as a service (DSaaS) where models may need to be deployed and reused by multiple customers and different data sets. You can learn more about how the Plumber API allows data science to be used by a wide range of tools and technologies <a href="https://www.rstudio.com/resources/webinars/expanding-r-horizons-integrating-r-with-plumber-apis/" target="_blank" rel="noopener noreferrer">here</a> in this webinar.

## Flexibility and custom visualization: A lasting path

Insights from data science have huge potential, but they’re only as good as the runway given for exploration, visualization, and changes on the fly. Analysts and BI teams need access to fast, flexible, and performant updates, relevant to the question at hand.

> *Even when reporting was a part of the equation, it almost always boiled down to one major requirement; customizable self-service analytics, that could be reproduced and deployed quickly.*
>

As a product manager for embedded analytics, I’ve spoken to thousands of customers and carefully analyzed their top needs. Even when reporting was a part of the equation, it almost always boiled down to one major requirement; customizable self-service analytics, that could be reproduced and deployed quickly. On one end of the spectrum, this may mean simply providing diversity and access to input controls and the ability to import and/or export data to ensure the flexibility required. On the other end, it may mean going the extra mile to connect data science results to BI systems (with APIs like Plumber) to ensure that end-users have full access to results directly inside a pre-built BI tool for full-service data analytics. This means putting the keys to the kingdom (with the right access) into the hands of managers, decision-makers, and final users, communicating results that are meant to be explored based on changes that are happening in real-time. 

Also important to consider when scaling out new systems is the time that will be required from concept to release. How often do new data and insights need to be put into different applications, visualizations, or sets of controls? What type of performance is expected and how many users will ultimately need to be supported? How much customization will be required with the final visualization of results? 

Luckily data scientists are already in a place where they are accustomed to working with code and have full access to a range of open-source packages tailored for building out interactive applications, input controls, and custom visualizations. <a href="https://shiny.rstudio.com/" target="_blank" rel="noopener noreferrer">Shiny</a> is one such package for R, which combines computational power with interactivity for the modern web. <a href="https://docs.bokeh.org/en/latest/docs/gallery.html" target="_blank" rel="noopener noreferrer">Bokeh</a> and <a href="https://plotly.com/dash/" target="_blank" rel="noopener noreferrer">Dash</a> are similar packages for Python, which in addition to Shiny are fully supported for easy deployment inside <a href="https://www.rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a>.

## Conclusion

Organizations and their stakeholders depend on data scientists to forge a path forward through data. Like trailblazers, they are carving a path and overcoming unique challenges and obstacles that others can follow with BI tools. Many organizations are struck by the sheer speed that insights can be deployed using tools and languages that are native to their data science teams today. RStudio supports the direct creation and integration of open-source data science and stands ready to help companies and organizations expand with <a href="https://www.rstudio.com/products/team/" target="_blank" rel="noopener noreferrer">enterprise-level tooling and deployment</a>.

Curious to learn more about our approach? Check out this <a href="https://blog.rstudio.com/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">previous post</a> where we explore not only the importance of agility and durability to Serious Data Science but the key aspect of <a href="https://blog.rstudio.com/2020/06/02/is-your-data-science-credible-enough/" target="_blank" rel="noopener noreferrer">credibility</a> and how having the correct access and tools to find insights that are relevant builds trust and a path forward to understanding.
