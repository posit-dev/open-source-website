---
title: 'BI and Data Science: Matching Approaches to Applications'
people:
  - Lou Bajuk
date: '2021-03-18'
slug: bi-and-data-science-the-tradeoffs
categories:
  - Data Science Leadership
tags:
  - BI tools
description: In this post, we'll provide some insights from organizations who have used both types of tools and give some guidance about which you should use when.
resources:
  - name:  "hero"
    src:   "thumbnail.jpg"
    title: "Lit matches"
blogcategories:
  - Data Science Leadership
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---
<sup>Photo by <a href="https://unsplash.com/@jamie452?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jamie Street</a> on <a href="/s/photos/match?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></sup>
  
In the previous posts in our series on Data Science and Business Intelligence, we first discussed how <a href="https://blog.rstudio.com/2021/03/04/bi-and-ds-part1/" target="_blank" rel="noopener noreferrer">data science can either complement or augment self-service BI tools</a> to deliver more combined value. We then explored the <a href="https://blog.rstudio.com/2021/03/11/bi-and-ds2-strengths-challenges/" target="_blank" rel="noopener noreferrer">strengths and challenges</a> of the two approaches, both of which aim to help an organization get more insights from their data and to make better decisions.

In this post, we'll provide insights from organizations who have used both types of tools and give some guidance about which you should use when. We'll also set the stage for future blog posts where we will explore specific integration points for BI and Data Science tools.

## Don't Get Trapped into a False Choice

In our prior post, we explored the <a href="https://blog.rstudio.com/2021/03/11/bi-and-ds2-strengths-challenges/" target="_blank" rel="noopener noreferrer">strengths and challenges</a> of both BI tools and open source data science. We won't repeat those arguments here. Instead, we'll hear from users who seem to understand that both approaches have their place.

BI tools are often an easier place for an organization to start when approaching an analytic problem, They provide a lower barrier to entry for the typical business user, who may not be comfortable coding in R or Python. The built-in features make it easy to visualize, explore and analyze data using a point-and-click approach and then to share that analysis with others.

For example, this user prefers Power BI for creating quick and easy visualizations, but switches to R and Shiny for their highly interactive user interfaces.

> *"Power BI is an easy to build visualization tool widely used in our organization to make data accessible to non-data people. This is a really great tool when we want to create a dashboard for trends and track some metrics. But it becomes very difficult when we want to enable high levels of user interactivity with the dashboard. That's where R Shiny helped us to build intuitive and highly interactive user interfaces."*
>
>      -- <a href="https://www.trustradius.com/reviews/rstudio-2020-11-19-19-05-28" target="_blank" rel="noopener noreferrer">A marketer at a large telecommunications firm</a>

Meanwhile this Biotech firm views Spotfire and Tableau as fine products so long as you are satisfied with their built-in capabilities, but sees R being more flexible.

> "*RStudio is code based, so in the beginning tools like Spotfire and Tableau have [their] advantages since many things are already built in, but in terms of flexibility RStudio will win over the longer term.*"
>
>      -- <a href="https://www.trustradius.com/reviews/rstudio-2020-12-01-23-31-23" target="_blank" rel="noopener noreferrer">A team lead in a biotech company</a>


The individuals below describe how they apply this flexibility and power from two different industry perspectives. 
The first is from a financial industry leader.

> *"Most of the work the data scientists did used the R language. They did a great job satisfying management's constant barrage of questions because iterative analysis is so easy with tools like R, and the powerful visualization tools made communication of results easy for sales people to grasp. As the CEO, I was gratified at how clear the presentations were and at how quickly presenters answered my difficult questions, in some cases on the fly during the presentations.*
>
> *As an R user myself, I know its code-based workflow lends itself to rapid iteration while, at the same time, documenting the process used. It was easy to unroll the tape to see every step that led to any conclusion."*
>
>      <a href="https://blog.rstudio.com/2020/10/13/open-source-data-science-in-investment-management/" target="_blank" rel="noopener noreferrer">-- Art Steinmetz</a>, former Chairman and CEO of Oppenheimer Funds

The second individual describes how he uses R in the beverages industry:

> *"The R ecosystem has vast power to quickly solve problems. With R, I can incorporate nearly any AI/ML model into a dashboard or Shiny app, without being reliant on proprietary data science tools. Executives can be confident I am using the best analytic approach for a given problem, and I can rapidly apply new approaches as they become available."*
>
>      -- Paul Ditterline, Director of Data Science at Heaven Hill Brands

While these may be only anecdotal evidence, they do show awareness of both approaches to data analysis and provide some color into why companies opt for each solution. They illustrate that as the questions get more complex, requiring greater analytic depth to answer, and more customization in how the analysis is done and presented, BI tools may struggle. Users will encounter a relatively low ceiling to the complexity of questions they can answer.

On the other hand, code-friendly data science tools represent a relatively high barrier to entry. They require those who create the analyses to have some understanding of coding in R and Python, and familiarity with applying and interpreting advanced analytic methods to get the most out of the tools. However, the flexibility and analytic breadth of code-friendly data science combines to provide a very high ceiling for answering difficult, valuable questions for an organization.

This just leaves open the question, "How should I select my approach?"


## Match Your Data Science Approach to Application Needs

We expect firms to continue struggling with this tradeoff between BI tools and open source data science for years to come. As we argued in our first post on the topic, this isn't about choosing between the two approaches, but how to exploit the strengths of each while mitigating their challenges.

