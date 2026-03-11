---
title: Is Your Data Science Team Agile?
people:
  - Lou Bajuk
  - Carl Howe
date: '2020-06-09'
slug: is-your-data-science-team-agile
categories:
- Data Science Leadership
tags:
- data science
description: Data science teams struggle to deliver results quickly. Agile techniques
  such as rapid iteration and continuous collaboration with stakeholders can help
  overcome these challenges.
resources:
- name: winding-path
  src: thumbnail.jpg
  title: Winding path through woods
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


<sup>Photo by <a href="https://unsplash.com/@vespir?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">James Forbes</a> on <a href="https://unsplash.com/s/photos/winding-path-through-woods?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Unsplash</a></sup>

As we recently wrote in our first post on <a href="https://deploy-preview-290--rstudio-blog.netlify.app/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">Serious Data Science</a>, there are numerous challenges to effectively implementing data science in an organization. Many industry surveys warn that **most analytics and data science projects fail**, and **most companies don’t achieve the revenue and profit growth that they hoped** their data science investments would deliver. In this post, we’ll examine some underlying causes of why this happens.

In our previous post in this series, we discussed how to tackle <a href="https://blog.rstudio.com/2020/06/02/is-your-data-science-credible-enough/" target="_blank" rel="noopener noreferrer">building credibility for your data science team</a>. Here, we will focus on the challenges of quickly delivering real value with your data science team with a platform that supports an agile approach. 


## Data Science Development is Often a Long and Winding Path to Value

In talking with many different data science teams, we’ve heard that it takes far too long for a team to ramp up, perform analyses, and then share those analyses in an impactful way with their organization. This makes it challenging for data science leaders to deliver value to the rest of their organization, which in turn makes it difficult to justify buying new tools, hiring new team members, and investing in their training. 

Several common obstacles make it difficult for a data science team to quickly ramp up and be productive:

*   **Training on new tools:** When an organization invests in a new data science platform or brings in new team members unfamiliar with that tool, teams often require extensive training before they can start reliably delivering analyses. 
*   **Monolithic applications:** Too many data science development projects try to solve all problems at once by building or buying a single grand solution. Frequently these new massive tools take months to implement, require major changes to processes and demand significant configuration and professional services before they can be used effectively. And, if the new platforms don’t integrate well with existing tools, data scientists are forced to use multiple different environments to get their work done, which impedes their productivity and often leads to those analytic investments being under-utilized. 
*   **Slow exploratory development:** Good data science requires the ability to rapidly explore many approaches to solving a problem and to revise proposed solutions with colleagues and stakeholders. However, many firms adopt point-and-click model development tools in their quests for ease of use, not realizing that those interactive systems lock data scientists into hours of manual labor to create a new version when stakeholders request changes.
*   **Difficult to share and access results:** Finally, if your stakeholders cannot find your data products, they won’t use them. Too many insights get delivered using ad hoc emails or isolated web links because existing tools make it difficult to deploy data science insights without extensive help from IT. This leads to stakeholders frequently struggling to find results, using analyses based on old data, or waiting too long to get an updated version. 

## Finding the Shortest Path to Value

Delivering data science value in an organization requires that your team be agile. While “Agile” usually refers to a very specific development methodology, here we use “agile” to simply describe a process that has four principles:

1. **Use what you have.** To quickly ramp up and deliver value, take advantage of the existing knowledge of your team and your previous investments.
2. **Collaborate regularly.** The users of the product continuously meet with and influence developers. 
3. **Iterate on deliverables rapidly.** Developers incorporate feedback into the product in short development cycles until it delivers what the users want.
4. **Deliver results frequently.** The process routinely delivers new products for users to critique and improve.

Applying these principles to the data science development process allows your team to deliver value more quickly and efficiently. They help your team overcome the obstacles noted previously, and they demonstrate commitment to a Serious Data Science approach (see Figure 1).

<div style="overflow-x:auto;">
  <table>
    <tr>
      <th>
     	Obstacles
      </th>
      <th>
      Solutions
      </th>
    </tr>
    <tr>
      <td>Training required on new tools
      </td>
      <td>Use tools many data scientists already know
      </td>
    </tr>
    <tr>
      <td>Monolithic applications take too long to set up and don’t use existing analytic investments
      </td>
      <td>Focus on small prototypes to prove value, using tools that integrate with your existing frameworks
      </td>
    </tr>
    <tr>
      <td>Slow exploratory development
      </td>
      <td>Rapid, code-based development
      </td>
    </tr>
    <tr>
      <td>Difficult to access and share results
      </td>
      <td>Deliver live results directly to stakeholders
      </td>
    </tr>
  </table>
