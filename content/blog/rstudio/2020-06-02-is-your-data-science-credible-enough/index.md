---
title: Is Your Data Science Credible Enough?
people:
  - Lou Bajuk
  - Carl Howe
date: '2020-06-02'
slug: is-your-data-science-credible-enough
categories:
- Data Science Leadership
tags:
- data science
description: For Data Science to be applied, decision makers must trust and accept
  the insights. Your team needs the tools to find relevant insights, and to communicate
  these insights in a way that builds trust and understanding.
resources:
- name: black-box
  src: black-box.jpg
  title: Black Box
blogcategories:
- Data Science Leadership
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: in-progress
---

<style type="text/css">
  table {
    border-top: 1px solid rgba(117,170,219,.6);
    border-bottom: 1px solid rgba(117,170,219,.6);
    margin: 45px 0 45px 0;
    padding: 40px 0 20px 0;
  }
  tr:nth-child(even) {
    background: #ffffff;
}
tr {
  vertical-align: top;
}
  th {
    font-size: 24px;
    font-weight: 400;
  } 
  td li {
    font-size: 15px;
  }
</style>

## Does Your Data Science Lack Credibility?

In <a href="https://blog.rstudio.com/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">a recent post</a>, we defined three key attributes of a concept we call Serious Data Science: Credibility, Agility and Durability. In this post, we’ll drill into the challenge of delivering credible insights to your stakeholders, and how to address that challenge.

Ultimately, organizations use data science to discover valuable insights and then apply those insights intelligently. Such applications might include making a better decision, improving  a process, or otherwise changing how things are usually done. However, to make this happen, the organization must do at least two things: 

*   Communicate these insights to the right decision-maker, stakeholder, or system (we’ll talk more about that in our next Serious Data Science post on being Agile).  
*   Convince decision makers to trust the insight and accept its implications. If decision makers lack this trust, then they will likely ignore the recommendation, and fall back on “the way we’ve always done things.”

Typically, a host of unasked questions underlie a decision-maker’s seeming resistance to data-driven insights. They might not act on the conclusions of a data science team because they:

*   **Don’t know the skills of the data scientist:** Does the person who created this insight know what they are doing? Do they understand business risks as well as they understand their models?
*   **Don’t trust data science tools:** Did the data scientist depend too much on software in creating this result? Did the data science team just use black box tools that auto-magically produced an answer without an understanding of the business?
*   **Don’t have confidence in the development process:** Did the data scientist consider all reasonable approaches to the problem? Was there any way for someone else to review what was done, and know how things changed over time?
*   **Don’t understand what the results mean:** What is this insight actually telling me? How does it apply to what I do? What factors does it reflect? Is it really better than what we have done before? Could I get fired for acting on this result?

All these questions and doubts contribute to stakeholder hesitation, especially when they feel that they, not the data scientist, will ultimately be held responsible for the result. Fortunately, there are ways to overcome these obstacles. 

## How Can You Deliver Credible Insights?

To deliver insights that your decision makers and other stakeholders trust and actually use, we recommend adopting a Serious Data Science approach. To do this, your team must have the training and tools to find insights that are relevant and valuable. And, your team must communicate these insights to other stakeholders in your organization in a way that builds trust and understanding. 

Here are the key elements which will help your team meet these challenges:

