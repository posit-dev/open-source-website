Input tokens for a single "Hi" turn with a clean HOME, following [posit-dev/assistant#2555](https://github.com/posit-dev/assistant/issues/2555). Run 2026-10-23 with pa built from posit-dev/assistant `main` at `3adfd8ce3`, Claude Code 2.1.309, and codex-cli 0.161.0.

```bash
# in /assistant
npm install && npm run build && npm run build -w @assistant/tui
codesign -s - -f packages/tui/dist/bin/pa   # unsigned builds get killed on launch

# in this folder
CAPTURE=1 bash token-profile.sh
python3 token-segments.py <Logs dir>/payloads ../data/token-profile.csv

# in the post folder
Rscript token-profile/plots.R
```

Changes from the 2026-09-28 scripts: `PA` points at the source build, the clean HOME reads the OpenAI key from `OPENAI_API_KEY` (the keychain helper fails under a different HOME), `token-segments.py` sends the `thinking-binding-controls-2026-08-01` beta that pa's payloads now need and can write a CSV, and pa's new `<environment_context>` block counts as environment context. Positron wasn't rerun.

| Tool | Model | Input tokens (billed) | 2026-09-28 |
|---|---|---|---|
| Assistant (TUI) | Opus 5.5 | 15,221 | 21,367 |
| Assistant (TUI) | GPT 6 Sol | 8,455 | 12,239 |
| `claude -p` | Opus 5.5 | 16,347 | 15,146 |
| `codex exec` | GPT 6 Sol | 11,997 | 12,096 |

| Section | pa / Opus 5.5 | pa / GPT 6 Sol | Claude Code / Opus 5.5 | Codex / GPT 6 Sol |
|---|---|---|---|---|
| System prompt | 5,342 | 3,573 | 2,113 | 3,703 |
| Tool definitions | 7,222 | 3,196 | 10,754 | 6,771 |
| Skill listing | 1,912 | 1,184 | 2,131 | 492 |
| Environment context | 603 | 397 | 399 | 183 |
| Per-turn reminders | 130 | 84 | 210 | — |
| Deferred tool names | — | — | 165 | — |
| Agent type listing | — | — | 563 | — |
| Modes, permissions, agents | — | — | — | 836 |
| Billing header | — | — | 43 | — |
| User message, framing | 12 | 21 | 12 | 12 |
| Total | 15,221 | 8,455 | 16,390 | 11,997 |

Section counts come from the token-counting endpoints, which match billed usage except for Claude Code (16,390 counted vs. 16,347 billed).
