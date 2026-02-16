---
description: ' Javascript Object Signing and Encryption for R'
github: r-lib/jose
languages:
- R
latest_release: '2021-11-06T13:38:21+00:00'
people:
- Jeroen Ooms
title: jose
website: ''

external:
  contributors:
  - jeroen
  - jandix
  - carlganz
  description: ' Javascript Object Signing and Encryption for R'
  first_commit: '2016-02-10T21:40:31+00:00'
  forks: 8
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.970752+00:00'
  latest_release: '2021-11-06T13:38:21+00:00'
  license: NOASSERTION
  people:
  - Jeroen Ooms
  repo: r-lib/jose
  stars: 54
  title: jose
  website: ''
---

jose is an R package that implements JavaScript Object Signing and Encryption (JOSE) standards, enabling you to work with modern cryptographic protocols that power secure authentication and data exchange across the web. The package provides a complete toolkit for handling JSON Web Keys (JWK), JSON Web Signatures (JWS), and JSON Web Tokens (JWT), making it easy to integrate R applications with OAuth 2.0 authentication flows, LetsEncrypt certificate management, and GitHub Apps. Its compatibility with the JavaScript WebCryptoAPI ensures seamless interoperability between R and browser-based applications.

jose supports multiple cryptographic methods including HMAC for shared secret signing, RSA for asymmetric key operations, and elliptic curve cryptography (ECDSA) for high-security applications. Whether you're building APIs that need to verify user tokens, integrating with third-party authentication providers, or implementing secure data transmission protocols, jose provides a straightforward interface that follows modern web standards. The package's adherence to RFCs 7515, 7517, and 7519 ensures your R applications can communicate securely with any platform that uses these widely adopted specifications.
