---
image: logo.svg
color: "#447099"
description: ICMP and TCP ping and related tools
github: r-lib/pingr
languages:
- C
latest_release: '2024-12-12T09:17:13+00:00'
people:
- Gábor Csárdi
- Jeroen Janssens
title: pingr
website: http://r-lib.github.io/pingr/

external:  # updated automatically, do not edit
  description: ICMP and TCP ping and related tools
  first_commit: '2014-09-21T14:36:10+00:00'
  forks: 9
  languages:
  - C
  last_updated: '2026-03-05T16:25:16.166817+00:00'
  latest_release: '2024-12-12T09:17:13+00:00'
  license: NOASSERTION
  people:
  - Gábor Csárdi
  - Jeroen Janssens
  repo: r-lib/pingr
  stars: 38
  title: pingr
  website: http://r-lib.github.io/pingr/
---

The pingr package provides tools to check if remote computers and web servers are accessible. It supports ICMP ping, TCP port checking, DNS queries, and determining if your computer is online.

The package offers a portable alternative to system-specific network utilities, working consistently across platforms. It can measure roundtrip times for network diagnostics, query your public IP address, and perform flexible DNS lookups with more functionality than base R's nsl(). The TCP ping feature is particularly useful for checking if specific services are running on remote hosts without relying on ICMP, which is often blocked by firewalls.
