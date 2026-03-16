---
title: Open Source Data Science in Investment Management
people:
  - Art Steinmetz
date: '2020-10-13'
slug: open-source-data-science-in-investment-management
categories:
  - Data Science Leadership
tags:
  - open source
  - data science
resources:
- name: "deluge"
  src: "deluge.jpg"
  title: "Stop sign under water"
blogcategories:
- Data Science Leadership
events: blog
ported_from: rstudio
port_status: in-progress
---


<sup>Photo by <a href="https://unsplash.com/@kellysikkema?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Kelly Sikkema</a> on <a href="https://unsplash.com/s/photos/flood?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">Unsplash</a></sup>

## Surviving the Data Deluge

Many of the strategies at my old investment shop were thematically oriented. Among them was the notion of the "data deluge." We sought to invest in companies that were positioned to help other companies manage the exponentially growing torrent of data arriving daily and turn that data into actionable business intelligence.

Ironically, we ourselves struggled to effectively use our own data. At the same time our employees throughout the company were taking it upon themselves to find the tools and do the work to better our processes. The tools they were using were open source, and it was only once we officially embraced an open source workflow that we dramatically sped up our business intelligence development.  

## Legacy System Migration Started the Flood

You might be surprised to see how old-school much of the investment management world is. Venerable firms like mine have legacy systems with customer records going back decades. These platforms run on COBOL, and our gray-bearded IT folks did a magnificent job of keeping them running. That was a good thing, because it took three years running in parallel before we could flip our CRM entirely to SalesForce.

A benefit of this migration was opening up an incredible volume of data, but that data posed a deeper question: What should we do with it? SalesForce has a plethora of analytic reports, but we needed serious data science for deeper insights. While SalesForce will happily create custom analysis for a fee, this is a brittle, slow process and, once it is done, the learning about HOW to do the work would have belonged to SalesForce, not us.

Fortunately open source tools allowed us to jump to a higher plane of insight very quickly, iterate continuously, and build our institutional knowledge about how to do this kind of work. Critically, an open source workflow allowed us to keep all the code for our projects in-house and usable for subsequent analysis, even if the original authors have moved on.

## Data Science Helped Tame The Fund Redemption Flow

<style type="text/css"> 
.quote-spacing { padding:0 80px; } 
.quote-size { font-size: 160%; line-height: 34px; } 
[@media] only screen and (max-width: 600px) {
.quote-spacing { padding:0; } 
.quote-size { font-size: 120%; line-height: 28px; }
}
</style>
<div style="background-color: #4476bb; color: #ffffff; padding:20px 30px 30px 30px; margin:50px 0;">
   <div class=".quote-spacing">
      <p class=".quote-size">
         <i>“Ultimately the project allowed us to retain several hundred million dollars of assets we would have otherwise lost, dropping millions of dollars to the bottom line.”
         </i>
      </p>
   </div>
</div>

As an investment management firm, we earn less than one percent a year on client assets, yet sales people are typically paid a commission of several percent up front. That means we have to hold onto the customer's investment for several years before we recoup the upfront commission. Meanwhile, the client can redeem their assets at any time. A dirty little secret of our industry is that annual redemptions run about 25% of the total asset base. It always bothered me that redemptions were treated as an exogenous factor, so when I became CEO I decided to pay some attention to it. The possibility of reducing redemption rates gave us a strong incentive to deliver a great customer experience. It is always cheaper to keep a customer than to find a new one.

Mutual fund redemption rates are an ideal subject for data science research. Financial firms have hundreds of sales people who talk to thousands of financial advisers who talk to hundreds of thousands of clients on a routine basis. We have literally millions of customer accounts. So why do people redeem? Bad fund performance is one reason. Changing goals or life circumstances are another. How can we help the customers make a better informed decision about whether getting out is the right choice? At the simplest level, we expect more communication with the customer would be better, but should that communication be a visit, a call or an email? What should we say? A visit or a call to every adviser is expensive so how should we identify the most at-risk accounts. Ultimately our intervention program must be cheaper than what it costs to attract new accounts.

As we thought about these questions we learned that our corporate parent had recently put together a data science team. As a new group, it had excess capacity which we were able to use, and the team members were enthusiastic about a project that would drop results directly to the bottom line.

First, the sales group sat down with the data scientists to discuss their assumptions about why people redeem. Then the science team went to work on the mountains of data we had and tested those assumptions. As expected, we found that fund performance was a big driver of redemptions, but also that market performance, which affects all funds, was a bigger one.

When we examined communication, we found that an increase in inbound calls was predictive of redemptions, even when those calls only concerned routine matters. We discovered that in-person visits helped reduce redemptions, but that email outreach was worthless. There were also some surprises. We found that advisers we call "churners" were more likely to redeem if we contacted them. Finally, since we had so many customers, we designed A/B tests to find the most effective treatments.

