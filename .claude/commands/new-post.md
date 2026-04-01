---
name: new-post
description: Scaffold a new blog post with inferred frontmatter, branch, and optional environment setup
---

Help the user create a new blog post for the Posit open-source website. Work through these steps in order.

## Step 1: Gather information

Ask the user for anything not already provided via arguments: `$ARGUMENTS`

- **Title** — the post title
- **Topic** — a brief description of what the post is about (use this to infer frontmatter)
- **Author(s)** — full name(s) of the people writing the post
- **Executable code?** — ask "Will this post include executable code chunks (R or Python)?" rather than asking about file format directly:
  - Yes → `.qmd`; also ask whether the code is R, Python, or both
  - No → `.md` (unless they specifically want `.ipynb`, which is fine to offer)

## Step 2: Infer frontmatter

From the title and topic, reason about:

- **slug** — lowercase, hyphenated, derived from the title
- **subfolder** — which project subfolder the post belongs in, if any:
  - Use `positron/`, `tidyverse/`, `shiny/`, `quarto/`, `great-tables/`, `plotnine/`, or `pointblank/` if the post is primarily about that project
  - Use the top level for general news, AI posts, or anything cross-cutting
- **software** — folder names from `content/software/` that the post is about (e.g. `ggplot2`, `quarto`, `great-tables`)
- **languages** — programming languages featured (R, Python, etc.)
- **categories** — one or more from the fixed set: Machine Learning, Artificial Intelligence, Visualization, Interactive Apps, Publishing, MLOps and Admin, Data Wrangling, Best Practices, Community
- **description** — a draft 1–2 sentence description of the post

Present your inferences clearly and ask the user to confirm or correct before proceeding.

For every shell command below, use a description that explains *why* this step is needed in the context of creating the blog post — not just what the command does. This text appears in the permission prompt and helps the author understand what's happening.

## Step 3: Create a branch

Description: "Creating a dedicated branch for this post so it can be reviewed as a PR before going live"

```sh
git checkout -b blog/<slug>
```

## Step 4: Scaffold the post

Description: "Scaffolding the post folder and frontmatter from the blog archetype"

```sh
hugo new blog/<subfolder-if-any><slug>/index.md
```

If the format is `.qmd`, rename the file:

Description: "Renaming to .qmd so Quarto will render this post to Markdown before Hugo builds it"

```sh
mv content/blog/<path>/index.md content/blog/<path>/index.qmd
```

## Step 5: Fill in the frontmatter

Edit the created file to replace the archetype defaults with the confirmed values:

- Set `title`, `date` (today), `people`, `description`
- Set `categories` to only the relevant values (remove the rest)
- Set `software` and `languages` to only the relevant values; remove empty `-` entries
- Remove empty `tags` entries
- Leave `image` and `image-alt` empty for the author to fill in

## Step 6: Set up an environment (`.qmd` posts only)

**Python only:**

Description: "Setting up a per-post Python environment so package versions are recorded alongside the post"

```sh
uv init --no-workspace
```
Then ask which packages are needed and `uv add` them.

**R only:**

Description: "Setting up a per-post R environment so package versions are recorded alongside the post"

```sh
Rscript -e "renv::init()"
```

**Both R and Python:**

Description: "Setting up a per-post R environment with reticulate so both R and Python packages are recorded"

```sh
Rscript -e "renv::init()"
Rscript -e "renv::install('reticulate')"
```

## Step 7: Open the file

Report the full path to the created file so the user can open it themselves.

## Step 8: Provide a checklist

Finish by giving the author this checklist:

- [ ] Review the inferred frontmatter — correct `categories`, `software`, `languages` if needed
- [ ] Add `image` (1920×1080 PNG or JPG recommended) and `image-alt`
- [ ] *(`.qmd` with R)* Install packages then run `renv::snapshot()` to lock the environment
- [ ] Preview: open a PR against `main` for a Netlify preview, or run `just dev` locally (see `content/blog/_authoring-guide.md` for setup)
