---
title: Code-First Data Science for the Enterprise
people:
  - Lou Bajuk
  - Nick Rohrbaugh
date: '2021-05-12'
slug: code-first-data-science-for-the-enterprise2
categories:
  - Data Science Leadership
tags:
  - Python
  - BI tools
  - Code-First
description: While you may already be a practitioner of code-first data science with R or Python, chances are you work within a larger organization with many analytic tools. In this post, we give you some advice on navigating this landscape, and convincing others in your organization of the value of code-first data science.
resources:
- name: "heart-hero"
  src: "i-heart-code.png"
  title: "I Heart Code"
- name: "webinar-hero"
  src: "code-first-ds-webinar-hero.png"
  title: "Webinar - Why Your Enterprise Needs Code-First Data Science"
blogcategories:
  - Data Science Leadership
events: blog
alttext: the word code in a heart
image: thumbnail.png
ported_from: rstudio
port_status: raw
---

<style type="text/css">
th          { font-size: 120%; background-color: #4D8DC9; color: #fff; vertical-align: center }
td          { font-size: 100%; background-color: #F6F6FF; vertical-align: top; line-height: 16px; 
  padding-bottom:0px;
  padding-right:10px;
  padding-left:15px; 
  }
table       { width: 100%; }
table      { border-top-style: hidden; border-bottom-style: hidden;padding: 30px 0 20px 0}
</style>


As a data scientist, or as a leader of a data science team, you know the power and flexibility that open source data science delivers. However, if your team works within a typical enterprise, you compete for budget and executive mindshare with a wide variety of other analytic tools, including self-service BI and point-and-click data science tools. Navigating this landscape, and convincing others in your organization of the value of open source data science, can be difficult. In this blog post, we draw on <a href="/resources/why-your-enterprise-needs-code-first-data-science/"> our recent webinar on this topic</a> to give you some talking points to use with your colleagues when tackling this challenge.  

However, it is important to keep in mind that “code-first” does not mean “code only.” While code is often the right choice, most organizations need multiple tools, to ensure you have the right tool for the task at hand. 

## The Pitfalls of BI Tools and Codeless Data Science

There are multiple ways to approach any given analytic problem. At their core, various data science and BI tools share many aspects. They all provide a way of drawing on data from multiple data sources, and to explore, visualize and understand that data in open-ended ways. Many tools support some way of creating applications and dashboards that can be shared with others to improve their decision-making.

Since these very different approaches can end up delivering applications and dashboards that may (at first glance) appear very similar, the strengths and nuances of the different approaches can be obscured to decision makers, especially to executive budget holders—which leads to the potential competition between the groups.

However, when taking a codeless approach, it can be difficult to achieve some critical analytic best practices, and to answer some very common and important questions:

* **Difficulty tracking changes and auditing work**: When modifications and additions are obscured in a series of point-and-click steps, it can be very challenging to answer questions like:
  * Why did we make this decision in our analysis?
  * How long has this error gone unnoticed?
  * Who made this change?
* **No single source of truth**: Without a centralized way of sharing and storing analyses and reports, different versions and spreadsheets can proliferate, leading to questions like:
  * Is this the most recent [data, report, dashboard]?
  * Is the file labeled `sales-data 2020-12 final FINAL Apr 21 NR (4).xlsx` **really** the most recent version of the analysis?
  * Where do I find the [data, report, dashboard] I am looking for? And who do I have to email to get the right link?
* **Difficult to extend and reproduce your work**: When you are depending on a proprietary platform for your analysis, with the details hidden behind the point-and-click interface, you might face questions like:
  * What did our model say 6 months ago?
  * Can I apply this analysis to this new (slightly different) data/problem?
  * Are we actually meeting the relevant regulatory requirements?
  * Is our work truly portable? Will others be able to reproduce and confirm our results?

At best, wrestling with questions like these will distract an analytics team, burning precious time that could be spent on new, valuable analyses. At worst, stakeholders end up with inconsistent or even incorrect answers because the analysis is wrong, not the correct version, or not reproducible. This can fundamentally undermine the credibility of the analytics team. Either way, the potential impact of the team for supporting decision makers is greatly reduced.

## The benefits of code-first data science

<a href="/about/">RStudio’s mission</a> is to create free and open-source software for data science, because we fundamentally believe that this enhances the production and consumption of knowledge, and facilitates collaboration and reproducible research.  

At the core of this mission is a focus on a code-first approach. Data scientists grapple every day with novel, complex, often vaguely-defined problems with potential value to their organization. Before the solution can be automated, someone needs to figure out how to solve it. These sorts of problems are most easily approached with code.

**With Code, the answer is always yes!**

Code is:

* **Flexible**: With code, there are no black box constraints. You can access and combine all your data, and analyze and present it exactly as you need to.
* **Iterative**: With code, you can quickly make changes and updates in response to feedback, and then share those updates with your stakeholders.
* **Reusable and extensible**: With a code-first approach, you can tackle similar problems in the future by applying your existing code, and extend that to novel problems as circumstances change. This makes code a fundamental source of Intellectual Property in your organization.
* **Inspectable**: With code, coupled with version control systems like git, you can track what has changed, when, by whom, and why. This helps you discover when errors might have been introduced, and audit the analytic approach.
* **Reproducible**: When combined with environment and package management (such as the capabilities provided by <a href="/products/team/">RStudio Team</a>, you can ensure that you will be able to rerun and verify your analyses. And since your data science is open source at its core, you can be confident that others will be able to rerun and reproduce your analysis, without being reliant on expensive proprietary tools.


<table>
  <thead>
  <tr>
    <th class="problem"> Codeless Problem </th>
    <th class="solution"> Code-First Solution </th>
  </tr>
  </thead>
  <tr>
    <td><p>Difficulty tracking changes and auditing work</p></td>
    <td>
      <p>Code, coupled with version control systems like git, to track what changed, when, by whom, and why.</p>
      <p>Code can be logged when run for auditing and monitoring.</p>
    </td>
</tr>
  <tr>
    <td>
      <p>No single source of truth</p>
    </td>
    <td>
      <p>Centralized tools to create a single source of truth for data, dashboards, and models.</p>
      <p>Version control to track multiple versions of code separately without creating conflicts.</p>
    </td>
</tr>
  <tr>
    <td><p>Difficult to extend and reproduce work</p></td>
    <td>
    <p>Code enables reproducibility by explicitly recording every step taken.</p>
    <p>Open-source code can be deployed on many platforms, and is not dependent on proprietary tools.</p>
    <p>Code can be copied, pasted, and modified to address novel problems as circumstances change.</p>
</td>
  </tr>
  <tr>
    <td><p>Black box constraints on how you analyze your data and present your insights</p></td>
    <td><p>Access and combine all your data, and analyze and present it exactly as you need to, in the form of tailored dashboards and reports.</p>
<p>Pull in new methods and build on other open source work without waiting for proprietary features to be added by vendors.</p></td>
  </tr>
</table>
*A summary of how a code-first approach helps tackle codeless challenges*

## Objections to Code-First Data Science

When discussing the benefits of a code-first approach within your organization, you may hear some common objections:

* **“Coding is too hard!”**: In truth, it’s never been easier to learn data science with R. RStudio is dedicated to the proposition that code-first data science is uniquely powerful, and that everyone can learn to code. We support this through <a href="https://education.rstudio.com/" target="_blank">our education efforts</a>, <a href="https://community.rstudio.com/" target="_blank">our Community site</a>, and making R easier to learn and use through our open source projects such as the <a href="https://www.tidyverse.org/" target="_blank">tidyverse</a>.
* **“Does code-first mean only code?”**: Absolutely not. It’s about choosing the right tool for the job, which is why RStudio focuses on the idea of <a href="https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/">Interoperability</a> with the other analytic frameworks in your organization, <a href="https://blog.rstudio.com/2021/01/13/one-home-for-r-and-python/">supporting Python alongside R</a>, and <a href="https://blog.rstudio.com/2021/03/18/bi-and-data-science-the-tradeoffs/">working closely with BI tools</a> to reach the widest possible range of users.
* **“But R doesn’t provide the enterprise features and infrastructure we need!”**: Not true. RStudio’s professional product suite, <a href="/products/team/">RStudio Team</a>, provides security, scalability, package management and centralized administration of development and deployment environments, delivering the enterprise features many organizations require. Our hosted offerings, <a href="https://rstudio.cloud/" target="_blank">RStudio Cloud</a> and <a href="https://www.shinyapps.io/" target="_blank">Shinyapps.io</a>, enable data scientists to develop and deploy data products on the cloud, without managing their own infrastructure.  


## To Learn More 

If you’d like to learn more about the advantages of code-first data science, and see some real examples in action, watch the free, on-demand webinar <a href="/resources/why-your-enterprise-needs-code-first-data-science/">Why Your Enterprise Needs Code-First Data Science</a>. Or, you can <a href="http://rstd.io/r_and_python" target="_blank">set up a meeting directly with our Customer Success team</a>, to get your questions answered and learn how RStudio can help you get the most out of your data science.  

  
<a class="btn btn-primary" href="http://rstd.io/r_and_python" target="_blank">Schedule a Conversation </a>
<a class="btn btn-info" href="https://www.rstudio.com/resources/why-your-enterprise-needs-code-first-data-science/" target="_blank">Watch the full code-first webinar </a>
