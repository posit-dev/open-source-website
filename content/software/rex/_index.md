---
description: Friendly regular expressions for R.
github: r-lib/rex
languages:
- R
latest_release: '2021-11-24T20:50:29+00:00'
people:
- Hadley Wickham
title: rex
website: https://rex.r-lib.org

external:
  contributors:
  - jimhester
  - kevinushey
  - robertzk
  - hadley
  - MichaelChirico
  - Ironholds
  - DarwinAwardWinner
  - jackwasey
  - salim-b
  - TimTaylor
  - yutannihilation
  description: Friendly regular expressions for R.
  first_commit: '2014-09-23T01:13:17+00:00'
  forks: 28
  languages:
  - R
  last_updated: '2026-02-13T14:17:18.671607+00:00'
  latest_release: '2021-11-24T20:50:29+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  repo: r-lib/rex
  stars: 335
  title: rex
  website: https://rex.r-lib.org
---

Rex transforms the notoriously cryptic world of regular expressions into readable, maintainable R code. Instead of wrestling with patterns like `^(?:(((?:[^:])+)://))?((?:(?:(?!:/).)*)+)(?:(:([[:digit:]]+)))?(?:(/.*))?$`, rex lets you construct expressions using intuitive functions such as `maybe()`, `capture()`, `one_or_more()`, and `numbers`. This human-readable approach dramatically reduces the cognitive load of regex syntax, making it easier to write complex patterns for tasks like URL validation, log parsing, and text extraction.

Built for data scientists and R developers who value code clarity, rex makes regular expressions accessible without sacrificing power. The package integrates seamlessly with PCRE (Perl Compatible Regular Expressions) and offers features like `rex_mode()` for temporary function access with auto-completion. By replacing dense pattern strings with structured, self-documenting code, rex ensures your regex patterns remain understandable months later and collaborative across teams.
