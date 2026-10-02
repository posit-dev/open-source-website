# Cheat sheet migration plan

Migrate every cheat sheet from the old site (<https://rstudio.github.io/cheatsheets/>, source: <https://github.com/rstudio/cheatsheets>) to `content/resources/cheatsheets/` on this site. That includes Posit sheets, community sheets, translations, and legacy or outdated material. It also adds a "By" (Posit / Community) filter to the overview page.

This document covers inventory and planning only. No cheat sheet or site code has been changed yet.

- Old repo snapshot inspected: `rstudio/cheatsheets@1e5e2bd` (2026-08-27, "Merge pull request #622 from rstudio/ml-yardsstick").
- New site snapshot: `main@e73b895e6`.
- Decisions that need a human are collected in [Open questions](#open-questions). They are tagged **Q1**, **Q2**, … and referenced throughout.

---

## Contents

1. [Summary](#summary)
2. [How the two sites are structured](#how-the-two-sites-are-structured)
3. [Design: the `by` field and "By" filter](#design-the-by-field-and-by-filter)
4. [Design: people, translations, source files](#design-people-translations-source-files)
5. [Migration plan and to-do list](#migration-plan-and-to-do-list)
6. [Open questions](#open-questions)
7. [Appendix A: Posit cheat sheets inventory](#appendix-a-posit-cheat-sheets-inventory)
8. [Appendix B: Community cheat sheets inventory](#appendix-b-community-cheat-sheets-inventory)
9. [Appendix C: Translations inventory](#appendix-c-translations-inventory)
10. [Appendix D: Legacy, archived, and orphaned files](#appendix-d-legacy-archived-and-orphaned-files)
11. [Appendix E: Method and how to reproduce](#appendix-e-method-and-how-to-reproduce)

---

## Summary

| | Count |
|---|---|
| Posit cheat sheets listed on the old site's index | 29 (incl. `renv`) |
| Posit cheat sheets in the old repo but **not** listed on the old index | 1 (`ml-measure-performance`) |
| Community cheat sheets on the old site's "Contributed" page | 65 |
| Translation PDFs shown on the old site's "Translations" page | 124 (17 languages) |
| Older translation PDFs in `previous … translations/` subfolders (not linked anywhere on the old site) | 8 |
| Cheat sheets on the new site | 30 |
| New-site-only cheat sheets | 1 (`polars`) |
| Old-site-only Posit cheat sheets | 1 (`renv`) |

Migration status of the 30 cheat sheets already on the new site:

| Status | Cheat sheets |
|---|---|
| **Complete** | `polars` (PDF + markdown + `.ai` source; no translations exist) |
| **PDF + English markdown** | `data-import`, `data-transformation`, `ml-create-models`, `ml-measure-performance`, `ml-preprocessing-data`, `ml-tidymodels` |
| **PDF only** | the other 23 Posit sheets |
| **Not started** | `renv` and all 65 community sheets |

No Posit sheet on the new site has its source files (Keynote/PowerPoint) yet. No translation on the new site has a translator credit or a translation source file.

### Key findings that change the scope

1. **20 of the 29 English PDFs on the new site are out of date.** The import script ran against an older state of the old site. Examples: `data-import` is "Updated: 2025-08" on the new site but "2026-08" in the old repo, and `posit-team` is 2024-09 vs. 2026-08. Only `ml-create-models`, `ml-measure-performance`, `ml-preprocessing-data`, `plotnine` and `shiny` match byte for byte. `quarto` and `shiny-python` have the same "Updated" date but different bytes. `ml-tidymodels` has the same date but is a 228 KB recompressed copy of a 16 MB original. So "completing" a sheet includes refreshing its PDF and thumbnails. See the "PDF" column in Appendix A.
2. **The old site has no explicit deprecated/outdated markers.** There are no banners or callouts, and the words "deprecated"/"outdated" don't appear on any page. The only signals are implicit:
   - the `old/` folder
   - root-level legacy copies (`data-visualization-2.1.pdf`, `rmarkdown-2.0.pdf`)
   - the `previous spanish translations/` and `previous japanese translations/` folders
   - translations of `data-wrangling`, a retired sheet whose English PDF only exists in `old/`
   - stale footers: many community PDFs date from 2017–2019 and reference "RStudio, Inc."

   See Appendix D and **Q4**.
3. **The old site's translation matcher has a bug, and the new site copied it.** `html/common.R::translation_list()` matches `{slug}.+\.pdf`, so `shiny` also picks up `shiny-python_es.pdf` and `gt` picks up `gtsummary_vi.pdf`. Both mistakes are now in the new site's front matter (`shiny/_index.md`, `gt/_index.md`).
4. **The new site is missing 3 translations of Posit sheets that the old site shows:** `data-import_el.pdf`, `tidyr_es.pdf`, `plumber_es.pdf`.
5. **`tidyeval` (and arguably `caret`) is listed as "contributed" but looks like Posit work.**
   - `tidyeval`: the footer says "CC BY SA Posit Software, PBC", the Keynote is in `keynotes/`, and it was added by Garrett Grolemund.
   - `caret`: by Max Kuhn (`max@rstudio.com` in the footer).

   See **Q2**.
6. **Contributed page credits nobody.** `contributed-cheatsheets.qmd` is a grid of thumbnails with no author names, so all community authors below come from the PDF footers. Commit history was used only when the PDF names nobody.
7. **Everything inside a Hugo page bundle is published.** For example, `polars/polars-cheatsheet.ai` is publicly downloadable at `/resources/cheatsheets/polars/polars-cheatsheet.ai`. Copying all old-repo source files would add about **815 MB** to the repo and to every deploy: ~468 MB English sources and ~347 MB translation sources. The largest file is `rstudio-ide.key` at 70 MB. The repo doesn't use Git LFS. See **Q6**.
8. **Four old-site "HTML" pages are stubs.** `gt`, `great-tables`, `positron` and `shinychat` say only "Will be updated soon!", so there is no markdown to port for them. Community sheets have no HTML/markdown versions at all. See **Q8**.

---

## How the two sites are structured

### Old site (`rstudio/cheatsheets`, Quarto website)

| What | Where |
|---|---|
| English PDFs (Posit + community) | repo root, `<slug>.pdf` (98 PDFs, incl. `0-template.pdf` and two legacy copies) |
| Thumbnails | `pngs/<slug>.png` (one image per sheet; `vivainsights_r` also has `_p1`/`_p2`) |
| Posit index page | `index.qmd`: a Quarto listing of `html/*.qmd` (29 entries, hard-coded order) |
| Accessible HTML versions | `html/<slug>.qmd`, using `html/common.R` helpers (`use_cheatsheet_logo()`, `pdf_preview_link()`, `translation_list()`); images in `html/images/` |
| Community page | `contributed-cheatsheets.qmd`: a 3-column grid of `[![name](pngs/x.png)](x.pdf)` links, no authors |
| Translations page | `translations.qmd`: R chunk that lists `translations/<language>/*.pdf` (top level only) |
| Translations | `translations/<language-name>/<slug>_<iso>[_<region>].pdf`, often with `.pptx`/`.key` next to them |
| Source files | `keynotes/*.key`, `powerpoints/*.pptx`, `illustrator/*.ai`, `inkscape/*.svg`, `latex/<slug>/` (`.tex`/`.Rnw`), `google-slides/*.md` (links to Google Slides) |
| Archive | `old/` (`pdfs/`, `pngs/`, `power-point-exports/`, `*.key`) |
| Authorship | **Nowhere in metadata.** Only in PDF footers ("CC BY SA <name> • <email> • …") and git history. Posit sheets all say "CC BY SA Posit Software, PBC". |

Origin is decided only by which page links to the sheet. Posit sheets are on `index.qmd`; community sheets are on `contributed-cheatsheets.qmd`.

### New site (Hugo, this repo)

Each cheat sheet is a **branch bundle**, `content/resources/cheatsheets/<slug>/_index.md`, with its PDF, `page-N.png` thumbnails, translation PDFs, and any images in the same directory. Front matter (from `data-import`, the richest example):

```yaml
title: Importing data with the tidyverse
image: page-1.png              # card image; can be a hex/logo (shiny.svg, team.png, hex-polars.svg)
color: '#cd792c'               # optional card background (polars, posit-team)
resource_type: cheatsheet      # selects layouts/resources/term.html cheat sheet branch + overview listing
date: '2026-02-25'
description: Learn about readr, readxl, haven, and googlesheets4.
download_url: data-import.pdf  # relative to the bundle
people:                        # `people` taxonomy (config/_default/hugo.toml), byline via partials/block/author.html
- Hadley Wickham
- Mine Çetinkaya-Rundel
thumbnails: [page-1.png, page-2.png]   # generated by scripts/create-cheatsheet-thumbnails.py
software: [readr, readxl, haven, googlesheets4]   # folder names in content/software/
languages: [R]                 # drives the Languages filter
translations:                  # list of single-key maps {Language label: file}
- Bengali: data-import_bn.pdf
- Spanish: data-import_es.pdf
# source_url: …                # supported by the template ("Source Code" button) but unused
```

The markdown body is the accessible text version, ported from `html/<slug>.qmd` with ```` ```{r} ```` changed to ```` ```r ````. Code isn't executed and outputs aren't included. Some Quarto chunk options leaked through (e.g. `#| include: false` in `data-import`; 43 `#|` lines across the cheat sheets).

How things are rendered:

- **Detail page:** `layouts/resources/term.html` (cheat sheet branch, ~line 245). It renders the thumbnails (lightbox, opens PDF page), a "Download PDF" button, an optional "Source Code" button (`source_url`), and "Available Translations" chips (`range $lang, $file := .`). A TOC is shown automatically.
- **Overview page:** `content/resources/cheatsheets.md` uses `layout: resource-type` with `resource_type_filter: cheatsheet` and contains a "Cheatsheets are being migrated" callout. Rendering goes through `layouts/resources/resource-type.html`:
  - It lists all `/resources` pages with `Params.resource_type == cheatsheet`, sorted by date.
  - It renders cards server-side with `partials/item.html`.
  - It emits `item-index.json` via `layouts/resources/resource-type.itemindex.json` → `partials/item-index-entry.html`.
- **Filters:** `assets/js/search-filter-sort.js`. Config comes from `data/filters.yaml` → `cheatsheet:` (sort by date/title; filters `topics` and `languages`, with values `Python`, `R`, `Other`).
  - `Other` uses the `other:` exclusion list, so it matches items whose languages are missing or not in [Python, R].
  - Within a dropdown, values are OR'ed; across dropdowns, AND'ed. An empty selection means "no filter".
  - State is synced to the URL (`?languages=R,Python`).
  - The `topics` dropdown only appears if some cheat sheet has topics. None do today.
- **Import tooling:**
  - `scripts/import-cheatsheets.py` scrapes `rstudio.github.io/cheatsheets/html/<slug>.html`, downloads the PDF and translations, and writes front matter. It has hard-coded slug→software/language maps and generated descriptions ("Quick reference guide for …").
  - `scripts/create-cheatsheet-thumbnails.py --pdf <path-or-slug>` (also `just create-cheatsheet-thumbnails`) renders every page at 150 dpi with `pdf2image`. It resizes them to 600 px wide, saves them as `page-N.png` next to the PDF, and rewrites `thumbnails:` in `_index.md`. The old site's `pngs/*.png` aren't used. For caveats, see Phase 1.10.
- **People:** any name in `people:` gets a taxonomy term page at `/people/<slug>/`. A profile in `content/people/<firstname-lastname>/_index.md` is optional. 82 of the 147 names used site-wide today have no profile, so profile-less people are normal.

---

## Design: the `by` field and "By" filter

### Front matter

```yaml
by: posit        # every Posit cheat sheet MUST have this
by: community    # community cheat sheets (recommended to be explicit)
# no `by` field   → treated as community
```

- `by` is a plain page param, not a taxonomy. It only has two values, and a taxonomy would create `/by/posit/` term pages we don't want.
- Values are lowercase in front matter. The UI shows **Posit** and **Community**.
- Add a build-time check, either in `scripts/` or as a `warnf` in the template. It should fail or warn if a cheat sheet has a `by` value other than `posit`/`community`, or if a sheet whose PDF footer says "Posit Software, PBC" lacks `by: posit`. This enforces "every Posit cheat sheet must have `by: posit`".

### Item index

In `layouts/partials/item-index-entry.html`, add a normalized `by` key for cheat sheets only. Blog posts, videos, and other types shouldn't suddenly become "Community" on mixed listings:

```go-html-template
{{ if eq $page.Params.resource_type "cheatsheet" }}
  {{ $by := cond (eq (lower ($page.Params.by | default "")) "posit") "Posit" "Community" }}
  {{ $entry = merge $entry (dict "by" $by) }}
{{ end }}
```

The default happens here, so "no `by` = community" is guaranteed in one place. The JS just matches strings, as it does for `languages`.

### Filter config (`data/filters.yaml` → `cheatsheet.filters`)

```yaml
    - key: by
      label: By
      values: [Posit, Community]
      default: [Posit]          # NEW option: pre-selected values
    - key: topics
      label: Topics
    - key: languages
      …
```

"By" goes first, so it sits next to the search box. `filter-controls.html` already renders any filter with `values` as a multi-select dropdown (`role="listbox" aria-multiselectable="true"`). No template change is needed for the dropdown itself.

### JavaScript changes (`assets/js/search-filter-sort.js`)

The component has no notion of a pre-selected default today. An empty set means "show all". Changes:

1. **Defaults.** In the constructor, store `defaults: new Set(f.default || [])` in `_filterCfgMap[key]`, and initialize `this.state.filters[key]` from it instead of `new Set()`.
2. **URL round-trip.**
   - `_updateURL()` writes `?by=` only when the selection differs from the default.
   - Deselecting everything must survive a reload, so an empty selection is written as `?by=` (key with an empty value). `_readURL()` treats a present-but-empty param as "explicitly empty", which shows everything, the same as selecting both.
   - Today `_readURL()` does `.split(',').filter(Boolean)` and only acts on `params.has(key)`. That still works if we keep the `has()` check and allow an empty Set.
   - A missing param means "use default".
3. **Reset.** `reset()` restores defaults instead of clearing to an empty set.
4. **"Active filters".** `_hasActiveFilters()` compares each set to its default, so the default view doesn't count as filtered. This affects the reset button and source-announcement logic.
5. **Badge and checkmarks.** On init, call `_updateBadge('by')` and `_updateFilterAria('by')` so the "Posit" option shows as checked and the badge shows "1" on first paint. See **Q10** on whether the badge should show for a default.
6. **Matching.** No change needed: `_matchesFilters()` already does `values.includes(active)`.

### Avoiding a flash of community cards

Cards are rendered server-side, and the filter applies only after `item-index.json` is fetched. Without care, community cards would show briefly, then disappear. Options:

- **Recommended:** in `resource-type.html`, pass `by` to the card wrapper (`data-by="community"`). Hide those cards with a `.js-filter-pending [data-by="community"] { display:none }` rule that is active only while JS initializes. The filter bar already uses an `invisible` → visible handoff, so the hook exists. Without JS, users still see everything.
- Alternative: sort Posit before Community server-side, so any flash happens below the fold.

### Overview page copy

When the migration is done, replace the "Cheatsheets are being migrated" callout in `content/resources/cheatsheets.md`. Add a line explaining the By filter and how to contribute (link to `CONTRIBUTING.md`).

### Other listings

Cheat sheets also show up on topic/tag/software/people term pages, the Atom feed, `llms.txt`, and Pagefind search. Those pages don't get the By filter, so community sheets will appear there unfiltered. See **Q11**.

---

## Design: people, translations, source files

### `people` (authors and translators)

- **Posit sheets:** authors come from the old repo's commit history (Appendix A). For sheets already on the new site, keep the existing `people` values; they came from this repo's history and the people involved. Merge in the old-repo authors after review (**Q3**).
- **Community sheets:** authors come from the PDF footer first, then commit history (Appendix B). Org-only credits ("ThinkR", "NIMBLE Development Team", "Sarid Research Institute", "the authors of the DRomics package", "ranalytics.vn") need a decision (**Q5**).
- **Translators:** they go into the cheat sheet's `people` list *and* into the per-translation entry (below), so each translator's `/people/<name>/` page lists the sheet. To keep the byline honest, `partials/block/author.html` should **exclude translator-only names from the byline** on cheat sheet pages. Translators are shown on the translation chips instead. See **Q7**.
- **Name normalization:** use one spelling per person, matching existing profiles where there is one:

  | Old spelling | New spelling |
  |---|---|
  | `Richard Iannone` | `Rich Iannone` (existing profile title) |
  | `Isabella Velasquez` | `Isabella Velásquez` |
  | `mine-cetinkaya-rundel`, `Mine Cetinkaya-Rundel` | `Mine Çetinkaya-Rundel` |
  | `Alex Coppock` | `Alexander Coppock` |
  | `Przemyslaw` | `Przemysław Biecek` |
  | `Christophe REGOUBY` | `Christophe Regouby` |
  | `Erik Petrovsky` | `Erik Petrovski` (GitHub name and pt-BR footer) |
  | `Michael maviolette` | probably `Michael Laviolette` (typo in the mosaic footer, **Q5**) |

- **Translator names with native scripts:** use the Latin-script name the translator gave in the PDF (e.g. "Kwangchun Lee" for 이광춘). Keep the native-script name in a comment if wanted.

**New people profiles.** None are *required*, because the taxonomy creates bare term pages. These Posit people will be referenced but have **no profile** today:

- Garrett Grolemund
- Averi Perny
- Andy Teucher (only if HTML-version authors are credited, **Q3**)
- Ryan Johnson
- Andrie de Vries (already used on the site without a profile)
- Gordon Shotwell

Existing profiles that will be used: Mine Çetinkaya-Rundel, Edgar Ruiz, Rich Iannone, Charlotte Wickham, Kevin Ushey, Carson Sievert, Greg Swinehart, Sara Altman, Tomasz Kalinowski, James Blair, Hadley Wickham, Jeroen Janssens, Hassan Kibirige, Thijs Nieuwdorp, Max Kuhn, Lionel Henry, Isabella Velásquez.

About 90 community authors and about 50 translators would get profile-less term pages. See **Q12** on whether that is wanted, and whether profiles should be created for any of them.

### Translations

The new site already has a translation format, so we keep it and extend it backwards-compatibly. Today each entry is a single-key map `{Label: file}`. Proposed:

```yaml
translations:
- language: Spanish            # chip label
  lang: es                     # BCP 47; used for hreflang/lang on the link
  file: data-import_es.pdf
  people: [David]              # translator(s); also added to page-level `people`
  source: data-import_es.pptx  # optional, see Source files
  updated: 2024-06             # optional; from the translated PDF footer
```

- The template (`term.html`, both translation blocks) should accept the old `{Label: file}` form too during the transition, so sheets can be migrated one at a time. Once all sheets are converted, drop the legacy branch.
- Chips render as `Spanish` with a tooltip/subtitle "translated by …".
- Labels must be unique per sheet:
  - `Chinese (Simplified)` / `Chinese (Traditional)` for `zh_cn`/`zh`/`zh_tw`
  - `Portuguese (Brazil)` for `pt_br` and `Portuguese` for `pt`
- **Location:** keep translation files in the English sheet's bundle (`<slug>/<slug>_<iso>.pdf`), as today. Keep the old file names, so URLs match the old repo's names.
- **Translations of sheets that don't exist in English on the new site** (`data-wrangling`, and translations of community sheets): they go into the bundle of the sheet they translate, so a community sheet's bundle contains its translations. Spanish-only originals (`introduccion-a-r`, `estadistica-descriptiva-con-R`) get their own bundle, flagged in **Q4**.
- **Thumbnails** for translations aren't needed. The lightbox uses the English PDF.

### Source files

Copy source files into the cheat sheet's bundle with their original names: `<slug>.key`, `<slug>.pptx`, `<slug>.ai`, `.svg`, or a `source/` subfolder for multi-file LaTeX. Add a front matter list:

```yaml
source_files:
- file: data-import.key
  format: Keynote
- file: data-import.pptx
  format: PowerPoint
```

The template renders one "Source (Keynote)" style button per entry, next to "Download PDF". This replaces the unused `source_url` param. Google Slides sources (`rgee`, `sparklyr`) are just URLs: `source_files: [{url: https://docs.google.com/…, format: Google Slides}]`.

Because bundle files are published as-is, this decision mainly comes down to size and hosting (**Q6**).

---

## Migration plan and to-do list

The phases are ordered so each one can ship on its own. Every step after Phase 1 is per-cheat-sheet and independent, which keeps PRs small.

### Phase 0: Decisions (blocking)

- [ ] Resolve the [open questions](#open-questions), at least Q1–Q8.
- [ ] Freeze an old-repo commit to migrate from (record the SHA in each PR). If the old repo keeps getting updates (it got PRs in Aug 2026), plan a final re-sync, Phase 6.

### Phase 1: Site groundwork (no cheat sheet content changes)

- [ ] 1.1 Add `by: posit` to all 30 existing cheat sheet `_index.md` files (all of them are Posit; see Q2 for `polars`).
- [ ] 1.2 `partials/item-index-entry.html`: emit normalized `by` for cheat sheets.
- [ ] 1.3 `data/filters.yaml`: add the `by` filter with `default: [Posit]`.
- [ ] 1.4 `search-filter-sort.js`: add default-selection support (defaults, URL round-trip incl. explicit empty, reset, `_hasActiveFilters`, badge/aria init).
- [ ] 1.5 `resource-type.html`/`item.html`: add a `data-by` attribute plus the pre-JS hide rule to avoid the flash.
- [ ] 1.6 `term.html`: support the extended translation entries (`language`/`lang`/`file`/`people`/`source`), keeping the legacy map form; show translators on chips.
- [ ] 1.7 `term.html`: render `source_files` buttons.
- [ ] 1.8 `block/author.html`: exclude translator-only people from the cheat sheet byline (if Q7 = yes).
- [ ] 1.9 Add a validation script (e.g. `scripts/validate-cheatsheets.py`, `uv run`) that checks:
  - `by` value
  - files referenced in `download_url`/`thumbnails`/`translations`/`source_files` exist
  - unique translation labels
  - `languages` present
  - `software` values exist in `content/software/`
- [ ] 1.10 Extend `scripts/import-cheatsheets.py`, or write a new `migrate-cheatsheet.py`, to work from a **local clone** of `rstudio/cheatsheets` instead of scraping HTML. For one slug it should:
  - copy the English PDF, translations, and sources
  - write or merge front matter (`by`, `people`, `translations` in the new format, `source_files`)
  - convert `html/<slug>.qmd` to markdown (```` ```{r} ```` → ```` ```r ````, strip `#|` lines, rewrite `images/` paths and copy the referenced images)
  - run `create-cheatsheet-thumbnails.py`

  Fix the slug-prefix translation bug (match `^{slug}_[a-z]{2}(_[a-z]{2})?\.pdf$`).

  Things to handle around `scripts/create-cheatsheet-thumbnails.py`:
  - **Multiple PDFs in one directory.** Given a slug, the script uses `<slug>/<slug>.pdf` and otherwise falls back to the only PDF in the directory. A bundle that has translation PDFs but no `<slug>.pdf` makes it exit with "Multiple PDFs". That happens for PDFs whose name differs from the slug, like `Machine Learning Modelling in R.pdf` or `polars-cheatsheet.pdf`. Always pass the full PDF path with `--pdf`.
  - **Front matter is rewritten.** The script loads the YAML and writes it back out with `yaml.dump`, so comments are lost and quoting and line wrapping change (key order is kept). Run it before writing the final front matter, or have the migration script set `thumbnails` itself and call only the rendering part.
  - **Stale thumbnails.** Extra `page-N.png` files aren't deleted when a refreshed PDF has fewer pages. Remove `page-*.png` before regenerating.
  - **`image:` isn't set.** The script only sets `thumbnails`. The migration script must set `image: page-1.png` itself, unless a logo or hex image is used.
  - **English PDF only.** Thumbnails are made for one PDF, so translations get none. That's fine with the current template.
  - **Dependencies.** `pdf2image` needs poppler (`pdftoppm`). Pages are rendered at 150 dpi and resized to 600 px wide, which matches the existing 600 × 463 thumbnails.
- [ ] 1.11 Run `yarn build-tailwind` if new Tailwind classes are introduced. Check the overview page:
  - default = Posit only
  - toggling Community shows all
  - deselecting both shows all
  - URL `?by=Community`, `?by=` and reset behave
  - the Languages filter still combines with By correctly
  - no flash of community cards

### Phase 2: Fix and complete the 30 existing cheat sheets

For each sheet, one PR or a small batch:

- [ ] Replace the PDF with the current old-repo PDF where they differ (Appendix A, "PDF" column), and regenerate thumbnails.
- [ ] Copy the source files listed in Appendix A.
- [ ] Port the markdown from `html/<slug>.qmd` where it's missing.
- [ ] Convert `translations` to the new format with translators. Add missing translations and their source files.
- [ ] Update `people` (after Q3).
- [ ] Clean up leftover `#|` chunk options in existing markdown.

Checklist (✓ = already done):

| Slug | PDF refresh | Markdown | Sources to copy | Translation fixes |
|---|---|---|---|---|
| data-import | [ ] | ✓ (clean `#|`) | [ ] key, pptx | [ ] add `el`; [ ] 5 translation sources |
| data-transformation | [ ] | ✓ | [ ] key, pptx | [ ] 7 translation sources |
| data-visualization | [ ] | [ ] port | [ ] key, pptx | [ ] 2 translation sources; [ ] fix `zh` label |
| factors | [ ] | [ ] port | [ ] key, pptx | [ ] 2 translation sources |
| great-tables | [ ] | [ ] write (old site stub, Q8) | [ ] key | — |
| gt | [ ] | [ ] write (old site stub, Q8) | [ ] key | [ ] **remove `gtsummary_vi.pdf`** (move to `gtsummary`) |
| keras | [ ] | [ ] port | [ ] key, pptx | [ ] 3 translation sources; [ ] `zh_cn` label |
| lubridate | [ ] | [ ] port | [ ] key, pptx | [ ] 4 translation sources |
| ml-create-models | ✓ same | ✓ | [ ] key | — |
| ml-measure-performance | ✓ same | ✓ | [ ] key | — |
| ml-preprocessing-data | ✓ same | ✓ | [ ] key | — |
| ml-tidymodels | [ ] (same date, recompressed; Q9) | ✓ | [ ] key | — |
| nlp-with-llms | [ ] | [ ] port | [ ] key | — |
| package-development | [ ] | [ ] port | [ ] key, pptx | [ ] 1 translation source |
| plotnine | ✓ same | [ ] port | [ ] ai | — |
| plumber | [ ] | [ ] port | [ ] key, pptx | [ ] **add `es`** + source |
| polars | ✓ | ✓ | ✓ ai | — (none exist) |
| posit-team | [ ] (2024-09 → 2026-08) | [ ] port | [ ] pptx | — |
| positron | [ ] | [ ] write (old site stub, Q8) | [ ] key | — |
| purrr | [ ] | [ ] port | [ ] key, pptx | [ ] 6 translation sources |
| quarto | [ ] (same date, differs) | [ ] port | [ ] key, pptx | [ ] 1 translation source |
| reticulate | [ ] | [ ] port | [ ] key, pptx | [ ] 1 translation source |
| rmarkdown | [ ] | [ ] port | [ ] key, pptx | [ ] 1 translation source |
| rstudio-ide | [ ] | [ ] port | [ ] key (70 MB), pptx (68 MB) | [ ] 2 translation sources |
| shiny | ✓ same | [ ] port | [ ] key, pptx | [ ] **remove `shiny-python_es.pdf`** (duplicate "Spanish"); [ ] 2 translation sources |
| shiny-python | [ ] (same date, differs) | [ ] port | [ ] key, pptx | [ ] 1 translation source |
| shinychat | [ ] | [ ] write (old site stub, Q8) | [ ] key | — |
| sparklyr | [ ] | [ ] port | [ ] pptx, Google Slides link | [ ] 4 translation sources; [ ] distinct `zh_cn`/`zh_tw` labels |
| strings | [ ] | [ ] port | [ ] key, pptx | [ ] 3 translation sources |
| tidyr | [ ] | [ ] port | [ ] key, pptx | [ ] **add `es`**; [ ] 3 translation sources |

Also fill gaps in existing front matter while touching these files:

- `languages` is missing on `posit-team`, `positron`, `quarto`.
- `software` is missing on `posit-team`.
- `nlp-with-llms` says only `Python`, but the title is "in R & Python".
- Descriptions are auto-generated ("Quick reference guide for …").

### Phase 3: Migrate the remaining Posit cheat sheet

- [ ] `renv`: PDF, thumbnails, markdown from `html/renv.qmd`, `keynotes/renv.key`, `by: posit`, people Kevin Ushey + Mine Çetinkaya-Rundel, `software: [renv]`, `languages: [R]`.
- [ ] `tidyeval`, `caret`: only if Q2 says they are Posit (then `by: posit`); otherwise they move with Phase 4.

### Phase 4: Migrate community cheat sheets

Per sheet (Appendix B):

- create `<new-slug>/` (slug rules: **Q1**)
- copy the PDF and run the thumbnail script
- set `by: community`, `people` (authors), `languages`, and `software` (only where a `content/software/` entry exists; otherwise omit, or decide per **Q13**)
- write a real `description`
- copy the sources and translations

Markdown body: a short summary only, unless Q8 decides otherwise.

Suggested batches (≈10 per PR):

- [ ] 4a. Sheets with translations (do these first, since they exercise the translation format): `base-r` (9 translations), `caret` (5), `metrica` (3), `datatable` (2), `git-github` (2), `regex` (2), `syntax` (2), `gtsummary` (1, moved from `gt`), `quanteda` (1), `survminer` (1), `tidyeval` (1), `torch` (1)
- [ ] 4b. Sheets with source files: `admiral`, `arrow`, `DRomics`, `h2o`, `imputeTS`, `jfa`, `labelled`, `overviewR`, `profile_optimise_py`, `R-best-practice`, `sas-r`, `SASvsRinPharma`, `SqueakR`, `srvyr`, `stata2r`, `time-series`, `vivainsights_r`, `vivainsights_py`, `quincunx` (svg), `sf` (svg), `collapse` (Rnw), `rgee` (Google Slides)
- [ ] 4c. PDF-only sheets: `bayesplot`, `bcea`, `cartography`, `declaredesign`, `distr6`, `estimatr`, `eurostat`, `gganimate`, `golem`, `gwasrapidd`, `how-big-is-your-graph`, `leaflet`, `Machine Learning Modelling in R`, `mapsf`, `mlr`, `mosaic`, `nardl`, `nimble`, `oSCR`, `packagefinder`, `parallel_computation`, `randomizr`, `rphylopic`, `SamplingStrata`, `sjmisc`, `slackr`, `teachR`, `tsbox`, `vegan`, `vtree`, `xplain`

### Phase 5: Legacy and orphaned material (per Q4)

- [ ] `data-wrangling` translations (7 languages). Either attach them to a new `data-wrangling` legacy bundle with the English `old/pdfs/data-wrangling-cheatsheet.pdf`, or attach them to `data-transformation` as "older version".
- [ ] `previous spanish translations/` (7 PDFs + keys) and `previous japanese translations/` (1 PDF).
- [ ] `introduccion-a-r.pdf`, `estadistica-descriptiva-con-R.pdf` (Spanish originals by Rosana Ferrero).
- [ ] `old/` archive (18 PDFs), `data-visualization-2.1.pdf`, `rmarkdown-2.0.pdf`.
- [ ] `0-template.pdf/.key/.pptx` and the `README.md` "Tips for making a new cheatsheet". Probably belong in `CONTRIBUTING.md` plus a template download, not as a cheat sheet (Q4).

### Phase 6: Cut-over

- [ ] Re-sync against the latest old-repo commit (PDF refreshes, new translations).
- [ ] Remove the "being migrated" callout and add the By-filter / contribute copy.
- [ ] Redirects and the old site's future (**Q14**). RStudio IDE's *Help > Cheat Sheets* menu and many external links point at `rstudio.github.io/cheatsheets/<slug>.pdf` and the legacy names (that's why `data-visualization-2.1.pdf`/`rmarkdown-2.0.pdf` exist).
- [ ] Update `rstudio/cheatsheets` `README.md`/`CONTRIBUTING.md` to point contributors at this repo, if the old repo is retired.
- [ ] Run the validation script and a link check (`scripts/lychee-errors.py`) over `/resources/cheatsheets/`.

---

## Open questions

Each needs a human decision before (or during) implementation.

**Q1. Slugs for community sheets.** Old file names mix cases and separators: `SASvsRinPharma`, `R-best-practice`, `parallel_computation`, `profile_optimise_py`, `vivainsights_r`, `Machine Learning Modelling in R`, `regex` (whose thumbnail is `regular-expressions.png`), `datatable`.
- Proposal: lowercase, `_`/spaces → `-`, keep the file name of the PDF as-is inside the bundle. For example `sas-vs-r-in-pharma/`, `machine-learning-modelling-in-r/`, `vivainsights-r/`, `profile-optimise-python/`, `regular-expressions/`, `data-table/`.
- OK, or keep the old names verbatim for URL parity?

**Q2. Origin edge cases.**
- (a) `tidyeval`: listed as contributed, but the footer says "Posit Software, PBC" and it was added by Garrett Grolemund. → `by: posit`?
- (b) `caret`: by Max Kuhn while at RStudio (`max@rstudio.com`), with the Keynote in `keynotes/`. → Posit or community?
- (c) `polars`: new-site-only, added by Jeroen Janssens (Posit) in #379. The footer says "Posit Software, PBC & Polars, Inc". Assumed `by: posit`; confirm.
- (d) `ml-measure-performance` is on the new site but not on the old index. Assumed Posit (Edgar Ruiz, Posit footer).

**Q3. Who counts as an author of a Posit sheet?** Commit history mixes:
- original authors (mostly Garrett Grolemund, 2017–2019)
- the 2021 design refresh (Averi Perny)
- current maintainer updates (Mine Çetinkaya-Rundel)
- bulk footer/license edits (Curtis Kephart, Averi Perny)
- HTML-version authors (Andy Teucher)
- PPTX conversions by the Spanish translator (`David`, 2024)

Appendix A proposes "original author(s) + substantive maintainers". Bulk edits and PPTX conversions are excluded. HTML-version authors are listed separately.
- Should Andy Teucher be credited on sheets whose markdown came from his HTML versions?
- Should existing new-site people be kept as-is where they differ from the commit history? `data-import` has Hadley Wickham, who isn't in the old repo's history; `plotnine` has Jeroen Janssens and Hassan Kibirige, while old history shows only Mine Çetinkaya-Rundel.

**Q4. What to do with legacy material** (Appendix D): `old/`, the two legacy root PDFs, `data-wrangling` translations, the `previous … translations/` folders, the two Spanish originals, and `0-template`. The brief says deprecated/outdated sheets are migrated too, but none are *marked* that way on the old site.
- Migrate all of it, as "Archived" bundles with an `archived: true` flag and a banner?
- Migrate only what the old site actually links to (i.e. skip `old/` and `previous …/`)?
- Or keep the old repo as the archive?

**Q5. Community credits that aren't a person, or are unclear.**
- Org-only credits:
  - `golem`: "ThinkR"; commit by Garrett Grolemund
  - `nimble`: "NIMBLE Development Team"
  - `teachR`: "Sarid Research Institute LTD."; commit by Adi Sarid
  - `DRomics`: "the authors of the DRomics package"; commit by Aurélie Siberchicot
  - Vietnamese translations: "ranalytics.vn"; commits by Anh Hoang Duc for 3 of them
- Inferred credits:
  - `imputeTS`: only the GitHub URL `SteffenMoritz/imputeTS` is in the PDF → Steffen Moritz?
  - `packagefinder`, `xplain`: only an email/GitHub handle → Joachim Zuckarelli
  - `admiral`, `arrow`: no credit in the PDF → committers Stefan Bundfuss, Mauricio Vargas
  - `mosaic`: "Michael maviolette" (typo?)

Use orgs as `people` entries, use the committer, or leave `people` empty?

**Q6. Source files: copy them all, and where should they live?**
- About 468 MB of English sources plus 347 MB of translation sources. The repo `.git` is already 3.4 GB, has no LFS, and every bundle file is published to Netlify. GitHub warns above 50 MB per file; `rstudio-ide.key` is 70 MB.
- Options:
  - (a) copy everything into bundles, as the brief says
  - (b) use Git LFS for `*.key`/`*.pptx`/`*.ai`
  - (c) keep sources in the bundle but exclude them from the Hugo publish (e.g. a `_source/` folder plus `build.publishResources`/cascade rules) and link to GitHub raw URLs instead
  - (d) link to the old repo's files instead of copying
- Recommendation: (b) or (c). Needs a decision before Phase 2.

**Q7. Translators in `people`.** The brief asks to put translators in `people`. That makes them appear in the byline next to the authors. Should the byline exclude translator-only people (shown on the translation chip instead), or should everyone be shown as authors?

**Q8. Markdown for sheets without an HTML version.** `gt`, `great-tables`, `positron`, and `shinychat` are stubs on the old site, and none of the 65 community sheets have a text version. Does "complete" require the markdown for these?
- Should someone write it (for Posit sheets: from the Keynote, by the authors)?
- Should a short summary plus the PDF be enough?
- What about community sheets: is a short description enough?

**Q9. PDF compression.** `ml-tidymodels.pdf` on the new site is a 228 KB recompressed version of the 16 MB original (same content date). The `polars` commit also notes "Compress PDF". Should all imported PDFs be recompressed, and if so with which tool/settings, or should originals be copied byte for byte?

**Q10. Badge on the default.** Should the "By" dropdown show a "1" badge when it's on its default (Posit only)? It signals that filtering is on, but it differs from other filters, which show no badge by default.

**Q11. Community sheets elsewhere.** Should community cheat sheets appear on topic/tag/software term pages, people pages, the Atom feed, `llms.txt`, and search like Posit sheets do, or only on the cheat sheet overview when enabled?

**Q12. People pages for ~140 external contributors.** Is a bare taxonomy term page per community author/translator acceptable, or should they be listed without linking? The taxonomy doesn't support that natively, so this would need, e.g., an `external_people` field. Should we create profiles for any of them?

**Q13. `software` for community sheets.** Most community packages (admiral, arrow, caret, gtsummary, golem, sf, …) have no `content/software/` entry. Should we omit `software`, add software entries, or use `tags`?

**Q14. Old site after migration.** Will `rstudio.github.io/cheatsheets` stay up, be redirected, or be archived? RStudio IDE links to it, and `pos.it/cheatsheets` is printed in every Posit PDF footer ("HTML cheatsheets at pos.it/cheatsheets"). Who owns updating the `pos.it` short links? Who keeps the two repos in sync until cut-over, given the old repo still receives PRs?

**Q15. Translation labels for variants.** The old site has `pt` and `pt_br`, and `zh`, `zh_cn` and `zh_tw`. `data-visualization_zh.pdf` is Simplified Chinese per its credits, even though it has no `_cn`. Are the proposed labels OK: "Portuguese (Brazil)" vs. "Portuguese", "Chinese (Simplified)"/"Chinese (Traditional)"?

**Q16. Outdated translations.** Most translations are of much older editions. For example `rmarkdown_ja.pdf` is rmarkdown 1.6 (2016) and `shiny_tr.pdf` is shiny 0.12 (2016), while the English versions are 2026. Should the new site show the edition/date on the chip (`updated:`) or mark them "older version"?

**Q17. The unlisted `ml-measure-performance`.** Was it intentionally left off the old index (e.g. not yet announced), or simply not added? Either way it's already live on the new site.

---

## Appendix A: Posit cheat sheets inventory

Legend:
- **Where:** B = both sites, O = old site only, N = new site only.
- **Status** (new site): ✗ not started · PDF · PDF+MD · ✓ complete (PDF, markdown, source files, all translations).
- **PDF:** "same" = byte-identical to the old repo; otherwise the "Updated:" footer of the new → old file.
- **Sources:** files in the old repo. None are in the new-site directory yet, except `polars`.
- **Authors** are from old-repo commit history (`git log --follow` on `<slug>.pdf`, `keynotes/<slug>.key`, `powerpoints/<slug>.pptx`, `html/<slug>.qmd`), excluding bulk footer/licence edits. "New site" shows what `people` currently says.
- **Deprecated:** none of these are marked deprecated or outdated on the old site.

| Slug | Title | Where | Status | PDF (new → old) | Proposed authors (commit history) | `people` on new site | Sources in old repo | Translations old site | On new site | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| data-import | Data import with the tidyverse | B | PDF+MD | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | Hadley Wickham, Mine Çetinkaya-Rundel | key, pptx | bn es fa pt_br ru tr uk uz **el** | all but **el** | new title "Importing data with the tidyverse"; leftover `#|` options in markdown |
| data-transformation | Data transformation with dplyr | B | PDF+MD | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | Mine Çetinkaya-Rundel | key, pptx | de es pt_br ru tr uk uz zh_cn | all 8 | HTML version by Andy Teucher |
| data-visualization | Data visualization with ggplot2 | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | — | key, pptx | de el es fr ja nl pt tr vi zh | all 10 | legacy copy `data-visualization-2.1.pdf` in old root |
| factors | Factors with forcats | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel, Garrett Grolemund, Averi Perny | — | key, pptx | es ja pt_br | all 3 | 1-page sheet |
| great-tables | Great Tables | B | PDF | 2025-07 → 2026-08 | Rich Iannone | — | key | — | — | old HTML page is a stub |
| gt | gt | B | PDF | 2025-07 → 2026-08 | Rich Iannone | — | key | (none; `gtsummary_vi` is mismatched) | `gtsummary_vi.pdf` **wrongly attached** | old HTML page is a stub |
| keras | Deep Learning with Keras | B | PDF | 2025-07 → 2026-07 | Andrie de Vries, Garrett Grolemund, Edgar Ruiz, Tomasz Kalinowski | — | key, pptx | es ja zh_cn | all 3 | translations are of keras 2.1 (2017) except es (2024) |
| lubridate | Dates and times with lubridate | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | — | key, pptx | es pt_br ru uk vi | all 5 | |
| ml-create-models | Create models with parsnip | B | PDF+MD | same | Edgar Ruiz | Edgar Ruiz | key | — | — | |
| ml-measure-performance | Measure model performance with yardstick | B* | PDF+MD | same | Edgar Ruiz | Edgar Ruiz | key | — | — | *in old repo but **not listed** on old index and no `html/` page (Q17) |
| ml-preprocessing-data | Preprocessing data with recipes | B | PDF+MD | same | Edgar Ruiz | Edgar Ruiz | key | — | — | |
| ml-tidymodels | Machine learning with tidymodels | B | PDF+MD | 2026-07 = 2026-07 (recompressed 16 MB → 228 KB) | Edgar Ruiz | Edgar Ruiz | key (38 MB) | — | — | Q9 |
| nlp-with-llms | Natural Language Processing using LLMs in R & Python | B | PDF | 2025-07 → 2026-07 | Edgar Ruiz | — | key | — | — | new `languages` only Python |
| package-development | Package Development | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel | — | key, pptx | de es it ko nl vi | all 6 | |
| plotnine | Data visualization with Plotnine | B | PDF | same (2025-08) | Mine Çetinkaya-Rundel (commits) | Jeroen Janssens, Hassan Kibirige | ai | — | — | Q3: commit history vs. new-site credits |
| plumber | REST APIs with plumber | B | PDF | 2025-08 → 2026-08 | James Blair, Mine Çetinkaya-Rundel | — | key, pptx | **es** | **missing es** | |
| polars | Python Polars: The Definitive Cheatsheet | N | ✓ | n/a | Jeroen Janssens (repo commit #379) | Jeroen Janssens, Thijs Nieuwdorp | `polars-cheatsheet.ai` (already in bundle) | — | — | origin Posit (Q2c); PDF name `polars-cheatsheet.pdf` ≠ slug |
| posit-team | Posit Team | B | PDF | 2024-09 → 2026-08 | Ryan Johnson | — | pptx | — | — | missing `languages`, `software` |
| positron | Positron | B | PDF | 2025-08 → 2026-08 | Mine Çetinkaya-Rundel | — | key | — | — | old HTML stub; missing `languages` |
| purrr | Apply functions with purrr | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | — | key, pptx | es ko pt_br ru uk vi | all 6 | Hadley Wickham edited HTML |
| quarto | Publish and Share with Quarto | B | PDF | 2026-06 = 2026-06 (bytes differ) | Charlotte Wickham | — | key, pptx | es | es | missing `languages` |
| renv | Reproducible R Environments with renv | **O** | ✗ | n/a → 2026-08 | Kevin Ushey, Mine Çetinkaya-Rundel | n/a | key | — | n/a | only Posit sheet not on new site |
| reticulate | Use Python with R with reticulate | B | PDF | 2025-07 → 2026-07 | Garrett Grolemund, Edgar Ruiz, Tomasz Kalinowski | — | key, pptx | es | es | |
| rmarkdown | rmarkdown | B | PDF | 2025-07 → 2026-08 | Garrett Grolemund, Averi Perny, Mine Çetinkaya-Rundel | — | key, pptx | de es it ja ko nl tr vi | all 8 | legacy copy `rmarkdown-2.0.pdf` in old root |
| rstudio-ide | RStudio IDE | B | PDF | 2025-07 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | — | key (70 MB), pptx (68 MB) | el es fr it ja pt vi | all 7 | largest sources |
| shiny | Shiny for R | B | PDF | same (2026-06) | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny, Carson Sievert, Greg Swinehart | — | key, pptx | de es fr tr vi | 5 + **bogus `shiny-python_es.pdf`** | two "Spanish" chips today |
| shiny-python | Shiny for Python | B | PDF | 2026-06 = 2026-06 (bytes differ) | Garrett Grolemund, Mine Çetinkaya-Rundel, Carson Sievert, Greg Swinehart, Gordon Shotwell | — | key, pptx | es | es | |
| shinychat | AI chatbots with shinychat | B | PDF | 2025-07 → 2026-08 | Sara Altman, Carson Sievert | — | key | — | — | old HTML stub |
| sparklyr | Data science in Spark with sparklyr | B | PDF | 2025-07 → 2026-08 | Garrett Grolemund, Edgar Ruiz, Mine Çetinkaya-Rundel | — | pptx, Google Slides link | de es ja zh_cn zh_tw | all 5 | both Chinese labelled "Chinese" today |
| strings | String manipulation with stringr | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | — | key, pptx | es pt_br vi | all 3 | Ryan Zomorrodi contributed fixes |
| tidyr | Data tidying with tidyr | B | PDF | 2025-08 → 2026-08 | Garrett Grolemund, Mine Çetinkaya-Rundel, Averi Perny | — | key, pptx | es pt_br zh_cn | **missing es** | |

Possibly Posit (Q2): `tidyeval` (Tidy evaluation with rlang, Garrett Grolemund, Posit footer, key + pptx, 1 translation) and `caret` (Max Kuhn). They're listed in Appendix B because the old site lists them as contributed.

HTML-version (markdown source) authors, if credited (Q3): Andy Teucher (most `html/*.qmd`), Mine Çetinkaya-Rundel, Edgar Ruiz (ml-*, keras, reticulate, nlp-with-llms), Charlotte Wickham (quarto), Kevin Ushey (renv).

---

## Appendix B: Community cheat sheets inventory

Every row here: **Where = old site only**, **Status = not started**, **Deprecated = not marked** (see Appendix D for stale footers).

- **Author source:** **P** = named in the PDF (text layer, or visually for image-only PDFs) · **C** = old-repo commit history (used only when the PDF names no person) · **O** = PDF names an organisation only (Q5).
- **Translations:** languages on the old site's translation page. None are on the new site.
- **Lang:** proposed `languages` value.
- **Updated:** PDF footer date, a rough "age" indicator.

| Old slug (PDF name) | Title (from PDF/alt text) | Author(s) | Src | Sources in old repo | Translations | Lang | Updated | Notes |
|---|---|---|---|---|---|---|---|---|
| admiral | admiral | Stefan Bundfuss | C | pptx | — | R | 2024-12 (commit) | no credit in PDF |
| arrow | Arrow for R | Mauricio Vargas | C | pptx | — | R | 2022-02 | no credit in PDF |
| base-r | Base R | Mhairi McNeill | P | LaTeX (`latex/base-r/`) | de el es ja ko pt_br tr vi zh (9) | R | — | old RStudio footer; ko has its own LaTeX source; pt_br has SVGs; zh has pptx |
| bayesplot | bayesplot | Edward A. Roualdes | P | — | — | R | 2020-05 | committed by Juan Telleria |
| bcea | BCEA | Gianluca Baio | P | — | — | R | 2021-02 | |
| caret | caret Package | Max Kuhn | P | key, pptx | es fr ko pt tr (5) | R | — | **Q2b** possibly Posit |
| cartography | Thematic maps with cartography | Timothée Giraud | P | — | — | R | 2018-07 | package superseded by mapsf (informational) |
| collapse | Advanced and Fast Data Transformation with collapse | Sebastian Krantz | P | LaTeX/Rnw (`latex/collapse/`) | — | R | 2023-10 | |
| datatable | data.table | Erik Petrovski, Mara Destefanis; edited by Tyson Barrett | P | pptx | fr pt_br (2) | R | 2026-07 | PDF spells "Petrovsky" |
| declaredesign | DeclareDesign | Graeme Blair, Jasper Cooper, Alexander Coppock, Macartan Humphreys, Neal Fultz | P | — | — | R | 2019-04 | |
| distr6 | distr6 | Raphael Sonabend | P | — | — | R | 2019-08 | |
| DRomics | DRomics | "authors of the DRomics package" → Aurélie Siberchicot | O→C | pptx | — | R | 2024-06 | Q5 |
| estimatr | estimatr | Graeme Blair, Jasper Cooper, Alexander Coppock, Macartan Humphreys, Luke Sonnet | P | — | — | R | 2018-11 | |
| eurostat | Access Eurostat data with eurostat | Przemysław Biecek, Markus Kainu | P (image) | — | — | R | 2019-11 | image-only PDF |
| gganimate | gganimate | Karl Hailperin | P | — | — | R | 2019-05 | |
| git-github | Git & GitHub | Mouna Belaid | P | pptx | es vi (2) | — | 2022-01 | no programming language |
| golem | golem | ThinkR | O | — | — | R | 2019-06 | Q5; committed by Garrett Grolemund |
| gtsummary | gtsummary | Esther Drill | P | pptx | vi (1) | R | 2022-04 | `gtsummary_vi` currently on new `gt` page |
| gwasrapidd | GWAS Catalog access with gwasrapidd | Ramiro Magno | P (image) | — | — | R | 2019-04 | image-only PDF |
| h2o | h2o | Juan Telleria Ruiz de Aguirre | P | pptx | — | R | 2018-06 | |
| how-big-is-your-graph | How big is your graph? | Steve Simon | P | — | — | R | — | |
| imputeTS | imputeTS | Steffen Moritz (inferred from URL in PDF) | P? | pptx | — | R | — | Q5 |
| jfa | jfa | Koen Derks | P | pptx | — | R | 2021-09 | |
| labelled | labelled | Joseph Larmarange | P | pptx | — | R | 2020-06 | |
| leaflet | Leaflet | Kejia Shi | P | — | — | R | — | |
| Machine Learning Modelling in R | Machine Learning Modelling in R | Arnaud Amsellem | P | — | — | R | 2018-03 | spaces in file name (Q1) |
| mapsf | mapsf | Ronan Ysebaert | P | — | — | R | 2021-11 | committed by Timothée Giraud (rCarto) |
| metrica | metrica | Carlos Hernandez, Adrian A. Correndo | P | pptx | es pt_br ru (3) | R | 2023-01 | |
| mlr | Machine Learning with mlr | Aaron Cooley | P (image) | — | — | R | — | mlr superseded by mlr3 (informational) |
| mosaic | mosaic | Michael "maviolette" (Laviolette?) | P | — | — | R | — | Q5 typo |
| nardl | nardl | Taha Zaghdoudi | P | — | — | R | — | |
| nimble | nimble | NIMBLE Development Team | O | — | — | R | 2020-05 | Q5 |
| oSCR | oSCR | Gabriela Palomo-Munoz | P | — | — | R | — | package by Chris Sutherland |
| overviewR | overviewR | Cosima Meyer, Dennis Hammerschmidt | P | key | — | R | 2022-09 | |
| packagefinder | Searching CRAN with packagefinder | Joachim Zuckarelli (from email/GitHub in PDF) | P? | — | — | R | — | |
| parallel_computation | Parallel computation | Ardalan Mirshani | P | — | — | R | 2019-03 | |
| profile_optimise_py | Profiling and Optimising in Python | Saranjeet Kaur Bhogal, Jost Migenda | P | pptx | — | Python | 2026-04 | |
| quanteda | quanteda | Stefan Müller, Kenneth Benoit | P | pptx | fr (1) | R | — | |
| quincunx | quincunx | Ramiro Magno | P | Inkscape SVG ×2 | — | R | 2021-05 | |
| randomizr | randomizr | Alexander Coppock ("Alex") | P | — | — | R | 2018-06 | |
| R-best-practice | R Best Practice | Jacob Scott | P | key | — | R | 2023-11 | |
| regex | Regular Expressions | Ian Kopacka | P | pptx | fr tr (2) | R | 2016-09 | thumbnail named `regular-expressions.png` |
| rgee | rgee | Antony Barja, Cesar Aybar | P | Google Slides link | — | R | — | |
| rphylopic | rphylopic | Gabriela Palomo-Munoz | P | — | — | R | — | package by Scott Chamberlain |
| SamplingStrata | SamplingStrata | Giulio Barcaroli | P | — | — | R | — | |
| sas-r | SAS <-> R | Brendan O'Dowd | P | pptx | — | R | 2022-10 | |
| SASvsRinPharma | SAS vs. R in Pharma | Bharath Kumar | P | pptx | — | R | 2022-11 | |
| sf | sf | Ryan Garnett | P | Inkscape SVG ×2 | — | R | — | |
| sjmisc | sjmisc | Daniel Lüdecke | P | — | — | R | — | |
| slackr | slackr | Daniel M. Villarreal | P | — | — | R | — | |
| srvyr | srvyr | Greg Freedman Ellis, Ben Schneider | P | pptx | — | R | 2025-01 | |
| stata2r | stata2r | Anthony Nguyen | P | pptx | — | R | 2019-10 | |
| survminer | survminer | Przemysław Biecek | P | — | es (1) | R | — | |
| syntax | R syntax comparison | Amelia McNamara | P | key | es ko (2) | R | 2018-01 | |
| SqueakR | SqueakR | Simon Ogundare | P | key | — | R | 2022-06 | |
| teachR | teachR | Sarid Research Institute LTD. (→ Adi Sarid) | O | — | — | R | 2019-03 | Q5 |
| tidyeval | Tidy evaluation with rlang | Posit Software, PBC → Garrett Grolemund | O→C | key, pptx | es (1) | R | 2018-11 | **Q2a** Posit footer |
| time-series | time-series | Yunjun Xia, Shuyu Huang | P | key | — | R | 2019-10 | |
| torch | torch | Christophe Regouby | P | key | fr (1) | R | 2023-02 | |
| tsbox | tsbox | Christoph Sax | P | — | — | R | 2019-04 | |
| vegan | vegan | Bruna Luiza Silva | P | — | — | R | — | |
| vivainsights_r | vivainsights (R) | Martin Chan | P | pptx (shared `vivainsights-r-py.pptx`) | — | R | 2024-11 | one pptx for both sheets |
| vivainsights_py | vivainsights (Python) | Martin Chan | P | pptx (shared) | — | Python | 2025-01 | |
| vtree | vtree | Nick Barrowman | P | — | — | R | 2020-07 | |
| xplain | xplain | Joachim Zuckarelli (from email/GitHub in PDF) | P? | — | — | R | — | |

---

## Appendix C: Translations inventory

All 124 translation PDFs on the old site's Translations page, grouped by the cheat sheet they translate.

- **New** = already in the new site's bundle (✓) or not (✗).
- **Translator source:** **P** = PDF credit · **C** = commit history (the PDF has no credit; usually the committer or the person who contributed the file) · **?** = unknown (committed in bulk by a Posit maintainer, no credit in PDF) · **O** = organisation only.
- **Src** = translation source file in the old repo (none are on the new site yet).

### Translations of Posit cheat sheets

| Sheet | Lang | File | Translator(s) | Src | New |
|---|---|---|---|---|---|
| data-import | Bengali | data-import_bn.pdf | Saif Kabir Asif (C) | pptx | ✓ |
| data-import | Greek | data-import_el.pdf | Nikolaos Koupidis (P) | — | **✗** |
| data-import | Spanish | data-import_es.pdf | David (`davidrsch`) (C) | pptx | ✓ |
| data-import | Persian | data-import_fa.pdf | Vahid Faraji Jobehdar, Reza Mazloomi (P) | — | ✓ |
| data-import | Portuguese (Brazil) | data-import_pt_br.pdf | Eric Scopinho (P) | pptx | ✓ |
| data-import | Russian | data-import_ru.pdf | ? | key | ✓ |
| data-import | Turkish | data-import_tr.pdf | Metin Yazici (P) | — | ✓ |
| data-import | Ukrainian | data-import_uk.pdf | ? | key | ✓ |
| data-import | Uzbek | data-import_uz.pdf | ? | — | ✓ |
| data-transformation | German | data-transformation_de.pdf | Lucia Gjeltema (P) | pptx | ✓ |
| data-transformation | Spanish | data-transformation_es.pdf | David (2024 update) (C); earlier Frans van Dunné (C) | key, pptx | ✓ |
| data-transformation | Portuguese (Brazil) | data-transformation_pt_br.pdf | Eric Scopinho (P) | pptx | ✓ |
| data-transformation | Russian | data-transformation_ru.pdf | Evgeni Chasnovski? (C) | key | ✓ |
| data-transformation | Turkish | data-transformation_tr.pdf | ? | — | ✓ |
| data-transformation | Ukrainian | data-transformation_uk.pdf | Evgeni Chasnovski? (C) | key | ✓ |
| data-transformation | Uzbek | data-transformation_uz.pdf | ? | — | ✓ |
| data-transformation | Chinese (Simplified) | data-transformation_zh_cn.pdf | Aicen Yu 于艾岑 (P) | key | ✓ |
| data-visualization | German | data-visualization_de.pdf | Lucia Gjeltema (P) | — | ✓ |
| data-visualization | Greek | data-visualization_el.pdf | Nikolaos Koupidis (P) | — | ✓ |
| data-visualization | Spanish | data-visualization_es.pdf | Carolina Mengoni (C), David (2024 update) (C) | pptx | ✓ |
| data-visualization | French | data-visualization_fr.pdf | Vincent Guyader (ThinkR) (P) | — | ✓ |
| data-visualization | Japanese | data-visualization_ja.pdf | ? | — | ✓ |
| data-visualization | Dutch | data-visualization_nl.pdf | ? | — | ✓ |
| data-visualization | Portuguese | data-visualization_pt.pdf | Augusto Queiroz de Macedo (P) | — | ✓ |
| data-visualization | Turkish | data-visualization_tr.pdf | ? | — | ✓ |
| data-visualization | Vietnamese | data-visualization_vi.pdf | ranalytics.vn (O) | — | ✓ |
| data-visualization | Chinese (Simplified) | data-visualization_zh.pdf | Guang-Teng Meng (P) | pptx | ✓ |
| factors | Spanish | factors_es.pdf | Laura Acion (C), David (2024 update) (C) | pptx | ✓ |
| factors | Japanese | factors_ja.pdf | Taiyo Nakashima (P) | — | ✓ |
| factors | Portuguese (Brazil) | factors_pt_br.pdf | Eric Scopinho (P) | pptx | ✓ |
| keras | Spanish | keras_es.pdf | David (2024) (C) | key, pptx | ✓ |
| keras | Japanese | keras_ja.pdf | Masato Takahashi (P) | — | ✓ |
| keras | Chinese (Simplified) | keras_zh_cn.pdf | Harry Zhu? (C) | key | ✓ |
| lubridate | Spanish | lubridate_es.pdf | Yanina Bellini Saibene (C), David (2024 update) (C) | pptx | ✓ |
| lubridate | Portuguese (Brazil) | lubridate_pt_br.pdf | Eric Scopinho (P) | pptx | ✓ |
| lubridate | Russian | lubridate_ru.pdf | Evgeni Chasnovski? (C) | key | ✓ |
| lubridate | Ukrainian | lubridate_uk.pdf | Evgeni Chasnovski? (C) | key | ✓ |
| lubridate | Vietnamese | lubridate_vi.pdf | ranalytics.vn (O); committed by Anh Hoang Duc | — | ✓ |
| package-development | German | package-development_de.pdf | Lucia Gjeltema (P) | — | ✓ |
| package-development | Spanish | package-development_es.pdf | Paola Corrales (C), David (2024 update) (C) | pptx | ✓ |
| package-development | Italian | package-development_it.pdf | Angelo Salatino (P) | — | ✓ |
| package-development | Korean | package-development_ko.pdf | Kwangchun Lee 이광춘 (xwMOOC) (P) | — | ✓ |
| package-development | Dutch | package-development_nl.pdf | ? | — | ✓ |
| package-development | Vietnamese | package-development_vi.pdf | ranalytics.vn (O) | — | ✓ |
| plumber | Spanish | plumber_es.pdf | David (C) | pptx | **✗** |
| purrr | Spanish | purrr_es.pdf | David (2024 update) (C) | key, pptx | ✓ |
| purrr | Korean | purrr_ko.pdf | Kwangchun Lee (P) | key | ✓ |
| purrr | Portuguese (Brazil) | purrr_pt_br.pdf | Eric Scopinho (P) | pptx | ✓ |
| purrr | Russian | purrr_ru.pdf | Evgeni Chasnovski? (C) | key | ✓ |
| purrr | Ukrainian | purrr_uk.pdf | Evgeni Chasnovski? (C) | key | ✓ |
| purrr | Vietnamese | purrr_vi.pdf | ranalytics.vn (O); committed by Anh Hoang Duc | — | ✓ |
| quarto | Spanish | quarto_es.pdf | David (C) | pptx | ✓ |
| reticulate | Spanish | reticulate_es.pdf | Vanesa Maribel (C), David (2024 update) (C) | pptx | ✓ |
| rmarkdown | German | rmarkdown_de.pdf | Lucia Gjeltema (P) | — | ✓ |
| rmarkdown | Spanish | rmarkdown_es.pdf | Jesica Formoso (C), David (2024 update) (C) | pptx | ✓ |
| rmarkdown | Italian | rmarkdown_it.pdf | Angelo Salatino (P) | — | ✓ |
| rmarkdown | Japanese | rmarkdown_ja.pdf | Masato Takahashi (P) | — | ✓ |
| rmarkdown | Korean | rmarkdown_ko.pdf | Kwangchun Lee (xwMOOC) (P) | — | ✓ |
| rmarkdown | Dutch | rmarkdown_nl.pdf | ? | — | ✓ |
| rmarkdown | Turkish | rmarkdown_tr.pdf | Metin Yazici (P) | — | ✓ |
| rmarkdown | Vietnamese | rmarkdown_vi.pdf | ranalytics.vn (O) | — | ✓ |
| rstudio-ide | Greek | rstudio-ide_el.pdf | Kleanthis Koupidis (P) | — | ✓ |
| rstudio-ide | Spanish | rstudio-ide_es.pdf | Monica Alonso (C), David (2024 update) (C) | pptx | ✓ |
| rstudio-ide | French | rstudio-ide_fr.pdf | Diane Beldame (ThinkR) (P) | — | ✓ |
| rstudio-ide | Italian | rstudio-ide_it.pdf | Angelo Salatino (P) | — | ✓ |
| rstudio-ide | Japanese | rstudio-ide_ja.pdf | Masato Takahashi (P) | — | ✓ |
| rstudio-ide | Portuguese | rstudio-ide_pt.pdf | Augusto Queiroz de Macedo (P) | — | ✓ |
| rstudio-ide | Vietnamese | rstudio-ide_vi.pdf | Le-Huynh Truc-Ly (C) | pptx | ✓ |
| shiny | German | shiny_de.pdf | Lucia Gjeltema (P) | — | ✓ |
| shiny | Spanish | shiny_es.pdf | Florencia D'Andrea (C), David (2024 update) (C) | key, pptx | ✓ |
| shiny | French | shiny_fr.pdf | Asma Balti, Vincent Guyader (ThinkR) (P) | — | ✓ |
| shiny | Turkish | shiny_tr.pdf | Metin Yazici (P) | — | ✓ |
| shiny | Vietnamese | shiny_vi.pdf | ranalytics.vn (O) | — | ✓ |
| shiny-python | Spanish | shiny-python_es.pdf | David (C) | pptx | ✓ (also wrongly on `shiny`) |
| sparklyr | German | sparklyr_de.pdf | Ke Zhang (P) | key | ✓ |
| sparklyr | Spanish | sparklyr_es.pdf | Daniela Prina (C), David (2024 update) (C) | pptx | ✓ |
| sparklyr | Japanese | sparklyr_ja.pdf | Masato Takahashi (P) | — | ✓ |
| sparklyr | Chinese (Simplified) | sparklyr_zh_cn.pdf | Ke Zhang 张克 (P) | key | ✓ |
| sparklyr | Chinese (Traditional) | sparklyr_zh_tw.pdf | Ke Zhang 張克 (P) | key | ✓ |
| strings | Spanish | strings_es.pdf | L.P. Rojas Saunero (C), David (2024 update) (C) | key, pptx | ✓ |
| strings | Portuguese (Brazil) | strings_pt_br.pdf | Eric Scopinho (P) | pptx | ✓ |
| strings | Vietnamese | strings_vi.pdf | ranalytics.vn (O); committed by Anh Hoang Duc | — | ✓ |
| tidyr | Spanish | tidyr_es.pdf | David (C) | pptx | **✗** |
| tidyr | Portuguese (Brazil) | tidyr_pt_br.pdf | Eric Scopinho (P) | pptx | ✓ |
| tidyr | Chinese (Simplified) | tidyr_zh_cn.pdf | Feifan Wang 王非凡 (P) | pptx | ✓ |

### Translations of community cheat sheets (none on new site)

| Sheet | Lang | File | Translator(s) | Src |
|---|---|---|---|---|
| base-r | German | base-r_de.pdf | Annika Kies, Martin Kies (LeverageData) (P) | — |
| base-r | Greek | base-r_el.pdf | Kleanthis Koupidis (P) | — |
| base-r | Spanish | base-r_es.pdf | Anthony Romero-Cerdán, Thatiane Ramírez Porras (ADIECS) (P) | pptx |
| base-r | Japanese | base-r_ja.pdf | ? | — |
| base-r | Korean | base-r_ko.pdf | Taeho Kim (P) | LaTeX dir + `.sty` |
| base-r | Portuguese (Brazil) | base-r_pt_br.pdf | Samuel Carleial (P) | SVG ×2 |
| base-r | Turkish | base-r_tr.pdf | Elif Kartal (P) | — |
| base-r | Vietnamese | base-r_vi.pdf | ranalytics.vn (O) | — |
| base-r | Chinese (Simplified) | base-r_zh.pdf | Fu Yongchao 付永超 (P) | `base-r.pptx` (in `chinese/`, no suffix) |
| caret | Spanish | caret_es.pdf | ? | key |
| caret | French | caret_fr.pdf | Ahmadou Dicko (C) | pptx |
| caret | Korean | caret_ko.pdf | Kwangchun Lee (P) | pptx |
| caret | Portuguese | caret_pt.pdf | Karen da Silva Lopes (P) | pptx |
| caret | Turkish | caret_tr.pdf | İlkim Ecem Emre (P) | — |
| datatable | French | datatable_fr.pdf | Christian Wiat (P) | pptx |
| datatable | Portuguese (Brazil) | datatable_pt_br.pdf | Samuel Carleial (P) | pptx |
| git-github | Spanish | git-github_es.pdf | Anthony Romero-Cerdán (ADIECS) (P) | pptx |
| git-github | Vietnamese | git-github_vi.pdf | Le-Huynh Truc-Ly (C) | pptx |
| gtsummary | Vietnamese | gtsummary_vi.pdf | Le-Huynh Truc-Ly (C) | pptx |
| metrica | Spanish | metrica_es.pdf | ? (committed by author Adrian Correndo) | pptx |
| metrica | Portuguese (Brazil) | metrica_pt_br.pdf | ? (committed by author Adrian Correndo) | pptx |
| metrica | Russian | metrica_ru.pdf | Denis Gazetdinov (P, listed with authors) | pptx |
| quanteda | French | quanteda_fr.pdf | Ahmadou Dicko (C) | pptx |
| regex | French | regex_fr.pdf | Ahmadou Dicko (P) | pptx |
| regex | Turkish | regex_tr.pdf | Zeki Özen (P) | — |
| survminer | Spanish | survminer_es.pdf | Maria Dermit (P) | pptx |
| syntax | Spanish | syntax_es.pdf | Riva Quiroga (C) | key |
| syntax | Korean | syntax_ko.pdf | Kwangchun Lee (P) | key |
| tidyeval | Spanish | tidyeval_es.pdf | Violeta Roizman (`Violeta R`) (C) | pptx |
| torch | French | torch_fr.pdf | Christophe Regouby (author) (C) | key |

### Translations of a retired sheet, and Spanish originals (Q4)

| Sheet | Lang | File | Translator(s) | Src |
|---|---|---|---|---|
| data-wrangling (retired; English only in `old/pdfs/data-wrangling-cheatsheet.pdf`) | German | data-wrangling_de.pdf | Lucia Gjeltema (P) | — |
| data-wrangling | Spanish | data-wrangling_es.pdf | Frans van Dunné (P) | key |
| data-wrangling | French | data-wrangling_fr.pdf | Diane Beldame (ThinkR) (P) | — |
| data-wrangling | Japanese | data-wrangling_ja.pdf | Tomo Masuda (P) | — |
| data-wrangling | Dutch | data-wrangling_nl.pdf | Frans van Dunné? (C, `FvD`) | — |
| data-wrangling | Portuguese | data-wrangling_pt.pdf | Augusto Queiroz de Macedo (P) | — |
| data-wrangling | Vietnamese | data-wrangling_vi.pdf | ranalytics.vn (O) | — |
| (Spanish original) | Spanish | introduccion-a-r.pdf | Rosana Ferrero, author (P); committed by Juan Luis López Garrancho | — |
| (Spanish original) | Spanish | estadistica-descriptiva-con-R.pdf | Rosana Ferrero, author (P) | — |

"?" rows need either a visual check of the PDF, which the OCR here couldn't decode (Cyrillic/CJK/Uzbek footers), or outreach. Russian and Ukrainian translations were partly fixed by Evgeni Chasnovski; whether he is the translator is unconfirmed.

---

## Appendix D: Legacy, archived, and orphaned files

None of these are marked "deprecated" or "outdated" on the old site. They're listed so Q4 can be decided.

| Item | Location | What it is |
|---|---|---|
| `data-visualization-2.1.pdf`, `rmarkdown-2.0.pdf` | old repo root | copies of current sheets under legacy names ("Add copies of new cheatsheets with old names", 2021-08), probably kept for old inbound links |
| `old/pdfs/` (18 PDFs) | `old/` | `data-import-cheatsheet`, `data-transformation-cheatsheet`, `data-wrangling-cheatsheet`, `devtools-cheatsheet`, `ggplot2-cheatsheet` (+ `-2.0`, `-2.1`), `list-columns-cheatsheet`, `rmarkdown-cheatsheet` (+ `-2.0`), `rmarkdown-reference`, `rstudio-IDE-cheatsheet`, `rstudio-IDE-poster`, `shiny-cheatsheet` (+ `-dark`, `-old`), `sparklyr`, `0-template` |
| `old/*.key`, `old/power-point-exports/*.pptx`, `old/pngs/` | `old/` | sources for the above |
| `translations/spanish/previous spanish translations/` | translations | `data-import-cheatsheet_Spanish`, `devtools-cheatsheet_Spanish` (Frans van Dunné), `lubridate_Spanish`, `rmarkdown_Spanish` (Frans van Dunné), `rstudio-entorno` (Rosana Ferrero), `shiny_Spanish` (Frans van Dunné), `sparklyrSpanish` (PDF + key each), `package-development.pptx`. Not linked from any old-site page |
| `translations/japanese/previous japanese translations/Rmarkdown-cheatsheet-2.0_ja.pdf` | translations | not linked |
| `data-wrangling_*` (7 languages) | translations | linked on the Translations page, but the English sheet is retired |
| `0-template.pdf/.key/.pptx`, `pngs/0-template.png` | root, keynotes, powerpoints | contributor template |
| `pngs/thumbnails/*-thumbs.png` | pngs | old-style thumbnails, not needed (the new site generates its own) |
| `misc-code/`, `html/python.*`, `html/common.R`, `renv/` | old repo | build helpers, not content |
| Stale community sheets | various | footers from 2016–2019 with "RStudio, Inc." and old package versions, e.g. `regex` (2016), `syntax` (2018-01), `estimatr` (2018), `h2o` (2018); `cartography` (superseded by `mapsf`) and `mlr` (superseded by `mlr3`). Informational only |

---

## Appendix E: Method and how to reproduce

- Old repo cloned to `/tmp/old-cheatsheets` (`git clone https://github.com/rstudio/cheatsheets`). Live pages fetched with `curl` to confirm the listings and which translations each HTML page links to (this showed the `shiny`/`gt` matcher bug live).
- **Authors:**
  - PDF text layer via `pdftotext`, grepping footers (`CC BY`, `Created by`, `Translated by`/`Traducido por`/`Traduit par`/`Übersetzt von`/`Çeviri`/`翻译`/`번역`/`Μετάφραση`/…).
  - Image-only PDFs (`eurostat`, `gwasrapidd`, `mlr`, `admiral`, `arrow`) were rendered with `pdftoppm` and read visually.
  - Translation footers without a text credit were OCR'd with `tesseract` (English model only).
  - Commit fallback: `git log --follow --format=%an -- <file>`. GitHub handles were resolved with `gh api users/<login>`.
- **PDF freshness:** `cmp` between the new-site and old-repo files, plus the `Updated:` footer string from `pdftotext`.
- **New-site status:** front matter keys and body line counts of each `_index.md`, plus `git log -- content/resources/cheatsheets`.
- **Sizes:** `du` on `keynotes/`, `powerpoints/`, `illustrator/`, `inkscape/` and `translations/**/*.{key,pptx}`.
