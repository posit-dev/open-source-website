---
title: Using Git and GitHub with RStudio
image: page-1.png
resource_type: cheatsheet
by: community
date: '2022-01-01'
description: Version-control R projects with Git and collaborate via GitHub directly from the RStudio IDE.
download_url: git-github.pdf
people:
- Mouna Belaid
thumbnails:
- page-1.png
languages:
- R
source_files:
- file: git-github.pptx
  format: PowerPoint
translations:
- language: Spanish
  lang: es
  file: git-github_es.pdf
  updated: 2022-01
  people:
  - Anthony Romero-Cerdán
  source: git-github_es.pptx
- language: Vietnamese
  lang: vi
  file: git-github_vi.pdf
  updated: 2022-01
  people:
  - Le-Huynh Truc-Ly
  source: git-github_vi.pptx
---

This cheat sheet covers using Git and GitHub from within RStudio, starting from installation and initial configuration through to everyday version-control and collaboration workflows. It documents common Git commands alongside their RStudio equivalents.

## What's covered
- Requirements and setup – installing Git, registering a GitHub account
- Introduce yourself to Git – `git config --global user.name` and `user.email`
- Basics – `git init`, `git clone`, `git add`, `git commit`, `git status`, `git log`, `git diff`
- Remote repositories – `git remote add`, `git fetch`, `git pull`, `git push`
- Undoing changes – `git revert`, `git reset`, `git clean`
- Rewriting Git history – `git commit --amend`, `git rebase`, `git reflog`
- Git branches – creating, listing, and switching branches
