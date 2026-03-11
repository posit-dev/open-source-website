---
title: Does your Data Science Team Deliver Durable Value?
people:
  - Lou Bajuk
  - Carl Howe
date: '2020-06-24'
slug: delivering-durable-value
categories:
- Data Science Leadership
tags:
- data science
description: Delivering persistent value over the long haul from your data science
  team requires reusability, reproducibility, and up-to-date insights, built on a
  sustainable platform.
resources:
- name: big-rock
  src: big-rock-hero.jpg
  title: Large durable rock
- name: b-corp
  src: logo-lockup.svg
  title: logo-lockup
blogcategories:
- Data Science Leadership
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---

<style type="text/css">
  table {
  border-top: 1px solid rgba(117,170,219,.6);
  border-bottom: 1px solid rgba(117,170,219,.6);
  margin: 25px 0 15px 0;
  padding: 40px 35px 35px 35px;
  width: 100%;
  }
  tr:nth-child(even) {
  background: #ffffff;
  }
  tr {
  vertical-align: top;
  }
  td {
  text-align: left;
  padding: 2px 5px;
  }
  th {
  font-size: 24px;
  font-weight: 400;
  padding-bottom: 15px;
  text-align: left;
  }
  td li {
  font-size: 15px;
  }
  .quote-spacing {
  padding:0 80px;
  }
  .quote-size {
  font-size: 140%;
  line-height: 34px;
  }
  @media only screen and (max-width: 600px) {
    .quote-spacing {
    padding:0;
    }
    .quote-size {
    font-size: 120%;
    line-height: 28px;
    }
    table {
    padding: 40px 0px 35px 0px;
    }
  }
</style>


<sup>Photo by <a href="https://unsplash.com/@zoltantasi?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Zoltan Tasi</a> on <a href="https://unsplash.com/s/photos/boulder-rock?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Unsplash</a></sup>

In a recent series of blog posts, we introduced the idea of <a href="https://blog.rstudio.com/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">Serious Data Science</a> to help tackle the challenges of effectively implementing data science in an organization. We then focused on the importance of <a href="https://blog.rstudio.com/2020/06/02/is-your-data-science-credible-enough/" target="_blank" rel="noopener noreferrer">delivering insights that are credible with your stakeholders</a> and <a href="https://blog.rstudio.com/2020/06/09/is-your-data-science-team-agile/" target="_blank" rel="noopener noreferrer">approaching data science projects in an agile way</a>. However, once you’ve created valuable insights, the challenge is then how to continue to deliver those insights in a repeatable and sustainable way. Otherwise, your initial impact may be short-lived. 

## Obstacles to providing ongoing value with data science

Once a valuable insight or tool has reached a decision maker, organizations struggle with maintaining and growing the value of these data science investments over time. Far too often, they need to start from scratch when solving a new problem or are forced to painfully reimplement old analyses when they are unexpectedly needed. Some of the key areas data science teams struggle with include:

*   **Lack of reuse:** Especially when your data science insights are locked up in a spreadsheet or a point-and-click tool, it can be nearly impossible to reuse that analysis in new ways. This forces data scientists to start from scratch when a new problem comes along and makes it difficult to build an analytical toolbox of valuable intellectual property over time. 
*   **Lack of reproducibility:** When you share your analysis with someone else, they may find it difficult to reproduce it if they don’t have identical versions of tools and libraries. As these tools evolve, you may find it impossible to recreate your analyses. Both of these situations are frustrating, leading to unnecessary work and anxiety as you attempt to figure out what element of the environment has changed.
*   **Stale insights and repetitive work:** While a stakeholder may value your analysis today, they'll likely want to run it again with updated data in the future. If your analysis is static, it quickly becomes stale which forces the decision maker to either make a decision on old data or to ask you for an update. These out-of-date analyses lead to frustration on both sides, as the stakeholder waits for the update, and the data scientist is forced to repeat work instead of working on new analyses.

<div style="overflow-x:auto;">
  <table>
    <tr>
      <th>Obstacles
      </th>
      <th>Solutions
      </th>
    </tr>
    <tr>
      <td>Lack of reuse
      </td>
      <td>Build your analyses with code, not clicks
      </td>
    </tr>
    <tr>
      <td>Lack of reproducibility
      </td>
      <td>Manage data science environments for repeatability
      </td>
    </tr>
    <tr>
      <td>Stale insights and repetitive work
      </td>
      <td>Deploy tools to keep insights up to date
      </td>
    </tr>
    <tr>
      <td>Unsustainable data science platforms
      </td>
      <td>Embrace platforms that support open source software
      </td>
    </tr>
  </table>
<div style="font-size:85%;padding-bottom: 20px;">
<i>Figure 1: Common obstacles to delivering durable value with your data science and approaches to mitigate them.</i>

</div>


## A Durable Approach to Data Science

To make the benefits of your data science insights durable over the long term, we recommend applying _Serious Data Science_ principles as outlined in Figure 1. We suggest that your data science teams:

*   **Build your analyses with code, not clicks.** Data science teams should use a code-oriented approach because code can be developed, applied, and adapted to solve similar problems in the future. This reusable and extensible code then becomes core intellectual property for your organization which will make it easier to solve new problems in the future and increase the aggregate value of your data science work. 
*   **Manage data science environments for repeatability.** Organizations need ways to reproduce reports and dashboards as projects, tools, and dependencies change. Otherwise, your team may spend far too much time attempting to recreate old results, or worse, it may give different answers to the same questions at different points in time, thereby undermining your team’s credibility. Use packages such as <a href="https://rstudio.github.io/renv/articles/renv.html" target="_blank" rel="noopener noreferrer">renv</a> for individual projects and use products such as <a href="https://rstudio.com/products/package-manager/" target="_blank" rel="noopener noreferrer">RStudio Package Manager</a> to improve reproducibility across a larger organization.
*   **Deploy tools to keep insights up to date.** No one wants to make a decision based on old data. Publish your insights on web-based tools such as <a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a> to keep your business stakeholders up to date with on-demand access and scheduled updates. Deploying insights this way also frees the data scientist to spend their time solving new problems rather than solving the same problem again and again.  