*   **Widely-used open source software:** The best way to make sure your team has the training to use a data science tool properly is to **use the tools they already know**. Millions of data scientists around the world learn data science using open source languages, such as R and Python. While some may argue which language is best (see <a href="https://blog.rstudio.com/2019/12/17/r-vs-python-what-s-the-best-for-language-for-data-science/" target="_blank" rel="noopener noreferrer">this blog post</a> for our take on that question), both have tremendous strengths and are trusted platforms. 
*   **Comprehensive data science capabilities:** To be confident your team will find the best approach to any particular question, they need a wide range of analytic approaches readily available to apply and compare. Powered and validated by huge, ever-expanding communities and package libraries, the R and Python ecosystems ensure your team will always have the broadest range of  tools for their analyses
*   **Process transparency via code:**  Code allows others to  inspect how a problem was first solved, and how that solution matured over time. Unlike point-and-click solutions where the history of how the analysis evolved is hidden beneath a pretty (inter)face or a spreadsheet where the logic is strewn across countless different cells, code explicitly describes what steps lead to the results. Further, code can be peer-reviewed and audited by third parties for further assurance of correct behavior.
*   **Understanding through visualizations:** Just as a picture is worth a thousand words, a great visualization can explain a thousand lines of code. Visualizations help stakeholders understand complex data science insights and build confidence in the results. Interactive tools  such as <a href="https://shiny.rstudio.com/" target="_blank" rel="noopener noreferrer">Shiny</a> allow data scientists to create visualizations that can improve the understanding of a data scientist’s work while spurring engagement from stakeholders.

Heather Nolis, Machine Learning Engineer at T-Mobile, and Jacqueline Nolis, Principal Data Scientist at Nolis, LLC, recently spoke at rstudio::conf 2020 about how they used Shiny to share their machine learning models drove engagement and built trust with their business stakeholders.
    
<div align="center" style="padding: 35px 0 35px 0;">
<script src="https://fast.wistia.com/embed/medias/58qjn34mxy.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_58qjn34mxy videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/58qjn34mxy/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>
</div>

## Serious Data Science: Credible, Agile, and Durable

These elements of Serious Data Science—trusted tools, comprehensive capabilities, flexibility, and transparency—will all help your team deliver insights that are more likely to be accepted by decision makers and actually have an impact. Next week, we will focus on Agility, and how your team can not only develop apps quickly but also regularly share those results with stakeholders to create a consensus, so you can make sure you are <a href="https://blog.rstudio.com/2020/04/22/getting-to-the-right-question/" target="_blank" rel="noopener noreferrer">Getting to the Right Question</a>. 

**Serious Data Science is:**

<div style="overflow-x:auto;">
  <table>
    <tr>
      <th> Credible</th>
      <th> Agile </th>
      <th> Durable </th>
    </tr>
    <tr>
      <td>
        <ul>
          <li>Uses widely deployed and trusted tools</li>
          <li>Includes comprehensive data science capabilities</li>
          <li>Offers flexibility through the use of code</li>
          <li>Provides transparency through visualizations and code</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Employs existing knowledge and analytic investments</li>
          <li>Allows rapid development and iteration</li>
          <li>Scales well for enterprise and production use</li>
          <li>Empowers your business stakeholders</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Provides reusable, reproducible code and results</li>
          <li>Delivers relevant, up-to-date insights</li>
          <li>Supports and is supported by a vital open source community</li>
          <li>Avoids vendor lock-in</li>
        </ul>
      </td>
     </tr>
  </table>
</div>

#### Figure 1: Being credible is one of the crucial elements of a Serious Data Science platform.

## Learn More about Serious Data Science

If you’d like to learn more about Serious Data Science, we recommend the following in addition to our previous posts in this series:

*   In <a href="https://rstudio.com/about/customer-stories/redfin/" target="_blank" rel="noopener noreferrer">a recent customer spotlight</a>, Jared Goulart, Director - Operations Analytics at Redfin, described how a serious data science approach helped his team engage with stakeholders, allowing them to quickly evaluate different scenarios and plan their budgets for the next year. 
*   <a href="https://rstudio.com/solutions/r-and-python/" target="_blank" rel="noopener noreferrer">R & Python: A Love Story</a> shows how RStudio helps make the full breadth and power of R and Python available to data science teams and helps them make an impact on their organizations. 
*   The <a href="https://shiny.rstudio.com/gallery/" target="_blank" rel="noopener noreferrer">Shiny Gallery</a> highlights some of the amazing interactive visualizations that Shiny developers have created with R to convey insights and help their stakeholders make better, more informed decisions.  

