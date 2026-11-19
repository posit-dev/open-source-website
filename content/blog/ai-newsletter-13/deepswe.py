# Derives the DeepSWE 1.1 (Python subset, 34 tasks) harness comparison from
# runs made with assistant-evals' `run_deepswe.sh`. Run from a checkout of
# assistant-evals that has the (untracked) logs locally:
#   .venv/bin/python path/to/deepswe.py path/to/data/deepswe.csv
# The Posit Assistant + Claude run was interrupted and completed with
# `inspect eval-retry`; the retry log holds all 34 samples.
import csv
import sys
from collections import Counter
from pathlib import Path

from inspect_ai.log import read_eval_log
from pa_eval.cost import run_cost
from pa_eval.pricing import load_pricing

LOGS = Path("logs/deepswe-python")
RUNS = [
    ("Posit Assistant", "Claude Sonnet 5.5", "pa-claude/2026-10-27T21-45-56-00-00_datacurve-deep-swe-1-1_nqdiwdT9ABNcUJuv3Rka6P.eval"),
    ("Claude Code", "Claude Sonnet 5.5", "claude-code/2026-10-27T20-59-54-00-00_datacurve-deep-swe-1-1_NgTtewjGpPkqegmrtU2c5U.eval"),
    ("Posit Assistant", "GPT 6.1 Sol", "pa-gpt/2026-10-27T20-59-30-00-00_datacurve-deep-swe-1-1_EK3caREG4qxJUpKSydau6u.eval"),
    ("Codex", "GPT 6.1 Sol", "codex/2026-10-27T20-59-49-00-00_datacurve-deep-swe-1-1_cCDEqLp68cKdt53zgXch9z.eval"),
]

pricing = load_pricing()
rows = []
for harness, model, log_file in RUNS:
    path = str(LOGS / log_file)
    log = read_eval_log(path)
    assert log.status == "success" and len(log.samples) == 34, path
    grades = Counter(s.scores["harbor_scorer"].value for s in log.samples)
    rows.append({
        "harness": harness,
        "model": model,
        "score": log.results.scores[0].metrics["accuracy"].value,
        "correct": grades[1.0],
        "incorrect": grades[0.0],
        "cost": run_cost(path, pricing),
    })

with open(sys.argv[1], "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
