---
title: Unfortunately, you need to care about token caching
slug: ai-newsletter
date: 2026-10-23T00:00:00.000Z
people:
  - Sara Altman
  - Simon Couch
description: |
  Understanding the anatomy of an LLM 'conversation' can help you
  save money.
image: images/hero.png
image-alt: >-
  Two stacked bar charts of cost per request for a three-request conversation.
  With no coffee break, request 3 is a cache hit and costs about $0.00062, for a
  conversation cost of $0.011. After a coffee break, request 3 is a cache miss
  and costs as much as request 1, nearly doubling the conversation cost to
  $0.021.
topics:
  - Artificial Intelligence
software: []
languages: []
tags:
  - ai-newsletter
  - llm-costs
source: []
nohero: false
hidesubscription: false
---


<link href="index_files/libs/htmltools-fill-0.5.9/fill.css" rel="stylesheet" />
<script src="index_files/libs/htmlwidgets-1.6.4/htmlwidgets.js"></script>
<script src="index_files/libs/plotly-binding-4.12.1/plotly.js"></script>
<script src="index_files/libs/typedarray-0.1/typedarray.min.js"></script>
<script src="index_files/libs/jquery-3.5.1/jquery.min.js"></script>
<link href="index_files/libs/crosstalk-1.2.2/css/crosstalk.min.css" rel="stylesheet" />
<script src="index_files/libs/crosstalk-1.2.2/js/crosstalk.min.js"></script>
<link href="index_files/libs/plotly-htmlwidgets-css-2.25.2/plotly-htmlwidgets.css" rel="stylesheet" />
<script src="index_files/libs/plotly-main-2.25.2/plotly-latest.min.js"></script>


How about a little riddle?

> You're using your favorite AI agent. The agent responds to you. If you respond right now, your next request will cost a fraction of a cent. If you go and make a coffee before responding, the same request will cost about a cent, roughly 16 times as much. How could that be?

## Token types

To understand what's going on, we need to take a step back. In the economics of LLMs, there are three kinds of tokens: *input tokens*, *output tokens*, and *cached input tokens*.

The first time you send a message to start a conversation, the system prompt (an "invisible" message provided by the agent that tells it how to behave) and your user prompt count as input tokens. They form the "input" that the model responds to. This response consumes output tokens.

To make this more concrete, let's walk through a hypothetical conversation with an agent. First, you say "Hi" to the agent. The agent's system prompt is made up of 10,000 tokens and "Hi" counts as one token, so sending that request consumes 10,001 *input* tokens. The model then responds with, "Hi! How can I help you today?," consuming something like ten *output* tokens.