In the table below, the *Use When You...* column augments the table we presented last week. While this guide won't be correct for every case, it at least provides a guideline for those times a data science leader needs a quick answer to an urgent project.

<style type="text/css">
p           { padding: 0 0 8px 0; }
th          { font-size: 90%; background-color: #4D8DC9; color: #fff; vertical-align: middle; }
td          { font-size: 80%; background-color: #F6F6FF; vertical-align: top; line-height: 16px; }
td.approach { font-size: 90%; background-color: #4D8DC9; color: #fff; vertical-align: middle; }
caption     { padding: 0 0 0 0; }
table       { width: 100%; padding: 0 0 16px 0; }
th.approach  { width: 16%; }  
th.strengths { width: 28%;; vertical-align: middle; }
th.challenges { width: 28%; vertical-align: middle; }
th.use { width: 28%; vertical-align: middle; }
table      { border-top-style: hidden; border-bottom-style: hidden;}
</style>

<table>
  <tr>
    <th class="approach">
    </th>
    <th class="strengths"><strong>Strengths</strong>
    </th>
    <th class="challenges"><strong>Challenges</strong>
    </th>
    <th class="use"><strong>Use When You...</strong>
    </th>
  </tr>
  <tr>
    <td class="approach"><strong>Self-service BI Tools</strong>
    </td>
    <td>
      <ul>
	<li>Explore and visualize data without coding skills</li>
	<li>Share analyses and interactive dashboards</li>
	<li>Do self-service reporting and scheduling</li>
	<li>Support data-driven organizations</li>
	</li>
      </ul>
    </td>
    <td>
      <ul>
	<li>Are difficult to adapt and inspect</li>
	<li>Are limited by their black box nature</li>
	<li>Struggle with enriched or wide data</li>
	<li>Create uncertain conclusions</li>
	<li>Include limited data science and machine learning</li> capabilities
	<li>Require skills that aren't easily transferred</li>
      </ul>
    </td>
    <td>
      <ul>
	<li>Must support analysis and sharing with people without coding skills</li>
	<li>Want to produce descriptive analytics and general reporting</li>
	<li>Know that your use is covered by your BI Tool's feature set</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td class="approach"><strong>Open Source Data Science</strong>
    </td>
    <td>
      <ul>
	<li>Provide a wide range of open source capabilities</li>
	<li>Unlock the benefits of code</li>
	<li>Allow fully customizable data products</li>
	<li>Have broad Interoperability</li>
	<li>Create transferable skills and analyses</li>
	<li>Tap a wider pool of potential talent</li>
      </ul>
    </td>
    <td>
      <ul>
	<li>Necessitate coding in R or Python</li>
	<li>May require package and environment management</li>
	<li>Provide limited native deployment capabilities</li>
	<li>Don't include enterprise security, scalability and cloud features</li>
      </ul>
    </td>
    <td>
      <ul>
	<li>Need flexibility to tackle novel problems</li>
	<li>Expect the analysis to be reused and will need to be reproducible without the code creator</li>
	<li>Need to solve harder questions, which require data science and ML on complex data </li>
	<li>Must  support complex decision-making with deep interactivity</li>
      </ul>
    </td>
  </tr>
</table>

*Table 1: Guidelines for when you should apply BI Tools or open source data science.*

## Summary

 RStudio is <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">dedicated to the proposition</a> that code-friendly data science is uniquely powerful, and that everyone can learn to code. We support this through <a href="https://education.rstudio.com/" target="_blank" rel="noopener noreferrer">our education efforts</a>, our <a href="https://community.rstudio.com/" target="_blank" rel="noopener noreferrer">Community site</a>, and making R easier to use through our open source projects such as the <a href="https://www.tidyverse.org/" target="_blank" rel="noopener noreferrer">tidyverse</a>. Our software is already used by millions of people to analyze data every day.

However, code-friendly data science does present a higher barrier to entry compared to BI tools, which are very valuable for the wider community of analysts and business users in an organization. Because of this, it is critical to leverage both, and use data science to augment and complement your BI tools.

In our next posts, we will explore specific points of integration between these tools. We're happy to help you explore these topics, so if you'd like to learn more about how RStudio products can help augment and complement your BI approaches, you can <a href="https://rstudio.chilipiper.com/book/schedule-time-with-rstudio" target="_blank" rel="noopener noreferrer">set up a meeting with our Customer Success team</a>.

## To Learn More

-   See the <a href="https://blog.rstudio.com/2021/03/11/bi-and-ds2-strengths-challenges/" target="_blank" rel="noopener noreferrer">second blog post in our BI series</a> for more information on how RStudio tackles the challenges of open source data science listed in the table above. <a href="https://rstudio.com/products/team/" target="_blank" rel="noopener noreferrer">RStudio Team</a> provides security, scalability, package management and the centralized management of development and deployment environments, delivering the enterprise features many organizations require.
-   Read this recent interview for more information on <a href="https://blog.rstudio.com/2020/11/17/an-interview-with-lou-bajuk/" target="_blank" rel="noopener noreferrer">Why RStudio focuses on code-friendly data science</a>.
-   For more information on what RStudio is doing to make deep learning and AI available in the R ecosystem, see the <a href="https://blogs.rstudio.com/ai/" target="_blank" rel="noopener noreferrer">RStudio AI blog</a>.
-   Explore the enterprise value of an open source, code-friendly approach in our blog post series, <a href="https://blog.rstudio.com/2020/06/24/delivering-durable-value/" target="_blank" rel="noopener noreferrer">importance and benefits of Serious Data Science</a>.

