---
title: 'AI Newsletter: How to choose a model'
slug: ai-newsletter
date: 2026-08-14T00:00:00.000Z
people:
  - Sara Altman
  - Simon Couch
description: |
  Which model is 'best'? A survey of the current model landscape.
image: images/hero.png
image-alt: >-
  On the left-hand side, three robot icons representing Posit's AI assistants.
  On the right, hex sticker logos for Posit's AI-related open source packages
  including mall, mcptools, vitals, ragnar, ellmer, chatlas, shinychat, and
  gander.
topics:
  - Artificial Intelligence
software: []
languages: []
tags:
  - ai-newsletter
source: []
nohero: false
hidesubscription: false
---


<div class="callout callout-note" role="note" aria-label="Note">
<div class="callout-header">
<span class="callout-title">Note</span>
</div>
<div class="callout-body">

**Subscribe to the AI Newsletter!**

The AI newsletter is published as an RSS feed. Follow it in your favorite reader:

<a href="/tags/ai-newsletter/index.xml" target="_blank" rel="noopener noreferrer" class="btn-shortcode inline-flex mb-5 mr-5 items-center px-4 py-3 text-sm leading-5 gap-2 rounded-lg bg-blue-400 !text-white font-semibold align-middle hover:bg-blue-500 transition no-underline">Subscribe via RSS</a>

**Want the newsletter as an email?** Paste the feed URL -- <https://opensource.posit.co/tags/ai-newsletter/index.xml> -- into a free RSS-to-email service such as [Blogtrottr](https://blogtrottr.com/), [Feedrabbit](https://feedrabbit.com/), or [Follow.it](https://follow.it/), and each new issue will arrive in your inbox.

</div>
</div>

<br>

How do you know which model to use and when? Often, it's not a question of which model is "best" but which model suits your task and needs at a given time. You might switch between models for different projects (e.g., for package development vs. data analysis), or even within a single project (e.g., for planning vs. implementation). Different tasks require a different balance of cost, token usage, speed, intelligence, and capabilities (some models, for example, don't have vision).

If you want our most durable, high-level advice: **start off with the most expensive model you have access to from one of the two frontier labs, OpenAI or Anthropic.**[^1] Then, once you have a sense for the "ceiling," try out less expensive models and see how they compare. Developing a feel for what's possible with LLMs will help you make better decisions about trade-offs. 

That said, we'll try to tackle this question more thoroughly in this post.

## The model landscape

Currently, Anthropic and OpenAI set the bar for AI capabilities. Many folks credibly consider Google Gemini a third frontier lab.

Anthropic and OpenAI each release a "family" of models: Claude and GPT, respectively. The most capable models in both families are also the slowest and most expensive. Conversely, the least capable models are the cheapest and quickest. Other labs tend to follow this same pattern, releasing a set of models with different tradeoffs on the cost vs. performance curve.

Models within a given family tend to be similar to each other in the shape of their intelligence, sharing similar capabilities (relative to model size), shortcomings, and idiosyncrasies. For example, Claude Fable 5, Claude Opus 5, and Claude Sonnet 5 often use the same turns of phrase and are quite good at writing and debugging code. Models from different families can have relatively different shapes of intelligence even if their benchmark scores and prices are very similar. For example, GPT 5.6 Terra and Claude Sonnet 5 are priced similarly and are similarly capable at agentic coding, but Terra doesn't "see" data visualizations as well as Sonnet, while Sonnet doesn't communicate as clearly as Terra.

Other labs release models that score nearly as high as models from Anthropic and OpenAI on benchmarks. However, these evaluation scores can often be deceiving. Labs can now train models that optimize for the benchmarks ("benchmaxxing"). These models score well on benchmark-shaped tasks, which tend to be highly autonomous and "tricky," but can fail to generalize to real-world tasks, which often involve more ambiguous requests. As a counterexample to this pattern, Kimi K3 and GLM 5.2 score well on the benchmarks, and we've found them to be exceptionally well-rounded and intuitive and thus [introduced them to Posit AI](https://opensource.posit.co/blog/2026-08-10_kimi-k3-glm-5-2-posit-ai/).

