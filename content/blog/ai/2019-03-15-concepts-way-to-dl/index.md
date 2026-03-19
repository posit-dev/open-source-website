---
title: "Math, code, concepts: A third road to deep learning"
description: |
  Not everybody who wants to get into deep learning has a strong background in math or programming. This post elaborates on a concepts-driven, abstraction-based way to learn what it's all about.
date: 2019-03-15
slug: keydana2019mathcodeconcepts
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
software: ["keras3"]
languages: ["R"]
categories:
  - Best Practices
ported_categories:
  - Meta
  - Concepts
---



In the previous version of their awesome deep learning MOOC, I remember fast.ai's Jeremy Howard saying something like this:

> You are either a math person or a code person, and \[...\] [^1]

I may be wrong about the *either*, and this is not about *either* versus, say, *both*. What if in reality, you're none of the above?

What if you come from a background that is close to neither math and statistics, nor computer science: the humanities, say? You may not have that intuitive, fast, effortless-looking understanding of LaTeX formulae that comes with natural talent and/or years of training, or both - the same goes for computer code.

Understanding always has to start somewhere, so it will have to start with math or code (or both). Also, it's always iterative, and iterations will often alternate between math and code. But what are things you can do when primarily, you'd say you are a *concepts person*?

When meaning doesn't automatically emerge from formulae, it helps to look for materials (blog posts, articles, books) that stress the *concepts* those formulae are all about. By concepts, I mean abstractions, concise, *verbal* characterizations of what a formula signifies.[^2]

Let's try to make *conceptual* a bit more concrete. At least three aspects come to mind: useful *abstractions*, *chunking* (composing symbols into meaningful blocks), and *action* (what does that entity actually *do*?)

## Abstraction

To many people, in school, math meant nothing. Calculus was about manufacturing cans: How can we get as much soup as possible into the can while economizing on tin. How about this instead: Calculus[^3] is about how one thing changes as another changes? Suddenly, you start thinking: What, in my world, can I apply this to?

A neural network is trained using backprop - just the *chain rule of calculus*, many texts say. How about life. How would my present be different had I spent more time exercising the ukulele? Then, how much more time would I have spent exercising the ukulele if my mother hadn't discouraged me so much? And then - how much less discouraging would she have been had she not been forced to give up her own career as a circus artist? And so on.

As a more concrete example, take optimizers. With gradient descent as a baseline, what, in a nutshell, is different about momentum, RMSProp, Adam?

Starting with momentum, this is the formula in one of the go-to posts, Sebastian Ruder's <http://ruder.io/optimizing-gradient-descent/> [^4]

$$v_t = \gamma v_{t-1} + \eta \nabla_{\theta} J(\theta) \\
\theta = \theta - v_t$$

The formula tells us that the change to the weights[^5] is made up of two parts: the gradient of the loss[^6] with respect to the weights, computed at some point in time $t$ (and scaled by the learning rate[^7]), and the previous change computed at time $t-1$ and discounted by some factor $\gamma$. What does this *actually* tell us?

In his Coursera MOOC, Andrew Ng introduces momentum (and RMSProp, and Adam) after two videos that aren't even about deep learning. He introduces exponential moving averages, which will be familiar to many R users: We calculate a running average where at each point in time, the running result is weighted by a certain factor (0.9, say), and the current observation by 1 minus that factor (0.1, in this example).
Now look at how *momentum* is presented:[^8]

$$v = \beta v + (1-\beta) dW \\ 
W = W - \alpha v$$

We immediately see how $v$ is the exponential moving average of gradients, and it is this that gets subtracted from the weights (scaled by the learning rate).

Building on that abstraction in the viewers' minds, Ng goes on to present RMSProp. This time, a moving average is kept of the *squared weights* [^9], and at each time, this average (or rather, its square root) is used to scale the current gradient.

$$s = \beta s + (1-\beta) dW^2 \\ 
W = W - \alpha \frac{dW}{\sqrt s}$$

