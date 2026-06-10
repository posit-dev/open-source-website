---
title: "A brief and biased history of Posit data science agents"
date: 2026-06-11
people:
  - Joe Cheng
description: What we learned from Positron Assistant and Databot
image: "images/featured.png"
image-alt: "Three logos representing the three Posit agents, connected left to right by dotted lines: a robot face wearing goggles (Positron Assistant), a cylinder wearing goggles (Databot), and a four-pointed star inside two diamonds (Posit Assistant), suggesting a progression from one data science agent to the next."
topics:
  - Artificial Intelligence
software: [positron, rstudio]
languages:
  - R
  - Python
tags:
  - posit-assistant
hidesubscription: false
---

For the last 18 months, many of us at Posit have been focused on building AI agents designed to help RStudio and Positron users get their work done faster and more effectively. And we truly believe that we've succeeded! Our latest agent, [Posit Assistant](https://posit-dev.github.io/assistant/), is extremely good and getting better with each passing week.

But Posit Assistant was not our first agent, and it's not likely to be our last. The proliferation of agents coming from Posit has started causing serious confusion. This post hopes to clear that up by providing a chronology of the agents we've created, our rationale for their design and architecture, and what you need to know about them today (if anything).

## TL;DR

Posit Assistant is our newest, most powerful agent for data science. It builds on what we learned from creating our previous agents: Positron Assistant and Databot.