In [previous](https://opensource.posit.co/blog/2026-07-17_ai-newsletter/) [newsletters](https://opensource.posit.co/blog/2026-06-19_ai-newsletter/) and [blog posts](https://posit.co/blog/introducing-bluffbench), we've shared results from targeted evaluations. Here, instead, we offer an approximate and entirely vibes-based comparison of these model families' strengths.

![A comparison of Anthropic, OpenAI, and Google Gemini across agentic coding, vision, image generation, intuitiveness, cost effectiveness, latency, and communication style. The horizontal scale runs from lower relative strength on the left to higher, better relative strength on the right.](images/model-landscape.png)

For data science applications broadly, you can loosely think of the relevant score as the average of the Agentic coding and Vision scores we've assigned here. Beyond writing R and Python data science code, models need to be able to interpret plots accurately and faithfully.

## Choosing a model by task

Much of model choice is constrained by the models you have access to. Your organization may only allow a certain provider, or you might not want to pay multiple (possibly expensive!) subscriptions just to have access to all the top models. 

Here are some quick guidelines, partially shaped by what models are currently available through [Posit AI](https://docs.posit.co/posit-ai/user/).

**The best open-weights model, especially for data analysis:** *Kimi K3*. 

As Simon wrote in the [Kimi K3 and GLM 5.2 in Posit AI announcement post](https://opensource.posit.co/blog/2026-08-10_kimi-k3-glm-5-2-posit-ai/), "Kimi K3 is currently the most capable open weights model out there. In our internal testing, it feels somewhere between Opus 5 and Fable 5, and is notably well-rounded compared to other open weights releases."

It also ranks near the top in [bluffbench2](https://github.com/posit-dev/bluffbench2) (13.46%, compared with 16.35% for the joint top scorers, Gemini 3.5 Flash and Claude Fable 5), which evaluates models' abilities to spot subtle data quality issues in visualizations.^[3]

**A highly autonomous model for a complex coding or data task when cost and speed aren't a concern:** *Claude Opus 5*, *Claude Fable 5*, or *GPT-5.6 Sol*. 

These are the top-of-the-line models from Anthropic and OpenAI. They are expensive and relatively slow, but could be justified for autonomous or ambitious work that you want to get right.

**A strong open-weights model for coding when you don't need vision:** *GLM 5.2* (from [Z.ai](https://z.ai/model-api)). 

["GLM 5.2 excels at agentic coding and less so at data analysis tasks."](https://opensource.posit.co/blog/2026-08-10_kimi-k3-glm-5-2-posit-ai/) It is much less expensive than the proprietary models it resembles for coding tasks, but it [does not natively support image inputs](https://docs.z.ai/guides/llm/glm-5.2).

**A middle-tier generalist for coding or data analysis:** *Claude Sonnet 5* or *GPT-5.6 Terra*. Both are capable across coding and routine data analysis, support vision, and are less expensive than their respective labs' top-of-the-line models.

**Good plot or image interpretation:** One of the *Gemini 3 Flash* models ([3.7 was released on August 13](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)). 

This model series is particularly strong at vision and performed well on [bluffbench](https://github.com/posit-dev/bluffbench) (3.5) and [bluffbench2](https://github.com/posit-dev/bluffbench2) (3.5 and 3.6).

**Fast answers from an Anthropic model for a task that is not particularly complex:** *Claude Haiku 4.5*.

**Fast answers from an open-weights model for a task that is not particularly complex:** [*Gemma 4*](https://posit.co/blog/gemma-4-new-budget-focused-model-posit-ai).

## Some August 2026 notes

In late summer 2026, there are a few developments that feel notable, but, as with much in the AI world, who knows how long they will last.

* **Google Gemini currently does not have any models that perform near the frontier.** With the releases of Gemini 2.5 Pro (June 2025) and the Gemini 3 series (November 2025), Google seemed positioned as a third frontier lab. However, it's been quite a while since they released a frontier model, and they're now meaningfully behind. Notably, in May 2026, they announced during I/O that they'd release Gemini 3.5 Pro in June. As of the time of writing, they've yet to release the model, instead noting that [they're training Gemini 4 and are excited about it](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/).

* For a year or so, it seemed like Anthropic was solidly ahead of OpenAI in agentic coding. However, **since the releases of Claude 4.6, it feels less clear that Anthropic is meaningfully ahead of OpenAI**. For one, Anthropic's current high-end models use newer tokenizers that, [according to Anthropic, produce roughly 30% more tokens for the same text than their predecessors, though the exact increase depends on the content and workload](https://platform.claude.com/docs/en/about-claude/models/migration-guide). This means the same listed price per token does not necessarily translate to the same cost for comparable text. Further, the Claude series has become increasingly token-hungry and difficult to communicate with. At the same time, OpenAI's models have a notably clear, concise communication style when compared to the Claude 5 series. On the measure of autonomous, long-horizon coding, Anthropic is still likely ahead, but on the measure of capable models that are pleasant to use for getting software engineering and data science work done, OpenAI is no longer behind.[^2]

* **There are now a number of balanced, well-rounded open-weights models relatively close to the closed-weights frontier.** The releases of Kimi K3 and GLM 5.2 especially show good-enough capabilities with a more pleasant, intuitive feel than their predecessors. While earlier open-weights models were just as close to the frontier in benchmark scores, a couple newer open-weights releases are notably more well-rounded and respond to prompting similarly effectively to proprietary models. Notably, these releases are priced at a steep discount compared to the proprietary models they feel most similar to. 

## Recent past newsletters

- [EDA log in Posit Assistant](../../blog/2026-07-31_ai-newsletter/)
- [Which models are best at spotting subtle data quality problems?](../../blog/2026-07-17_ai-newsletter/)

<br>
<br>

<a href="/tags/ai-newsletter/index.xml" target="_blank" rel="noopener noreferrer" class="btn-shortcode inline-flex mb-5 mr-5 items-center px-4 py-3 text-sm leading-5 gap-2 rounded-lg bg-blue-400 text-white font-semibold align-middle hover:bg-blue-500 transition no-underline">Subscribe via RSS</a>

[^1]: By "access to," we mean either the most expensive model you can afford or the most expensive model that's among the models that your organization allows you to use.

[^2]: Notably, many of our colleagues are still using Claude Opus 4.6 as their daily driver. Despite being less capable on especially long-horizon work, the model is capable of day-to-day software engineering and is cheaper in practice than newer high-end Claude models. For example, [Opus 4.6 and Opus 5 have the same listed per-token price](https://platform.claude.com/docs/en/about-claude/pricing), but Opus 4.6 predates [the newer tokenizer that can produce up to roughly 35% more tokens for the same text](https://platform.claude.com/docs/en/about-claude/models/migration-guide#migrating-from-claude-opus-46). Many of our colleagues also find Opus 4.6 easier to communicate with.

[^3]: Kimi K3 supports `low`, `high`, and `max` reasoning levels. This run used `high`, its middle setting.
