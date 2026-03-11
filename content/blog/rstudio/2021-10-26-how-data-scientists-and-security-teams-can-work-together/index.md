---
title: How Data Scientists and Security Teams Can Effectively Work Together
people:
  - Alex Gold
  - Tatsuya Shigeta 
  - Isabella Velásquez
date: '2021-10-26'
slug: how-data-scientists-and-security-teams-can-work-together
categories:
  - Data Science Leadership
tags:
  - Security
description: At a recent RStudio Enterprise Meetup, Gordon Shotwell from Socure shared advice on resolving common tensions between data science and security teams. Through continuous conversation, closed systems for data, and streamlined tools, organizations can set up the relationships and systems needed to be successful.
alttext: Child's room with four small carriages and a wooden dollhouse 
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---


<sup>
Photo by <a href="https://unsplash.com/@liliane?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Liliane Limpens</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</sup>


Data scientists are hungry for every bit of data they can use in their work. Security teams, on the other hand, are primarily concerned with making sure that data stays put and no one ever gets access without authorization. There's a natural tension, which can result in friction and miscommunication.

<a href="https://www.linkedin.com/in/ACoAAAEYB6gB3vIwnR8fiq-cA4aCOrs99Me2jWc" target = "_blank" rel = "noopener noreferrer">Gordon Shotwell</a>, lead data scientist at <a href="https://www.socure.com/" target = "_blank" rel = "noopener noreferrer">Socure</a>, has dealt with this tension  firsthand. The team at Socure builds best-in-class fraud models for top banks and credit card companies, so they’re constantly working with sensitive data. During a <a href="https://www.youtube.com/watch?v=UnLpB4IDpZU" target = "_blank" rel = "noopener noreferrer">RStudio Enterprise Meetup</a>, he explained how his quickly-growing team cooperates with Socure’s security team to move fast without harming organizational security.

## Become friends to achieve collective goals

##### <i>Step into the mindset of security</i>

Data scientists should show their intention of being allies to the security folks in their organizations, starting by putting themselves in the security team's shoes. Imagine the scenario: you worry all day about events that, though unlikely, could be catastrophic to your organization. You constantly anger your colleagues by saying ‘no’ to cool, new tools because of the risk to security. You are rarely recognized when your work goes well, but everyone will know if something goes wrong.

By empathizing with security teams, data scientists can better understand where they are coming from, acknowledge the potential risks, and understand why they are important.

##### <i>Advocate for security projects</i>

Even important security projects can get buried because of more urgent tasks. Data scientists should advocate for security improvements to their work. By raising these projects to other teams, data scientists can reinforce that they’re on the same side as their security-focused colleagues.

##### <i>Prove that you can make security improvements</i>

Data scientists shouldn't be all talk when it comes to security projects. They should prove that they can actually improve their security practices. This means knowing the context of what the different teams want to do, finding solutions that work for both of them, _and following through on what was decided_. The relationship between the teams strengthens when security knows that data scientists can fulfill their promises.

## Mutually understand value and threats

Security professionals usually don’t have an intuitive sense of the value that data science brings to the organization. By articulating the business value to the security organization, data scientists can get security teams on their side.

Does creating that public-facing app provide a critical new capability for customers? Does accessing that internal database allow for automation that will save staff time and money? Does having write access to the database allow for machine learning models that will impact the company’s bottom line?

At the same time, security teams should describe the <i>“threat model”</i> — that improbable but devastating event that they are trying to prevent. Are they concerned about data scientists accidentally putting proprietary data in a public app? Or are they worried that outside hackers could find a way in to steal customer payment information? Do they stay up at night worrying that a disgruntled employee could exfiltrate intellectual property? Or are there regulatory regimes in place that specify how they’re allowed to provide access to data that identify customers? Very different prevention and mitigation strategies are warranted depending on the threat.

Data scientists who understand the threat model can help ensure the gravest threats are less likely, and they can also point out where security choices don’t make sense given the threat model.

A common example is a database that contains a combination of sensitive and non-sensitive data. A data scientist might want to use sales order data to build a model of the customers that are the highest value for marketing purposes. But if that data is in the same database as customer names, addresses, and credit card information, security is going to be (and should be!) really restrictive on where that data goes. 