If you know a bit about Adam, you can guess what comes next: Why not have moving averages in the numerator as well as the denominator?

$$v = \beta_1 v + (1-\beta_1) dW \\ 
s = \beta_2 s + (1-\beta_2) dW^2 \\
W = W - \alpha \frac{v}{\sqrt s + \epsilon}$$

Of course, actual implementations may differ in details, and not always expose those features that clearly. But for understanding and memorization, abstractions like this one - *exponential moving average* - do a lot. Let's now see about chunking.

## Chunking

Looking again at the above formula from Sebastian Ruder's post,

$$v_t = \gamma v_{t-1} + \eta \nabla_{\theta} J(\theta) \\
\theta = \theta - v_t$$

how easy is it to parse the first line? Of course that depends on experience, but let's focus on the formula itself.[^10]

Reading that first line, we mentally build something like an AST (abstract syntax tree). Exploiting programming language vocabulary even further, operator precedence is crucial: To understand the right half of the tree, we want to first parse $\nabla_{\theta} J(\theta)$, and then only take $\eta$ into consideration.

Moving on to larger formulae, the problem of operator precedence becomes one of *chunking*: Take that bunch of symbols and see it as a whole. We could call this abstraction again, just like above. But here, the focus is not on *naming* things or verbalizing, but on *seeing*: Seeing at a glance that when you read

$$\frac{e^{z_i}}{\sum_j{e^{z_j}}}$$

it is "just a softmax". Again, my inspiration for this comes from Jeremy Howard, who I remember demonstrating, in one of the fastai lectures, that this is how you read a paper.

Let's turn to a more complex example. Last year's article on [Attention-based Neural Machine Translation with Keras](/blog/ai/2018-07-30-attention-layer/) included a short exposition of *attention*, featuring four steps:

1.  Scoring encoder hidden states as to inasmuch they are a fit to the current decoder hidden state.

Choosing Luong-style attention now[^11], we have

$$score(\mathbf{h}_t,\bar{\mathbf{h}_s}) = \mathbf{h}_t^T \mathbf{W}\bar{\mathbf{h}_s}$$

On the right, we see three symbols, which may appear meaningless at first but if we mentally "fade out" the weight matrix in the middle, a dot product appears, indicating that essentially, this is calculating *similarity*.

1.  Now comes what's called *attention weights*: At the current timestep, which encoder states matter most?

$$\alpha_{ts} = \frac{exp(score(\mathbf{h}_t,\bar{\mathbf{h}_s}))}{\sum_{s'=1}^{S}{score(\mathbf{h}_t,\bar{\mathbf{h}_{s'}})}}$$

Scrolling up a bit, we see that this, in fact, is "just a softmax" (even though the physical appearance is not the same). Here, it is used to normalize the scores, making them sum to 1.

1.  Next up is the *context vector*:

$$\mathbf{c}_t= \sum_s{\alpha_{ts} \bar{\mathbf{h}_s}}$$

Without much thinking - but remembering from right above that the $\alpha$s represent attention *weights* - we see a weighted average.

Finally, in step

1.  we need to actually combine that context vector with the current hidden state (here, done by training a fully connected layer on their concatenation):

$$\mathbf{a}_t = tanh(\mathbf{W_c} [ \mathbf{c}_t ; \mathbf{h}_t])$$

This last step may be a better example of abstraction than of chunking, but anyway those are closely related: We need to chunk adequately to name concepts, and intuition about concepts helps chunk correctly.
Closely related to abstraction, too, is analyzing what entities *do*.

## Action

Although not deep learning related (in a narrow sense), my favorite quote comes from one of Gilbert Strang's lectures on linear algebra:[^12]

> Matrices don't just sit there, they do something.

If in school calculus was about saving production materials, matrices were about matrix multiplication - the rows-by-columns way. (Or perhaps they existed for us to be trained to compute determinants, seemingly useless numbers that turn out to have a meaning, as we are going to see in a future post.)
Conversely, based on the much more illuminating *matrix multiplication as linear combination of columns* (resp. rows) view, Gilbert Strang introduces types of matrices as agents, concisely named by initial.

