---
title: "Group-equivariant neural networks with escnn"
description: |
  Escnn, built on PyTorch, is a library that, in the spirit of Geometric Deep Learning, provides a high-level interface to designing and training group-equivariant neural networks. This post introduces important mathematical concepts, the library's key actors, and essential library use.
date: 2023-05-09T00:00:00.000Z
categories:
  - Torch
  - R
  - Concepts
  - Image Recognition & Image Processing
author:
  - name: Sigrid Keydana
    affiliation: Posit
    affiliation_url: https://www.posit.co/
people:
  - Sigrid Keydana
image: thumbnail.jpg
ported_from: ai
port_status: raw
---



Today, we resume our exploration of group equivariance. This is the third post in the series. The [first](https://blogs.rstudio.com/ai/posts/2023-03-09-group-equivariant-cnn-1/) was a high-level introduction: what this is all about; how equivariance is operationalized; and why it is of relevance to many deep-learning applications. The [second](https://blogs.rstudio.com/ai/posts/2023-03-27-group-equivariant-cnn-2/) sought to concretize the key ideas by developing a group-equivariant CNN from scratch. That being instructive, but too tedious for practical use, today we look at a carefully designed, highly-performant [library](https://github.com/QUVA-Lab/escnn) that hides the technicalities and enables a convenient workflow.

First though, let me again set the context. In physics, an all-important concept is that of symmetry[^1], a symmetry being present whenever some quantity is being conserved. But we don't even need to look to science. Examples arise in daily life, and -- otherwise why write about it - in the tasks we apply deep learning to.

In daily life: Think about speech -- me stating "it is cold", for example. Formally, or denotation-wise, the sentence will have the same meaning now as in five hours. (Connotations, on the other hand, can and will probably be different!). This is a form of translation symmetry, translation in time.

In deep learning: Take image classification. For the usual convolutional neural network, a cat in the center of the image is just that, a cat; a cat on the bottom is, too. But one sleeping, comfortably curled like a half-moon "open to the right", will not be "the same" as one in a mirrored position. Of course, we can train the network to treat both as equivalent by providing training images of cats in both positions, but that is not a scaleable approach. Instead, we'd like to make the network aware of these symmetries, so they are automatically preserved throughout the network architecture.

## Purpose and scope of this post

Here, I introduce [`escnn`](https://github.com/QUVA-Lab/escnn), a PyTorch extension that implements forms of group equivariance for CNNs operating on the plane or in (3d) space. The library is used in various, amply illustrated research papers; it is appropriately documented; and it comes with introductory notebooks both relating the math and exercising the code. Why, then, not just refer to the [first notebook](https://github.com/QUVA-Lab/escnn/blob/master/examples/introduction.ipynb), and immediately start using it for some experiment?

In fact, this post should -- as quite a few texts I've written -- be regarded as an introduction to an introduction. To me, this topic seems anything but easy, for various reasons. Of course, there's the math. But as so often in machine learning, you don't need to go to great depths to be able to apply an algorithm correctly. So if not the math itself, what generates the difficulty? For me, it's two things.

First, to map my understanding of the mathematical concepts to the terminology used in the library, and from there, to correct use and application. Expressed schematically: We have a concept A, which figures (among other concepts) in technical term (or object class) B. What does my understanding of A tell me about how object class B is to be used correctly? More importantly: How do I use it to best attain my goal C? This first difficulty I'll address in a very pragmatic way. I'll neither dwell on mathematical details, nor try to establish the links between A, B, and C in detail. Instead, I'll present the characters[^2] in this story by asking what they're good for.

Second -- and this will be of relevance to just a subset of readers -- the topic of group equivariance, particularly as applied to image processing, is one where visualizations can be of tremendous help. The quaternity[^3] of conceptual explanation, math, code, and visualization can, together, produce an understanding of emergent-seeming quality... if, and only if, all of these explanation modes "work" for you. (Or if, in an area, a mode that does not wouldn't contribute that much anyway.) Here, it so happens that from what I saw, several papers have excellent visualizations[^4], and the same holds for some lecture slides and accompanying notebooks[^5]. But for those among us with limited spatial-imagination capabilities -- e.g., people with [Aphantasia](https://en.wikipedia.org/wiki/Aphantasia) -- these illustrations, intended to help, can be very hard to make sense of themselves. If you're not one of these, I totally recommend checking out the resources linked in the above footnotes. This text, though, will try to make the best possible use of verbal explanation to introduce the concepts involved, the library, and how to use it.

That said, let's start with the software.

## Using *escnn*

`Escnn` depends on PyTorch. Yes, PyTorch, not `torch`; unfortunately, the library hasn't been ported to R yet.[^6] For now, thus, we'll employ [`reticulate`](https://rstudio.github.io/reticulate/)[^7] to access the Python objects directly.

The way I'm doing this is install `escnn` in a virtual environment, with PyTorch version 1.13.1. As of this writing, Python 3.11 is not yet supported by one of `escnn`'s dependencies; the virtual environment thus builds on Python 3.10. As to the library itself, I am using the development version from GitHub, running `pip install git+https://github.com/QUVA-Lab/escnn`.

Once you're ready, issue

``` r
library(reticulate)
# Verify correct environment is used.
# Different ways exist to ensure this; I've found most convenient to configure this on
# a per-project basis in RStudio's project file (<myproj>.Rproj)
py_config()

# bind to required libraries and get handles to their namespaces
torch <- import("torch")
escnn <- import("escnn")
```

`Escnn` loaded, let me introduce its main objects and their roles in the play.

## Spaces, groups, and representations: `escnn$gspaces`

We start by peeking into `gspaces`, one of the two sub-modules we are going to make direct use of.

``` r
gspaces <- escnn$gspaces
py_list_attributes(gspaces) |> (\(vec) grep("On", vec, value = TRUE))() |> sort()
```

    [1] "conicalOnR3" "cylindricalOnR3" "dihedralOnR3" "flip2dOnR2" "flipRot2dOnR2" "flipRot3dOnR3"
    [7] "fullCylindricalOnR3" "fullIcoOnR3" "fullOctaOnR3" "icoOnR3" "invOnR3" "mirOnR3 "octaOnR3"
    [14] "rot2dOnR2" "rot2dOnR3" "rot3dOnR3" "trivialOnR2" "trivialOnR3"    

The methods I've listed instantiate a `gspace`. If you look closely, you see that they're all composed of two strings, joined by "On". In all instances, the second part is either `R2` or `R3`. These two are the available base spaces -- $\mathbb{R}^2$ and $\mathbb{R}^3$ -- an input signal can live in. Signals can, thus, be images, made up of pixels, or three-dimensional volumes, composed of voxels. The first part refers to the group you'd like to use. Choosing a group means choosing the symmetries to be respected. For example, `rot2dOnR2()` implies equivariance as to rotations, `flip2dOnR2()` guarantees the same for mirroring actions, and `flipRot2dOnR2()` subsumes both.

Let's define such a `gspace`. Here we ask for rotation equivariance on the Euclidean plane, making use of the same cyclic group -- $C_4$ -- we developed in our [from-scratch implementation](https://blogs.rstudio.com/ai/posts/2023-03-27-group-equivariant-cnn-2/):

``` r
r2_act <- gspaces$rot2dOnR2(N = 4L)
r2_act$fibergroup
```

In this post, I'll stay with that setup, but we could as well pick another rotation angle -- `N = 8`, say, resulting in eight equivariant positions separated by forty-five degrees. Alternatively, we might want *any* rotated position to be accounted for. The group to request then would be [SO(2)](https://en.wikipedia.org/wiki/Orthogonal_group#Special_orthogonal_group), called the *special orthogonal group,* of continuous, distance- and orientation-preserving transformations on the Euclidean plane:

``` r
(gspaces$rot2dOnR2(N = -1L))$fibergroup
```

    SO(2)

Going back to $C_4$, let's investigate its [*representations*](https://en.wikipedia.org/wiki/Group_representation):

``` r
r2_act$representations
```

    $irrep_0
    C4|[irrep_0]:1

    $irrep_1
    C4|[irrep_1]:2

    $irrep_2
    C4|[irrep_2]:1

    $regular
    C4|[regular]:4

A representation, in our current context *and* very roughly speaking, is a way to encode a group action as a matrix, meeting certain conditions. In `escnn`, representations are central, and we'll see how in the next section.

First, let's inspect the above output. Four representations are available, three of which share an important property: they're all [irreducible](https://en.wikipedia.org/wiki/Irreducible_representation). On $C_4$, any non-irreducible representation [can be decomposed](https://en.wikipedia.org/wiki/Maschke%27s_theorem) into into irreducible ones. These irreducible representations are what `escnn` works with internally. Of those three, the most interesting one is the second. To see its action, we need to choose a group element. How about counterclockwise rotation by ninety degrees:

``` r
elem_1 <- r2_act$fibergroup$element(1L)
elem_1
```

    1[2pi/4]

Associated to this group element is the following matrix:

``` r
r2_act$representations[[2]](elem_1)
```

                 [,1]          [,2]
    [1,] 6.123234e-17 -1.000000e+00
    [2,] 1.000000e+00  6.123234e-17

This is the so-called standard representation,

$$\begin{bmatrix} \cos(\theta) & -\sin(\theta) \\ \sin(\theta) & \cos(\theta) \end{bmatrix}$$

, evaluated at $\theta = \pi/2$. (It is called the standard representation because it directly comes from how the group is defined (namely, a rotation by $\theta$ in the plane).

The other interesting representation to point out is the fourth: the only one that's not irreducible.

``` r
r2_act$representations[[4]](elem_1)
```

    [1,]  5.551115e-17 -5.551115e-17 -8.326673e-17  1.000000e+00
    [2,]  1.000000e+00  5.551115e-17 -5.551115e-17 -8.326673e-17
    [3,]  5.551115e-17  1.000000e+00  5.551115e-17 -5.551115e-17
    [4,] -5.551115e-17  5.551115e-17  1.000000e+00  5.551115e-17

This is the so-called *regular* representation. The regular representation acts via permutation of group elements, or, to be more precise, of the basis vectors that make up the matrix. Obviously, this is only possible for finite groups like $C_n$, since otherwise there'd be an infinite amount of basis vectors to permute.

To better see the action encoded in the above matrix, we clean up a bit:

``` r
round(r2_act$representations[[4]](elem_1))
```

        [,1] [,2] [,3] [,4]
    [1,]    0    0    0    1
    [2,]    1    0    0    0
    [3,]    0    1    0    0
    [4,]    0    0    1    0

This is a step-one shift to the right of the identity matrix. The identity matrix, mapped to element 0, is the non-action; this matrix instead maps the zeroth action to the first, the first to the second, the second to the third, and the third to the first.

We'll see the regular representation used in a neural network soon. Internally -- but that need not concern the user -- *escnn* works with its decomposition into irreducible matrices. Here, that's just the bunch of irreducible representations we saw above, numbered from one to three.

Having looked at how groups and representations figure in `escnn`, it is time we approach the task of building a network.

## Representations, for real: `escnn$nn$FieldType`

So far, we've characterized the input space ($\mathbb{R}^2$), and specified the group action. But once we enter the network, we're not in the plane anymore, but in a space that has been extended by the group action. Rephrasing, the group action produces *feature vector fields* that assign a feature vector to each spatial position in the image.

Now we have those feature vectors, we need to specify how they transform under the group action. This is encoded in an `escnn$nn$FieldType` . Informally, we could say that a field type is the *data type* of a feature space. In defining it, we indicate two things: the base space, a `gspace`, and the representation type(s) to be used.

In an equivariant neural network, field types play a role similar to that of channels in a convnet. Each layer has an input and an output field type. Assuming we're working with grey-scale images, we can specify the input type for the first layer like this:

``` r
nn <- escnn$nn
feat_type_in <- nn$FieldType(r2_act, list(r2_act$trivial_repr))
```

The *trivial* representation is used to indicate that, while the image as a whole will be rotated, the pixel values themselves should be left alone. If this were an RGB image, instead of `r2_act$trivial_repr` we'd pass a list of three such objects.

So we've characterized the input. At any later stage, though, the situation will have changed. We will have performed convolution once for every group element. Moving on to the next layer, these feature fields will have to transform equivariantly, as well. This can be achieved by requesting the *regular* representation for an output field type:

``` r
feat_type_out <- nn$FieldType(r2_act, list(r2_act$regular_repr))
```

Then, a convolutional layer may be defined like so:

``` r
conv <- nn$R2Conv(feat_type_in, feat_type_out, kernel_size = 3L)
```

## Group-equivariant convolution

What does such a convolution do to its input? Just like, in a usual convnet, capacity can be increased by having more channels, an equivariant convolution can pass on several feature vector fields, possibly of different type (assuming that makes sense). In the code snippet below, we request a list of three, all behaving according to the regular representation.

``` r
feat_type_in <- nn$FieldType(r2_act, list(r2_act$trivial_repr))
feat_type_out <- nn$FieldType(
  r2_act,
  list(r2_act$regular_repr, r2_act$regular_repr, r2_act$regular_repr)
)

conv <- nn$R2Conv(feat_type_in, feat_type_out, kernel_size = 3L)
```

We then perform convolution on a batch of images, made aware of their "data type" by wrapping them in `feat_type_in`:

``` r
x <- torch$rand(2L, 1L, 32L, 32L)
x <- feat_type_in(x)
y <- conv(x)
y$shape |> unlist()
```

    [1]  2  12 30 30

The output has twelve "channels", this being the product of group cardinality -- four distinguished positions -- and number of feature vector fields (three).

If we choose the simplest possible, approximately, test case, we can verify that such a convolution is equivariant by direct inspection. Here's my setup:

``` r
feat_type_in <- nn$FieldType(r2_act, list(r2_act$trivial_repr))
feat_type_out <- nn$FieldType(r2_act, list(r2_act$regular_repr))
conv <- nn$R2Conv(feat_type_in, feat_type_out, kernel_size = 3L)

torch$nn$init$constant_(conv$weights, 1.)
x <- torch$vander(torch$arange(0,4))$view(tuple(1L, 1L, 4L, 4L)) |> feat_type_in()
x
```

    g_tensor([[[[ 0.,  0.,  0.,  1.],
                [ 1.,  1.,  1.,  1.],
                [ 8.,  4.,  2.,  1.],
                [27.,  9.,  3.,  1.]]]], [C4_on_R2[(None, 4)]: {irrep_0 (x1)}(1)])

Inspection could be performed using any group element. I'll pick rotation by $\pi/2$:

``` r
all <- iterate(r2_act$testing_elements)
g1 <- all[[2]]
g1
```

Just for fun, let's see how we can -- literally -- come whole circle by letting this element act on the input tensor four times:

``` r
all <- iterate(r2_act$testing_elements)
g1 <- all[[2]]

x1 <- x$transform(g1)
x1$tensor
x2 <- x1$transform(g1)
x2$tensor
x3 <- x2$transform(g1)
x3$tensor
x4 <- x3$transform(g1)
x4$tensor
```

    tensor([[[[ 1.,  1.,  1.,  1.],
              [ 0.,  1.,  2.,  3.],
              [ 0.,  1.,  4.,  9.],
              [ 0.,  1.,  8., 27.]]]])
              
    tensor([[[[ 1.,  3.,  9., 27.],
              [ 1.,  2.,  4.,  8.],
              [ 1.,  1.,  1.,  1.],
              [ 1.,  0.,  0.,  0.]]]])
              
    tensor([[[[27.,  8.,  1.,  0.],
              [ 9.,  4.,  1.,  0.],
              [ 3.,  2.,  1.,  0.],
              [ 1.,  1.,  1.,  1.]]]])
              
    tensor([[[[ 0.,  0.,  0.,  1.],
              [ 1.,  1.,  1.,  1.],
              [ 8.,  4.,  2.,  1.],
              [27.,  9.,  3.,  1.]]]])

You see that at the end, we are back at the original "image".

Now, for equivariance. We could first apply a rotation, then convolve.

Rotate:

``` r
x_rot <- x$transform(g1)
x_rot$tensor
```

This is the first in the above list of four tensors.

Convolve:

``` r
y <- conv(x_rot)
y$tensor
```

    tensor([[[[ 1.1955,  1.7110],
              [-0.5166,  1.0665]],

             [[-0.0905,  2.6568],
              [-0.3743,  2.8144]],

             [[ 5.0640, 11.7395],
              [ 8.6488, 31.7169]],

             [[ 2.3499,  1.7937],
              [ 4.5065,  5.9689]]]], grad_fn=<ConvolutionBackward0>)

Alternatively, we can do the convolution first, then rotate its output.

Convolve:

``` r
y_conv <- conv(x)
y_conv$tensor
```

    tensor([[[[-0.3743, -0.0905],
              [ 2.8144,  2.6568]],

             [[ 8.6488,  5.0640],
              [31.7169, 11.7395]],

             [[ 4.5065,  2.3499],
              [ 5.9689,  1.7937]],

             [[-0.5166,  1.1955],
              [ 1.0665,  1.7110]]]], grad_fn=<ConvolutionBackward0>)

Rotate:

``` r
y <- y_conv$transform(g1)
y$tensor
```

    tensor([[[[ 1.1955,  1.7110],
              [-0.5166,  1.0665]],

             [[-0.0905,  2.6568],
              [-0.3743,  2.8144]],

             [[ 5.0640, 11.7395],
              [ 8.6488, 31.7169]],

             [[ 2.3499,  1.7937],
              [ 4.5065,  5.9689]]]])

Indeed, final results are the same.

At this point, we know how to employ group-equivariant convolutions. The final step is to compose the network.

## A group-equivariant neural network

Basically, we have two questions to answer. The first concerns the non-linearities; the second is how to get from extended space to the data type of the target.

First, about the non-linearities. This is a potentially intricate topic, but as long as we stay with point-wise operations (such as that performed by ReLU) equivariance is given intrinsically.

In consequence, we can already assemble a model:

``` r
feat_type_in <- nn$FieldType(r2_act, list(r2_act$trivial_repr))
feat_type_hid <- nn$FieldType(
  r2_act,
  list(r2_act$regular_repr, r2_act$regular_repr, r2_act$regular_repr, r2_act$regular_repr)
  )
feat_type_out <- nn$FieldType(r2_act, list(r2_act$regular_repr))

model <- nn$SequentialModule(
  nn$R2Conv(feat_type_in, feat_type_hid, kernel_size = 3L),
  nn$InnerBatchNorm(feat_type_hid),
  nn$ReLU(feat_type_hid),
  nn$R2Conv(feat_type_hid, feat_type_hid, kernel_size = 3L),
  nn$InnerBatchNorm(feat_type_hid),
  nn$ReLU(feat_type_hid),
  nn$R2Conv(feat_type_hid, feat_type_out, kernel_size = 3L)
)$eval()

model
```

    SequentialModule(
      (0): R2Conv([C4_on_R2[(None, 4)]:
           {irrep_0 (x1)}(1)], [C4_on_R2[(None, 4)]: {regular (x4)}(16)], kernel_size=3, stride=1)
      (1): InnerBatchNorm([C4_on_R2[(None, 4)]:
           {regular (x4)}(16)], eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (2): ReLU(inplace=False, type=[C4_on_R2[(None, 4)]: {regular (x4)}(16)])
      (3): R2Conv([C4_on_R2[(None, 4)]:
           {regular (x4)}(16)], [C4_on_R2[(None, 4)]: {regular (x4)}(16)], kernel_size=3, stride=1)
      (4): InnerBatchNorm([C4_on_R2[(None, 4)]:
           {regular (x4)}(16)], eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
      (5): ReLU(inplace=False, type=[C4_on_R2[(None, 4)]: {regular (x4)}(16)])
      (6): R2Conv([C4_on_R2[(None, 4)]:
           {regular (x4)}(16)], [C4_on_R2[(None, 4)]: {regular (x1)}(4)], kernel_size=3, stride=1)
    )

Calling this model on some input image, we get:

``` r
x <- torch$randn(1L, 1L, 17L, 17L)
x <- feat_type_in(x)
model(x)$shape |> unlist()
```

    [1]  1  4 11 11

What we do now depends on the task. Since we didn't preserve the original resolution anyway -- as would have been required for, say, segmentation -- we probably want one feature vector per image. That we can achieve by spatial pooling:

``` r
avgpool <- nn$PointwiseAvgPool(feat_type_out, 11L)
y <- avgpool(model(x))
y$shape |> unlist()
```

    [1] 1 4 1 1

We still have four "channels", corresponding to four group elements. This feature vector is (approximately) translation-*in*variant, but rotation-*equi*variant, in the sense expressed by the choice of group. Often, the final output will be expected to be group-invariant as well as translation-invariant (as in image classification). If that's the case, we pool over group elements, as well:

``` r
invariant_map <- nn$GroupPooling(feat_type_out)
y <- invariant_map(avgpool(model(x)))
y$tensor
```

    tensor([[[[-0.0293]]]], grad_fn=<CopySlices>)

We end up with an architecture that, from the outside, will look like a standard convnet, while on the inside, all convolutions have been performed in a rotation-equivariant way. Training and evaluation then are no different from the usual procedure.

## Where to from here

This "introduction to an introduction" has been the attempt to draw a high-level map of the terrain, so you can decide if this is useful to you. If it's not just useful, but interesting theory-wise as well, you'll find lots of excellent materials linked from the [README](https://github.com/QUVA-Lab/escnn). The way I see it, though, this post already should enable you to actually experiment with different setups.

One such experiment, that would be of high interest to me, might investigate how well different types and degrees of equivariance actually work for a given task and dataset. Overall, a reasonable assumption is that, the higher "up" we go in the feature hierarchy, the less equivariance we require. For edges and corners, taken by themselves, full rotation equivariance seems desirable, as does equivariance to reflection; for higher-level features, we might want to successively restrict allowed operations, maybe ending up with equivariance to mirroring merely. Experiments could be designed to compare different ways, and levels, of restriction.[^8]

Thanks for reading!

Photo by <a href="https://unsplash.com/@astrovol?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Volodymyr Tokar</a> on <a href="https://unsplash.com/photos/hwcWBLq1jO8?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>

Weiler, Maurice, Patrick Forré, Erik Verlinde, and Max Welling. 2021. "Coordinate Independent Convolutional Networks - Isometry and Gauge Equivariant Convolutions on Riemannian Manifolds." *CoRR* abs/2106.06020. <https://arxiv.org/abs/2106.06020>.

[^1]: This is nicely explained in, for example, Jakob Schwichtenberg's [Physics from symmetry](http://physicsfromsymmetry.com/).

[^2]: If you have some background on representations: No, not *those* characters ...

[^3]: Yes, that word [exists](https://www.merriam-webster.com/dictionary/quaternity), although I must admit I didn't know before typing it into a search engine.

[^4]: One paper particularly stood out to me: (Weiler et al. 2021).

[^5]: Directly pertinent to today's topic, thinking of the materials produced for University of Amsterdam's [course on group-equivariant deep learning](https://uvagedl.github.io/).

[^6]: If, after reading this post, you feel that maybe *you* would be interested in porting it -- I can definitely say I think that's a great idea!

[^7]: If you're new to `reticulate`, please consult its excellent documentation on topics like [calling Python from R](https://rstudio.github.io/reticulate/articles/calling_python.html), [determining the Python version used](https://rstudio.github.io/reticulate/articles/versions.html), [installing Python packages](https://rstudio.github.io/reticulate/articles/python_packages.html), as well as an outstanding [introduction to Python for R users](https://rstudio.github.io/reticulate/articles/python_primer.html).

[^8]: See the documentation for [`escnn$nn$RestrictionModule`](https://quva-lab.github.io/escnn/api/escnn.nn.html?highlight=restrictionmodule#escnn.nn.RestrictionModule) for how to do this.
