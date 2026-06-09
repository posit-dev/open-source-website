---
title: "Deep Learning with R, 3rd Edition"
date: 2026-06-09
people:
  - Tomasz Kalinowski
  - François Chollet
description: >
  Deep Learning with R, Third Edition is now available in print and online,
  covering Keras 3, modern pretrained models, Transformers, diffusion models,
  and practical deep learning workflows in R.
image: "featured.jpg"
image-alt: "A copy of Deep Learning with R, Third Edition, shown at an angle on a light green background."
source: ai
topics:
  - Artificial Intelligence
  - Machine Learning
software:
  - keras3
  - tensorflow
  - torch
languages:
  - R
tags:
  - Deep Learning with R
  - Keras
hidesubscription: false
---

Today we're pleased to announce the release of [_Deep Learning with R, Third
Edition_](https://deep-learning-with-r.site/). The book is now in print from
[Manning](https://www.manning.com/books/deep-learning-with-r-third-edition),
and the complete online version is available for free at
<https://deep-learning-with-r.site/>.

Compared with the second edition, this edition grows from 14 chapters to 20.
But that number undersells the change. The deep learning landscape has shifted
dramatically since 2022: Keras is now a multi-backend framework, Transformers
and diffusion models have become everyday developer tools, and large pretrained
models are now part of the normal workflow. The third edition has been rebuilt
around this new stack.

This book shows you how to get started with Keras, TensorFlow, PyTorch, and JAX
in R, even if you have no background in mathematics or data science. The book
covers:

* Deep learning from first principles
* Keras 3 in R, with TensorFlow, PyTorch, and JAX backends
* Image classification, interpretability, segmentation, and object detection
* Timeseries forecasting
* Text classification, machine translation, language models, and Transformers
* Text generation, LLM fine-tuning, and multimodal models
* Image generation with VAEs, diffusion models, and Stable Diffusion
* Hyperparameter tuning, ensembling, distributed training, mixed precision, and
  quantization

Only modest R knowledge is assumed; everything else is explained from the
ground up with examples that make the mechanics explicit. Learn what a
tensor is by manipulating arrays and seeing how NumPy broadcasting differs from
R recycling. Learn how backpropagation works by following gradients through
actual code. Learn how the pieces of a neural network fit together by
implementing a dense layer, a sequential model, a batch generator, and a
training loop from scratch in R.

The biggest platform change is Keras 3. In the second edition, Keras meant
Keras and TensorFlow. In the third edition, Keras is presented as a high-level
API that can run on TensorFlow, PyTorch, or JAX. You will learn how these
frameworks relate to each other, how to choose and configure a backend from R,
and how core deep learning ideas look in each framework. It walks through pure
TensorFlow, pure PyTorch, and pure JAX examples, then shows how Keras provides
a higher-level workflow without giving up access to lower-level control. By the
time you reach the advanced chapters, Keras should feel like a dependable place
to work: a simple interface when that is all you need, and a doorway to the
machinery underneath when you need more.

That progressive path is central to the book. You will start with `compile()`
and `fit()`, then move on to callbacks, custom metrics, custom losses, and
custom layers. For more control, the book shows how to override `train_step()`
while still keeping the conveniences of `fit()`. For complete control, it moves
all the way to custom training loops using the gradient APIs of TensorFlow,
PyTorch, or JAX. The goal is the same as before: no magic, no hand-waving, and
no unexplained black boxes.

Every major applied section has been rebuilt or expanded. Computer vision now
spans five chapters. The section starts with a small convnet for image
classification, then works through data augmentation, KerasHub backbones,
pretrained Xception feature extraction, and fine-tuning. It then opens up the
architecture patterns behind modern convnets, including residual connections,
batch normalization, depthwise separable convolutions, and the role of Vision
Transformers. It also shows how to inspect what convnets see, using
intermediate activations, filter visualizations, and Grad-CAM heatmaps.

The vision material now goes well beyond classification. It includes training
an image segmentation model from scratch on Oxford-IIIT Pets, then using the
pretrained Segment Anything model through KerasHub. It explains how object
detection differs from segmentation, how YOLO-style single-stage detectors work,
how to parse COCO annotations and build detection targets, and how to use a
pretrained RetinaNet detector. The emphasis throughout is practical intuition:
when is a class label enough, when are pixels needed, and when are bounding
boxes the right output? After these chapters, you will be able to approach
computer vision less as a list of model names and more as a set of tools you
know how to choose among.

The timeseries chapter keeps the same engineering spirit. Before reaching for a
large model, it builds common-sense baselines. It then compares dense models,
1D convnets, LSTMs, dropout-regularized LSTMs, and stacked GRUs on the Jena
weather forecasting task. Along the way, it shows how to prepare rolling
windows with `timeseries_dataset_from_array()`, why validation splits must
respect temporal order, why periodicity matters, and why a simple baseline is
often the most important model in the project.

The text chapters have been completely reworked for the Transformer and LLM
era. They begin with practical text classification: tokenization,
`TextVectorization`, set models, sequence models, embeddings, and pretraining.
The book is careful about tradeoffs. Sometimes a bag-of-words or bigram model
is the fastest, cheapest, and most robust answer. Sometimes the right tool is a
sequence model. And sometimes the right tool is a pretrained Transformer.

From there, the book builds up language models and Transformers step by step:
training a character-level Shakespeare model, building a
sequence-to-sequence English-to-Spanish translator, implementing attention, and
assembling Transformer encoders and decoders. You will train a miniature
GPT-style model from scratch before moving to pretrained Gemma 3 models via
KerasHub. The chapter also covers sampling strategies, prompt behavior,
hallucinations, instruction fine-tuning, reinforcement learning from human
feedback, retrieval-augmented generation, and multimodal models. By the end,
you will understand enough of the machinery to adapt an LLM from R with
confidence.

LLM fine-tuning gets special attention because it exposes a very real
constraint: accelerator memory. The book walks through Low-Rank Adaptation
(LoRA), showing how nearly all of a billion-parameter Gemma model can be
frozen while training only a small set of low-rank adapter weights, making this
kind of fine-tuning practical on much smaller hardware.

Generative image modeling has also been updated for the current moment.
Previous editions covered GANs; this edition focuses on VAEs and diffusion
models, which have become the dominant approach for high-quality image
generation. The chapter builds a diffusion model from scratch, then uses Stable
Diffusion 3 through KerasHub, exploring prompts, negative prompts, diffusion
steps, and latent-space interpolation.

Finally, the real-world practice material has grown substantially. It covers
hyperparameter tuning with KerasTuner, ensembling, validation-set overfitting,
deployment to TensorFlow SavedModel and ONNX, and inference optimization. It
also shows how modern large-scale training is done: data parallelism, model
parallelism, device meshes, layout maps, multi-GPU and TPU training with JAX,
mixed precision, float8 training, and int8 quantization.

The book also makes space for perspective. A new chapter on the future of AI
examines what deep learning can and cannot do, and why fluent model outputs
should not be confused with human-like reasoning. Today's models are powerful
pattern-learning systems, but using them well still requires careful validation,
a clear understanding of failure modes, and a willingness to build systems
around their limitations.

Throughout the book, the guiding idea is the same as in previous editions: deep
learning is best learned by building. The abstractions matter, but they should
never remain mysterious. Work through the third edition and you will be able to
apply deep learning to common tasks in R, adapt modern pretrained models, and
reason about new problems with enough context to choose the right tool for the
job.

[_Deep Learning with R, Third Edition_](https://deep-learning-with-r.site/) is
available now. Read it online for free, or order the print edition from
[Manning](https://www.manning.com/books/deep-learning-with-r-third-edition).
