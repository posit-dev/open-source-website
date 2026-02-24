---
description: scrypt cryptographic functions for R
github: rstudio/rscrypt
languages:
- C
title: rscrypt
website: ''

external:  # updated automatically, do not edit
  description: scrypt cryptographic functions for R
  first_commit: '2013-12-20T16:13:16+00:00'
  forks: 11
  languages:
  - C
  last_updated: '2026-02-24T09:26:14.596295+00:00'
  license: BSD-2-Clause
  repo: rstudio/rscrypt
  stars: 33
  title: rscrypt
  website: ''
---

rscrypt provides R bindings for the scrypt password-based key derivation function, designed by Colin Percival to resist large-scale hardware attacks through high memory requirements. It offers functions for hashing and verifying passwords, as well as direct access to the scrypt key derivation algorithm.

The package's hash format is compatible with the Node.js scrypt implementation, making it suitable for cross-platform applications. Hashes include embedded parameters (n, r, p), salt, and integrity checks via SHA256 checksums and HMAC-SHA256, enabling secure password storage without requiring separate parameter tracking. The scrypt algorithm's memory-intensive design makes it more resistant to brute-force attacks using custom hardware like ASICs or GPUs compared to traditional password hashing functions.