<div class="plotly html-widget html-fill-item" id="htmlwidget-8a01c67aa5927004509d" style="width:672px;height:336px;"></div>
<script type="application/json" data-for="htmlwidget-8a01c67aa5927004509d">{"x":{"data":[{"orientation":"v","width":0.79999999999999993,"base":10001,"x":[1],"y":[10],"text":"<b>Request 1 — Output<\/b><br>10 tokens<br><br>Model: Hi! How can I help you today?","type":"bar","textposition":"none","marker":{"autocolorscale":false,"color":"rgba(204,121,167,1)","line":{"width":1.8897637795275593,"color":"transparent"}},"name":"Output","legendgroup":"Output","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"orientation":"v","width":0.79999999999999993,"base":0,"x":[1],"y":[10001],"text":"<b>Request 1 — Input<\/b><br>10,001 tokens<br><br>System: [10,000-token system prompt; omitted]<br>You: Hi","type":"bar","textposition":"none","marker":{"autocolorscale":false,"color":"rgba(230,159,0,1)","line":{"width":1.8897637795275593,"color":"transparent"}},"name":"Input","legendgroup":"Input","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"orientation":"v","width":0.79999999999999993,"base":0,"x":[1],"y":[0],"text":"","type":"bar","textposition":"none","marker":{"autocolorscale":false,"color":"rgba(0,158,115,1)","line":{"width":1.8897637795275593,"color":"transparent"}},"name":"Cached input","legendgroup":"Cached input","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null}],"layout":{"margin":{"t":60,"r":7.9701120797011216,"b":24.707347447073481,"l":66.151930261519325},"paper_bgcolor":"rgba(255,255,255,1)","font":{"color":"rgba(0,0,0,1)","family":"","size":15.940224159402243},"xaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[0.19999999999999996,6.7999999999999998],"tickmode":"array","ticktext":["Request 1"],"tickvals":[1],"categoryorder":"array","categoryarray":["Request 1"],"nticks":null,"ticks":"","tickcolor":null,"ticklen":3.9850560398505608,"tickwidth":0,"showticklabels":true,"tickfont":{"color":"rgba(107,107,107,1)","family":"","size":12.7521793275218},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":false,"gridcolor":null,"gridwidth":0,"zeroline":false,"anchor":"y","title":{"text":"","font":{"color":null,"family":null,"size":0}},"hoverformat":".2f","fixedrange":true},"yaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[0,10511.549999999999],"tickmode":"array","ticktext":["0","2,500","5,000","7,500","10,000"],"tickvals":[0,2500,5000,7500,10000],"categoryorder":"array","categoryarray":["0","2,500","5,000","7,500","10,000"],"nticks":null,"ticks":"","tickcolor":null,"ticklen":3.9850560398505608,"tickwidth":0,"showticklabels":true,"tickfont":{"color":"rgba(107,107,107,1)","family":"","size":12.7521793275218},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(232,232,232,1)","gridwidth":0.72455564360919289,"zeroline":false,"anchor":"x","title":{"text":"Tokens","font":{"color":"rgba(107,107,107,1)","family":"","size":15.940224159402243}},"hoverformat":".2f","fixedrange":true},"shapes":[],"showlegend":true,"legend":{"bgcolor":null,"bordercolor":null,"borderwidth":0,"font":{"color":"rgba(107,107,107,1)","family":"","size":12.7521793275218},"orientation":"h","x":0.5,"y":-0.14999999999999999,"xanchor":"center","yanchor":"top","title":{"text":"","font":{"color":null,"family":null,"size":0}}},"hovermode":"closest","barmode":"relative","dragmode":false,"hoverlabel":{"bgcolor":"white","bordercolor":"#d9d9d9","font":{"color":"#333333","size":12}},"annotations":[{"text":"10 output tokens","x":1.3,"y":10011,"xanchor":"left","showarrow":true,"ax":40,"ay":-16,"arrowhead":2,"arrowsize":0.80000000000000004,"arrowwidth":1,"arrowcolor":"#6b6b6b","font":{"color":"#6b6b6b","size":12}},{"text":"10 output tokens","x":1.3,"y":10011,"xanchor":"left","showarrow":true,"ax":40,"ay":-16,"arrowhead":2,"arrowsize":0.80000000000000004,"arrowwidth":1,"arrowcolor":"#6b6b6b","font":{"color":"#6b6b6b","size":12}}]},"config":{"doubleClick":false,"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false,"displayModeBar":false,"scrollZoom":false},"source":"A","attrs":{"e5f02e38ca1d":{"text":{},"x":{},"y":{},"fill":{},"type":"bar"}},"cur_data":"e5f02e38ca1d","visdat":{"e5f02e38ca1d":["function (y) ","x"]},"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":{"render":[{"code":"function(el) {\n        el.on('plotly_hover', function() {\n          // Keep callouts from competing with the tooltip while hovering.\n          el.querySelectorAll('.annotation').forEach(function(annotation) {\n            annotation.style.visibility = 'hidden';\n          });\n          window.requestAnimationFrame(function() {\n            var layer = el.querySelector('.hoverlayer');\n            if (!layer) return;\n            layer.removeAttribute('transform');\n            var frame = el.getBoundingClientRect();\n            var box = layer.getBoundingClientRect();\n            var dx = Math.max(0, frame.left + 8 - box.left) -\n              Math.max(0, box.right - frame.right + 8);\n            var dy = Math.max(0, frame.top + 8 - box.top) -\n              Math.max(0, box.bottom - frame.bottom + 8);\n            layer.setAttribute('transform', 'translate(' + dx + ',' + dy + ')');\n          });\n        });\n        el.on('plotly_unhover', function() {\n          el.querySelectorAll('.annotation').forEach(function(annotation) {\n            annotation.style.removeProperty('visibility');\n          });\n          var layer = el.querySelector('.hoverlayer');\n          if (layer) layer.removeAttribute('transform');\n        });\n      }","data":null}]}}</script>

Now, you're ready to send another message to the agent.[^1] This time, the numbers are going to shift around a bit. You ask the agent, "When was ggplot2 released?". Assuming the cache is still warm, the 10,001 tokens sent as input on the first request can now count as *cached input tokens*. A cached input token is an input token that the model provider has already processed and stored, so it can reuse that work instead of doing it again.

There are also new input tokens: the model's previous 10-token reply, which is being sent back as input for the first time, and your second question ("When was ggplot2 released?"), which we'll count as another 10 tokens. That makes 20 new input tokens. The model answers the question in a sentence, resulting in another 10 output tokens.

So, by request:

<div class="plotly html-widget html-fill-item" id="htmlwidget-9415b9baff1eda5b7048" style="width:672px;height:336px;"></div>
<script type="application/json" data-for="htmlwidget-9415b9baff1eda5b7048">{"x":{"data":[{"orientation":"v","width":[0.79999999999999993,0.79999999999999982],"base":[10001,10021],"x":[1,2],"y":[10,10],"text":["<b>Request 1 — Output<\/b><br>10 tokens<br><br>Model: Hi! How can I help you today?","<b>Request 2 — Output<\/b><br>10 tokens<br><br>Model: ggplot2 was first released in 2007."],"type":"bar","textposition":"none","marker":{"autocolorscale":false,"color":"rgba(204,121,167,1)","line":{"width":1.8897637795275593,"color":"transparent"}},"name":"Output","legendgroup":"Output","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"orientation":"v","width":[0.79999999999999993,0.79999999999999982],"base":[0,10001],"x":[1,2],"y":[10001,20],"text":["<b>Request 1 — Input<\/b><br>10,001 tokens<br><br>System: [10,000-token system prompt; omitted]<br>You: Hi","<b>Request 2 — Input<\/b><br>20 tokens<br><br>Model: Hi! How can I help you today?<br>You: When was ggplot2 released?"],"type":"bar","textposition":"none","marker":{"autocolorscale":false,"color":"rgba(230,159,0,1)","line":{"width":1.8897637795275593,"color":"transparent"}},"name":"Input","legendgroup":"Input","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null},{"orientation":"v","width":[0.79999999999999993,0.79999999999999982],"base":[0,0],"x":[1,2],"y":[0,10001],"text":["","<b>Request 2 — Cached input<\/b><br>10,001 tokens<br><br>System: [10,000-token system prompt; omitted]<br>You: Hi"],"type":"bar","textposition":"none","marker":{"autocolorscale":false,"color":"rgba(0,158,115,1)","line":{"width":1.8897637795275593,"color":"transparent"}},"name":"Cached input","legendgroup":"Cached input","showlegend":true,"xaxis":"x","yaxis":"y","hoverinfo":"text","frame":null}],"layout":{"margin":{"t":60,"r":7.9701120797011216,"b":24.707347447073481,"l":66.151930261519325},"paper_bgcolor":"rgba(255,255,255,1)","font":{"color":"rgba(0,0,0,1)","family":"","size":15.940224159402243},"xaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[0.19999999999999996,6.7999999999999998],"tickmode":"array","ticktext":["Request 1","Request 2"],"tickvals":[1,2],"categoryorder":"array","categoryarray":["Request 1","Request 2"],"nticks":null,"ticks":"","tickcolor":null,"ticklen":3.9850560398505608,"tickwidth":0,"showticklabels":true,"tickfont":{"color":"rgba(107,107,107,1)","family":"","size":12.7521793275218},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":false,"gridcolor":null,"gridwidth":0,"zeroline":false,"anchor":"y","title":{"text":"","font":{"color":null,"family":null,"size":0}},"hoverformat":".2f","fixedrange":true},"yaxis":{"domain":[0,1],"automargin":true,"type":"linear","autorange":false,"range":[0,10532.549999999999],"tickmode":"array","ticktext":["0","2,500","5,000","7,500","10,000"],"tickvals":[0,2500,5000,7500,10000],"categoryorder":"array","categoryarray":["0","2,500","5,000","7,500","10,000"],"nticks":null,"ticks":"","tickcolor":null,"ticklen":3.9850560398505608,"tickwidth":0,"showticklabels":true,"tickfont":{"color":"rgba(107,107,107,1)","family":"","size":12.7521793275218},"tickangle":-0,"showline":false,"linecolor":null,"linewidth":0,"showgrid":true,"gridcolor":"rgba(232,232,232,1)","gridwidth":0.72455564360919289,"zeroline":false,"anchor":"x","title":{"text":"Tokens","font":{"color":"rgba(107,107,107,1)","family":"","size":15.940224159402243}},"hoverformat":".2f","fixedrange":true},"shapes":[],"showlegend":true,"legend":{"bgcolor":null,"bordercolor":null,"borderwidth":0,"font":{"color":"rgba(107,107,107,1)","family":"","size":12.7521793275218},"orientation":"h","x":0.5,"y":-0.14999999999999999,"xanchor":"center","yanchor":"top","title":{"text":"","font":{"color":null,"family":null,"size":0}}},"hovermode":"closest","barmode":"relative","dragmode":false,"hoverlabel":{"bgcolor":"white","bordercolor":"#d9d9d9","font":{"color":"#333333","size":12}}},"config":{"doubleClick":false,"modeBarButtonsToAdd":["hoverclosest","hovercompare"],"showSendToCloud":false,"displayModeBar":false,"scrollZoom":false},"source":"A","attrs":{"e5f0d7e7d1b":{"text":{},"x":{},"y":{},"fill":{},"type":"bar"}},"cur_data":"e5f0d7e7d1b","visdat":{"e5f0d7e7d1b":["function (y) ","x"]},"highlight":{"on":"plotly_click","persistent":false,"dynamic":false,"selectize":false,"opacityDim":0.20000000000000001,"selected":{"opacity":1},"debounce":0},"shinyEvents":["plotly_hover","plotly_click","plotly_selected","plotly_relayout","plotly_brushed","plotly_brushing","plotly_clickannotation","plotly_doubleclick","plotly_deselect","plotly_afterplot","plotly_sunburstclick"],"base_url":"https://plot.ly"},"evals":[],"jsHooks":{"render":[{"code":"function(el) {\n        el.on('plotly_hover', function() {\n          // Keep callouts from competing with the tooltip while hovering.\n          el.querySelectorAll('.annotation').forEach(function(annotation) {\n            annotation.style.visibility = 'hidden';\n          });\n          window.requestAnimationFrame(function() {\n            var layer = el.querySelector('.hoverlayer');\n            if (!layer) return;\n            layer.removeAttribute('transform');\n            var frame = el.getBoundingClientRect();\n            var box = layer.getBoundingClientRect();\n            var dx = Math.max(0, frame.left + 8 - box.left) -\n              Math.max(0, box.right - frame.right + 8);\n            var dy = Math.max(0, frame.top + 8 - box.top) -\n              Math.max(0, box.bottom - frame.bottom + 8);\n            layer.setAttribute('transform', 'translate(' + dx + ',' + dy + ')');\n          });\n        });\n        el.on('plotly_unhover', function() {\n          el.querySelectorAll('.annotation').forEach(function(annotation) {\n            annotation.style.removeProperty('visibility');\n          });\n          var layer = el.querySelector('.hoverlayer');\n          if (layer) layer.removeAttribute('transform');\n        });\n      }","data":null}]}}</script>

### Cached input tokens are much cheaper

It's great news that most of this second turn is composed of cached input tokens. Why? Because cached input tokens are *much less expensive* than uncached input tokens. Output tokens often cost several times as much as input tokens, and uncached input tokens can cost 10--20 times as much as cached input tokens. For our example, we'll use ratios of 10× and 20×, respectively.[^2] At those ratios, output tokens cost 200× as much as cached input tokens.

## Cache hits and misses

Now, let's revisit the question we kicked off this post with. The agent has just told us when ggplot2 was released. Before sending your next message, you can go and make a coffee if you want, but your next message will cost much more if you do. Why?

We've already seen that cached input tokens cost far less than normal input tokens. The kicker is that you don't always hit the cache. The cache is essentially the provider storing your already-processed tokens, which takes up space, so they only keep it "warm" for a certain amount of time. After that time, they discard it to make room for other users' conversations, and even tokens previously sent to the model are treated as new, "unseen" ones and billed accordingly.

While you've stepped away from your computer to make a coffee, your cache might grow "cold" when your provider discards it. If that happens, the next request you send will miss the cache, and all the tokens that would otherwise be billed as cached input tokens will instead be billed as normal input tokens.

So, the chart above could look one of two ways, depending on whether your third message is a cache hit or not:

<img src="index.markdown_strict_files/figure-markdown_strict/request-3-hit-miss-1.png" data-fig-align="center" width="672" />

Such large discrepancies in price-per-token mean that charts showing only the token counts of a given request might lead to poor intuitions about the cost of conversations. Here's the same chart, but the y-axis has been switched from number of tokens to cost of tokens:

<img src="index.markdown_strict_files/figure-markdown_strict/request-3-hit-miss-cost-1.png" data-fig-align="center" width="672" />

## So can I ever take a break again?

This all might seem pretty stressful. Does this mean you can never take a coffee break again?! Do agents really need our attention this desperately? In practice, many mediating factors mean that cache misses aren't usually so bad. However, that doesn't mean you can ignore token caching if you're using coding agents in an intensive way. The cost of ignoring cache concerns entirely adds up really fast.

But there are a couple of considerations that should make you feel better about taking that break.

### Cache hits can be partial

Our opening example treated the cache status of the previously submitted input as all-or-nothing: either the next request reused all of it, or none of it. In practice, a request may constitute a partial cache hit, reusing a cached beginning (called a *prefix*) often made up of the system prompt and tool definitions, even if your messages are not cached.

For example, suppose our 10,000-token system prompt is already cached when the conversation starts and stays cached throughout. After a coffee break, the third request can still reuse that cached beginning, even if it has to process the later conversation history again:

<figure>
<img src="index.markdown_strict_files/figure-markdown_strict/system-prompt-cached-1.png" data-fig-align="center" width="672" alt="Hypothetical costs with the system prompt cached throughout. After the coffee break, request 3 reuses the system prompt but not the later conversation history." />
<figcaption aria-hidden="true">Hypothetical costs with the system prompt cached throughout. After the coffee break, request 3 reuses the system prompt but not the later conversation history.</figcaption>
</figure>

If that happens, the coffee break costs less than a complete cache miss would.

### How long does the cache stay warm?

In our example, the time it takes to make a coffee was enough to cause a cache miss. In reality, you might have longer, depending on the agent.

Some model providers provide explicit cache *time-to-live*, or TTL. A cache TTL means that, if you submit a compatible prompt within a specified window, its matching cached prefix is eligible for cached input pricing. For example, OpenAI offers a 30-minute cache TTL on GPT-5.6 and later models. By paying slightly more for cache writes the first time around (1.25x the ordinary input-token rate), you can pay the cached input price for matching, eligible prefixes when you submit another message (whether in Codex or [Posit Assistant](https://assistant.posit.co/)) in the next 30 minutes.

In Claude Code, requests billed per token default to a 5-minute cache TTL, with a more expensive 60-minute option. The main conversation defaults to 60 minutes when using a Claude subscription's included usage.

Not all providers offer a defined cache-retention window, so how long you can wait before a cache miss isn't always predictable.[^3]

So, in reality, you often have longer than the time it takes to make a coffee, but this depends on the provider.

### Posit Assistant helps keep your cache warm

More good news: if you're using [Posit Assistant](https://assistant.posit.co/), you'll probably have more time to devote to making an elaborate coffee without missing the cache. This is because Posit Assistant has a feature called *cache keepalive* that helps keep the cache warm. Cache keepalive is enabled by default for supported models. By default, it can send pings for up to 30 minutes after a real model request to keep the cache warm.

With Anthropic models, Posit Assistant uses a 5-minute cache TTL by default. Most requests from Posit Assistant (many of them tool results rather than user messages) are submitted much more quickly than 5 minutes after the most recent response; it thus doesn't make much sense to pay the premium for a 60-minute cache TTL. That said, even with a 5-minute cache TTL, we can help our users avoid a cache miss by sending lightweight requests under the hood about every 4 minutes and 30 seconds, capping output at 1 token. These "pings" refresh the cache but still have a cost, so the feature has to be tuned correctly to save the user money. We've found that sending a few of these pings for active sessions reliably reduces costs, at least among Posit Assistant's developers.

## How to keep costs down

There are also actions you as the user can take (besides never leaving your agents alone, which we don't recommend) to manage your cache.

### Understand what your conversation costs

You don't have to guess whether your requests are hitting the cache. The available information varies by agent, but the key number to look for is *cache reads*: input tokens whose processing the provider reused.

#### Posit Assistant

In Posit Assistant, you can see conversation information by clicking the token counter next to the model picker.

Hover over a bar in the token/cost usage chart to inspect an individual request.

<figure>
<img src="images/session-info-hud.png" data-fig-align="center" data-fig-alt="Session-information panel with a context meter, token-usage chart, and table separating output, uncached input, cache writes, and cache reads. The table shows 66.2% cache efficiency. Controls below enable cost displays and cache-keepalive pings." width="636" alt="Posit Assistant’s session-information panel breaks down token usage and estimated costs by token type." />
<figcaption aria-hidden="true">Posit Assistant’s session-information panel breaks down token usage and estimated costs by token type.</figcaption>
</figure>

#### Claude Code

In recent versions of Claude Code, you can see cache statistics by running [`/usage`](https://code.claude.com/docs/en/costs).

#### Other agents

For any agent, you can also use tools like [AgentsView](https://agentsview.io), which reports token usage and costs across many coding agents, or inspect your transcripts directly to learn more about your token and cache usage. For Claude Code, transcripts are written to `~/.claude/projects/` by default. For Codex, it's `~/.codex/sessions/`. You can ask a coding agent to take a look at these transcripts to get a more detailed view of your conversations.

### Know which changes can disrupt cache reuse

Other changes besides just time can disrupt cache reuse. One change you might encounter is switching models in the middle of the conversation, which will result in a cache miss. The conversation cache does not transfer from one model to another. For some models, this is also the case for switching from one thinking level to another. For example, switching from Opus 5 (low) to Opus 5 (high). Some newer model releases support switching thinking levels without breaking the cache, though.

### Manage conversation length

Our earlier example, where the system prompt was about ten thousand tokens while the user and agent messages were on the order of tens of tokens, was a bit contrived. In reality, agentic conversations can grow quite large quite quickly. It's not uncommon to see conversations where, for each short message (say, ~100 tokens) a user sends, there are 10 rounds of back-and-forth where the model calls tools and receives a response. In this case, if the typical tool call takes 300 output tokens, and the typical tool result takes 1000 input tokens, the full conversation length will be about 131,000 tokens after 10 user messages. Here's what each of those 100 requests looks like in tokens and in cost, assuming every one of them hits the cache:

<img src="index.markdown_strict_files/figure-markdown_strict/long-conversation-1.png" data-fig-align="center" data-fig-alt="Two stacked bar charts of the same 100 requests side by side. In tokens, the bars climb steadily to about 130,000 and are almost entirely cached input. In cost, output and new input stay about the same size in every bar while cached input grows, so the bars rise from under half a cent to about one cent, dipping slightly every tenth request, when the user sends a new message." width="672" />

Because every request resends the entire conversation so far, each request is bigger than the one before it. In tokens, that rereading dominates: almost every bar is cached input. In dollars, caching keeps the rereading cheap, so output and new input, which cost about the same every time, make up a much larger share of each request. At our illustrative prices, the last request costs only about 3 times as much as the first.

Long conversations raise the stakes of a cache miss, though, because a miss means paying full price for all of that history. If you take a coffee break before the last request and miss the cache, that one message costs about \$0.13 instead of \$0.01, roughly 12 times as much.

To keep token costs down, you might keep an eye out for good "stopping moments" in the conversation. If you come across one, start a new conversation or clear the current conversation history (`/clear` in most coding agents). If you want to retain a summary of your work, compact the conversation instead (`/compact` in most coding agents).

We recommend starting new conversations or compacting when switching from one task to another, such as when you're finished planning a feature and want to start implementing it. You should also probably find a stopping place once the conversation length exceeds 200,000 tokens or so (for models that support longer conversations). With this in mind, Posit Assistant has a small circle beside the conversation length that is green for shorter conversations, yellow for mid-length, and red for very long ones. Once you see a yellow circle, look for a natural stopping point.

## Unfortunately, you do need to care about caching

It can be tempting to ignore caching and carry on conversations with your agents at your preferred pace, not theirs. But these costs can really add up. The plots in this post deal in cents, but over a month, the difference between paying attention to caching and ignoring it can amount to tens or hundreds of dollars (or more) depending on how heavily you use these tools. That's probably especially worth keeping in mind if you're paying for tokens yourself. Understanding how your agent handles caching can help you avoid paying more than you need to for tokens.

[^1]: LLMs are stateless. They don't remember earlier requests on their own. Each new request therefore typically provides the entire conversation history as input, including earlier model replies.

[^2]: The cost charts in this post use illustrative prices with these ratios: \$10 per million output tokens, \$1 per million input tokens, and \$0.05 per million cached input tokens. Actual prices vary by model.

[^3]: For OpenAI models before GPT-5.6, cache retention is best-effort rather than guaranteed. In-memory caches typically last 5--10 minutes of inactivity and may last up to an hour. Some of these models support extended retention, also without a guaranteed lifetime. See OpenAI's prompt-caching guide: https://developers.openai.com/api/docs/guides/prompt-caching.
