---
description: scrypt cryptographic functions for R
github: rstudio/rscrypt
languages:
- C
title: rscrypt
website: ''

external:
  contributors:
  - kippandrew
  - bobjansen
  - kevinushey
  description: scrypt cryptographic functions for R
  first_commit: '2013-12-20T16:13:16+00:00'
  forks: 11
  languages:
  - C
  last_updated: '2026-02-13T14:17:01.370379+00:00'
  license: BSD-2-Clause
  repo: rstudio/rscrypt
  stars: 33
  title: rscrypt
  website: ''
---

rscrypt brings enterprise-grade cryptographic functionality to R, implementing the scrypt password-based key derivation algorithm designed specifically for secure password hashing. Unlike traditional hashing methods, scrypt is memory-hard, making it computationally expensive to perform large-scale brute-force attacks. This makes it ideal for data scientists and developers who need to protect sensitive information in their R applications, from securing user authentication systems to safeguarding confidential data workflows.

The package provides intuitive functions for hashing and verifying passwords, generating derived keys, and performing cryptographic operations directly within R. Hash outputs include built-in security parameters, salt values, and HMAC verification for integrity checking, ensuring comprehensive protection. With compatibility across Node.js implementations and no external dependencies beyond standard development tools, rscrypt makes it straightforward to incorporate robust security practices into your data science projects and R-based applications.
