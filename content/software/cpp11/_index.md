---
description: cpp11 helps you to interact with R objects using C++ code.
github: r-lib/cpp11
languages:
- C++
latest_release: '2026-01-20T19:57:34+00:00'
people:
- Davis Vaughan
- Jeroen Ooms
- Jenny Bryan
- Hadley Wickham
- Emil Hvitfeldt
- Thomas Lin Pedersen
- Neal Richardson
title: cpp11
website: https://cpp11.r-lib.org/

external:
  contributors:
  - jimhester
  - DavisVaughan
  - romainfrancois
  - bkietz
  - sbearrows
  - alyst
  - jeroen
  - richfitz
  - pachadotdev
  - jennybc
  - kevinushey
  - klmr
  - hadley
  - thisisnic
  - EmilHvitfeldt
  - MichaelChirico
  - mpadge
  - eutwt
  - vspinu
  - xhochy
  - tcpan
  - tmastny
  - thomasp85
  - patrickvossler18
  - nealrichardson
  - batpigandme
  - renkun-ken
  - krlmlr
  - jonthegeek
  - IndrajeetPatil
  - yutannihilation
  - paleolimbot
  - amoeba
  - Anirban166
  - andrjohns
  description: cpp11 helps you to interact with R objects using C++ code.
  first_commit: '2020-06-10T18:40:48+00:00'
  forks: 54
  languages:
  - C++
  last_updated: '2026-02-13T14:17:20.339203+00:00'
  latest_release: '2026-01-20T19:57:34+00:00'
  license: NOASSERTION
  people:
  - Davis Vaughan
  - Jeroen Ooms
  - Jenny Bryan
  - Hadley Wickham
  - Emil Hvitfeldt
  - Thomas Lin Pedersen
  - Neal Richardson
  repo: r-lib/cpp11
  stars: 222
  title: cpp11
  website: https://cpp11.r-lib.org/
---

cpp11 is a header-only library that enables seamless integration between R and C++ code, offering a modern and safer approach to extending R with high-performance compiled code. When you need to optimize computationally intensive operations in your R packages or leverage existing C++ libraries, cpp11 provides an intuitive interface that enforces copy-on-write semantics to prevent unintended data modifications while supporting modern features like ALTREP objects and UTF-8 string handling. Its architecture delivers faster compilation times with reduced memory requirements compared to traditional approaches, making it ideal for package developers who want to boost performance without sacrificing safety.

What makes cpp11 particularly valuable for R package developers is its completely header-only design, which eliminates ABI compatibility issues and allows you to vendor the headers directly into your package for maximum stability. The library leverages C++11 features to provide more efficient vector growth mechanisms and an optimized memory protection system, while maintaining a syntax that will feel familiar if you have used similar tools. Whether you are building statistical algorithms, data manipulation routines, or interfaces to external C++ libraries, cpp11 provides a robust foundation that balances performance, safety, and developer productivity.
