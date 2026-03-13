---
title: What LLMs Actually Do (and What They Don’t)
description: >
  Welcome to The Shiny Side of LLMs: a blog series explaining large language
  models

  in plain English, without the fancy and difficult buzzwords. In this first
  part:

  what LLMs are, how they work, what they’re good at, and why they don't
  magically solve all your problems.
people:
  - Veerle Eeftink - van Leemput
date: '2025-07-31'
image: shiny-side-of-llms-header.png
image-alt: The Shiny Side of LLMs part 1
resources:
  - shiny-side-of-llms-header.png
  - shiny-side-of-llms-back-propagation-1.png
  - shiny-side-of-llms-back-propagation-2.png
  - shiny-side-of-llms-stats.png
  - shiny-side-of-llms-chat.png
  - shiny-side-of-llms-code-gen.png
  - shiny-side-of-llms-image-gen.png
ported_from: shiny
port_status: in-progress
---


# Welcome to the Shiny Side of LLMs!

Large language models (LLMs) are everywhere, and we're way beyond denying their existence.
New use cases pop up every single day, from autocompleting code to customer support bots, summarisers, and tutors.
And everybody feels the urge to jump in.
Tools like ChatGPT, Claude, and GitHub Copilot have made us all comfortable using AI.
But when it comes to building something that is tailored, interactive, and actually useful for others, it all starts to feel... muddy.
Buzzwords start flying: embedding, encoding, RAG, vector databases, streaming tokens... and suddenly you're wondering if this is still for you.

Spoiler alert: it is, and it's all more accessible than it seems.
Yes, the underlying technology is complex, but that doesn't mean it's out of reach.
For the first time, you have easy access to something that mimics human reasoning.
As a programmer, that means you can describe a problem in plain language and get useful output: code, explanations, ideas, or even full analyses.
And you don't need to train your own models or master deep learning theory to use it.
You just need to understand what's happening under the hood well enough to start building.
In this blog series, we'll demystify all the buzzwords and walk you through:

- What LLMs really do, conceptually and technically, but explained super simply
- How to interact with them while staying in your comfort zone (Python or R)
- How to turn those interactions into real, usable tools using Shiny (again: Python or R)
- The magic of mixing in your own data such as documents, notes, and anything else you use

This isn't just about building a chatbot.
It's about understanding how things work and how you can use an LLM to build your own tools.
A document summariser, a smart search assistant, or a decision helper for your team: the choice is yours.
We'll go step by step.
From "zero" (I've only ever typed things into ChatGPT) to "hero" (I've built my own LLM-powered app and I understand how it works).

No need to know anything about model hosting, server clusters, or fancy acronyms.
Just you, some Python or R, and a fun idea!

