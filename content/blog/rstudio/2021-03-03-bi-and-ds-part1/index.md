---
title: 'BI and Data Science: The Best of Both Worlds'
people:
  - Lou Bajuk
date: '2021-03-04'
slug: bi-and-ds-part1
description: "In many large organizations, Business Intelligence and Data Science teams compete for budget and mindshare. By focusing on how data science can both augment and complement BI tools such as Tableau and PowerBI, these teams can unite on their common goal: delivering data-driven insights for better decision making."
categories:
  - Data Science Leadership
tags:
  - BI tools
alttext: two lego men dueling with swords
blogcategories:
- Data Science Leadership
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---

<sup>Photo by <a href="https://unsplash.com/@stillnes_in_motion?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Stillness InMotion</a> on <a href="https://unsplash.com/s/photos/robot-fencing?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Unsplash</a></sup>


In previous posts, we've talked about the critical importance of <a href="https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/" target="_blank" rel="noopener noreferrer">interoperability</a>, and how it helps organizations and data science teams get the most out of their analytic investments. We've focused recently on the ways that R and Python can be used together, and how RStudio's products <a href="https://blog.rstudio.com/2021/01/13/one-home-for-r-and-python/" target="_blank" rel="noopener noreferrer">provide a single home for R and Python</a>.  For the next few posts, we will turn our attention to a different aspect of interoperability: the intersection between Business Intelligence (BI) and data science platforms. 

## BI and Data Science: Organizational Rivals?

Organizations, large and small, have taken various paths on the quest for better, more data-driven decision making. Historically, many large organizations were dependent on centralized IT-driven projects to develop reports and dashboards. As pressure has increased to become more agile in creating and delivering insights to improve how decisions are made, organizations typically adopt these approaches:

-   **Self-service BI tools:** These tools, such as Tableau, PowerBI and Spotfire, are typically used by those who understand data, but may not be comfortable coding in languages such as R or Python. Often, these users are looking for the next level of analytic and visualization depth beyond spreadsheets.  These tools typically include a way of sharing these analyses with others.
-   **Open source data science frameworks:** These applications, using tools such as Shiny, R Markdown, Dash, Streamlit and Bokeh, are typically created by data scientists coding in R or Python and draw on the full analytic and visualization richness of these ecosystems. These applications can be shared in various ways, both through homegrown solutions and professional products such as <a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a>. 

Both approaches allow the analytically-minded to draw on data from multiple data sources and to explore, visualize and understand that data in flexible and powerful ways. They also allow users to create rich interactive applications and dashboards that can be shared with others to improve their decision-making.

These common purposes and capabilities, ironically, often trap the teams that use and maintain these tools as organizational competitors for software budgets and executive mindshare.  These very different approaches can end up delivering applications and dashboards that may (at first glance) appear very similar. The strengths, weaknesses and nuances of the two approaches can be obscured to decision makers, especially to executive budget holders. 

However, this confusion obscures the distinct opportunities each type of tool provides and how using the tools together can deliver even more value to the organization. 

## Data Science Should Complement and Augment your BI Tools

In our next post, we will do a deeper dive into the strengths and challenges of self-service BI tools and code-oriented, open source data science — and what to consider when choosing an approach.

In talking with many different analytic teams at organizations that have successfully combined BI and Data Science, their strategies have typically fallen into two categories: Using data science to either **complement** or **augment** self-service BI.

In the **complement** approach, organizations use BI and data science tools side by side for:

-   **Widespread reporting:** Where standard visualizations and simpler analytic approaches are sufficient, these organizations use BI tools such as Tableau or PowerBI to empower a wide range of analysts to create dashboards and reports and share them across the organization. 
-   **Specialized applications:** For use cases that require custom visualizations, deeper predictive or machine learning capabilities, or simply a higher level of customization in the data analysis and presentation, these organizations develop applications using code-based frameworks. These frameworks include Shiny, RMarkdown, Dash, Streamlit and Bokeh, and the R and Python languages they are built on. In some cases, these tools are used to create highly tailored applications that support critical decision making by executive teams, which can be rapidly iterated and redeployed in response to feedback and questions. 
-   **A broader spectrum of data products:** Frequently this mixed approach utilizes <a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a>, which also supports the delivery of predictive models, APIs for automated decision making, Jupyter Notebooks and automated data pipelines. This broader selection of outputs greatly enhances the ways that data-driven insights can be applied in an organization. 

