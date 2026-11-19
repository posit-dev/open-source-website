---
title: slackr
image: page-1.png
resource_type: cheatsheet
by: community
date: '2021-03-01'
description: Send files, messages, R objects, and images to Slack directly from R.
download_url: slackr.pdf
people:
- Daniel M. Villarreal
thumbnails:
- page-1.png
languages:
- R
---

The slackr package lets R users post results and outputs directly to Slack channels, including
ggplot2 graphics, R objects saved as RData files, and plain text messages. It supports both
single-channel webhook bots and fully authenticated multi-channel bots.

## What's covered
- Installation – CRAN and development versions
- Setup – creating a Slack app and configuring OAuth scopes
- Single-channel bot setup – incoming webhook configuration
- Multi-channel bot setup – OAuth token and scope configuration
- Common functions – `ggslackr`, `save_slackr`, `slackr_bot`, `slackr_delete`, `slackr_msg`, `slackr_upload`
- Other utility functions – `auth_test`, `call_slack_api`, `slackr_channels`, `slackr_users`, `with_pagination`
- Vignettes – webhook, scoped bot, and usage guides
