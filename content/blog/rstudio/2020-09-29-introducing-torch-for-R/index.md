---
title: Introducing torch for R
people:
  - RStudio Team
date: '2020-09-29'
slug: torch
categories:
  - Machine Learning
tags:
  - Data science
  - Deep learning
  - RStudio
  - Packages
  - News
editor_options:
  markdown:
    wrap: 72
resoruces:
  - name: torch
    src: torch.jpg
    title: Torch
blogcategories:
  - Products and Technology
  - Company News and Events
  - Open Source
ported_from: rstudio
port_status: in-progress
languages: ["R"]
ported_categories:
  - Packages
  - News
---


<sup>Photo by <a href="https://unsplash.com/@ilepilin?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Igor Lepilin</a> on <a href="https://unsplash.com/s/photos/torch?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></sup>


As of this writing, two deep learning frameworks are widely used in the
Python community: [TensorFlow](https://www.tensorflow.org/) and
[PyTorch](https://pytorch.org/). TensorFlow, together with its
high-level API Keras, has been usable from R since 2017, via the
[tensorflow](https://tensorflow.rstudio.com/) and
[keras](https://keras.rstudio.com/) packages. Today, we are thrilled to
announce that now, you can use Torch [natively from
R](http://torch.mlverse.org/)!

This post addresses three questions:

-   What is deep learning, and why might I care?
-   What's the difference between `torch` and `tensorflow`?
-   How can I participate?

If you are already familiar with deep learning -- or all you can think
right now is "show me some code" -- you might want to head directly over
to the [more technical introduction on the AI blog](https://blogs.rstudio.com/ai/posts/2020-09-29-introducing-torch-for-r/). Otherwise, you
may find it more useful to hear about the context first, and then play
with the step-by-step example in that complementary post.

## What is deep learning, and why might I care?

If you're a data scientist, and your data normally comes in tabular,
mostly-numerical form, a toolbox of linear and non-linear methods like
those presented in James et al.'s *Introduction to Statistical Learning*
may be all you need. This holds even more strongly if the number of data
points is limited, as tends to be the case in some academic fields, such
as anthropology or ethnology. In this case, Bayesian modeling, as taught
by Richard McElreath's *Statistical Rethinking*, may be the best
approach. Carrying the argument to the extreme: Yes, we *can* construct
deep learning models to predict penguin species based on biometric
attributes, and doing this may be very useful in teaching, but this type
of task is not really where deep learning shines.

In contrast, deep learning has seen its greatest successes when there
are *lots* of data of a type that is often (misleadingly) called
"unstructured" -- images, text, heterogeneous data resisting
unification. Over the last decade, public triumphs have spread from
image classification and related tasks, like segmentation and detection
(important in many sciences), to natural language processing (NLP);
prominent examples are translation, summarization, and dialogue
generation. Beyond these areas of benchmark datasets and official,
academically organized competitions, deep learning is pervasively employed in
generative art, recommendation systems, and probabilistic modeling.
Needless to say, current research is working to expand its limits even
more, striving to integrate capabilities for e.g. concept learning or
causal inference.

Many readers are likely to work in a field that could benefit from deep
learning. But even if you don't, learning about how a technology works
yields power, power to look behind appearances and make up your own mind
and decisions.

## What's the difference between `torch` and `tensorflow`?

In the Python world, as of 2020, which framework you end up using for a
project may be largely a matter of chance and context. (Admittedly, to
say so takes the fun out of "TensorFlow vs. PyTorch" debates, but that's
no different from other popular "comparison games". Take *vim vs.
emacs*, for example. How many people, among those who use one of them
preferentially, have come to do so because "that's what I learned first"
or "that's what was used in my first company"?).

Not too long ago, there was a big difference, though. Before the
introduction of TensorFlow 2 (the current release is 2.3), TensorFlow
code was compiled to a static graph, and raw TensorFlow code was hard to
write. Many users didn't have to write low-level code, however: The
high-level API [Keras](http://keras.io) provided concise, declarative
idioms to define, train, and evaluate a neural network. On the other
hand, Keras did not, at that time, offer a way to easily customize the
training process. Ease of customization, then, used to be PyTorch's
competitive advantage, relevant to researchers in particular. On the
other hand, PyTorch did not, initially, excel in production and
deployment facilities. Historically, thus, the respective strengths used
to be seen as ease of experimentation on the one side, and production
readiness on the other.

Today, however, with TensorFlow having become more flexible and PyTorch being
increasingly employed in production settings, the traditional dichotomy
has weakened. For the R user, this means that practical considerations
are likely to prevail.

One such practical consideration that, for some users, may be of
tremendous importance, is the following. `tensorflow` and `keras` are
based on [reticulate](https://github.com/rstudio/reticulate), that
helpful genie which lets you use Python packages seamlessly from R. In
other words, they do not *replace* Python TensorFlow/Keras; instead,
they wrap its functionality and in many cases, add syntactic sugar,
resulting in more R-like, aestethically-pleasing (to the R user) code.

`torch` is different. It is built directly on
[libtorch](https://github.com/pytorch/pytorch/blob/master/docs/libtorch.rst),
PyTorch's C++ backend. There is no dependency on Python, resulting in a
leaner software stack and more straightforward installation. This should
make a huge difference, especially in environments where users have no
control over, or are not allowed to modify, the software their
organization provides.

Otherwise, at the current point in time, maturity of the ecosystem (on
the R side) naturally constitutes a major difference. As of this
writing, a lot more functionality -- as well as documentation -- is
available in the `tensorflow` ecosystem than in the `torch` one. But
time doesn't stand still, and we'll get to that in a second.

To wrap up, let's quickly mention another aspect, to be explained in
more detail in a dedicated article. Due to its in-built facility to do
automatic differentiation, `torch` can also be used as an R-native,
high-performing, highly-customizable optimization tool, beyond the realm
of deep learning. For now though, back to our hopes for the future.

## How can I participate?

As with other projects, we sincerely hope that the R community will find
the new functionality useful. But that is not all. We also hope that
you, many of you, will take part in the journey. There is not just a
whole framework to be built. There is not just a whole "bag of data
types" to be taken care of (images, text, audio...), each of which
requires their own pre-processing functionality. There is also the
expanding, flourishing ecosystem of libraries built on top of PyTorch:
[PySyft](https://github.com/OpenMined/PySyft) and
[CrypTen](https://github.com/facebookresearch/CrypTen) for
privacy-preserving machine learning, [PyTorch
Geometric](https://github.com/rusty1s/pytorch_geometric) for deep
learning on manifolds, and [Pyro](http://pyro.ai/) for probabilistic
programming, to name just a few.

Whether small PRs for [torch](https::/github.com/mlverse/torch) or
[torchvision](https::/github.com/mlverse/torchvision), or model
implementations, or help with porting some of the PyTorch ecosystem --
we welcome any participation and support from the R community!

Thanks for reading, and have fun with `torch`!
