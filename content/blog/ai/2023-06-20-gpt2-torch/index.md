---
title: "GPT-2 from scratch with torch"
description: |
  Implementing a language model from scratch is, arguably, the best way to develop an accurate idea of how its engine works. Here, we use torch to code GPT-2, the immediate successor to the original GPT. In the end, you'll dispose of an R-native model that can make direct use of Hugging Face's pre-trained GPT-2 model weights.
date: 2023-06-20T00:00:00.000Z
slug: keydanagpt2
categories:
  - Torch
  - R
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



Whatever your take on Large Language Models (LLMs) -- are they beneficial? dangerous? a short-lived fashion, like crypto? -- they are *here*, *now*. And that means, it is a good thing to know (at a level one needs to decide for oneself) how they work. On this same day, I am publishing [What are Large Language Models? What are they not?](/blog/ai/2023-06-20-llm-intro), intended for a more general audience. In this post, I'd like to address deep learning practitioners, walking through a `torch` implementation of GPT-2 (Radford et al. 2019), the second in OpenAI's succession of ever-larger models trained on ever-more-vast text corpora. You'll see that a complete model implementation fits in fewer than 250 lines of R code.

## Sources, resources

The code I'm going to present is found in the [`minhub`](https://github.com/mlverse/minhub) repository. This repository deserves a mention of its own. As emphasized in the README,

