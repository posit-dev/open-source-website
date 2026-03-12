---
title: 'BI and Open Source Data Science: Strengths and Challenges'
people:
  - Lou Bajuk
date: '2021-03-11'
slug: bi-and-ds2-strengths-challenges
categories:
  - Data Science Leadership
tags:
  - BI tools
description: Continuing our series on self-service BI tools and code-friendly, open source data science, in this post we dive into the strengths and challenges of the different approaches.
blogcategories:
- Data Science Leadership
events: blog
alttext: image of old kitchen scales 
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---

<sup>Photo by <a href="https://unsplash.com/@romankraft?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Roman Kraft</a> on <a href="https://unsplash.com/s/photos/balance?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Unsplash</a></sup>

In <a href="https://blog.rstudio.com/2021/03/04/bi-and-ds-part1/" target="_blank" rel="noopener noreferrer">our first post in this series</a>, we started examining a critical aspect of <a href="https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/" target="_blank" rel="noopener noreferrer">interoperability</a>: the intersection between Business Intelligence (BI) and data science platforms. The two approaches share a common goal: delivering rich interactive applications and dashboards that can be shared with others to improve their decision-making. However, this common purpose often leads to the tools (and the teams that support and use them) being seen as competitors for software budgets and executive mindshare in a large organization.

In the previous post, we reviewed two high-level approaches for combining these tools to deliver increased value to an organization: Using data science to either **complement** or **augment** self-service BI. That is, using the tools either side by side to tackle different use cases, or together to tackle a single analytic problem.

In this post, we'll focus on the strengths and challenges of the two approaches, to help you identify which tool to use in different situations.

## **Strengths and Challenges of Self-Service BI**

Self-Service BI tools, such as Tableau, PowerBI or Spotfire, are widely used because they allow business analysts to:

-   **Explore and visualize data without coding skills or being dependent on data scientists:** While these business users may not understand R, Python, or advanced modeling methods, they are typically very familiar with the data and the business problems they are trying to solve. These BI tools enable them to apply that knowledge.
-   **Share analyses and interactive dashboards:** Another key strength of BI tools is that users can easily share these analyses with others, typically without relying on IT for deployment. More advanced users with specialized skills can create interactive dashboards and applications, enabling other users to apply the same analytic approach in the future.
-   **Do self-service reporting and scheduling:** Many organizations require consistent, visually-appealing reports on a regular schedule, for both internal stakeholders and clients. BI tools usually provide a way to schedule the updates of reports, and then notify stakeholders of the updates.
-   **Support data-driven organizations:** When these tools are adopted as a corporate standard and widely deployed, they provide a common platform for sharing insights and supporting decision-making. That common platform helps support a data-driven culture in an organization.

Despite the strengths of BI tools, they also present challenges that may not be obvious at first glance. BI tools:

-   **Are difficult to adapt and inspect:** Analyses and visualizations are typically heavily tied to the specific data schema they are built on, making them difficult to adapt when the underlying data changes substantially. Data transformations are often obscured in a series of point-and-click actions, which reinforces this challenge. This makes extending an analysis to new data difficult, errors difficult to find, and processes challenging to audit.
-   **Are limited by their black box nature:** While modern BI tools have a wide range of visualizations and some basic statistical tools, they are largely constrained by the proprietary capabilities their vendors implement. Going beyond these standard options often requires heroic effort, such as embedding custom javascript visualizations or custom extension development in C++. Similarly, these tools have limited workflow and application development capabilities, so automating a series of steps for data retrieval and transformation can be difficult. Tasks such as integrating specialized data sources (e.g., web scraping) can be impossible with standard functionality.
-   **Struggle with enriched or wide data:** While data access is a major focus, these tools typically provide limited ways to interact with "enriched" or unstructured data. BI tools may also have challenges when dealing with many variables. Interactive visualization of wide data sets can overwhelm users, who may be uncertain which variables are most relevant. This typically requires the application of advanced analytic methods, such as eliminating correlated columns or principal component analysis, to reduce the data.
-   **Create uncertain conclusions:** Humans are hardwired to see patterns and create explanations for them--even if they are not real. It can be very difficult for a BI user to know if an apparent pattern can be relied upon for future decision making. In some cases, it can be difficult to draw any conclusions at all without the application of more advanced analytic methods.
-   **Include limited data science and machine learning capabilities:** BI platforms typically have native support only for very basic predictive/ML models. It can also be very difficult to embed the work done by a data science team in the BI product, since that often requires data scientists to work with unfamiliar development environments and limited integration points. This slows the process, hampers iteration and reduces productivity.
-   **Require skills that aren't easily transferred:** Getting the most out of these BI tools, especially creating reusable analyses, requires specialized skills developed over time. If the analyst moves to another organization, or their organization decides not to renew expensive commercial software, these platform-specific skills are wasted. Similarly, if you wish to share your analyses with colleagues who may not have access to the tool, it will be difficult for them to run the analysis themselves. Or if they can, the analyses may be difficult to reuse, adapt and inspect, as described above.

