# Link Checking

Track link checking progress and document broken links found across ported blogs.

## Running lychee

Use [lychee](https://github.com/lycheeverse/lychee) to check links in ported posts.

### Against live dev server (recommended)

```bash
# Start Hugo dev server first: hugo server
lychee --base-url http://localhost:1313 content/blog/shiny/*/index.md
```

### Offline mode (limited)

```bash
lychee --offline content/blog/shiny/*/index.md
```

## Interpreting results

### False positives to ignore

- **Relative image paths** (e.g., `[500] http://localhost:1313/image.png`) - lychee misresolves relative paths like `![](image.png)` to site root instead of post folder. These work correctly in Hugo.
- **429 Too Many Requests** - GitHub rate limiting. Not broken, just throttled.
- **403 Forbidden** - Some sites block automated requests (NOAA, academic journals).
- **Conference registration links** - `reg.conf.posit.co` often blocks bots.

### Actual issues to fix

- **404 Not Found** - Dead external links
- **Relative paths to other site sections** - e.g., `../r/getstarted/` should be `https://shiny.posit.co/r/getstarted/`
- **Root-relative blog links** - e.g., `../blog/posts/foo/` should be `/blog/shiny/foo/`
- **Malformed URLs** - e.g., `../../https://` from sed replacement gone wrong

## Writing links in source files

**Important:**
- Fix links in BOTH the source file (`.qmd`, `.Rmd`, `.Rmarkdown`, `.ipynb`) AND the rendered file (`.md`, `.markdown`). Otherwise re-rendering will revert your fixes.
- In source files, never use relative links like `../`. Always use site-root paths or absolute URLs.
- Never use `https://posit.co/blog/...` for internal links — that's a different site.

### How Quarto processes links

| In source file | Rendered `.md` output |
|----------------|----------------------|
| Absolute URL (`https://...`) | Unchanged |
| Site-root (`/blog/foo/`) | Converted to relative (`../foo/`) |
| Relative (`../foo/`) | Unchanged |

Quarto converts site-root links to relative paths based on the output file's location. This is fine — Hugo resolves both correctly. The key is keeping source files clear and maintainable.

### What to use

| Link type | Use for | Example |
|-----------|---------|---------|
| **Absolute URL** | External sites, legacy blog docs | `https://posit-dev.github.io/pointblank/...` |
| **Site-root** | Internal blog links (this site) | `/blog/great-tables/foo/` |

## Link patterns to fix during porting

| Pattern | Fix |
|---------|-----|
| `https://shiny.posit.co/blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `/blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `../blog/posts/<slug>/` | `/blog/shiny/<slug>/` |
| `/r/...` or `/py/...` | `https://shiny.posit.co/r/...` or `https://shiny.posit.co/py/...` |
| `../r/...` or `../py/...` | `https://shiny.posit.co/r/...` or `https://shiny.posit.co/py/...` |
| `https://connect.rstudioservices.com/...` | `https://connect.posit.it/...` |
| `../../../../get-started/...` (great-tables) | `https://posit-dev.github.io/great-tables/get-started/...` |
| `../../user-guide/...` (pointblank) | `https://posit-dev.github.io/pointblank/user-guide/...` |

---

## Progress by blog

| Blog | Status | Notes |
|------|--------|-------|
| shiny | ✅ Done | Internal links fixed, external issues documented below |
| quarto | ✅ Done | Relative doc links fixed, external issues documented below |
| great-tables | ✅ Done | Interlinks stripped, external issues documented below |
| pointblank | ✅ Done | External issues documented below |
| plotnine | ✅ Done | |
| tidyverse | ⬜ TODO | |
| education | ⬜ TODO | |
| ai | ⬜ TODO | |
| rstudio | ⬜ TODO | |
| positron | ⬜ TODO | |

---

## Cross-blog links

Links between legacy blogs that need updating once both posts are ported.

| Post | Link | Target |
|------|------|--------|
| [plumber2-0-2-0](tidyverse/plumber2-0-2-0/index.md) | `https://shiny.posit.co/blog/posts/shiny-r-1.12/` | [shiny-r-1.12](shiny/shiny-r-1.12/index.md) |
| [dplyr-performance](tidyverse/dplyr-performance/index.md) | `https://tidyverse.org/blog/2026/02/dplyr-1-2-0/` | [dplyr-1-2-0](tidyverse/dplyr-1-2-0/index.md) |
| [shiny-python-1.0](shiny/shiny-python-1.0/index.md) | `https://shiny.posit.co/blog/posts/shiny-python-general-availability/` | [shiny-python-general-availability](shiny/shiny-python-general-availability/index.md) |
| [shiny-python-1.0](shiny/shiny-python-1.0/index.md) | `https://shiny.posit.co/blog/posts/shiny-express/` | [shiny-express](shiny/shiny-express/index.md) |

---

## Broken links by blog

### shiny

**Dead external links (404):**

| URL | Post |
|-----|------|
| https://www1.ncdc.noaa.gov/pub/data/normals/1981-2010/... | [weather-lookup-about](shiny/weather-lookup-about/index.md) |
| https://www.ncdc.noaa.gov/data-access/land-based-station-data/... | [weather-lookup-about](shiny/weather-lookup-about/index.md) |
| https://rstudio.github.io/bslib/articles/layouts.html | [bslib-dashboards](shiny/bslib-dashboards/index.md) |
| https://rstudio.github.io/shinyuieditor/articles/ui-editor-live-demo.html | [shinyuieditor-out-of-alpha](shiny/shinyuieditor-out-of-alpha/index.md) |
| https://shinyconf.appsilon.com/state-of-shiny-2023/ | [shiny-python-0.6.1](shiny/shiny-python-0.6.1/index.md) |
| https://github.com/rstudio/bslib/tree/main/inst/examples/flights | [bslib-dashboards](shiny/bslib-dashboards/index.md) |
| https://github.com/rstudio/otel | [shiny-r-1.12](shiny/shiny-r-1.12/index.md) |
| https://shiny.posit.co/py/api/express.ui.layout_columns.html | [responsive-shiny-layouts](shiny/responsive-shiny-layouts/index.md) |
| https://shiny.posit.co/py/docs/workflow-server.html | [shiny-on-hugging-face](shiny/shiny-on-hugging-face/index.md) |
| https://shiny.posit.co/py/api/ExTooltip.html | [shiny-python-0.5.0](shiny/shiny-python-0.5.0/index.md) |
| https://shiny.posit.co/py/docs/r-quickstart.html | [shiny-python-general-availability](shiny/shiny-python-general-availability/index.md) |
| https://shiny.posit.co/r/articles/build/bookmarking-state/ | [shinychat-tool-ui](shiny/shinychat-tool-ui/index.md) |

**GitHub user 404s (accounts deleted/renamed):**
kangjf1943, KRRLP-PL, MalteSteinCytel, oozbeker-onemagnify, jonathanmburns, ngoodkindGSI, bioinformzhang, howardbaek, MartinBaumga, TopBottomTau, toxintoxin, dependabot[bot]

### quarto

**Dead external links (404):**

| URL | Post |
|-----|------|
| https://www.r-consortium.org/r-medicine-quarto-for-reproducible-medical-manuscripts | [2022-07-28-rstudio-conf-2022-quarto](quarto/2022-07-28-rstudio-conf-2022-quarto/index.md) |

### great-tables

**Dead external links (404):**

| URL | Post |
|-----|------|
| https://docs.pola.rs/user-guide/expressions/lists/ | [introduction-0.4.0](great-tables/introduction-0.4.0/index.md) |
| https://fastht.ml/gallery/split_view?category=visualizations&project=great_tables_tables | [polars-dot-style](great-tables/polars-dot-style/index.md) |

### ai

**Slug mismatch:**

| Post | Issue |
|------|-------|
| [sparklyr-updates-q1-2024](ai/sparklyr-updates-q1-2024/index.md) | Original slug was `sparklyr-updates` |
