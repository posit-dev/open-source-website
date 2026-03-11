---
title: Driving Real, Lasting Value with Serious Data Science
people:
  - Lou Bajuk
date: '2020-05-19'
description: Driving lasting value in an organization with data science is critical
  but difficult. The truth is most projects fail. What’s the answer? Serious Data
  Science is credible, agile and durable.
slug:
- serious-data-science
tags:
- data science
categories:
- Data Science Leadership
resources:
- name: giant-windmills
  src: windmills.jpg
  title: Giant Dutch windmills
images:
- /2020/05/19/driving-real-lasting-value-with-serious-data-science/windmills.jpg
blogcategories:
- Data Science Leadership
events: blog
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

Data science is now a hot area of investment for many organizations. Countless blogs, articles, and analyst reports emphasize that effective data science is critical for competitive advantage, and many business leaders believe that data science is vital for an organization to survive, much less thrive, over the next several years.

However, many data science leaders grapple with an existential crisis for their teams. On the one hand, many vendors and analyst reports emphasize the rise of Citizen Data Scientists, empowered by tools that promise to augment and automate the hard work of data science to automagically answer vital questions, no Data Scientist required. On the other hand, machine learning and deep learning methods in the hands of software engineers, fueled by lots of  computational power, answer more and more questions (as long as the problem is well-defined, and there is sufficient data available). Squeezed in between these trends, what is the role of a data scientist? 

Even worse, nearly as many blogs and analyst reports emphasize the challenges of effectively implementing data science in an organization, and emphatically state that **most analytics and data science projects fail**, and **most companies don’t achieve the revenue and profit growth that they hoped** their data science investments would deliver.

We will dive into the role of a data scientist in more detail in the coming weeks, but here we will focus on this question: Why is getting real, lasting value from data science investments so difficult? 

## Many data science projects lack credibility and impact over time

In talking to many different organizations implementing data science projects, we have seen many challenges that prevent data science investments from delivering the value they should. These typically fall into three categories: 

- **Lack of credibility:** Data science leaders grapple with whether their team has the necessary training and the right tools to discover relevant and valuable insights in their data. Once the team has found something interesting, how can others in the organization understand and trust those insights enough to actually change their behavior, and make decisions based on them? This problem is compounded if the approach is a difficult-to-explain, black box model. 

- **Slow path to value:** Seemingly simple questions like "Which customers will be our most profitable next quarter?" often turn into month-long research projects as data scientists scour the firm for data and struggle to wrangle it into shape (a topic we discussed in a recent blog post, <a href="https://blog.rstudio.com/2020/05/05/wrangling-unruly-data/" target="_blank" rel="noopener noreferrer">Wrangling Unruly Data</a>). Then once the data scientists start to develop an analysis, they find iterating and refining their results with stakeholders slow and unwieldy (something we covered in another blog post, <a href="https://blog.rstudio.com/2020/04/22/getting-to-the-right-question/" target="_blank" rel="noopener noreferrer"> Getting to the Right Question</a>). These slow response times frustrate business sponsors and often stymie putting data insights into action. Worse, they encourage decision makers to go with their gut intuition instead of data.

- **Ephemeral benefits:** Once a valuable insight or tool has reached a decision maker, organizations struggle with maintaining and growing the value of these data science investments over time. They find it difficult to implement repeatable and reproducible processes as their systems and data science tools evolve, which often forces them to start from scratch when solving a new problem, or to reimplement old analyses when needed. Furthermore, data science practice at an organization often become dependent on a single software vendor, and that vendor may try to extract more of the value the customer receives as software license revenue.

Andrew Mangano, Data Intelligence Lead at Salesforce, spoke at rstudio::conf 2020 about the importance of delivering useful insights to your stakeholders.

<div style="padding: 35px 0 35px 0;">
<script src="https://fast.wistia.com/embed/medias/67q4k9196d.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_67q4k9196d videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/67q4k9196d/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>
</div>

## Real-world problems need serious data science

So what’s the answer? And how do you cut through all the hype and confusion?

The reality is that hard, vaguely defined but valuable to solve, problems exist in the world. Commodity approaches (whether via augmented analytics for citizen data scientists, or standard machine learning approaches for software engineers) yield commodity answers. **Real-world business problems require smart, agile data science teams** empowered with the flexibility and breadth of open source languages like R and Python. We know this because **tens of thousands of you use our software every day to do amazing things.**

To deliver real, lasting value, organizations need to set aside the hype and build on a strong foundation. We recommend adopting a strategy we call *Serious Data Science*. As shown in Figure 1, Serious Data Science is an approach to data science designed to deliver insights that are:

- **Credible:** The first step is to ensure that your team has the training and tools to find insights that are relevant and valuable, and that your team can communicate these insights to other stakeholders in your organization in a way that builds trust and understanding. 
- **Agile:** Next, the platform you use must enable data scientists to quickly develop and iterate those valuable insights, and get them to your decision makers, where they can have an impact.
- **Durable:** Finally, to deliver lasting value, the platform must also make it easy to reuse and reproduce your team’s data science work, to deliver up-to-date insights, and do so in a sustainable way for the long term. 

#### Serious Data Science is....

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

#### Figure 1: Crucial elements of a Serious Data Science platform.

## Why you should adopt Serious Data Science

We'll be writing in detail about these components of Serious Data Science in the weeks to come. But before we get to that, we must address a topic near and dear to every data science leader: the role of the data scientist within the organization. Our post next Tuesday will address how that role is changing in today's organizations, and why they will need the Serious Data Science framework to continue demonstrating their value in the months and years to come.

## Learn more about Serious Data Science

If you’d like to learn more about Serious Data Science, we recommend:

- <a href="https://rstudio.com/about/customer-stories/brown-forman/" target="_blank" rel="noopener noreferrer">**Paul Ditterline describes a Serious Data Science approach adopted by Brown-Forman**</a>, reducing dependency on tools like Excel, to solve more, and more complex, data science problems more efficiently. 
- <a href="https://blog.rstudio.com/2020/04/28/avoid-irrelevancy-and-fire-drills-in-data-science-teams/" target="_blank" rel="noopener noreferrer">**Avoiding Irrelevancy and Fire Drills in Data Science Teams**</a> is another view of the challenges facing today’s data science teams, and how to tackle those challenges.
- <a href="https://rstudio.com/about/what-makes-rstudio-different/" target="_blank" rel="noopener noreferrer">**What Makes RStudio Different**</a> highlights RStudio’s mission to create free and open-source software for data science, in order to allow anyone with access to a computer to participate freely in a data-centric global economy.
- <a href="https://rstudio.com/solutions/r-and-python/" target="_blank" rel="noopener noreferrer">**R & Python: A Love Story**</a> shows how RStudio helps make the full breadth and power of R and Python available to data science teams, and helps them make an impact on their organizations. 
- <a href="https://rstudio.com/resources/rstudioconf-2020/" target="_blank" rel="noopener noreferrer">**Recorded talks from rstudio::conf 2020**</a>  highlight the amazing, impactful, creative work that the open source data science community is doing.  

