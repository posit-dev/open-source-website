---
title: "LLaMA in R with Keras and TensorFlow"
description: |
  Implementation and walk-through of LLaMA, a Large Language Model, in R, with TensorFlow and Keras.
date: 2023-05-25T00:00:00.000Z
categories:
  - TensorFlow/Keras
  - R
  - Generative Models
  - Natural Language Processing
author:
  - name: Tomasz Kalinowski
    affiliation: Posit
    affiliation_url: https://www.posit.co/
people:
  - Tomasz Kalinowski
image: thumbnail.jpg
ported_from: ai
port_status: raw
---



OpenAI's chatGPT has awakened a collective awareness of what Large
Language Models (LLMs) are capable of. With that awakening comes a daily
march of LLM news: new products, new features, new models, new
capabilities, (and new worries). It seems we're in the early stages of a
Cambrian explosion of LLMs and LLM powered tools; it's not yet clear how
LLMs will impact and influence our professional and personal lives, but
it seems clear that they will, in some way.

Since LLMs are here to stay, it's worthwhile to take some time to
understand how these models work from a first-principles perspective.
Starting with the mechanics can help foster durable intuitions that will
inform our usage of these models now and in the future. (Especially if
the future is one where LLMs are a staple of the data scientist's
toolbox, as common as an `lm()` function call).