## **Strengths and Challenges of Code-Friendly Data Science**

When compared with self-service BI tools, open source data science tools using R and Python provide:

-   **A wide range of open source capabilities:** Users can draw on a broad spectrum of capabilities, ranging from classical models to cutting-edge deep learning techniques. These expansive libraries ensure that data scientists will always have the right tool for the analytic problem at hand.
-   **The benefits of code:** Code-based approaches are inherently reusable, extensible and inspectable. Changes are easy to track over time using version control. These aspects of code actually reduce complexity compared to point-and-click solutions. Reproducible code becomes core intellectual property for your organization, making it easier to solve new problems in the future and increase the aggregate value of your data science work.
-   **Fully customizable data products:** Code-based solutions allow you to fully customize reports, dashboards, visualizations, and applications, allowing you to tailor them to the needs of your decision-makers. In addition, these data products are built using the same languages that data scientists already know, instead of requiring them to learn a new framework.
-   **Broad interoperability**: As discussed <a href="https://blog.rstudio.com/2020/07/15/interoperability-maximize-analytic-investments/" target="_blank" rel="noopener noreferrer">in this blog post</a>, teams need interoperable tools that give a data scientist direct access to different platforms and tools. This access is critical because it keeps data scientists more productive and helps ensure better utilization of IT and data resources. The ability to use data in many different formats, including unstructured and non-traditional data, makes it far easier to enrich analyses and reports.
-   **Transferable skills and analyses:** When you use open source as the core of your data science, you are not constrained by commercial platforms. This means that you can use your hard-won skills at any organization, regardless of what software they purchase, and you can share your analyses and insights with anyone, regardless of what software they can afford. This premise is the heart of <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">RStudio's mission to support open source data science</a>.
-   **A wider pool of potential talent:** R and Python are widely adopted, and taught almost universally in colleges and universities. This allows organizations to draw on a much wider pool of knowledgeable data scientists when hiring. They can be confident that these new hires will already be familiar with the languages, and become productive members of the organization much more quickly.

Despite these strengths, teams which adopt open source, code-friendly data science do encounter a number of challenges. Open source data science tools:

-   **Necessitate coding skills**: Business users who are used to Excel often find code-based approaches foreign and inaccessible and therefore hesitate to deploy them. While Shiny applications and other data products can easily be used by stakeholders unfamiliar with R or Python, these data products require someone familiar with the languages to develop them.
-   **May require package and environment management:** A key strength of the R and Python ecosystems is the broad universe of packages. However, unless data science teams make special efforts, this rapidly evolving ecosystem can make it difficult to maintain stable, reproducible applications as those packages change over time.
-   **Provide limited native deployment capabilities:** Open source data science teams often must create their own ways to deploy and share applications and dashboards to their community of users. These homegrown solutions can be difficult to develop and maintain and may run into objections from IT groups.
-   **Don't include enterprise security, scalability and cloud features:** Similarly, R and Python do not provide many enterprise-required features as part of the open source ecosystem. Organizations frequently struggle to support large teams, whether for development or deployment, on premise or in the cloud.

