---
title: Building Effective Data Science Teams
people:
  - Rachael Dempsey
date: '2021-06-03'
slug: building-effective-data-science-teams
categories:
  - Data Science Leadership
tags:
  - business communication
description: Last month’s webinar featured data science leaders from Caliber Home Loans, The Looma Project, Saturn Cloud, T-Mobile, and Warner Music Group to start to answer the question, "What does it take to build a successful data science team?"
blogcategories:
  - Data Science Leadership
events: blog
alttext: A painting titled "Data and Goliath" showing R on a cliff and a huge database in the distance.
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---

<sup> "Data and Goliath"-gouache painting by Jacqueline Nolis (image from her <a href="https://www.etsy.com/shop/NolisMusings" target="_blank">Etsy store</a>)</sup>

**So what does it take to build a successful data science team?** Whether you are the first “data person” at your organization or leading a team of hundreds, we know success is not based on just technology; it requires people to create a productive, effective, and collaborative data science team.

Last month’s webinar featured data science leaders from Caliber Home Loans, The Looma Project, Saturn Cloud, T-Mobile, and Warner Music Group to start to answer this question. 

Our panelists for this webinar were:  

* **Kobi Abayomi**, Senior VP of Data Science at Warner Music Group  
* **Gregory Berg**, VP of Data Science at Caliber Home Loans  
* **Elaine McVey**, VP of Data Science at The Looma Project  
* **Jacqueline Nolis**, Head of Data Science at Saturn Cloud  
* **Nasir Uddin**, Director of Strategy & Inspirational Analytics at T-Mobile  
* Moderated by **Julia Silge**, Software Engineer at RStudio, PBC  

![Image of Webinar Panelists](blogpanelists.jpg)

You can view the recording of the webinar at <a href="https://www.rstudio.com/resources/webinars/building-effective-data-science-teams/" target="_blank">Building Effective Data Science Teams</a>.

There were so many great follow-up questions that we’d like to keep this conversation going. We will dive deeper into specific topics through:

*  Future blog posts <a href="https://www.rstudio.com/about/subscription-management/" target ="_blank">(Subscribe here)</a>
*  Open meetup discussions with data science leaders - join this <a href="https://www.meetup.com/RStudio-Enterprise-Community-Meetup" target="_blank">meetup group</a> for an event on June 24th with John Thompson, Global Head of Advanced Analytics & AI at CSL Behring
*  <a href="https://community.rstudio.com/c/industry/44" target="_blank">RStudio Community</a>   

We’ve also added links to an RStudio Community thread for each individual question if you’d like to continue the conversation there as well. 

We will summarize the questions and answers brought up during the panel that focus on three main themes that we think contribute to effective data science teams:   

