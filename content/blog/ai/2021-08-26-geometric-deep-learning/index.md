---
title: 'Beyond alchemy: A first look at geometric deep learning'
description: |
  Geometric deep learning is a "program" that aspires to situate deep learning architectures and techniques in a framework of mathematical priors. The priors, such as various types of invariance, first arise in some physical domain. A neural network that well matches the domain will preserve as many invariances as possible. In this post, we present a very conceptual, high-level overview, and highlight a few applications.
date: '2021-08-26'
slug: keydanageometricdl
categories:
  - Best Practices
author:
  - name: Sigrid Keydana
    affiliation: RStudio
    affiliation_url: https://www.rstudio.com/
people:
  - Sigrid Keydana
image: thumbnail.jpg
ported_from: ai
port_status: in-progress
languages: ["R"]
ported_categories:
  - Concepts
  - Meta
  - R
---



To the practitioner, it may often seem that with deep learning, there is a lot of magic involved. Magic in how hyper-parameter choices affect performance, for example. More fundamentally yet, magic in the impacts of architectural decisions. Magic, sometimes, in that it even works (or not). Sure, papers abound that strive to mathematically prove why, for specific solutions, in specific contexts, this or that technique will yield better results. But theory and practice are strangely dissociated: If a technique *does* turn out to be helpful in practice, doubts may still arise to whether that is, in fact, due to the purported mechanism. Moreover, level of generality often is low.

In this situation, one may feel grateful for approaches that aim to elucidate, complement, or replace some of the magic. By "complement or replace", I'm alluding to attempts to incorporate domain-specific knowledge into the training process. Interesting examples exist in several sciences, and I certainly hope to be able to showcase a few of these, on this blog at a later time. As for the "elucidate", this characterization is meant to lead on to the topic of this post: the program of *geometric deep learning*.

## Geometric deep learning: An attempt at unification

Geometric deep learning (henceforth: GDL) is what a group of researchers, including Michael Bronstein, Joan Bruna, Taco Cohen, and Petar Velicković, call their attempt to build a framework that places deep learning (DL) on a solid mathematical basis.

Prima facie, this is a scientific endeavor: They take existing architectures and practices and show where these fit into the "DL blueprint". DL research being all but confined to the ivory tower, though, it's fair to assume that this is not all: From those mathematical foundations, it should be possible to derive new architectures, new techniques to fit a given task. Who, then, should be interested in this? Researchers, for sure; to them, the framework may well prove highly inspirational. Secondly, everyone interested in the mathematical constructions themselves --- this probably goes without saying. Finally, the rest of us, as well: Even understood at a purely conceptual level, the framework offers an exciting, inspiring view on DL architectures that -- I think -- is worth getting to know about as an end in itself. The goal of this post is to provide a high-level introduction .

