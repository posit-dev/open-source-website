---
title: "Kimi K3 and GLM 5.2 are now in Posit AI"
date: 2026-08-10
people:
  - Simon Couch
description: >
  A new batch of open weights models in Posit AI show impressive capabilities at a fraction of the price.
image: "featured.png"
image-alt: "The Posit AI logo sitting above a histogram of green dots capped by orange dots on a pale green/tan background."
topics:
  - Artificial Intelligence
software: []
languages: []
source: ai
hidesubscription: false
---

We're super stoked to share that two more open weights models—Kimi K3 and GLM 5.2—are now available as part of [Posit AI](https://posit.ai/). Both of these models are substantially cheaper than the proprietary models they feel most similar to, albeit a bit rougher on the edges. Notably, as well, these models are served much more quickly than Anthropic models; we've been seeing these models stream almost twice as many tokens per second in our internal testing, and working with them is a qualitatively different feel. [As with the other models](https://docs.posit.co/posit-ai/user/faq/#privacy-data-storage) made available in Posit AI, **your conversation histories will not be stored unless you choose to opt-in to data retention at sign-up.**

Kimi K3 is currently the most capable open weights model out there. In our internal testing, it feels somewhere between Opus 5 and Fable 5, and is notably well-rounded compared to other open weights releases. It's priced at the same price-per-token as Claude Sonnet 5.[^sonnet-pricing]

[^sonnet-pricing]: Claude Sonnet 5 is currently priced at a promotional \$2/\$10, but will be back to its usual \$3/\$15 in a few weeks. The pricing is the same _after_ Sonnet 5's promotional pricing ends.

GLM 5.2 excels at agentic coding and less so at data analysis tasks. Because the model is not vision-capable, it cannot 'see' plots and thus feels less capable for data science work. Its per-token pricing is also similar to Haiku 4.5, but feels something like Opus 4.6 or Sonnet 5 for agentic coding tasks.

## Pricing

The models in Posit AI today, at a glance:

| Model | Cached input | Input | Cache write | Output | Context length |
|:--|--:|--:|--:|--:|--:|
| Claude Opus 5 | \$0.55 | \$5.50 | \$6.875 | \$27.50 | 1M |
| Claude Sonnet 5 | \$0.33 | \$3.30 | \$4.125 | \$16.50 | 1M |
| **Kimi K3** | **\$0.33** | **\$3.30** | **\$0.00** | **\$16.50** | **250K**[^kimi-context] |
| **GLM 5.2** | **\$0.154** | **\$1.54** | **\$0.00** | **\$4.84** | **256K** |
| Claude Haiku 4.5 | \$0.11 | \$1.10 | \$1.375 | \$5.50 | 200K |
| Gemma 4 26B A4B | \$0.033 | \$0.33 | \$0.00 | \$1.65 | 100K |

[^kimi-context]: While Kimi K3 technically supports a 1M-token context window, we've limited it to 250K in Posit AI to ensure we have enough capacity.

**The cost savings are greater than the per-token pricing differences alone might suggest.** For one, the Claude 5 series models use a tokenizer that results in substantially more tokens (~35%) per word than Kimi K3's or GLM 5.2's tokenizer. Also, users are not billed at a higher rate for Cache writes than 'normal' input tokens; all input tokens are written to the cache by default, but we can't make a guarantee that you'll hit the cache after any specific delay between requests. In practice, we've seen that the cache efficiency of conversations with these deployments is slightly lower than with Claude models.

## Get started

To get started, open up [Posit Assistant](https://assistant.posit.co/) and update when prompted! Then, select your model of choice under the Posit AI model provider. If you're not already a Posit AI subscriber, you can learn more [here](https://posit.ai/).

It's worth saying that we suspect these models will rotate somewhat regularly in the service; as the months go by, we plan to introduce support for new models and deprecate others.
