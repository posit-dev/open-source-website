---
title: "What are Large Language Models? What are they not?"
description: |
  This is a high-level, introductory article about Large Language Models (LLMs), the core technology that enables the much-en-vogue chatbots as well as other Natural Language Processing (NLP) applications. It is directed at a general audience, possibly with some technical and/or scientific background, but no knowledge is assumed of either deep learning or NLP. Having looked at major model ingredients, training workflow, and mechanics of output generation, we also talk about what these models are not.
date: 2023-06-20T00:00:00.000Z
slug: keydanallm
categories:
  - Meta
  - Concepts
  - Natural Language Processing
author:
  - name: Sigrid Keydana
    affiliation: Posit
    affiliation_url: https://www.posit.co/
people:
  - Sigrid Keydana
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
---



> "At this writing, the only serious ELIZA scripts which exist are some which cause ELIZA to respond roughly as would certain psychotherapists (Rogerians). ELIZA performs best when its human correspondent is initially instructed to"talk" to it, via the typewriter of course, just as one would to a psychiatrist. This mode of conversation was chosen because the psychiatric interview is one of the few examples of categorized dyadic natural language communication in which one of the participating pair is free to assume the pose of knowing almost nothing of the real world. If, for example, one were to tell a psychiatrist "I went for a long boat ride" and he responded "Tell me about boats", one would not assume that he knew nothing about boats, but that he had some purpose in so directing the subsequent conversation. It is important to note that this assumption is one made by the speaker. Whether it is realistic or not is an altogether separate question. In any case, it has a crucial psychological utility in that it serves the speaker to maintain his sense of being heard and understood. The speaker furher defends his impression (which even in real life may be illusory) by attributing to his conversational partner all sorts of background knowledge, insights and reasoning ability. But again, these are the speaker's contribution to the conversation."
>
> Joseph Weizenbaum, creator of ELIZA (Weizenbaum 1966).

