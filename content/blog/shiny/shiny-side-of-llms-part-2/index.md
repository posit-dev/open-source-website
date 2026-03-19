---
title: 'Talking to LLMs: From Prompt to Response'
description: >
  In this second part of The Shiny Side of LLMs we get into the fun of actually
  talking to an LLM. From crafting prompts that get the responses you want, to
  turning messy outputs into something useful, giving models extra powers with
  tools, and figuring out what all the chatter really costs.
people:
  - Veerle Eeftink - van Leemput
date: '2025-09-05'
image: shiny-side-of-llms-header.png
image-alt: The Shiny Side of LLMs part 2
ported_from: shiny
port_status: in-progress
---


Welcome back to "The Shiny Side of LLMs": a blog series for Python and R users who want to build real, useful LLM-powered apps without getting buried in jargon or deep learning theory.

In [Part 1: What LLMs Actually Do (and What They Don't)](../../../blog/shiny/shiny-side-of-llms-part-1/), we looked at how large language models generate responses, why they sometimes seem so smart (and other times so confidently wrong), and what kinds of tasks they're actually good at. Now it's time to get hands-on!

In this part, we'll focus on what it means to talk to an LLM. We'll cover crafting prompts to parsing responses, and everything in between. You'll learn:

- How to call an LLM via [`chatlas`](https://posit-dev.github.io/chatlas/) (Python) and [`ellmer`](https://ellmer.tidyverse.org/) (R)
- The basics of prompt design: roles, instructions, system messages, temperature, and more
- What goes in and what comes out, and how your own data fits into that loop
- How to work with model outputs: parsing, structuring, and getting predictable results
- How to give LLMs extra power with tools
- Costs involved when talking to LLMs

By the end of this part, you'll be ready to go from "I asked ChatGPT a thing" to "I can programmatically talk to an LLM by sending custom prompts and doing something useful with the results".

> **No time for the walkthrough?**
>
> Jump straight to the [full workflow](#full-workflow).

# The app: DeckCheck

In this series we're working towards a genius app that gets rid of lengthy unfocused presentations, like a perfect "Presentation Rehearsal Buddy". No app without a snappy name, so hello "DeckCheck". The goal: let users upload their Quarto presentation and provide them with feedback on how to make it better.

So how would we go about that? To give meaningful feedback on a presentation, we need to ask the LLM the right questions. For example:

- Does the presentation have a clear structure?
- Are the key messages easy to spot?
- Does the tone match the intended audience?
- Are the slides too wordy, too vague, or just right?
- Is there a good balance between words, visuals, and code?

If you've used ChatGPT or another LLM in a chat interface, the process feels straightforward: you ask any of the above questions, and the model replies. But when you're building an app, you're not just having a conversation. You want to have some form of control. After all, you're designing a system. You need to construct prompts carefully, handle responses programmatically, and ensure the whole exchange is stable enough to support user-facing features. In our case, that means feeding slide content into the LLM and asking targeted questions about structure, clarity, and tone. And we're not just hoping for a helpful paragraph with some witty comments. For our app we need output that's predictable, parseable, and ready to plug into our app logic. Eventually we want to be able to extract suggestions, metrics, scores: things that we also need to retrieve programmatically.

So in this part, it's not just about asking questions, it's about:

- How to design prompts that get reliable, structured answers
- How to "control" model behaviour (as far as you can, at least)
- How to send slide content (or any other data) to an LLM
- And how to process the model's output into something our future app can actually use

Let's build!

> **What can you expect from this second part?**
>
> This part focusses on programmatically talking to an LLM. We leave the Shiny app building to the third and last part of "The Shiny Side of LLMs" series. The code we end up with in this part serves as a basis for the back-end of our app in this next part.

# What do you need?

Ah, is it even a tutorial if there isn't a "getting started" step? But there's one obvious thing we need: access to an LLM. To get that, you'll need to sign up for a (developer) account with a provider like OpenAI or Anthropic. And with that comes something that feels like a huge barrier: setting up payment details. I feel you when you might be getting anxious about an invoice with a lot of zeros, but really, don't worry too much about that. Almost all platforms offer free trial credits, and you can usually set usage limits or buy fixed prepaid credits (Anthropic makes this especially easy). So that invoice-nightmare won't come alive easily. Still a little bit worried? Google's model Gemini offers a generous free tier.

Once you've registered, you can get an API key. You need this key to authenticate with the LLM provider. Never, ever hardcode the key directly into your script. You'll be amazed how many keys are publicly available on GitHub repos. Don't be that developer. As always with secrets, store it as an environment variable. Just note that the exact name of the key depends on the provider. For example, Anthropic expects `ANTHROPIC_API_KEY=yourkey`, while OpenAI uses `OPENAI_API_KEY=yourkey`.

To keep things simple, we'll go with Anthropic for the examples in this blog series, but feel free to choose any provider you want. Don't worry about lock-in either: you'll see that switching providers and models is super easy.

## Where to store your API key

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-1" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-1-1">Python</a></li>
<li><a href="#tabset-1-2">R</a></li>
</ul>
<div id="tabset-1-1">

In Python, the recommended approach is to create a `.env` file in your project folder:

``` python
ANTHROPIC_API_KEY=yourkey
```

It's recommended to use the `dotenv` package to load the `.env` file into your environment:

``` python
from dotenv import load_dotenv

load_dotenv()
```

</div>
<div id="tabset-1-2">

In R, environment variables are typically stored in a `.Renviron` file. You can create this file in your project root or in your home directory (`~/.Renviron`). Or, if you want to make it yourself really easy: you can also open/edit the relevant file with `usethis::edit_r_environ()`.

``` r
ANTHROPIC_API_KEY=yourkey
```

</div>
</div>

Just be sure to add `.env` and `.Renviron` to your `.gitignore` file so you don't accidentally publish your keys.

## Installing `chatlas` or `ellmer`

Working with different LLM providers can be a pain, but luckily there is the perfect solution: [`chatlas`](https://posit-dev.github.io/chatlas/) for Python and [`ellmer`](https://ellmer.tidyverse.org) for R. Hello simple and consistent interface! From Anthropic's Claude to (Azure) OpenAI and Google Gemini: it's all possible. And bonus: `chatlas` and `ellmer` both have the same interface, making it easy to translate your LLM projects between Python and R!

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-2" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-2-1">Python</a></li>
<li><a href="#tabset-2-2">R</a></li>
</ul>
<div id="tabset-2-1">

For Python, `chatlas` is available on PyPI, so you can install it easily with `pip`:

``` bash
pip install chatlas
```

Or, if you're using `uv`, add it like so:

``` bash
uv add chatlas
```

Once installed, import it like this:

``` python
import chatlas
```

Depending on the LLM provider you will choose, you might need to install additional packages (e.g. `anthropic` for, surprise, models from Anthropic). For every provider, the relevant function reference page in the [`chatlas` docs](https://posit-dev.github.io/chatlas/reference/) will tell you what's necessary together with credential acquisition tips (e.g. [`ChatAnthropic`](https://posit-dev.github.io/chatlas/reference/ChatAnthropic.html)).

</div>
<div id="tabset-2-2">

You can install `ellmer` from CRAN using:

``` r
install.packages("ellmer")
```

Once installed, load the package as usual:

``` r
library(ellmer)
```

</div>
</div>

> **Switching between Python and R**
>
> Did you know you can very easily switch between Python and R in [Positron](https://positron.posit.co)? Just select the interpreter you want (you can even choose between Python and R installs), and you're good to go!

# Your first conversation

Time to chat! Whether you're using Python or R, the workflow is the same. First, you need to create a chat object. You can give it any name you like, but `chat` seems the most obvious choice here. This `chat` object is created with a specific function for your chosen provider, where you (optionally) can specify the model. While the `model` argument isn't required, it is strongly recommended you do specify it. After all, we're looking for consistent behaviour in our Shiny app, and a change in default model choice isn't going to give us that. In our case we will go for claude-sonnet-4-20250514 from [Anthropic](https://docs.anthropic.com/en/docs/about-claude/models/overview), which is the latest (reasonably priced) model at the time of writing.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-3" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-3-1">Python</a></li>
<li><a href="#tabset-3-2">R</a></li>
</ul>
<div id="tabset-3-1">

``` python
from dotenv import load_dotenv
from chatlas import ChatAnthropic

load_dotenv()  # Loads key from the .env file

chat = ChatAnthropic(model="claude-sonnet-4-20250514")
```

</div>
<div id="tabset-3-2">

``` r
library(ellmer)

chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514"
)
```

In `ellmer` 0.3.0 you can also use `chat()` using a string like `chat("anthropic")` or `chat("openai/gpt-4.1-nano")`.

Not sure what models are available? You can use `models_*()`, e.g. `models_anthropic()`, to get a list of available models.

</div>
</div>

> **API keys and environment variables**
>
> There's no need to explicitly provide your API key to `chatlas` or `ellmer`. If you specify it with the correct name in your environment file (`.env` or `.Renviron`), `chatlas` or `ellmer` will automatically find it. There's an `api_key` argument, but generally you won't use this. For Python, it's recommended to use the `dotenv` package to load the `.env` file into your environment.

You can call the `chat` method on the `chat` object. When you use the `chat` method:

- You see the response appear in your console, piece by piece, like it's being typed out. That's the streaming part.
- The full message is also (invisibly) saved as a character vector, so you can use it in your code later.

For simplicity, let's start with our very basic first prompt: "I'm working on a presentation with the title: 'The Shiny Side of LLMs'. What's your feedback just based on that title?"

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-4" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-4-1">Python</a></li>
<li><a href="#tabset-4-2">R</a></li>
</ul>
<div id="tabset-4-1">

``` python
from dotenv import load_dotenv
from chatlas import ChatAnthropic

load_dotenv()  # Loads key from the .env file

chat = ChatAnthropic(model="claude-sonnet-4-20250514")

chat.chat(
  "I'm working on a presentation with the title: 'The Shiny Side of LLMs'. 
  What's your feedback just based on that title?"
)
```

<details class="code-fold">
<summary>Show output</summary>

``` python
"""
That's a clever and engaging title! Here's my feedback:                                           

What works well:                                                                                            
  • The wordplay on "shiny" is effective - it suggests both the exciting/promising aspects of LLMs and has a 
  nice tech-forward feel                                                                                   
  • It's concise and memorable                                                                               
  • Sets an optimistic, forward-looking tone for your presentation                                           

Potential considerations:                                                                         

  • The phrase "shiny side" might evoke "bright side" or even "dark side," which could work for or against   
  you depending on your audience's associations                                                            
  • It's somewhat informal - great for most audiences, but consider if your context requires more formal     
  language                                                                                                 
  • Without additional context, it's not immediately clear what specific aspects you'll cover (capabilities, 
  applications, benefits, etc.)                                                                            

Questions to consider:                                                                            
  
  • Who's your audience? (Technical experts, business leaders, general public?)                              
  • Are you contrasting with challenges/limitations, or purely focusing on positives?                        
  • What's the main takeaway you want people to remember?                                                    

Overall, it's an attention-grabbing title that should work well for most presentations about LLM benefits   
and capabilities. You might consider a subtitle if you want to hint at your specific focus areas. 
"""
```

</details>
</div>
<div id="tabset-4-2">

``` r
library(ellmer)

chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514"
)

chat$chat(
  "I'm working on a presentation with the title: 'The Shiny Side of LLMs'. 
  What's your feedback just based on that title?"
)
```

<details class="code-fold">
<summary>Show output</summary>

``` r
#> That's a clever and engaging title! Here's my feedback:
#> 
#> **Strengths:**
#> - **Memorable wordplay** – "shiny" is a nice play on both the positive aspects and the tech/AI aesthetic  
#> - **Clear focus** – Immediately signals you're highlighting the benefits/successes rather than risks or limitations  
#> - **Accessible language** – Avoids jargon while still being specific to your audience  
#> 
#> **Considerations:**
#> - **Audience expectations** – The playful tone suggests this might be more of an overview/promotional presentation rather than a deep technical dive. Make sure that aligns with your goals.  
#> - **Balance question** – Will you acknowledge any limitations, or is this specifically meant to be a positive-focused presentation? The title suggests the latter.  
#> 
#> **Potential alternatives** (if you want to explore):  
#> - "LLMs: The Bright Side of AI"  
#> - "When LLMs Shine: Success Stories and Breakthroughs"  
#> - "The Promise of LLMs: Real-World Wins"  
#> 
#> But honestly, your original title works well – it's catchy and sets clear expectations. The success will depend on whether your content delivers on that promise of showcasing genuinely impressive LLM capabilities and applications.  
#> 
#> What's the context/audience for this presentation?
```

</details>
</div>
</div>

The `chat` object is a stateful object, which means it "remembers stuff". It accumulates conversation history by default. This history is provided to the LLM with every subsequent question. So if you send a second question, it will package your prompt so it contains the first question, the first answer, and your second question. This is desired behaviour for multi-turn conversations since it allows the model to "remember" previous interactions. That's important, because out of the box, the model doesn't remember what you said two messages ago. It only has the input you provide, right here, right now. That's its entire world. So every time (with every request) you have to remind the LLM of prior context. You can learn more about this in [the first part of this series](../../../blog/shiny/shiny-side-of-llms-part-1/).

> **Some chat terminology**
>
> Let's get some terms straight: you (the user) have a chat with the LLM (the assistant). Every chat, aka conversation, consists of pairs of user and assistant turns. The questions you ask correspond to an HTTP request, and the response that gets returned corresponds to an HTTP response.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-5" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-5-1">Python</a></li>
<li><a href="#tabset-5-2">R</a></li>
</ul>
<div id="tabset-5-1">

``` python
from dotenv import load_dotenv
from chatlas import ChatAnthropic

load_dotenv()  # Loads key from the .env file

chat = ChatAnthropic(model="claude-sonnet-4-20250514")

chat.chat(
    "I'm working on a presentation with the title: 'The Shiny Side of LLMs'. 
    What's your feedback just based on that title?"
)
chat.chat("What is my presentation title?")
```

``` python
"""
Your presentation title is: "The Shiny Side of LLMs"
"""
```

In the remainder of this article, we will leave the `dotenv` part out for brevity. You do need it for the `.env` approach, but there are also other ways to load environment variables, like setting them in your bash/zsh profile.

</div>
<div id="tabset-5-2">

``` r
library(ellmer)

chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514"
)

chat$chat(
  "I'm working on a presentation with the title: 'The Shiny Side of LLMs'. 
  What's your feedback just based on that title?"
)

chat$chat("What is my presentation title?")
```

``` r
#> Your presentation title is: "The Shiny Side of LLMs"
```

</div>
</div>

# Designing effective prompts

> **TL;DR**
>
> Defining the **role**, **task**, **context**, and **output format** sets the foundation for a good conversation with the model.

In our first conversation, our prompt ("I'm working on a presentation with the title: 'The Shiny Side of LLMs'. What's your feedback just based on that title?") is very general and leads to some issues: the model, Claude, doesn't know who the audience is, what kind of feedback you're looking for (tone, clarity, technical depth?), or what role it should take. As a result, the response is polite and somewhat helpful, but not really focused or consistent. It's basically guessing, and it will guess something different every single time. Our prompt is very important for the model's output, so we need to make it better by including:

- **Role**: who the model is acting as. We didn't tell the model who it should be or how it should respond. Saying something like: "You are a presentation coach for data scientists", helps to get more relevant feedback. It also referred to as adding "colour" to your prompt, or framing.
- **Task**: what the model should do. We asked for "feedback", but that's not explicit at all. It's better to ask something like: "Evaluate the title's clarity, tone, and relevance for a non-technical audience".
- **Context**: a bit more information about the situation. The more a model knows, the more on-point an answer will be. Who's our intended audience? Is it a keynote, a lightning talk or a workshop? In our to-be app, we can get this information directly from the user when they are uploading their Quarto slides, and include it in our prompt. It's as simple as adding: "This is for a 10-minute lightning talk at [posit::conf(2025)](https://posit.co/conference/) for people curious about AI". How much context (aka tokens) you can add is dependent on the model. Claude Sonnet 4 recently [supports 1M tokens of context](https://www.anthropic.com/news/1m-context), which really is a lot! Context is also important for refusal protection: if there's not enough context, sometimes the model refuses to answer. Giving clear background and reassuring details helps avoid these unnecessary refusals, making the interaction smoother and more reliable. Of course, keep in mind that you are responsible the model's output: sometimes refusals are there for a reason.
- **Output format**: how you want the answer. If you want a list, markdown, a table, or a short paragraph, say so! You can (and should) be very detailed here. For example: "Return your answer as a JSON array of objects with keys 'aspect' and 'feedback'". Choose something that's easily parsable in Python or R later. Also remember the few-shot learning we talked about in Part 1: if you provide an example of what your output should look like, it's easier for the model to repeat that pattern.

Up to this point we've talked about adding role, task, context, and output format directly into "the" prompt. Like it's just one big thing. But there are actually two kinds of prompts you can use when chatting with a model: the system prompt and the user prompt.

- The **system prompt** is where you set the ground rules: it tells the model who it is, how it should behave, and what the answer should look like. Think of it as the "job description" that stays the same no matter what question you ask later. It's stable context.
- The **user prompt** is the specific request you make right now, like checking the clarity of a particular title. It can change every time. The model responds to this request within the "job description".

If you put everything into the user prompt, you end up repeating rules and formatting instructions over and over, which makes the conversation messy and can confuse the model (aka "context pollution"). By keeping the stable rules and output format in the system prompt, and putting specifics or content in the user prompt, you get clearer, more reliable answers. In both `chatlas` and `ellmer` you can use the `system_prompt` argument when initialising the `chat` object.

> **Why put the details in a system prompt?**
>
> Even though past messages are sent along in a conversation, putting the fixed details in the system prompt still makes a difference. The model pays more attention to instructions in the system prompt, so they're less likely to be ignored or overridden. It also keeps the chat history cleaner, since you don't need to repeat the same background and formatting rules in every user message. This way, the user prompt stays focused on just the part that changes (like a new title) while the system prompt handles the rest.

So what to do if you did all that and still get answers that are not up to your standards? In that case, you can try **Chain-of-Thought prompting**, where you ask the model to explain its reasoning step-by-step before answering. This makes complex tasks easier to follow and helps you understand how the model thinks. It's great for debugging to see where the model started to get off.

Now, with all that knowledge, let's change our prompt from:

``` markdown
I'm working on a presentation with the title: 'The Shiny Side of LLMs'. What's your feedback just based on that title?
```

To the following system prompt:

``` markdown
You are a presentation coach for data scientists. 
You give constructive, focused, and practical feedback on titles, structure, and storytelling. 

The presentation you are helping with is a 10-minute lightning talk at posit::conf(2025).  
The audience is Python and R users who are curious about AI and large language models, 
but not all of them have a deep technical background. 
The talk uses Shiny as a way to demo and explore LLMs in practice. 

Always return your feedback as a JSON array of objects, where each object has the following keys:
- 'aspect': one of 'clarity', 'tone', or 'relevance'
- 'feedback': a concise assessment
- 'suggestion': an optional improvement if applicable
```

And related user prompt for the task at hand:

``` markdown
Evaluate the title: 'The Shiny Side of LLMs'
```

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-6" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-6-1">Python</a></li>
<li><a href="#tabset-6-2">R</a></li>
</ul>
<div id="tabset-6-1">

``` python
from chatlas import ChatAnthropic

chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt="""
    You are a presentation coach for data scientists. 
    You give constructive, focused, and practical feedback on titles, structure, and storytelling. 

    The presentation you are helping with is a 10-minute lightning talk at posit::conf(2025).  
    The audience is Python and R users who are curious about AI and large language models, 
    but not all of them have a deep technical background. 
    The talk uses Shiny as a way to demo and explore LLMs in practice. 

    Always return your feedback as a JSON array of objects, where each object has the following keys:
    - 'aspect': one of 'clarity', 'tone', or 'relevance'
    - 'feedback': a concise assessment
    - 'suggestion': an optional improvement if applicable
    """,
)

chat.chat("Evaluate the title: 'The Shiny Side of LLMs'")
```

<details class="code-fold">
<summary>Show output</summary>

``` python
"""
  [                                                                                                                 
   {                                                                                                               
     "aspect": "clarity",                                                                                          
     "feedback": "The title uses a clever play on words with 'Shiny' but may create confusion about whether this i 
 primarily about the Shiny framework or LLMs. The wordplay might obscure the main focus for attendees scanning the 
 program.",                                                                                                        
     "suggestion": "Consider a title that more clearly positions Shiny as the tool and LLMs as the subject, such a 
 'Exploring LLMs with Shiny: Interactive AI Demos Made Simple'"                                                    
   },                                                                                                              
   {                                                                                                               
     "aspect": "tone",                                                                                             
     "feedback": "The playful tone with 'Shiny Side' is appropriate for a lightning talk and fits the Posit        
 conference atmosphere. It suggests an accessible, positive approach that aligns well with the audience's curiosit 
 about AI.",                                                                                                       
     "suggestion": null                                                                                            
   },                                                                                                              
   {                                                                                                               
     "aspect": "relevance",                                                                                        
     "feedback": "Highly relevant for the audience - Python/R users at Posit::conf would immediately recognize     
 'Shiny' and appreciate learning how to apply it to trending AI/LLM topics. The focus on practical demos matches   
 what this audience values.",                                                                                      
     "suggestion": "Consider adding a subtitle to reinforce the practical angle: 'The Shiny Side of LLMs: Building 
 Interactive AI Demos'"                                                                                            
   }                                                                                                               
 ]
 """
```

</details>
</div>
<div id="tabset-6-2">

``` r
library(ellmer)

chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = "
  You are a presentation coach for data scientists. 
  You give constructive, focused, and practical feedback on titles, structure, and storytelling. 

  The presentation you are helping with is a 10-minute lightning talk at posit::conf(2025).  
  The audience is Python and R users who are curious about AI and large language models, 
  but not all of them have a deep technical background. 
  The talk uses Shiny as a way to demo and explore LLMs in practice. 

  Always return your feedback as a JSON array of objects, where each object has the following keys:
  - 'aspect': one of 'clarity', 'tone', or 'relevance'
  - 'feedback': a concise assessment
  - 'suggestion': an optional improvement if applicable
  "
)

chat$chat("Evaluate the title: 'The Shiny Side of LLMs'")
```

<details class="code-fold">
<summary>Show output</summary>

``` r
#> ```json
#> [
#>   {
#>     "aspect": "clarity",
#>     "feedback": "The title is somewhat ambiguous - 'shiny side' could refer to positive aspects of LLMs or literally to the Shiny framework. This wordplay might confuse audiences unfamiliar with both concepts.",
#>     "suggestion": "Consider 'Exploring LLMs with Shiny: Interactive AI Demos' or 'Building LLM Interfaces with Shiny' for clearer technical focus"
#>   },
#>   {
#>     "aspect": "tone",
#>     "feedback": "The playful wordplay fits well with the posit::conf audience and lightning talk format. It's approachable and not intimidating, which works for mixed technical backgrounds.",
#>     "suggestion": null
#>   },
#>   {
#>     "aspect": "relevance",
#>     "feedback": "Highly relevant for the audience - directly connects familiar Shiny technology with trending AI/LLM topics. Perfect for Python/R users wanting practical AI applications.",
#>     "suggestion": null
#>   }
#> ]
#> ```
```

</details>
</div>
</div>

That's already something we can programmatically work with. Note that there are still differences between runs and between Python and R (just take a look at both examples). That is expected, even though our prompt is exactly the same. We'll come back to that a bit later.

# Choosing the right input format

The goal of the DeckCheck app is to do more than just looking at a title: we want to analyse Quarto slides. That means we need to provide our presentation in the chat. The question is... How do we do that? The most straightforward choice to provide this kind of data to an LLM is markdown. Markdown is lightweight, readable, and has a nice structure. It captures headings, bullet points, code blocks, and text, which is perfect.

But markdown isn't the only option:

- **Plain text** is the most basic. It's simple, but you lose structure. Titles become regular text, as well as bullet points, code blocks etc. This makes it harder to analyse.
- **HTML** keeps all the structure but comes with a lot of noise (tags, attributes) that the LLM might happily read but we might not want to include.
- **Structured JSON chunks** give the most control, but is a big step from Quarto slides compared to plain markdown.

If we're starting from a Quarto `.qmd` or `.ipynb` file, we can:

- Directly render Quarto slides to markdown via `quarto render` with `-to markdown`
- We're not getting into the nitty gritty of [markdown vs Quarto](https://quarto.org/docs/authoring/markdown-basics.html), but Quarto is basically markdown with some fancy extras, which can cause noise for our goal. So we might want to strip slide metadata, speaker notes, and other extras with custom filters or scripts, depending on what we want to keep (and to be honest: how sophisticated we want it to be).

Let's say we have a very basic Quarto presentation that talks about "The Shiny Side of LLMs", loosely resembling what we've already talked about in this article, but is written in a sub-optimal way. The file is named ["my-presentation.qmd"](https://github.com/hypebright/the-shiny-side-of-llms/blob/8857ca5ae4f74a86105ce9d1f04df3354eeee866/Quarto/my-presentation.qmd) and lives in a Quarto folder in our working directory.

> **About the presentation file**
>
> It's not necessary to read this presentation line-by-line, it is just there for demo purposes and for reference if you want to make sense of the output that Claude is going to give later. In subsequent code we will simply refer to it as "my-presentation.qmd".

<details class="code-fold">
<summary>See full Quarto presentation</summary>

``` r
---
title: "The Shiny Side of LLMs"
author: "Veerle Eeftink - van Leemput"
format:
  revealjs: 
    theme: [default]
include-in-header: 
  text: |
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
highlight-style: "nord"
---

# Hey 👋

In this demo presentation we will explore how to use LLMs in Shiny applications. Because everybody is doing it, right? 😉

# What do you need?

- The means to authenticate. Depending on your provider, you might need an API key (e.g. Anthropic, OpenAI), a token (e.g. Hugging Face), or other authentication methods.
- Put those credentials in a suitable place (for R: `.Renviron`, for Python: `.env`)
- Install the necessary packages:
  - For Python: `chatlas`, `shiny`
  - For R: `ellmer`, `shiny`, `shinychat`, and optionally `bslib`
- An creative idea for your LLM-powered app!

# What are we building

We're building an app called DeckCheck: it's your favourite Presentation Rehearsal Buddy.

With DeckCheck, you can upload your Quarto presentation and get tailored feedback!

No more lengthy, boring presentations 🤠.

# Where to start?

1. Talk to an LLM with the help of `chatlas` (Python) and `ellmer` (R)
2. Get a basic `shiny` app ready
3. Integrate `chatlas`/`ellmer` in that `shiny` app using a simple chat interface
4. Build it out to an app where you can upload slides, see metrics about your presentation, and more.

# Talk to an LLM with chatlas

For Python, we can use `chatlas`:

\`\`\`python
from chatlas import ChatAnthropic

chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt="You are a presentation coach for data scientists. You give constructive, focused, and practical feedback on titles, structure, and storytelling.",
)

chat.chat("I'm working on a presentation with the title: 'The Shiny Side of LLMs'. What's your feedback just based on that title?")
\`\`\`

\# Talk to an LLM with ellmer

For R, we can use `ellmer`:

\`\`\`r
library(ellmer)

chat <- chat_anthropic(
    model = "claude-sonnet-4-20250514",
    system_prompt = "You are a presentation coach for data scientists. You give constructive, focused, and practical feedback on titles, structure, and storytelling."
)

chat$chat("I'm working on a presentation with the title: 'The Shiny Side of LLMs'. What's your feedback just based on that title?")
\`\`\`

\# Why Shiny?

-   Shiny is a web application framework for R and Python that allows you to build interactive web applications.
-   It provides a reactive programming model, making it easy to create dynamic user interfaces and handle user inputs.
-   Perfect for your LLM-powered app!

\# Shiny basics: Python

\`\`\`python
from shiny import App, ui, render

# Define UI
app_ui = ui.page_fluid(
    ui.h1("DeckCheck"),

    # Card with content
    ui.card(
        ui.card_header("Welcome"),

        ui.p("This is a basic Shiny for Python application."),

        # Input: text
        ui.input_text_area("text", "What's your question?"),

        # Output: echo text back
        ui.output_text("echo")
    )
)

# Define server
def server(input, output, session):
    @render.text
    def echo():
        return f"You asked: {input.text()}"

# Create app
app = App(app_ui, server)
\`\`\`

\# Shiny basics: R

Tip: combine with `bslib` for fancy looks!

\`\`\`r
library(shiny)
library(bslib)

ui <- page_fluid(
  theme = bs_theme(bootswatch = "minty"),

  # App title
  h1("DeckCheck"),

  # Create a card
  card(
    card_header("Welcome"),
    p("This is a simple Shiny app using bslib for layout and styling."),

    # Input: text
    textAreaInput("text", "What's your question?"),

    # Output: echo the text back
    textOutput("echo")
  )
)

server <- function(input, output, session) {
  # Reactive output
  output$echo <- renderText({
    paste("You asked:", input$text)
  })
}

shinyApp(ui, server)
\`\`\`

\# Where's the magic?

We're here for some AI magic, right? So let's talk to an LLM via our Shiny application!

![AI Magic](https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmZ0cmd1aGZzM3JqdW1zbng0czU2c2RwejNtM25jMW8xdnYzNXVrdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OlxeZT285uhFydNetO/giphy.gif)

\# Shiny and chatlas

We can add a chat component to our UI with `ui.chat_ui` from `shiny`, and use `ChatAnthropic` from `chatlas` to send our messages to Claude. With minimal change, our Shiny for Python app is already LLM-powered!

`\`\`python
from shiny import App, ui
from chatlas import ChatAnthropic

# Define UI
app_ui = ui.page_fluid(
    ui.h1("DeckCheck"),
    # Card with chat component
    ui.card(
        ui.card_header("Get started"),
        ui.p("Ask me anything about your presentation 💡"),
        # Chat component
        ui.chat_ui(id="my_chat"),
    ),
)

# Define server
def server(input, output, session):
    chat_component = ui.Chat(id="my_chat")

    chat = ChatAnthropic(
        model="claude-sonnet-4-20250514",
        system_prompt="You are a presentation coach for data scientists. You give constructive, focused, and practical feedback on titles, structure, and storytelling.",
    )

    @chat_component.on_user_submit
    async def handle_user_input(user_input: str):
        response = await chat.stream_async(user_input)
        await chat_component.append_message_stream(response)

# Create app
app = App(app_ui, server)
\`\`\`

\# Shiny, shinychat and ellmer We can add a chat component to our UI with `chat_mod_ui` from `shinychat`, and use `chat_anthropic` from `ellmer` to send our messages to Claude. With minimal change, our Shiny for R app is already LLM-powered!

\`\`\`r
library(shiny)
library(bslib)
library(ellmer)
library(shinychat)

ui <- page_fluid(
  theme = bs_theme(bootswatch = "minty"),

  # App title
  h1("DeckCheck"),

  # Create a card
  card(
    card_header("Get started"),
    p("Ask me anything about your presentation 💡"),

    # Chat component
    chat_mod_ui("chat_component")
  )
)

server <- function(input, output, session) {
  chat <- chat_anthropic(
    model = "claude-sonnet-4-20250514",
    system_prompt = "You are a presentation coach for data scientists. 
  You give constructive, focused, and practical feedback on titles, structure, and storytelling."
  )

  chat_mod_server("chat_component", chat)
}

shinyApp(ui, server)
\`\`\`

\# User experience

When using an LLM in a Shiny application, it is important to consider the user experience. The LLM should enhance the application, not overwhelm it. This means that the LLM's responses should be concise and relevant to the user's query. Additionally, it is crucial to handle errors gracefully, providing users with helpful feedback if the LLM cannot generate a response or if there are issues with the API. Therefore, implementing proper error handling and fallback mechanisms is essential.

\# Up next

Of course we're not ready yet. Next steps include:

-   Adding a file upload button
## Reading the content of the presentation
-   Crafting our prompt
-   Extract information in a structured way
-   Display that information in a visually appealing manner (value boxes, use of colours, icons, functionality to export the feedback...

\# Thank you!
```

</details>

This presentation would be suitable for a lightning talk (a maximum of 10 minutes), and for an audience that is not yet familiar with `shiny` and `chatlas`/`ellmer`.

To turn this `.qmd` file programmatically into markdown (`.md`) we would need to call quarto from our system. This can be done via the CLI or, in the case of R, via the [`quarto` package](https://quarto-dev.github.io/quarto-r/). Note that our simple presentation doesn't make much use of the fancy stuff you can do with Quarto, so our `.md` file will almost look exactly the same as our `.qmd` file. But keep in mind we're building for a wider audience!

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-7" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-7-1">Python</a></li>
<li><a href="#tabset-7-2">R</a></li>
</ul>
<div id="tabset-7-1">

We can run quarto from the CLI with `subprocess`:

``` python
import subprocess

subprocess.run(["quarto", "render", "my-presentation.qmd", "--to", "markdown"])
```

</div>
<div id="tabset-7-2">

Using the `quarto` package:

``` r
quarto::quarto_render("my-presentation.qmd", output_format = "markdown")
```

or as a sytem command:

``` r
system("quarto render my-presentation.qmd --to markdown")
```

</div>
</div>

Now our system prompt can look something like this:

``` markdown
You are a presentation coach for data scientists that analyses presentation slide decks written in Markdown. 
You extract key information, evaluate quality, and return structured feedback that is constructive, focused and practical.

The presentation you are helping with is a 10-minute lightning talk at posit::conf(2025).  
The audience is Python and R users who are curious about AI and large language models, 
but not all of them have a deep technical background. 
The talk uses Shiny as a way to demo and explore LLMs in practice. 

You extract the following information:

...

You score the presentation on the following categories (from 1–10), and give a concise explanation:

...

Always return your answer as a JSON object with the following structure:

...
```

<details class="code-fold">
<summary>Show full prompt</summary>

``` python
"""
You are a presentation coach for data scientists that analyses presentation slide decks written in Markdown. 
You extract key information, evaluate quality, and return structured feedback that is constructive, focused and practical.

The presentation you are helping with is a 10-minute lightning talk at posit::conf(2025).  
The audience is Python and R users who are curious about AI and large language models, 
but not all of them have a deep technical background. 
The talk uses Shiny as a way to demo and explore LLMs in practice. 

You extract the following information:

1. The presentation title
2. Total number of slides
3. Percentage of slides containing code blocks
4. Percentage of slides containing images
5. Estimated presentation length (in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide)
6. Tone (a brief description)

You score the presentation on the following categories (from 1–10), and give a concise explanation:

1. Clarity of content: evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?
2. Relevance for intended audience: assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?
3. Visual design: judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?
4. Engagement: estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?
5. Pacing: analyze the distribution of content across slides. Are some slides too dense or too light? 
6. Structure: review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?
7. consistency: evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?
8. Accessibility: consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?

Always return your answer as a JSON object with the following structure:

{
  "presentation_title": "",
  "total_slides": 0,
  "percent_with_code": 0,
  "percent_with_images": 0,
  "estimated_duration_minutes": 0,
  "tone": "",
  "clarity": {
    "score": 0,
    "justification": ""
  },
  "relevance": {
    "score": 0,
    "justification": ""
  },
  "visual_design": {
    "score": 0,
    "justification": ""
  },
  "engagement": {
    "score": 0,
    "justification": ""
  },
  "pacing": {
    "score": 0,
    "justification": ""
  },
  "structure": {
    "score": 0,
    "justification": ""
  },
  "concistency": {
    "score": 0,
    "justification": ""
  },
  "accessibility": {
    "score": 0,
    "justification": ""
  }
}
"""
```

</details>

And our user prompt:

``` markdown
Here are the slides in Markdown: ...
```

# Storing prompts and dynamic data

As you know by know, you need to provide very specific instructions in your prompt if you're looking for good outcomes. And the more you specify, the lengthier your prompt becomes. Eventually this is going to be very annoying to put in your code directly. Therefore, it's a good idea to store your prompt somewhere. We determined markdown is the way to go for inputting slide content, but the same motivation applies to our prompt. Besides that, markdown allows us to structure our prompt more clearly too: headers, bullet points, numbered lists... That's nice for the LLM and for you!

The recommended file naming convention is to use `prompt.md` if you only have one prompt, and use informative names like `prompt-analyse-slides.md` if you have multiple. For clarity, we'll go with the latter even though we only have one prompt (so far).

Since your prompt(s) are very important for the outcome of your LLM-powered app, it's also a good idea to track these files using git. You don't want to lose that precious carefully prompt that worked so well before you decided to change the whole thing.

Prompt(s) don't have to be static: they can be dynamic too. We want our app to improve Quarto presentations world-wide: many users, many Quarto slides, many audiences and presentation lengths. Our prompt needs to be able to work with this dynamic data, so our prompt needs to change depending on those variables. Luckily, we can use the `interpolate_file()` or `interpolate()` function, which, as the names suggest, can interpolate variables into a prompt template stored in a file, or in a simple string. To do so, we use the `{ x }` syntax, making our `prompt-analyse-slides.md` file look like this:

``` markdown
...

The presentation you are helping with is a {{ length }}-minute {{ type }} at {{ event }}.  
The audience is {{ audience }}. 

...
```

<details class="code-fold">
<summary>Show full prompt</summary>

``` python
"""
You are a presentation coach for data scientists that analyses presentation slide decks written in Markdown. 
You extract key information, evaluate quality, and return structured feedback that is constructive, focused and practical.

The presentation you are helping with is a {{ length }}-minute {{ type }} at {{ event }}.  
The audience is {{ audience }}. 

You extract the following information:

1. The presentation title
2. Total number of slides
3. Percentage of slides containing code blocks
4. Percentage of slides containing images
5. Estimated presentation length (in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide)
6. Tone (a brief description)

You score the presentation on the following categories (from 1–10), and give a concise explanation:

1. Clarity of content: evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?
2. Relevance for intended audience: assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?
3. Visual design: judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?
4. Engagement: estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?
5. Pacing: analyze the distribution of content across slides. Are some slides too dense or too light? 
6. Structure: review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?
7. consistency: evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?
8. Accessibility: consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?

Always return your answer as a JSON object with the following structure:

{
  "presentation_title": "",
  "total_slides": 0,
  "percent_with_code": 0,
  "percent_with_images": 0,
  "estimated_duration_minutes": 0,
  "tone": "",
  "clarity": {
    "score": 0,
    "justification": ""
  },
  "relevance": {
    "score": 0,
    "justification": ""
  },
  "visual_design": {
    "score": 0,
    "justification": ""
  },
  "engagement": {
    "score": 0,
    "justification": ""
  },
  "pacing": {
    "score": 0,
    "justification": ""
  },
  "structure": {
    "score": 0,
    "justification": ""
  },
  "concistency": {
    "score": 0,
    "justification": ""
  },
  "accessibility": {
    "score": 0,
    "justification": ""
  }
}
"""
```

</details>

Our user prompt is going directly into the `chat` method and will be:

``` markdown
Here are the slides in Markdown: {{ markdown }}
```

Note: if your user prompt is long you might want to put this in a separate prompt file as well.

> **Note**
>
> You might wonder why we don't we put the Markdown content in our system prompt. The reason is that we don't want to overload our system prompt with big chunks of data like our Markdown slides. As mentioned previously, the system prompt sets the role, the rules, and provides task instructions. It is stable context. The Markdown slides are the actual content to analyse, and they change from one run to the other. This fits better in a user prompt. It's also good practice to keep the system prompt clean so it is reusable across runs.

Those are prompts we can work with! So let's chat away:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-8" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-8-1">Python</a></li>
<li><a href="#tabset-8-2">R</a></li>
</ul>
<div id="tabset-8-1">

``` python
from chatlas import ChatAnthropic, interpolate_file, interpolate
import subprocess
from pathlib import Path

# Get Quarto presentation and convert to plain Markdown
subprocess.run(
    ["quarto", "render", "./Quarto/my-presentation.qmd", "--to", "markdown"]
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content = "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content = "10"
type_content = "lightning talk"
event_content = "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file = Path("./Quarto/docs/my-presentation.md")
markdown_content = markdown_file.read_text(encoding="utf-8")

# Define prompt file
system_prompt_file = Path("./prompts/prompt-analyse-slides.md")

# Create system prompt
system_prompt = interpolate_file(
    system_prompt_file,
    variables={
        "audience": audience_content,
        "length": length_content,
        "type": type_content,
        "event": event_content,
    },
)

# Initialise chat with Claude Sonnet 4 model
chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt=system_prompt,
)
# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat.chat(interpolate("Here are the slides in Markdown: {{ markdown_content }}"))
```

<details class="code-fold">
<summary>Show output</summary>

``` python
"""
  {                                                                                  
   "presentation_title": "The Shiny Side of LLMs",                                  
   "total_slides": 16,                                                              
   "percent_with_code": 44,                                                         
   "percent_with_images": 6,                                                        
   "estimated_duration_minutes": 22,                                                
   "tone": "Casual, enthusiastic, and approachable with emojis and informal languag 
 aimed at making technical concepts accessible",                                    
   "clarity": {                                                                     
     "score": 7,                                                                    
     "justification": "Content is generally clear with good step-by-step progressio 
 but some technical concepts could benefit from more explanation for non-technical  
 audience members. Code examples are well-structured but may be overwhelming for    
 beginners."                                                                        
   },                                                                               
   "relevance": {                                                                   
     "score": 8,                                                                    
     "justification": "Well-targeted for the audience - provides both Python and R  
 examples, acknowledges varying technical backgrounds, and focuses on practical     
 implementation rather than deep theory. The DeckCheck example is relatable to the  
 conference audience."                                                              
   },                                                                               
   "visual_design": {                                                               
     "score": 5,                                                                    
     "justification": "Heavy reliance on text and code blocks with minimal visual   
 elements. Only one image (GIF) used. Code blocks dominate several slides, making   
 them potentially overwhelming. Layout appears basic without clear visual hierarchy 
   },                                                                               
   "engagement": {                                                                  
     "score": 6,                                                                    
     "justification": "Uses emojis and casual language to maintain interest, includ 
 a relatable example (DeckCheck), and has one engaging GIF. However, lacks          
 interactive elements beyond code examples and could benefit from more storytelling 
 elements."                                                                         
   },                                                                               
   "pacing": {                                                                      
     "score": 4,                                                                    
     "justification": "Uneven pacing with several code-heavy slides that would      
 require significant time to explain, while some slides have minimal content. The   
 estimated 22-minute duration exceeds the 10-minute lightning talk format           
 considerably."                                                                     
   },                                                                               
   "structure": {                                                                   
     "score": 8,                                                                    
     "justification": "Clear logical progression from introduction to requirements, 
 basic concepts, implementation examples, and next steps. Good parallel structure   
 showing both Python and R approaches. Solid beginning, middle, and end."           
   },                                                                               
   "concistency": {                                                                 
     "score": 7,                                                                    
     "justification": "Maintains consistent casual tone and formatting throughout.  
 Code examples follow similar patterns for both languages. Some inconsistency in    
 slide density and the single image feels somewhat disconnected from the overall    
 style."                                                                            
   },                                                                               
   "accessibility": {                                                               
     "score": 6,                                                                    
     "justification": "Code blocks may be challenging for those with visual         
 impairments due to syntax highlighting and smaller fonts. The casual tone and emoj 
 help with cognitive accessibility, but the technical density could be overwhelming 
 for some audience members."                                                        
   }                                                                                
 }
"""
```

</details>
</div>
<div id="tabset-8-2">

``` r
library(ellmer)

# Get Quarto presentation and convert to plain Markdown
quarto::quarto_render(
  "./Quarto/my-presentation.qmd",
  output_format = "markdown"
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content <- "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content <- "10"
type_content <- "lightning talk"
event_content <- "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file <- "./Quarto/docs/my-presentation.md"
markdown_content <- readChar(markdown_file, file.size(markdown_file))

# Define prompt file
system_prompt_file <- "./prompts/prompt-analyse-slides.md"

# Create system prompt
system_prompt <- interpolate_file(
  path = system_prompt_file,
  audience = audience_content,
  length = length_content,
  type = type_content,
  event = event_content
)

# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt,
  params = params(
    temperature = 0.8 # default is 1
  )
)

# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat$chat(interpolate(
  "Here are the slides in Markdown: {{ markdown_content }}"
))
```

<details class="code-fold">
<summary>Show output</summary>

``` r
#> {
#>   "presentation_title": "The Shiny Side of LLMs",
#>   "total_slides": 16,
#>   "percent_with_code": 37.5,
#>   "percent_with_images": 6.25,
#>   "estimated_duration_minutes": 14,
#>   "tone": "Casual, friendly, and enthusiastic with emoji use and conversational 
#> language that makes technical content approachable",
#>   "clarity": {
#>     "score": 7,
#>     "justification": "Content is generally clear with good progression from basics 
#> to implementation. However, some technical details could benefit from more 
#> explanation, and the system prompts in code examples could be better integrated 
#> into the narrative."
#>   },
#>   "relevance": {
#>     "score": 8,
#>     "justification": "Excellent match for the audience - shows practical 
#> integration of LLMs with familiar tools (Shiny), provides both Python and R 
#> examples, and focuses on a relatable use case (presentation feedback) that 
#> resonates with the posit::conf audience."
#>   },
#>   "visual_design": {
#>     "score": 6,
#>     "justification": "Basic markdown structure is clean but lacks visual hierarchy 
#> and design elements. Code blocks are well-formatted, but slides could benefit from 
#> more visual breaks, bullet points, and consistent formatting. The single GIF adds 
#> some visual interest."
#>   },
#>   "engagement": {
#>     "score": 7,
#>     "justification": "Good use of humor, emojis, and relatable scenarios (boring 
#> presentations). The progression from simple to complex keeps interest, and the 
#> practical demo concept is engaging. Could benefit from more interactive elements or
#> storytelling."
#>   },
#>   "pacing": {
#>     "score": 6,
#>     "justification": "Some slides are too dense (UX slide, code-heavy slides) while
#> others are very light (Thank you slide). The progression is logical but could be 
#> more evenly distributed. Code slides may take longer than estimated."
#>   },
#>   "structure": {
#>     "score": 8,
#>     "justification": "Clear logical flow from introduction to requirements, basic 
#> concepts, implementation, and next steps. Good parallel structure showing both 
#> Python and R implementations. Strong opening and clear progression toward building 
#> the demo app."
#>   },
#>   "concistency": {
#>     "score": 7,
#>     "justification": "Generally consistent tone and approach throughout. Code 
#> formatting is consistent between languages. However, some slides vary significantly
#> in content density, and the casual tone occasionally conflicts with more technical 
#> sections."
#>   },
#>   "accessibility": {
#>     "score": 5,
#>     "justification": "Basic markdown structure is accessible, but lacks 
#> considerations for screen readers (no alt text for the GIF), may have contrast 
#> issues depending on theme, and code blocks could be challenging for some users. 
#> Font sizes and spacing depend on presentation software."
#>   }
#> }
```

</details>
</div>
</div>

> **Inconsistencies in the output**
>
> Did you already notice that some meta-data, like the percentage of slides with code and/or images is inconsistent? For example, the "percent_with_code" is 40, but other times it's 37.5 or 45. It seems like a broken calculator! To understand why this happens you can read [part 1](../../../blog/shiny/shiny-side-of-llms-part-1/) again, where we talk about why LLMs are really good at some tasks, and others, well... Not so much. That doesn't mean it's completely out of our hands. We can help the LLM with a "tool". Keep on reading to learn more about that concept.

It's not too bad for a first try and it serves as a basis we can depart from. We can go back and forth many times, aka do some "prompt engineering", to make sure we are getting results that are usable. The prompt that we used mostly returns a broad analysis (makes sense, we asked it to), but if we want our users to take action we need to provide specific improvements. So we could extend our prompt with "provide specific and actionable improvements" and provide specific instructions like "keep each suggestion concise and mention the slide number(s) if applicable":

``` markdown
...

You score the presentation on the following categories (from 1–10), and give a concise explanation:

...

For each of the above scoring categories, provide specific and actionable improvements. Follow these instructions:

- Keep each suggestion concise and mention the slide number(s) if applicable.
- Do not invent issues and only suggest improvements when the content would clearly benefit from them.
- For each catogory, estimate what the new score would be if these improvements are implemented.
- Return the improvement and new score as part of the response for that category.

...
```

<details class="code-fold">
<summary>Show full prompt</summary>

``` python
"""
You are a presentation coach for data scientists that analyses presentation slide decks written in Markdown. 
You extract key information, evaluate quality, and return structured feedback that is constructive, focused and practical.

The presentation you are helping with is a {{ length }}-minute {{ type }} at {{ event }}.  
The audience is {{ audience }}. 

You extract the following information:

1. The presentation title
2. Total number of slides
3. Percentage of slides containing code blocks
4. Percentage of slides containing images
5. Estimated presentation length (in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide)
6. Tone (a brief description)

You score the presentation on the following categories (from 1–10), and give a concise explanation:

1. Clarity of content: evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?
2. Relevance for intended audience: assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?
3. Visual design: judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?
4. Engagement: estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?
5. Pacing: analyze the distribution of content across slides. Are some slides too dense or too light? 
6. Structure: review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?
7. consistency: evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?
8. Accessibility: consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?

For each of the above scoring categories, provide specific and actionable improvements. Follow these instructions:

- Keep each suggestion concise and mention the slide number(s) if applicable.
- Do not invent issues and only suggest improvements when the content would clearly benefit from them.
- For each catogory, estimate what the new score would be if these improvements are implemented.
- Return the improvement and new score as part of the response for that category.

Always return your answer as a JSON object with the following structure:

{
  "presentation_title": "",
  "total_slides": 0,
  "percent_with_code": 0,
  "percent_with_images": 0,
  "estimated_duration_minutes": 0,
  "tone": "",
  "clarity": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  },
  "relevance": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  },
  "visual_design": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  },
  "engagement": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  },
  "pacing": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  },
  "structure": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  },
  "consistency": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  },
  "accessibility": {
    "score": 0,
    "justification": "",
    "improvements": "",
    "score_after_improvements": 0
  }
"""
```

</details>
<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-9" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-9-1">Python</a></li>
<li><a href="#tabset-9-2">R</a></li>
</ul>
<div id="tabset-9-1">

``` python
# Define prompt file
system_prompt_file = Path("./prompts/prompt-analyse-slides-with-improvements.md")

# Create system prompt
system_prompt = interpolate_file(
    system_prompt_file,
    variables={
        "audience": audience_content,
        "length": length_content,
        "type": type_content,
        "event": event_content,
    },
)

# Initialise chat with Claude Sonnet 4 model
chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt=system_prompt,
)

# Start conversation with the chat
chat.chat(interpolate("Here are the slides in Markdown: {{ markdown_content }}"))
```

<details class="code-fold">
<summary>Show complete code</summary>

``` python
from chatlas import ChatAnthropic, interpolate_file, interpolate
import subprocess
from pathlib import Path

# Get Quarto presentation and convert to plain Markdown
subprocess.run(
    ["quarto", "render", "./Quarto/my-presentation.qmd", "--to", "markdown"]
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content = "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content = "10"
type_content = "lightning talk"
event_content = "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file = Path("./Quarto/docs/my-presentation.md")
markdown_content = markdown_file.read_text(encoding="utf-8")

# Define prompt file
system_prompt_file = Path("./prompts/prompt-analyse-slides-with-improvements.md")

# Create system prompt
system_prompt = interpolate_file(
    system_prompt_file,
    variables={
        "audience": audience_content,
        "length": length_content,
        "type": type_content,
        "event": event_content,
    },
)

# Initialise chat with Claude Sonnet 4 model
chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt=system_prompt,
)

# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat.chat(interpolate("Here are the slides in Markdown: {{ markdown_content }}"))
```

</details>
<details class="code-fold">
<summary>Show output</summary>

``` python
"""
  {                                                                                                  
   "presentation_title": "The Shiny Side of LLMs",                                                  
   "total_slides": 16,                                                                              
   "percent_with_code": 43.75,                                                                      
   "percent_with_images": 6.25,                                                                     
   "estimated_duration_minutes": 23,                                                                
   "tone": "Casual, enthusiastic, and developer-friendly with emojis and informal language",        
   "clarity": {                                                                                     
     "score": 7,                                                                                    
     "justification": "Content is generally clear with good explanations of technical concepts, but 
 some slides lack necessary context or detail for the intended audience",                           
     "improvements": "Define 'chatlas' and 'ellmer' when first introduced (slides 5-6). Add brief   
 explanation of what 'system_prompt' does. Explain what 'reactive programming model' means in       
 practical terms (slide 7).",                                                                       
     "score_after_improvements": 8                                                                  
   },                                                                                               
   "relevance": {                                                                                   
     "score": 8,                                                                                    
     "justification": "Very relevant for Python and R users interested in AI/LLMs. Code examples ar 
 appropriate and the practical focus matches audience needs",                                       
     "improvements": "Add a brief comparison of when to choose Python vs R approach (slide 4).      
 Include mention of cost considerations for API usage in slide 2.",                                 
     "score_after_improvements": 9                                                                  
   },                                                                                               
   "visual_design": {                                                                               
     "score": 5,                                                                                    
     "justification": "Heavy text density on many slides, particularly slides with code blocks.     
 Limited visual elements beyond one GIF",                                                           
     "improvements": "Break up text-heavy slides (2, 14) into bullet points or multiple slides. Add 
 diagrams showing app architecture (slides 4, 7). Use consistent formatting for code blocks and     
 ensure proper syntax highlighting.",                                                               
     "score_after_improvements": 7                                                                  
   },                                                                                               
   "engagement": {                                                                                  
     "score": 6,                                                                                    
     "justification": "Casual tone and emojis add personality, and the practical demo concept is    
 engaging, but lacks interactive elements or storytelling",                                         
     "improvements": "Add a brief demo video or screenshots of the final app. Include a 'What you'l 
 learn today' slide early on. Add audience poll question about their LLM experience (slide 2).",    
     "score_after_improvements": 8                                                                  
   },                                                                                               
   "pacing": {                                                                                      
     "score": 4,                                                                                    
     "justification": "Presentation is too long for 10-minute slot (estimated 23 minutes) with unev 
 distribution - some slides very dense, others very light",                                         
     "improvements": "Combine slides 5-6 into one comparison slide. Merge slides 8-9 into single    
 Python/R comparison. Remove or significantly shorten slide 14. Condense setup requirements (slide  
 2).",                                                                                              
     "score_after_improvements": 7                                                                  
   },                                                                                               
   "structure": {                                                                                   
     "score": 7,                                                                                    
     "justification": "Good logical flow from introduction to implementation, but missing clear     
 conclusion and call-to-action",                                                                    
     "improvements": "Add agenda/outline slide after slide 1. Include key takeaways and resources   
 slide before 'Thank you'. Make slide 15 more specific about next steps.",                          
     "score_after_improvements": 8                                                                  
   },                                                                                               
   "consistency": {                                                                                 
     "score": 8,                                                                                    
     "justification": "Generally consistent tone and formatting throughout, with good parallel      
 structure between Python and R examples",                                                          
     "improvements": "Ensure consistent code block formatting and indentation. Standardize bullet   
 point styles across all slides.",                                                                  
     "score_after_improvements": 9                                                                  
   },                                                                                               
   "accessibility": {                                                                               
     "score": 6,                                                                                    
     "justification": "Code examples may have small font sizes, and some slides are text-heavy whic 
 could be challenging for some viewers",                                                            
     "improvements": "Ensure code font size is at least 14pt. Add alt text description for the GIF  
 (slide 11). Break up dense paragraphs with more white space and bullet points.",                   
     "score_after_improvements": 8                                                                  
   }                                                                                                
 }
""" 
```

</details>
</div>
<div id="tabset-9-2">

``` r
# Define prompt file
system_prompt_file <- "./prompts/prompt-analyse-slides-with-improvements.md"

# Create system prompt
system_prompt <- interpolate_file(
  path = system_prompt_file,
  audience = audience_content,
  length = length_content,
  type = type_content,
  event = event_content
)

# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt
)

# Start conversation with the chat
chat$chat(interpolate(
  "Here are the slides in Markdown: {{ markdown_content }}"
))
```

<details class="code-fold">
<summary>Show complete code</summary>

``` r
library(ellmer)

# Get Quarto presentation and convert to plain Markdown
quarto::quarto_render(
  "./Quarto/my-presentation.qmd",
  output_format = "markdown"
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content <- "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content <- "10"
type_content <- "lightning talk"
event_content <- "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file <- "./Quarto/docs/my-presentation.md"
markdown_content <- readChar(markdown_file, file.size(markdown_file))

# Define prompt file
system_prompt_file <- "./prompts/prompt-analyse-slides-with-improvements.md"

# Create system prompt
system_prompt <- interpolate_file(
  path = system_prompt_file,
  audience = audience_content,
  length = length_content,
  type = type_content,
  event = event_content
)

# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt
)

# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat$chat(interpolate(
  "Here are the slides in Markdown: {{ markdown_content }}"
))
```

</details>
<details class="code-fold">
<summary>Show output</summary>

``` r
#> {
#>   "presentation_title": "The Shiny Side of LLMs",
#>   "total_slides": 16,
#>   "percent_with_code": 37.5,
#>   "percent_with_images": 6.25,
#>   "estimated_duration_minutes": 14,
#>   "tone": "Casual, friendly, and practical with a playful touch (emojis, informal 
#> language, and humor)",
#>   "clarity": {
#>     "score": 7,
#>     "justification": "Content is generally clear with good code examples and 
#> explanations. However, some technical terms could use more definition for the 
#> mixed-technical audience.",
#>     "improvements": "Define key terms like 'reactive programming' (slide 7), 
#> explain what API keys/tokens are (slide 2), and clarify what 'system_prompt' does 
#> in the code examples (slides 5-6).",
#>     "score_after_improvements": 8
#>   },
#>   "relevance": {
#>     "score": 8,
#>     "justification": "Excellent match for the audience - Python and R users curious
#> about AI/LLMs. Provides practical, hands-on examples in both languages and focuses 
#> on implementation rather than deep theory.",
#>     "improvements": "Add a brief slide explaining what LLMs are and their basic 
#> capabilities for audience members completely new to AI (slide 3 area).",
#>     "score_after_improvements": 9
#>   },
#>   "visual_design": {
#>     "score": 5,
#>     "justification": "Heavy reliance on text and code blocks. Most slides are 
#> text-dense with minimal visual elements. Only one image used, and code blocks 
#> dominate several slides.",
#>     "improvements": "Add visual diagrams showing the Shiny-LLM integration flow 
#> (slide 4), include screenshots of the final app (slide 3), reduce text density on 
#> slides 13 and 15, and add icons or visual elements to break up text-heavy slides.",
#>     "score_after_improvements": 7
#>   },
#>   "engagement": {
#>     "score": 6,
#>     "justification": "Casual tone with emojis and humor helps engagement, but heavy
#> code blocks and text-dense slides could lose audience attention. The practical 
#> 'build along' approach is engaging.",
#>     "improvements": "Add interactive moments like 'raise your hand if you've used 
#> Shiny before' (slide 7), include a live demo or video clip of the app in action 
#> (slide 11), and break up slide 13 with bullet points or visual elements.",
#>     "score_after_improvements": 8
#>   },
#>   "pacing": {
#>     "score": 6,
#>     "justification": "Some slides are too dense (slides 8, 9, 11, 12, 13) while 
#> others are very light (slides 1, 16). The code-heavy slides will take longer to 
#> present than estimated.",
#>     "improvements": "Split slide 11 into two slides (one for Python UI, one for 
#> server), break slide 13 into key points with visuals, and add more content to the 
#> thank you slide (slide 16) with contact info or resources.",
#>     "score_after_improvements": 8
#>   },
#>   "structure": {
#>     "score": 8,
#>     "justification": "Clear logical flow from introduction to requirements to 
#> implementation to next steps. Good progression from basic concepts to integration. 
#> Clear beginning, middle, and end.",
#>     "improvements": "Add a brief agenda slide after slide 1 to preview the journey,
#> and include a 'key takeaways' slide before the thank you slide.",
#>     "score_after_improvements": 9
#>   },
#>   "concistency": {
#>     "score": 7,
#>     "justification": "Generally consistent tone and formatting. Code blocks are 
#> well-formatted. Some inconsistency in slide density and the mix of casual/technical
#> language.",
#>     "improvements": "Standardize slide titles (some are questions, some 
#> statements), ensure consistent bullet point formatting across slides, and maintain 
#> consistent emoji usage throughout.",
#>     "score_after_improvements": 8
#>   },
#>   "accessibility": {
#>     "score": 6,
#>     "justification": "Code blocks may be challenging to read for some viewers. 
#> Heavy text density on several slides could be overwhelming. No obvious color 
#> contrast issues mentioned.",
#>     "improvements": "Increase font size in code blocks (slides 5-6, 8-9, 11-12), 
#> add alt text descriptions for the GIF image (slide 10), reduce text density on 
#> slide 13, and ensure sufficient white space between elements.",
#>     "score_after_improvements": 8
#>   }
#> }
```

</details>
</div>
</div>

And of course Claude believes that all the suggested improvements increase the relevant scores. However, don't be surprised if the numbers are off. Remember from [part 1](../../../blog/shiny/shiny-side-of-llms-part-1/) that it's just a model that predicts a next token. It's good to do some sanity checks.

# Ensuring structured and consistent output

As mentioned previously, specifying an output format makes your outcomes better. That's why we included: *"Please extract the following information... Return your answer as a JSON object with the following structure..."* in our prompt. Formats like JSON, YAML, and Markdown tables are common, and JSON tends to be a safe bet for both Python and R. It's clean, structured, and easy to parse.

And even though we're explicitly guiding the model toward structured JSON output, we don't always get what we expect: the model might wrap its output in a code block (e.g., \`\`\`json), or forget a comma, or produce something that looks like JSON but isn't quite valid. That's weird, right? It's because specifying the format in the prompt is essentially giving the model strong instructions in plain language. You're still relying on the model to follow your instructions correctly and generate the output in that format. This works reasonably well, but it's still a natural language generation task under the hood. And as we learned in part I: it's all just predicting one token after the other. If the probability of a space instead of a comma is higher... Well, goodbye parsable JSON.

So we need something smarter. That's where something called "structured output" comes in. Structured output refers to LLMs that support structured schemas as part of the API or function call and not just as instructions in the prompt. These tell the model not just what to output, but how to constrain the generation itself. The model generates a structure directly (like a JSON object or typed dictionary), and the output is guaranteed to match that structure.

The difference is:

- Prompting: "Please follow this format" (model might comply)
- Structured output: "You must generate output that fits this exact shape" (enforced)

With `chatlas` and `ellmer` we can make use of this structured data feature. Bonus: `chatlas` will convert the response into a structured Python dictionary, and `ellmer` into an R data structure so it's immediately ready to use!

To return structured data we need to change two things: call `chat_structured()` and provide a specification. In this specification we can specify the fields, their type, and add a description for each of them. Optionally, to prevent duplication, we can remove the field descriptions from our prompt, and refer to the "data model" instead:

``` markdown
...

Always return the result as a JSON object that conforms to the provided data model.
```

<details class="code-fold">
<summary>Show full prompt</summary>

``` python
"""
You are a presentation coach for data scientists that analyses presentation slide decks written in Markdown. 
You extract key information, evaluate quality, and return structured feedback that is constructive, focused and practical.

The presentation you are helping with is a {{ length }}-minute {{ type }} at {{ event }}.  
The audience is {{ audience }}. 

You extract the following information:

1. The presentation title
2. Total number of slides
3. Percentage of slides containing code blocks
4. Percentage of slides containing images
5. Estimated presentation length (in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide)
6. Tone (a brief description)

You score the presentation on the following categories (from 1–10), and give a concise explanation:

1. Clarity of content: evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?
2. Relevance for intended audience: assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?
3. Visual design: judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?
4. Engagement: estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?
5. Pacing: analyze the distribution of content across slides. Are some slides too dense or too light? 
6. Structure: review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?
7. consistency: evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?
8. Accessibility: consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?

For each of the above scoring categories, provide specific and actionable improvements. Follow these instructions:

- Keep each suggestion concise and mention the slide number(s) if applicable.
- Do not invent issues and only suggest improvements when the content would clearly benefit from them.
- For each catogory, estimate what the new score would be if these improvements are implemented.
- Return the improvement and new score as part of the response for that category.

Always return the result as a JSON object that conforms to the provided data model.
"""
```

</details>

> **Double work or Don't Repeat Yourself (DRY)?**
>
> This approach assumes the model actually has access to the data model definition, either via a tool, API schema, or injected example. Without that, results may be inconsistent. It seems that Claude's results are quite good this way, but it may vary for other models, so it's good to try different things.
>
> For educational purposes it's nice to see that the LLM is getting the required information from the provided data model, and not from the system prompt.
>
> Having both the description in the prompt and in a data model is an option to, especially when:
>
> - You want strong guidance and fallback validation.
> - You're building for reliability or multi-model use (not all models treat schemas equally).
> - You're iterating and want to troubleshoot what part is helping.

We'll come back to why the Don't-Repeat-Yourself (DRY) principle might be worthwhile for the token count and cost too.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-10" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-10-1">Python</a></li>
<li><a href="#tabset-10-2">R</a></li>
</ul>
<div id="tabset-10-1">

To use structured output, you give the model some input and a [Pydantic model](https://docs.pydantic.dev/latest/concepts/models/) that describes the kind of data you want. The Pydantic model is like a form with specific fields and types, like `title: string` or `duration: integer`.

``` python
# Define data structure to extract from the input
ScoreType = Annotated[int, Field(ge=0, le=10)]
PercentType = Annotated[float, Field(ge=0.0, le=100.0)]
MinutesType = Annotated[int, Field(ge=0)]
SlideCount = Annotated[int, Field(ge=0)]

class ScoringCategory(BaseModel):
    score: ScoreType = Field(..., description="Score from 1–10.")
    justification: str = Field(..., description="Brief explanation of the score.")
    improvements: Optional[str] = Field(
        None,
        description="Concise, actionable improvements, mentioning slide numbers if applicable.",
    )
    score_after_improvements: ScoreType = Field(
        ..., description="Estimated score after suggested improvements."
    )

class DeckAnalysis(BaseModel):
    presentation_title: str = Field(..., description="The presentation title.")
    total_slides: SlideCount
    percent_with_code: PercentType
    percent_with_images: PercentType
    estimated_duration_minutes: MinutesType
    tone: str = Field(
        ..., description="Brief description of the tone of the presentation."
    )

    clarity: ScoringCategory = Field(
        ...,
        description="Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    )
    relevance: ScoringCategory = Field(
        ...,
        description="Assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    )
    visual_design: ScoringCategory = Field(
        ...,
        description="Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    )
    engagement: ScoringCategory = Field(
        ...,
        description="Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    )
    pacing: ScoringCategory = Field(
        ...,
        description="Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    )
    structure: ScoringCategory = Field(
        ...,
        description="Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    )
    concistency: ScoringCategory = Field(  # spelling kept as-is
        ...,
        description="Evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    )
    accessibility: ScoringCategory = Field(
        ...,
        description="Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    )

# Initialise chat with Claude Sonnet 4 model
chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt=system_prompt,
)

# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat.chat_structured(
    interpolate("Here are the slides in Markdown: {{ markdown_content }}"),
    data_model=DeckAnalysis,
)
```

<details class="code-fold">
<summary>Show complete code</summary>

``` python
from chatlas import ChatAnthropic, interpolate_file, interpolate
import subprocess
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Annotated, Optional

# Get Quarto presentation and convert to plain Markdown
subprocess.run(
    ["quarto", "render", "./Quarto/my-presentation.qmd", "--to", "markdown"]
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content = "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content = "10"
type_content = "lightning talk"
event_content = "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file = Path("./Quarto/docs/my-presentation.md")
markdown_content = markdown_file.read_text(encoding="utf-8")

# Define prompt file
system_prompt_file = Path("./prompts/prompt-analyse-slides-structured.md")

# Create system prompt
system_prompt = interpolate_file(
    system_prompt_file,
    variables={
        "audience": audience_content,
        "length": length_content,
        "type": type_content,
        "event": event_content,
    },
)

# Define data structure to extract from the input
ScoreType = Annotated[int, Field(ge=0, le=10)]
PercentType = Annotated[float, Field(ge=0.0, le=100.0)]
MinutesType = Annotated[int, Field(ge=0)]
SlideCount = Annotated[int, Field(ge=0)]

class ScoringCategory(BaseModel):
    score: ScoreType = Field(..., description="Score from 1–10.")
    justification: str = Field(..., description="Brief explanation of the score.")
    improvements: Optional[str] = Field(
        None,
        description="Concise, actionable improvements, mentioning slide numbers if applicable.",
    )
    score_after_improvements: ScoreType = Field(
        ..., description="Estimated score after suggested improvements."
    )

class DeckAnalysis(BaseModel):
    presentation_title: str = Field(..., description="The presentation title.")
    total_slides: SlideCount
    percent_with_code: PercentType
    percent_with_images: PercentType
    estimated_duration_minutes: MinutesType
    tone: str = Field(
        ..., description="Brief description of the tone of the presentation."
    )

    clarity: ScoringCategory = Field(
        ...,
        description="Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    )
    relevance: ScoringCategory = Field(
        ...,
        description="Assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    )
    visual_design: ScoringCategory = Field(
        ...,
        description="Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    )
    engagement: ScoringCategory = Field(
        ...,
        description="Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    )
    pacing: ScoringCategory = Field(
        ...,
        description="Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    )
    structure: ScoringCategory = Field(
        ...,
        description="Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    )
    concistency: ScoringCategory = Field(  # spelling kept as-is
        ...,
        description="Evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    )
    accessibility: ScoringCategory = Field(
        ...,
        description="Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    )

# Initialise chat with Claude Sonnet 4 model
chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt=system_prompt,
)

# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat.chat_structured(
    interpolate("Here are the slides in Markdown: {{ markdown_content }}"),
    data_model=DeckAnalysis,
)
```

</details>
<details class="code-fold">
<summary>Show output</summary>

``` python
{'presentation_title': 'The Shiny Side of LLMs',
 'total_slides': 16,
 'percent_with_code': 31.25,
 'percent_with_images': 6.25,
 'estimated_duration_minutes': 10,
 'tone': 'Casual and friendly with a teaching approach, using emojis and humor to make technical content approachable',
 'clarity': {'score': 6,
  'justification': 'Good step-by-step approach and clear explanations, but heavy code blocks may confuse non-technical audience members. Key concepts are well-defined.',
  'improvements': "Simplify code examples on slides 5-6, 8-9, 11-12 to show only essential lines with comments. Add brief explanations of technical terms like 'reactive programming' on slide 7.",
  'score_after_improvements': 8},
 'relevance': {'score': 8,
  'justification': 'Highly relevant to the posit::conf audience with practical Python and R examples. Addresses real need for AI integration in data science workflows.',
  'improvements': 'Add a brief mention of common use cases data scientists might have for LLM-powered apps beyond presentation feedback (slide 3 or 14).',
  'score_after_improvements': 8},
 'visual_design': {'score': 4,
  'justification': 'Very text-heavy with large code blocks that will be difficult to read in a presentation setting. Limited visual hierarchy and only one image/GIF.',
  'improvements': 'Replace full code blocks on slides 5-6, 8-9, 11-12 with key snippets only. Add diagrams showing the app architecture on slide 4. Include screenshots of DeckCheck app on slide 3.',
  'score_after_improvements': 7},
 'engagement': {'score': 7,
  'justification': 'Good use of humor, emojis, and relatable examples (DeckCheck concept). The magic GIF adds personality. However, code-heavy sections may lose audience attention.',
  'improvements': 'Add interactive elements or polls. Include a brief live demo or recorded demo on slide 10 instead of the GIF. Show before/after examples of presentation feedback.',
  'score_after_improvements': 8},
 'pacing': {'score': 5,
  'justification': 'Uneven distribution with slides 5-6, 8-9, 11-12 being too dense for a 10-minute talk. Some slides like slide 1 and 15 are very light.',
  'improvements': 'Condense setup information from slides 2-4 into 2 slides. Reduce code examples to key snippets. Combine slides 1 and 2 into a single introduction slide.',
  'score_after_improvements': 7},
 'structure': {'score': 7,
  'justification': 'Logical flow from introduction through setup, basic concepts, and implementation. Clear progression from simple to complex. Good use of the DeckCheck example throughout.',
  'improvements': 'Add an agenda slide after slide 1. Create clearer section breaks between setup (slides 2-4), concepts (slides 5-7), and implementation (slides 8-12).',
  'score_after_improvements': 8},
 'concistency': {'score': 8,
  'justification': 'Consistent tone, formatting, and use of the DeckCheck example throughout. Parallel structure for Python and R examples works well.',
  'improvements': None,
  'score_after_improvements': 8},
 'accessibility': {'score': 4,
  'justification': 'Code blocks will be difficult to read for audience members, especially those with visual challenges. Font sizes in code examples are likely too small for presentation setting.',
  'improvements': 'Use larger fonts and fewer lines in code examples (slides 5-6, 8-9, 11-12). Add high contrast between text and background. Include alt text descriptions for the GIF on slide 10.',
  'score_after_improvements': 7}
```

</details>

The code above defines a set of Pydantic models that describe the expected structure of our output.`ScoringCategory` is a reusable model containing a score (an integer constrained between 0 and 10), a justification string, optional improvement suggestions, and an estimated score after implementing the improvements. Numeric fields in the top-level model, `DeckAnalysis`, are validated using `Annotated` types with constraints defined via `Field(...)` . For example, to ensure percentages are between 0.0 and 100.0, and counts are non-negative. The `DeckAnalysis` model nests eight `ScoringCategory` models. It saves some duplication. The top-level model is given to the `chat_structured()` method: `chat.chat_structured(interpolate("Here are the slides in Markdown: {{ markdown_content }}"), data_model=DeckAnalysis)` .

</div>
<div id="tabset-10-2">

To use structured output, you use `$chat_structured()` instead of the `$chat()`method. You'll also need to define a type specification that describes the structure of the data that you want.

``` r
# Reusable scoring category
type_scoring_category <- type_object(
  score = type_integer(
    description = "Score from 1 to 10."
  ),
  justification = type_string(
    description = "Brief explanation of the score."
  ),
  improvements = type_string(
    description = "Concise, actionable improvements, mentioning slide numbers if applicable.",
    required = FALSE
  ),
  score_after_improvements = type_integer(
    description = "Estimated score after suggested improvements."
  )
)

# Top-level deck analysis object
type_deck_analysis <- type_object(
  presentation_title = type_string(description = "The presentation title."),
  total_slides = type_integer(description = "Total number of slides."),
  percent_with_code = type_number(
    description = "Percentage of slides containing code blocks (0–100)."
  ),
  percent_with_images = type_number(
    description = "Percentage of slides containing images (0–100)."
  ),
  estimated_duration_minutes = type_integer(
    description = "Estimated presentation length in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide."
  ),
  tone = type_string(
    description = "Brief description of the presentation tone (e.g., informal, technical, playful)."
  ),
  clarity = type_array(
    description = "Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    type_scoring_category
  ),
  relevance = type_array(
    description = "Asses how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    type_scoring_category
  ),
  visual_design = type_array(
    description = "Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    type_scoring_category
  ),
  engagement = type_array(
    description = "Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    type_scoring_category
  ),
  pacing = type_array(
    description = "Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    type_scoring_category
  ),
  structure = type_array(
    description = "Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    type_scoring_category
  ),
  concistency = type_array(
    description = "Evaluate whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    type_scoring_category
  ),
  accessibility = type_array(
    description = "Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    type_scoring_category
  )
)

# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt
)

# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat$chat_structured(
  interpolate(
    "Here are the slides in Markdown: {{ markdown_content }}"
  ),
  type = type_deck_analysis
)
```

<details class="code-fold">
<summary>Show complete code</summary>

``` r
library(ellmer)

# Get Quarto presentation and convert to plain Markdown
quarto::quarto_render(
  "./Quarto/my-presentation.qmd",
  output_format = "markdown"
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content <- "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content <- "10"
type_content <- "lightning talk"
event_content <- "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file <- "./Quarto/docs/my-presentation.md"
markdown_content <- readChar(markdown_file, file.size(markdown_file))

# Define prompt file
system_prompt_file <- "./prompts/prompt-analyse-slides-structured.md"

# Create system prompt
system_prompt <- interpolate_file(
  path = system_prompt_file,
  audience = audience_content,
  length = length_content,
  type = type_content,
  event = event_content
)

# Reusable scoring category
type_scoring_category <- type_object(
  score = type_integer(
    description = "Score from 1 to 10."
  ),
  justification = type_string(
    description = "Brief explanation of the score."
  ),
  improvements = type_string(
    description = "Concise, actionable improvements, mentioning slide numbers if applicable.",
    required = FALSE
  ),
  score_after_improvements = type_integer(
    description = "Estimated score after suggested improvements."
  )
)

# Top-level deck analysis object
type_deck_analysis <- type_object(
  presentation_title = type_string(description = "The presentation title."),
  total_slides = type_integer(description = "Total number of slides."),
  percent_with_code = type_number(
    description = "Percentage of slides containing code blocks (0–100)."
  ),
  percent_with_images = type_number(
    description = "Percentage of slides containing images (0–100)."
  ),
  estimated_duration_minutes = type_integer(
    description = "Estimated presentation length in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide."
  ),
  tone = type_string(
    description = "Brief description of the presentation tone (e.g., informal, technical, playful)."
  ),
  clarity = type_array(
    description = "Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    type_scoring_category
  ),
  relevance = type_array(
    description = "Asses how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    type_scoring_category
  ),
  visual_design = type_array(
    description = "Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    type_scoring_category
  ),
  engagement = type_array(
    description = "Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    type_scoring_category
  ),
  pacing = type_array(
    description = "Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    type_scoring_category
  ),
  structure = type_array(
    description = "Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    type_scoring_category
  ),
  concistency = type_array(
    description = "Evaluate whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    type_scoring_category
  ),
  accessibility = type_array(
    description = "Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    type_scoring_category
  )
)

# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt
)

# Start conversation with the chat
# Since all the instructions are in the system prompt, we can just
# provide the Markdown content as a message
chat$chat_structured(
  interpolate(
    "Here are the slides in Markdown: {{ markdown_content }}"
  ),
  type = type_deck_analysis
)
```

</details>
<details class="code-fold">
<summary>Show output</summary>

``` r
#> $presentation_title
#> [1] "The Shiny Side of LLMs"

#> $total_slides
#> [1] 16

#> $percent_with_code
#> [1] 56.25

#> $percent_with_images
#> [1] 6.25

#> $estimated_duration_minutes
#> [1] 12

#> $tone
#> [1] "Informal, friendly, and technical with playful elements"

#> $clarity
#>   score
#> 1     7
#> justification
#> 1 Content is generally clear with good step-by-step explanations, but some technical concepts could benefit from more context for non-technical audience members.
#> improvements
#> 1 Add brief explanations of what Shiny and LLMs are in slides 2-3. Define technical terms like 'reactive programming' in slide 7. Provide more context about API keys and authentication in slide 2.
#> score_after_improvements
#> 1                        8

#> $relevance
#>   score
#> 1     8
#> justification
#> 1 Content is highly relevant to the Python and R user audience at posit::conf, with practical examples in both languages. Good mix of beginner-friendly and intermediate concepts.
#> improvements
#> 1 Add a brief slide explaining why LLMs are relevant for data scientists specifically. Include more context about when to use LLM-powered apps in data science workflows.
#> score_after_improvements
#> 1                        9

#> $visual_design
#>   score
#> 1     6
#> justification
#> 1 Code blocks are well-formatted, but slides are text-heavy with minimal visual hierarchy. Only one image used throughout the presentation.
#> improvements
#> 1 Add visual diagrams showing the app architecture in slides 4-5. Use bullet points and icons to break up text in slides 2 and 15. Consider adding screenshots of the actual app interface.
#> score_after_improvements
#> 1                        8

#> $engagement
#>   score
#> 1     7
#> justification
#> 1 Good use of emojis and casual tone keeps it engaging. The magic GIF adds personality, but more interactive elements could enhance engagement.
#> improvements
#> 1 Add a live demo or screenshots of the working app. Include audience interaction prompts in slides 11-12. Add visual progress indicators showing the app development journey.
#> score_after_improvements
#> 1                        8

#> $pacing
#>   score
#> 1     6
#> justification
#> 1 Some slides are code-heavy (slides 8-9, 12-13) while others are very light (slide 3). The transition from basics to implementation could be smoother.
#> improvements
#> 1 Split the heavy code slides (8-9, 12-13) into smaller chunks. Add transition slides between major sections. Balance slide 14 with more concrete examples.
#> score_after_improvements
#> 1                        7

#> $structure
#>   score
#> 1     8
#> justification
#> 1 Clear logical flow from introduction to requirements to implementation. Good progression from basic concepts to advanced integration.
#> improvements
#> 1 Add an agenda slide after slide 1. Include a recap slide before the conclusion. Make the transition from slide 14 to 15 smoother with a bridge sentence.
#> score_after_improvements
#> 1                        9

#> $concistency
#>   score
#> 1     7
#> justification
#> 1 Generally consistent formatting and tone, but code highlighting varies between Python and R sections. Some inconsistency in slide structure.
#> improvements
#> 1 Ensure consistent code block styling across Python and R examples. Standardize the format for requirement lists in slide 2. Use consistent header styles throughout.
#> score_after_improvements
#> 1                        8

#> $accessibility
#>   score
#> 1     7
#> justification
#> 1 Good contrast in code blocks and readable font sizes. However, the single GIF lacks alt text description and some code blocks are quite dense.
#> improvements
#> 1 Add alt text description for the magic GIF in slide 11. Break up dense code blocks in slides 8-9, 12-13. Use larger font sizes for code comments.
#> score_after_improvements
#> 1                        8
```

</details>

You can also specify the full schema that you want to get back from the LLM as a JSON schema. This could be handy if you're not keen on manually converting everything using the `type_*()`functions (or if an LLM doesn't provide you with the correct output after asking 6 times). Your friend: `type_from_schema()`.

> **Tip**
>
> `type_object()` returns a named list in R. If you want to extract a data frame from a single prompt (e.g. reading information from a markdown table), you can wrap `type_object()` in `type_array()` and create an array of objects. We do something similar here for the scoring categories. It can be hard to wrap your head around as an R user. The `ellmer` documentation contains some more [good examples](https://ellmer.tidyverse.org/articles/structured-data.html#data-frames).

</div>
</div>

# When LLMs guess, tools know

As you've seen in our conversation with Claude so far, LLMs struggle with tasks like counting slides. This is because they don't actually run code or parse content structurally like a proper parser would. LLMs aren't doing magic, they are simply predicting the next word based on patterns in text. So when you ask an LLM, "how many slides contain code?", it's making an educated guess based on the wording of the slides. It does not actually scan them line-by-line and checking for code blocks. The result: inconsistent answers. In our example, there are 16 slides, 6 with code, and 1 with an image (aka 37.5% code slides and 6.25% image slides). The LLM gets close, but its answers vary and we're not aiming for "close enough." The solution: build something on top of the LLM that does this reliably for us. Hello something fancy called "tool calling"!

Everyone talks about tool calling these days, and for a good reason: it's that extra bit of power you give to an LLM. While it sounds complicated, it's easy to explain: you let your code handle tasks that the LLM struggles with, like accurately counting how many slides have code or images, and then the LLM uses those exact numbers. You basically help the LLM with its answer. This help comes in the form of a tool (aka a function) that you've written and exposed to the model. Of course the LLM needs to know that the tool is there to begin with, and it needs to know how to use it. Luckily `chatlas` and `ellmer` can help us doing that.

So how would this work of we want to improve the slide counts for DeckCheck? First, we construct a simple Python or R function that reads our slides, spots code blocks and images, and gives exact percentages. To make our life a little bit easier, we're opting for the HTML version of Quarto slides here, and not Markdown. In this case, HTML is handy because each slide is neatly contained in a `<section>` tag, and code is clearly marked with a `sourceCode` class. For an LLM, HTML is noisy (full of CSS, scripts, and other distractions). But for a parsing function like we're going to write, it's straightforward to process. The nice thing about such a function is that you can fully customise it: maybe you only want to count Python or R code chunks only, or ignore very short examples. We call our function `calculate_slide_metric`:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-11" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-11-1">Python</a></li>
<li><a href="#tabset-11-2">R</a></li>
</ul>
<div id="tabset-11-1">

``` python
def calculate_slide_metric(metric: str) -> Union[int, float]:
    """
    Calculates the total number of slides, percentage of slides with code blocks,
    and percentage of slides with images in a Quarto presentation HTML file.

    Parameters
    ----------
    metric : str
        The metric to calculate: "total_slides" for total number of slides,
        "code" for percentage of slides containing fenced code blocks,
        or "images" for percentage of slides containing images.

    Returns
    -------
    float or int
        The calculated metric value.
    """
    html_file = Path("./Quarto/docs/my-presentation.html")
    if not html_file.exists():
        raise FileNotFoundError(f"HTML file {html_file} does not exist.")

    # Read HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Split on <section> tags to get individual slides
    slides = html_content.split("<section")
    total_slides = len(slides)

    if metric == "total_slides":
        result = total_slides
    elif metric == "code":
        slides_with_code = sum('class="sourceCode"' in slide for slide in slides)
        result = round((slides_with_code / total_slides) * 100, 2)
    elif metric == "images":
        slides_with_image = sum("<img" in slide for slide in slides)
        result = round((slides_with_image / total_slides) * 100, 2)
    else:
        raise ValueError("Unknown metric: choose 'total_slides', 'code', or 'images'")

    return result
```

</div>
<div id="tabset-11-2">

``` r
#' Calculates the total number of slides, percentage of slides with code blocks,
#' and percentage of slides with images in a Quarto presentation HTML file.
#'
#' @param metric The metric to calculate: "total_slides" for total number of slides,
#' "code" for percentage of slides containing fenced code blocks, or "images"
#' for percentage of slides containing images.
#' @return The calculated metric value.
calculate_slide_metric <- function(metric) {
  html_file <- "./Quarto/docs/my-presentation.html"
  if (!file.exists(html_file)) {
    stop(
      "HTML file does not exist. Please render your Quarto presentation first."
    )
  }
  # Read HTML file
  html_content <- readChar(html_file, file.size(html_file))

  # Split on <section> tags to get individual slides
  slides <- unlist(strsplit(html_content, "<section"))

  total_slides <- length(slides)

  if (metric == "total_slides") {
    result <- total_slides
  } else if (metric == "code") {
    # Count slides where we see the "sourceCode" class
    slides_with_code <- sum(grepl('class="sourceCode"', slides))
    result <- round((slides_with_code / total_slides) * 100, 2)
  } else if (metric == "images") {
    # Count slides with image tag
    slides_with_image <- sum(grepl('<img', slides))
    result <- round((slides_with_image / total_slides) * 100, 2)
  } else {
    stop("Unknown metric: choose 'total_slides', 'code', or 'images'")
  }

  return(result)
}
```

</div>
</div>

This function is the tool the LLM can call to accurately count slides. It has one input argument: `metric`. To let the model know that this tool is available, we register it with `register_tool` before we start talking to the LLM.

> **Who does the work?**
>
> Note that the LLM itself is not going to read the HTML file. The underlying Python or R session that execute the function is.

There's a little catch though: structured data extraction automatically disables tool calling. Hmm... But we used structured data! Luckily you can work around this by doing a regular `chat()` and then using `chat_structured()`. We're basically adding an extra pair of user and assistant turn by dividing one task into two. This means we need to reorganise our system prompt by telling the LLM that there is a first task, and a subsequent task. The first one going to focus on retrieving the meta data, and the second one on extracting scores and improvements. For clarity, the tasks are numbered and have short alias (e.g. "Task 1 (counts)"). This makes it easier to reference them in our user prompts.

``` markdown
...

You can be asked for one of the following tasks. Each has a number and a name:

# Task 1 (counts)

...

Return only the JSON results, nothing else.

# Task 2 (suggestions)

...

You bundle your results with the results from the first task. Always return the result as a JSON object that conforms to the provided data model.
```

<details class="code-fold">
<summary>Show full prompt</summary>

``` python
"""
You are a presentation coach for data scientists that analyses presentation slide decks written in Markdown. 
You extract key information, evaluate quality, and return structured feedback that is constructive, focused and practical.

The presentation you are helping with is a {{ length }}-minute {{ type }} at {{ event }}.  
The audience is {{ audience }}. 

You can be asked for one of the following tasks. Each has a number and a name:

# Task 1 (counts)

You extract the following information:
- The number of slides
- The percentage of slides containing code blocks
- The percentage of slides containing images 

Return only the JSON results, nothing else.

# Task 2 (suggestions)

You extract the following information:
- The presentation title
- Estimated presentation length (in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide)
- Tone (a brief description)

You score the presentation on the following categories (from 1–10), and give a concise explanation:

1. Clarity of content: evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?
2. Relevance for intended audience: assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?
3. Visual design: judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?
4. Engagement: estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?
5. Pacing: analyze the distribution of content across slides. Are some slides too dense or too light? 
6. Structure: review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?
7. consistency: evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?
8. Accessibility: consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?

For each of the above scoring categories, provide specific and actionable improvements. Follow these instructions:

- Keep each suggestion concise and mention the slide number(s) if applicable.
- Do not invent issues and only suggest improvements when the content would clearly benefit from them.
- For each catogory, estimate what the new score would be if these improvements are implemented.
- Return the improvement and new score as part of the response for that category.

You bundle your results with the results from the first task. Always return the result as a JSON object that conforms to the provided data model.
"""
```

</details>

Because the `chat` object stateful (and therefore remembers previous responses), it can use the response from the first prompt for the response of the second one. Handy!

Altogether, this results in the following workflow:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-12" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-12-1">Python</a></li>
<li><a href="#tabset-12-2">R</a></li>
</ul>
<div id="tabset-12-1">

``` python
# Initialise chat with Claude Sonnet 4 model
chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt="Your system prompt",
)

# Register the tool with the chat
chat.register_tool(calculate_slide_metric)

# Start conversation with the chat
# Task 1: regular chat to extract meta-data
chat.chat(
    interpolate(
        "Execute Task 1 (counts). Here are the slides in Markdown: ..."
    )
)

# Task 2: structured chat to further analyse the slides
chat.chat_structured(
    "Execute Task 2 (suggestions)",
    data_model=DeckAnalysis,
)
```

<details class="code-fold">
<summary>Show complete code</summary>

``` python
from chatlas import ChatAnthropic, interpolate_file, interpolate
import subprocess
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Annotated, Optional, Union

# Get Quarto presentation and convert to plain Markdown + HTML
subprocess.run(
    ["quarto", "render", "./Quarto/my-presentation.qmd", "--to", "markdown,html"]
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content = "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content = "10"
type_content = "lightning talk"
event_content = "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file = Path("./Quarto/docs/my-presentation.md")
markdown_content = markdown_file.read_text(encoding="utf-8")

# Define prompt file
system_prompt_file = Path("./prompts/prompt-analyse-slides-structured-tool.md")

# Create system prompt
system_prompt = interpolate_file(
    system_prompt_file,
    variables={
        "audience": audience_content,
        "length": length_content,
        "type": type_content,
        "event": event_content,
        "markdown_content": markdown_content,
    },
)

# Define data structure to extract from the input
ScoreType = Annotated[int, Field(ge=0, le=10)]
PercentType = Annotated[float, Field(ge=0.0, le=100.0)]
MinutesType = Annotated[int, Field(ge=0)]
SlideCount = Annotated[int, Field(ge=0)]

class ScoringCategory(BaseModel):
    score: ScoreType = Field(..., description="Score from 1–10.")
    justification: str = Field(..., description="Brief explanation of the score.")
    improvements: Optional[str] = Field(
        None,
        description="Concise, actionable improvements, mentioning slide numbers if applicable.",
    )
    score_after_improvements: ScoreType = Field(
        ..., description="Estimated score after suggested improvements."
    )

class DeckAnalysis(BaseModel):
    presentation_title: str = Field(..., description="The presentation title.")
    total_slides: SlideCount
    percent_with_code: PercentType
    percent_with_images: PercentType
    estimated_duration_minutes: MinutesType
    tone: str = Field(
        ..., description="Brief description of the tone of the presentation."
    )

    clarity: ScoringCategory = Field(
        ...,
        description="Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    )
    relevance: ScoringCategory = Field(
        ...,
        description="Assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    )
    visual_design: ScoringCategory = Field(
        ...,
        description="Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    )
    engagement: ScoringCategory = Field(
        ...,
        description="Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    )
    pacing: ScoringCategory = Field(
        ...,
        description="Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    )
    structure: ScoringCategory = Field(
        ...,
        description="Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    )
    concistency: ScoringCategory = Field(  # spelling kept as-is
        ...,
        description="Evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    )
    accessibility: ScoringCategory = Field(
        ...,
        description="Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    )

# Define a tool to calculate some metrics
# Start with a function:
def calculate_slide_metric(metric: str) -> Union[int, float]:
    """
    Calculates the total number of slides, percentage of slides with code blocks,
    and percentage of slides with images in a Quarto presentation HTML file.

    Parameters
    ----------
    metric : str
        The metric to calculate: "total_slides" for total number of slides,
        "code" for percentage of slides containing fenced code blocks,
        or "images" for percentage of slides containing images.

    Returns
    -------
    float or int
        The calculated metric value.
    """
    html_file = Path("./Quarto/docs/my-presentation.html")
    if not html_file.exists():
        raise FileNotFoundError(f"HTML file {html_file} does not exist.")

    # Read HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Split on <section> tags to get individual slides
    slides = html_content.split("<section")
    total_slides = len(slides)

    if metric == "total_slides":
        result = total_slides
    elif metric == "code":
        slides_with_code = sum('class="sourceCode"' in slide for slide in slides)
        result = round((slides_with_code / total_slides) * 100, 2)
    elif metric == "images":
        slides_with_image = sum("<img" in slide for slide in slides)
        result = round((slides_with_image / total_slides) * 100, 2)
    else:
        raise ValueError("Unknown metric: choose 'total_slides', 'code', or 'images'")

    return result

# Initialise chat with Claude Sonnet 4 model
chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt=system_prompt,
)

# Register the tool with the chat
chat.register_tool(calculate_slide_metric)

# Start conversation with the chat
# Task 1: regular chat to extract meta-data
chat.chat(
    interpolate(
        "Execute Task 1 (counts). Here are the slides in Markdown: {{ markdown_content }}"
    )
)

# Task 2: structured chat to further analyse the slides
chat.chat_structured(
    "Execute Task 2 (suggestions)",
    data_model=DeckAnalysis,
)
```

</details>

We can clearly see that our tool was being called 3 times for our 3 metrics, just like it should:

``` python
# 🔧 tool request (toolu_01JSsxrB8Jj9yDY35pg1g1bc)                      
 calculate_slide_metric(metric=total_slides)                                                    



 # ✅ tool result (toolu_01JSsxrB8Jj9yDY35pg1g1bc)                        
 16                                                                      



 # 🔧 tool request (toolu_019635a7mRAotqTFNx2TfCsm)                      
 calculate_slide_metric(metric=code)                                                            



 # ✅ tool result (toolu_019635a7mRAotqTFNx2TfCsm)                        
 37.5                                                                    



 # 🔧 tool request (toolu_01Kv6nPiUeZmABADZFeN8Qgi)                      
 calculate_slide_metric(metric=images)                                                          



 # ✅ tool result (toolu_01Kv6nPiUeZmABADZFeN8Qgi)                       
 6.25                                                                    



 {                                                                       
   "total_slides": 16,                                                   
   "percentage_slides_with_code": 37.5,                                  
   "percentage_slides_with_images": 6.25                                 
 }
```

<details class="code-fold">
<summary>Show the rest of the output</summary>

``` python
{'presentation_title': 'The Shiny Side of LLMs',
 'total_slides': 16,
 'percent_with_code': 37.5,
 'percent_with_images': 6.25,
 'estimated_duration_minutes': 10,
 'tone': 'Conversational and friendly with technical depth, using emojis and casual language to make complex topics approachable',
 'clarity': {'score': 8,
  'justification': 'Clear explanations with step-by-step progression from basics to implementation. Code examples are well-structured and concepts are explained in accessible terms.',
  'improvements': "Add brief explanations of what chatlas/ellmer are on slides 5-6. Define 'reactive programming' on slide 7 for non-technical audience members.",
  'score_after_improvements': 9},
 'relevance': {'score': 9,
  'justification': 'Highly relevant to the posit::conf audience of Python/R users interested in AI. Content matches the technical level and practical focus expected.',
  'improvements': 'Consider adding a brief mention of when NOT to use LLMs in presentations on slide 14 to provide balanced perspective.',
  'score_after_improvements': 9},
 'visual_design': {'score': 6,
  'justification': 'Slides are text-heavy with large code blocks. Only one visual element (GIF on slide 11). Layout is clean but could benefit from more visual variety.',
  'improvements': 'Add diagrams showing app architecture on slides 4 or 8. Break up dense text on slide 14 into bullet points. Consider visual examples of the DeckCheck app interface.',
  'score_after_improvements': 8},
 'engagement': {'score': 7,
  'justification': 'Good use of emojis, casual tone, and interactive elements. The GIF adds humor and the practical demo concept is engaging.',
  'improvements': 'Add a live demo screenshot or mockup of the DeckCheck app on slide 3. Include audience interaction prompts on slides 2-3 asking about their presentation challenges.',
  'score_after_improvements': 8},
 'pacing': {'score': 7,
  'justification': 'Generally well-paced but some slides are dense (slides 8-9, 12-13) while others are light (slide 11). Code-heavy slides may take longer to explain.',
  'improvements': 'Split slide 14 into two slides - one for UX principles, one for error handling. Reduce code on slides 8-9 to focus on key concepts only.',
  'score_after_improvements': 8},
 'structure': {'score': 8,
  'justification': 'Clear logical flow from introduction to requirements to implementation to next steps. Good narrative arc building toward a complete solution.',
  'improvements': "Add a brief agenda/outline slide after slide 1 to preview the journey. Include a summary slide before 'Thank you' recapping key takeaways.",
  'score_after_improvements': 9},
 'concistency': {'score': 8,
  'justification': 'Consistent formatting, tone, and code style throughout. Good parallel structure between Python and R examples.',
  'improvements': 'Ensure consistent capitalization in slide titles (slide 11 uses title case while others use sentence case). Standardize code comment styles across examples.',
  'score_after_improvements': 9},
 'accessibility': {'score': 7,
  'justification': 'Text appears readable but code blocks are quite dense. Good contrast likely but some slides have significant cognitive load.',
  'improvements': 'Increase font size in code blocks on slides 5-6, 8-9, 12-13. Add alt text description for the GIF on slide 11. Use consistent heading hierarchy.',
  'score_after_improvements': 8}}
```

</details>
</div>
<div id="tabset-12-2">

``` r
# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt
)

# Register the tool with the chat
chat$register_tool(calculate_slide_metric)

# Start conversation with the chat
# Task 1: regular chat to extract meta-data
chat$chat(
  interpolate(
    "Execute Task 1 (counts). Here are the slides in Markdown: {{ markdown_content }}"
  )
)

# Task 2: structured chat to further analyse the slides
chat$chat_structured(
  "Execute Task 2 (suggestions)",
  type = type_deck_analysis
)
```

<details class="code-fold">
<summary>Show complete code</summary>

``` r
library(ellmer)

# Get Quarto presentation and convert to plain Markdown + HTML
quarto::quarto_render(
  "./Quarto/my-presentation.qmd",
  output_format = c("markdown", "html")
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content <- "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content <- "10"
type_content <- "lightning talk"
event_content <- "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file <- "./Quarto/docs/my-presentation.md"
markdown_content <- readChar(markdown_file, file.size(markdown_file))

# Define prompt file
system_prompt_file <- "./prompts/prompt-analyse-slides-structured-tool.md"

# Create system prompt
system_prompt <- interpolate_file(
  path = system_prompt_file,
  audience = audience_content,
  length = length_content,
  type = type_content,
  event = event_content
)

# Reusable scoring category
type_scoring_category <- type_object(
  score = type_integer(
    description = "Score from 1 to 10."
  ),
  justification = type_string(
    description = "Brief explanation of the score."
  ),
  improvements = type_string(
    description = "Concise, actionable improvements, mentioning slide numbers if applicable.",
    required = FALSE
  ),
  score_after_improvements = type_integer(
    description = "Estimated score after suggested improvements."
  )
)

# Top-level deck analysis object
type_deck_analysis <- type_object(
  presentation_title = type_string(description = "The presentation title."),
  total_slides = type_integer(description = "Total number of slides."),
  percent_with_code = type_number(
    description = "Percentage of slides containing code blocks (0–100)."
  ),
  percent_with_images = type_number(
    description = "Percentage of slides containing images (0–100)."
  ),
  estimated_duration_minutes = type_integer(
    description = "Estimated presentation length in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide."
  ),
  tone = type_string(
    description = "Brief description of the presentation tone (e.g., informal, technical, playful)."
  ),
  clarity = type_array(
    description = "Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    type_scoring_category
  ),
  relevance = type_array(
    description = "Asses how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    type_scoring_category
  ),
  visual_design = type_array(
    description = "Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    type_scoring_category
  ),
  engagement = type_array(
    description = "Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    type_scoring_category
  ),
  pacing = type_array(
    description = "Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    type_scoring_category
  ),
  structure = type_array(
    description = "Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    type_scoring_category
  ),
  concistency = type_array(
    description = "Evaluate whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    type_scoring_category
  ),
  accessibility = type_array(
    description = "Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    type_scoring_category
  )
)

# Define a tool to calculate some metrics
# Start with a function:

#' Calculates the total number of slides, percentage of slides with code blocks,
#' and percentage of slides with images in a Quarto presentation HTML file.
#'
#' @param metric The metric to calculate: "total_slides" for total number of slides,
#' "code" for percentage of slides containing fenced code blocks, or "images"
#' for percentage of slides containing images.
#' @return The calculated metric value.
calculate_slide_metric <- function(metric) {
  html_file <- "./Quarto/docs/my-presentation.html"
  if (!file.exists(html_file)) {
    stop(
      "HTML file does not exist. Please render your Quarto presentation first."
    )
  }
  # Read HTML file
  html_content <- readChar(html_file, file.size(html_file))

  # Split on <section> tags to get individual slides
  slides <- unlist(strsplit(html_content, "<section"))

  total_slides <- length(slides)

  if (metric == "total_slides") {
    result <- total_slides
  } else if (metric == "code") {
    # Count slides where we see the "sourceCode" class
    slides_with_code <- sum(grepl('class="sourceCode"', slides))
    result <- round((slides_with_code / total_slides) * 100, 2)
  } else if (metric == "images") {
    # Count slides with image tag
    slides_with_image <- sum(grepl('<img', slides))
    result <- round((slides_with_image / total_slides) * 100, 2)
  } else {
    stop("Unknown metric: choose 'total_slides', 'code', or 'images'")
  }

  return(result)
}

# Optionally, to avoid manual work:
# create_tool_def(calculate_slide_metric)
calculate_slide_metric <- tool(
  calculate_slide_metric,
  "Returns the calculated metric value",
  metric = type_string(
    'The metric to calculate: "total_slides" for total number of slides, 
      "code" for percentage of slides containing fenced code blocks, or "images"
      for percentage of slides containing images.',
    required = TRUE
  )
)

# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt
)

# Register the tool with the chat
chat$register_tool(calculate_slide_metric)

# Start conversation with the chat
# Task 1: regular chat to extract meta-data
chat$chat(
  interpolate(
    "Execute Task 1 (counts). Here are the slides in Markdown: {{ markdown_content }}"
  )
)

# Task 2: structured chat to further analyse the slides
chat$chat_structured(
  "Execute Task 2 (suggestions)",
  type = type_deck_analysis
)
```

</details>

We can clearly see that our tool was being called 3 times for our 3 metrics, just like it should:

``` r
#> ◯ [tool call] calculate_slide_metric(metric = "total_slides")
#> ● #> 16
#> ◯ [tool call] calculate_slide_metric(metric = "code")
#> ● #> 37.5
#> ◯ [tool call] calculate_slide_metrimetric = "images")
#> ● #> 6.25
#> ```json
#> {
#>   "total_slides": 16,
#>   "percentage_slides_with_code": 37.5,
#>   "percentage_slides_with_images": 6.25
#> }
#> ```
```

<details class="code-fold">
<summary>Show the rest of the output</summary>

``` r
#> ◯ [tool call] calculate_slide_metric(metric = "total_slides")
#> ● #> 16
#> ◯ [tool call] calculate_slide_metric(metric = "code")
#> ● #> 37.5
#> ◯ [tool call] calculate_slide_metric(metric = "images")
#> ● #> 6.25
#> ```json
#> {
#>   "total_slides": 16,
#>   "percentage_slides_with_code": 37.5,
#>   "percentage_slides_with_images": 6.25
#> }
#> ```
#> $presentation_title
#> [1] "The Shiny Side of LLMs"
#> 
#> $total_slides
#> [1] 16
#> 
#> $percent_with_code
#> [1] 37.5
#> 
#> $percent_with_images
#> [1] 6.25
#> 
#> $estimated_duration_minutes
#> [1] 12
#> 
#> $tone
#> [1] "Informal and conversational with technical depth"
#> 
#> $clarity
#>   score
#> 1     8
#>                                                                                                                  justification
#> 1 Content is well-explained with clear examples and step-by-step progression. Technical concepts are introduced appropriately.
#>                                                                                                                                                                      improvements
#> 1 Add brief definition of LLMs on slide 2 for audience members new to the topic. Consider adding expected output examples on slides 5-6 to show what the LLM responses look like.
#>   score_after_improvements
#> 1                        9
#> 
#> $relevance
#>   score
#> 1     9
#>                                                                                                                                                justification
#> 1 Highly relevant for the posit::conf audience - focuses on practical implementation in both R and Python with Shiny, which is core to the conference theme.
#>                                                                             improvements
#> 1 Content is already well-targeted for the audience. No significant improvements needed.
#>   score_after_improvements
#> 1                        9
#> 
#> $visual_design
#>   score
#> 1     6
#>                                                                                                                              justification
#> 1 Layout is clean but quite text-heavy. Code blocks are well-formatted, but some slides like slide 8 and 14 contain large amounts of text.
#>                                                                                                                                                                                                                            improvements
#> 1 Break up slide 8 (Shiny basics: Python) into 2 slides - separate UI and server logic. Split slide 14 (User experience) into bullet points or multiple slides. Add more visual elements like diagrams or screenshots of the final app.
#>   score_after_improvements
#> 1                        8
#> 
#> $engagement
#>   score
#> 1     7
#>                                                                                                                                           justification
#> 1 Good use of emojis and conversational tone. The magic GIF on slide 10 adds personality. However, mostly text-based with limited interactive elements.
#>                                                                                                                                                                     improvements
#> 1 Add a live demo screenshot or video on slide 15 showing the final DeckCheck app in action. Consider adding a simple architecture diagram on slide 4 to visualize the workflow.
#>   score_after_improvements
#> 1                        8
#> 
#> $pacing
#>   score
#> 1     7
#>                                                                                                                        justification
#> 1 Good balance overall, but some slides are content-heavy (slides 8, 9, 12, 13) which may feel rushed in a 10-minute lightning talk.
#>                                                                                                                                                                                           improvements
#> 1 Simplify code examples on slides 8-9 by showing only key parts. Break slide 12-13 into smaller, focused slides. Consider removing some implementation details to focus on the core concept and demo.
#>   score_after_improvements
#> 1                        8
#> 
#> $structure
#>   score
#> 1     8
#>                                                                                                                         justification
#> 1 Clear logical flow from introduction to implementation to next steps. Good progression from basic concepts to complete integration.
#>                                                                                                                                                          improvements
#> 1 Add a brief agenda or roadmap slide after slide 1 to set expectations. Include a quick recap slide before the 'Up next' section to summarize what was accomplished.
#>   score_after_improvements
#> 1                        9
#> 
#> $concistency
#>   score
#> 1     8
#>                                                                                                                          justification
#> 1 Consistent formatting for code blocks and good parallel structure between R and Python examples. Tone remains consistent throughout.
#>                                                                                                                                             improvements
#> 1 Ensure slide titles follow consistent capitalization (slide 10 'Where's the magic?' vs others). Standardize bullet point formatting across all slides.
#>   score_after_improvements
#> 1                        9
#> 
#> $accessibility
#>   score
#> 1     7
#>                                                                                                                                justification
#> 1 Code is readable with good contrast. However, some slides have dense text that may be challenging to read quickly during a lightning talk.
#>                                                                                                                                                 improvements
#> 1 Increase font size for code blocks on slides 5-6, 8-9, 12-13. Reduce text density on slide 14. Ensure the GIF on slide 10 has alt text for screen readers.
#>   score_after_improvements
#> 1                        8
```

</details>
</div>
</div>

So how does the LLM know that it needs to use a tool? We didn't specifically tell it to use it. We just registered it and let the LLM figure it out for itself. How does that work? The first step in the process is turning a vague, human-friendly request into something a tool can actually run. In our case, our prompt contained this:

``` markdown
...

You extract the following information:
- The number of slides
- The percentage of slides containing code blocks
- The percentage of slides containing images 

Return only the JSON results, nothing else.

...
```

When the LLM sees "The percentage of slides containing images," it doesn't just guess. It translates that phrase into structured parameters for the registered tool: `calculate_slide_metric`. The LLM knows it needs to set `metric` to `"images"` or `"code"`, depending on the request. Once it has those details, it calls the tool with this parameter and responds with the result in JSON (and nothing else, as we told it to: LLMs love to talk).

This is where tool calling really shines. It's not just about running code: it's about structuring messy, open-ended requests into something that can be understood by our code. You could ask "Show me how code-heavy my slides are," "Can you tell me how many images are in this presentation?" or "What percentage of slides have images?" and the LLM would know to call the same tool. The wording changes, but the intent is the same, and the LLM can map all those variations to the right parameters. It's pretty clever!

The parameters make it even more powerful. If we created a tool with no parameters (e.g. one that only ever returned the percentage of image slides), it could only answer that exact question. But by designing it with parameters, it's way more flexible. The same `calculate_slide_metric` function can handle requests for total slides, code slides, image slides, or anything else we choose to add later. And because the LLM can chain tool calls, aka run the tool more than once in a conversation, it can check for the 3 metrics all at once and bundle the results together in one tidy JSON.

# From tools to agents

Right now, DeckCheck's tool does one (or, ok, technically speaking, three) things: it calculates the metrics you've defined. That's it. But tool calling can go much further. Imagine that, instead of passing parameters to code you've already written, the LLM could actually write its own code to analyse your slides. Creepy, right? The LLM is just... doing its own thing. This is sometimes called "agentic AI", where the LLM can formulate and execute coding tasks to learn about *and alter* the state of the world.

Sounds cool, but what if the LLM decides to do something that's harmful? Imagine it dropping database tables, overwriting files, or sending data somewhere it shouldn't. Without limits, arbitrary code execution can be as risky as it is powerful. That's why you need to take some safety measures. For example, if you let the LLM write SQL statements, you can limit it so it only allows read-only SQL executing. This is exactly what [querychat](https://github.com/posit-dev/querychat) does. Or, instead of giving the LLM complete freedom, you can add a human back into the loop by asking explicit user approval before anything gets executed. An example of such a project is the new (experimental) agent called [Databot](https://open-vsx.org/extension/posit/databot). Databot is there to assist you in your data analysis, making you faster and more efficient. But it doesn't mean it can replace you: to use these tools effectively and safely, [your human skills are still needed](https://posit.co/blog/databot-is-not-a-flotation-device/). Curious to learn more about Databot? Check out the [official announcement](https://posit.co/blog/introducing-databot/)!

This is also where MCP ([Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro)) comes in. You have data or tools (an R/Python function, an API, a database, spreadsheet, whatever). You want an LLM to use them. But the LLM doesn't know what you have or how to access it. The problem is, the LLM doesn't automatically know what you have or how to use it. MCP solves that by providing a standard way to describe these tools and make them available to the model. It's like handing the LLM a clearly written "menu" of what's on offer and how to order it. That's why MCP is often described as "a USB-C port for LLM applications": it standardises how models can plug into all sorts of tools and data sources. It opens a world of possibilities. But the details of MCP are a whole topic on their own, so we'll leave that for another time. If you got curious about MCP, you can check out the relevant section in the [`chatlas` documentation](https://posit-dev.github.io/chatlas/misc/mcp-tools.html), or [`mcptools`](https://posit-dev.github.io/mcptools/) for some R fun with MCP.

# Model parameters

We covered the "big" parts to get a response we can work with: we set a system prompt, crafted a nice detailed input prompt, used structured output, and gave the LLM some extra calculation power with a tool. But still we are getting slightly different results every single time: the suggested improvements are always different and even things like estimated duration vary. Ideally, we want to have as much "control" as possible over the response an LLM generates. And while we can't 100% control what an LLM does, we can tweak its behaviour by changing (some of) the settings. These settings are also called model parameters.

> **A bit playing around the edges**
>
> Tweaking model parameters is playing around the edges: it won't magically fix a bad prompt. Writing a good prompt and knowing how to use `chatlas` or `ellmer` programmatically already give a solid foundation. Normally default settings for model parameters are the default for a reason: they tend to give the most desired results. But understanding which parameters there are and what kind of effect they have on the LLM's response is a good exercise anyway!

There are many model parameters, and the ones you can change are different for each provider and model, but generally, these are the most noteworthy ones:

- **Temperature**: when you ask an LLM the same question you might expect the same answer, just like a calculator always gives the same result for 2 + 2. But an LLM isn't a calculator: it's more like a smart writer. It "knows" how it should answer your question, but it can phrase it in many ways. That's because its default settings allow a little randomness, a little "creativity". The wording, order, or formatting might change, even if the meaning stays the same. This creativity is also called the model's temperature. Typically, the temperature ranges from 0.0 to 1.0. A temperature closer to 1.0 is great for creative and generative tasks, and a temperature closer to 0.0 is best for analytical tasks. Note that a temperature of 0 doesn't mean an LLM will be fully deterministic: probability mechanisms will always cause slight variations in answers. Also note that a temperature of 1 might lead to very creative answers that don't make much sense anymore.

- **Seed**: adds a bit of predictability to a model that's normally unpredictable. As mentioned before, asking the same question twice (especially with a higher temperature) gives you slightly different answers. That's great for creativity, but not always what you want. By setting a seed you make randomness reproducible. It tells the model to "start from the same random point" every time. This is especially helpful for testing or generating consistent results in production. Note: not all LLM providers support the seed parameter! Looking at the [documentation](https://docs.anthropic.com/en/api/messages), Anthropic does not seem to support this parameter in API calls.

- **Top-p**: controls how many possible words the model can choose from when generating a response. It does this by adding up the most likely words until a probability threshold is reached. Let's take our original prompt as an example: "I'm working on a presentation with the title: 'The Shiny Side of LLMs'. What's your feedback just based on that title?". The model considers several next phrases:

  - "is catchy and clear" (50%)
  - "could be more specific" (25%)
  - "is creative but vague" (15%)
  - "needs glitter" (7%)
  - "mentions Dalmatians" (3%)

  If top-p = 0.9, only the top three are used (since 50% + 25% + 15% = 90%). The model randomly picks one of those three options, with the probability of each token still guiding the choice (so the 50% token is much more likely to be picked than the 15% one). If top-p = 0.75, the model only considers the first two options. A higher top-p value leads to more variety, while a lower top-p leads to more focussed and "safe" answers.

  It's not recommended to control creativity via both temperature or top-p: pick one. If you start tweaking both parameters they might cancel each other out and it can lead to a weird balance. Changing the temperature is the simpler and more predictive way to control creativity: it's more linear and easier to wrap your head around.

- **Maximum length or maximum output tokens**: the limit on how long the model's response can be. Different models have different maximum values for this parameter. Note that with tokens, you're not counting characters or words. Instead, you're telling the model: "Don't generate more than X chunks of language". For example, Claude Sonnet 4 has a [maximum output of 64,000 tokens](https://docs.anthropic.com/en/docs/about-claude/models/overview#model-comparison-table) (which is around 48,000 words).

And to come back to some jargon, changing any of these model parameters is called inference tweaking. It's trying to control how creative, long, or focused responses are.

Model parameters are supported by most providers and with `chatlas` and `ellmer` you can quickly set them in a provider-agnostic way.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-13" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-13-1">Python</a></li>
<li><a href="#tabset-13-2">R</a></li>
</ul>
<div id="tabset-13-1">

``` python
# Set model parameters (optional)
chat.set_model_params(
    temperature=0.8, # default is 1
)
```

By using the [`set_model_params()`](https://posit-dev.github.io/chatlas/reference/Chat.html#set_model_params.qmd) method on the chat object, you can quickly set things like `temperature`, `max_tokens` or `top_p`. These model parameters apply to the whole chat. If you want to revert to the default parameters, you can pass `None` to the relevant parameter.

</div>
<div id="tabset-13-2">

``` r
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  params = params(
    temperature = 0.8 # default is 1
  )
)
```

Adding parameters to our model is easy: we use the [`params` argument](https://ellmer.tidyverse.org/reference/params.html) in `chat_anthropic()`. We create those parameters with [`params()`](https://ellmer.tidyverse.org/reference/params.html). This helper function creates a list of parameters, where parameter names are automatically standardised and included in the correctly place in the API call. You won't have to do a thing. Thanks `ellmer`!

Note: since `ellmer` 0.3.0 you can also use [`chat()`](https://ellmer.tidyverse.org/reference/chat-any.html) and pass the `params` argument there.

</div>
</div>

Besides model parameters, which are commonly used across providers, there's also something called [chat parameters](https://posit-dev.github.io/chatlas/get-started/parameters.html#chat-parameters). The difference is that the latter are specific to the model provider you're using.

# Full workflow

A nice prompt, structured output, tool calling, model parameters... It all led us to the following workflow:

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-14" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-14-1">Python</a></li>
<li><a href="#tabset-14-2">R</a></li>
<li><a href="#tabset-14-3">System prompt</a></li>
</ul>
<div id="tabset-14-1">

> **Get this code from GitHub**
>
> You can grab the code directly from [here](https://github.com/hypebright/the-shiny-side-of-llms/blob/d1094d2774f9d0c213c7ddf6e17f94da706b1b76/Py/demo/conversation-tool.py).

<details class="code-fold">
<summary>See full workflow</summary>

``` python
from chatlas import ChatAnthropic, interpolate_file
import subprocess
from pathlib import Path
from pydantic import BaseModel, Field
from typing import Annotated, Optional, Union

chat = ChatAnthropic(
    model="claude-sonnet-4-20250514",
    system_prompt="You are a presentation coach for data scientists. You give constructive, focused, and practical feedback on titles, structure, and storytelling.",
)

# Set model parameters (optional)
chat.set_model_params(
    temperature=0.8,  # default is 1
)

# Get Quarto presentation and convert to plain Markdown + HTML
subprocess.run(
    ["quarto", "render", "./my-presentation.qmd", "--to", "markdown,html"]
)

# Use prompt file
# Step 1: first step of the analysis (meta-data)
prompt_file_1 = "./prompts/prompt-analyse-slides-structured-tool-1.md"
# Step 2: second step of the analysis (detailed analysis with improvements)
prompt_file_2 = Path("./prompts/prompt-analyse-slides-structured-tool-2.md")

# Dynamic data
# Audience, length in minutes, type, and event
audience_content = "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content = "10"
type_content = "lightning talk"
event_content = "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file = Path("./docs/my-presentation.md")
markdown_content = markdown_file.read_text(encoding="utf-8")

# Construct the first prompt
prompt_complete_1 = interpolate_file(
    prompt_file_1,
    variables={
        "audience": audience_content,
        "length": length_content,
        "type": type_content,
        "event": event_content,
        "markdown": markdown_content,
    },
)

# Read the second prompt (no dynamic data)
prompt_complete_2 = prompt_file_2.read_text(encoding="utf-8")

# Define data structure to extract from the input
ScoreType = Annotated[int, Field(ge=0, le=10)]
PercentType = Annotated[float, Field(ge=0.0, le=100.0)]
MinutesType = Annotated[int, Field(ge=0)]
SlideCount = Annotated[int, Field(ge=0)]

class ScoringCategory(BaseModel):
    score: ScoreType = Field(..., description="Score from 1–10.")
    justification: str = Field(..., description="Brief explanation of the score.")
    improvements: Optional[str] = Field(
        None,
        description="Concise, actionable improvements, mentioning slide numbers if applicable.",
    )
    score_after_improvements: ScoreType = Field(
        ..., description="Estimated score after suggested improvements."
    )

class DeckAnalysis(BaseModel):
    presentation_title: str = Field(..., description="The presentation title.")
    total_slides: SlideCount
    percent_with_code: PercentType
    percent_with_images: PercentType
    estimated_duration_minutes: MinutesType
    tone: str = Field(
        ..., description="Brief description of the tone of the presentation."
    )

    clarity: ScoringCategory = Field(
        ...,
        description="Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    )
    relevance: ScoringCategory = Field(
        ...,
        description="Assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    )
    visual_design: ScoringCategory = Field(
        ...,
        description="Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    )
    engagement: ScoringCategory = Field(
        ...,
        description="Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    )
    pacing: ScoringCategory = Field(
        ...,
        description="Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    )
    structure: ScoringCategory = Field(
        ...,
        description="Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    )
    concistency: ScoringCategory = Field(  # spelling kept as-is
        ...,
        description="Evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    )
    accessibility: ScoringCategory = Field(
        ...,
        description="Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    )

# Define a tool to calculate some metrics
# Start with a function:
def calculate_slide_metric(metric: str) -> Union[int, float]:
    """
    Calculates the total number of slides, percentage of slides with code blocks,
    and percentage of slides with images in a Quarto presentation HTML file.

    Parameters
    ----------
    metric : str
        The metric to calculate: "total_slides" for total number of slides,
        "code" for percentage of slides containing fenced code blocks,
        or "images" for percentage of slides containing images.

    Returns
    -------
    float or int
        The calculated metric value.
    """
    html_file = Path("./docs/my-presentation.html")
    if not html_file.exists():
        raise FileNotFoundError(f"HTML file {html_file} does not exist.")

    # Read HTML file
    with open(html_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Split on <section> tags to get individual slides
    slides = html_content.split("<section")
    total_slides = len(slides)

    if metric == "total_slides":
        result = total_slides
    elif metric == "code":
        slides_with_code = sum('class="sourceCode"' in slide for slide in slides)
        result = round((slides_with_code / total_slides) * 100, 2)
    elif metric == "images":
        slides_with_image = sum("<img" in slide for slide in slides)
        result = round((slides_with_image / total_slides) * 100, 2)
    else:
        raise ValueError("Unknown metric: choose 'total_slides', 'code', or 'images'")

    return result

chat.register_tool(calculate_slide_metric)

# Step 1: use regular chat to extract meta-data
# Note that this *should* make use of our tool
chat.chat(prompt_complete_1)

# Step 2: use structured chat to further analyse the slides
chat.chat_structured(prompt_complete_2, data_model=DeckAnalysis)
```

</details>
</div>
<div id="tabset-14-2">

> **Get this code from GitHub**
>
> You can grab the code directly from [here](https://github.com/hypebright/the-shiny-side-of-llms/blob/d1094d2774f9d0c213c7ddf6e17f94da706b1b76/R/demo/conversation-tool.R).

<details class="code-fold">
<summary>See full workflow</summary>

``` r
library(ellmer)

# Get Quarto presentation and convert to plain Markdown + HTML
quarto::quarto_render(
  "./Quarto/my-presentation.qmd",
  output_format = c("markdown", "html")
)

# Dynamic data
# Audience, length in minutes, type, and event
audience_content <- "Python and R users who are curious about AI and large language models, but not all of them have a deep technical background"
length_content <- "10"
type_content <- "lightning talk"
event_content <- "posit::conf(2025)"

# Read the generated Markdown file containing our slides
markdown_file <- "./Quarto/docs/my-presentation.md"
markdown_content <- readChar(markdown_file, file.size(markdown_file))

# Define prompt file
system_prompt_file <- "./prompts/prompt-analyse-slides-structured-tool.md"

# Create system prompt
system_prompt <- interpolate_file(
  path = system_prompt_file,
  audience = audience_content,
  length = length_content,
  type = type_content,
  event = event_content
)

# Reusable scoring category
type_scoring_category <- type_object(
  score = type_integer(
    description = "Score from 1 to 10."
  ),
  justification = type_string(
    description = "Brief explanation of the score."
  ),
  improvements = type_string(
    description = "Concise, actionable improvements, mentioning slide numbers if applicable.",
    required = FALSE
  ),
  score_after_improvements = type_integer(
    description = "Estimated score after suggested improvements."
  )
)

# Top-level deck analysis object
type_deck_analysis <- type_object(
  presentation_title = type_string(description = "The presentation title."),
  total_slides = type_integer(description = "Total number of slides."),
  percent_with_code = type_number(
    description = "Percentage of slides containing code blocks (0–100)."
  ),
  percent_with_images = type_number(
    description = "Percentage of slides containing images (0–100)."
  ),
  estimated_duration_minutes = type_integer(
    description = "Estimated presentation length in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide."
  ),
  tone = type_string(
    description = "Brief description of the presentation tone (e.g., informal, technical, playful)."
  ),
  clarity = type_array(
    description = "Evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?",
    type_scoring_category
  ),
  relevance = type_array(
    description = "Asses how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?",
    type_scoring_category
  ),
  visual_design = type_array(
    description = "Judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?",
    type_scoring_category
  ),
  engagement = type_array(
    description = "Estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?",
    type_scoring_category
  ),
  pacing = type_array(
    description = "Analyze the distribution of content across slides. Are some slides too dense or too light? ",
    type_scoring_category
  ),
  structure = type_array(
    description = "Review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?",
    type_scoring_category
  ),
  concistency = type_array(
    description = "Evaluate whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?",
    type_scoring_category
  ),
  accessibility = type_array(
    description = "Consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?",
    type_scoring_category
  )
)

# Define a tool to calculate some metrics
# Start with a function:

#' Calculates the total number of slides, percentage of slides with code blocks,
#' and percentage of slides with images in a Quarto presentation HTML file.
#'
#' @param metric The metric to calculate: "total_slides" for total number of slides,
#' "code" for percentage of slides containing fenced code blocks, or "images"
#' for percentage of slides containing images.
#' @return The calculated metric value.
calculate_slide_metric <- function(metric) {
  html_file <- "./Quarto/docs/my-presentation.html"
  if (!file.exists(html_file)) {
    stop(
      "HTML file does not exist. Please render your Quarto presentation first."
    )
  }
  # Read HTML file
  html_content <- readChar(html_file, file.size(html_file))

  # Split on <section> tags to get individual slides
  slides <- unlist(strsplit(html_content, "<section"))

  total_slides <- length(slides)

  if (metric == "total_slides") {
    result <- total_slides
  } else if (metric == "code") {
    # Count slides where we see the "sourceCode" class
    slides_with_code <- sum(grepl('class="sourceCode"', slides))
    result <- round((slides_with_code / total_slides) * 100, 2)
  } else if (metric == "images") {
    # Count slides with image tag
    slides_with_image <- sum(grepl('<img', slides))
    result <- round((slides_with_image / total_slides) * 100, 2)
  } else {
    stop("Unknown metric: choose 'total_slides', 'code', or 'images'")
  }

  return(result)
}

# Optionally, to avoid manual work:
# create_tool_def(calculate_slide_metric)
calculate_slide_metric <- tool(
  calculate_slide_metric,
  "Returns the calculated metric value",
  metric = type_string(
    'The metric to calculate: "total_slides" for total number of slides, 
      "code" for percentage of slides containing fenced code blocks, or "images"
      for percentage of slides containing images.',
    required = TRUE
  )
)

# Initialise chat with Claude Sonnet 4 model
chat <- chat_anthropic(
  model = "claude-sonnet-4-20250514",
  system_prompt = system_prompt,
  params = params(
    temperature = 0.8 # default is 1
  )
)

# Register the tool with the chat
chat$register_tool(calculate_slide_metric)

# Start conversation with the chat
# Task 1: regular chat to extract meta-data
chat$chat(
  interpolate(
    "Execute Task 1 (counts). Here are the slides in Markdown: {{ markdown_content }}"
  )
)

# Task 2: structured chat to further analyse the slides
chat$chat_structured(
  "Execute Task 2 (suggestions)",
  type = type_deck_analysis
)
```

</details>
</div>
<div id="tabset-14-3">
<details class="code-fold">
<summary>Show full prompt</summary>

``` python
"""
You are a presentation coach for data scientists that analyses presentation slide decks written in Markdown. 
You extract key information, evaluate quality, and return structured feedback that is constructive, focused and practical.

The presentation you are helping with is a {{ length }}-minute {{ type }} at {{ event }}.  
The audience is {{ audience }}. 

You can be asked for one of the following tasks. Each has a number and a name:

# Task 1 (counts)

You extract the following information:
- The number of slides
- The percentage of slides containing code blocks
- The percentage of slides containing images 

Return only the JSON results, nothing else.

# Task 2 (suggestions)

You extract the following information:
- The presentation title
- Estimated presentation length (in minutes, assuming ~1 minute per text slide and 2–3 minutes per code or image-heavy slide)
- Tone (a brief description)

You score the presentation on the following categories (from 1–10), and give a concise explanation:

1. Clarity of content: evaluate how clearly the ideas are communicated. Are the explanations easy to understand? Are terms defined when needed? Is the key message clear?
2. Relevance for intended audience: assess how well the content matches the audience’s background, needs, and expectations. Are examples, depth of detail, and terminology appropriate for the audience type?
3. Visual design: judge the visual effectiveness of the slides. Are they readable, visually balanced, and not overcrowded with text or visuals? Is layout used consistently?
4. Engagement: estimate how likely the presentation is to keep attention. Are there moments of interactivity, storytelling, humor, or visual interest that invite focus?
5. Pacing: analyze the distribution of content across slides. Are some slides too dense or too light? 
6. Structure: review the logical flow of the presentation. Is there a clear beginning, middle, and end? Are transitions between topics smooth? Does the presentation build toward a conclusion?
7. consistency: evaluatue whether the presentation is consistent when it comes to formatting, tone, and visual elements. Are there any elements that feel out of place?
8. Accessibility: consider how accessible the presentation would be for all viewers, including those with visual or cognitive challenges. Are font sizes readable? Is there sufficient contrast? Are visual elements not overwhelming?

For each of the above scoring categories, provide specific and actionable improvements. Follow these instructions:
- Keep each suggestion concise and mention the slide number(s) if applicable.
- Do not invent issues and only suggest improvements when the content would clearly benefit from them.
- For each catogory, estimate what the new score would be if these improvements are implemented.
- Return the improvement and new score as part of the response for that category.

You bundle your results with the results from the first task. Always return the result as a JSON object that conforms to the provided data model.
"""
```

</details>
</div>
</div>

But there's one questions that might still be lingering in your mind: how much does this cost?!

# Understanding tokens and costs

Back to our nightmare from the beginning: a bill with a lot of zeros for using an LLM. Luckily you can prevent this pretty easily and it all starts with understanding how and for what you're being charged.

Whenever you talk to an LLM, you're essentially paying for how much you say and how much it says back. Responses are all measured in tokens, those small chunks of text we talked about in Part 1 of this series. For every x amount of tokens, you pay a particular price. For example, at the time of writing, [Claude Sonnet 4](https://docs.anthropic.com/en/docs/about-claude/pricing) has a price of 3 USD per million tokens for input, and a price of 15 USD per million tokens for output.

When talking about costs it's important to understand that you pay for both input and output. That means you're billed for what you send and for what the assistant replies with. So if you ask a really long question and get a really long answer, that's going to cost more than a question that requires a yes or no answer.

This is why your prompt and structure matters. If you keep repeating the same context or include an entire Quarto presentation each time you make a call, your token count will add up fast. Remember that the history is send to the LLM with every subsequent question! A deeply nested chat history can cause costs to go up quickly. This is also true for very long system prompts. Therefore, it's often worth trimming what you send, summarising where possible, and being intentional about what the model really needs to see. There's a fine balance between giving as much context as possible for the best possible response, and making sure you're not overdoing it.

Manually keeping track of your tokens would be annoying, so with `chatlas` or `ellmer`, you've got a few handy functions to help estimate token use:

- `get_tokens()` gives you a raw count of how many tokens you've used so far.
- `get_cost()` gives you an estimate of how much your chat might cost. Note how it says "estimate". Model providers can change their pricing overnight, and there might not even be a heads-up. This estimate therefore serves as a rough guide, not the truth.

Now for the real thing you want to know: for our full workflow, we pay around 0.06 USD.

<div class="panel-tabset" data-tabset-group="language">
<ul id="tabset-15" class="panel-tabset-tabby">
<li><a data-tabby-default href="#tabset-15-1">Python</a></li>
<li><a href="#tabset-15-2">R</a></li>
</ul>
<div id="tabset-15-1">

``` python
chat.get_tokens()
chat.get_cost()
```

``` python
[{'role': 'user', 'tokens': 3611, 'tokens_cached': 0, 'tokens_total': 3611},
 {'role': 'assistant', 'tokens': 133, 'tokens_cached': 0, 'tokens_total': 133},
 {'role': 'user', 'tokens': 102, 'tokens_cached': 0, 'tokens_total': 3846},
 {'role': 'assistant', 'tokens': 52, 'tokens_cached': 0, 'tokens_total': 52},
 {'role': 'user', 'tokens': 2435, 'tokens_cached': 0, 'tokens_total': 6333},
 {'role': 'assistant', 'tokens': 947, 'tokens_cached': 0, 'tokens_total': 947}]
```

``` python
0.058350000000000006
```

</div>
<div id="tabset-15-2">

``` r
chat$get_tokens()
#>1      user   3552         3552
#>2 assistant    148          148
#>3      user    101         3801
#>4 assistant     48           48
#>5      user   1839         5688
#>6 assistant    932          932

chat$get_cost()
#>[1] $0.06
```

</div>
</div>

> **Costs differ between runs!**
>
> Token counts and cost vary because the answers of the LLM vary too (thanks to the creativity of the model).

In our case, we might be working with pretty long Quarto presentations. The bigger the presentation, the more tokens our input will have. So far, we only played around with a demo presentation for a 10-minute talk, and basically put everything in one prompt. But we might have subsequent questions to the LLM, too. Overall, there are two strategies that can be used to reduce token count and cost:

1.  Batching: instead of sending multiple small calls, combine them into a single, well-structured one when possible. It reduces overhead and often results in fewer total tokens. Keep it DRY to: don't repeat yourself by providing information twice. For example, when using structured output it's not strictly necessary to put all the specifications for the output in the prompt itself too. And it shouldn't be a surprise, but batching is also possible in `ellmer` with [`batch_chat()`](https://ellmer.tidyverse.org/reference/batch_chat.html) and (soon!) in `chatlas` with a similar function.
2.  Summarising: if you're feeding in the same context repeatedly, have the model summarise it first. Then reuse that summary instead of the full text. It's a small change that can lead to big savings.

Every token counts. And if you want to build something that scales, getting a grip on your usage early can save you a lot down the road.

# What's next

The output that we are currently receiving is nice, but it's not something that would amaze our users. For us humans, it's annoying to read information from JSON as well. We need something different. To really get a wow-effect we need to design an appealing user interface. We need to make it easy for users to upload their content, give us additional information (aka our required variables), and analyse the results. Nobody likes a boring static app, so we need to add some shiny interactive features as well. And those shiny interactive features? That's a perfect job for Shiny!

In this part of "The Shiny Side of LLMs" we built a foundation for our Shiny app: using either `chatlas` (Python) or `ellmer` (R) we can now analyse any Quarto presentation. Our current workflow allows us to:

- Convert a Quarto file to plain markdown (and HTML), which can easily be consumed by an LLM
- Call any LLM from any (or ok, most) providers through their API (our chosen model being Claude from Anthropic). Thanks `chatlas` and `ellmer`!
- Send a carefully crafted prompt that guides the LLM to analyse the markdown content
- Let the LLM use a tool to accurately calculate some metrics
- Tweak model parameters if we really want to go the extra mile
- Receive consistent, structured and useful JSON output that we can use in our Shiny app

The only thing left to do? Wrap it in that Shiny interface. See you in the third and last part of "The Shiny Side of LLMs" series!