Most of the work the data scientists did used the R language. They did a great job satisfying management's constant barrage of questions because iterative analysis is so easy with tools like R, and the powerful visualization tools made communication of results easy for sales people to grasp. As the CEO, I was gratified at how clear the presentations were and at how quickly presenters answered my difficult questions, in some cases on the fly during the presentations. As an R user myself, I know its code-based workflow lends itself to rapid iteration while, at the same time, documenting the process used. It was easy to unroll the tape to see every step that led to any conclusion.

While this project was not a panacea for all redemptions, we did manage to bend the redemption curve downward a couple percentage points while making our customers happier. Our sales people knew better how to spend their time speaking to the right people with the right message. Ultimately the project allowed us to retain several hundred million dollars of assets we would have otherwise lost, dropping millions of dollars to the bottom line.

## Our Quantitative Strategy: Focus on Long-Term Insights

</style>
<div style="background-color: #4476bb; color: #ffffff; padding:20px 30px 30px 30px; margin:50px 0;">
   <div class=".quote-spacing">
      <p class=".quote-size">
         <i>“The data scientists used Python for this project but, as with the sales project, the rapid prototyping, easy iterating and powerful tools for clear visualization enabled by open source tools created a jazz band of creativity between the investment analysts and the data scientists.”
         </i>
      </p>
   </div>
</div>

The sales side was pretty eager to embrace anything that might give them an edge with the customer. However, the senior leaders of the investment teams, who are generally analytical and quantitative, were quite wary of "the robots taking over." Seeing how many purely quantitative funds there are out there, I understand their concern.

Our challenge was to convince the investment teams to see our fuller quantitative effort as a force multiplier. One day I was making the pitch for a more "quant-y" approach to a portfolio manager, and my argument was "You've been using a shovel to dig ditches for 20 years. While those may have been nice ditches, I'm now giving you a backhoe. Do you really want to reject it?" Fortunately, even as I was trying to convince this manager, the analysts in the trenches were already taking matters into their own hands thanks to the availability of open source tools.

The challenge for us was to recognize what data science could do to enhance our process rather than remake ourselves into a whole new company. Oppenheimerfunds (now Invesco) is fundamentally a long-term investment manager, not a high-frequency trader. Our quantitative insights need to persist over a duration that is actionable on our human-centered decision time line and be large enough to matter when we hold investments over months and years, not seconds and minutes.

One avenue that we explored was text mining of corporate regulatory findings and earnings call transcripts. The question was "do changes in company reports over time signal future stock returns?" Modern open-source data science tools allow near instant processing of the vast collections of documents, and these transcripts fit into a somewhat standard template, making it easy to compare changes over time.

Our security analysts started noodling around with this problem on their own using open source tools, but they recognized their expertise was limited. We didn't have the data scientists in-house who could do this work, so we partnered with Draper Labs in Boston who had a large team and were looking to branch out from their traditional work with defense contractors. One fun aspect of this project was the mutual learning that occurred. Our portfolio managers began to understand the force multiplier feature of these techniques, our analysts upped their data science game, and the data scientists learned the practical challenges of real-world trading beyond the results in the academic literature.

We sold our company before this project came to full fruition, but we were excited by the early results. While we were not the only firm working on text mining, there still seemed to be plenty of gold in the ground. The data scientists used Python for this project but, as with the sales project, the rapid prototyping, easy iterating and powerful tools for clear visualization enabled by open source tools created a jazz band of creativity between the investment analysts and the data scientists.

This project also illustrated the importance of support from the top. The security analysts were the driving force behind this project but their bosses were ambivalent at first. Air cover from the office of the CEO made clear this project was a priority for the firm. It would not have been done otherwise.

## In Conclusion: Let Water Find Its Own Level

Many techniques used by modern data scientists were developed decades ago. Now, two factors have converged to make serious data science possible for every firm:

1.  The exponential decline in computing costs, with cloud computing being the most recent evolutionary step, and

2.  Open source data science tools such as R and Python.

Open source tools put incredible power in the hands of everyone in the organization. Not everyone should or will use these tools but, as we found at OppenheimerFunds, once people see what is possible on their own, the push to advance business intelligence gathers its own momentum, and internal support to devote serious resources to the effort will grow. Managers within investment firms will inevitably want to support these efforts within their own teams because the competitive pressures are too strong, and the insights gained too great. Those that ignore the trend risk being swept away.

<hr />

### About Art Steinmetz

Art Steinmetz is the former Chairman, CEO and President of OppenheimerFunds. After joining the firm in 1986, Art was an analyst, portfolio manager and Chief Investment Officer. Art was named President in 2013, CEO in 2014, and, in 2015, Chairman of the firm with $250 billion under management. He stepped down when the firm was folded into Invesco.

Currently, Art is a private investor located in New York City. He is an avid amateur data scientist and is active in the R statistical programming language community.

  