<style type="text/css">
p           { padding: 0 0 8px 0; }
th          { font-size: 90%; background-color: #4D8DC9; color: #fff; vertical-align: middle; }
td          { font-size: 80%; background-color: #F6F6FF; vertical-align: top; line-height: 16px; }
td.approach { font-size: 90%; background-color: #4D8DC9; color: #fff; vertical-align: middle; }
caption     { padding: 0 0 0 0; }
table       { width: 100%; padding: 0 0 16px 0; }
th.approach  { width: 24%; }  
th.strengths { width: 38%; vertical-align: middle; }
th.challenges { width: 38%; vertical-align: middle; }
table thead th {
  border-bottom: 1px solid #ddd;
}
th {
  font-size: 90%;
  background-color: #4D8DC9;
  color: #fff;
  vertical-align: center 
}
td {
  font-size: 80%;
  background-color: #F6F6FF;
  vertical-align: top;
  line-height: 16px;
}
caption {
  padding: 0 0 16px 0;
}
table {
  width: 100%;
}
th.problem {
  width: 15%;
}
th.solution {
  width: 15%;
}
th.proscons {
  width: 35%;
}
th.options {
  width: 35%;
}
div.action {
  padding: 0 0 16px 0;
}
div.procon {
  padding: 0 0 0 0;
}
td.ul {
  padding: 0 0 0 0;
  margin-block-start: 0em;
}
table {
  border-top-style: hidden;
  border-bottom-style: hidden;
  border-collapse: separate;
  text-indent: initial;
  border-spacing: 2px;
}
table>thead>tr>th, .table>thead>tr>th {
  font-size: 0.7em !important;
}
table>tbody>tr>td {
  line-height: inherit;
  vertical-align: baseline;
}
table tbody td, td.approach {
  font-size: 14px;
}
</style>
<div class="text-center mt-5">
<caption><b>Table 1: Summary of the strengths and challenges of using Self-Service BI and open source data science tools.</b></caption>
</div>
<table>
  
  <thead>
  <tr>
    <th></th>
    <th class="strengths"> Strengths </th>
    <th class="challenges"> Challenges </th>
  </tr>
  </thead>
  <tr><td class="approach"><strong>Self-service BI Tools</strong></td>
      <td><ul><li>Explore and visualize data without coding skills</li>
                       <li>Share analyses and interactive dashboards</li>
                       <li>Do self-service reporting and scheduling</li>
                       <li>Support data-driven organizations</li>
    </ul></td>
    <td>
    <ul><li>Are difficult to adapt and inspect</li>
        <li>Are limited by their black box nature</li>
        <li>Struggle with enriched or wide data</li>
        <li>Create uncertain conclusions</li>
        <li>Include limited data science and machine learning capabilities</li>
        <li>Require skills that aren't easily transferred</li>
    </ul>
    </td>
  </tr>
  <tr>
    <td class="approach"><strong>Open Source Data Science Tools</strong></td>
    <td>
    <ul><li>Provide a wide range of open source capabilities</li>
        <li>Unlock the benefits of code</li>
        <li>Allow fully customizable data products</li>
        <li>Have broad Interoperability</li>
        <li>Create transferable skills and analyses</li>
        <li>Tap a wider pool of potential talent</li>
    </ul>
    </td>
    <td><ul>
    	<li>Necessitate coding in R or Python</li>
      <li>May require package and environment management</li>
      <li>Provide limited native deployment capabilities</li>
      <li>Don't include enterprise security, scalability and cloud features</li>
      </ul>
    </td>
  </tr>
</table>

## **RStudio Tackles the Open Source Challenges**

The challenges for open source data science summarized above are significant--and are the specific challenges that RStudio addresses.

-   We are <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">dedicated to the proposition</a> that code-friendly data science is uniquely powerful, and that everyone can learn to code. We support this through <a href="https://education.rstudio.com/" target="_blank" rel="noopener noreferrer">our education efforts</a>, our <a href="https://community.rstudio.com/" target="_blank" rel="noopener noreferrer">Community site</a>, and making R easier to use through our open source projects such as the <a href="https://www.tidyverse.org/" target="_blank" rel="noopener noreferrer">tidyverse</a>.
-   <a href="https://rstudio.com/products/team/" target="_blank" rel="noopener noreferrer">RStudio Team</a> provides security, scalability, package management and the centralized management of development and deployment environments, delivering the enterprise features many organizations require.
-   <a href="https://rstudio.com/products/cloud/" target="_blank" rel="noopener noreferrer">RStudio Cloud</a> and <a href="https://rstudio.com/products/shinyapps/" target="_blank" rel="noopener noreferrer">Shinyapps.io</a> enable data scientists to develop and deploy data products on the cloud.

## **Complement and Augment your BI Tools**

Code-friendly data science with R and Python is powerful, and can be even more valuable when used in conjunction with self-service BI tools (as discussed <a href="https://blog.rstudio.com/2021/03/04/bi-and-ds-part1/" target="_blank" rel="noopener noreferrer">in our first post</a>).

The strengths and challenges above show that:

-   BI tools are powerful and have a lower barrier to entry for most users, but have limits to their flexibility and analytic depth. This limits the complexity of the questions they can answer.
-   Open source data science has a higher barrier to entry, requiring coding skills for development. But its flexibility and analytic power is nearly limitless. This allows organizations to answer the most complex questions they have.

Organizations must consider this balance, between the barrier to entry and the complexity of the questions that need to be answered, when choosing an approach. In future blog posts, we will dive more deeply into this topic, explore specific integration points for BI and Data Science tools, and provide concrete recommendations.

We're happy to help you explore these topics, so if you'd like to learn more about how RStudio products can help augment and complement your BI approaches, you can <a href="https://rstudio.chilipiper.com/book/schedule-time-with-rstudio" target="_blank" rel="noopener noreferrer">set up a meeting with our Customer Success team</a>.

## **To Learn More**

-   For an example of how a data science team used RStudio products to create and share applications without needing to learn new languages, see this <a href="https://rstudio.com/about/customer-stories/brown-forman/" target="_blank" rel="noopener noreferrer">customer story from Brown-Forman</a>.
-   Read about <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">RStudio's mission to support open source data science</a> and why we've <a href="https://blog.rstudio.com/2020/01/29/rstudio-pbc/" target="_blank" rel="noopener noreferrer">dedicated ourselves to that mission as a Public Benefit Corporation</a>.

