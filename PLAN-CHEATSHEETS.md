# Cheat sheet migration plan

Migrate every cheat sheet from the old site (<https://rstudio.github.io/cheatsheets/>, source: <https://github.com/rstudio/cheatsheets>) to `content/resources/cheatsheets/` on this site. That covers Posit sheets, community sheets, and translations. It also adds a "By" (Posit / Community) filter to the overview page.

This document covers inventory and planning only. No cheat sheet or site code has been changed yet.

- Old repo snapshot inspected: `rstudio/cheatsheets@1e5e2bd` (2026-08-27, "Merge pull request #622 from rstudio/ml-yardsstick").
- New site snapshot: `main@e73b895e6`.
- The answers to the first round of questions are in [Decisions](#decisions) (**D1**–**D17**); the follow-ups are in [Follow-up decisions](#follow-up-decisions) (**R1**–**R3**, plus the LFS build note). They're applied throughout.
- Implementation status is tracked in [Implementation progress](#implementation-progress).

---

## Contents

1. [Summary](#summary)
2. [Implementation progress](#implementation-progress)
3. [Decisions](#decisions)
4. [How the two sites are structured](#how-the-two-sites-are-structured)
5. [Design: the `by` field and "By" filter](#design-the-by-field-and-by-filter)
6. [Design: people, translations, source files, PDFs](#design-people-translations-source-files-pdfs)
7. [Migration plan and to-do list](#migration-plan-and-to-do-list)
8. [Follow-up decisions](#follow-up-decisions)
9. [Appendix A: Posit cheat sheets inventory](#appendix-a-posit-cheat-sheets-inventory)
10. [Appendix B: Community cheat sheets inventory](#appendix-b-community-cheat-sheets-inventory)
11. [Appendix C: Translations inventory](#appendix-c-translations-inventory)
12. [Appendix D: Excluded legacy material](#appendix-d-excluded-legacy-material)
13. [Appendix E: Method and how to reproduce](#appendix-e-method-and-how-to-reproduce)

---

## Summary

| | Count |
|---|---|
| Posit cheat sheets (D2) | **33**: 29 on the old index (incl. `renv`), plus `ml-measure-performance` (unlisted on the old site), `polars` (new site only), `tidyeval` and `caret` (listed as contributed on the old site) |
| Community cheat sheets | **65**: the 63 remaining on the old "Contributed" page, plus 2 Spanish-language originals from the Translations page (`introduccion-a-r`, `estadistica-descriptiva-con-R`, see R2) |
| Translations to migrate | **115**: the 124 on the old Translations page, minus 7 `data-wrangling` translations (D4) and the 2 Spanish originals counted above. 91 translate Posit sheets, 24 community sheets |
| Excluded as old (D4) | `old/`, the 2 legacy root copies, 8 PDFs in `previous … translations/`, 7 `data-wrangling` translations, `0-template` (Appendix D) |
| Cheat sheets on the new site today | 30 |

Migration status of the 33 Posit sheets on the new site:

| Status | Cheat sheets |
|---|---|
| **Complete** | `polars`. Its PDF is a Ghostscript copy without tags, though; see Phase 2. |
| **PDF + English markdown** | `data-import`, `data-transformation`, `ml-create-models`, `ml-measure-performance`, `ml-preprocessing-data`, `ml-tidymodels` |
| **PDF only** | the other 23 Posit sheets already on the new site |
| **Not started** | `renv`, `tidyeval`, `caret`, and all 65 community sheets |

### Key findings

1. **20 of the 29 English PDFs on the new site are older than the old repo's.** Most are the 2025 editions; the old repo has the 2026 updates. Completing a sheet therefore includes refreshing its PDF and thumbnails (Appendix A, "PDF" column).
2. **The old site's translation matcher is buggy, and the new site inherited the bug.** `html/common.R::translation_list()` matches `{slug}.+\.pdf`, so `shiny` lists `shiny-python_es.pdf` and `gt` lists `gtsummary_vi.pdf`. Both are now wrong in the new site's front matter.
3. **The new site is missing 3 Posit translations:** `data-import_el.pdf`, `tidyr_es.pdf`, `plumber_es.pdf`.
4. **Nothing on the old site is explicitly marked deprecated or outdated.** D4 settles what counts as "old".
5. **Ghostscript strips PDF tags.** 131 of the 222 PDFs in the old repo are tagged, i.e. have the accessibility structure screen readers use. The two new-site PDFs that went through Ghostscript (`ml-tidymodels`, `polars`) have lost their tags. D9 picks a tool that keeps them.
6. **Four Posit sheets and every community sheet lack a text version.** The old HTML pages for `gt`, `great-tables`, `positron` and `shinychat` are stubs ("Will be updated soon!"). `tidyeval`, `caret` and all community sheets have no HTML page at all. These get a short summary instead (D8).
7. **Source files are about 815 MB.** That's ~468 MB of English sources and ~347 MB of translation sources; the largest is `rstudio-ide.key` at 70 MB. These go into Git LFS (D6). The build doesn't need them: Hugo ignores them, and the source buttons link to the files on GitHub.

---

## Implementation progress

The working to-do list, updated with each implementation commit on `migrate-cheatsheets`.

- [x] **T1.** Plan updated with R1–R3 and the LFS build note
- [x] **T2.** Git LFS: `.gitattributes`, `ignoreFiles` for source files, `cheatsheetSourceBaseURL` param, `polars-cheatsheet.ai` moved to LFS, contributor note
- [ ] **T3.** `by` field + "By" filter: `by: posit` on existing sheets, item index, `filters.yaml`, JS defaults/URL/reset/badge, no-flash CSS
- [ ] **T4.** Detail page: extended translations (label, edition · date, translators), `source_files` buttons
- [ ] **T5.** Tooling: `compress-cheatsheet-pdf.py`, `validate-cheatsheets.py`, migration script + manifest
- [ ] **T6.** Phase 2: refresh, compress, and complete the 30 existing sheets (PDFs, thumbnails, sources, translations, people, markdown)
- [ ] **T7.** Phase 3: `renv`, `tidyeval`, `caret`
- [ ] **T8.** Phase 4: 65 community sheets (bundles, PDFs, thumbnails, sources, translations, summaries)
- [ ] **T9.** Wrap-up: overview copy, contributor docs, validation, Hugo build check, final plan update

---

## Decisions

| # | Topic | Decision | How it's applied in this plan |
|---|---|---|---|
| D1 | Community slugs | Use the proposal | Lowercase, with `_` and spaces → `-`. Named exceptions: `datatable` → `data-table`, `regex` → `regular-expressions`, `profile_optimise_py` → `profile-optimise-python`, `SASvsRinPharma` → `sas-vs-r-in-pharma`. PDF file names inside the bundle keep their old names. Appendix B lists every new slug. |
| D2 | Origin edge cases | All Posit | `tidyeval`, `caret`, `polars`, `ml-measure-performance` get `by: posit` and move to Appendix A. |
| D3 | Who is an author of a Posit sheet | Everybody who worked on it | `people` = every identifiable person in the old-repo history of the sheet's PDF/Keynote/PowerPoint/Illustrator/HTML files, plus the people already on the new site. Excluded: commits in this repo that only migrated files (imports, PDF copies); old-site thumbnail commits, since those PNGs aren't migrated; handles without a clear name (D5). |
| D4 | Legacy material | Don't include old | Skip `old/`, `data-visualization-2.1.pdf`, `rmarkdown-2.0.pdf`, the `previous … translations/` folders, the `data-wrangling` translations (their English sheet only exists in `old/`), and `0-template`. See Appendix D. |
| D5 | Community credits | People only, not organisations. If unclear, don't use | Org-only credits are dropped: ThinkR, NIMBLE Development Team, ranalytics.vn, and so on. A commit author is used as the fallback only when they added the file themselves; a Posit maintainer bulk-uploading doesn't count. Dropped as unclear: credits only implied by a URL (`imputeTS`), the typo'd `mosaic` name, translators marked "?" or with only a GitHub first name or handle (`Violeta R`, `MikeJohnPage`, `Carter`; `David`/`davidrsch` was later identified, see R1), and guessed translators (Evgeni Chasnovski, Harry Zhu). Applied to Posit sheets too. |
| D6 | Source files | Git LFS; the build doesn't need them | `.gitattributes` tracks `*.key`, `*.pptx`, `*.ai` under `content/resources/cheatsheets/`. CI is unchanged (no LFS fetch). Hugo ignores these files (`ignoreFiles`), and the source buttons link to `github.com/posit-dev/open-source-website/raw/main/…`, which serves LFS content. See [Source files](#source-files). |
| D7 | Translators | Kept separate; shown only on the cheat sheet page | Translators go in `translations[].people` only. They're **not** in the page-level `people`, so they appear in no byline, card, search index or `/people/` page. |
| D8 | Missing markdown | Short summary when there's no markdown or text | Port `html/<slug>.qmd` where it has real content. Otherwise write a short summary (a few sentences plus the main topics, taken from the PDF). |
| D9 | PDF compression | Compress; tool is my choice | A new `scripts/compress-cheatsheet-pdf.py` (uv, `pikepdf` + Pillow). It downsamples images above 300 ppi, re-packs losslessly, and keeps tags. **Not Ghostscript**, because it strips tags. See [PDFs](#pdfs). |
| D10 | Badge on the default selection | Show "1" | Initialize the badge from the defaults. |
| D11 | Community sheets elsewhere | Appear everywhere | No special handling. The By filter exists only on the cheat sheet overview. |
| D12 | People pages | Bare taxonomy pages are fine | No new profiles are needed. |
| D13 | `software` for community sheets | Add entries, using only existing `content/software/` slugs | Proposed values are in Appendix B. Most community sheets have none. |
| D14 | Old site after migration | It will be archived; out of scope | No redirect or short-link work in this plan. |
| D15 | Translation labels | Proposed labels are OK | `Chinese (Simplified)`, `Chinese (Traditional)`, `Portuguese (Brazil)`, `Portuguese`. |
| D16 | Outdated translations | Show edition and date | Each translation entry has `edition` and `updated`, shown on its chip. Values are in Appendix C. |
| D17 | Unlisted `ml-measure-performance` | Out of scope | Treated as a normal Posit sheet. |

---

## How the two sites are structured

### Old site (`rstudio/cheatsheets`, Quarto website)

| What | Where |
|---|---|
| English PDFs (Posit + community) | repo root, `<slug>.pdf` |
| Thumbnails | `pngs/<slug>.png` (not used by the new site) |
| Posit index page | `index.qmd`: a Quarto listing of `html/*.qmd` (29 entries) |
| Accessible HTML versions | `html/<slug>.qmd` with `html/common.R` helpers; images in `html/images/` |
| Community page | `contributed-cheatsheets.qmd`: a thumbnail grid with no author names |
| Translations page | `translations.qmd`: lists `translations/<language>/*.pdf` (top level only) |
| Translations | `translations/<language-name>/<slug>_<iso>[_<region>].pdf`, often with `.pptx`/`.key` next to them |
| Source files | `keynotes/*.key`, `powerpoints/*.pptx`, `illustrator/*.ai`, `inkscape/*.svg`, `latex/<slug>/` (`.tex`/`.Rnw`), `google-slides/*.md` (links) |
| Authorship | No metadata anywhere. It's only in PDF footers and git history. |

### New site (Hugo, this repo)

Each cheat sheet is a **branch bundle**, `content/resources/cheatsheets/<slug>/_index.md`. Its PDF, `page-N.png` thumbnails, translation PDFs and images sit in the same directory. Current front matter:

```yaml
title: Importing data with the tidyverse
image: page-1.png              # card image; can be a logo (shiny.svg, team.png, hex-polars.svg)
color: '#cd792c'               # optional card background
resource_type: cheatsheet
date: '2026-02-25'
description: Learn about readr, readxl, haven, and googlesheets4.
download_url: data-import.pdf
people: [Hadley Wickham, Mine Çetinkaya-Rundel]   # `people` taxonomy → byline + /people/<slug>/
thumbnails: [page-1.png, page-2.png]
software: [readr, readxl, haven, googlesheets4]   # folder names in content/software/
languages: [R]                                    # drives the Languages filter
translations:                                     # list of single-key maps {Label: file}
- Bengali: data-import_bn.pdf
# source_url: …   # supported by the template ("Source Code" button) but unused
```

- **Markdown body:** the accessible text version, ported from `html/<slug>.qmd` with ```` ```{r} ```` changed to ```` ```r ````. Code isn't run and outputs aren't included. Some `#|` chunk options leaked through (43 lines).
- **Detail page:** `layouts/resources/term.html`, in the cheat sheet branch at about line 245. It renders the thumbnail lightbox, "Download PDF", the optional "Source Code" button (`source_url`), and the "Available Translations" chips.
- **Overview page:** `content/resources/cheatsheets.md` uses `layouts/resources/resource-type.html`. It renders cards with `partials/item.html` and emits `item-index.json` via `partials/item-index-entry.html`.
- **Filters:** handled by `assets/js/search-filter-sort.js`, configured in `data/filters.yaml` under `cheatsheet:`.
  - Values within one dropdown are OR'ed; separate dropdowns are AND'ed.
  - An empty selection means "no filter".
  - The selection is synced to the URL.
  - The `Other` option uses an exclusion list.
- **Import tooling:**
  - `scripts/import-cheatsheets.py` scrapes the old HTML pages.
  - `scripts/create-cheatsheet-thumbnails.py --pdf <path-or-slug>` (also `just create-cheatsheet-thumbnails`) renders every page at 150 dpi with `pdf2image`. It resizes them to 600 px wide, saves `page-N.png` next to the PDF, and rewrites `thumbnails:` in `_index.md`. Caveats are listed under Phase 1.10.
- **People:** any name in `people:` gets a taxonomy page at `/people/<slug>/`. A profile in `content/people/<firstname-lastname>/` is optional (D12).
- **Build and deploy:** GitHub Actions builds the site and deploys it to Netlify.
  - The build is the reusable `.github/workflows/build-deploy.yml`, used by `deploy-production.yml` (daily cron) and `deploy-preview.yml`.
  - `netlify.toml` has `ignore = "exit 0"`, so Netlify doesn't build anything itself.
  - All files in a bundle are published, so source files become downloadable.

---

## Design: the `by` field and "By" filter

### Front matter

```yaml
by: posit        # required on every Posit cheat sheet
by: community    # community sheets (set explicitly when migrating)
# no `by` field  → treated as community
```

`by` is a plain page param, not a taxonomy. The validation script (Phase 1.9) fails if `by` has any other value. It also flags a sheet without `by: posit` whose PDF footer says "Posit Software, PBC".

### Item index (`layouts/partials/item-index-entry.html`)

Add the key for cheat sheets only, so mixed listings (topics, tags, people) aren't affected:

```go-html-template
{{ if eq $page.Params.resource_type "cheatsheet" }}
  {{ $by := cond (eq (lower ($page.Params.by | default "")) "posit") "Posit" "Community" }}
  {{ $entry = merge $entry (dict "by" $by) }}
{{ end }}
```

### Filter config (`data/filters.yaml` → `cheatsheet.filters`)

```yaml
    - key: by
      label: By
      values: [Posit, Community]
      default: [Posit]          # new option: pre-selected values
    - key: topics
      …
    - key: languages
      …
```

`filter-controls.html` already renders this as a multi-select dropdown, so no template change is needed.

### JavaScript (`assets/js/search-filter-sort.js`)

1. **Defaults:** read `f.default` into `_filterCfgMap[key].defaults` and initialize `state.filters[key]` from it.
2. **URL:**
   - `_updateURL()` writes `?by=` only when the selection differs from the default.
   - An explicitly empty selection is written as `?by=`, which shows all.
   - `_readURL()` treats a missing param as "use default" and an empty param as an explicit empty set.
3. **Reset:** `reset()` restores the defaults.
4. **Active filters:** `_hasActiveFilters()` compares each set with its default.
5. **Badge:** call `_updateBadge('by')` and `_updateFilterAria('by')` on init. Per D10, the badge shows **"1"** in the default state.
6. **Matching:** no change; `_matchesFilters()` already does `values.includes(active)`.

### No flash of community cards

Add `data-by` to the card wrapper in `resource-type.html`. A CSS rule hides `[data-by="community"]` cards only while the filter is initializing, under a class on the container that the JS removes when it's ready. Without JS, everything stays visible.

### Elsewhere (D11)

Community sheets appear on topic/tag/software/people pages, in feeds, `llms.txt` and search, exactly like Posit sheets. No changes are needed there.

### Overview page copy

Replace the "Cheatsheets are being migrated" callout in `content/resources/cheatsheets.md` with a short explanation of the By filter and a link to `CONTRIBUTING.md`.

---

## Design: people, translations, source files, PDFs

### `people` (authors only)

- **Posit sheets (D3):** everybody who worked on the sheet. The proposed lists are in Appendix A. Name variants are merged by commit email: `mine-cetinkaya-rundel`, `Mine Cetinkaya-Rundel` → `Mine Çetinkaya-Rundel`; `Garrett` → `Garrett Grolemund`; `averiperny`, `Averi P` → `Averi Perny`; `Carson` → `Carson Sievert`; `gregswinehart` → `Greg Swinehart`; `skaltman` → `Sara Altman`; `ryjohnson09` → `Ryan Johnson`; `ryanzomorrodi` → `Ryan Zomorrodi`; `fbriody` → `Frank Briody`.
- **Spellings match existing profiles:** `Rich Iannone` (not Richard) and `Isabella Velásquez`.
- **Community sheets (D5):** the people named in the PDF footer. A commit author is the fallback only when the PDF names no person and that commit author added the file themselves. Organisations and unclear credits are left out, so `people` is empty for `golem`, `nimble`, `imputeTS` and `mosaic`.
- **Spellings for community authors:** `Alexander Coppock` (one name for `Alex` and `Alexander`), `Przemysław Biecek`, `Christophe Regouby`, `Erik Petrovski`, `Bharath Kumar`.
- **Profiles:** none needed (D12). Posit people who will get bare pages: Garrett Grolemund, Averi Perny, Andy Teucher, Curtis Kephart, Ryan Johnson, Andrie de Vries, Gordon Shotwell, Frank Briody, Mara Averick, Marie-Helene Burle, Wouter Overmeire, Ryan Zomorrodi, Elen Le Foll.

### Translations

The existing format is extended. The template keeps accepting the legacy `{Label: file}` form until every sheet is converted, then that branch is removed.

```yaml
translations:
- language: Spanish            # chip label (D15)
  lang: es                     # BCP 47, used for hreflang/lang on the link
  file: data-import_es.pdf
  edition: readxl 1.4.3, googlesheets4 1.1.1   # D16, from the translated PDF's footer
  updated: 2024-05             # D16, footer date, or the date it was added to the old repo
  people: [Jane Doe]           # D7: shown only here, not in page-level `people`
  source: data-import_es.pptx  # optional, stored in Git LFS
```

- **Chip:** shows `Spanish`. The edition and date go next to or under it, e.g. "readxl 1.4.3 · 2024-05". The translators go in a tooltip or second line ("Translated by …").
- **Missing data:** if `updated` comes from the "added" fallback, show it as "added 2018-05". If there's no edition or date, show the label only.
- **People:** translators aren't added to the `people` taxonomy (D7), so `block/author.html` needs no change.
- **Files:** translations stay in the English sheet's bundle with their old file names. Community translations go into the community sheet's bundle.

### Source files

Copy them into the bundle with their original names and list them in front matter:

```yaml
source_files:
- file: data-import.key
  format: Keynote
- file: data-import.pptx
  format: PowerPoint
- url: https://docs.google.com/presentation/d/…   # rgee, sparklyr
  format: Google Slides
```

`term.html` renders one button per entry, e.g. "Source (Keynote)", next to "Download PDF". This replaces the unused `source_url` param. Multi-file LaTeX sources (`base-r`, `base-r_ko`, `collapse`) go into a `source/` subfolder. The `.tex`/`.Rnw`/`.svg` files are plain git, and Hugo ignores the `source/` folder too.

**Git LFS (D6):**

- **Tracking:** add a `.gitattributes`:

  ```gitattributes
  content/resources/cheatsheets/**/*.key  filter=lfs diff=lfs merge=lfs -text
  content/resources/cheatsheets/**/*.pptx filter=lfs diff=lfs merge=lfs -text
  content/resources/cheatsheets/**/*.ai   filter=lfs diff=lfs merge=lfs -text
  ```

  SVG, `.tex` and `.Rnw` sources are small text files and stay in plain git. PDFs and PNGs stay in plain git too: they're compressed and every build needs them.
- **Existing file:** move `polars/polars-cheatsheet.ai` to LFS with `git rm --cached` and re-add it. History isn't rewritten.
- **Build (not needed):** CI keeps its normal checkout, without `lfs: true`. Source files are listed in `ignoreFiles` (`config/_default/hugo.toml`, pattern `resources/cheatsheets/.*\.(key|pptx|ai)$`), so Hugo never reads or publishes them, not even as pointer files.
- **Downloads:** the "Source (…)" buttons link to `https://github.com/posit-dev/open-source-website/raw/main/content/resources/cheatsheets/<slug>/<file>`. GitHub redirects that to the LFS object. The base URL is the site param `cheatsheetSourceBaseURL`. These links only work once the files are on `main`.
- **Contributors:** document `git lfs install` in `CONTRIBUTING.md`. It's only needed for editing or adding source files, not for building the site.

### PDFs

**Compression tool (D9): `scripts/compress-cheatsheet-pdf.py`.** It's a uv script built on `pikepdf` and Pillow, using poppler's `pdfimages -list` to get each image's effective ppi.

What it does:

1. Downsamples raster images above 300 ppi to 300 ppi. Each soft mask (alpha channel) is downsampled along with its image, and ICC colour spaces are kept.
2. Re-encodes images that were JPEG as JPEG (quality ≈ 85) and everything else losslessly. Re-encoding JPEGs losslessly makes screenshot-heavy files larger; the prototype grew `positron`.
3. Saves with object streams and recompressed Flate streams. The structure tree and tags are left untouched.
4. Keeps the result only if it's smaller. It then verifies:
   - the page count is the same
   - the `pdftotext` word count is the same
   - the `Tagged` status is the same
   - the rendered pages differ from the original by less than 2% RMSE

   If any check fails, the original is kept.

Prototype results (tested on old-repo originals; JPEG handling not yet added):

| PDF | Original | pikepdf prototype | Ghostscript `/printer` | Ghostscript `/ebook` |
|---|---|---|---|---|
| ml-tidymodels | 16.0 MB | **0.95 MB**, tagged | 0.57 MB, **untagged** | 0.25 MB, untagged, soft |
| keras | 1.14 MB | **0.45 MB**, tagged | 0.26 MB, untagged | — |
| shinychat | 1.91 MB | **1.22 MB**, tagged | 2.00 MB (larger) | — |
| data-visualization | 1.06 MB | **0.88 MB**, tagged | 0.95 MB, untagged | 0.41 MB, untagged |
| rstudio-ide | 0.73 MB | **0.59 MB**, tagged | 0.45 MB, untagged | 0.38 MB, untagged |

Text layers came through identical in every case. `ml-tidymodels` looked the same as the original on a visual check (≈1% RMSE).

Thumbnails are made from the compressed PDF, so run the thumbnail script after the compression script.

---

## Migration plan and to-do list

Each phase can ship on its own. After Phase 1, the work is per cheat sheet and independent, so PRs stay small.

### Phase 1: Site groundwork and tooling

- [ ] 1.1 Add `by: posit` to all 30 existing cheat sheets.
- [ ] 1.2 `partials/item-index-entry.html`: emit `by` for cheat sheets.
- [ ] 1.3 `data/filters.yaml`: add the `by` filter with `default: [Posit]`.
- [ ] 1.4 `search-filter-sort.js`: support default selections (defaults, URL round-trip including explicit empty, reset, `_hasActiveFilters`, badge "1", aria).
- [ ] 1.5 `resource-type.html`/`item.html`: add `data-by` and the hide-while-initializing rule.
- [ ] 1.6 `term.html`: render extended translation entries (label, edition · date, translators on the cheat sheet page only), keeping the legacy form.
- [ ] 1.7 `term.html`: render `source_files` buttons.
- [ ] 1.8 Git LFS: add `.gitattributes`, the `ignoreFiles` entry, the `cheatsheetSourceBaseURL` param, and a contributor note. Move `polars-cheatsheet.ai` to LFS.
- [ ] 1.9 `scripts/validate-cheatsheets.py` (uv). It checks:
  - the `by` value
  - that referenced files exist (`download_url`, `thumbnails`, `translations[].file`/`source`, `source_files`)
  - unique translation labels
  - `languages` is present
  - `software` values exist in `content/software/`
  - `.key`/`.pptx`/`.ai` files are LFS pointers in git
  - PDFs that were tagged in the old repo are still tagged
- [ ] 1.10 `scripts/compress-cheatsheet-pdf.py` (D9), including JPEG handling.
- [ ] 1.11 A migration script (extend `scripts/import-cheatsheets.py` or add `migrate-cheatsheet.py`) that works from a local clone of `rstudio/cheatsheets`. For one slug it:
  1. copies the English PDF, translations and sources
  2. compresses the PDFs
  3. writes or merges front matter (`by`, `people`, `translations` with `edition`/`updated`/`people`, `source_files`, `software`)
  4. converts `html/<slug>.qmd` to markdown: ```` ```{r} ```` → ```` ```r ````, strip `#|` lines, rewrite `images/` paths and copy the images
  5. runs the thumbnail script

  It matches translations with `^{slug}_[a-z]{2}(_[a-z]{2})?\.pdf$`, which fixes the old prefix bug. Things to handle around `create-cheatsheet-thumbnails.py`:
  - **Multiple PDFs in one directory.** Given a slug, the script uses `<slug>/<slug>.pdf`, falling back to the only PDF in the directory. A bundle with translation PDFs but no `<slug>.pdf` makes it exit with "Multiple PDFs". That happens wherever the PDF name differs from the slug (`Machine Learning Modelling in R.pdf`, `polars-cheatsheet.pdf`, and most D1 renames), so always pass the full path with `--pdf`.
  - **Front matter is rewritten.** The script round-trips the whole front matter through `yaml.dump`, losing comments and changing quoting and wrapping. Run it before writing the final front matter, or have the migration script set `thumbnails` itself and call only the rendering part.
  - **Stale thumbnails.** Extra `page-N.png` files aren't deleted when a PDF gets shorter. Remove `page-*.png` first.
  - **`image:` isn't set.** The migration script must set `image: page-1.png` itself, unless a logo is used.
  - **English PDF only.** Translations get no thumbnails, which is fine with the current template.
  - **Dependencies.** Needs poppler (`pdftoppm`); output is 150 dpi resized to 600 px wide, matching the existing 600 × 463 thumbnails.
- [ ] 1.12 Run `yarn build-tailwind` if new classes are added. Check the overview page:
  - Posit-only by default, with badge "1"
  - turning on Community shows all
  - deselecting both shows all
  - `?by=Community`, `?by=` and reset all behave
  - By combines correctly with Languages
  - no flash of community cards
  - source files are absent from `public/`, and the buttons point at GitHub

### Phase 2: Complete the 30 existing cheat sheets

For each sheet:

- refresh and compress the PDF, then regenerate thumbnails
- copy sources (LFS)
- port the markdown, or write a summary (D8)
- convert `translations` to the new format with translators, edition and date, then add missing translations and their sources
- set `people` (Appendix A)
- clean leftover `#|` lines from existing markdown

| Slug | PDF | Markdown | Sources | Translation fixes |
|---|---|---|---|---|
| data-import | [ ] refresh | ✓ (clean `#|`) | [ ] key, pptx | [ ] add `el`; [ ] 5 sources |
| data-transformation | [ ] refresh | ✓ | [ ] key, pptx | [ ] 7 sources |
| data-visualization | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 2 sources |
| factors | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 2 sources |
| great-tables | [ ] refresh | [ ] summary | [ ] key | — |
| gt | [ ] refresh | [ ] summary | [ ] key | [ ] **remove `gtsummary_vi.pdf`** (moves to `gtsummary`) |
| keras | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 3 sources |
| lubridate | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 4 sources |
| ml-create-models | [ ] compress (same file) | ✓ | [ ] key | — |
| ml-measure-performance | [ ] compress (same file) | ✓ | [ ] key | — |
| ml-preprocessing-data | [ ] compress (same file) | ✓ | [ ] key | — |
| ml-tidymodels | [ ] **replace the untagged Ghostscript copy** with the compressed original | ✓ | [ ] key (38 MB) | — |
| nlp-with-llms | [ ] refresh | [ ] port | [ ] key | — |
| package-development | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 1 source |
| plotnine | [ ] compress (same file) | [ ] port | [ ] ai | — |
| plumber | [ ] refresh | [ ] port | [ ] key, pptx | [ ] **add `es`** + source |
| polars | [ ] re-export a tagged PDF from `polars-cheatsheet.ai` (needs Illustrator), then compress with the new script | ✓ | [ ] move `.ai` to LFS | — |
| posit-team | [ ] refresh | [ ] port | [ ] pptx | — |
| positron | [ ] refresh | [ ] summary | [ ] key | — |
| purrr | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 6 sources |
| quarto | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 1 source |
| reticulate | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 1 source |
| rmarkdown | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 1 source |
| rstudio-ide | [ ] refresh | [ ] port | [ ] key (70 MB), pptx (68 MB) | [ ] 2 sources |
| shiny | [ ] compress (same file) | [ ] port | [ ] key, pptx | [ ] **remove `shiny-python_es.pdf`**; [ ] 2 sources |
| shiny-python | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 1 source |
| shinychat | [ ] refresh | [ ] summary | [ ] key | — |
| sparklyr | [ ] refresh | [ ] port | [ ] pptx + Google Slides link | [ ] 4 sources; [ ] distinct `zh_cn`/`zh_tw` labels |
| strings | [ ] refresh | [ ] port | [ ] key, pptx | [ ] 3 sources |
| tidyr | [ ] refresh | [ ] port | [ ] key, pptx | [ ] **add `es`**; [ ] 3 sources |

Also fill front matter gaps:

- add `languages` on `posit-team`, `positron`, `quarto`
- add `R` to `nlp-with-llms` ("in R & Python")
- replace the auto-generated descriptions ("Quick reference guide for …")

### Phase 3: Migrate the remaining Posit cheat sheets

- [ ] `renv`: markdown from `html/renv.qmd`, `keynotes/renv.key`, `software: [renv]`, `languages: [R]`.
- [ ] `tidyeval`: summary (D8); key + pptx; `software: [rlang]`; `languages: [R]`; 1 translation (es).
- [ ] `caret`: summary; key + pptx; no `software` slug exists; `languages: [R]`; 5 translations (es, fr, ko, pt, tr).

### Phase 4: Migrate community cheat sheets

For each sheet (Appendix B):

- create the bundle under the D1 slug and copy the PDF (old name)
- compress the PDF and generate thumbnails
- set `by: community`, `people`, `languages`, `software` (D13) and a real `description`
- write the summary body (D8)
- copy sources (LFS) and translations

Batches of about 10 per PR:

- [ ] 4a. With translations: `base-r` (9), `metrica` (3), `data-table` (2), `git-github` (2), `regular-expressions` (2), `syntax` (2), `gtsummary` (1, moved from `gt`), `quanteda` (1), `survminer` (1), `torch` (1)
- [ ] 4b. With sources: `admiral`, `arrow`, `dromics`, `h2o`, `imputets`, `jfa`, `labelled`, `overviewr`, `profile-optimise-python`, `r-best-practice`, `sas-r`, `sas-vs-r-in-pharma`, `squeakr`, `srvyr`, `stata2r`, `time-series`, `vivainsights-r`, `vivainsights-py`, `quincunx` (svg), `sf` (svg), `collapse` (Rnw), `rgee` (Google Slides)
- [ ] 4c. PDF only: `bayesplot`, `bcea`, `cartography`, `declaredesign`, `distr6`, `estimatr`, `eurostat`, `gganimate`, `golem`, `gwasrapidd`, `how-big-is-your-graph`, `leaflet`, `machine-learning-modelling-in-r`, `mapsf`, `mlr`, `mosaic`, `nardl`, `nimble`, `oscr`, `packagefinder`, `parallel-computation`, `randomizr`, `rphylopic`, `samplingstrata`, `sjmisc`, `slackr`, `teachr`, `tsbox`, `vegan`, `vtree`, `xplain`
- [ ] 4d. Spanish originals (if R2 confirms): `introduccion-a-r`, `estadistica-descriptiva-con-r`

### Phase 5: Wrap-up

- [ ] Re-sync against the latest old-repo commit before it's archived (D14): pick up new PDF updates or translations.
- [ ] Replace the "being migrated" callout with the By-filter/contribute copy.
- [ ] Run `scripts/validate-cheatsheets.py` and the link check (`scripts/lychee-errors.py`) over `/resources/cheatsheets/`.

---

## Follow-up decisions

| # | Question | Decision | Applied |
|---|---|---|---|
| R1 | "David" (`davidrsch`) | He's **David Díaz Rodríguez** | Credited as translator on all 18 Spanish translations he worked on (sole translator on 7). Under D3 he's also added to `people` on the 18 Posit sheets whose PowerPoint versions he made. |
| R2 | Spanish originals | Don't drop them | `introduccion-a-r` and `estadistica-descriptiva-con-r` are migrated as community sheets (Phase 4d). |
| R3 | Committer fallback and contact-derived credits | Sounds good | As proposed: Stefan Bundfuss, Mauricio Vargas, Aurélie Siberchicot, Adi Sarid, Anh Hoang Duc, Joachim Zuckarelli. |
| — | LFS in the build | The build doesn't need the LFS files | No CI changes. Hugo ignores the source files, and the buttons link to GitHub (D6). |

---

## Appendix A: Posit cheat sheets inventory

Legend:
- **Where:** B = both sites, O = old site only, N = new site only.
- **Status** (new site): ✗ not started · PDF · PDF+MD · ✓ complete.
- **PDF:** "same" = byte-identical to the old repo; otherwise the "Updated" footer of new → old.
- **`people` (D3):** every identifiable contributor, most commits first, combined with the people already on the new site (marked †). Unclear handles excluded (D5) are listed under "Notes". David Díaz Rodríguez is included per R1.
- **Sources:** the old-repo files to copy. None are in the new site yet, except `polars`.
- **Translations:** old-site translations, with ✗ marking those missing on the new site.

| Slug | Title | Where | Status | PDF (new → old) | `people` (D3) | Sources | Translations | `software` | Notes |
|---|---|---|---|---|---|---|---|---|---|
| caret | caret Package | O | ✗ | n/a | Garrett Grolemund, Mine Çetinkaya-Rundel, Max Kuhn | key, pptx | es fr ko pt tr (all ✗) | — (no slug) | was on Contributed page (D2) |
| data-import | Data import with the tidyverse | B | PDF+MD | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel†, Averi Perny, Andy Teucher, Curtis Kephart, Hadley Wickham†, David Díaz Rodríguez | key, pptx | bn es fa pt_br ru tr uk uz, el ✗ | readr, readxl, haven, googlesheets4 | excluded: Carter (inkcartrich) |
| data-transformation | Data transformation with dplyr | B | PDF+MD | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel†, Averi Perny, Andy Teucher, Curtis Kephart, David Díaz Rodríguez | key, pptx | de es pt_br ru tr uk uz zh_cn | dplyr |  |
| data-visualization | Data visualization with ggplot2 | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel, Garrett Grolemund, Averi Perny, Curtis Kephart, Andy Teucher, Thomas Lin Pedersen, David Díaz Rodríguez | key, pptx | de el es fr ja nl pt tr vi zh | ggplot2 |  |
| factors | Factors with forcats | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel, Averi Perny, Andy Teucher, Curtis Kephart, Garrett Grolemund, David Díaz Rodríguez | key, pptx | es ja pt_br | forcats |  |
| great-tables | Great Tables | B | PDF | 2025-07 → 2026-08 | Mine Çetinkaya-Rundel, Rich Iannone | key | — | great-tables | summary (D8) |
| gt | gt | B | PDF | 2025-07 → 2026-08 | Mine Çetinkaya-Rundel, Rich Iannone | key | — (remove `gtsummary_vi`) | gt | summary (D8) |
| keras | Deep Learning with Keras | B | PDF | 2025-07 → 2026-07 | Edgar Ruiz, Mine Çetinkaya-Rundel, Garrett Grolemund, Andy Teucher, Tomasz Kalinowski, Andrie de Vries, David Díaz Rodríguez | key, pptx | es ja zh_cn | keras3 |  |
| lubridate | Dates and times with lubridate | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Andy Teucher, Averi Perny, Curtis Kephart, Mara Averick, Wouter Overmeire, David Díaz Rodríguez | key, pptx | es pt_br ru uk vi | lubridate |  |
| ml-create-models | Create models with parsnip | B | PDF+MD | same | Edgar Ruiz†, Mine Çetinkaya-Rundel | key | — | parsnip | |
| ml-measure-performance | Measure model performance with yardstick | B | PDF+MD | same | Edgar Ruiz† | key | — | yardstick | not on old index (D17) |
| ml-preprocessing-data | Preprocessing data with recipes | B | PDF+MD | same | Edgar Ruiz† | key | — | recipes | |
| ml-tidymodels | Machine learning with tidymodels | B | PDF+MD | 2026-07 = 2026-07 (new copy is Ghostscript-compressed and untagged) | Edgar Ruiz†, Mine Çetinkaya-Rundel | key (38 MB) | — | tidymodels | |
| nlp-with-llms | Natural Language Processing using LLMs in R & Python | B | PDF | 2025-07 → 2026-07 | Edgar Ruiz, Mine Çetinkaya-Rundel | key | — | mall | add `R` to languages |
| package-development | Package Development | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel, Garrett Grolemund, Andy Teucher, Curtis Kephart, Averi Perny, David Díaz Rodríguez | key, pptx | de es it ko nl vi | devtools, usethis |  |
| plotnine | Data visualization with Plotnine | B | PDF | same | Mine Çetinkaya-Rundel, Jeroen Janssens†, Hassan Kibirige† | ai | — | plotnine | |
| plumber | REST APIs with plumber | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel, James Blair, Andy Teucher, Curtis Kephart, Averi Perny, David Díaz Rodríguez | key, pptx | es ✗ | plumber |  |
| polars | Python Polars: The Definitive Cheatsheet | N | ✓ | n/a (Ghostscript-compressed, untagged) | Jeroen Janssens†, Thijs Nieuwdorp† | ai (in bundle, move to LFS) | — | great-tables, plotnine | D2 |
| posit-team | Posit Team | B | PDF | 2024-09 → 2026-08 | Mine Çetinkaya-Rundel, Ryan Johnson | pptx | — | — (no slug) | add `languages` |
| positron | Positron | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel | key | — | positron | summary (D8); add `languages` |
| purrr | Apply functions with purrr | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny, Andy Teucher, Curtis Kephart, Hadley Wickham, Marie-Helene Burle, David Díaz Rodríguez | key, pptx | es ko pt_br ru uk vi | purrr | excluded: MikeJohnPage |
| quarto | Publish and Share with Quarto | B | PDF | 2026-06 = 2026-06 (bytes differ) | Charlotte Wickham, Mine Çetinkaya-Rundel, Isabella Velásquez, David Díaz Rodríguez | key, pptx | es | quarto | add `languages` |
| renv | Reproducible R Environments with renv | O | ✗ | n/a → 2026-08 | Mine Çetinkaya-Rundel, Kevin Ushey | key | — | renv | |
| reticulate | Use Python with R with reticulate | B | PDF | 2025-07 → 2026-07 | Edgar Ruiz, Mine Çetinkaya-Rundel, Andy Teucher, Tomasz Kalinowski, Averi Perny, Garrett Grolemund, Curtis Kephart, David Díaz Rodríguez | key, pptx | es | reticulate |  |
| rmarkdown | rmarkdown | B | PDF | 2025-07 → 2026-08 | Mine Çetinkaya-Rundel, Averi Perny, Garrett Grolemund, Andy Teucher, Curtis Kephart, David Díaz Rodríguez | key, pptx | de es it ja ko nl tr vi | rmarkdown |  |
| rstudio-ide | RStudio IDE | B | PDF | 2025-07 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny, Curtis Kephart, Andy Teucher, David Díaz Rodríguez | key (70 MB), pptx (68 MB) | el es fr it ja pt vi | rstudio |  |
| shiny | Shiny for R | B | PDF | same | Mine Çetinkaya-Rundel, Garrett Grolemund, Andy Teucher, Carson Sievert, Averi Perny, Greg Swinehart, Isabella Velásquez, Curtis Kephart, Frank Briody, Edgar Ruiz, David Díaz Rodríguez | key, pptx | de es fr tr vi (remove `shiny-python_es`) | shiny-r |  |
| shiny-python | Shiny for Python | B | PDF | 2026-06 = 2026-06 (bytes differ) | Mine Çetinkaya-Rundel, Garrett Grolemund, Carson Sievert, Greg Swinehart, Isabella Velásquez, Gordon Shotwell, Karan Gathani, David Díaz Rodríguez | key, pptx | es | shiny-python |  |
| shinychat | AI chatbots with shinychat | B | PDF | 2025-07 → 2026-08 | Mine Çetinkaya-Rundel, Sara Altman, Carson Sievert | key | — | shinychat | summary (D8) |
| sparklyr | Data science in Spark with sparklyr | B | PDF | 2025-07 → 2026-08 | Mine Çetinkaya-Rundel, Garrett Grolemund, Edgar Ruiz, Andy Teucher, Curtis Kephart, David Díaz Rodríguez | pptx, Google Slides link | de es ja zh_cn zh_tw | sparklyr |  |
| strings | String manipulation with stringr | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny, Andy Teucher, Ryan Zomorrodi, Curtis Kephart, Elen Le Foll, David Díaz Rodríguez | key, pptx | es pt_br vi | stringr | |
| tidyeval | Tidy evaluation with rlang | O | ✗ | n/a | Garrett Grolemund, Mine Çetinkaya-Rundel | key, pptx | es ✗ | rlang | was on Contributed page (D2); summary (D8) |
| tidyr | Data tidying with tidyr | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel, Garrett Grolemund, Averi Perny, Andy Teucher, Curtis Kephart, David Díaz Rodríguez | key, pptx | pt_br zh_cn, es ✗ | tidyr |  |

---

## Appendix B: Community cheat sheets inventory

Every row is old-site only, not started, and not marked deprecated.

- **`people` source:** **P** = named in the PDF · **C** = commit fallback (R3) · — = none usable (D5).
- **`software` (D13):** only existing `content/software/` slugs. — = no matching slug.
- **Markdown:** a summary for all of them (D8).

| Old file | New slug (D1) | Title | `people` | Src | Sources | Translations | `languages` | `software` |
|---|---|---|---|---|---|---|---|---|
| admiral | admiral | admiral | Stefan Bundfuss | C | pptx | — | R | — |
| arrow | arrow | Arrow for R | Mauricio Vargas | C | pptx | — | R | dplyr |
| base-r | base-r | Base R | Mhairi McNeill | P | LaTeX (`latex/base-r/`) | de el es ja ko pt_br tr vi zh | R | — |
| bayesplot | bayesplot | bayesplot | Edward A. Roualdes | P | — | — | R | — |
| bcea | bcea | BCEA | Gianluca Baio | P | — | — | R | — |
| cartography | cartography | Thematic maps with cartography | Timothée Giraud | P | — | — | R | — |
| collapse | collapse | Advanced and Fast Data Transformation with collapse | Sebastian Krantz | P | LaTeX/Rnw (`latex/collapse/`) | — | R | — |
| datatable | data-table | data.table | Erik Petrovski, Mara Destefanis, Tyson Barrett | P | pptx | fr pt_br | R | — |
| declaredesign | declaredesign | DeclareDesign | Graeme Blair, Jasper Cooper, Alexander Coppock, Macartan Humphreys, Neal Fultz | P | — | — | R | — |
| distr6 | distr6 | distr6 | Raphael Sonabend | P | — | — | R | — |
| DRomics | dromics | DRomics | Aurélie Siberchicot | C | pptx | — | R | — |
| estimatr | estimatr | estimatr | Graeme Blair, Jasper Cooper, Alexander Coppock, Macartan Humphreys, Luke Sonnet | P | — | — | R | — |
| eurostat | eurostat | Access Eurostat data with eurostat | Przemysław Biecek, Markus Kainu | P | — | — | R | — |
| gganimate | gganimate | gganimate | Karl Hailperin | P | — | — | R | — |
| git-github | git-github | Git & GitHub | Mouna Belaid | P | pptx | es vi | — | — |
| golem | golem | golem | — (ThinkR, org) | — | — | — | R | — |
| gtsummary | gtsummary | gtsummary | Esther Drill | P | pptx | vi | R | — |
| gwasrapidd | gwasrapidd | GWAS Catalog access with gwasrapidd | Ramiro Magno | P | — | — | R | — |
| h2o | h2o | h2o | Juan Telleria Ruiz de Aguirre | P | pptx | — | R | — |
| how-big-is-your-graph | how-big-is-your-graph | How big is your graph? | Steve Simon | P | — | — | R | — |
| imputeTS | imputets | imputeTS | — (unclear) | — | pptx | — | R | — |
| jfa | jfa | jfa | Koen Derks | P | pptx | — | R | — |
| labelled | labelled | labelled | Joseph Larmarange | P | pptx | — | R | haven |
| leaflet | leaflet | Leaflet | Kejia Shi | P | — | — | R | leaflet |
| Machine Learning Modelling in R | machine-learning-modelling-in-r | Machine Learning Modelling in R | Arnaud Amsellem | P | — | — | R | — |
| mapsf | mapsf | mapsf | Ronan Ysebaert | P | — | — | R | — |
| metrica | metrica | metrica | Carlos Hernandez, Adrian A. Correndo | P | pptx | es pt_br ru | R | — |
| mlr | mlr | Machine Learning with mlr | Aaron Cooley | P | — | — | R | — |
| mosaic | mosaic | mosaic | — (unclear) | — | — | — | R | — |
| nardl | nardl | nardl | Taha Zaghdoudi | P | — | — | R | — |
| nimble | nimble | nimble | — (NIMBLE Development Team, org) | — | — | — | R | — |
| oSCR | oscr | oSCR | Gabriela Palomo-Munoz | P | — | — | R | — |
| overviewR | overviewr | overviewR | Cosima Meyer, Dennis Hammerschmidt | P | key | — | R | — |
| packagefinder | packagefinder | Searching CRAN with packagefinder | Joachim Zuckarelli (R3) | P | — | — | R | — |
| parallel_computation | parallel-computation | Parallel computation | Ardalan Mirshani | P | — | — | R | — |
| profile_optimise_py | profile-optimise-python | Profiling and Optimising in Python | Saranjeet Kaur Bhogal, Jost Migenda | P | pptx | — | Python | — |
| quanteda | quanteda | quanteda | Stefan Müller, Kenneth Benoit | P | pptx | fr | R | — |
| quincunx | quincunx | quincunx | Ramiro Magno | P | Inkscape SVG ×2 | — | R | — |
| randomizr | randomizr | randomizr | Alexander Coppock | P | — | — | R | — |
| R-best-practice | r-best-practice | R Best Practice | Jacob Scott | P | key | — | R | usethis, reprex, renv |
| regex | regular-expressions | Regular Expressions | Ian Kopacka | P | pptx | fr tr | R | stringr |
| rgee | rgee | rgee | Antony Barja, Cesar Aybar | P | Google Slides link | — | R | — |
| rphylopic | rphylopic | rphylopic | Gabriela Palomo-Munoz | P | — | — | R | — |
| SamplingStrata | samplingstrata | SamplingStrata | Giulio Barcaroli | P | — | — | R | — |
| sas-r | sas-r | SAS <-> R | Brendan O'Dowd | P | pptx | — | R | tidyverse |
| SASvsRinPharma | sas-vs-r-in-pharma | SAS vs. R in Pharma | Bharath Kumar | P | pptx | — | R | — |
| sf | sf | sf | Ryan Garnett | P | Inkscape SVG ×2 | — | R | — |
| sjmisc | sjmisc | sjmisc | Daniel Lüdecke | P | — | — | R | — |
| slackr | slackr | slackr | Daniel M. Villarreal | P | — | — | R | — |
| srvyr | srvyr | srvyr | Greg Freedman Ellis, Ben Schneider | P | pptx | — | R | — |
| stata2r | stata2r | stata2r | Anthony Nguyen | P | pptx | — | R | — |
| survminer | survminer | survminer | Przemysław Biecek | P | — | es | R | — |
| syntax | syntax | R syntax comparison | Amelia McNamara | P | key | es ko | R | ggplot2, dplyr |
| SqueakR | squeakr | SqueakR | Simon Ogundare | P | key | — | R | — |
| teachR | teachr | teachR | Adi Sarid (R3) | C | — | — | R | — |
| time-series | time-series | time-series | Yunjun Xia, Shuyu Huang | P | key | — | R | — |
| torch | torch | torch | Christophe Regouby | P | key | fr | R | torch |
| tsbox | tsbox | tsbox | Christoph Sax | P | — | — | R | — |
| vegan | vegan | vegan | Bruna Luiza Silva | P | — | — | R | — |
| vivainsights_r | vivainsights-r | vivainsights (R) | Martin Chan | P | pptx (shared `vivainsights-r-py.pptx`) | — | R | — |
| vivainsights_py | vivainsights-py | vivainsights (Python) | Martin Chan | P | pptx (shared) | — | Python | — |
| vtree | vtree | vtree | Nick Barrowman | P | — | — | R | — |
| xplain | xplain | xplain | Joachim Zuckarelli (R3) | P | — | — | R | — |
| introduccion-a-r (Spanish) | introduccion-a-r | Introducción a R | Rosana Ferrero | P | — | — | R | — |
| estadistica-descriptiva-con-R (Spanish) | estadistica-descriptiva-con-r | Estadística descriptiva con R | Rosana Ferrero | P | — | — | R | — |

For each community slug, check while migrating that it doesn't clash with a Posit sheet's slug. None do today.

---

## Appendix C: Translations inventory

115 translations: 91 of Posit sheets and 24 of community sheets. The `data-wrangling` translations are excluded (D4), and the 2 Spanish originals are in Appendix B.

- **Translator(s):** people only (D5). **P** = PDF credit · **C** = commit history · — = no usable credit (27 translations).
- **Src:** translation source file in the old repo (goes into LFS).
- **Edition · date (D16):**
  - The edition is the package version(s) from the translated PDF's footer.
  - The date is the footer date, normalized to `YYYY-MM`.
  - If the footer has no date, it's the month the translation was added to the old repo, shown as "added YYYY-MM".
  - The script extracted these automatically; spot-check them while migrating.
- **New:** whether the file is already on the new site.

### Translations of Posit cheat sheets

| Sheet | Language | File | Translator(s) | Src | Edition · date | New |
|---|---|---|---|---|---|---|
| caret | French | caret_fr.pdf | Ahmadou Dicko (C) | pptx | 2017-09 | **✗** |
| caret | Korean | caret_ko.pdf | Kwangchun Lee (P) | pptx | added 2017-09 | **✗** |
| caret | Portuguese | caret_pt.pdf | Karen da Silva Lopes (P) | pptx | 2017-09 | **✗** |
| caret | Spanish | caret_es.pdf | — | key | 2017-09 | **✗** |
| caret | Turkish | caret_tr.pdf | İlkim Ecem Emre (P) | — | 2017-09 | **✗** |
| data-import | Bengali | data-import_bn.pdf | Saif Kabir Asif (C) | pptx | added 2021-09 | ✓ |
| data-import | Greek | data-import_el.pdf | Nikolaos Koupidis (P) | — | readr 2.0.0, readxl 1.3.1, googlesheets4 1.0.0 · 2021-08 | **✗** |
| data-import | Persian | data-import_fa.pdf | Vahid Faraji Jobehdar, Reza Mazloomi (P) | — | readr 1.1.0, tibble 1.2.12, tidyr 0.6.0 · 2019-08 | ✓ |
| data-import | Portuguese (Brazil) | data-import_pt_br.pdf | Eric Scopinho (P) | pptx | readr 2.0.0, readxl 1.3.1, googlesheets4 1.0.0 · 2021-08 | ✓ |
| data-import | Russian | data-import_ru.pdf | — | key | readr 1.1.0, tibble 1.2.12, tidyr 0.6.0 · 2017-01 | ✓ |
| data-import | Spanish | data-import_es.pdf | David Díaz Rodríguez (C) | pptx | readxl 1.4.3, googlesheets4 1.1.1 · 2024-05 | ✓ |
| data-import | Turkish | data-import_tr.pdf | Metin Yazici (P) | — | readr 1.1.0, tibble 1.2.12, tidyr 0.6.0 · 2017-01 | ✓ |
| data-import | Ukrainian | data-import_uk.pdf | — | key | readr 1.1.0, tibble 1.2.12, tidyr 0.6.0 · 2017-01 | ✓ |
| data-import | Uzbek | data-import_uz.pdf | — | — | added 2017-08 | ✓ |
| data-transformation | Chinese (Simplified) | data-transformation_zh_cn.pdf | Aicen Yu 于艾岑 (P) | key | dplyr 0.7.0, tibble 1.2.0 · added 2017-01 | ✓ |
| data-transformation | German | data-transformation_de.pdf | Lucia Gjeltema (P) | pptx | added 2017-09 | ✓ |
| data-transformation | Portuguese (Brazil) | data-transformation_pt_br.pdf | Eric Scopinho (P) | pptx | dplyr 1.0.7 · 2021-07 | ✓ |
| data-transformation | Russian | data-transformation_ru.pdf | — | key | dplyr 0.5.0, tibble 1.2.0 · added 2017-01 | ✓ |
| data-transformation | Spanish | data-transformation_es.pdf | Frans van Dunné (C), David Díaz Rodríguez (C) | key, pptx | dplyr 1.1.4 · 2024-05 | ✓ |
| data-transformation | Turkish | data-transformation_tr.pdf | — | — | dplyr 0.5.0, tibble 1.2.0 · 2017-01 | ✓ |
| data-transformation | Ukrainian | data-transformation_uk.pdf | — | key | dplyr 0.5.0, tibble 1.2.0 · added 2017-01 | ✓ |
| data-transformation | Uzbek | data-transformation_uz.pdf | — | — | added 2017-08 | ✓ |
| data-visualization | Chinese (Simplified) | data-visualization_zh.pdf | Guang-Teng Meng (P) | pptx | ggplot2 3.3.5 · 2021-08 | ✓ |
| data-visualization | Dutch | data-visualization_nl.pdf | — | — | ggplot2 0.9.3.1, ggplot2 1.0.0 · 2015-04 | ✓ |
| data-visualization | French | data-visualization_fr.pdf | Vincent Guyader (P) | — | ggplot2 1.0.0 · 2015-04 | ✓ |
| data-visualization | German | data-visualization_de.pdf | Lucia Gjeltema (P) | — | added 2018-05 | ✓ |
| data-visualization | Greek | data-visualization_el.pdf | Nikolaos Koupidis (P) | — | ggplot2 3.3.5 · 2021-08 | ✓ |
| data-visualization | Japanese | data-visualization_ja.pdf | — | — | ggplot2 2.0.0 · 2015-12 | ✓ |
| data-visualization | Portuguese | data-visualization_pt.pdf | Augusto Queiroz de Macedo (P) | — | ggplot2 0.9.3.1, ggplot2 2.0.0 · 2016-03 | ✓ |
| data-visualization | Spanish | data-visualization_es.pdf | Carolina Mengoni (C), David Díaz Rodríguez (C) | pptx | ggplot2 3.5.1 · 2024-05 | ✓ |
| data-visualization | Turkish | data-visualization_tr.pdf | — | — | ggplot2 2.1.0 · 2016-11 | ✓ |
| data-visualization | Vietnamese | data-visualization_vi.pdf | — | — | ggplot2 2.0.0 · 2015-12 | ✓ |
| factors | Japanese | factors_ja.pdf | Taiyo Nakashima (P) | — | forcats 0.3.0 · 2019-02 | ✓ |
| factors | Portuguese (Brazil) | factors_pt_br.pdf | Eric Scopinho (P) | pptx | forcats 0.5.1 · added 2022-09 | ✓ |
| factors | Spanish | factors_es.pdf | Laura Acion (C), David Díaz Rodríguez (C) | pptx | forcats 1.0.0 · 2024-05 | ✓ |
| keras | Chinese (Simplified) | keras_zh_cn.pdf | — | key | keras 2.1.2 · 2017-12 | ✓ |
| keras | Japanese | keras_ja.pdf | Masato Takahashi (P) | — | keras 2.1.2 · 2017-12 | ✓ |
| keras | Spanish | keras_es.pdf | David Díaz Rodríguez (C) | key, pptx | keras3 1.0.0 · 2024-06 | ✓ |
| lubridate | Portuguese (Brazil) | lubridate_pt_br.pdf | Eric Scopinho (P) | pptx | lubridate 1.7.10 · 2021-07 | ✓ |
| lubridate | Russian | lubridate_ru.pdf | — | key | lubridate 1.6.0 · 2017-12 | ✓ |
| lubridate | Spanish | lubridate_es.pdf | Yanina Bellini Saibene (C), David Díaz Rodríguez (C) | pptx | lubridate 1.9.3 · 2024-05 | ✓ |
| lubridate | Ukrainian | lubridate_uk.pdf | — | key | lubridate 1.6.0 · 2017-12 | ✓ |
| lubridate | Vietnamese | lubridate_vi.pdf | Anh Hoang Duc (C) | — | lubridate 1.6.0 · 2017-12 | ✓ |
| package-development | Dutch | package-development_nl.pdf | — | — | devtools 1.6.1 · 2015-01 | ✓ |
| package-development | German | package-development_de.pdf | Lucia Gjeltema (P) | — | added 2018-05 | ✓ |
| package-development | Italian | package-development_it.pdf | Angelo Salatino (P) | — | devtools 1.6.1 · 2015-01 | ✓ |
| package-development | Korean | package-development_ko.pdf | Kwangchun Lee 이광춘 (P) | — | added 2018-05 | ✓ |
| package-development | Spanish | package-development_es.pdf | Paola Corrales (C), David Díaz Rodríguez (C) | pptx | devtools 2.4.5, usethis 2.2.2, testthat 3.2.1.1 · 2024-05 | ✓ |
| package-development | Vietnamese | package-development_vi.pdf | — | — | added 2018-05 | ✓ |
| plumber | Spanish | plumber_es.pdf | David Díaz Rodríguez (C) | pptx | plumber 1.2.2 · 2024-05 | **✗** |
| purrr | Korean | purrr_ko.pdf | Kwangchun Lee (P) | key | purrr 0.2.3 · 2017-10 | ✓ |
| purrr | Portuguese (Brazil) | purrr_pt_br.pdf | Eric Scopinho (P) | pptx | purrr 0.3.4 · 2021-07 | ✓ |
| purrr | Russian | purrr_ru.pdf | — | key | purrr 0.2.3 · 2017-09 | ✓ |
| purrr | Spanish | purrr_es.pdf | David Díaz Rodríguez (C) | key, pptx | purrr 1.0.2 · 2024-05 | ✓ |
| purrr | Ukrainian | purrr_uk.pdf | — | key | purrr 0.2.3 · 2017-09 | ✓ |
| purrr | Vietnamese | purrr_vi.pdf | Anh Hoang Duc (C) | — | purrr 0.2.3 · 2017-09 | ✓ |
| quarto | Spanish | quarto_es.pdf | David Díaz Rodríguez (C) | pptx | Quarto 1.4 · 2024-05 | ✓ |
| reticulate | Spanish | reticulate_es.pdf | Vanesa Maribel (C), David Díaz Rodríguez (C) | pptx | reticulate 1.37 · 2024-06 | ✓ |
| rmarkdown | Dutch | rmarkdown_nl.pdf | — | — | rmarkdown 0.2.50 · 2014-08 | ✓ |
| rmarkdown | German | rmarkdown_de.pdf | Lucia Gjeltema (P) | — | 2016-02 | ✓ |
| rmarkdown | Italian | rmarkdown_it.pdf | Angelo Salatino (P) | — | 2016-02 | ✓ |
| rmarkdown | Japanese | rmarkdown_ja.pdf | Masato Takahashi (P) | — | rmarkdown 1.6 · 2016-02 | ✓ |
| rmarkdown | Korean | rmarkdown_ko.pdf | Kwangchun Lee (P) | — | added 2018-05 | ✓ |
| rmarkdown | Spanish | rmarkdown_es.pdf | Jesica Formoso (C), David Díaz Rodríguez (C) | pptx | rmarkdown 2.27 · 2024-05 | ✓ |
| rmarkdown | Turkish | rmarkdown_tr.pdf | Metin Yazici (P) | — | rmarkdown 1.6 · 2016-02 | ✓ |
| rmarkdown | Vietnamese | rmarkdown_vi.pdf | — | — | added 2018-05 | ✓ |
| rstudio-ide | French | rstudio-ide_fr.pdf | Diane Beldame (P) | — | added 2017-01 | ✓ |
| rstudio-ide | Greek | rstudio-ide_el.pdf | Kleanthis Koupidis (P) | — | 2017-09 | ✓ |
| rstudio-ide | Italian | rstudio-ide_it.pdf | Angelo Salatino (P) | — | 2016-01 | ✓ |
| rstudio-ide | Japanese | rstudio-ide_ja.pdf | Masato Takahashi (P) | — | 2017-09 | ✓ |
| rstudio-ide | Portuguese | rstudio-ide_pt.pdf | Augusto Queiroz de Macedo (P) | — | 2016-03 | ✓ |
| rstudio-ide | Spanish | rstudio-ide_es.pdf | Monica Alonso (C), David Díaz Rodríguez (C) | pptx | 2024-05 | ✓ |
| rstudio-ide | Vietnamese | rstudio-ide_vi.pdf | Le-Huynh Truc-Ly (C) | pptx | Awesome 5.15.3 · 2021-07 | ✓ |
| shiny | French | shiny_fr.pdf | Asma Balti, Vincent Guyader (P) | — | Shiny 0.10.0 · 2014-06 | ✓ |
| shiny | German | shiny_de.pdf | Lucia Gjeltema (P) | — | shiny 0.12.0 · 2015-06 | ✓ |
| shiny | Spanish | shiny_es.pdf | Florencia D'Andrea (C), David Díaz Rodríguez (C) | key, pptx | shiny 1.8.1.1 · 2024-05 | ✓ |
| shiny | Turkish | shiny_tr.pdf | Metin Yazici (P) | — | shiny 0.12.0 · 2016-01 | ✓ |
| shiny | Vietnamese | shiny_vi.pdf | — | — | shiny 0.12.0 · 2015-06 | ✓ |
| shiny-python | Spanish | shiny-python_es.pdf | David Díaz Rodríguez (C) | pptx | shiny 0.10.2 · 2024-05 | ✓ |
| sparklyr | Chinese (Simplified) | sparklyr_zh_cn.pdf | Ke Zhang 张克 (P) | key | added 2017-01 | ✓ |
| sparklyr | Chinese (Traditional) | sparklyr_zh_tw.pdf | Ke Zhang 張克 (P) | key | added 2017-01 | ✓ |
| sparklyr | German | sparklyr_de.pdf | Ke Zhang (P) | key | added 2017-01 | ✓ |
| sparklyr | Japanese | sparklyr_ja.pdf | Masato Takahashi (P) | — | sparklyr 0.5 · 2016-12 | ✓ |
| sparklyr | Spanish | sparklyr_es.pdf | Daniela Prina (C), David Díaz Rodríguez (C) | pptx | sparklyr 1.8.6 · 2024-05 | ✓ |
| strings | Portuguese (Brazil) | strings_pt_br.pdf | Eric Scopinho (P) | pptx | stringr 1.4.0 · 2021-08 | ✓ |
| strings | Spanish | strings_es.pdf | L.P. Rojas Saunero (C), David Díaz Rodríguez (C) | key, pptx | stringr 1.5.1 · 2024-05 | ✓ |
| strings | Vietnamese | strings_vi.pdf | Anh Hoang Duc (C) | — | stringr 1.2.0 · 2017-09 | ✓ |
| tidyeval | Spanish | tidyeval_es.pdf | — | pptx | rlang 0.3.0 · 2019-10 | **✗** |
| tidyr | Chinese (Simplified) | tidyr_zh_cn.pdf | Feifan Wang 王非凡 (P) | pptx | tibble 3.1.2, tidyr 1.1.3 · 2021-08 | ✓ |
| tidyr | Portuguese (Brazil) | tidyr_pt_br.pdf | Eric Scopinho (P) | pptx | tibble 3.1.2, tidyr 1.1.3 · 2021-08 | ✓ |
| tidyr | Spanish | tidyr_es.pdf | David Díaz Rodríguez (C) | pptx | tidyr 1.3.1, tibble 3.2.1 · 2024-05 | **✗** |

### Translations of community cheat sheets (none on the new site yet)

| Sheet | Language | File | Translator(s) | Src | Edition · date |
|---|---|---|---|---|---|
| base-r | Chinese (Simplified) | base-r_zh.pdf | Fu Yongchao 付永超 (P) | pptx (`base-r.pptx`) | added 2021-09 |
| base-r | German | base-r_de.pdf | Annika Kies, Martin Kies (P) | — | added 2020-04 |
| base-r | Greek | base-r_el.pdf | Kleanthis Koupidis (P) | — | 2015-03 |
| base-r | Japanese | base-r_ja.pdf | — | — | 2015-03 |
| base-r | Korean | base-r_ko.pdf | Taeho Kim (P) | LaTeX dir | 2015-03 |
| base-r | Portuguese (Brazil) | base-r_pt_br.pdf | Samuel Carleial (P) | SVG ×2 | 2015-03 |
| base-r | Spanish | base-r_es.pdf | Anthony Romero-Cerdán, Thatiane Ramírez Porras (P) | pptx | 2015-03 |
| base-r | Turkish | base-r_tr.pdf | Elif Kartal (P) | — | 2015-03 |
| base-r | Vietnamese | base-r_vi.pdf | — | — | added 2018-05 |
| datatable | French | datatable_fr.pdf | Christian Wiat (P) | pptx | added 2025-09 |
| datatable | Portuguese (Brazil) | datatable_pt_br.pdf | Samuel Carleial (P) | pptx | data.table 1.11.8 · 2019-01 |
| git-github | Spanish | git-github_es.pdf | Anthony Romero-Cerdán (P) | pptx | 2022-01 |
| git-github | Vietnamese | git-github_vi.pdf | Le-Huynh Truc-Ly (C) | pptx | 2022-01 |
| gtsummary | Vietnamese | gtsummary_vi.pdf | Le-Huynh Truc-Ly (C) | pptx | 2022-04 |
| metrica | Portuguese (Brazil) | metrica_pt_br.pdf | — | pptx | 2023-01 |
| metrica | Russian | metrica_ru.pdf | Denis Gazetdinov (P) | pptx | 2023-01 |
| metrica | Spanish | metrica_es.pdf | — | pptx | 2023-01 |
| quanteda | French | quanteda_fr.pdf | Ahmadou Dicko (C) | pptx | added 2019-09 |
| regex | French | regex_fr.pdf | Ahmadou Dicko (P) | pptx | added 2019-08 |
| regex | Turkish | regex_tr.pdf | Zeki Özen (P) | — | 2016-09 |
| survminer | Spanish | survminer_es.pdf | Maria Dermit (P) | pptx | added 2021-08 |
| syntax | Korean | syntax_ko.pdf | Kwangchun Lee (P) | key | 2018-02 |
| syntax | Spanish | syntax_es.pdf | Riva Quiroga (C) | key | 2018-01 |
| torch | French | torch_fr.pdf | Christophe Regouby (C) | key | torch 0.9.0 · 2023-02 |

---

## Appendix D: Excluded legacy material

Excluded per D4. Nothing here is migrated.

| Item | Location | Notes |
|---|---|---|
| `data-visualization-2.1.pdf`, `rmarkdown-2.0.pdf` | old repo root | copies of current sheets under legacy names (2021-08) |
| `old/pdfs/` (18 PDFs), `old/*.key`, `old/power-point-exports/`, `old/pngs/` | `old/` | the 2016–2017 sheets: data-wrangling, devtools, ggplot2 2.0/2.1, list-columns, rmarkdown, rmarkdown-reference, rstudio-IDE (+ poster), shiny (+ dark/old), sparklyr, 0-template |
| `translations/spanish/previous spanish translations/` (7 PDFs + keys, 1 pptx) | translations | not linked from the old site |
| `translations/japanese/previous japanese translations/` (1 PDF) | translations | not linked |
| `data-wrangling_{de,es,fr,ja,nl,pt,vi}.pdf` (+ `data-wrangling_es.key`) | translations | the English sheet only exists in `old/` |
| `0-template.pdf/.key/.pptx`, `pngs/0-template.png` | root, keynotes, powerpoints | contributor template, not a cheat sheet |
| `pngs/`, `pngs/thumbnails/` | pngs | the new site generates its own thumbnails |
| `misc-code/`, `html/python.*`, `html/common.R`, `renv/`, `_freeze/` | old repo | build helpers |

---

## Appendix E: Method and how to reproduce

- **Sources:**
  - old repo cloned to `/tmp/old-cheatsheets`
  - live old-site pages fetched with `curl`, to confirm the listings and the per-page translation links
- **Authors (Posit, D3):**
  - `git log --follow --format='%ae%x09%an' -- <slug>.pdf`, plus `git log` on `keynotes/<slug>.key`, `powerpoints/<slug>.pptx`, `illustrator/<slug>.ai`, `html/<slug>.qmd`, `google-slides/<slug>.md`
  - names merged by email; GitHub handles resolved with `gh api users/<login>`
- **Authors and translators (community and translations):**
  - the PDF text layer via `pdftotext`
  - image-only PDFs rendered with `pdftoppm` and read visually
  - footers without a text credit OCR'd with `tesseract` (English model)
  - commit fallback as described in D5/R3
- **Edition and date (D16):** regexes over the footer lines of each translated PDF (`Updated`, `Actualizado`, `Atualizado`, `Mise-à-jour`, `Обновлено`, `Оновлено`, `更新于`, `갱신월`, `Çeviri Tarihi`, …, plus `<pkg> <version>`). The fallback is `git log --diff-filter=A` on the file.
- **`software` (D13):** `library()`/`pkg::` calls and frequent package names in each PDF's text, matched against `ls content/software`. The mapping was then narrowed to packages the sheet is about or teaches substantially.
- **PDFs:**
  - freshness via `cmp` and the "Updated" footer
  - tags via `pdfinfo` (`Tagged:`)
  - compression compared between Ghostscript (`/ebook`, `/printer`), `qpdf`, and a `pikepdf` prototype
  - quality checked with `pdftotext` word counts and `magick compare` RMSE on renders
- **Build pipeline:** `netlify.toml`, `.github/workflows/build-deploy.yml`, and Netlify's documentation on `GIT_LFS_ENABLED`. That variable isn't relevant here, because the site is built in GitHub Actions.