GPT, the ancestor all numbered [GPTs](https://en.wikipedia.org/wiki/Generative_pre-trained_transformer), was released in June, 2018 -- five years ago, as I write this. Five years: that's a long time. It certainly is as measured on the time scale of deep learning, the thing that is, usually, behind when people talk of "AI". One year later, GPT was followed by GPT-2; another year later, by GPT-3. At this point, public attention was still modest -- as expected, really, for these kinds of technologies that require lots of specialist knowledge. (For GPT-2, what may have increased attention beyond the normal, a bit, was OpenAI 's refusal to publish the complete training code and full model weights, supposedly due to the threat posed by the model's capabilities -- alternatively, as argued by others, as a marketing strategy, or yet alternatively, as a way to preserve one's own competitive advantage just a tiny little bit longer.

As of 2023, with GPT-3.5 and GPT-4 having followed, everything looks different. (Almost) everyone seems to know GPT, at least when that acronym appears prefixed by a certain syllable. Depending on who you talk to, people don't seem to stop talking about that fantastic \[insert thing here\] ChatGPT generated for them, about its enormous usefulness with respect to \[insert goal here\]... or about the flagrant mistakes it made, and the danger that legal regulation and political enforcement will never be able to catch up.

What made the difference? Obviously, it's [ChatGPT](https://en.wikipedia.org/wiki/ChatGPT), or put differently, the fact that now, there is a means for people to make active use of such a tool, employing it for whatever their personal needs or interests are[^1]. In fact, I'd argue it's more than that: ChatGPT is not some impersonal tool -- it *talks* to you, picking up your clarifications, changes of topic, mood... It is *someone* rather than *something*, or at least that's how it seems. I'll come back to that point in [It's us, really: Anthropomorphism unleashed](#its-us-really-anthropomorphism-unleashed). Before, let's take a look at the underlying technology.

## Large Language Models: What they are

How is it even possible to build a machine that talks to you? One way is to have that machine *listen* a lot. And listen is what these machines do; they do it a lot. But listening alone would never be enough to attain results as impressive as those we see. Instead, LLMs practice some form of "maximally active listening": Continuously, they try to predict the speaker's next utterance. By "continuously", I mean word-by-word: At each training step, the model is asked to produce the subsequent word in a text.

Maybe in my last sentence, you noted the term "train". As per common sense, "training" implies some form of supervision. It also implies some form of method. Since learning material is scraped from the internet, the true continuation is always known. The precondition for supervision is thus always fulfilled: A supervisor can just compare model prediction with what really follows in the text. Remains the question of method. That's where we need to talk about deep learning, and we'll do that in [Model training](#model-training).

### Overall architecture

Today's LLMs are, in some way or the other, based on an architecture known as the *Transformer*. This architecture was originally introduced in a paper catchily titled "Attention is all you need" (Vaswani et al. 2017). Of course, this was not the first attempt at automating natural-language generation -- not even in deep learning, the sub-type of machine learning whose defining characteristic are many-layered ("deep") artificial neural networks. But there, in deep learning, it constituted some kind of paradigm change. Before, models designed to solve sequence-prediction tasks (time-series forecasting, text generation...) tended to be based on some form of recurrent architecture, introduced in the 1990's (eternities ago, on the time scale of deep-learning) by (Hochreiter and Schmidhuber 1997). Basically, the concept of recurrence, with its associated threading of a latent state, was replaced by "attention". That's what the paper's title was meant to communicate: The authors did not *introduce* "attention"[^2]; instead, they fundamentally expanded its usage so as to render recurrence superfluous.

How did that ancestral Transformer look? -- One prototypical task in natural language processing is machine translation. In translation, be it done by a machine or by a human, there is an input (in one language) and an output (in another). That input, call it a *code*. Whoever wants to establish its counterpart in the target language first needs to *decode* it. Indeed, one of two top-level building blocks of the archetypal Transformer was a decoder, or rather, a stack of decoders applied in succession. At its end, out popped a phrase in the target language[^3]. What, then, was the other high-level block? It was an *encoder*, something that takes text (or tokens, rather, i.e., something that has undergone tokenization) and converts it into a form the decoder can make sense of. (Obviously, there is no analogue to this in human translation.)

From this two-stack architecture, subsequent developments tended to keep just one. The GPT family, together with many others, just kept the decoder stack. Now, doesn't the decoder need *some* kind of input -- if not to translate to a different language, then to reply to, as in the chatbot scenario? Turns out that no, it doesn't -- and that's why you can also have the bot initiate the conversation. Unbeknownst to you, there will, in fact, be an input to the model -- some kind of token signifying "end of input". In that case, the model will draw on its training experience to generate a word likely to start out a phrase. That one word will then become the new input to continue from, and so forth. Summing up so far, then, GPT-like LLMs are *Transformer Decoders*.

The question is, how does such a stack of decoders succeed in fulfilling the task?

### GPT-type models up close

In opening the black box, we focus on its two interfaces -- input and output -- as well as on the internals, its core.

#### Input

For simplicity, let me speak of words, not tokens. Now imagine a machine that is to work with -- more even: "understand"[^4] -- words. For a computer to process non-numeric data, a conversion to numbers necessarily has to happen. The straightforward way to effectuate this is to decide on a fixed lexicon, and assign each word a number. And this works: The way deep neural networks are trained, they don't need semantic relationships to exist between entities in the training data to memorize formal structure. Does this mean they will appear perfect while training, but fail in real-world prediction? -- If the training data are representative of how we converse, all will be fine. In a world of perfect surveillance, machines could exist that have internalized our every spoken word. Before that happens, though, the training data will be imperfect.

A much more promising approach than to simply index words, then, is to represent them in a richer, higher-dimensional space, an *embedding* space. This idea, popular not just in deep learning but in natural language processing overall, really goes far beyond anything domain-specific -- linguistic entities, say[^5]. You may be able to fruitfully employ it in virtually any domain -- provided you can devise a method to sensibly map the given data into that space. In deep learning, these embeddings are obtained in a clever way: as a by-product of sorts of the overall training workflow. Technically, this is achieved by means of a dedicated neural-network layer[^6] tasked with evolving these mappings. Note how, smart though this strategy may be, it implies that the overall setting -- everything from training data via model architecture to optimization algorithms employed -- necessarily affects the resulting embeddings. And since these may be extracted and made use of in down-stream tasks, this matters[^7].

As to the GPT family, such an embedding layer constitutes part of its input interface -- one "half", so to say. Technically, the second makes use of the same type of layer, but with a different purpose. To contrast the two, let me spell out clearly what, in the part we've talked about already, is getting mapped to what. The mapping is between a word index -- a sequence `1, 2, …, <vocabulary size>` -- on the one hand and a set of continuous-valued vectors of some length -- 100, say -- on the other. (One of them could like this: $\begin{bmatrix} 1.002 & 0.71 & 0.0004 &...\\ \end{bmatrix}$) Thus, we obtain an embedding for every word. But language is more than an unordered assembly of words. Rearranging words, if syntactically allowed, may result in drastically changed semantics. In the pre-transformer paradigma, threading a sequentially-updated hidden state took care of this. Put differently, in that type of model, information about input order never got lost throughout the layers. Transformer-type architectures, however, need to find a different way. Here, a variety of rivaling methods exists. Some assume an underlying periodicity in semanto-syntactic structure. Others -- and the GPT family, as yet and *insofar* *we know*, has been part of them[^8] -- approach the challenge in exactly the same way as for the lexical units: They make learning these so-called *position embeddings* a by-product of model training. Implementation-wise, the only difference is that now the input to the mapping looks like this: `1, 2, …, <maximum position>` where "maximum position" reflects choice of maximal sequence length supported.

Summing up, verbal input is thus encoded -- *embedded*, enriched -- twofold as it enters the machine. The two types of embedding are combined and passed on to the model core, the already-mentioned decoder stack.

#### Core Processing

The decoder stack is made up of some number of identical blocks (12, in the case of GPT-2). (By "identical" I mean that the architecture is the same; the *weights* -- the place where a neural-network layer stores what it "knows" -- are not. More on these "weights" soon.)

Inside each block, some sub-layers are pretty much "business as usual". One is not: the attention module, the "magic" ingredient that enabled Transformer-based architectures to forego keeping a latent state. To explain how this works, let's take translation as an example.

In the classical encoder-decoder setup, the one most intuitive for machine translation, imagine the very first decoder in the stack of decoders. It receives as input a length-seven cypher, the encoded version of an original length-seven phrase. Since, due to how the encoder blocks are built, input order is conserved, we have a faithful representation of source-language word order. In the target language, however, word order can be very different. A decoder module, in producing the translation, had rather not do this by translating each word as it appears. Instead, it would be desirable for it to know which among the already-seen tokens is most relevant right now, to generate the very next output token. Put differently, it had better know where to direct its *attention*.

Thus, figure out how to distribute focus is what attention modules do. How do they do it? They compute, for each available input-language token, how good a match, a fit, it is for their own current input. Remember that every token, at every processing stage, is encoded as a vector of continuous values. How good a match any of, say, three source-language vectors is is then computed by projecting one's current input vector onto each of the three. The closer the vectors, the longer the projected vector. [^9] Based on the projection onto each source-input token, that token is weighted, and the attention module passes on the aggregated assessments to the ensuing neural-network module.

To explain what attention modules are for, I've made use of the machine-translation scenario, a scenario that should lend a certain intuitiveness to the operation. But for GPT-family models, we need to abstract this a bit. First, there is no encoder stack, so "attention" is computed among decoder-resident tokens only. And second -- remember I said a stack was built up of identical modules? -- this happens in every decoder block. That is, when intermediate results are bubbled up the stack, at each stage the input is weighted as appropriate *at that stage*. While this is harder to intuit than what happened in the translation scenario, I'd argue that in the abstract, it makes a lot of sense. For an analogy, consider some form of hierarchical categorization of entities. As higher-level categories are built from lower-level ones, at each stage the process needs to look at its input afresh, and decide on a sensible way of subsuming similar-in-some-way categories.

#### Output

Stack of decoders traversed, the multi-dimensional codes that pop out need to be converted into something that can be compared with the actual phrase continuation we see in the training corpus. Technically, this involves a projection operation as well a strategy for picking the output word -- that word in target-language vocabulary that has the highest probability. How do you decide on a strategy? I'll say more about that in the section [Mechanics of text generation](#mechanics-of-text-generation), where I assume a chatbot user's perspective.

### Model training

Before we get there, just a quick word about model training. LLMs are deep neural networks, and as such, they are trained like any network is. First, assuming you have access to the so-called "ground truth", you can always compare model prediction with the true target. You then quantify the difference -- by which algorithm will affect training results. Then, you communicate that difference -- the *loss* -- to the network. It, in turn, goes through its modules, from back/top to start/bottom, and updates its stored "knowledge" -- matrices of continuous numbers called *weights*. Since information is passed from layer to layer, in a direction reverse to that followed in computing predictions, this technique is known as *back-propagation*.

And all that is not triggered once, but iteratively, for a certain number of so-called "epochs", and modulated by a set of so-called "hyper-parameters". In practice, a lot of experimentation goes into deciding on the best-working configuration of these settings.

### Mechanics of text generation

We already know that during model training, predictions are generated word-by-word; at every step, the model's knowledge about what has been said so far is augmented by one token: the word that really was following at that point. If, making use of a trained model, a bot is asked to reply to a question, its response must by necessity be generated in the same way. However, the actual "correct word" is not known. The only way, then, is to feed back to the model its own most recent prediction. (By necessity, this lends to text generation a very special character, where every decision the bot makes co-determines its future behavior.)

Why, though, talk about decisions? Doesn't the bot just act on behalf of the core model, the LLM -- thus passing on the final output? Not quite. At each prediction step, the model yields a vector, with values as many as there are entries in the vocabulary. As per model design and training rationale, these vectors are "scores" -- ratings, sort of, how good a fit a word would be in this situation. Like in life, higher is better. But that doesn't mean you'd just pick the word with the highest value. In any case, these scores are converted to probabilities, and a suitable probability distribution is used to non-deterministically pick a likely (or likely-ish) word. The probability distribution commonly used is the multinomial distribution, appropriate for discrete choice among more than two alternatives. But what about the conversion to probabilities? Here, there is room for experimentation.

Technically, the algorithm employed is known as the *softmax* function. It is a simplified version of the [Boltzmann distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution), famous in statistical mechanics, used to obtain the probability of a system's state given that state's energy and the temperature of the system. But for temperature[^10], both formulae are, in fact, identical. In physical systems, temperature modulates probabilities in the following way: The hotter the system, the closer the states' probabilities are to each other; the colder it gets, the more distinct those probabilities. In the extreme, at very low temperatures there will be a few clear "winners" and a silent majority of "losers".

In deep learning, a like effect is easy to achieve (by means of a scaling factor). That's why you may have heard people talk about some weird thing called "temperature" that resulted in \[insert adjective here\] answers. If the application you use lets you vary that factor, you'll see that a low temperature will result in deterministic-looking, repetitive, "boring" continuations, while a high one may make the machine appear as though it were on drugs.

That concludes our high-level overview of LLMs. Having seen the machine dissected in this way may already have left you with some sort of opinion of what these models are -- not. This topic more than deserves a dedicated exposition -- and papers are being written pointing to important aspects all the time -- but in this text, I'd like to at least offer some input for thought.

## Large Language Models: What they are not

In part one,describing LLMs technically, I've sometimes felt tempted to use terms like "understanding" or "knowledge" when applied to the machine. I may have ended up using them; in that case, I've tried to remember to always surround them with quotes. The latter, the adding quotes, stands in contrast to many texts, even ones published in an academic context (Bender and Koller 2020). The question is, though: Why did I even feel compelled to use these terms, given I do *not* think they apply, in their usual meaning? I can think of a simple -- shockingly simple, maybe -- answer: It's because us, humans, we think, talk, share our thoughts in these terms. When I say *understand*, I surmise you will *know* what I *mean*.

Now, why do I think that these machines do not *understand* human language, in the sense we usually imply when using that word?

### A few facts

I'll start out briefly mentioning empirical results, conclusive thought experiments, and theoretical considerations. All aspects touched upon (and many more) are more than worthy of in-depth discussion, but such discussion is clearly out of scope for this synoptic-in-character text.

First, while it is hard to put a number on the quality of a chatbot's answers, performance on standardized benchmarks is the "bread and butter" of machine learning -- its reporting being an essential part of the prototypical deep-learning publication. (You could even call it the "cookie", the driving incentive, since models usually are explicitly trained and fine-tuned for good results on these benchmarks.) And such benchmarks exist for most of the down-stream tasks the LLMs are used for: machine translation, generating summaries, text classification, and even rather ambitious-sounding setups associated with -- quote/unquote -- reasoning.

How do you assess such a capability? Here is an example from a benchmark named "Argument Reasoning Comprehension Task" (Habernal et al. 2018).

    Claim: Google is not a harmful monopoly
    Reason: People can choose not to use Google
    Warrant: Other search engines don’t redirect to Google
    Alternative: All other search engines redirect to Google

Here *claim* and *reason* together make up the *argument*. But what, exactly, is it that links them? At first look, this can even be confusing to a human. The missing link is what is called warrant here -- add it in, and it all starts to make sense. The task, then, is to decide which of warrant or alternative supports the conclusion, and which one does not.

If you think about it, this is a surprisingly challenging task. Specifically, it seems to inescapingly require *world knowledge*. So if language models, as has been claimed, perform nearly as well as humans, it seems they must have such knowledge -- no quotes added. However, in response to such claims, research has been performed to uncover the hidden mechanism that enables such seemingly-superior results. For that benchmark, it has been found (Niven and Kao 2019) that there were spurious statistical cues in the way the dataset was constructed -- those removed, LLM performance was no better than random.

World knowledge, in fact, is one of the main things an LLM lacks. Bender et al. (Bender and Koller 2020) convincingly demonstrate its essentiality by means of two thought experiments. One of them, situated on a lone island, imagines an octopus[^11] inserting itself into some cable-mediated human communication, learning the chit-chat, and finally -- having gotten bored -- impersonating one of the humans. This works fine, until one day, its communication partner finds themselves in an emergency, and needs to build some rescue tool out of things given in the environment. They urgently ask for advice -- and the octopus has no idea what to respond. It has no ideas what these words actually *refer to*.

The other argument comes directly from machine learning, and strikingly simple though it may be, it makes its point very well. Imagine an LLM trained as usual, including on lots of text involving plants. It has also been trained on a dataset of unlabeled photos, the actual task being unsubstantial -- say it had to fill out masked areas. Now, we pull out a picture and ask: How many of that blackberry's blossoms have already opened? The model has no chance to answer the question.

Now, please look back at the Joseph Weizenbaum quote I opened this article with. It is still true that language-generating machine have no knowledge of the world we live in.

Before moving on, I'd like to just quickly hint at a totally different type of consideration, brought up in a (2003!) paper by Spärck Jones (Spaerck 2004). Though written long before LLMs, and long before deep learning started its winning conquest, on an abstract level it is still very applicable to today's situation. Today, LLMs are employed to "learn language", i.e., for language acquisition. That skill is then built upon by specialized models, of task-dependent architecture. Popular real-world[^12] down-stream tasks are translation, document retrieval, or text summarization. When the paper was written, there was no such two-stage pipeline. The author was questioning the fit between how language modeling was conceptualized -- namely, as a form of *recovery* -- and the character of these down-stream tasks. Was recovery -- inferring a missing, for whatever reasons -- piece of text a good model, of, say, condensing a long, detailed piece of text into a short, concise, factual one? If not, could the reason it still seemed to work just fine be of a very different nature -- a technical, operational, coincidental one?

> \[...\] the crucial characterisation of the relationship between the input and the output is in fact offloaded in the LM approach onto the choice of training data. We can use LM for summarising because we know that some set of training data consists of full texts paired with their summaries.[^13]

It seems to me that today's two-stage process notwithstanding, this is still an aspect worth giving some thought.

### It's us: Language learning, shared goals, and a shared world

We've already talked about world knowledge. What else are LLMs missing out on?

In our world, you'll hardly find anything that does not involve other people. This goes a lot deeper than the easily observable facts: our constantly communicating, reading and typing messages, documenting our lives on social networks... We don't experience, explore, explain a world of our own. Instead, all these activities are inter-subjectively constructed. Feelings are[^14]. Cognition is; meaning is. And it goes deeper yet. Implicit assumptions guide us to constantly look for meaning, be it in overheard fragments, mysterious symbols, or life events.

How does this relate to LLMs? For one, they're islands of their own. When you ask them for advice -- to develop a research hypothesis and a matching operationalization, say, or whether a detainee should be released on parole -- they have no stakes in the outcome, no motivation (be it intrinsic or extrinsic), no goals. If an innocent person is harmed, they don't feel the remorse; if an experiment is successful but lacks explanatory power, they don't sense the shallowness; if the world blows up, it won't have been *their* world.

Secondly, it's us who are *not* islands. In Bender et al.'s octopus scenario, the human on one side of the cable plays an active role not just when they speak. In making sense of what the octopus says, they contribute an essential ingredient: namely, what they think the octopus wants, thinks, feels, expects... Anticipating, they reflect on what the octopus anticipates.

As Bender et al. put it:

> It is not that O's utterances make sense, but rather, that A can make sense of them.

That article (Bender and Koller 2020) also brings impressive evidence from human language acquisition: Our predisposition towards language learning notwithstanding, infants don't learn from the availability of input alone. A situation of *joint attention* is needed for them to learn. Psychologizing, one could hypothesize they need to get the impression that these sounds, these words, and the fact they're linked together, actually matters.

Let me conclude, then, with my final "psychologization".

### It's us, *really*: Anthropomorphism unleashed

Yes, it is amazing what these machines do. (And that makes them incredibly dangerous power instruments.) But this in no way affects the human-machine differences that have been existing throughout history, and continue to exist today. That we are inclined to think they understand, know, mean -- that maybe even they're conscious: that's on us. We can experience deep emotions watching a movie; hope that if we just try enough, we can sense what a distant-in-evolutionary-genealogy creature is feeling; see a cloud encouragingly smiling at us; read a sign in an arrangement of pebbles.

Our inclination to anthropomorphize is a gift; but it can sometimes be harmful. And nothing of this is special to the twenty-first century.

Like I began with him, let me conclude with Weizenbaum.

> Some subjects have been very hard to convince that ELIZA (with its present script) is *not* human.

Photo by <a 
href="https://unsplash.com/@marjan_blan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Marjan
Blan</a> on <a 
href="https://unsplash.com/photos/8TLfX3-705M?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Bender, Emily M., and Alexander Koller. 2020. "Climbing Towards NLU: On Meaning, Form, and Understanding in the Age of Data." *Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics* (Online), July, 5185--98. <https://doi.org/10.18653/v1/2020.acl-main.463>.

Caliskan, Aylin, Pimparkar Parth Ajay, Tessa Charlesworth, Robert Wolfe, and Mahzarin R. Banaji. 2022. "Gender Bias in Word Embeddings." *Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society*, July. <https://doi.org/10.1145/3514094.3534162>.

Habernal, Ivan, Henning Wachsmuth, Iryna Gurevych, and Benno Stein. 2018. "The Argument Reasoning Comprehension Task: Identification and Reconstruction of Implicit Warrants." *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long Papers)* (New Orleans, Louisiana), June, 1930--40. <https://doi.org/10.18653/v1/N18-1175>.

Hochreiter, Sepp, and Jürgen Schmidhuber. 1997. "Long Short-Term Memory." *Neural Computation* 9 (December): 1735--80. <https://doi.org/10.1162/neco.1997.9.8.1735>.

Niven, Timothy, and Hung-Yu Kao. 2019. "Probing Neural Network Comprehension of Natural Language Arguments." *CoRR* abs/1907.07355. <http://arxiv.org/abs/1907.07355>.

Spaerck, Karen. 2004. "Language Modelling's Generative Model : Is It Rational?"

Vaswani, Ashish, Noam Shazeer, Niki Parmar, et al. 2017. *Attention Is All You Need*. <https://arxiv.org/abs/1706.03762>.

Weizenbaum, Joseph. 1966. "ELIZA - a Computer Program for the Study of Natural Language Communication Between Man and Machine." *Commun. ACM* (New York, NY, USA) 9 (1): 36--45. <https://doi.org/10.1145/365153.365168>.

[^1]: Evidently, this is not about singling out ChatGPT as opposed to other chatbots; rather, I'm adopting it as the prototypical such application, since it is the one omnipresent in the media these days.

[^2]: I'm using quotes to refer to how attention is *operationalized in deep learning*, as opposed to how it is conceptualized in cognitive science or psychology.

[^3]: If you're wondering how that is possible -- shouldn't there be a separate, top-level module for generation? -- no, there need not be. That's because training *implies* prediction.

[^4]: Why the quotes? See [Large Language Models: What they are not](#large-language-models-what-they-are-not).

[^5]: As a fascinating example from dynamical systems theory, take [delay coordinate embeddings](https://en.wikipedia.org/wiki/Takens%27s_theorem).

[^6]: Suitably named *embedding layer.*

[^7]: See, for example, (Caliskan et al. 2022).

[^8]: For GPT-4, even high-level model information has not been released.

[^9]: Mathematically, this is achieved by a pretty standard and pervasively-used, in machine learning, operation, the *dot product*.

[^10]: ... and the Boltzmann constant -- but that being a constant, we don't consider it here.

[^11]: That choice of species is probably not a coincidence: see <https://en.wikipedia.org/wiki/Cephalopod_intelligence>.

[^12]: As opposed to the aforementioned problems subsumed under "reasoning", those having been constructed for research purposes.

[^13]: From (Spaerck 2004).

[^14]: See <https://lisafeldmanbarrett.com/books/how-emotions-are-made/>.