> *minhub* is a collection of minimal implementations of deep learning models, inspired by [minGPT](https://github.com/karpathy/minGPT/blob/master/mingpt/model.py). All models are designed to be self-contained, single-file, and devoid of external dependencies, making them easy to copy and integrate into your own projects.

Evidently, this makes them excellent learning material; but that is not all. Models also come with the option to load pre-trained weights from Hugging Face's [model hub](https://huggingface.co/models). And if that weren't enormously convenient already, you don't have to worry about how to get tokenization right: Just download the matching tokenizer from Hugging Face, as well. I'll show how this works in the [final section](#end-to-end-usage-using-pre-trained-weights) of this post. As noted in the `minhub` README, these facilities are provided by packages [`hfhub`](https://github.com/mlverse/hfhub) and [`tok`](https://github.com/mlverse/tok).

As realized in `minhub`, [gpt2.R](https://github.com/mlverse/minhub/blob/main/R/gpt2.R) is, mostly, a port of Karpathy's [MinGPT](https://github.com/karpathy/minGPT/blob/master/mingpt/model.py). Hugging Face's (more sophisticated) [implementation](https://github.com/huggingface/transformers/blob/v4.29.1/src/transformers/models/gpt2/modeling_gpt2.py) has also been consulted. For a Python code walk-through, see <https://amaarora.github.io/posts/2020-02-18-annotatedGPT2.html>. This text also consolidates links to blog posts and learning materials on language modeling with deep learning that have become "classics" in the short time since they were written.

## A minimal GPT-2

#### Overall architecture

The original Transformer (Vaswani et al. 2017) was built up of both an encoder and a decoder stack, a prototypical use case being machine translation. Subsequent developments, dependent on envisaged primary usage, tended to forego one of the stacks. The first GPT, which differs from GPT-2 only in relative subtleties, kept only the decoder stack. With "self-attention" wired into every decoder block, as well as an initial embedding step, this is not a problem -- external input is not technically different from successive internal representations.

Here is a screenshot from the initial GPT paper (Radford and Narasimhan 2018), visualizing the overall architecture. It is still valid for GPT-2. Token as well as position embedding are followed by a twelve-fold repetition of (identical in structure, though not sharing weights) transformer blocks, with a task-dependent linear layer constituting model output.

<img src="images/transformer.png" data-fig-alt="Overall architecture of GPT-2. The central part is a twelve-fold repetition of a transformer block, chaining, consecutively, multi-head self-attention, layer normalization, a feed-forward sub-network, and a second instance of layer normalization. Inside this block, arrows indicate residual connections omitting the attention and feed-forward layers. Below this central component, an input-transformation block indicates both token and position embedding. On its top, output blocks list a few alternative, task-dependent modules." width="144" />

In [gpt2.R](https://github.com/mlverse/minhub/blob/main/R/gpt2.R), this global structure and what it does is defined in `nn_gpt2_model()`. (The code is more modularized -- so don't be confused if code and screenshot don't perfectly match.)

First, in `initialize()`, we have the definition of modules:

``` r
self$transformer <- nn_module_dict(list(
  wte = nn_embedding(vocab_size, n_embd),
  wpe = nn_embedding(max_pos, n_embd),
  drop = nn_dropout(pdrop),
  h = nn_sequential(!!!map(
    1:n_layer,
    \(x) nn_gpt2_transformer_block(n_embd, n_head, n_layer, max_pos, pdrop)
  )),
  ln_f = nn_layer_norm(n_embd, eps = 1e-5)
))

self$lm_head <- nn_linear(n_embd, vocab_size, bias = FALSE)
```

The two top-level components in this model are the `transformer` and `lm_head`, the output layer. This code-level distinction has an important semantic dimension, with two aspects standing out. First, and quite directly, `transformer`'s definition communicates, in a succinct way, what it is that constitutes a Transformer. What comes thereafter -- `lm_head`, in our case -- may vary. Second, and importantly, the distinction reflects the essential underlying idea, or essential operationalization, of natural language processing in deep learning. Learning consists of two steps, the first -- and indispensable one -- being to learn about *language* (this is what LLMs do), and the second, much less resource-consuming, one consisting of adaptation to a concrete task (such as question answering, or text summarization).

To see in what order (and how often) things happen, we look inside `forward()`:

``` r
tok_emb <- self$transformer$wte(x) 
pos <- torch_arange(1, x$size(2))$to(dtype = "long")$unsqueeze(1) 
pos_emb <- self$transformer$wpe(pos)
x <- self$transformer$drop(tok_emb + pos_emb)
x <- self$transformer$h(x)
x <- self$transformer$ln_f(x)
x <- self$lm_head(x)
x
```

All modules in `transformer` are called, and thus executed, once; this includes `h` -- but `h` itself is a sequential module made up of transformer *blocks*.

Since these blocks are the core of the model, we'll look at them next.

#### Transformer block

Here's how, in `nn_gpt2_transformer_block()`, each of the twelve blocks is defined.

``` r
self$ln_1 <- nn_layer_norm(n_embd, eps = 1e-5)
self$attn <- nn_gpt2_attention(n_embd, n_head, n_layer, max_pos, pdrop)
self$ln_2 <- nn_layer_norm(n_embd, eps = 1e-5)
self$mlp <- nn_gpt2_mlp(n_embd, pdrop)
```

On this level of resolution, we see that self-attention is computed afresh at every stage, and that the other constitutive ingredient is a feed-forward neural network. In addition, there are two modules computing *layer normalization*, the type of normalization employed in transformer blocks. Different normalization algorithms tend to distinguish themselves from one another in what they average over; layer normalization (Ba et al. 2016) -- surprisingly, maybe, to some readers -- does so per batch *item*. That is, there is one mean, and one standard deviation, for each unit in a module. All other dimensions (in an image, that would be spatial dimensions as well as channels) constitute the input to that item-wise statistics computation.

Continuing to zoom in, we will look at both the attention- and the feed-forward network shortly. Before, though, we need to see how these layers are called. Here is all that happens in `forward()`:

``` r
x <- x + self$attn(self$ln_1(x))
x + self$mlp(self$ln_2(x))
```

These two lines deserve to be read attentively. As opposed to just calling each consecutive layer on the previous one's output, this inserts skip (also termed *residual*) connections that, each, circumvent one of the parent module's principal stages. The effect is that each sub-module does not replace, but just update what is passed in with its own view on things.

#### Transformer block up close: Self-attention

Of all modules in GPT-2, this is by far the most intimidating-looking. But the basic algorithm employed here is the same as what the classic "dot product attention paper" (Bahdanau et al. 2014) proposed in 2014: Attention is conceptualized as similarity, and similarity is measured via the dot product. One thing that can be confusing is the "self" in self-attention. This term first appeared in the Transformer paper (Vaswani et al. 2017), which had an encoder as well as a decoder stack. There, "attention" referred to how the decoder blocks decided where to focus in the message received from the encoding stage, while "self-attention" was the term coined for this technique being applied inside the stacks themselves (i.e., between a stack's internal blocks). With GPT-2, only the (now redundantly-named) self-attention remains.

Resuming from the above, there are two reasons why this might look complicated. For one, the "triplication" of tokens introduced, in Transformer, through the "query - key - value" frame[^1]. And secondly, the additional batching introduced by having not just one, but several, parallel, independent attention-calculating processes per layer ("multi-head attention"). Walking through the code, I'll point to both as they make their appearance.

We again start with module initialization. This is how `nn_gpt2_attention()` lists its components:

``` r
# key, query, value projections for all heads, but in a batch
self$c_attn <- nn_linear(n_embd, 3 * n_embd)
# output projection
self$c_proj <- nn_linear(n_embd, n_embd)

# regularization
self$attn_dropout <- nn_dropout(pdrop)
self$resid_dropout <- nn_dropout(pdrop)

# causal mask to ensure that attention is only applied to the left in the input sequence
self$bias <- torch_ones(max_pos, max_pos)$
  bool()$
  tril()$
  view(c(1, 1, max_pos, max_pos)) |>
  nn_buffer()
```

Besides two dropout layers, we see:

- A linear module that effectuates the above-mentioned triplication. Note how this is different from just having three identical versions of a token: Assuming all representations were initially mostly equivalent (through random initialization, for example), they will not remain so once we've begun to train the model.
- A module, called `c_proj`, that applies a final affine transformation. We will need to look at usage to see what this module is for.
- A *buffer* -- a tensor that is part of a module's state, but exempt from training -- that makes sure that attention is not applied to previous-block output that "lies in the future". Basically, this is achieved by masking out future tokens, making use of a lower-triangular matrix.

As to `forward()`, I am splitting it up into easy-to-digest pieces.

As we enter the method, the argument, `x`, is shaped just as expected, for a language model: batch dimension times sequence length times embedding dimension.

    x$shape
    [1]   1  24 768

Next, two batching operations happen: (1) triplication into queries, keys, and values; and (2) making space such that attention can be computed for the desired number of attention heads all at once. I'll explain how after listing the complete piece.

``` r
# batch size, sequence length, embedding dimensionality (n_embd)
c(b, t, c) %<-% x$shape

# calculate query, key, values for all heads in batch and move head forward to be the batch dim
c(q, k, v) %<-% ((self$c_attn(x)$
  split(self$n_embd, dim = -1)) |>
  map(\(x) x$view(c(b, t, self$n_head, c / self$n_head))) |>
  map(\(x) x$transpose(2, 3)))
```

First, the call to `self$c_attn()` yields query, key, and value vectors for each embedded input token. `split()` separates the resulting matrix into a list. Then `map()` takes care of the second batching operation. All of the three matrices are re-shaped, adding a fourth dimension. This fourth dimension takes care of the attention heads. Note how, as opposed to the multiplying process that triplicated the embeddings, this divides up what we have among the heads, leaving each of them to work with a subset inversely proportional to the number of heads used. Finally, `map(\(x) x$transpose(2, 3)` mutually exchanges head and sequence-position dimensions.

Next comes the computation of attention itself.

``` r
# causal self-attention; Self-attend: (B, nh, T, hs) x (B, nh, hs, T) -> (B, nh, T, T)
att <- q$matmul(k$transpose(-2, -1)) * (1 / sqrt(k$size(-1)))
att <- att$masked_fill(self$bias[, , 1:t, 1:t] == 0, -Inf)
att <- att$softmax(dim = -1)
att <- self$attn_dropout(att)
```

First, similarity between queries and keys is computed, matrix multiplication effectively being a batched dot product. (If you're wondering about the final division term in line one, this scaling operation is one of the few aspects where GPT-2 differs from its predecessor. Check out the paper if you're interested in the related considerations.) Next, the aforementioned mask is applied, resultant scores are normalized, and dropout regularization is used to encourage sparsity.

Finally, the computed *attention*[^2] needs to be passed on to the ensuing layer. This is where the value vectors come in -- those members of this trinity that we haven't yet seen in action.

``` r
y <- att$matmul(v) # (B, nh, T, T) x (B, nh, T, hs) -> (B, nh, T, hs)
y <- y$transpose(2, 3)$contiguous()$view(c(b, t, c)) # re-assemble all head outputs side by side

# output projection
y <- self$resid_dropout(self$c_proj(y))
y
```

Concretely, what the matrix multiplication does here is weight the value vectors by the *attention*, and add them up. This happens for all attention heads at the same time, and really represents the outcome of the algorithm as a whole.

Remaining steps then restore the original input size. This involves aligning the results for all heads one after the other, and then, applying the linear layer `c_proj` to make sure these results are not treated equally and/or independently, but combined in a useful way. Thus, the projection operation hinted at here really is a made up of a mechanical step (`view()`) and an "intelligent" one (transformation by `c_proj()`).

#### Transformer block up close: Feed-forward network (MLP)

Compared to the first, the attention module, there really is not much to say about the second core component of the transformer block (`nn_gpt2_mlp()`). It really is "just" an MLP -- no "tricks" involved. Two things deserve pointing out, though.

First, you may have heard about the MLP in a transformer block working "position-wise", and wondered what is meant by this. Consider what happens in such a block:

``` r
x <- x + self$attn(self$ln_1(x))
x + self$mlp(self$ln_2(x))
```

The MLP receives its input (almost) directly from the attention module. But that, as we saw, was returning tensors of size \[`batch size`, `sequence length`, embedding dimension\]. Inside the MLP -- cf. its `forward()` -- the number of dimensions never changes:

``` r
x |>
  self$c_fc() |>       # nn_linear(n_embd, 4 * n_embd)
  self$act() |>        # nn_gelu(approximate = "tanh")
  self$c_proj() |>     # nn_linear(4 * n_embd, n_embd)
  self$dropout()       # nn_dropout(pdrop)
```

Thus, these transformations are applied to all elements in the sequence, *independently*.

Second, since this is the only place where it appears, a note on the activation function employed. GeLU stands for "Gaussian Error Linear Units", proposed in (Hendrycks and Gimpel 2020). The idea here is to combine ReLU-like activation effects with regularization/stochasticity. In theory, each intermediate computation would be weighted by its position in the (Gaussian) cumulative distribution function -- effectively, by how much bigger (smaller) it is than the others. In practice, as you see from the module's instantiation, an approximation is used.

And that's it for GPT-2's main actor, the repeated transformer block. Remain two things: what happens before, and what happens thereafter.

#### From words to codes: Token and position embeddings

Admittedly, if you tokenize the input dataset as required (using the matching tokenizer from Hugging Face -- see below), you do not really end up with *words*. But still, the well-established fact holds: Some change of representation has to happen if the model is to successfully extract linguistic knowledge. Like many Transformer-based models, the GPT family encodes tokens in two ways. For one, as word embeddings. Looking back to `nn_gpt2_model()`, the top-level module we started this walk-through with, we see:

``` r
wte = nn_embedding(vocab_size, n_embd)
```

This is useful already, but the representation space that results does not include information about semantic relations that may vary with *position in the sequence* -- syntactic rules, for example, or phrase pragmatics. The second type of encoding remedies this. Referred to as "position embedding", it appears in `nn_gpt2_model()` like so:

``` r
wpe = nn_embedding(max_pos, n_embd)
```

Another embedding layer? Yes, though this one embeds not tokens, but a pre-specified number of valid positions (ranging from 1 to 1024, in GPT's case). In other words, the network is supposed to *learn* what position in a sequence entails. This is an area where different models may vary vastly. The original Transformer employed a form of sinusoidal encoding; a more recent refinement is found in, e.g., GPT-NeoX (Su et al. 2021).

Once both encodings are available, they are straightforwardly added (see `nn_gpt2_model()$forward()`):

``` r
tok_emb <- self$transformer$wte(x) 
pos <- torch_arange(1, x$size(2))$to(dtype = "long")$unsqueeze(1) 
pos_emb <- self$transformer$wpe(pos)
x <- self$transformer$drop(tok_emb + pos_emb)
```

The resultant tensor is then passed to the chain of transformer blocks.

#### Output

Once the transformer blocks have been applied, the last mapping is taken care of by `lm_head`:

``` r
x <- self$lm_head(x) # nn_linear(n_embd, vocab_size, bias = FALSE)
```

This is a linear transformation that maps internal representations back to discrete vocabulary indices, assigning a score to every index. That being the model's final action, it is left to the sample generation process is to decide what to make of these scores. Or, put differently, that process is free to choose among different established techniques. We'll see one -- pretty standard -- way in the next section.

This concludes model walk-through. I have left out a few details (such as weight initialization); consult [gpt.R](https://github.com/mlverse/minhub/blob/main/R/gpt2.R) if you're interested.

## End-to-end-usage, using pre-trained weights

It's unlikely that many users will want to train GPT-2 from scratch. Let's see, thus, how we can quickly set this up for sample generation.

#### Create model, load weights, get tokenizer

The Hugging Face [model hub](https://huggingface.co/models) lets you access (and download) all required files ([weights](https://huggingface.co/gpt2/blob/main/model.safetensors) and [tokenizer](https://huggingface.co/gpt2/blob/main/tokenizer.json)) directly from the [GPT-2 page](https://huggingface.co/gpt2/tree/main). All files are versioned; we use the most recent version.

``` r
 identifier <- "gpt2"
 revision <- "e7da7f2"
 # instantiate model and load Hugging Face weights
 model <- gpt2_from_pretrained(identifier, revision)
 # load matching tokenizer
 tok <- tok::tokenizer$from_pretrained(identifier)
 model$eval()
```

#### tokenize

Decoder-only transformer-type models don't need a prompt. But usually, applications will want to pass input to the generation process. Thanks to `tok`, tokenizing that input couldn't be more convenient:

``` r
idx <- torch_tensor(
  tok$encode(
    paste(
      "No duty is imposed on the rich, rights of the poor is a hollow phrase...)",
      "Enough languishing in custody. Equality"
    )
  )$
    ids
)$
  view(c(1, -1))
idx
```

    torch_tensor
    Columns 1 to 11  2949   7077    318  10893    319    262   5527     11   2489    286    262

    Columns 12 to 22  3595    318    257  20596   9546   2644  31779   2786   3929    287  10804

    Columns 23 to 24    13  31428
    [ CPULongType{1,24} ]

#### Generate samples

Sample generation is an iterative process, the model's last prediction getting appended to the -- growing -- prompt.

``` r
prompt_length <- idx$size(-1)

for (i in 1:30) { # decide on maximal length of output sequence
  # obtain next prediction (raw score)
  with_no_grad({
    logits <- model(idx + 1L)
  })
  last_logits <- logits[, -1, ]
  # pick highest scores (how many is up to you)
  c(prob, ind) %<-% last_logits$topk(50)
  last_logits <- torch_full_like(last_logits, -Inf)$scatter_(-1, ind, prob)
  # convert to probabilities
  probs <- nnf_softmax(last_logits, dim = -1)
  # probabilistic sampling
  id_next <- torch_multinomial(probs, num_samples = 1) - 1L
  # stop if end of sequence predicted
  if (id_next$item() == 0) {
    break
  }
  # append prediction to prompt
  idx <- torch_cat(list(idx, id_next), dim = 2)
}
```

To see the output, just use `tok$decode()`:

``` r
tok$decode(as.integer(idx))
```

    [1] "No duty is imposed on the rich, rights of the poor is a hollow phrase...
         Enough languishing in custody. Equality is over"

To experiment with text generation, just copy the self-contained file, and try different sampling-related parameters. (And prompts, of course!)

As always, thanks for reading!

Photo by <a 
href="https://unsplash.com/@marjan_blan?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Marjan
Blan</a> on <a 
href="https://unsplash.com/photos/UDdkJlfn7cU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Ba, Jimmy Lei, Jamie Ryan Kiros, and Geoffrey E. Hinton. 2016. *Layer Normalization*. <https://arxiv.org/abs/1607.06450>.

Bahdanau, Dzmitry, Kyunghyun Cho, and Yoshua Bengio. 2014. "Neural Machine Translation by Jointly Learning to Align and Translate." *CoRR* abs/1409.0473. <http://arxiv.org/abs/1409.0473>.

Hendrycks, Dan, and Kevin Gimpel. 2020. *Gaussian Error Linear Units (GELUs)*. <https://arxiv.org/abs/1606.08415>.

Radford, Alec, and Karthik Narasimhan. 2018. "Improving Language Understanding by Generative Pre-Training."

Radford, Alec, Jeff Wu, Rewon Child, David Luan, Dario Amodei, and Ilya Sutskever. 2019. "Language Models Are Unsupervised Multitask Learners."

Su, Jianlin, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. 2021. "RoFormer: Enhanced Transformer with Rotary Position Embedding." *arXiv Preprint arXiv:2104.09864*.

Vaswani, Ashish, Noam Shazeer, Niki Parmar, et al. 2017. *Attention Is All You Need*. <https://arxiv.org/abs/1706.03762>.

[^1]: If this terminology is unfamiliar, you'll find a nice (and very popular) introduction [here](http://jalammar.github.io/illustrated-transformer/).

[^2]: I am italicizing the word so as to hint at a special way of using the term. While the expression in itself does sound rather strange, *attention* is often employed to signify the state reached after normalizing the -- usually seen as "raw" -- *scores*.
