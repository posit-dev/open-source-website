---
title: "torch Ecosystem Updates"
date: 2026-04-30
people:
  - Daniel Falbel
  - Tomasz Kalinowski
description: >
  An overview of recent updates across the torch ecosystem.
image: "thumbnail.svg"
image-alt: "torch hex logo on a dark blue gradient background"
topics:
  - Machine Learning
software:
  - torch
languages:
  - R
---

We've just published a new round of CRAN releases across the [torch](https://github.com/mlverse/torch) ecosystem. Here's a tour of what's new in each package.

## torch v0.17.0

The most exciting experimental new feature is support for the [cudatoolkit](https://github.com/mlverse/cudatoolkit)
packages. With this, you no longer need a global CUDA toolkit installation in order to use torch on the GPU.

You can now do:

```r
install.packages(
  "cuda12.8", 
  repos = c("https://mlverse.r-universe.dev", "https://cloud.r-project.org")
)
install.packages("torch")
```

The `{cuda12.8}` package bundles all the CUDA runtime libraries and torch can find it and use it by default.
See more details in the [installation docs](https://torch.mlverse.org/docs/articles/installation#cudatoolkit).

We also highlight the update to LibTorch v2.8.0 led by [Troy Hernandez](https://github.com/TroyHernandez) ([#1419](https://github.com/mlverse/torch/pull/1419)).

Additionally, this release includes many small bug fixes and small additions to the API. See the full release notes
in the [changelog](https://torch.mlverse.org/docs/news/#torch-0170).

## torchvision v0.9.0

[torchvision](https://github.com/mlverse/torchvision) provides datasets, model architectures, and image transformations for computer vision. This is a big release with new models, datasets, and many improvements — largely driven by community contributors.

### New models:

- `model_maskrcnn_resnet50_fpn()` and `model_maskrcnn_resnet50_fpn_v2()` for instance segmentation.
- `model_convnext_*_detection()` for object detection (tiny/small/base).
- `model_convnext_*_fcn()` and `model_convnext_*_upernet()` for semantic segmentation (tiny/small/base).

### New datasets and features:

- `vggface2_dataset()` for loading the VGGFace2 dataset.
- New `coco_segmentation_dataset()`, split from `coco_detection_dataset()`, reducing memory usage by ~50%.
- Collection dataset catalog with `search_collection()`, `get_collection_catalog()`, and `list_collection_datasets()` for discovering and exploring datasets.
- New visualization utilities `draw_segmentation_masks()` and `vision_make_grid()`.

See the full release notes in the [changelog](https://github.com/mlverse/torchvision/releases/tag/v0.9.0).

A huge thank you to the community contributors who made this release possible: [@cregouby](https://github.com/cregouby), [@ANAMASGARD](https://github.com/ANAMASGARD), [@Chandraveersingh1717](https://github.com/Chandraveersingh1717), [@DerrickUnleashed](https://github.com/DerrickUnleashed), and [@srishtiii28](https://github.com/srishtiii28).

## Other releases

Most of the other packages don't have significant changes, and the releases add minimal improvements to docs, CI infrastructure and CRAN related updates.

- **[luz](https://github.com/mlverse/luz/releases/tag/v0.5.2)** v0.5.2 — Higher-level API for torch with a Keras-like interface for training neural networks.
- **[hfhub](https://github.com/mlverse/hfhub/releases/tag/v0.1.2)** v0.1.2 — Download and cache files from Hugging Face Hub repositories, making it easy to use pretrained models and datasets from R.
- **[tok](https://github.com/mlverse/tok/releases/tag/v0.2.2)** v0.2.2 — Fast tokenizers for R, powered by the Hugging Face Tokenizers library written in Rust. Supports BPE, WordPiece, and other tokenization algorithms.
- **[torchdatasets](https://github.com/mlverse/torchdatasets/releases/tag/v0.3.1)** v0.3.1 — Extra ready-to-use datasets for torch, complementing the built-in datasets in torchvision.
- **[safetensors](https://github.com/mlverse/safetensors/releases/tag/v0.2.1)** v0.2.1 — Read and write the Safetensors file format, a safe and fast format for storing and loading tensors.
- **[tfevents](https://github.com/mlverse/tfevents/releases/tag/v0.0.5)** v0.0.5 — Write event files compatible with TensorBoard from R for experiment tracking and visualization.
- **[wav](https://github.com/mlverse/wav/releases/tag/v0.1.1)** v0.1.1 — Read and write WAV files in R.

## New maintainer

We're excited to welcome [Tomasz Kalinowski](https://github.com/t-kalinowski) as the new maintainer of torch and the broader mlverse ecosystem.