Both the data science and security teams can appreciate the potential value of identifying valuable customers and the threat of exposing customer data. It might become obvious that splitting the database so the sales order data isn’t merged with the sensitive customer data would serve everyone. 

## Make it easy to follow the rules

For fast-growing organizations, there’s no way security education can keep up with team growth — the resources and time needed to continuously train every new data scientist will become unsustainable. And once a company is big, security cannot audit everything that everybody is doing.

Data scientists are hired because they're smart problem-solvers. So if they are locked in a room without something they need, they will waste time trying to get to it — and they're unlikely to discover the safest or best path. A better plan would be to figure out how to create an environment for data scientists  that's super secure but doesn't leave them needing more.

Let’s take the example of a database that requires access authentication. Instead of having everyone develop their own connection to the database, security can write R and Python packages that include wrapper functions for access. Everybody is getting the data in a secure way and when there is a reason to update — say, to a more secure connection method — users don’t have to change their code and can just upgrade to the new version of the package. The system may change over time but the users can continue working with minimal interruption.

##### <i>Set up child-proof [data science environments] to work efficiently and securely</i>

_> A place that has all of their stuff and is really nice, and they can’t burn your house down._

Organizations can embed security directly into systems by setting up “child-proof rooms”. These closed systems for data ensure that users adhere to the organization’s security boundaries. Less training is needed for new users since the environment has made it impossible to do the wrong thing, allowing them to quickly and safely get started on their work.

In general, closed systems are more secure than open ones. But if those systems aren’t provisioned with the things data scientists need, they’re unlikely to get used. Instead, it’s important to pair restrictions with power. If it’s necessary to lock data scientists into a specific environment, let it be a playroom where they can do what they need while everyone else rests easy.

A server that can’t connect to the internet or edit corporate data would be restrictive on its own. Security teams can provide read access, a closed analytics database, and offline access to data science tools (such as R and Python packages through <a href="https://www.rstudio.com/products/package-manager/" target = "_blank" rel = "noopener noreferrer">RStudio Package Manager</a>), empowering data scientists to run their models inside a safe environment.

##### <i>Buy tools (don't build them) for continuous, high-quality security</i>

Organizations sometimes create their own security systems or tools. However, most don’t make money on security, so it can be under-resourced and is often first on the chopping block when times are tough. On the other hand, security is a _feature_ for software vendors. They have a vested interest in creating and maintaining secure features and systems. Vendors also aim to make their tools user-friendly and pretty (making following the rules easy!). 

By buying tools, organizations can turn their own cost center into someone else’s revenue stream. Security gets prioritized appropriately and the company can instead focus on the growth of their people and capabilities.

## Arrive at the good place

Tension between data science and security teams is common and even expected, but that doesn’t mean they can’t work together so that data scientists can get their jobs done without opening security vulnerabilities. Through continuous conversation, closed systems for data, and streamlined tools, organizations can set up the relationships and systems needed in order to be successful.

Watch Gordon’s full talk below. **Interested in working at the good place? <a href="https://www.socure.com/about/careers" target = "_blank" rel = "noopener noreferrer">Socure</a> is hiring!**

<script src="https://fast.wistia.com/embed/medias/kvxdrd04wr.jsonp" async></script><script src="https://fast.wistia.com/assets/external/E-v1.js" async></script><div class="wistia_responsive_padding" style="padding:56.25% 0 0 0;position:relative;"><div class="wistia_responsive_wrapper" style="height:100%;left:0;position:absolute;top:0;width:100%;"><div class="wistia_embed wistia_async_kvxdrd04wr videoFoam=true" style="height:100%;position:relative;width:100%"><div class="wistia_swatch" style="height:100%;left:0;opacity:0;overflow:hidden;position:absolute;top:0;transition:opacity 200ms;width:100%;"><img src="https://fast.wistia.com/embed/medias/kvxdrd04wr/swatch" style="filter:blur(5px);height:100%;object-fit:contain;width:100%;" alt="" aria-hidden="true" onload="this.parentNode.style.opacity=1;" /></div></div></div></div>