Before we get started though, let me mention the primary source for this text: [Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges](https://arxiv.org/abs/2104.13478) (Bronstein et al. (2021)).

### Geometric priors

A *prior*, in the context of machine learning, is a constraint imposed on the learning task. A generic prior could come about in different ways; a *geometric* prior, as defined by the GDL group, arises, originally, from the underlying *domain* of the task. Take image classification, for example. The domain is a two-dimensional grid. Or graphs: The domain consists of collections of nodes and edges.

In the GDL framework, two all-important geometric priors are symmetry and scale separation.

#### Symmetry

A symmetry, in physics and mathematics, is a transformation that leaves some property of an object unchanged. The appropriate meaning of "unchanged" depends on what sort of property we're talking about. Say the property is some "essence", or identity --- what object something is. If I move a few steps to the left, I'm still myself: The essence of being "myself" is shift-*invarian*t. (Or: translation-invariant.) But say the property is location. If I move to the left, my location moves to the left. Location is shift-*equivariant*. (Translation-equivariant.)

So here we have two forms of symmetry: invariance and equivariance. One means that when we transform an object, the thing we're interested in stays the same. The other means that we have to transform that thing as well.

The next question then is: What are possible transformations? Translation we already mentioned; on images, rotation or flipping are others. Transformations are composable; I can rotate the digit `3` by thirty degrees, then move it to the left by five units; I could also do things the other way around. (In this case, though not necessarily in general, the results are the same.) Transformations can be undone: If first I rotate, in some direction, by five degrees, I can then rotate in the opposite one, also by five degrees, and end up in the original position. We'll see why this matters when we cross the bridge from the domain (grids, sets, etc.) to the learning algorithm.

#### Scale separation

After symmetry, another important geometric prior is scale separation. Scale separation means that even if something is very "big" (extends a long way in, say, one or two dimensions), we can still start from small patches and "work our way up". For example, take a cuckoo clock. To discern the hands, you don't need to pay attention to the pendulum. And vice versa. And once you've taken inventory of hands and pendulum, you don't have to care about their texture or exact position anymore.

In a nutshell, given scale separation, the top-level structure can be determined through successive steps of *coarse-graining*. We'll see this prior nicely reflected in some neural-network algorithms.

### From domain priors to algorithmic ones

So far, all we've really talked about is the *domain*, using the word in the colloquial sense of "on what structure", or "in terms of what structure", something is given. In mathematical language, though, domain is used in a more narrow way, namely, for the "input space" of a *function*. And a function, or rather, two of them, is what we need to get from priors on the (physical) domain to priors on neural networks.

The first function maps from the physical domain to *signal* space. If, for images, the domain was the two-dimensional grid, the signal space now consists of images the way they are represented in a computer, and will be worked with by a learning algorithm. For example, in the case of RGB images, that representation is three-dimensional, with a color dimension on top of the inherited spatial structure. What matters is that by this function, the priors are preserved. If something is translation-invariant before "real-to-virtual" conversion, it will still be translation-invariant thereafter.

Next, we have another function: the algorithm, or neural network, acting on signal space. Ideally, this function, again, would preserve the priors. Below, we'll see how basic neural-network architectures typically preserve some important symmetries, but not necessarily all of them. We'll also see how, at this point, the actual *task* makes a difference. Depending on what we're trying to achieve, we may want to maintain some symmetry, but not care about another. The task here is analogous to the property in physical space. Just like in physical space, a movement to the left does not alter *identity*, a *classifier*, presented with that same shift, won't care at all. But a *segmentation* algorithm will -- mirroring the real-world shift in *position*.

Now that we've made our way to algorithm space, the above requirement, formulated on physical space -- that transformations be composable -- makes sense in another light: Composing functions is exactly what neural networks do; we want these compositions to work just as deterministically as those of real-world transformations.

In sum, the geometric priors and the way they impose constraints, or desiderates, rather, on the learning algorithm lead to what the GDL group call their deep learning "blueprint". Namely, a network should be composed of the following types of modules:

- Linear group-equivariant layers. (Here group is the group of transformations whose symmetries we're interested to preserve.)

- Nonlinearities. (This really does not follow from geometric arguments, but from the observation, often stated in introductions to DL, that without nonlinearities, there is no hierarchical composition of features, since all operations can be implemented in a single matrix multiplication.)

- Local pooling layers. (These achieve the effect of coarse-graining, as enabled by the scale separation prior.)

- A group-invariant layer (global pooling). (Not every task will require such a layer to be present.)

Having talked so much about the concepts, which are highly fascinating, this list may seem a bit underwhelming. That's what we've been doing anyway, right? Maybe; but once you look at a few domains and associated network architectures, the picture gets colorful again. So colorful, in fact, that we can only present a very sparse selection of highlights.

## Domains, priors, architectures

Given cues like "local" and "pooling", what better architecture is there to start with than CNNs, the (still) paradigmatic deep learning architecture? Probably, it's also the one a prototypic practitioner would be most familiar with.

### Images and CNNs

Vanilla CNNs are easily mapped to the four types of layers that make up the blueprint. Skipping over the nonlinearities, which, in this context, are of least interest, we next have two kinds of pooling.

First, a local one, corresponding to max- or average-pooling layers with small strides (2 or 3, say). This reflects the idea of successive coarse-graining, where, once we've made use of some fine-grained information, all we need to proceed is a summary.

Second, a global one, used to effectively remove the spatial dimensions. In practice, this would usually be global average pooling. Here, there's an interesting detail worth mentioning. A common practice, in image classification, is to replace global pooling by a combination of flattening and one or more feedforward layers. Since with feedforward layers, position in the input matters, this will do away with translation invariance.

Having covered three of the four layer types, we come to the most interesting one. In CNNs, the local, group-equivariant layers are the convolutional ones. What kinds of symmetries does convolution preserve? Think about how a kernel slides over an image, computing a dot product at every location. Say that, through training, it has developed an inclination toward singling out penguin bills. It will detect, and mark, one everywhere in an image --- be it shifted left, right, top or bottom in the image. What about rotational motion, though? Since kernels move vertically and horizontally, but not in a circle, a rotated bill will be missed. Convolution is shift-equivariant, not rotation-invariant.

There is something that can be done about this, though, while fully staying within the framework of GDL. Convolution, in a more generic sense, does not have to imply constraining filter movement to horizontal and vertical translation. When reflecting a general *group convolution*, that motion is determined by whatever transformations constitute the group action. If, for example, that action included translation by sixty degrees, we could rotate the filter to all valid positions, then take these filters and have them slide over the image. In effect, we'd just wind up with more channels in the subsequent layer -- the intended base number of filters times the number of attainable positions.

This, it must be said, it just one way to do it. A more elegant one is to apply the filter in the Fourier domain, where convolution maps to multiplication. The Fourier domain, however, is as fascinating as it is out of scope for this post.

The same goes for extensions of convolution from the Euclidean grid to manifolds, where distances are no longer measured by a straight line as we know it. Often on manifolds, we're interested in invariances beyond translation or rotation: Namely, algorithms may have to support various types of deformation. (Imagine, for example, a moving rabbit, with its muscles stretching and contracting as it hobbles.) If you're interested in these kinds of problems, the GDL book goes into those in great detail.

For group convolution on grids -- in fact, we may want to say "on things that can be arranged in a grid" -- the authors give two illustrative examples. (One thing I like about these examples is something that extends to the whole book: Many applications are from the world of natural sciences, encouraging some optimism as to the role of deep learning ("AI") in society.)

One example is from medical volumetric imaging (MRI or CT, say), where signals are represented on a three-dimensional grid. Here the task calls not just for translation in all directions, but also, rotations, of some sensible degree, about all three spatial axes. The other is from DNA sequencing, and it brings into play a new kind of invariance we haven't mentioned yet: reverse-complement symmetry. This is because once we've decoded one strand of the double helix, we already know the other one.

Finally, before we wrap up the topic of CNNs, let's mention how through creativity, one can achieve -- or put cautiously, try to achieve -- certain invariances by means other than network architecture. A great example, originally associated mostly with images, is data augmentation. Through data augmentation, we may hope to make training invariant to things like slight changes in color, illumination, perspective, and the like.

### Graphs and GNNs

Another type of domain, underlying many scientific and non-scientific applications, are graphs. Here, we are going to be a lot more brief. One reason is that so far, we have not had many posts on deep learning on graphs, so to the readers of this blog, the topic may seem fairly abstract. The other reason is complementary: That state of affairs is exactly something we'd like to see changing. Once we write more about graph DL, occasions to talk about respective concepts will be plenty.

In a nutshell, though, the dominant type of invariance in graph DL is permutation equivariance. Permutation, because when you stack a node and its features in a matrix, it doesn't matter whether node one is in row three or row fifteen. Equivariance, because once you *do* permute the nodes, you also have to permute the adjacency matrix, the matrix that captures which node is linked to what other nodes. This is very different from what holds for images: We can't just randomly permute the pixels.

### Sequences and RNNs

With RNNs, we are going be very brief as well, although for a different reason. My impression is that so far, this area of research -- meaning, GDL as it relates to sequences -- has not received too much attention yet, and (maybe) for that reason, seems of lesser impact on real-world applications.

In a nutshell, the authors refer two types of symmetry: First, translation-invariance, as long as a sequence is left-padded for a sufficient number of steps. (This is due to the hidden units having to be initialized *somehow*.) This holds for RNNs in general.

Second, *time warping*: If a network can be trained that correctly works on a sequence measured on some time scale, there is another network, of the same architecture but likely with different weights, that will work equivalently on re-scaled time. This invariance only applies to *gated* RNNs, such as the LSTM.

### What's next?

At this point, we conclude this conceptual introduction. If you want to learn more, and are not too scared by the math, definitely check out the book. (I'd also say it lends itself well to incremental understanding, as in, iteratively going back to some details once one has acquired more background.)

Something else to wish for certainly is practice. There is an intimate connection between GDL and deep learning on graphs; which is one reason we're hoping to be able to feature the latter more frequently in the future. The other is the wealth of interesting applications that take graphs as their input. Until then, thanks for reading!

Photo by [NASA](https://unsplash.com/@nasa?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Bronstein, Michael M., Joan Bruna, Taco Cohen, and Petar Velickovic. 2021. "Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges." *CoRR* abs/2104.13478. <https://arxiv.org/abs/2104.13478>.
