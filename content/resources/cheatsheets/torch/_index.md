---
title: Deep learning with torch
image: page-1.png
resource_type: cheatsheet
by: community
date: '2023-02-01'
description: Build and train deep learning models in R using the torch package and its PyTorch backend.
download_url: torch.pdf
people:
- Christophe Regouby
thumbnails:
- page-1.png
- page-2.png
software:
- torch
languages:
- R
source_files:
- file: torch.key
  format: Keynote
translations:
- language: French
  lang: fr
  file: torch_fr.pdf
  edition: torch 0.9.0
  updated: 2023-02
  people:
  - Christophe Regouby
  source: torch_fr.key
---

The torch R package is based on PyTorch and provides a flexible low-level interface for building
neural networks with optional GPU acceleration. It supports defining custom modules, assembling
sequential networks, training loops, and a broad set of layer types for image, text, and tabular data.

## What's covered
- Working with torch models – `nn_module`, `nn_sequential`, model fit and evaluation
- Optimization – `optim_sgd`, `optim_adam`
- Classification loss functions – `nn_cross_entropy_loss`, `nn_bce_loss`, `nn_nll_loss`, and others
- Regression loss functions – `nn_l1_loss`, `nn_mse_loss`, `nn_kl_div_loss`, and others
- Neural-network layers – `nn_linear`, `nn_sigmoid`, `nn_relu`, `nn_dropout`, `nn_batch_norm1d`
- Convolutional layers – `nn_conv1d`, `nn_conv2d`, `nn_conv3d`, transposed convolutions
- Pooling layers – max pooling, average pooling, and adaptive pooling (1D–3D)
- Recurrent layers – `nn_rnn`, `nn_gru`, `nn_lstm`
- Tensor manipulation – creation, shape operations, slicing, concatenation, and value operations
- Pre-trained models and importing from PyTorch