A great example of this approach comes from Dr. Behrooz Hassani-Mahmooei, Principal Specialist and Director at the Strategic Intelligence and Insights Unit at Monash University:

> "Tools such as PowerBI are very useful when you want to start from data and generate information. But when you have a specific decision that you are expected to inform, especially a strategic decision, you need tools that enable you to start from that decision and reverse engineer back to the data. That is where R and RStudio helped us as a competitive advantage, in what we call strategic analytics, where you need maximum flexibility and reproducibility as well as clarity for communication and translation." 

In the **augment** approach, organizations use BI and Data Science tools together to: 

-   **Validate insights:** When the user of a BI tool finds a potentially interesting pattern, data scientists might be asked to verify the insight. Those data scientists can apply more rigorous analytic approaches to confirm whether those results are significant enough to base future decision making on. The data scientists validating the results may communicate that finding back to the BI team or deploy the insight on a low-cost open source platform.  
-   **Enrich data for BI reporting:** Data science tools can complement BI tools by enriching the underlying data using more advanced analytic techniques, such as eliminating highly-correlated columns. This can help the BI users focus on the most important aspects of the data. Data science teams can also encorporate non-traditional data sources, add model scores, and provide calculated columns that might be difficult to create in the BI tools. These additions can be delivered using shared data sources or API calls that take advantage of robust, customizable data and machine learning pipelines.
-   **Expand the audience for data science insights:** Data science teams who deliver their insights through an organization's corporate-standard BI tool can reach a much broader audience. This can boost the visibility and perceived value of the data science team as well as increase the impact of generated features and model scores.
-   **Overcome BI limitations:** While modern BI tools have a wide range of visualizations and basic statistical tools, they are largely constrained by the proprietary capabilities their vendors implement. Code-oriented data science can extend these capabilities with customizable visualizations and provide access to the rich and evolving ecosystem of open source R and Python.

An example of the augment approach was highlighted in <a href="https://www.trustradius.com/reviews/rstudio-2020-12-18-15-36-31" target="_blank" rel="noopener noreferrer"> recent TrustRadius review</a>, where an IT Analyst at a real estate company shared:

> "If you are an R user and you have models or reports that you work with regularly, RStudio is a great solution. I also find it handy for building quick apps using `Flask-Admin` for user config tables that support Tableau or Power BI reports for budget tables, KPI targets, and metric targets."

## Data Science and BI in Your Organization

In our next posts, we will dive more deeply into the strengths and challenges of self-service BI tools and recommend specific approaches and points of integration to consider. For now, if you are part of a BI or Data Science team in an organization, I encourage you to reach out to your counterparts and explore how you can better tackle your common purpose of improving decision making in your organization.

We're happy to help, so if you'd like to learn more about how RStudio products can help augment and complement your BI approaches,  you can <a href="https://rstudio.chilipiper.com/book/schedule-time-with-rstudio" target="_blank" rel="noopener noreferrer">set up a meeting with our Customer Success team</a>, or start a conversation <a href="https://www.linkedin.com/in/loubajuk/" target="_blank" rel="noopener noreferrer">with me on LinkedIn</a>. 

## To Learn More

-   Read <a href="https://rstudio.com/about/customer-stories/brown-forman/" target="_blank" rel="noopener noreferrer">this customer spotlight</a> to learn how Brown-Forman used RStudio products to help their data science team "turn into application developers and data engineers without learning any new languages or computer science skills."
-   Read more about the importance of <a href="https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/" target="_blank" rel="noopener noreferrer">interoperability</a> and how <a href="https://blog.rstudio.com/2021/01/13/one-home-for-r-and-python/" target="_blank" rel="noopener noreferrer">RStudio provides a single home for R and Python</a>
-   If you'd like to know <a href="https://blog.rstudio.com/2020/11/17/an-interview-with-lou-bajuk/" target="_blank" rel="noopener noreferrer">why RStudio focuses on code-friendly data science</a>, read this recap of a recent podcast.
- At rstudio::conf 2020, George Kastrinakis from the Financial Times <a href="https://rstudio.com/resources/rstudioconf-2020/building-a-new-data-science-pipeline-for-the-ft-with-rstudio-connect/" target="_blank" rel="noopener noreferrer">presented a case study</a> on building a new data science pipeline using R and RStudio Connect.