> **What can you expect from this first part?**
>
> This is Part 1 of "The Shiny Side of LLMs" series: *What LLMs Actually Do (and What They Don't).* It is intended to give you some insight into how LLMs work under the hood.
>
> You don't *need* to know all this to start building things.
> But having a basic understanding of the mechanics can help you reason more clearly about what LLMs are (and aren't) good at and avoid getting lost in the hype.

# The "Large", the "Language", and the "Model"

> **TL;DR**
>
> When we talk about a "Large Language Model", we're really talking about a system trained on huge amounts of text, designed to predict and generate human-like language, powered by a model that recognises patterns at scale.

First things first, what is a Large Language Model?
A good first step is breaking down the term "Large Language Model".
Let's do it backwards, starting with the last word: "Model".
In this context, a model is a statistical system that learns patterns from data and uses them to make predictions.
Yes, that's right: plain old statistics.

When we're talking about a "Language Model" we make predictions about a language, consisting of sentences and its words.
It all boils down to the likelihood of a next word, or sequence of words.
A language model is trained to understand the kinds of words that tend to appear together, how sentences flow, and how meaning is built from context.
Early models could only guess a single word at a time and struggled with anything longer or more complex, but modern ones can generate entire paragraphs or documents that stay on topic and sound surprisingly coherent.
Almost like a human.

Bigger is better.
The "Large" in "Large Language Model" refers to both the amount of data the model is trained on and the number of parameters it has (the internal settings the model adjusts as it learns).
The "larger" a model is, the more patterns it can recognise and the more fluent its outputs tend to be.

So what does that mean when you interact with one?
When you ask an LLM something, you prompt it to do something (that's why the input or text you type is also called a prompt).
That something is to predict the most likely sequence of words based on the sequence you have given.

> **LLMs and AI**
>
> You didn't see much mention of Artificial Intelligence (AI) yet, and that's on purpose.
> While LLMs are a specific kind of AI, they're just one part of a much broader field.
> But since LLMs are the most visible (and frankly, the most hyped) examples of AI right now, people often use the terms interchangeably.
> To keep things focussed, we'll only use the term LLM here.

# How LLMs learn

We can talk about LLMs like they're the newest thing, but the foundation is still as "ancient" as statistics.
It's about understanding data: making inferences, finding patterns, estimating (un)certainty.
Machine Learning (ML) is statistics, and ML models learn patterns from data.
Think about algorithms like decision trees, support vector machines, and linear regression that all rely on the same idea: learning from examples.

LLMs learn through a technique called deep learning, which is a subfield of ML.
At the core of deep learning are neural networks: mathematical structures loosely inspired by biological neurons within the brain.
You can think of them as layers of tiny decision-makers, where each layer takes in numbers, transforms them, and passes them on to the next.

Each connection between layers has a weight, aka a number that determines how strongly one "neuron" influences another.
During training, the model adjusts these weights millions (or billions) of times to reduce the gap between its predictions and the actual data.
This process is called back propagation, and it's basically a giant optimisation loop: the model makes a guess, sees how wrong it was, tweaks the weights, and tries again.
Over time, it gets surprisingly good at spotting patterns in language.

![](shiny-side-of-llms-back-propagation-1.png)

<figure>
<img src="shiny-side-of-llms-back-propagation-2.png" alt="A simplified explanation of back propagation in neural networks" />
<figcaption aria-hidden="true">A simplified explanation of back propagation in neural networks</figcaption>
</figure>

The bigger the model, the more opportunities it has to learn how to make good guesses.
That's why the "Large" in "Large Language Model" is so important.
In the last few years, model size and model capability has exploded.
This is due to hardware improvements (something has to crunch all that data), better training techniques and something called transformers.
Ah, jargon.

A transformer is a kind of model architecture.
"Model architecture" sounds difficult, but in simple terms this is a blueprint for how a model processes and learns from data.
It was introduced by [Vaswani et al. (2017)](https://arxiv.org/pdf/1706.03762).
Transformers are part of the neural network family, and they're designed to handle huge amounts of data quickly and efficiently, which makes them perfect for crunching lots of text.

What made transformers such a game-changer is a clever idea called attention.
Instead of reading text word by word like older models, transformers look at the whole sentence (or paragraph) at once and figure out which words matter most to each other.
That's how large language models can generate surprisingly accurate, context-aware text.

They also made it possible to train on much bigger chunks of data and pick up more subtle patterns in language.
This is combined with a technique called self-supervised learning, where the model learns to predict missing words in sentences.
If you show it "I lifted some \_\_\_" it learns that "weights" is more likely than "horses".
Because the data itself provides the training signals, we don't need humans to label anything.
That makes training scalable.
It doesn't mean it's totally label-free, though.
The "labels" (like missing words) just come naturally from the text.

The combo of smart architecture and massive training data is what unlocked the big leap in quality of today's LLMs and made models like ChatGPT possible.
Fun fact: the "T" in GPT stands for Transformer.
Now you know why that is!

From statistics to transformers, to models we can chat with and help us to get things done faster.
How's that for the "ancient" statistical techniques?!

<figure>
<img src="shiny-side-of-llms-stats.png" alt="It all starts with statistics" />
<figcaption aria-hidden="true">It all starts with statistics</figcaption>
</figure>

It all sounds too good to be true: a model that learns on its own, getting "smarter" with every chunk of input you provide.
And it indeed is, because with this self-supervised learning come challenges too.
As more online text is generated by LLMs, there's a risk the model ends up learning from itself.
It's like copying a copy: input gets blurry.
And in the end LLM are just models that predict something based on the data it has been given.
If that data is garbage, so is the outcome.
If we don't want to end up with boring, soulless, similar, and even incorrect content, we still have to write content ourselves.

Still, one thing is clear: what makes LLMs so powerful is the amount of data they learn from.
And that leads us straight into the magic of scale.

# The magic of scale

As LLMs are trained on more and more data, something cool happens: they begin to show emergent abilities ([Wei et al., 2022](https://doi.org/10.48550/arXiv.2206.07682)).
These are skills the model wasn't directly trained for, yet still manages to do.
Nobody explicitly programmed an LLM to summarise text, translate between languages, or generate code.
But once the model is large enough and has seen enough examples, these abilities just... emerge.
Magic!

This is different from what we call generative abilities.
"Generative" simply means the model can generate new text.
All LLMs are generative and can produce new text.
You give them a prompt, and they predict what comes next.
That's their basic job and it's expected behaviour.
Emergent abilities were not in the original job description and the model just suddenly gets good at tasks nobody told it to do.
It's surprising behaviour.

For example, you can ask it to convert a sentence into pirate-speak, even if it was never explicitly trained to do that.
It uses general language patterns it has learned to give it a try, which is known as zero-shot learning.
And if the model struggles to understand what you want, you can help it by giving a few examples in your prompt: few-shot learning.
If you want a list reformatted in a certain way, you can provide some examples and let the LLM finish the rest.

All of this is possible not because the model is "intelligent" in a human sense, but because it has seen so much text and learned such general patterns that it can apply them in all kinds of situations.
This ability to generalise, or doing more with less instruction, is one of the most powerful outcomes of large-scale learning.

# What LLMs aren't

So you might think LLMs are pretty smart.
After all, they can write essays, answer questions, and even debug your Python and R code.
It's the shiny side of LLMs.
But it isn't all rainbows and unicorns: LLMs aren't smart and they aren't thinking.
LLMs don't reason like humans.
They don't understand what they're saying.
They don't "know" facts in the way we do.
What they do is predict the next word in a sentence, based on patterns they've seen in massive amounts of text.

That means an LLM can be confidently wrong.
They might "hallucinate" an answer that sounds plausible but is completely made up.
The code it generates might look solid, but when you actually run it you notice that it contains packages that don't exist or variable names that were never defined.
They might reflect or even amplify biases in their training data.
They might sound accurate, but miss the mark entirely.
And crucially, you don't really control them.
You can't force an LLM to always give a safe or correct answer.
What you can do is guide it with better prompts, build tools around it that check its output, and design systems that use the model responsibly.

So while LLMs are great at generalising across tasks, that power doesn't come from intelligence.
It comes from scale.
And that is important to remember when building with LLMs.

# Let's talk about context

As mentioned earlier, LLMs can understand and generate surprisingly accurate, context-aware text.
And that context deserves some attention (literally: remember transformers!).
It's the context that makes sure an LLM doesn't blurt out random sentences (or, ok, only occasionally do).
But what does "context" actually mean for a Large Language Model?

It all starts with tokens, which are tiny chunks of text.
A token can be a word, a part of a word, or even just characters or punctuation.
Every time you type something into an LLM, your input is split into these tokens.
Depending on the model, an LLM can "see" a certain number of tokens at once.
This is called the context window.
Think of it like a sliding window over a long scroll of text.
The model can only see what fits inside that window.
If your input is too long and tokens fall outside of that window: too bad.
An LLM might trims the beginning or the end and hopes you didn't put anything important there.
The exact behaviour varies by provider and how the system around the model is designed.
Some providers implement strategies like summarising or condensing previous conversation history, while others simply drop older messages to make room for new ones.
And in some cases, the system might reject the request outright rather than attempt to process an incomplete prompt.

But wait... We previously learned LLMs were trained on all of language right?
Yes.
But at generation time, it doesn't remember everything it's ever seen.
It only has this input, right now, and the tokens inside the window.
That's its entire world.
There's no long-term memory (unless you've built that in, we'll get to that later).
So if you want the model to give you a good answer, what you say really matters.
And that's not the only thing: it also matters how you say it.

Imagine these two prompts:

    1. “Create a Shiny for Python app that plots a histogram of random numbers”
    2. “Plot a histogram of random numbers. Use Shiny for Python.”

Same words.
Different order.
Potentially different behaviour.

Language models are super sensitive to the flow of a sentence.
If you put instructions at the start, the model is more likely to follow them.
Bury them at the end, and it might treat it more like a side-note.
Clarity is an LLMs best friend.

So context isn't just about what's in the window.
It's also about where words are and how they're phrased.
Order and surrounding words matter.
In the model's brain, each token looks around (thanks to that attention trick you met earlier) and asks, "who's standing next to me, and what story are we telling?"
Those neighbouring words:

1.  **Disambiguate meaning:** words on their own only say so much. "Bass" is a fish next to "river", and a guitar next to "band."
2.  **Signal tone:** a single word can flip the sentiment. For example, "nice" after "not". On its own, the word "nice" would be positive.
3.  **Set expectations:** since a model is trained on sequences of tokens actually written by humans, some sequences are familiar. So after "Once upon a" the model is primed for "time," not "ship".

Because the model predicts the next word by weighing everything it can see in the window, every surrounding word tweaks the odds.
Change one word, and the whole probability landscape shifts.
This becomes clear with these different prompts:

    1. “Write a short horror story about a clown”
    2. “Write a funny short horror story about a clown”

Can you already sense why "prompt engineering" became so hot?

Now back to the memory thing.
Out of the box, the model doesn't "remember" what you said three chats ago.
It doesn't even remember what you said two messages ago, unless you send the whole chat history in the current prompt.
So how big a prompt can get, determines how much an LLM can remember.
This brings us back to the context window.
The maximum number of tokens they can handle at once matter.
It could be 2000 or 128000 tokens.
That all depends on the model.
If your conversation gets longer than the model can hold, the oldest messages get chopped off.
That's why in very long chats, you might notice an LLM starts "forgetting" early facts.
These facts are not in the context window anymore, so the model can't "see" them anymore either.

<figure>
<img src="shiny-side-of-llms-chat.png" alt="Ok, this isn’t a “very long” chat, but you get the idea: whatever is outside the context window is “lost” information" />
<figcaption aria-hidden="true">Ok, this isn’t a “very long” chat, but you get the idea: whatever is outside the context window is “lost” information</figcaption>
</figure>

It is possible for models to have access to persistent memory across conversations, but in that case facts and knowledge have to be explicitly stored somewhere.
This memory is separate from the context window.
Whether and how that memory gets updated depends on the broader system designed by the LLM provider.
This system, the surrounding infrastructure and logic around the model, determines what's worth saving.
Only if something seems important enough the memory will be updated.

# From tokens to embedding to encoding

Your prompt is divided into tokens, those tiny chunks of text.
But computers don't "understand" words like we do.
Computers work with numbers.
That's where something fancy called "embedding" comes in: each token is turned into numbers that represents its meaning.
And these numbers are not a plain "4982" or "2974", but rather a pattern of numbers.
You can compare it with an unique barcode.
To "understand" your prompt, the model looks at all these number patterns together and uses the earlier mentioned attention to figure out how they relate to each other and what the relationship between the words is.
This process is called encoding.
A well-known model that does this is BERT, which was introduced by Google in 2018 ([Devlin et al., 2019](https://doi.org/10.48550/arXiv.1810.04805)).

Because of word embeddings and encoding, a prompt like "Create a Shiny for Python app that plots a histogram" is not just a set of random words.
The model knows that "Shiny" and "Python" relate to things like "web app" or "dashboard" because their embeddings are close together.
It gives the model directions on the tech stack to use.
It also sees that "plot" and "histogram" are both in the prompt, so it understands you want a chart.
And the word "create" signals that you're asking for code, not just an explanation.
All these relationships, links and signals are taken into account when generating the output token by token.

<figure>
<img src="shiny-side-of-llms-code-gen.png" alt="From input to output: how an LLM generates code" />
<figcaption aria-hidden="true">From input to output: how an LLM generates code</figcaption>
</figure>

So far, we only talked about generating language, like plain text or some code.
But what about images?
The latest models can take images as input and they spit out a polished (perhaps fake-looking) image when being asked too.
These multimodal models (like GPT-4o or Claude 3) combine both vision and language.
How?
By treating images like language!

> **Images and multimodal models**
>
> When talking about images, we're taking a small side-step in our LLM journey.
> Image tasks are typically handled by specialised models (like diffusion models for image generation) or by multimodal LLMs (like GPT-4o or Gemini) that can process both text and images.
> So when we talk about "LLMs" generating or understanding images, we're really referring to LLMs with extra capabilities.

Just like text is broken down into tokens, images are also converted into a form the model can understand.
Instead of words, an image is split into patches (tiny chunks of pixels).
You can think of this as "tokenizing an image." And just like tokens, patches are turned into numbers that capture the meaning of those pixels, which brings us back to the fancy word: "embedding".
These image embeddings are then processed by the model just like text embeddings.
That's how a model can look at an image and describe it or answer questions about it.

Generating new images is also not a problem: in that case embeddings are translated to a visual representation (pixels) and a full image is being built from it.
This is exactly what well-known generative vision models like DALL·E, Midjourney, or Stable Diffusion do: they're trained to turn a sequence of text tokens into a sequence of image tokens, gradually "painting" a picture that matches the prompt.
If we ask Stable Diffusion for "A weightlifting Dalmatian holding a barbell with red plates", it has no problem doing so.
It's all about processing the embeddings together and figure out how every word relates to each other.
In this case, "weightlifting" modifies what the "Dalmatian" should look like, and "holding" links "Dalmatian" and "barbell".

<figure>
<img src="shiny-side-of-llms-image-gen.png" alt="Generating images works pretty similar to generating language for LLMs with those extra capabilities" />
<figcaption aria-hidden="true">Generating images works pretty similar to generating language for LLMs with those extra capabilities</figcaption>
</figure>

Note that depending on the model you're using, you might need to provide more context in your prompt by saying something like "Generate an image that shows...".
This is especially important for multimodal models, like GPT-4o or Gemini, which can generate text, images, audio, and more.
A prompt like "A weightlifting Dalmatian holding a barbell with red plates" might seem clear to you and me, but to a multimodal model, it could mean several things: perhaps you want an image, or a description, or a funny meme.
This is different for a model like Stable Diffusion, a text-to-image model, which is trained specifically for image generation.
Naturally it will assume you want an image when you give it a prompt.

# More jargon: RAG and vector databases

LLMs can only generate such "human-like" language because they are good at embeddings, encodings, and understanding context.
Context is everything.
This context comes from the "knowledge" an LLM has, or from you.
On their own, LLMs can only use data that has been used during training to generate output.
LLMs only "know" facts that happened during their training process (and not after), and proprietary information is off limits.
That doesn't mean you can't let an LLM use new facts, or private company info.
You can add it to the context, taking the context window into account.
So what do you do when you want to add so much information that it doesn't fit that window?
Hello, RAG!

It's probably not the first time you encountered the term "RAG".
RAG stands for Retrieval-Augmented Generation ([Lewis et al., 2020](https://doi.org/10.48550/arXiv.2005.11401)).
It means that instead of relying only on what the language model was trained on, it first retrieves relevant information (like from a document or database) and then generates a response using both your prompt and that retrieved info.
This helps the model give more accurate and up-to-date answers.

"Retrieving information" sounds simple when you just have one document, but imagine you have a big pile of documents.
That's a bit more complicated.
To make retrieval easier, RAG systems usually break documents into smaller chunks, like paragraphs or even sentences.
Each chunk gets turned into a vector and stored in a vector database.
When you ask a question, the system searches for the chunks whose vectors are closest in meaning to your query and uses those to be added to the context.
It's all about making the most of the context window.

# So many models

We're not talking about one big giant LLM in this blog series.
It's plural: LLMs.
That's because there are a lot of different LLMs out there.
All these models are trained a little differently.
That's important, because how a model is trained (what and how many data it saw, what tasks it practiced, what architecture it uses) shapes what it's good at.
Some models are trained mostly on text (think books, articles, web pages), while others are trained more heavily on code (like GitHub repos).
That's why some models might be better suited as your coding-companion, and others may serve you well as your ghostwriter.

There are many ways to compare LLMs, but here are few things you might want to consider:

- **Context window**: larger windows help with long documents or multi-turn conversations.
- **Training data**: what kind of data the model was exposed to (e.g. text, code, math problems, dialogue, or some mix).
- **Instruction tuning**: some models are trained to follow prompts more precisely, often using human feedback (this has a very lengthy name: Reinforcement Learning from Human Feedback, aka RLHF).
- **Output quality**: ah, there it is! Probably the the most important thing. How good are the model's answers?! This depends on everything above, plus things like formatting ability, reasoning steps, or hallucination rates.
- **Cost and speed**: we'll come back when actually talking to LLMs, but not all models are priced equally, and speed can vary a lot.

Since output quality is probably one of your top priorities, you might wonder how you can quickly get a sense of LLM performance.
You can try out different models, sure.
But as a data-savvy person you're probably keen to turn towards a more objective method.
Luckily, there are tools like [llm-stats.com](https://llm-stats.com/), [Vellum's leaderboard](https://www.vellum.ai/open-llm-leaderboard), and [LM Arena](https://lmarena.ai/leaderboard) that help you with a comparison.
The latter is based on subjective human ratings of output quality across tasks.

Looking at these leaderboards you see all the popular models like GPT (OpenAI), Claude (Anthropic), Gemini (Google), Llama (Meta), DeepSeek, Mistral and Nemotron (NVIDIA).
And all of these models have different versions too!
It might spin your head.
Each model has strengths and weaknesses.
Some are better with long input, some are cheaper, some are open source... But honestly, don't stress too much about picking the "perfect" one.
Once you start integrating an LLM into your Shiny app, it's easy to change models later if you need to.
At this stage, it's more important to just get started.

When it comes to personal experience and "word on the street" from Python and R developers: with Claude you're generally good when it comes to writing code (e.g. as a copilot) and summarising text.
If you're looking for a model with a large context window, Gemini might be what you would be after.
And your friendly neighbourhood LLM could potentially be found in GPT models (like GPT-4o) which generally have a good balance between reasoning, code, and creative tasks.

# Building with LLMs

LLMs can be applied in a wide range of natural language tasks.
They're perfect for building chatbots or virtual assistants.
They can generate content, which can be blog posts, emails, or code snippets.
They can handle machine translation across languages, summarise long reports into key points, and perform sentiment analysis to extract opinions or emotional tone from text.
They even can do data analysis for you.

It's worth recognising that the examples above can have multiple use cases: you can use LLMs to increase your own productivity, or you can move from using an LLM to building with one.
As a copilot, an LLM can help you write code, draft content, summarise documents, or generate ideas, which (hopefully) makes you faster and more efficient in your day-to-day work.
But when you start building tools for others, the focus shifts.
Now it's not just about what the model can do, but how you wrap it in a helpful interface.
You need to think about the user's problem, how they interact with your tool, and how to guide their input to get meaningful results.
That's a different kind of challenge.
And this is exactly where something like Shiny shines.
Whether you're using Python or R, Shiny makes it easy to build interactive, user-friendly applications that connect to an LLM behind the scenes.
You can quickly prototype ideas, test interfaces, and deliver real value.
It's the perfect bridge between your data science skills and creating practical tools powered by LLMs.
The only thing you need is a bit of creativity, some coding skills, and a foundational understanding of LLMs.
The latter we tackled already!

So what are we going to build in this blog series?
Imagine you need to present something to your colleagues in the development team, you're a little nervous and would like to have some feedback on the presentation first.
Since you're a data scientist who loves reproducible slides, you've chosen to build a [Quarto presentation](https://quarto.org).
Wouldn't it be wonderful if you could upload your slides in an app and get instant feedback?
Like the perfect "Presentation Rehearsal Buddy" that analyses your slides and gives you tailored suggestions?
And wouldn't it be great if you can help other data scientists with the same problem?
You can even prevent your colleagues from giving too lengthly and unfocussed presentations.
Also, it's great for polishing your talks at conferences, like [posit::conf(2025)](https://posit.co/conference/).
Now that's a cool app!

And it's the kind of thing you can actually start building now you understand what LLMs can and can't do.
But wait... I can feel your creativity flowing, the app idea growing on you, and I understand you might be dreaming bigger.
Maybe a model trained on your own (sensitive) company data to really tailor presentations to your work?
Amazing!
You probably heard it's not the best idea to send sensitive data to just any public API, so your mind jumps to a local LLM: one that runs on your own machine(s), just for you.
A private model that knows everything about your org... That's tempting!
And while it sounds wonderful, it's probably not the best place to start.

Running your own LLM comes with lots of complexity: infrastructure, cost, fine-tuning, and security.
It's a bit like buying a race car before learning to drive, then trying to build the track and engine from scratch.
A better place to begin?
Use the best pre-trained models that are already available.

And remember the magic of scale: LLMs show their real power only when trained on massive amounts of data and compute.
That's where those emergent abilities come from.
Why reinvent the wheel when you can just take it for a spin?
There's a reason why the best performing models can't be run on a laptop!

# Responsible use and regulations

Ready, set, ... disclaimers.
Damn.
This is not an ethics class.
We're here to code.
But we can't get around some disclaimers, and if you're using an LLM, you should take some things into account when it comes to responsible use:

- Perhaps this goes without saying, but you can't bluntly copy and paste data or (sensitive) information into any LLM. That means your own data, and somebody else's data. Generated or uploaded input (text, data, prompts, images, etc.) could (and will) be used for other purposes, such as the training of AI models. If you don't want things to be out in the open, you shouldn't input it unless you're really sure that data will not be re-used.
- You can't trust an LLM completely either. You must always take a critical approach to using the output produced and be aware of the limitations, such as bias, hallucinations and inaccuracies.
- You're accountable for the integrity of the content generated by or with the support of an LLM. There's also an important difference between *using* an LLM for your own tasks and *building* tools on top of LLMs that others will rely on. In the first case, you're the human in the loop, judging what to trust and what to ignore. But when others interact with your app, you're responsible for the entire experience: how the model is prompted, how outputs are presented, and whether users are warned of uncertainty. In any case, if you use an LLM to make decisions or build an app that others use to act upon, you can't blame the LLM for giving false directions.

Many organisations know this too, and it makes them wary of using LLM-based tools.
Especially in regulated environments, there's a natural hesitation to adopt these tools without strong safeguards in place.
If you want your organisation to be open to the idea, you need to think about clear data handling policies, usage boundaries, a transparent explanation of how the model is prompted, what kind of outputs are produced, and where the limitations lie.
The more control and clarity you can offer, the more trust you'll build.

If your organisation already trusts a cloud vendor like AWS, Azure, or Google Cloud with your data, then using an LLM hosted by that same vendor often fits within existing security and compliance frameworks, which might make it easier to justify adoption.

It's also good to be aware of applicable regulations and guidelines.
Know what you can and can't use an LLM for when building your application.
For example, in Europe, there's the [AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai) (which is the first-ever legal framework on AI).
Generally speaking, legislation is not that fast, but since AI capabilities are quickly expanding it's only a matter of time before rules and guidelines do catch up.
Stay informed!

And with those less fun but necessary warnings we wrap up this introduction to LLMs.
It's not a magic all-mighty black box anymore: you now know exactly what LLMs are and what they are not.

# Coming up: talking to LLMs

Our app for polished Quarto presentations is just around the corner, but before we can build it, we need to learn how to actually talk to an LLM.
Programmatically that is.
After all, the magic only happens once you know how to send the right prompts, pass along the right content, and make sense of what comes back.
In our case, that means: extracting a presentation's content, feeding it to the model with smart prompts, and formatting the output into something useful.
Think about value boxes, improvement tips, or even edits to your Quarto file directly.
That's where we're headed.
But first, the next step in our app-building journey: talking to an LLM.

# References

Devlin, J., Chang, M. W., Lee, K., & Toutanova, K.
(2019).
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.
*arXiv.* <https://doi.org/10.48550/arXiv.1810.04805>

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D.
(2020).
Retrieval‑augmented generation for knowledge‑intensive NLP tasks.
*arXiv*.
<https://doi.org/10.48550/arXiv.2005.11401>

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I.
(2017).
Attention is all you need.
*arXiv*.
<https://doi.org/10.48550/arXiv.1706.03762>

Wei, J., Tay, Y., Bommasani, R., Raffel, C., Zoph, B., Borgeaud, S., Yogatama, D., Bosma, M., Zhou, D., Metzler, D., Chi, E. H., Hashimoto, T., Vinyals, O., Liang, P., Dean, J., & Fedus, W.
(2022).
Emergent Abilities of Large Language Models (Version 2).
*arXiv.* <https://doi.org/10.48550/arXiv.2206.07682>
