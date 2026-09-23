---
image: logo.svg
color: "#D44000"
description: LibTorch builds for the M1 Macs
github: mlverse/libtorch-mac-m1
latest_release: '2023-05-09T14:33:40+00:00'
people:
- Daniel Falbel
title: libtorch-mac-m1
website: ''

external:  # updated automatically, do not edit
  description: LibTorch builds for the M1 Macs
  first_commit: '2022-10-03T14:23:44+00:00'
  forks: 9
  last_updated: '2026-09-18T14:19:08.360133+00:00'
  latest_release: '2023-05-09T14:33:40+00:00'
  people:
  - Daniel Falbel
  repo: mlverse/libtorch-mac-m1
  stars: 54
  title: libtorch-mac-m1
  website: ''
---

This repository provides a GitHub Actions workflow for building LibTorch (PyTorch's C++ frontend library) on Apple Silicon (M1) Macs. Built libraries are published as GitHub releases for easy download.

The builds follow the official PyTorch CMake instructions with MPS (Metal Performance Shaders) support enabled, allowing GPU-accelerated inference and training on Apple Silicon hardware. This is useful for developers who need precompiled LibTorch binaries for M1/M2 Macs without having to build from source themselves, which can be a time-consuming process requiring a specific toolchain and environment setup.