| Name | Description | Status |
|------|-------------|--------|
| **[Posit Assistant](https://posit-dev.github.io/assistant/)** | Coding agent available in RStudio and Positron (and more) | Active |
| **[Positron&nbsp;Assistant](https://positron.posit.co/assistant.html)** | Positron's coding agent | Superseded by Posit Assistant, still available until Q3 2026 |
| **[Databot](https://positron.posit.co/databot.html)** | EDA agent in Positron | Superseded by Posit Assistant |

<div class="callout callout-note" role="note" aria-label="Note">
<div class="callout-header">
<span class="callout-title">What about Posit AI?</span>
</div>
<div class="callout-body">

[Posit AI](https://posit.ai/), not to be confused with Posit Assistant or Positron Assistant, is a model subscription service that can be used to power Posit Assistant.

</div>
</div>

## Positron Assistant

- **Strengths:** Time to market; connects to a variety of providers; tight IDE integration
- **Weaknesses:** Legacy agent architecture; not available in RStudio IDE
- **Status:** Succeeded by Posit Assistant (as of June 2026)

This was the first "off the shelf" data science agent we ever shipped, and is available exclusively in Positron. It was forked from GitHub Copilot, and like Copilot, you can ask it general coding questions, have it write code, and have it explain existing code to you.

While the [Positron Assistant](https://positron.posit.co/assistant.html) experience is largely the same as Copilot, there are two major differences. The first is that it can access Positron-specific features like running code in an interactive R or Python session, inspecting variables, and generating/inspecting plots. These features make it much more useful for data work.

The second major difference is the ability to connect to other LLM providers than the Copilot service, right out of the box. At this time, Positron Assistant can connect to Anthropic and OpenAI (with API key), AWS Bedrock, Snowflake Cortex, GitHub Copilot, Microsoft Foundry, Google Gemini, [Posit AI](https://posit.ai/), and even custom (OpenAI-compatible) providers. When running in a properly configured Posit Workbench installation, these can often be seamlessly authenticated.

GitHub Copilot is tightly integrated with VS Code, and Positron Assistant is similarly well integrated with Positron. You can start an "inline chat" right at your editor cursor and ask Positron Assistant to fix or explain errors with one click. These were major benefits to starting with GitHub Copilot as a base.

Unfortunately, there are serious downsides to the GitHub Copilot heritage as well. The architecture and core APIs of Copilot were designed to be extended [in ways](https://code.visualstudio.com/api/extension-guides/ai/chat) that didn't end up being very popular, while tool calling felt grafted on and cache control nonexistent. The net effect was a lot of abstraction and complexity between the user prompt and what actually went into the LLM request, making it difficult for us to get the best performance out of the LLM. And users noticed this, saying that Positron Assistant was generally effective but also duller than other agents, including Databot and Claude Code, even when using the same underlying model.

Another big downside to GitHub Copilot was that its chat UI was more austere and harder to customize than what we could do on our own. Any changes we made were asking for technical debt, multiplied by the incredibly fast pace of upstream changes that we need to regularly merge.

Overall, the Positron Assistant project gave us what we needed at the time: a competitive, full-featured, IDE-integrated, agentic coding assistant. But for data work, we felt like we knew how to do better in a number of ways, including agent performance and UI/UX.

## Databot

- **Strengths:** Effective agent harness; well tailored to exploration tasks
- **Weaknesses:** Not general purpose enough; not available in RStudio IDE
- **Status:** Succeeded by Posit Assistant (as of June 2026)

Databot was conceived in December 2024, in response to a specific question: what would happen if we took a frontier model (Claude 3.5 Sonnet), seeded it with simple instructions, and gave it unfettered access to the most powerful tool we could think of (a live R or Python session)?

At the time, it seemed hopelessly reckless to give so much power to an LLM, and we ran the first prototype with real trepidation! Fortunately, this approach is more effective and significantly less dangerous in practice than in theory. In a world before Claude Code, Databot felt like absolute magic. That magic was compounded by three decisions we made in an effort to make Databot excellent for exploratory data analysis (EDA):

1. The ability not only to execute code but to see the results (including tables and plots)
2. Keeping the human in the feedback loop by only allowing so many tool calls before stopping to summarize progress and check in with the user
3. Always providing three to five suggestions of what to do next

With a suitably capable LLM, this combination makes data exploration feel like flying.

It took us months to convince ourselves that a tool like this was safe enough to ship to users, and months more to turn the prototype into production-ready software. Since this felt like such an aggressive architecture, we constrained Databot to a narrow remit: it was only for interactively exploring data. After exploration was complete, it could also export a reproducible Quarto report that records both the findings and the methods, but that was pretty much it.

We officially launched Databot on August 28, 2025 with [this blog post](https://posit.co/blog/introducing-databot). We were still so nervous about the dangers that we published a [companion blog post](https://posit.co/blog/databot-is-not-a-flotation-device) at the same time, telling users how *not* to use Databot. As models have gotten better, and tens of millions of users have grown accustomed to aggressively agentic AI tools, this second blog post remains technically accurate but perhaps reads a bit alarmist. In practice, agentic AI coding tools are not completely safe, but neither are they necessarily as dangerous as they may theoretically appear. Their usefulness across a wide variety of tasks helps balance this risk.

Databot's crucial weakness turned out not to be that it was too dangerous, but too narrowly scoped. EDA does not happen in a vacuum. It's often done in service of some larger project, and insights derived from EDA typically immediately lead to the creation of a reproducible cleaning script, interactive Shiny app, automated data transformation job, etc. As an EDA-focused agent harness, Databot did not have the tools needed to do those tasks well.

This constrained nature left users feeling frustrated. Databot could be so intelligent, so facile with data exploration, yet so suddenly clumsy the moment you asked it to edit a data cleaning script, and the distinction felt arbitrary. Even if you understood Databot's limitations, it still left you needing to manually perform a "hand off" between an EDA session in Databot and a Shiny app authoring session in Positron Assistant.

### Why did we make two agents instead of one?

Given the obvious downsides of creating two distinct agents for Positron instead of focusing on one — confusion, disjointed experience, duplication of effort — why did we do it?

First, as stated above, Databot felt not just risky but borderline reckless in how much power we were encouraging the agent to wield. Positron Assistant had very similar behavior to Copilot, so while not totally "safe", it felt like a widely understood and accepted set of tradeoffs. It felt reasonable to have one conservative agent that we could tell everyone to use in Positron Assistant, and one aggressive agent for early adopters to play with in Databot.

Second, Positron Assistant seemed easier to build because we could start with so much existing functionality from Copilot. For Databot, we had to build everything from scratch: the agent harness, the chat UI, loading and saving past conversations, everything, and it was hard to know in the beginning how fast we could do it and how successful we would be. Again, it felt right to have one agent that we knew we could ship quickly, and one that might take longer but would potentially give us a better long-term platform.

These reasons made sense to us in early 2025, but they haven't stood the test of time. As Databot gestated, Claude Code showed the world that powerful AI agents had a usefulness-to-risk ratio that far, far exceeded most people's thresholds. And forking Copilot didn't give us nearly the boost in development speed we expected: while it did give Positron Assistant a huge head start, it also saddled Positron Assistant with many unnecessarily complex abstractions and introduced us to the very expensive recurring task of merging the torrent of upstream Copilot changes with our extensive modifications.

A final reason had to do not with risk but with specialization: Databot's [WEAR loop](https://posit.co/blog/introducing-databot) felt distinct from Positron Assistant's generic loop, and this felt like a pretty fundamental UX difference. Once we got serious about combining the two, it turned out not to be so fundamental after all, and for the most part we feel like our next agent succeeds at "code-switching" as needed.

## Posit Assistant

- **Strengths:** Effective agent harness; great for EDA, coding, and general-purpose agent tasks; integrated into both Positron and RStudio
- **Weaknesses:** Not designed for highly autonomous or highly parallel agentic work (if that's what you're into)
- **Status:** Now available in RStudio, in preview in Positron

Posit Assistant is our newest data science agent, designed to build on what we liked most about each of the AI agents we've built and used in the past:

- A simple agent harness with a small number of powerful and general tools
- Prompting, tools, and UI/UX designed for the needs of data scientists
- Full access to live R/Python sessions, including variables and plots
- Integrated into our data science IDEs
- A codebase designed for fast iteration
- Extension points based on MCP and skills

Crucially, we built Posit Assistant to live in both RStudio (since April 2026) and Positron (since June 2026). Not only did this finally bring an integrated agent to RStudio, where most R users still live today, but it also meant that every ounce of effort we put into improving Posit Assistant helps both RStudio and Positron users.

While Positron Assistant (the older one) grew out of Copilot, Posit Assistant (the new one) grew out of Databot. There was much we liked about Databot, and it didn't take much effort to expand its mission from the narrow task of exploratory data analysis to being a great general-purpose agent.

The big advantage of Positron Assistant in early 2025 turned out to be a big disadvantage by early 2026: being built on GitHub Copilot. While Copilot was arguably one of the two or three best coding agents for most of its existence, by the end of 2025 it was thoroughly outmatched by Claude Code.

At the risk of oversimplifying, the Copilot approach thinks the user should play a major role in deciding what context the underlying LLM gets to see. For example, Copilot and Positron Assistant have UI features that let you specify what files from your project you want to include with your next user prompt. You can also use `@-mentions` to bring in reference materials (for example, the Shiny VS Code extension lets you mention `@shiny` to bring in the Shiny docs).

In contrast, Claude Code's approach is to give an LLM access to powerful general-purpose abilities, like reading/writing/editing files and executing arbitrary bash commands, and then trusting the LLM to use them to gather the information it needs. This approach worked well when Claude Code was released in February 2025, and then dramatically improved over the course of 2025. The overall effect was that Claude Code felt significantly smarter and more engaged, even when using the same underlying language model.

**The highest compliment I can give to Posit Assistant is this: when exploring data, it feels a lot like Databot, and when coding, it feels a lot like Claude Code.** And where Claude Code is a general-purpose coding agent, Posit Assistant is built specifically for people who work with data, with modes and skills for data tasks like data cleaning, Shiny app creation, and predictive modeling.

### Why did we call it "Posit Assistant" when we already had "Positron Assistant"!?

Maybe the most controversial thing about Posit Assistant is its name: Posit Assistant. First, it's quite dull. Second, why isn't it "Posit Agent"? Third, why would you give it almost-but-not-exactly the same name as the thing it's superseding?

These are all decisions that were made by me, Joe Cheng, and if you think they are bad decisions, then just know the Posit Assistant team agrees with you. (I stand by the name, but only just!)

**On dullness:** A natively integrated AI chatbot for an IDE is table stakes, not a distinguishing feature. While we need a name today, I want users to eventually think of Posit Assistant as "RStudio's chat pane" or "Positron's built-in AI", that is, for its identity to be subsumed into the host IDE. We believe most data practitioners will continue to use IDEs even as these models get more capable, and that the "I" in IDE is where we can offer real value. Instead of trying to build a new, distinct brand, I wanted there to barely be a brand at all.

**On "Agent":** The term "agent" is heavily overloaded these days. In the sense that it's been used so far in this article, it means ["models using tools in a loop,"](https://simonwillison.net/2025/May/22/tools-in-a-loop/) and Posit Assistant definitely fits that definition. But a lot of our customers understand the word to refer to "models working highly autonomously for long periods of time", and we really wanted to avoid this connotation. Posit Assistant does have the ability to work autonomously if necessary and appropriate, but much of our harness encourages the model not to work autonomously in situations where it otherwise would.

**On Positron Assistant/Posit Assistant:** This one is truly confusing, and the hardest one to defend. My defense is that the confusion is temporary. For most of Positron Assistant's short history, Posit Assistant didn't exist. For most of Posit Assistant's history, Positron Assistant will no longer exist. We're in a moment right now where we're mid-transition, so it's very confusing, but hopefully, that confusion is temporary.

I hope you will find this explanation to be satisfactory, and if not, at least now you know who to blame!
