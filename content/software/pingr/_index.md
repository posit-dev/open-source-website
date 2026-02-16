---
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

external:
  contributors:
  - gaborcsardi
  - pekkarr
  - jeroenjanssens
  - edavidaja
  description: ICMP and TCP ping and related tools
  first_commit: '2014-09-21T14:36:10+00:00'
  forks: 9
  languages:
  - C
  last_updated: '2026-02-13T14:17:18.638960+00:00'
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

pingr is a lightweight R package that provides essential network diagnostic tools for checking server availability and connectivity status. Whether you need to verify that a remote server is responding, check if a specific service is running on a TCP port, or determine your public IP address, pingr offers a clean, R-native interface to these fundamental networking operations. The package leverages system-level ICMP ping utilities and TCP connections to deliver reliable connectivity checks that are crucial for automated workflows, monitoring systems, and troubleshooting network issues.

What makes pingr particularly valuable for data scientists and developers is its comprehensive approach to connectivity verification. Beyond basic ping functionality, it includes specialized tools like `ping_port()` for checking whether specific services are listening on particular ports, `is_online()` for robust internet connectivity detection using multiple fallback methods, and enhanced DNS query capabilities that surpass R's standard lookup functions. These features make it an indispensable tool for building resilient data pipelines that depend on remote resources, automating server health checks, or simply diagnosing connectivity problems in reproducible workflows.