Sharla Gelfand recently spoke at rstudio::conf 2020 about the benefits of reproducible reports for the College of Nurses of Ontario:

<div style="padding: 20px 0 35px 0;">
  <script src="https://fast.wistia.com/embed/medias/cj68m8on14.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_cj68m8on14 videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/cj68m8on14/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>
</div>

## Building on a Sustainable Foundation

To this point, our serious data science approach has largely been independent of the underlying data science platform. However, your choice of data science platform can itself pose a risk to the durability of the work you do. Your data platform can become unsustainable over time due to: 

*   **High license costs:** Expensive software and variable budgets often force teams to restrict platform access to a select few data scientists. Worse, those teams may have to hold off on tackling new data science projects or deploying to more stakeholders until Finance approves money for more seats. 
*   **Dwindling communities:** If the platform or language decreases in its popularity with developers, it may become difficult to find new data scientists who are familiar with it. 
*   **Vendor acquisitions or shifts in business models:** If the platform maker is acquired by a larger company or shifts their business model, it may abandon or scale back investment in their previous product. Alternatively, sometimes vendors move from an innovation to a value extraction model, where locked-in customers are forced to pay higher license fees over time. 

Regardless of the underlying reason, an unsustainable platform can drive up costs and potentially even force an organization to start from scratch with a new platform. To reduce these threats, we recommend embracing platforms that support open source software. Doing so improves the sustainability of your data science because these platforms are: 

*   **Cost effective:** Open source software can deliver tremendous value at minimal cost, which mitigates the risk of losing your data science platform due to future budget cuts. It also makes it much easier to expand to more users as your data science team grows.
*   **Widely supported:** The R and Python open source communities are large and growing, so you can be confident these tools, and the expertise to use them will be available for many years to come. These communities are further bolstered by <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">RStudio’s mission</a>, which is dedicated to sustainable investment in free and open-source software for data science. 
*   **Vendor independent:** RStudio’s founder JJ Allaire wrote the following in a <a href=" https://blog.rstudio.com/2020/01/29/rstudio-pbc/" target="_blank" rel="noopener noreferrer">recent blog post</a>:

<div style="background-color: #f8f8f8;padding:50px 30px 30px 30px;margin:50px 0;">
  <div style="text-align:center;padding-bottom:10px;">
    <img src="logo-lockup.svg" width="400px">
  </div>
  <div class="quote-spacing">
    <p class="quote-size"><i>"Users should be wary of the underlying motivations and goals of software companies, especially ones that provide the essential tools required to carry out their work."</i></p>
    <p style="text-align: right;">JJ Allaire, CEO, RStudio<br><a href="https://rstudio.com/pbc-keynote" target="_blank">rstudio.com/pbc-keynote</a></p>
  </div>
</div>

With this caution in mind, consider building your data science investments on a platform with an open source core. Should they change their business or licensing model, everything you need to do your core data science work will still be freely available, and you can freely choose whether you want to pay the vendor’s price.

## Learn more about Serious Data Science

For more information, check our previous posts <a href="https://blog.rstudio.com/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">introducing the concepts of Serious Data Science</a>, <a href="https://blog.rstudio.com/2020/06/02/is-your-data-science-credible-enough/" target="_blank" rel="noopener noreferrer">drilling into the importance of credibility</a>, and exploring <a href="https://blog.rstudio.com/2020/06/09/is-your-data-science-team-agile/" target="_blank" rel="noopener noreferrer">how to apply agile principles</a> to your data science work. 

If you’d like to learn more, we also recommend:

*   In this upcoming webinar, <a href="https://pages.rstudio.net/BeyondDashboardFatigueWebinar.html" target="_blank" rel="noopener noreferrer">Beyond Dashboard Fatigue</a> , we'll discuss how to repeatably deliver up-to-data analyses to your stakeholders using proactive email notifications through the blastula and gt packages, and how RStudio pro products can be used to scale out those solutions for enterprise applications
*   In this <a href="https://rstudio.com/about/customer-stories/astra_zeneca/" target="_blank" rel="noopener noreferrer"> customer spotlight</a>, Paul Metcalf, Head, Machine Learning and AI, Oncology R&D at AstraZeneca, describes how his team “created a robust toolchain for routine tasks and enabled reproducible research” with R, RStudio, and Shiny. 
*   To learn more about how RStudio Connect makes it simple to deliver repeatable, up-to-date data products to your stakeholders, check out the <a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect product page</a>. 
*   RStudio’s Sean Lopp explores the importance of Reproducible Environments in this <a href="https://rviews.rstudio.com/2019/04/22/reproducible-environments/" target="_blank" rel="noopener noreferrer">RViews Blog post</a>.
*   Garrett Grolemund <a href="https://rstudio.com/resources/webinars/reproducibility-in-production/" target="_blank" rel="noopener noreferrer">presented a webinar</a> on the role that computational documents like RMarkdown play in supporting reproducibility in production.
*   <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">What Makes RStudio Different</a> explains that RStudio’s mission is to sustainably create free and open-source software for data science and allow anyone with access to a computer to participate freely in a data-centric global economy.