For example, when multiplying another matrix $A$ on the right, this permutation matrix $P$

$$\mathbf{P} = \left[\begin{array}
{rrr}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right]$$

puts $A$'s third row first, its first row second, and its second row third:

$$\mathbf{PA} = \left[\begin{array}
{rrr}
0 & 0 & 1 \\
1 & 0 & 0 \\
0 & 1 & 0
\end{array}\right]
\left[\begin{array}
{rrr}
0 & 1 & 1 \\
1 & 3 & 7 \\
2 & 4 & 8
\end{array}\right] =
\left[\begin{array}
{rrr}
2 & 4 & 8 \\
0 & 1 & 1 \\
1 & 3 & 7
\end{array}\right]$$

In the same way, reflection, rotation, and projection matrices are presented via their *actions*. The same goes for one of the most interesting topics in linear algebra from the point of view of the data scientist: matrix factorizations. $LU$, $QR$, eigendecomposition, $SVD$ are all characterized by *what they do*. [^13]

Who are the agents in neural networks? Activation functions are agents; this is where we have to mention `softmax` for the third time: Its strategy was described in [Winner takes all: A look at activations and cost functions](/blog/ai/2018-10-11-activations-intro/).

Also, optimizers are agents, and this is where we finally include some code. The explicit training loop used in all of the eager execution blog posts so far

    with(tf$GradientTape() %as% tape, {
         
      # run model on current batch
      preds <- model(x)
         
      # compute the loss
      loss <- mse_loss(y, preds, x)
    })
        
    # get gradients of loss w.r.t. model weights
    gradients <- tape$gradient(loss, model$variables)
        
    # update model weights
    optimizer$apply_gradients(
      purrr::transpose(list(gradients, model$variables)),
      global_step = tf$train$get_or_create_global_step()
    )

has the optimizer do a single thing: *apply* the gradients it gets passed from the gradient tape.[^14] Thinking back to the characterization of different optimizers we saw above, this piece of code adds vividness to the thought that optimizers differ in what they *actually do* once they got those gradients.

## Conclusion

Wrapping up, the goal here was to elaborate a bit on a conceptual, abstraction-driven way to get more familiar with the math involved in deep learning (or machine learning, in general). Certainly, the three aspects highlighted interact, overlap, form a whole, and there are other aspects to it. Analogy may be one, but it was left out here because it seems even more subjective, and less general.
Comments describing user experiences are very welcome.

[^1]: If I don't remember correctly: please just allow me to use this as the perfect intro to this post.

[^2]: Certainly *visualization* may be very useful, too, depending on the topic/algorithm and on "how visual a person" you are. But there is no need to stress the importance of visualization - everybody agrees on it - so this post is dedicated to verbal/conceptual methods.

[^3]: Differential calculus, to be precise.

[^4]: This is of course an excellent article that *does* mention concepts. It is just not intended for beginners, in contrast to the approach highlighted below.

[^5]: $\theta$

[^6]: $J$

[^7]: $\eta$

[^8]: Following the notation from the video, marginally simplified. Here $\beta$ is the scale factor applied to the running average, $dW$ is the gradient of the loss with respect to the weights, and $\alpha$ is the learning rate.

[^9]: $W^2$

[^10]:  As a side note, picking up on Jeremy Howard again: The Greek letters of course don't make things any easier, but even with a history of studying ancient Greek for five years those formulae aren't necessarily parsed easily.

[^11]: The original post showed Bahdanau-style attention.

[^12]: At least that's what I remember him saying, approximately. The exact wording does not matter here.

[^13]: Although, if this were the paragraph about *abstractions*, Gilbert Strang's books would yield perfect examples as well.

[^14]: In other use cases, the optimizer class may also be used to compute gradients. But that method (`optimizer$compute_gradients`) is defined in the optimizer superclass and not subclass specific.
