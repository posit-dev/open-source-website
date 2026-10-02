---
title: PGS Catalog access with quincunx
image: page-1.png
resource_type: cheatsheet
by: community
date: '2021-05-01'
description: Access the PGS Catalog database of published polygenic scores from R using quincunx's REST API interface.
download_url: quincunx.pdf
people:
- Ramiro Magno
thumbnails:
- page-1.png
- page-2.png
languages:
- R
source_files:
- file: quincunx_cheatsheet_page01.svg
  format: Inkscape (SVG, page 1)
- file: quincunx_cheatsheet_page02.svg
  format: Inkscape (SVG, page 2)
---

The quincunx package provides programmatic access to the PGS Catalog, a curated repository of published polygenic scores maintained by EMBL-EBI and the University of Cambridge. It maps the five core catalog entities—scores, publications, sample sets, performance metrics, and traits—to S4 objects in R, and supports retrieval by PGS ID, EFO ID, PubMed ID, author, or trait term.

## What's covered
- Introduction – PGS Catalog overview and REST API structure
- PGS Catalog entities in R – S4 classes for scores, publications, sample sets, performance metrics, and traits with tidy relational tables
- Get PGS Catalog entities – retrieval functions with `pgs_id`, `pgp_id`, `pss_id`, `efo_id`, and `pubmed_id` query criteria
- Other S4 entities – `trait_categories`, `cohorts`, `releases`
- Cohorts, samples, and sample sets – data structure, identifiers, and demographics tables
- PGS construction process – GWAS samples, polygenic score derivation, and performance metrics
- Polygenic scoring file – file format description and field reference
