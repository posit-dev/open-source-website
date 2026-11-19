"""Attribute input tokens to payload sections by removing each one and re-counting.

Usage:
  python3 token-segments.py <payloads dir from `CAPTURE=1 token-profile.sh`> [out.csv]
  python3 token-segments.py <Positron raw-http *-request.http log> [out.csv]
"""

import copy
import csv
import glob
import json
import os
import re
import sys
import urllib.request

ANTHROPIC_BETAS = "mid-conversation-system-2026-04-07,thinking-binding-controls-2026-08-01,advanced-tool-use-2025-11-20,context-management-2025-06-27"


def main():
    arg = sys.argv[1]
    loaded = load_positron(arg) if arg.endswith(".http") else load(arg)
    out = []
    for tag, (kind, payload, segments) in loaded.items():
        full = count(kind, payload)
        rows = [(name, full - count(kind, drop(copy.deepcopy(payload)))) for name, drop in segments]
        rows.append(("other (user message, framing)", full - sum(n for _, n in rows)))
        print(f"\n{tag}: {full:,} total")
        for name, n in rows:
            print(f"  {name:<32} {n:>7,}  {n / full:>4.0%}")
            out.append({"tag": tag, "section": name, "tokens": n})
    if len(sys.argv) > 2:
        with open(sys.argv[2], "w", newline="") as f:
            w = csv.DictWriter(f, ["tag", "section", "tokens"])
            w.writeheader()
            w.writerows(out)


def load(payloads):
    read = lambda pattern: json.load(open(glob.glob(os.path.join(payloads, pattern))[0]))
    out = {}

    for tag, pattern, kind in [("pa-opus", "pa-opus-*", "anthropic"), ("pa-gpt", "pa-gpt-*", "openai")]:
        p = read(pattern)
        if kind == "anthropic":
            p = {k: p[k] for k in ["model", "system", "messages", "tools", "thinking"]}
            sys_text = lambda p: p["system"][0]
            user_blocks = lambda p: p["messages"][0]["content"]
        else:
            p = {k: p[k] for k in ["model", "input", "tools"]}
            sys_text = lambda p: p["input"][0]["content"][0]
            user_blocks = lambda p: [b for m in p["input"][1:] for b in m["content"]]
        out[tag] = (kind, p, [
            ("system prompt", keep_only(sys_text, r"## Available Skills.*")),
            ("tool definitions", drop_keys("tools", "tool_choice")),
            ("skill listing", cut(sys_text, r"## Available Skills.*")),
            ("environment context", lambda p: drop_blocks(user_blocks, "<environment_context>")(drop_blocks(user_blocks, "<workspace-context>")(p))),
            ("per-turn reminders", drop_blocks(user_blocks, "<system-reminder>")),
        ])

    c = read("claude-*")
    c = {k: c[k] for k in ["model", "system", "tools", "thinking", "context_management", "output_config"]} | {
        "messages": [{k: v for k, v in m.items() if k != "output_config"} for m in c["messages"]]
    }
    env_msg = lambda p: p["messages"][1]["content"][0]
    core_sys = lambda p: p["system"]
    out["claude"] = ("anthropic", c, [
        ("system prompt", lambda p: {**p, "system": p["system"][:1]}),
        # Tool schemas as sent: most tools are deferred behind ToolSearch.
        ("tool definitions", drop_keys("tools")),
        ("skill listing", cut(env_msg, r"The following skills are available.*")),
        ("environment context", cut(env_msg, r"# Environment.*?(?=The following deferred tools)")),
        ("deferred tool names", cut(env_msg, r"The following deferred tools.*?(?=Available agent types)")),
        ("agent type listing", cut(env_msg, r"Available agent types.*?(?=The following skills)")),
        ("per-turn reminders", lambda p: {**p, "messages": [{**p["messages"][0], "content": p["messages"][0]["content"][1:]}] + p["messages"][1:]}),
        ("billing header", lambda p: {**p, "system": p["system"][1:]}),
    ])

    # Codex prewarms the base instructions and tools, then sends the turn with previous_response_id.
    prewarm, turn = [json.load(open(f)) for f in sorted(glob.glob(os.path.join(payloads, "codex-*")))]
    x = {"model": prewarm["model"], "input": [i for i in prewarm["input"] if i.get("content") or i.get("tools")] + turn["input"]}
    item_with = lambda marker: lambda p: [i for i in p["input"] if marker in json.dumps(i)]
    out["codex"] = ("openai", x, [
        ("system prompt", drop_items(lambda i: "You are Codex" in json.dumps(i))),
        ("tool definitions", drop_items(lambda i: i.get("type") == "additional_tools")),
        ("skill listing", drop_content(item_with("<skills_instructions>"), "<skills_instructions>")),
        ("environment context", drop_items(lambda i: "<environment_context>" in json.dumps(i))),
        ("modes, permissions, agents", lambda p: drop_items(lambda i: "<multi_agent" in json.dumps(i))(
            drop_content(item_with("<permissions instructions>"), "<permissions instructions>", "<collaboration_mode>")(p))),
    ])
    return out


