---
description: A simple S3 class for representing BLOBs
github: tidyverse/blob
languages:
- R
latest_release: '2026-01-13T06:57:50+00:00'
people:
- Hadley Wickham
- Davis Vaughan
- Jeroen Janssens
title: blob
website: https://blob.tidyverse.org

external:
  contributors:
  - krlmlr
  - hadley
  - IndrajeetPatil
  - batpigandme
  - MichaelChirico
  - DavisVaughan
  - jeroenjanssens
  - jimhester
  - MikeJohnPage
  description: A simple S3 class for representing BLOBs
  first_commit: '2016-10-27T13:11:54+00:00'
  forks: 14
  languages:
  - R
  last_updated: '2026-02-13T14:17:08.734697+00:00'
  latest_release: '2026-01-13T06:57:50+00:00'
  license: NOASSERTION
  people:
  - Hadley Wickham
  - Davis Vaughan
  - Jeroen Janssens
  repo: tidyverse/blob
  stars: 49
  title: blob
  website: https://blob.tidyverse.org
---

blob is a lightweight R package that provides a standardized way to handle binary data within data frames. It wraps raw vectors in a simple S3 class that integrates seamlessly with R's data frame infrastructure, making it possible to store and manipulate binary objects alongside traditional data types. For data scientists working with databases or binary file formats, blob operates transparently in the background, automatically handling BLOB columns imported from SQL databases or other sources that contain non-text data.

While most users may never directly call blob's functions, the package plays a critical role in R's data ecosystem by standardizing how binary content is represented and manipulated. This standardization eliminates the complexity of working with raw binary data in analytical workflows, whether you're reading images from a database, handling encrypted data, or processing binary file formats. By providing a consistent interface through functions like blob(), as_blob(), and new_blob(), the package ensures that binary data can be treated as naturally as numeric or character vectors in your data analysis pipelines.
