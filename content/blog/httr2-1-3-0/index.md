---
title: "httr2 1.3.0"
date: 2026-07-13
people:
  - Hadley Wickham
description: >
  httr2 1.3.0 changes how OAuth tokens are cached on disk — you'll need to re-authenticate once after upgrading — and rolls up faster streaming, OAuth server metadata discovery, OpenTelemetry tracing, and a new httr2_translate() function.
image: "featured.jpg"
image-alt: "A baseball player in a pinstriped uniform holds two baseballs against his hip, standing on a blurred green outfield."
topics:
  - Data Wrangling
software:
  - httr2
languages:
  - R
source: tidyverse
hidesubscription: false
photo:
  url: https://unsplash.com/photos/hKzmPs8Axh8
  author: Jose Francisco Morales
---

We're chuffed to announce the release of [httr2](https://httr2.r-lib.org) 1.3.0. httr2 makes it easy to work with web APIs from R, providing a pipeable interface for building requests and a suite of tools for processing the responses.

Get it now:

```r
# install.packages("pak")
pak::pak("httr2")
```

The headline changes in this release all relate to OAuth token caching. They happen behind the scenes, so you shouldn't need to change any code, but you'll likely need to re-authenticate once after upgrading. The rest of this post explains why, and rounds up a handful of smaller features that landed in recent patch releases. See a full list of changes in the [release notes](https://github.com/r-lib/httr2/releases/tag/v1.3.0).

## OAuth token caching

First, a bit of background. When you authenticate with an API using OAuth, the API typically returns a refresh token that you can reuse for a set period. That means you don't have to log in every single time you use the API, which makes for a much nicer experience. To reuse a token across R sessions, however, httr2 has to write it to disk, and that creates a risk: anyone who can read the token could use it to access the API as you.

httr2 takes every precaution it can to keep these tokens safe. They're stored in a user-local cache directory, which is usually excluded from backups and, because it lives outside your working directory, carries no risk of being accidentally committed to git. On top of that, the tokens are encrypted so that only httr2 can read them.

Each token's path on disk is derived from a hash computed with `rlang::hash()`. We recently discovered a bug in that hashing code, and fixing it changes every hash. As a result, httr2 can no longer find your existing cached tokens, so you'll need to re-authenticate once after upgrading.

Since that change already invalidates your cached tokens, we took the opportunity to move where they're stored. Previously we used the rappdirs package to locate the cache directory, but since R 4.0.0 there's been a better built-in alternative: `tools::R_user_dir("httr2", which = "cache")`. We've switched to that, which makes httr2's cache location consistent with other packages and removes the rappdirs dependency.

Making these changes surfaced a long-standing bug. Every time httr2 loads, it's supposed to automatically delete any cached tokens older than 30 days, so that stale tokens don't linger indefinitely. Unfortunately, that pruning never actually worked. Now it does, so old tokens will be cleaned up once they pass 30 days, regardless of which cache directory or hashing algorithm produced them. This is good security practice: the longer a credential sits on disk, the more opportunities there are for it to leak, so removing tokens you're no longer using shrinks that window of exposure. If you'd like to prune every cached token yourself, you can call `oauth_cache_prune(max_age_days = 0)`.

## Other features

Alongside the token caching work, this release also rolls up a few smaller features that first appeared in recent patch releases:

- **Faster streaming** (1.2.3): `resp_stream_lines()`, `resp_stream_sse()`, and `resp_stream_aws()` now decode whole chunks at a time and hold the results in a queue, instead of rescanning and recopying the buffer for every line or event. This makes memory use and run time scale linearly rather than quadratically, so large streams are dramatically faster (e.g. reading a 1 MB response of short lines is now around 200x faster and uses around 180x less memory). `resp_stream_sse()` is used heavily by [ellmer](https://ellmer.tidyverse.org), so this should make your LLM streaming feel a little zippier.

- **OAuth server metadata discovery** (1.2.3): the new `oauth_server_metadata()` discovers an OAuth/OIDC issuer's endpoints from its `.well-known` document, and `oauth_client()` gains a `metadata` argument so you can supply all of those endpoints at once.

- **OpenTelemetry tracing** (1.2.2): httr2 now emits OpenTelemetry traces for all requests when tracing is enabled. This requires the otelsdk package and is part of our cross-package work to improve the [observability of R packages](https://opensource.posit.co/blog/2026-05-07_opentelemetry/).

- **`httr2_translate()`** (1.2.3): this new function translates an httr2 request into the equivalent curl command. It's handy for debugging, or for creating reprexes to share with people who don't use R.