</div>

Figure 1: Use agile principles in a Serious Data Science approach to address common development obstacles. 

To make your team more agile in your data science development process, we recommend that you:

*   **Apply your existing knowledge.** Many data scientists already know how to use R and  Python because of the huge open source communities around these languages. This means your team will not require extensive training on a new platform. Using R and Python as the foundation of your data science platform also helps you quickly recruit and retain the best Data Science talent by letting your data scientists work in the environments they already know and love. 
*   **Focus on small prototypes that prove value.** Instead of trying to build or buy a single data science platform, focus your development on small easy-to-test modules that can then be combined with code or scripts. As an example, instead of trying to reinvent the entire customer buying experience, break up that concept into independent prototypes that improve recommendations, streamline purchases, and improve pricing for profitability. And choose a platform that integrates well with the other analytic frameworks you’ve already built, so that you can exploit those investments, rather building everything from scratch. (We will be talking about this principle of Interoperability in greater detail in the future).
*   **Rapidly evolve your solution using code-based development.** We recommended using a code-based data science foundation such as R or Python that allows easy auditing and peer review in our <a href="https://blog.rstudio.com/2020/06/02/is-your-data-science-credible-enough/" target="_blank" rel="noopener noreferrer">prior blog post about credibility</a>. Code also allows you to rapidly evolve your solution to explore new approaches and accommodate stakeholder feedback. One of the features of R and Python that users love most is how easy it is to explore different analytic approaches to solving any given problem. For example, this <a href="https://rstudio.com/about/customer-stories/liberty-mutual/" target="_blank" rel="noopener noreferrer">recent customer spotlight with Liberty Mutual</a> highlights the power and flexibility of R in their data science environment.
*   **Deliver live results directly to stakeholders.** Stakeholder feedback is critical to agile development, but it won’t help if they don’t have your latest results. You can eliminate that concern if you publish data science results on a web-based platform such as <a href="https://rstudio.com/products/connect/" target="_blank" rel="noopener noreferrer">RStudio Connect</a>. You can even automate this publication process using continuous integration development techniques such as Github actions. You can also notify stakeholders with automated emails from packages like _blastula_, which we will be covering in more detail in an upcoming webinar. Speeding up this delivery and feedback mechanism ensures stakeholders get input and see the value your data science team is delivering in real-time. 

### Astellas’ Aymen Waqar discusses the analytics communications gap:

<div style="padding: 15px 40px 35px 40px;text-align: center;">
<script src="https://fast.wistia.com/embed/medias/iwmemji2xh.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><span class="wistia_embed wistia_async_iwmemji2xh popover=true popoverAnimateThumbnail=true videoFoam=true" style="display:inline-block;height:100%;position:relative;width:100%">&nbsp;</span></div></div>
</div>

## Learn more about Serious Data Science

For more information, see our previous posts <a href="https://blog.rstudio.com/2020/05/19/driving-real-lasting-value-with-serious-data-science/" target="_blank" rel="noopener noreferrer">introducing the concepts of Serious Data Science</a>, and <a href="https://blog.rstudio.com/2020/06/02/is-your-data-science-credible-enough/" target="_blank" rel="noopener noreferrer">drilling into the importance of credibility</a>. In the coming weeks, we will round out this series with a post on how to make sure the value your data science team provides is durable.   

If you’d like to learn more, we also recommend:

*   <a href="https://rstudio.com/about/customer-stories/brown-forman/" target="_blank" rel="noopener noreferrer">Paul Ditterline describes a Serious Data Science approach adopted by Brown-Forman</a>, in which building on familiar open-source languages allowed their data scientists to ramp up quickly, and “turn into application developers and data engineers without learning any new languages or computer science skills.”
*   <a href="https://rstudio.com/solutions/r-and-python/" target="_blank" rel="noopener noreferrer">R and Python: A Love Story</a> shows how RStudio enables collaboration between the R and Python users on your data science team and helps all of them easily share their data science insights with your stakeholders. 
*   Visit the <a href="https://rstudio.com/products/team/" target="_blank" rel="noopener noreferrer">RStudio Team product page</a> to learn how the RStudio Team platform for data science allows you to capitalize on your existing analytic investments and rapidly deliver value to your organization.
*   For more information on using RStudio Connect and the blastula package to send custom emails to your stakeholders with plots, tables, and results inline, see <a href="https://blog.rstudio.com/2020/01/22/rstudio-connect-1-8-0/" target="_blank" rel="noopener noreferrer">this recent blog post</a> on the Connect 1.8 release.
* See <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">What Makes RStudio Different</a> to learn about how RStudio helps support open source data science.