def load_positron(path):
    p = json.loads(open(path).read().split("\n\n", 1)[1])
    if "input" in p:
        kind = "openai"
        p = {k: p[k] for k in ["model", "input", "tools"]}
        sys_text = lambda p: p["input"][0]["content"][0]
        blocks = lambda p: [b for m in p["input"][1:] for b in m["content"]]
    else:
        kind = "anthropic"
        p = {k: p[k] for k in ["model", "system", "messages", "tools", "thinking"]}
        sys_text = lambda p: p["system"][0]
        blocks = lambda p: p["messages"][0]["content"]
    workspace = lambda p: next(b for b in blocks(p) if b["text"].startswith("<workspace-context>"))
    drop_memory = cut(workspace, r"<memory\b.*?</memory>\s*")
    drop_project_skills = cut(sys_text, r"<skill>(?:(?!</skill>).)*<location>project</location>\s*</skill>\s*")
    # Project config (AGENTS.md, project skills) is measured, then stripped for the comparable breakdown.
    clean = drop_project_skills(drop_memory(copy.deepcopy(p)))
    return {
        "positron (as sent)": (kind, p, [
            ("project memory (AGENTS.md)", drop_memory),
            ("project skills", drop_project_skills),
        ]),
        "positron (without project config)": (kind, clean, [
            ("system prompt", keep_only(sys_text, r"## Available Skills.*")),
            ("tool definitions", drop_keys("tools", "tool_choice")),
            ("skill listing", cut(sys_text, r"## Available Skills.*")),
            ("workspace context", drop_blocks(blocks, "<workspace-context>")),
            ("open files, date, R session", drop_blocks(blocks, "<environment_context>")),
            ("per-turn reminders", drop_blocks(blocks, "<system-reminder>")),
        ]),
    }


def keep_only(get, pattern):
    """Remove a text block except for the part matching `pattern`."""
    def f(p):
        block = get(p)
        m = re.search(pattern, block["text"], re.S)
        block["text"] = m.group(0) if m else " "
        return p
    return f


def cut(get, pattern):
    def f(p):
        block = get(p)
        block["text"] = re.sub(pattern, "", block["text"], flags=re.S) or " "
        return p
    return f


def drop_keys(*keys):
    return lambda p: {k: v for k, v in p.items() if k not in keys}


def drop_blocks(get_blocks, marker):
    def f(p):
        for msgs in (p.get("messages") or [], p.get("input") or []):
            for m in msgs:
                if isinstance(m.get("content"), list):
                    m["content"] = [b for b in m["content"] if not b.get("text", "").startswith(marker)] or [{"type": m["content"][0]["type"], "text": " "}]
        return p
    return f


def drop_items(pred):
    return lambda p: {**p, "input": [i for i in p["input"] if not pred(i)]}


def drop_content(get_items, *markers):
    def f(p):
        for item in get_items(p):
            item["content"] = [b for b in item["content"] if not any(b.get("text", "").startswith(m) for m in markers)]
        p["input"] = [i for i in p["input"] if i.get("content") != []]
        return p
    return f


def count(kind, payload):
    if kind == "anthropic":
        url, headers = "https://api.anthropic.com/v1/messages/count_tokens", {
            "x-api-key": os.environ["ANTHROPIC_API_KEY"],
            "anthropic-version": "2023-06-01",
            "anthropic-beta": ANTHROPIC_BETAS,
        }
    else:
        url, headers = "https://api.openai.com/v1/responses/input_tokens", {
            "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
        }
    req = urllib.request.Request(url, json.dumps(payload).encode(), {**headers, "content-type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(req))["input_tokens"]
    except urllib.error.HTTPError as e:
        sys.exit(f"{url}: {e.read().decode()}")


main()
