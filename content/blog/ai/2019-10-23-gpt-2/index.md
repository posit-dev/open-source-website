---
title: "Innocent unicorns considered harmful? How to experiment with GPT-2 from R"
description: |
  Is society ready to deal with challenges brought about by artificially-generated information - fake images, fake videos, fake text? While this post won't answer that question, it should help form an opinion on the threat exerted by fake text as of this writing, autumn 2019. We introduce gpt2, an R package that wraps OpenAI's public implementation of GPT-2, the language model that early this year surprised the NLP community with the unprecedented quality of its creations.
date: 2019-10-23
slug: keydanaluraschi2019gpt2
categories:
  - Natural Language Processing
  - Packages/Releases
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
  - name: Javier Luraschi
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
  - Javier Luraschi
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
---



When this year in February, OpenAI presented [GPT-2](https://openai.com/blog/better-language-models/)(Radford et al. 2019), a large *Transformer*-based language model trained on an enormous amount of web-scraped text, their announcement caught great attention, not just in the NLP community. This was primarily due to two facts. First, the samples of generated text were stunning.

Presented with the following input

> In a shocking finding, scientist \[sic\] discovered a herd of unicorns living in a remote, previously unexplored valley, in the Andes Mountains. Even more surprising to the researchers was the fact that the unicorns spoke perfect English.

this was how the model continued:

> The scientist named the population, after their distinctive horn, Ovid's Unicorn. These four-horned, silver-white unicorns were previously unknown to science.
> Now, after almost two centuries, the mystery of what sparked this odd phenomenon is finally solved.
> Dr. Jorge Pérez, an evolutionary biologist from the University of La Paz, and several companions, were exploring the Andes Mountains when they found a small valley, with no other animals or humans. Pérez noticed that the valley had what appeared to be a natural fountain, surrounded by two peaks of rock and silver snow. \[...\]

Second, "due to our concerns about malicious applications" (quote) they didn't release the full model, but a smaller one that has less than one tenth the number of parameters. Neither did they make public the dataset, nor the training code.

While at first glance, this may look like a marketing move (*we created something so powerful that it's too dangerous to be released to the public!*), let's not make things that easy on ourselves.

## With great power ...

Whatever your take on the "innate priors in deep learning" discussion -- how much knowledge needs to be hardwired into neural networks for them to solve tasks that involve more than pattern matching? -- there is no doubt that in many areas, systems driven by "AI" [^1] will impact
our lives in an essential, and ever more powerful, way. Although there may be some awareness of the ethical, legal, and political problems this poses, it is probably fair to say that by and large, society is closing its eyes and holding its hands over its ears.

If you were a deep learning researcher working in an area susceptible to abuse, generative ML say, what options would you have? As always in the history of science, what can be done will be done; all that remains is the search for antidotes. You may doubt that on a political level, constructive responses could evolve. But you can encourage other researchers to scrutinize the artifacts your algorithm created and develop other algorithms designed to spot the fakes -- essentially like in malware detection. Of course this is a feedback system: Like with GANs, impostor algorithms will happily take the feedback and go on working on their shortcomings. But still, deliberately entering this circle *might* be the only viable action to take.

Although it may be the first thing that comes to mind, the question of veracity here isn't the only one. With ML systems, it's always: garbage in - garbage out. What is fed as training data determines the quality of the output, and any biases in its upbringing will carry through to an algorithm's grown-up behavior. Without interventions, software designed to do translation, autocompletion and the like will be biased [^2].

In this light, all we can sensibly do is -- constantly -- point out the biases, analyze the artifacts, and conduct adversarial attacks. These are the kinds of responses OpenAI was asking for. In appropriate modesty, they called their approach an *experiment*. Put plainly, no-one today knows how to deal with the threats emerging from powerful AI appearing in our lives. But there is no way around exploring our options.

## The story unwinding

Three months later, OpenAI published an update to the initial post, stating that they had decided on a staged-release strategy. In addition to making public the next-in-size, 355M-parameters version of the model, they also released a dataset of [generated outputs from all model sizes](https://github.com/openai/gpt-2-output-dataset), to facilitate research. Last not least, they announced partnerships with academic and non-academic institutions, to increase "societal preparedness" (quote).

Again after three months, in a [new post](https://openai.com/blog/gpt-2-6-month-follow-up/) OpenAI announced the release of a yet larger -- 774M-parameter -- version of the model. At the same time, they reported evidence demonstrating insufficiencies in current statistical fake detection, as well as study results suggesting that indeed, text generators exist that can trick humans.

Due to those results, they said, no decision had yet been taken as to the release of the biggest, the "real" model, of size 1.5 billion parameters.

## GPT-2

So what is GPT-2? Among state-of-the-art NLP models, GPT-2 stands out due to the gigantic (40G) dataset it was trained on, as well as its enormous number of weights. The architecture, in contrast, wasn't new when it appeared. GPT-2, as well as its predecessor GPT (Radford 2018), is based on a transformer architecture.

The original Transformer (Vaswani et al. 2017) is an encoder-decoder architecture designed for sequence-to-sequence tasks, like machine translation. The paper introducing it was called "Attention is all you need", emphasizing -- by absence -- what you don't need: RNNs.

Before its publication, the prototypical model for e.g. machine translation would use some form of RNN as an encoder, some form of RNN as a decoder, and an attention mechanism that at each time step of output generation, told the decoder where in the encoded input to look. Now the transformer was disposing with RNNs, essentially replacing them by a mechanism called *self-attention* where already during *encoding*, the encoder stack would encode each token not independently, but as a weighted sum of tokens encountered before (including itself). [^3]

Many subsequent NLP models built on the Transformer, but -- depending on purpose -- either picked up the encoder stack only, or just the decoder stack.
GPT-2 was trained to predict consecutive words in a sequence. It is thus a *language model*, a term resounding the conception that an algorithm which can predict future words and sentences somehow has to *understand* language (and a lot more, we might add).
As there is no input to be encoded (apart from an optional one-time prompt), all that is needed is the stack of decoders.

In our experiments, we'll be using the biggest as-yet released pretrained model, but this being a pretrained model our degrees of freedom are limited. We can, of course, condition on different input prompts. In addition, we can influence the sampling algorithm used.

## Sampling options with GPT-2

Whenever a new token is to be predicted, a *softmax* is taken over the vocabulary [^4]. Directly taking the softmax output amounts to maximum likelihood estimation. In reality, however, always choosing the maximum likelihood estimate results in highly repetitive output.

A natural option seems to be using the softmax outputs as probabilities: Instead of just taking the *argmax*, we sample from the output distribution. Unfortunately, this procedure has negative ramifications of its own. In a big vocabulary, very improbable words together make up a substantial part of the probability mass; at every step of generation, there is thus a non-negligible probability that an improbable word may be chosen. This word will now exert great influence on what is chosen next. In that manner, highly improbable sequences can build up.

The task thus is to navigate between the Scylla of determinism and the Charybdis of weirdness. With the GPT-2 model presented below, we have three options:

- vary the *temperature* (parameter `temperature`);
- vary `top_k`, the number of tokens considered; or
- vary `top_p`, the probability mass considered.

The *temperature* concept is rooted in statistical mechanics. Looking at the Boltzmann distribution used to model state probabilities $p_i$dependent on energy $\epsilon_i$:

$$p_i \sim e^{-\frac{\epsilon_i}{kT}}$$

we see there is a moderating variable *temperature* $T$ [^5] that dependent on whether it's below or above 1, will exert an either amplifying or attenuating influence on differences between probabilities.

Analogously, in the context of predicting the next token, the individual logits are scaled by the temperature, and only then is the softmax taken. Temperatures below zero would make the model even more rigorous in choosing the maximum likelihood candidate; instead, we'd be interested in experimenting with temperatures above 1 to give higher chances to less likely candidates -- hopefully, resulting in more human-like text.

In top-$k$ sampling, the softmax outputs are sorted, and only the top-$k$ tokens are considered for sampling. The difficulty here is how to choose $k$. Sometimes a few words make up for almost all probability mass, in which case we'd like to choose a low number; in other cases the distribution is flat, and a higher number would be adequate.

This sounds like rather than the number of candidates, a target probability mass should be specified. This is the approach suggested by (Holtzman et al. 2019). Their method, called top-$p$, or Nucleus sampling, computes the cumulative distribution of softmax outputs and picks a cut-off point $p$. Only the tokens constituting the top-$p$ portion of probability mass is retained for sampling.

Now all you need to experiment with GPT-2 is the model.

## Setup

Install `gpt2` from [github](https://github.com/r-tensorflow/gpt2):

``` r
remotes::install_github("r-tensorflow/gpt2")
```

The R package being a wrapper to the implementation [provided by OpenAI](https://github.com/openai/gpt-2), we then need to install the Python runtime.

``` r
gpt2::install_gpt2(envname = "r-gpt2")
```

This command will also install TensorFlow into the designated environment. All TensorFlow-related installation options (resp. recommendations) apply. Python 3 is required.

While OpenAI indicates a dependency on TensorFlow 1.12, the R package was adapted to work with more current versions. The following versions have been found to be working fine:

- if running on GPU: TF 1.15
- CPU-only: TF 2.0

Unsurprisingly, with GPT-2, running on GPU vs. CPU makes a huge difference.

As a quick test if installation was successful, just run `gpt2()` with the default parameters:

``` r
# equivalent to:
# gpt2(prompt = "Hello my name is", model = "124M", seed = NULL, batch_size = 1, total_tokens = NULL,
#      temperature = 1, top_k = 0, top_p = 1)
# see ?gpt2 for an explanation of the parameters
#
# available models as of this writing: 124M, 355M, 774M
#
# on first run of a given model, allow time for download
gpt2()
```

## Things to try out

So *how dangerous exactly* is GPT-2? We can't say, as we don't have access to the "real" model. But we can compare outputs, given the same prompt, obtained from all available models. The number of parameters has approximately doubled at every release -- 124M, 355M, 774M. The biggest, yet unreleased, model, again has twice the number of weights: about 1.5B. In light of the evolution we observe, what do we expect to get from the 1.5B version?

In performing these kinds of experiments, don't forget about the different sampling strategies explained above. Non-default parameters might yield more real-looking results.

Needless to say, the prompt we specify will make a difference. The models have been trained on a web-scraped dataset, [subject to the quality criterion "3 stars on reddit"](https://openai.com/blog/better-language-models/). We expect more fluency in certain areas than in others, to put it in a cautious way.

Most definitely, we expect various biases in the outputs.

Undoubtedly, by now the reader will have her own ideas about what to test. But there is more.

## "Language Models are Unsupervised Multitask Learners"

Here we are citing the title of the official GPT-2 paper (Radford et al. 2019). What is that supposed to mean? It means that a model like GPT-2, trained to predict the next token in naturally occurring text, can be used to "solve" standard NLP tasks that, in the majority of cases, are approached via supervised training (translation, for example).

The clever idea is to present the model with cues about the task at hand. Some information on how to do this is given in the paper; more (unofficial; conflicting or confirming) hints can be found on the net.
From what we found, here are some things you could try.

### Summarization

The clue to induce summarization is "TL;DR:", written on a line by itself. The authors report that this worked best setting `top_k = 2` and asking for 100 tokens. Of the generated output, they took the first three sentences as a summary.

To try this out, we chose a sequence of content-wise standalone paragraphs from [a NASA website dedicated to climate change](https://climate.nasa.gov/evidence/), the idea being that with a clearly structured text like this, it should be easier to establish relationships between input and output.

    # put this in a variable called text

    The planet's average surface temperature has risen about 1.62 degrees Fahrenheit
    (0.9 degrees Celsius) since the late 19th century, a change driven largely by
    increased carbon dioxide and other human-made emissions into the atmosphere.4 Most
    of the warming occurred in the past 35 years, with the five warmest years on record
    taking place since 2010. Not only was 2016 the warmest year on record, but eight of
    the 12 months that make up the year — from January through September, with the
    exception of June — were the warmest on record for those respective months.

    The oceans have absorbed much of this increased heat, with the top 700 meters
    (about 2,300 feet) of ocean showing warming of more than 0.4 degrees Fahrenheit
    since 1969.

    The Greenland and Antarctic ice sheets have decreased in mass. Data from NASA's
    Gravity Recovery and Climate Experiment show Greenland lost an average of 286
    billion tons of ice per year between 1993 and 2016, while Antarctica lost about 127
    billion tons of ice per year during the same time period. The rate of Antarctica
    ice mass loss has tripled in the last decade.

    Glaciers are retreating almost everywhere around the world — including in the Alps,
    Himalayas, Andes, Rockies, Alaska and Africa.

    Satellite observations reveal that the amount of spring snow cover in the Northern
    Hemisphere has decreased over the past five decades and that the snow is melting
    earlier.

    Global sea level rose about 8 inches in the last century. The rate in the last two
    decades, however, is nearly double that of the last century and is accelerating
    slightly every year.

    Both the extent and thickness of Arctic sea ice has declined rapidly over the last
    several decades.

    The number of record high temperature events in the United States has been
    increasing, while the number of record low temperature events has been decreasing,
    since 1950. The U.S. has also witnessed increasing numbers of intense rainfall events.

    Since the beginning of the Industrial Revolution, the acidity of surface ocean
    waters has increased by about 30 percent.13,14 This increase is the result of humans
    emitting more carbon dioxide into the atmosphere and hence more being absorbed into
    the oceans. The amount of carbon dioxide absorbed by the upper layer of the oceans
    is increasing by about 2 billion tons per year.

    TL;DR:

``` r
gpt2(prompt = text,
     model = "774M",
     total_tokens = 100,
     top_k = 2)
```

Here is the generated result, whose quality on purpose we don't comment on. (Of course one can't help having "gut reactions"; but to actually present an evaluation we'd want to conduct a systematic experiment, varying not only input prompts but also function parameters. All we want to show in this post is how you can set up such experiments yourself.)

    "\nGlobal temperatures are rising, but the rate of warming has been accelerating.
    \n\nThe oceans have absorbed much of the increased heat, with the top 700 meters of
    ocean showing warming of more than 0.4 degrees Fahrenheit since 1969.
    \n\nGlaciers are retreating almost everywhere around the world, including in the
    Alps, Himalayas, Andes, Rockies, Alaska and Africa.
    \n\nSatellite observations reveal that the amount of spring snow cover in the
    Northern Hemisphere has decreased over the past"

Speaking of parameters to vary, -- they fall into two classes, in a way. It is unproblematic to vary the sampling strategy, let alone the prompt. But for tasks like summarization, or the ones we'll see below, it doesn't feel right to have to tell the model how many tokens to generate. Finding the right length of the answer seems to be part of the task. [^6] Breaking our "we don't judge" rule just a single time, we can't help but remark that even in less clear-cut tasks, language generation models that are meant to approach human-level competence would have to fulfill a criterion of *relevance* (Grice 1975).

### Question answering

To trick GPT-2 into question answering, the common approach seems to be presenting it with a number of *Q:* / *A:* pairs, followed by a final question and a final *A:* on its own line.

We tried like this, asking questions on the above climate change - related text:

``` r
q <- str_c(str_replace(text, "\nTL;DR:\n", ""), " \n", "
Q: What time period has seen the greatest increase in global temperature? 
A: The last 35 years. 
Q: What is happening to the Greenland and Antarctic ice sheets? 
A: They are rapidly decreasing in mass. 
Q: What is happening to glaciers? 
A: ")

gpt2(prompt = q,
     model = "774M",
     total_tokens = 10,
     top_p = 0.9)
```

This did not turn out so well.

    "\nQ: What is happening to the Arctic sea"

But maybe, more successful tricks exist.

### Translation

For translation, the strategy presented in the paper is juxtaposing sentences in two languages, joined by " = ", followed by a single sentence on its own and a" =".
Thinking that English \<-\> French might be the combination best represented in the training corpus, we tried the following:

    # save this as eng_fr

    The issue of climate change concerns all of us. = La question du changement
    climatique nous affecte tous. \n
    The problems of climate change and global warming affect all of humanity, as well as
    the entire ecosystem. = Les problèmes créés par les changements climatiques et le
    réchauffement de la planète touchent toute l'humanité, de même que l'écosystème tout
    entier.\n
    Climate Change Central is a not-for-profit corporation in Alberta, and its mandate
    is to reduce Alberta's greenhouse gas emissions. = Climate Change Central est une
    société sans but lucratif de l'Alberta ayant pour mission de réduire les émissions
    de gaz. \n
    Climate change will affect all four dimensions of food security: food availability,
    food accessibility, food utilization and food systems stability. = "

    gpt2(prompt = eng_fr,
         model = "774M",
         total_tokens = 25,
         top_p = 0.9)

Results varied a lot between different runs. Here are three examples:

    "ét durant les pages relevantes du Centre d'Action des Sciences Humaines et dans sa
    species situé,"

    "études des loi d'affaires, des reasons de demande, des loi d'abord and de"

    "étiquettes par les changements changements changements et les bois d'escalier,
    ainsi que des"

## Conclusion

With that, we conclude our tour of "what to explore with GPT-2". Keep in mind that the yet-unreleased model has double the number of parameters; essentially, *what we see is not what we get*.

This post's goal was to show how you can experiment with GPT-2 from R. But it also reflects the decision to, from time to time, widen the narrow focus on technology and allow ourselves to think about ethical and societal implications of ML/DL.

Thanks for reading!

Grice, H. P. 1975. "Logic and Conversation." In *Syntax and Semantics: Vol. 3: Speech Acts*. Academic Press. <http://www.ucl.ac.uk/ls/studypacks/Grice-Logic.pdf>.

Holtzman, Ari, Jan Buys, Maxwell Forbes, and Yejin Choi. 2019. "The Curious Case of Neural Text Degeneration." *arXiv e-Prints*, April, arXiv:1904.09751. <https://arxiv.org/abs/1904.09751>.

Radford, Alec. 2018. "Improving Language Understanding by Generative Pre-Training."

Radford, Alec, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. *Language Models Are Unsupervised Multitask Learners*.

Sun, Tony, Andrew Gaut, Shirlyn Tang, et al. 2019. "Mitigating Gender Bias in Natural Language Processing: Literature Review." *CoRR* abs/1906.08976. <http://arxiv.org/abs/1906.08976>.

Vaswani, Ashish, Noam Shazeer, Niki Parmar, et al. 2017. "Attention Is All You Need." In *Advances in Neural Information Processing Systems 30*, edited by I. Guyon, U. V. Luxburg, S. Bengio, et al. Curran Associates, Inc. <http://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf>.

[^1]: The acronym here is used for convenience only, not to imply any specific view on what is, or is not, "artificial intelligence".

[^2]: For an overview of bias detection and mitigation specific to gender bias, see e.g. (Sun et al. 2019)

[^3]: For a detailed, and exceptionally visual, explanation of the Transformer, *the* place to go is [Jay Alammar's post](https://jalammar.github.io/illustrated-transformer/). Also check out [The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning](http://jalammar.github.io/illustrated-bert/), the article that might be held mainly responsible for the pervasive sesame-streetification of NLP.

[^4]: For an introduction to how softmax activation behaves, see [Winner takes all: A look at activations and cost functions](/blog/ai/2018-10-11-activations-intro/).

[^5]: $k$ is the Boltzmann constant

[^6]: Formally, `total_tokens` isn't a required parameter. If not passed, a default based on model size will be applied, resulting in lengthy output that definitely will have to be processed by some human-made rule.