And what better way is there to learn than by doing. So with that
preamble, in this post we'll walk through an implementation of an LLM,
[LLaMA](https://arxiv.org/abs/2302.13971) (Touvron et al. 2023)
specifically, in TensorFlow and Keras, with the goal being to develop
understanding first, capability second.

Why LLaMA? With the sheer volume of LLM related content and news out
there, it can seem daunting to know where to get started. Almost weekly
it seems there is a new model announced. Browsing some hubs of LLM
activity ([HuggingFace](https://huggingface.co/models),
[TFHub](https://tfhub.dev/s?module-type=text-language-model),
[reddit](https://www.reddit.com/r/deeplearning/),
[HackerNews](https://hn.algolia.com/?q=LLM)) muddies the waters even
more. How to pick a specific model?

Of the many LLM-related news items in the past months, one that stands
head-and-shoulders above the crowd is the [release of
LLaMA](https://ai.facebook.com/blog/large-language-model-llama-meta-ai/),
a modern, foundational LLM made available to the public by Meta AI in
February 2023. On common benchmarks, LLaMA outperforms OpenAI's GPT-3,
while being substantially smaller (though still *large*).

LLaMA is a great starting place because it is a simple and modern
architecture, has excellent performance on benchmarks, and is open. The
model architecture has had just a few new ideas incorporated into it since
the original Transformer architecture first described in,
"[Attention Is All You Need](https://arxiv.org/abs/1706.03762)"
published from Google (Vaswani et al. 2017). Four different sizes of
LLaMA have been released: 7 billion and 13 billion parameter models
trained on 1 Trillion tokens, and 33 billion and 65 billion parameter
models trained on 1.4 trillion tokens. This is an enormous amount of
training data these models have seen--the largest 65B model has been
trained on approximately the ["Chinchilla
compute-optimum"](https://arxiv.org/abs/2203.15556) (Hoffmann et al. 2022)
number of tokens, while the smaller LLaMAs are substantially
beyond that optimum. In this blog post we'll focus on the smallest, 7B
parameter LLaMA model, which you can comfortably load locally and run on
CPU with only 64Gb of RAM.

While not strictly necessary, to follow along locally, you'll probably
want to acquire the pre-trained LLaMA weights [one
way](https://forms.gle/jk851eBVbX1m5TAv5) or
[another](https://github.com/facebookresearch/llama/pull/73). Note, the
weights do come with their own license, which you can preview
[here](https://github.com/facebookresearch/llama/pull/234).

So, without further ado, let's get started.

### Setup

First, we'll want to install the required R and Python packages, and
configure a virtual environment:

``` r
remotes::install_github(c("rstudio/reticulate",
                          "rstudio/tensorflow",
                          "rstudio/keras"))
# reticulate::install_python("3.10:latest")                          
reticulate::virtualenv_create("./.venv", version = "3.10:latest")
tensorflow::install_tensorflow(envname = "./.venv", version = "release",
                               extra_packages = "tensorflow-text")
```

With that out of the way, let's load some packages and prepare our R
session:

``` r
library(purrr)
library(envir)

library(tensorflow)
library(tfautograph)
library(keras)

use_virtualenv("./.venv")
options(tensorflow.extract.warn_tensors_passed_asis = FALSE)

attach_eval({
  import_from(glue, glue)
  import_from(jsonlite, read_json)
  import_from(withr, with_dir, with_options)
  import_from(keras$layers, Dense)
  np <- reticulate::import("numpy", convert = FALSE)

  seq_len0 <- function(x) seq.int(from = 0L, length.out = x)
})
```

If you've acquired the pre-trained weights, it'll be convenient to
convert them from the torch checkpoint format to something that's more
framework agnostic (you only need to do this once, of course):

``` r
# reticulate::py_install("torch", pip = TRUE)
torch <- reticulate::import("torch", convert = FALSE)
with_dir("~/github/facebookresearch/llama/weights/LLaMA/7B", {
  pretrained_weights <- torch$load("consolidated.00.pth",
                                   map_location = "cpu")
  for (name in names(pretrained_weights)) {
    filename <- sprintf("%s.npy", name)
    array <- pretrained_weights[[name]]$numpy()
    np$save(filename, array)
    message(glue(
      "wrote: '{basename(filename)}' with shape: {array$shape}"))
  }
})
```

We'll also define a helper function so we can avoid having to retype the
full path to our weights:

``` r
weights_path <- function(filename) normalizePath(file.path(
  "~/github/facebookresearch/llama/weights/LLaMA/",
  glue(filename, .envir = parent.frame())), mustWork = TRUE)
```

And load the model configuration parameters specific to the 7B LLaMA,
which we'll use to build the model.

``` r
params <- read_json(weights_path("7B/params.json"))
str(params)
```

    List of 6
     $ dim        : int 4096
     $ multiple_of: int 256
     $ n_heads    : int 32
     $ n_layers   : int 32
     $ norm_eps   : num 1e-06
     $ vocab_size : int -1

### Tokenizer

The first component to LLaMA is the tokenizer, which converts text to a
sequence of integers. The LLaMA model uses the
[SentencePiece](https://github.com/google/sentencepiece) tokenizer from
Google. SentencePiece is available as a TensorFlow graph operation
through
[`tf_text.SentencepieceTokenizer`](https://www.tensorflow.org/text/api_docs/python/text/SentencepieceTokenizer),
and also as a Keras layer in
[`keras_nlp.tokenizers.SentencepieceTokenizer`](https://keras.io/api/keras_nlp/tokenizers/sentence_piece_tokenizer/).
By choice of a coin flip, we'll use the lower-level `tf_text` interface.

``` r
tf_text <- reticulate::import("tensorflow_text")
tokenizer_path <- weights_path("tokenizer.model")
tokenizer <- tf_text$SentencepieceTokenizer(
  tf$io$gfile$GFile(tokenizer_path, "rb")$read(),
  add_bos = TRUE, add_eos = FALSE,
)
```

Let's test it out with a prompt:

``` r
prompt <- "The best way to attract bees"
tokenizer$tokenize(prompt)
```

    tf.Tensor([    1   450  1900   982   304 13978   367   267], shape=(8), dtype=int32)

``` r
prompt |> tokenizer$tokenize() |> tokenizer$detokenize()
```

    tf.Tensor(b'The best way to attract bees', shape=(), dtype=string)

Let's define a `show_tokens()` helper function and play with the
tokenizer a little.

``` r
show_tokens <- function(what) {
  if(is.character(what))
    token_ids <- what |> tokenizer$tokenize() |> as.integer()
  else
    token_ids <- as.integer(what)
  tokens <- token_ids |>
    map_chr(function(id) {
      id |>
        as_tensor(shape = c(1)) |>
        tokenizer$detokenize() |>
        as.character()
    })

  names(tokens) <- token_ids
  tokens
}

show_tokens(prompt)
```

            1       450      1900       982       304     13978       367       267
           ""     "The"    "best"     "way"      "to" "attract"      "be"      "es"

Note that "bees" is two tokens. Not every token corresponds to a word.
For example, one non-word token we can reliably expect to show up in a
tokenizer trained on a corpus of English text is "ing". However, *when* the
"ing" token shows up will not always follow your intuitions, because
common words get their own token id, even if they can be decomposed into
multiple tokens.

``` r
show_tokens("ing")
```

        1  2348
       "" "ing"

``` r
show_tokens("working")
```

            1      1985
           "" "working"

``` r
show_tokens("flexing")
```

         1   8525    292
        "" "flex"  "ing"

``` r
show_tokens("wonking")
```

         1   2113   9292
        ""  "won" "king"

Another thing to note about the tokenizer is that each token sequence
starts with token id `1`. This is a special *beginning-of-sequence*
token that we requested be added when we loaded the tokenizer with
`add_bos = TRUE`. There are two other such special tokens that we will
encounter later: an *end-of-sequence* special tokens with id `2`, and an
*unknown-token* with id `0`.

``` r
as.character(tokenizer$id_to_string(0L))
```

    [1] "<unk>"

``` r
as.character(tokenizer$id_to_string(1L))
```

    [1] "<s>"

``` r
as.character(tokenizer$id_to_string(2L))
```

    [1] "</s>"

``` r
show_tokens(c(1, 0, 2))
```

        1     0     2
       "" " ⁇ "    ""

Overall, there are 32,000 tokens.

``` r
as.integer(tokenizer$vocab_size())
```

    [1] 32000

One last observation is that the more frequently encountered tokens are
assigned lower ids.

``` r
show_tokens(seq(50, len = 10))
```

     50  51  52  53  54  55  56  57  58  59
    "/" "0" "1" "2" "3" "4" "5" "6" "7" "8"

``` r
show_tokens(seq(100, len = 10))
```

    100 101 102 103 104 105 106 107 108 109
    "a" "b" "c" "d" "e" "f" "g" "h" "i" "j"

``` r
show_tokens(seq(1000, len = 10))
```

       1000    1001    1002    1003    1004    1005    1006    1007    1008    1009
      "ied"    "ER"  "stat"   "fig"    "me"   "von" "inter"  "roid"  "ater" "their"

``` r
show_tokens(seq(10000, len = 10))
```

       10000    10001    10002    10003    10004    10005    10006    10007
       "ång"  "citep"    "Ill"   "rank" "sender"   "beim"    "рак" "compat"
       10008    10009
    "occurs"  "diese"

``` r
show_tokens(seq(20000, len = 10))
```

        20000     20001     20002     20003     20004     20005     20006     20007
      "admit" "Comment"     "стя"    "Vien"      "ці"  "permut"     "cgi"    "crít"
        20008     20009
    "Console"    "ctic"

``` r
show_tokens(seq(to = as.integer(tokenizer$vocab_size()) - 1, len = 10))
```

    31990 31991 31992 31993 31994 31995 31996 31997 31998 31999
      "ὀ"  "げ"  "べ"  "边"  "还"  "黃"  "왕"  "收"  "弘"  "给"

Moving on, the next step after tokenization is embedding. An embedding
layer is effectively a dictionary lookup that converts an integer (token
id) to a 1-d float array. For this we can use the standard keras
`Embedding` layer.

``` r
tok_embeddings <- keras$layers$Embedding(
  input_dim = tokenizer$vocab_size(),
  output_dim = params$dim,
  embeddings_initializer =
    \(...) np$load(weights_path("7B/tok_embeddings.weight.npy"))
)

tok_embeddings(3L) |> str()
```

    <tf.Tensor: shape=(4096), dtype=float32, numpy=…>

``` r
prompt |> # "The best way to attract bees"
  tokenizer$tokenize() |>
  tok_embeddings() |>
  str()
```

    <tf.Tensor: shape=(8, 4096), dtype=float32, numpy=…>

### `TransformerBlock`

Once it's tokenized and embedded, the input then passes through the bulk
of the model, a sequence of repeating `TransformerBlock` layers. The 7B
model has 32 of these `TransformerBlock` layers, while the 65B model has
80 of them.

``` r
weights_path("7B/params.json")  |> read_json() |> _$n_layers
```

    [1] 32

``` r
weights_path("65B/params.json") |> read_json() |> _$n_layers
```

    [1] 80

Here is what the transformer block looks like:

``` r
TransformerBlock(keras$layers$Layer) %py_class% {
  initialize <- function(attn_head_size, attn_n_heads,
                         norm_eps = k_epsilon(), ...,
                         block_id = NULL) {
    super$initialize(...)

    self$attention <- Attention(attn_head_size, attn_n_heads,
                                block_id = block_id)

    self$feed_forward <- FeedForward(
      hidden_dim = 4 * attn_head_size * attn_n_heads,
      block_id = block_id)

    self$attention_norm <- RMSNorm(eps = norm_eps,
                                   block_id = block_id,
                                   feeds_into = "attention")
    self$feed_forward_norm <- RMSNorm(eps = norm_eps,
                                      block_id = block_id,
                                      feeds_into = "ffn")
  }

  call <- function(x) {

    # norm and attention
    x2 <- x |>
      self$attention_norm() |>
      self$attention()

    x <- x + x2 # add residual

    # norm and swiglu
    x2 <- x %>%
      self$feed_forward_norm() %>%
      self$feed_forward()

    x <- x + x2 # residual again

    x
  }
}
```

While there is not a lot of code, there are a lot of ideas packed in
there. This block forms the main trunk of the model, so it's worth
taking the time to go through it slowly.

We implement the `TransformerBlock` as a subclassed
`keras.layers.Layer`. This is gives us some niceties like the ability to
compose with other Keras layers, but these are mostly irrelevant to the
purpose of this blog post; we could just as easily implement this as,
for example, a vanilla R6 class. Our `TransformerBlock` class has two
methods: `initialize`, called when we first create the block, and
`call`, called when we run the forward pass of the block.

In `initialize`, we create 4 layers: an `Attention` layer, a
`FeedForward` layer, and 2 `RMSNorm` layers. We'll take a close look at
each of these soon, but even before we do so, we can see how they fit
together by looking at the `TransformerBlock$call()` method.

The `call` method has a few simple ideas. In no particular order, the
first one to observe is the composition pattern of adding residuals.

``` r
x2 <- x |> ...
x <- x + x2 # add residual x to x2
```

This is a common pattern that helps with model training, and especially
to help with the [vanishing gradient
problem](https://en.wikipedia.org/wiki/Vanishing_gradient_problem). It's
a skip-connection in the other-wise linear sequence of matrix
transformations. It reinjects information (during the forward pass), and
gradients (during back propagation), back into the trunk. You can think
of these residual connections as freeing the learnable layers in-between
(the `...` in the pseudo code) from the burden of having to
"pass-through" or "preserve" information in `x`, allowing the weights to
instead focus on learning transformations that are, (in corporatese
vernacular), *value-adding*.

The next composition pattern to note is the repeating usage of a
normalization layer:

``` r
x2 <- x |> norm() |> ...
x <- x + x2
```

There are many kinds of normalization layers, but to slightly
over-generalize, they can all be thought of as a stabilizer that helps
with training. Like their deep-learning cousins the regularizers, their
main function is to keep values passing through in a sensible range--in
the ball park of (-1, 1), typically. We'll take a closer look at
`RMSNorm` soon.

Stripped of two tricks that are mostly there to help the model train,
residuals and normalization, the core of the `TransformerBlock` is just
this:

``` r
x |> attention() |> feed_forward()
```

In a moment we'll see that that `feed_foward` is a slightly fancier
variation of a conventional sequence of `Dense` layer. Before we get
there we can we safely skip ahead to distill the following intuition: a
`TransformerBlock` is basically an `Attention` layer followed by a few
(fancy) dense layers, with some simple composition patterns (tricks)
that help with training. `Attention` is the heart of the model: it's the
most interesting, and also the most involved.

With the framing in place, let's go through and take a closer look at
`RMSNorm`, `FeedForward`, and then with the foundation in place, we'll
turn our attention to `Attention`.

### `RMSNorm`

``` r
RMSNorm(keras$layers$Layer) %py_class% {
  initialize <-
    function(eps = 1e-6, ..., block_id = NULL, feeds_into = NULL) {
      super$initialize(...)
      self$eps <- eps
      self$block_id <- block_id
      self$feeds_into <- feeds_into
    }

  build <- function(input_shape) {
    # input_shape == (batch_size, seqlen, params$dim)
    # self$w will broadcast over batch_size and seqlen dims.
    # w_shape == (1, 1, params$dim)
    w_shape <- rep(1L, length(input_shape))
    w_shape[length(input_shape)] <- as.integer(input_shape) |> tail(1L)

    # define a local function that will load
    # the pretrained-weights if we supplied `block_id` and `feeds_into`
    import_from({self}, block_id, feeds_into)
    initializer <-if (is.null(block_id))
      "ones"
      else if (block_id >=0) {
        \(...) weights_path("7B/layers.{block_id}.{feeds_into}_norm.weight.npy") |>
               np$load() |> np$expand_dims(0:1)
      } else if(block_id == -1)
        # load weights for the final output normalization layer, which is not
        # part of a TransformerBlock
        \(...) weights_path("7B/norm.weight.npy") |>
               np$load() |> np$expand_dims(0:1)

    self$w <- self$add_weight(shape = w_shape,
                              initializer = initializer,
                              trainable = TRUE)
  }

  rrms <- function(x) {
    # reciprocal root mean square along the last axis
    x %>% # (batch_size, seqlen, n_features)
      tf$math$square() %>%
      tf$reduce_mean(axis = -1L, keepdims = TRUE) %>% # (batch_size, seqlen, 1)
      tf$math$add(self$eps) %>% # for numerical stability
      tf$math$rsqrt()
  }

  call <- function(x) {
    x * self$rrms(x) * self$w
  }
}
```

`RMSnorm()` has a single trainable tensor `w`. In the forward pass, each
value in the input is multiplied by the reciprocal-root-mean-square of
all the values in the feature axis and by `w`. Certainly a mouthful, but
just a simple sequence of arithmetic transformations in the end,
designed for the express purpose of adjusting the range of values
passing through.

Let's kick the tires on it:

``` r
norm <- RMSNorm()
m <- matrix(c(0, 1,
              2, 3), nrow = 2)
norm(m)
```

    tf.Tensor(
    [[0.         1.4142132 ]
     [0.44721353 1.3416406 ]], shape=(2, 2), dtype=float32)

``` r
norm(m*10)
```

    tf.Tensor(
    [[0.         1.4142137 ]
     [0.44721362 1.3416408 ]], shape=(2, 2), dtype=float32)

``` r
norm(m*100)
```

    tf.Tensor(
    [[0.        1.4142137]
     [0.4472136 1.3416408]], shape=(2, 2), dtype=float32)

### `FeedForward`

Next up is `FeedForward()`

``` r
FeedForward(keras$layers$Layer) %py_class% {

  initialize <- function(hidden_dim, multiple_of = 256L,
                         ..., block_id = NULL) {
    super$initialize()

    if(!is.null(multiple_of)) {
      hidden_dim <- hidden_dim %>%
        { as.integer( . * (2/3)) } %>%
        { (. + multiple_of - 1) %/% multiple_of } %>%
        { . * multiple_of }
    }

    self$hidden_dim <- hidden_dim
    self$block_id <- block_id
  }

  build <- function(input_shape) {
    output_dim <- input_shape |> as.integer() |> tail(1)

    if(is.null(self$block_id))
      load_weight <- \(...) NULL
    else
      load_weight <- \(name) \(...) np$load(weights_path(
        "7B/layers.{self$block_id}.feed_forward.{name}.weight.npy"))$`T`

    self$w1 <- Dense(self$hidden_dim, use_bias = FALSE,
                     kernel_initializer = load_weight("w1"))
    self$w2 <- Dense(output_dim, use_bias = FALSE,
                     kernel_initializer = load_weight("w2"))
    self$w3 <- Dense(self$hidden_dim, use_bias = FALSE,
                     kernel_initializer = load_weight("w3"))

    super$build(input_shape)
  }

  call <- function(x) {
    import_from({self}, w1, w2, w3)
    import_from(tf$nn, silu)

    x %>%
      { silu(w1(.)) * w3(.) } %>% # SwiGLU
      w2()
  }

}
```

`FeedForward` consists of three `Dense` layers. `initialize` does some
simple arithmetic, munging on the input value `hidden_dim` to ensure the
size is a performant multiple of 256, and `build` is mostly boiler plate
for creating the layers and loading the weights.

The novelty of `FeedForward()` is in the `call()` method, where rather
than composing the `Dense` layers in a conventional sequential model
with, say, ReLU activations in between and maybe some dropout, the
layers are composed to form a "SwiGLU" unit. The publication by Shazeer (2020)
of SwiGLU and other variations on GLU is an exemplar of the types
of explorations and improvements around the Transformer architecture
since its initial publication in
[2017](https://arxiv.org/abs/1706.03762); a steady accretion of
enhancements that has brought us to today. The `Feedforward$call()` is
just a single SwiGLU followed by a linear projection. In its essence,
it's a clever composition of three (learned) linear projections, an
element-wise multiplication, and a [`silu()`
activation](https://www.tensorflow.org/api_docs/python/tf/nn/silu)
function.

Perhaps the most surprising observation to make here is the relative
dearth of activation functions, or even non-linearities, not just in
`FeedForward`, but overall. The `silu()` in this feedforward, the
reciprocal-root-mean-square in `RMSnorm()`, and a `softmax()` in
`Attention()` are the only non-linear transformations in the whole
sequence of `TransformerBlock`s. Everything else is a linear
transformation!

### `Attention`

Finally, let's turn our attention to `Attention()`.

``` r
Attention(keras$layers$Layer) %py_class% {
  initialize <- function(head_size, n_heads,
                         ..., block_id = NULL) {
    super$initialize(...)

    self$head_size <- head_size
    self$n_heads <- n_heads

    if (is.null(block_id))
      load_weight <- function(name) NULL
    else
      load_weight <- \(name) \(...) np$load(weights_path(
        "7B/layers.{block_id}.attention.{name}.weight.npy"))$`T`

    Dense <- function(name) keras$layers$Dense(
      units = n_heads * head_size,
      use_bias = FALSE,
      kernel_initializer = load_weight(name)
    )

    self$wq <- Dense("wq")
    self$wk <- Dense("wk")
    self$wv <- Dense("wv")
    self$wo <- Dense("wo")
  }

  call <- function(x) {
    c(batch_size, seqlen, n_features) %<-% tf$unstack(tf$shape(x))

    # 1. project (linear transform) x into
    #    query, key, and value tensors
    # 2. reshape q k v, splitting out the last dim (n_features)
    #    into n_heads independent subspaces,
    #    each with size head_size.
    #    (n_features == head_size * n_heads)
    split_heads_shape <- c(batch_size, seqlen,
                           self$n_heads, self$head_size)
    q <- x |> self$wq() |> tf$reshape(split_heads_shape)
    k <- x |> self$wk() |> tf$reshape(split_heads_shape)
    v <- x |> self$wv() |> tf$reshape(split_heads_shape)

    # embed positional information in query and key
    # (bsz, seqlen, n_heads, head_size)
    q %<>% apply_rotary_embedding()
    k %<>% apply_rotary_embedding()

    # reshape:
    #   move heads out of the last 2 axes,
    #   so later matmuls are performed across the subspaces (heads)
    #   between (seqlen, head_size) axes
    v <- tf$transpose(v, c(0L, 2L, 1L, 3L)) # (bsz, n_heads, seqlen, head_size)
    q <- tf$transpose(q, c(0L, 2L, 1L, 3L)) # (bsz, n_heads, seqlen, head_size)
    k <- tf$transpose(k, c(0L, 2L, 3L, 1L)) # (bsz, n_heads, head_size, seqlen)

    # calculate and normalize attention scores
    scores <- q %*% k                       # (bsz, n_heads, seqlen, seqlen)
    scores <- scores / sqrt(self$head_size) # scale

    # apply causal mask, so the model can't "look ahead" during training
    mask <- make_mask(seqlen, dtype = scores$dtype)
    scores %<>% { . + mask }

    scores <- tf$nn$softmax(scores, axis = -1L)

    # adjust values tensor with attention scores
                      # scores (bsz, n_heads, seqlen, seqlen)
                      # v      (bsz, n_heads, seqlen, head_size)
    output <- scores %*% v   # (bsz, n_heads, seqlen, head_size)

    # combine heads back into a single features dim,
    # so Attention output_shape==input_shape
    output <- output |>
      tf$transpose(c(0L, 2L, 1L, 3L)) |> # (bsz, seqlen, n_heads, head_size)
      tf$reshape(tf$shape(x))            # (bsz, seqlen, n_heads * head_size)

    # one more trainable linear projection for good luck
    output <- self$wo(output) # (bsz, seqlen, n_heads * head_size)

    output
  }
}
```

`Attention` in LLaMA is similar but not identical to the Attention
described in the [original Transformers
paper](https://arxiv.org/abs/1706.03762) (and available as a keras
builtin under `keras$layers$MultiHeadAttention()`). The core novelty is
the addition of the `apply_rotary_embedding()` function, which we'll
describe shortly. The additional novelty is balanced by the simplicity
from the fact that the layer is performing self-attention---we don't need
to pass in different query, key, and value tensors (or reason about what
that means), since the same input serves all three roles. Note that the
conventional `MultiHeadAttention()` layer is covered quite thoroughly in
the 2nd Edition of [Deep Learning with R](http://rstd.io/dlwr-2e),
including a full implementation of attention in base R.

To develop an understanding of the mechanics in a layer like this, it's
helpful to temporarily *unsee* some of the minutia that can act as a fog
obscuring the essence of the operation. In this instance, if we
temporarily strip out the `transpose()`s and `reshape()`s (as clever and
vital as they are), this is what's left:

``` r
call <- function(x) {
  # split input into three learned linear projections
  q <- x |> self$wq()
  k <- x |> self$wk()
  v <- x |> self$wv()

  # rotate q,k to inject position information.
  # cross q,k to calculate an attention score for each token pair.
  scores <- rotate(q) %*% rotate(k)   |>  normalize_scores()

  # adjust the 3rd projection with the attention scores
  output <- scores %*% v

  self$wo(output) # one more learned linear projection for good luck
}
```

Returning to the `transpose()`s and `reshapes()`, you can observe that
their purpose is to make it so that the attention calculations are
performed across `n_heads` independent subspaces, rather than in a
single larger space. The same reasoning drives this decision as that
driving usage of depthwise-separable convolutions in image models.
Empirically, for the fixed compute budget, factoring features into
independent subspaces performs better than doing the same core
operations in single larger feature space. As with all things, there is
a balance to strike between `n_heads` (the number of subspaces) and
`head_dim` (the size of each subspace). The LLaMA authors have struck
the balance like this at the various model sizes:

``` r
lapply(c("7B", "13B", "30B", "65B"), \(size) {
  p <- read_json(weights_path("{size}/params.json"))
  with(p, list(llama_size = size,
               n_heads = n_heads,
               head_dim = dim %/% n_heads))
}) |> dplyr::bind_rows()
```

    # A tibble: 4 × 3
      llama_size n_heads head_dim
      <chr>        <int>    <int>
    1 7B              32      128
    2 13B             40      128
    3 30B             52      128
    4 65B             64      128

Next lets turn our attention to the causal attention mask.

``` r
make_mask <- function(seqlen, dtype = k_floatx()) {
  x <- tf$range(seqlen)
  mask <- tf$where(x[, tf$newaxis] < x[tf$newaxis, ],
                   tf$constant(-Inf, dtype = dtype),
                   tf$constant(0, dtype = dtype))

  # broadcast over batch and heads dim
  mask[tf$newaxis, tf$newaxis, , ] # (1, 1, seqlen, seqlen)
}
```

The mask is a strictly upper triangular matrix filled with `-Inf`
values. Adding the mask to the attention scores prevents the model from
being able to "look ahead" and see the attention score for a token
pairing it hasn't seen yet at a particular position in the sequence.
This need for a mask is best thought of as a vestige from training,
an apparatus that the model needed to learn with and now it can't function without.
During training, gradients are calculated for predictions from all
token positions in a sequence, including predictions tokens where the correct
answer is *right there*, as the very next token in same sequence. The mask
prevents the model from being able to cheat and look ahead into the future,
something it won't be able to do once it's we're running it for inference.

``` r
make_mask(seqlen = 5L)
```

    tf.Tensor(
    [[[[  0. -inf -inf -inf -inf]
       [  0.   0. -inf -inf -inf]
       [  0.   0.   0. -inf -inf]
       [  0.   0.   0.   0. -inf]
       [  0.   0.   0.   0.   0.]]]], shape=(1, 1, 5, 5), dtype=float32)

### Rotary Position Embedding

Next lets turn our attention to `apply_rotary_embedding()`. This core
innovation was published by Su et al. (2022) in the paper titled
["RoFormer: Enhanced Transformer with Rotary Position Embedding"](https://arxiv.org/abs/2104.09864).

Some context:

- The bare `Attention()` mechanism doesn't leave any possibility for a
  token's position in a sequence to affect the attention scores, since
  only token-pairs are scored. Attention treats its input like a
  bag-of-tokens.

- The position of a token in a sequence is clearly important, and the
  attention layer should have access to that information.

- The absolute position of a token in a sequence is less important
  than the relative position between tokens. (Especially so for long
  sequences).

Which leads us into the complex plane. If we imagine the features as
complex numbers, we can rotate them, and we can calculate angles between
them. From the Roformers paper:

> Specifically, incorporating the relative position embedding is
> straightforward: simply rotate the affine-transformed word embedding
> vector by amount of angle multiples of its position index and thus
> interprets the intuition behind *Rotary Position Embedding*

Expanding slightly: the rotation matrix is designed so that
subsequently, after rotating our `q` and `k` token sequence embedding
the same way, the *angle* between token features is a function of the
relative distance between those tokens in the token sequence. The
relative angle between two tokens is invariant to the absolute
position of those tokens in the full sequence.

In short, the rotation injects positional information. The meaning or
interpretability of that positional information, or how it is meant to
be used, or even extracted from the result of `q %*% k`, is left to the
model to learn.

Here is the code:

``` r
apply_rotary_embedding <- function(x) {
  c(., seqlen, ., head_size) %<-%
    tf$unstack(tf$shape(x))

  rotation_matrix <- compute_rotation_matrix(seqlen, head_size)

  x %>%
    view_as_complex() %>%
    { . * rotation_matrix } %>%
    view_as_real()

}

compute_rotation_matrix <-
  function(seqlen, feature_dim, theta = 10000) {
    # `feature_dim` here is going to be attention$head_size
    # `seqlen` is going to match the token sequence length.

    t <- tf$range(seqlen, dtype = tf$float32)
    freqs <- tf$range(start = 0, limit = 1, delta = 1 / (feature_dim %/% 2),
                      dtype = tf$float32)
    tf_assert(tf$size(freqs) == feature_dim %/% 2)
    freqs <- 1.0 / (theta ^ freqs)

    # outer product; (seqlen, head_size/2)
    freqs <- tf$einsum('a,b->ab', t, freqs)

    rot_mat <- tf$complex(tf$cos(freqs), tf$sin(freqs))

    # the positional embedding will be broadcast across batch and heads dim
    rot_mat[tf$newaxis, , tf$newaxis, ] #(1, seqlen, 1, headdim/2)
  }

view_as_complex <- function(x) {
  tf$complex(x[all_dims(), `::2`],
             x[all_dims(), `2::2`])
}

view_as_real <- function(x) {
  # xs = (..., f);  xs2 = (..., f*2)
  xs <- tf$shape(x)
  xs2 <- tf$concat(list(xs[1:(length(xs)-1)],
                        xs[length(xs), drop = FALSE] * 2L),
                   axis = 0L)

  x2 <- tf$stack(list(Re(x), Im(x)), axis = -1L)

  # (..., f, 2) -> (..., f*2)
  tf$reshape(x2, xs2)
}
```

As you can see, to imagine the embedding features as existing in the
complex plane, we merely treat adjacent pairs of floats in the
underlying array as the real and imaginary part of a complex number. We
rotate the embeddings in the complex plane, then go back to imagining
the features as existing in the real plane. Again, the job of
interpreting the meaning of the features after rotation is left to the
model to learn.

We can quickly confirm that the rotary embeddings *only* rotate features
and don't scale them:

``` r
near <- function (x, y, tol = 1e-6) abs(x - y) < tol
all(near(1, Mod(compute_rotation_matrix(2048L, 128L))))
```

    tf.Tensor(True, shape=(), dtype=bool)

There is one more trick to observe before moving on: because of some of
the mathematical properties of the rotation matrix, it's possible to
avoid doing a full complex multiply operation and still arrive at the
same result. Also, since the rotation matrix never changes, it makes
sense to only compute it once and cache it, like so:

``` r
precomputed_rotation_matrix <- compute_rotation_matrix(
  seqlen = 2048L, # LLaMA max seqlen
  feature_dim = with(params, dim %/% n_heads)  # head_size
)

apply_rotary_embedding_faster <- function(x) {

  rotate_every_two <- function(x) {
    x1 <- x[all_dims(), `::2`]
    x2 <- x[all_dims(), `2::2`]
    x_ <- tf$stack(list(-x2, x1), axis = -1L)
    tf$reshape(x_, tf$shape(x))
  }

  repeat_each_twice <- function(x) {
    tf$`repeat`(x, 2L, axis = -1L)
  }

  seqlen <- tf$shape(x)[2]
  rot <- precomputed_rotation_matrix[, NA:seqlen, , ]

  cos <- Re(rot) |> repeat_each_twice()
  sin <- Im(rot) |> repeat_each_twice()

  (x * cos) + (rotate_every_two(x) * sin)
}
```

``` r
rand <- tf$random$uniform(shape(3, 8, params$n_heads, 128))
all(apply_rotary_embedding(rand) ==
    apply_rotary_embedding_faster(rand))
```

    tf.Tensor(True, shape=(), dtype=bool)

``` r
apply_rotary_embedding <- apply_rotary_embedding_faster
```

Finally, note that the rotary positional embeddings are applied within
each `Attention` layer. This is different from the original Transformer
implementation, where a positional embedding was only added once at the
head of the model. Similar to residual connections, you can think of the
presence of these repeated injections of positional information as
relieving the remaining trainable layers from the burden of allocating
some of their weights to the task of "passing through" or "preserving"
the positional information for later layers.

Positional embeddings are a rich subject that also comes up in other
deep learning architectures, like denoising diffusion (Falbel and Keydana 2023),
so time spent understanding them better is time well
spent. For the purposes of this blog post we've covered the points
needed and we'll move on to tying all pieces together. To go deeper and
develop a more mathematically informed understand of RoPE, two excellent
starting points are:

1.  [The original paper](https://arxiv.org/abs/2104.09864) by Su et al. (2022)

2.  [This blog post](https://blog.eleuther.ai/rotary-embeddings/) by
    Biderman et al. (2021)

### Tying it all together

With `Tokenizer`, `Embedding`, `TransformerBlock` (`RMSNorm`,
`Attention` `FeedForward` and `apply_rotary_embedding`) all covered,
it's time to tie all the pieces together into a `Transformer` model. We
could do this using `%py_class%` like with the other layers above, but
it's just as easy to move over to using the Keras functional API at this
point.

``` r
layer_transformer_block <- create_layer_wrapper(TransformerBlock)
layer_rms_norm <- create_layer_wrapper(RMSNorm)

# input to the model will be output from the tokenizer
input <- layer_input(shape(NA)) #, dtype = "int32")

x <- input |>
  tok_embeddings()  # instantiated earlier in the blog-post

for(block_id in seq_len0(params$n_layers)) {
  x <- x |>
    layer_transformer_block(attn_head_size = params$dim %/% params$n_heads,
                            attn_n_heads = params$n_heads,
                            norm_eps = params$norm_eps,
                            block_id = block_id)
}

# final output projection into logits of output tokens
x <- x |>
  layer_rms_norm(block_id = -1, eps = params$norm_eps) |>
  layer_dense(
    tokenizer$vocab_size(), use_bias = FALSE,
    kernel_initializer = \(...) np$load(weights_path("7B/output.weight.npy"))$`T`
  )

# slice out the logits for the last token
with_options(c(tensorflow.extract.warn_negatives_pythonic = FALSE), {
  output <- x[, -1, ]
})

llama <- keras_model(input, output) %>%
  compile(jit_compile = TRUE)
```

The input to the model is tokenized text and the output is the
(unnormalized) probabilities for each token in `tokenizer$vocab_size()`
being the next token in the sequence.

``` r
next_token_probs <- prompt %>%
  tokenizer$tokenize() %>%
  llama()

next_token_probs
```

    tf.Tensor(
    [[-2.4503722e+00 -3.4463339e+00  1.3200411e+01 ...  4.8804146e-01
      -1.3277926e+00  9.9985600e-03]], shape=(1, 32000), dtype=float32)

Sampling strategies for selecting a token from the token logits is a
rich topic, (also covered thoroughly in the [Deep Learning with
R](http://rstd.io/dlwr-2e) book), but this blog post is long enough
already. So for now, let's just take the `argmax()`.

``` r
sampler <- \(logits) tf$argmax(logits, axis = -1L, output_type = "int32")

(next_token <- sampler(next_token_probs))
```

    tf.Tensor([304], shape=(1), dtype=int32)

``` r
tokenizer$detokenize(next_token) |> as.character()
```

    [1] "to"

Let's run it for a few tokens and let LLaMa finish the sentence:

``` r
prompt_tokens <- tokenizer$tokenize("The best way to attract bees")

for (i in 1:20) {

  next_token_probs <- prompt_tokens |> llama()
  next_token <- sampler(next_token_probs)

  prompt_tokens %<>% { tf$concat(c(., next_token), axis = -1L) }

  # end of sentence
  if (as.logical(next_token == tokenizer$string_to_id(".")))
    break
}

prompt_tokens |>
  tokenizer$detokenize() |>
  as.character() |>
  strwrap(60) |> writeLines()
```

    The best way to attract bees to your garden is to plant a
    variety of flowers that bloom at different times.

### Wrapping up

In this blog post we've walked through the LLaMA architecture
implemented in R TensorFlow, including how to load pretrained weights,
and then run the model to generate a sentence. Note, much of the code in
this blog post is tailored for didactic purposes. While the
implementation of the LLaMA architecture covered in this blog post is
appropriate for training, there are a few modifications you'll want to
make before doing a lot of text generation. Those include things like:

- In the `Attention` layer, caching the `k` and `v` tensors. Then,
  after the first forward pass with the initial prompt, only feeding
  the model the one new token from the `sampler()`, rather than
  feeding the model all the tokens of the full prompt on each forward
  pass.

- Only generating the causal mask `make_mask()` and `rotary_matrix`
  slices once per forward pass, instead of within each `Attention`
  call.

- Updating the `TransformerBlock` to be cache-aware and to pass
  through the appropriate arguments to `Attention()`

- Wrapping all the additional book-keeping logic in a custom
  `TransformerDecoder()` class.

The changes required to implement these optimizations for inference
balloon the code size and are mostly about book-keeping, so we won't go
through them in this blog post. However, you can find a fuller
implementation of LLaMA in R Tensorflow, including a cache-aware
`generate()` method that only feeds the model one token at a time during
the main inference loop, (and compiles to XLA!),
[here](https://gist.github.com/t-kalinowski/62e9a1bbf8d670b712082c1765be4df4).

That's all for now. Thanks for reading and happy travels to all
exploring this exciting LLM terrain!

Photo by <a href="https://unsplash.com/@sebastiengoldberg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Sébastien Goldberg</a> on <a href="https://unsplash.com/photos/xgQZ1rXbYa4?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Biderman, Stella, Sid Black, Charles Foster, et al. 2021. *Rotary Embeddings: A Relative Revolution*. <a href="blog.eleuther.ai/rotary-embeddings/" class="uri">Blog.eleuther.ai/rotary-embeddings/</a>.

Falbel, Daniel, and Sigrid Keydana. 2023. *Posit AI Blog: De-Noising Diffusion with Torch*. <https://blogs.rstudio.com/tensorflow/posts/2023-04-13-denoising-diffusion/>.

Hoffmann, Jordan, Sebastian Borgeaud, Arthur Mensch, et al. 2022. *Training Compute-Optimal Large Language Models*. <https://arxiv.org/abs/2203.15556>.

Shazeer, Noam. 2020. *GLU Variants Improve Transformer*. <https://arxiv.org/abs/2002.05202>.

Su, Jianlin, Yu Lu, Shengfeng Pan, Ahmed Murtadha, Bo Wen, and Yunfeng Liu. 2022. *RoFormer: Enhanced Transformer with Rotary Position Embedding*. <https://arxiv.org/abs/2104.09864>.

Touvron, Hugo, Thibaut Lavril, Gautier Izacard, et al. 2023. *LLaMA: Open and Efficient Foundation Language Models*. <https://doi.org/10.48550/ARXIV.2302.13971>.

Vaswani, Ashish, Noam Shazeer, Niki Parmar, et al. 2017. *Attention Is All You Need*. <https://arxiv.org/abs/1706.03762>.
