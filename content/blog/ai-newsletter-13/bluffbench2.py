# Rederives the bluffbench2 harness comparison from posit-dev/assistant-evals#2.
# Run from a checkout of assistant-evals on the `bluffbench2` branch, which has
# the Claude Code and Codex logs locally (they're untracked):
#   .venv/bin/python path/to/bluffbench2.py path/to/data/bluffbench2.csv
import csv
import sys
from collections import Counter
from pathlib import Path

from inspect_ai.log import read_eval_log
from pa_eval.cost import run_cost
from pa_eval.pricing import load_pricing

RUNS = [
    ("Posit Assistant", "Claude Sonnet 5.5", "docs/bluffbench2/anthropic-claude-sonnet-5-5-medium/logs/logs"),
    ("Claude Code + Console", "Claude Sonnet 5.5", "claude_code/logs/bluffbench2/claude-code-sonnet-5-5-medium-console"),
    ("Claude Code, shell only", "Claude Sonnet 5.5", "claude_code/logs/bluffbench2/claude-code-sonnet-5-5-medium-shell"),
    ("Posit Assistant", "GPT 6.1 Sol", "docs/bluffbench2/openai-gpt-6.1-sol-medium/logs/logs"),
    ("Codex + Console", "GPT 6.1 Sol", "claude_code/logs/bluffbench2/codex-gpt-6.1-sol-medium-console"),
    ("Codex, shell only", "GPT 6.1 Sol", "claude_code/logs/bluffbench2/codex-gpt-6.1-sol-medium-shell"),
]

pricing = load_pricing()
rows = []
for harness, model, log_dir in RUNS:
    path = next(Path(log_dir).glob("*.eval"))
    log = read_eval_log(str(path))
    grades = Counter(s.scores["bluff2_scorer"].answer for s in log.samples)
    rows.append({
        "harness": harness,
        "model": model,
        "score": log.results.scores[0].metrics["mean"].value,
        "correct": grades["C"],
        "partial": grades["P"],
        "incorrect": grades["I"],
        "cost": run_cost(str(path), pricing),
    })

with open(sys.argv[1], "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