* [**Building and maintaining credibility**](#Building-and-Maintaining-Credibility)
* [**Delivering real value**](#Delivering-Real-Value)
* [**Collaboration across an organization**](#Collaboration-Across-an-Organization)

We have paraphrased and distilled portions of the responses for brevity and narrative quality.  

## Panel Questions
### <a name="Building-and-Maintaining-Credibility"></a>Building and Maintaining Credibility

**What is a symptom that you have observed, during your time in this field, of a team being low on credibility within an organization or with stakeholders?**  

**Jacqueline**: Maybe this isn't low credibility per se, but I would categorize this as an unhealthy relationship with stakeholders. Something I think I've noticed happening in unhealthy relationships is that there is no partnership. 

The business person should be able to say, “I trust if I have a business question, I can go to you, and you're going to come back with an answer.” And the data science people can trust that, “Hey, you're going to bring us the important questions and the context needed to answer them.” 

One sign that the relationship isn't working well is when those boundaries aren't held. When you have a stakeholder who says “Well, I'm not sure you should be using a logistic regression here. I just read a blog post about neural nets. Why aren't we using those?” But also if the data scientist says, “No, what we really need to be building is a churn model. We think the value's in the churn model and we don't care what you think.” I think keeping good boundaries is a really important sign of healthiness there. 

**Nasir**: In addition to what Jacqueline said, one symptom is that you feel like there is a lack of interest from the stakeholder side. You can overcome that problem by generating confidence among the stakeholders. By delivering outcomes in a more transparent way, you can empower the stakeholders and put them in the driver's seat. You can do this through a self-service tool, like a Shiny app. If you deliver results even from the beginning of the project, you can receive feedback from them and can iteratively develop and improve upon that. It's all about developing the self-service tool and delivering this in a meaningful way.

**Taking that further, how can we build credibility and maintain credibility once we have it?**

**Elaine**: I think a lot of the things that come to mind are related to communication. One thing to build on what's been said is communicating the results of data science work in a way that is appropriate to the audience. One problem that we can have is usually, people assume we're really smart and know all these amazing magical things. But then we present in a way that they struggle to understand, and that really shows some lack of connection between the perspective of the business stakeholders and the team. One avenue of communication that you can demonstrate is in the way you present. Even if this means leaving out a lot of really interesting and cool details that you understand, what is the end game of your work and how will people need to consume it? That helps build credibility. 

The other is around communicating what work is happening on the team and what work is coming up, in a way that people can understand what the value can be from that and have a productive conversation about what the priorities are. Especially starting data science in a company for the first time, there's a lot of things people imagine could be done and a whole range of things - anything related to data that can come your way. Building a process that allows people to help you and understand where the team will be able to contribute the most to prioritize those things can be really helpful.

**Kobi**: These days, in the way that data science has taken on its own life, it is often divorced from a lot of the feature engineering and covariates response that a lot of us were previously familiar with as long-time statisticians. We can lose the importance of having models that have clearly explanatory effects in them. Business people aren't often interested in convergence rates and things like that. They're interested in, “if I do this, this thing happens.” 

We try to be transparent with the models that we create so that they have an immediate utility to the things that people in business understand. That's not just a conversation. That's a first principles thing. Let's start off making things that are, on the face, transparent with features that match KPIs [Key Performance Indicators] that the business finds important. That dance between doing something that's precise, balanced with the utility of the explanation. That's something that we think about all the time. 

### <a name="Delivering-Real-Value"></a>Delivering Real Value

**What are data teams like, that are able to be pretty effective, impactful, and really make a difference?**

**Greg**: I have a couple ideas. First, the ability to communicate effectively with the stakeholders. I mean Jacqueline, Elaine, Nasir, and Kobi all mentioned this - communicating with stakeholders. I don't think that point can be hammered in enough - getting that relationship, communicating effectively, and keeping them in mind when developing things instead of developing things in isolation. It may seem like common sense, but it's not always done in practice. Also, continually involve them in decisions throughout the process instead of going off into your own world, creating something and then coming back. The "here's what I did for you" approach can come off negatively, instead of "let's work on this together and solve this business problem." 

Another thing, from the organizational standpoint, is a mindset of being open to change. Just because this is how things have always been done doesn't necessarily mean they always have to be done that way. Having that ability to change and being open to change is important. 

The other characteristic - and I've seen this in several areas - is a diverse set of backgrounds for the team members. For instance, if everyone was like me and had a PhD in economics, focusing on econometrics, we'd communicate well and all be thinking of the same thing, but that doesn't help the business. That doesn't help my team. I’d want to include computer scientists, industrial engineers, etc. I want other disciplines that have a broader perspective, and that really opens up an open source of ideas. It's not just the leader coming up with the ideas. If you have this diverse skill set, they'll come up with great ideas on their own, working with the business, and it creates an environment of growth and value for the business. 

**Jacqueline**: I agree with everything that was said, and I think a real truth that I've noticed when I've led data science teams, is that the team rarely fails because, “Oh, we had one data scientist and two data engineers. We should have had two data scientists and one engineer.” What usually fails is there's not a clear focus. A team fails when they're hired because “Hey, we have a lot of data, and, hey, you're data scientists. You figure out what to do with that.” A team will fail if there's not a clear focus. 

To the point of flexibility, when the team recognizes that they aren't finding value in this project, how quickly can they pivot to something better? This is partly people who are flexible and can do that and partly a business environment where the data science team can say, “It turns out that a churn model isn't actually effective here.” And people say, “All right, that's fine. Let's move on to something else.” Instead of, “Well, why don’t you spend another year on it and then come back?”

**Greg**: To add on to that, I think it builds credibility if you can deliver negative results and explain that. Sometimes the business has an idea of what they want and they may be really excited, but it's not how it works in reality. Having the ability to say, “No, this is not how it works” lifts the credibility of the department being the impartial observer and giving results, rather than just giving people what they want to see.

**Julia**: It's interesting that you bring that up, because having to say no or explain a negative result, that the thing you wanted to do is no better than the way things were before, is something I have actually personally experienced as being quite challenging. 

**What is your perspective on team characteristics that allow resilience in the face of delivering negative results, or being able to handle that well?**

**Kobi**: I'm not going to say anything related to scientific characteristics. I think a baseline level of competence, maturity, and having experience of trying things, allows you to be honest with what you're doing and what output it generates. One of the gospels I preach at my job is the experimental design philosophy. We're not generating one answer. Answers aren't static things. Experiments have different results. I flip a coin once, I get heads. I flip another time, I get tails. Have a structure and apparatus in place that can generate an answer at the time that it's asked. Sometimes, you'll get an answer you like, sometimes you get an answer in a direction. All of that is information, and we try to treat what we offer to the business as something that's come from an experimental investigation.

**Data scientists sometimes have a reputation for valuing their autonomy or wanting to spend their time on fancy algorithms over delivering valuable results. Do you think that’s fair? How do you deal with this?**  

**Nasir**: Most data scientists would like to leverage the latest and greatest types of algorithms, like deep learning. In reality, you may be able to solve the business problem with simple regression techniques. As we’ve mentioned, it’s about building credibility and delivering transparent results. It's not about the latest and greatest technology, it's more about how you can deliver meaningful outcomes to the business and that you can explain it. Whatever you'll be delivering, you can explain it better. 

Model explainability is a huge field and there is still a lack of explanation of very complex black box types of models. Data scientists should not go to complex techniques first but try simple techniques, and see whether you can answer the business question. 

**Jacqueline**: I do think it's very fair. I think we, as a field, set this up. What's every big blog post? “Check out GPT-4! Look how much bigger and better - we make the exciting stuff, the new giant GPUs, whatever.” I think when junior data scientists come in they have a zest for trying the latest and greatest,  which is okay but you've got to have a sit down conversation and explain that the metric isn't if the model the most technically accurate. Is it easy to use? Is it robust to rerun? 

As a junior data scientist, I learned the hard way when a bunch of my work had to be thrown out. If you have senior data scientists still making this mistake later in their career, now that's a problem. That's a toxic scenario where you have someone who has a lot of influence and power not helping out the business. I would say as the manager, it's your job to assess how much can I guide them towards the right path and how much do I have to say “this behavior is actually going to cause major problems and we need to have harsh talks and cut it down?” I do think that's a very real thing that happens all the time.

**Julia**: I agree with both of you that this is real - this is a stereotype because it's real. It's something for us, as a field, to grapple with as we think about how we are going to be effective in organizations.

**Elaine**: Building on something Jacqueline said before about companies hiring data scientists just because they have data and the goal isn't clear. I think we can set ourselves up to be more successful here, partly in the hiring process, by not lying to people and saying we're doing these cool, new, sophisticated things. I try to be honest with candidates about the places where we might get to do really cool new things. There's also a lot of getting the right data, providing averages, and doing some of that data democratization. If what you really want to do is do the latest and greatest all day long, you need to go work somewhere where there's real business value in that bleeding edge. At most places, that is not what we're doing the vast majority of the time and can potentially weed out some people who just don't understand what they're getting into.

### <a name="Collaboration-Across-an-Organization"></a>Collaboration Across an Organization

**What contributes to data science teams that collaborate well with non-data stakeholders?**  

**Greg**: I think part of that is just the willingness to communicate. Sometimes, people want to work in a box or in isolation, so breaking that mindset and saying no, we need to collaborate with each other. We're all on the same team. We want to provide value for the company. We want the company to be successful. 

Shift the mindset to all being on the same team, working together for this as opposed to “let me go do something and bring it back and see if it works.” The latter comes across as something that's being done to the business rather than something they're a part of so the adoption and use would suffer. This goes into the value as well. If they're not using it, then there's obviously no value. 

Again, it's also about being open to change. Just because we've always done it this way doesn't mean we have to. So some of those same topics are relevant here as well.

**Kobi**: I’ve been at media companies not tech companies for my last couple of jobs. Collaboration is a huge piece of being able to understand the way that the business measures success. I'm listening to all the things that everybody else said on the panel. When you first asked that question, Greg said it exactly, communication. 

Also, product management. When I first started, coming from academia, I was less of a devotee to product management but I found it extremely useful to have someone whose job is to figure out how this thing looks, how people will react with it, push that back onto the data science team, all while having having that role separate from the people who are going to use it. People will get frustrated if they don't feel that they have the same language that you do. I think what I found more often than not, is people in frustration will just get quiet rather than push back so that you can refine and change it. Carving out a role on the team for somebody whose job is just to do that, the ingress and egress to the client side, is super important.

**Julia**: That's an interesting point because I think a lot of us have probably heard about self-service data and democratizing data in our organizations to make it so everyone can query the database and everyone can get their own stuff, but then have also experienced frustration as you just said. Like, "oh no, people are finding some kind of trend that I don't think is real." Maybe you have experienced frustrations with giving people mass access to data or the democratization of data. I'm wondering if part of it is the lack of applying the lessons of product management to those self-service data internally and not thinking like a product manager as you make these things available internally?

**Kobi**: Let me give you an exact example without divulging any intellectual property. Optimization. The linear programmers and operations research want to solve for the most optimal outcome. At one job, one of the things we were optimizing over was the number of views of something over a certain period of time and arranging things to make that most optimal. Turns out in some settings, like ad sales, that's not actually what you want. You're dealing with inventory that has different costs, different rates of return, and it's a nuanced thing. There's a bit of an art to it. The first go round, I'm telling a story in developing a model where we know we're hitting this at 100% and causing a bunch of frustration elsewhere in the organization because it made it more difficult for them to do other things that they needed to do. 

It's those sorts of conversations that you need to have - again going back to communication, communication, and communication. This is a relatively new field, we do something which is relatively technical, and society in general is relatively innumerate. The lift here is important in being able to converse with what's going on and the people who are making the money. It's super important because the downside or the negative outcome is the silence that can happen between a data science team and the rest of the organization. I worry about that at any company, in any data science team, and as I think about data science as a field. 

I remember when places were getting rid of their statistics departments, when you would see an econometrics department and a psychometrics department, but there wouldn’t be a stats department. I remember trying to think of different names, being at society meetings and thinking, "Should we call it analytics? Should we call it data science?" We enjoy a time of popularity in the zeitgeist right now and I think it's important for us, as we're instantiating ourselves in this business, to do it in the best way. Communication is super important and to have that language back and forth about the technical things we create and the things that are meaningful, especially at places that aren't tech companies.

**Jacqueline**: I think one thing that came up was this idea that people are silent when they should be talking. This is something I've noticed leading a data science team. I have tried to teach my team about going and telling people stuff, even if it's kind of scary. 

To another point that was made, if someone says something you don't agree with even if they're more senior than you, you have the right to push back on it. If you don't feel comfortable pushing back, that is the job of your manager or the data science leader. I think it's certainly the case that communication is key. But to the people who are not yet managers or directors, communication can be really difficult. I think a lot of our job is to figure out how to actually get people to do the communication that you know the team needs, but is not necessarily obvious. I really want to stress that mentoring on communication is so much of the job of a data science leader and I feel very passionate about that. 

**Elaine**: To emphasize that, I remember someone on my team who had done this great work and it had kind of gotten brushed aside because people didn't really understand how it fit. I told him, if you spend three times as much time continuing to communicate this until people understand as you did doing the work, it will be worth it. I don't think he was excited to hear that, but we need to shift our thinking to making sure that people understand the work that we do. It really doesn't matter how great it is, the communication is even more a legitimate part of the job. People need to think of that as a valuable way to spend their time, especially when they're coming out of school and new to a team.


## Let's keep talking

Thank you so much to our panelists for their insights and for opening up the conversation on building effective data science teams. As mentioned above, we’d love to keep this discussion going and dive deeper into specific topics through future blogs, RStudio Community, and open meetup discussions.

### Future Blogs

<a href="https://www.rstudio.com/about/subscription-management/" target ="_blank">Subscribe to future blog posts</a> on Building Effective Data Science Teams. In the next blog post on this topic, we'll share the attendee questions and answers that were asked live during the session:

*  **What tips would you provide for organizations where data science is not fully established?**
*  **How do you evaluate data science candidates for roles?**
*  **How can I convince senior leadership about where data scientists should be in different parts of the business?**
*  **I'm currently a data scientist and I am interested in moving into leadership. What do you think I should do?**

### RStudio Community

<a href="https://community.rstudio.com/c/industry/44" target="_blank">Continue the conversation</a> through RStudio Community and use the link for each individual webinar question to share your thoughts or ask follow-up questions on a specific topic.

### Open Meetup Discussion

<a href="https://www.meetup.com/RStudio-Enterprise-Community-Meetup" target="_blank">Join the RStudio Enterprise Community Meetup Group</a> for this open discussion on June 24th with John Thompson, Global Head of Advanced Analytics & AI at CSL Behring.  

We'll kick off this conversation with a few unanswered attendee questions from the <a href="https://www.rstudio.com/resources/webinars/building-effective-data-science-teams/" target="_blank">Building Effective Data Science Teams</a> webinar:  

*  **What tips do you have for training a data science team of varied skillsets?**
*  **Are engineering and DevOps tightly integrated with the data science team and in either case, how do you create a common vocabulary across these roles? How do you build partnerships with other teams, such as security?**
*  **How do you establish coding standards across your team and secondly how do you decide what tools are going to be used - whether that’s certain software, internal packages, visualization tools, etc.?**


