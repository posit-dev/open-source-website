---
title: GWAS Catalog access with gwasrapidd
image: page-1.png
resource_type: cheatsheet
by: community
date: '2019-06-01'
description: Retrieve studies, associations, variants, and traits from the NHGRI-EBI GWAS Catalog REST API programmatically in R.
download_url: gwasrapidd.pdf
people:
- Ramiro Magno
thumbnails:
- page-1.png
languages:
- R
---

gwasrapidd provides programmatic access to the GWAS Catalog, a manually curated database of published genome-wide association studies from the EMBL-EBI and NHGRI. Each of the four core catalog entities is mapped to an S4 R object, which can be retrieved, inspected, and subset.

## What's covered
- Introduction – GWAS Catalog entities: studies, associations, variants, traits
- Get GWAS Catalog entities – `get_studies()`, `get_associations()`, `get_variants()`, `get_traits()`
- S4 class studies – slots and primary key
- S4 class associations – slots and primary key
- S4 class variants – slots and primary key
- S4 class traits – EFO traits table
- Manipulate cases – subset by identifier or position, `union()`, `bind()`
