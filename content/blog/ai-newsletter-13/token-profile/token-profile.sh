#!/usr/bin/env bash
# Total input tokens (cached + uncached) for a single "Hi" turn, with a clean HOME.
# CAPTURE=1 also routes requests through mitmdump reverse proxies, saves the payloads,
# and checks them for user-level instructions, skills, and MCP servers.
set -euo pipefail

PROMPT="${PROMPT:-Hi}"
CAPTURE="${CAPTURE:-0}"
ASSISTANT_REPO="${ASSISTANT_REPO:-$HOME/Documents/rrr/assistant}"
# Built from source with `npm run build && npm run build -w @assistant/tui` in ASSISTANT_REPO.
PA="${PA:-$ASSISTANT_REPO/packages/tui/dist/bin/pa}"
OUT="$(mktemp -d)"
H="$OUT/home"
mkdir -p "$H/.posit/ai/auth" "$H/.codex" "$H/work"

# Credentials only: no instructions, skills, plugins, or MCP servers.
# `security` can't reach the login keychain with a different HOME, so read the OpenAI key from the environment.
jq '.providers.openai.apiKeyHelper = {command: "/bin/sh", args: ["-c", "printf %s \"$OPENAI_API_KEY\""]}' \
  ~/.posit/ai/providers.json > "$H/.posit/ai/providers.json"
cp ~/.posit/ai/auth/data.json "$H/.posit/ai/auth/"
cp ~/.codex/auth.json "$H/.codex/"
# Stand in for pa's built-in skills, which the compiled TUI never discovers (posit-dev/assistant#915).
mkdir -p "$H/.posit/assistant"
cp -R "$ASSISTANT_REPO/packages/core/skills" "$H/.posit/assistant/skills"
: "${ANTHROPIC_API_KEY:?Claude Code needs ANTHROPIC_API_KEY with a clean HOME}"
: "${OPENAI_API_KEY:?pa needs OPENAI_API_KEY with a clean HOME}"

claude_env=()
codex_args=()
if [ "$CAPTURE" = 1 ]; then
  mkdir -p "$OUT/payloads"
  cat > "$OUT/dump.py" <<'EOF'
import itertools, os
from mitmproxy import http

OUT = os.environ["PAYLOAD_DIR"]
TAG_FILE = os.environ["TAG_FILE"]
counter = itertools.count()

def save(suffix, content):
    tag = open(TAG_FILE).read().strip()
    with open(os.path.join(OUT, f"{tag}-{next(counter):03d}-{suffix}"), "wb") as f:
        f.write(content or b"")

def request(flow: http.HTTPFlow) -> None:
    if flow.request.method == "POST":
        save(flow.request.path.split("?")[0].strip("/").replace("/", "_"), flow.request.get_content(strict=False))

# Codex sends its turn over a WebSocket.
def websocket_message(flow: http.HTTPFlow) -> None:
    msg = flow.websocket.messages[-1]
    if msg.from_client:
        save("ws", msg.content)
EOF
  export PAYLOAD_DIR="$OUT/payloads" TAG_FILE="$OUT/tag"
  echo setup > "$TAG_FILE"
  uvx --from mitmproxy mitmdump -q --mode reverse:https://api.anthropic.com -p 8081 -s "$OUT/dump.py" > "$OUT/mitm-anthropic.log" 2>&1 &
  uvx --from mitmproxy mitmdump -q --mode reverse:https://api.openai.com -p 8082 -s "$OUT/dump.py" > "$OUT/mitm-openai.log" 2>&1 &
  trap 'kill $(jobs -p) 2>/dev/null' EXIT
  until nc -z 127.0.0.1 8081 2>/dev/null && nc -z 127.0.0.1 8082 2>/dev/null; do sleep 1; done

  jq '.providers.anthropic.baseUrl = "http://127.0.0.1:8081/v1" | .providers.openai.baseUrl = "http://127.0.0.1:8082/v1"' \
    "$H/.posit/ai/providers.json" > "$OUT/providers.json" && mv "$OUT/providers.json" "$H/.posit/ai/providers.json"
  # With a custom base URL, Claude Code otherwise sends every tool schema inline.
  claude_env=(ANTHROPIC_BASE_URL=http://127.0.0.1:8081 ENABLE_TOOL_SEARCH=true)
  # Codex ignores OPENAI_BASE_URL.
  codex_args=(-c 'openai_base_url="http://127.0.0.1:8082/v1"')
fi

tag() { [ "$CAPTURE" = 1 ] && echo "$1" > "$TAG_FILE" || true; }

# Sequential: concurrent pa runs race on the shared conversation index, and capture tags payloads by run.
cd "$H/work"
tag pa-opus; HOME="$H" "$PA" -vv -m anthropic/claude-opus-5-5 "$PROMPT" > "$OUT/pa-opus.log" 2>&1
tag pa-gpt; HOME="$H" "$PA" -vv -m openai/gpt-6-sol "$PROMPT" > "$OUT/pa-gpt.log" 2>&1
tag claude; env HOME="$H" "${claude_env[@]}" claude -p "$PROMPT" --model claude-opus-5-5 --output-format json > "$OUT/claude.json" 2>/dev/null
tag codex; HOME="$H" CODEX_HOME="$H/.codex" codex exec --json --skip-git-repo-check -m gpt-6-sol "${codex_args[@]}" "$PROMPT" < /dev/null > "$OUT/codex.jsonl" 2>/dev/null

pa_tokens() { grep -m1 -oE '"inputTokens": [0-9]+' "$1" | grep -oE '[0-9]+'; }

printf '%-28s %s\n' \
  "pa / Opus 5.5" "$(pa_tokens "$OUT/pa-opus.log")" \
  "pa / GPT 6 Sol" "$(pa_tokens "$OUT/pa-gpt.log")" \
  "claude -p / Opus 5.5" "$(jq '[.modelUsage[] | .inputTokens + .cacheReadInputTokens + .cacheCreationInputTokens] | add' "$OUT/claude.json")" \
  "codex exec / GPT 6 Sol" "$(jq -s 'map(select(.type == "turn.completed"))[0].usage.input_tokens' "$OUT/codex.jsonl")"

if [ "$CAPTURE" = 1 ]; then
  python3 - "$OUT/payloads" <<'EOF'
import glob, json, os, re, sys
from pathlib import Path

home = Path.home()
# Markers of the real (non-clean) user setup.
lines = set()
for f in ["CLAUDE.md", ".claude/CLAUDE.md", ".codex/AGENTS.md", ".posit/assistant/AGENTS.md", ".agents/AGENTS.md"]:
    p = home / f
    if p.exists():
        lines |= {l.strip() for l in p.read_text().splitlines() if len(l.strip()) > 40}
for p in (home / ".claude/projects").glob("*/memory/*.md"):
    lines |= {l.strip() for l in p.read_text().splitlines() if len(l.strip()) > 40}
names = set()
for d in [".claude/skills", ".codex/skills", ".agents/skills", ".posit/assistant/skills"]:
    names |= {p.name.removesuffix(".skill") for p in (home / d).glob("*") if not p.name.startswith(".")}
toml = home / ".codex/config.toml"
if toml.exists():
    names |= set(re.findall(r"^\[mcp_servers\.([\w-]+)\]", toml.read_text(), re.M))
cj = home / ".claude.json"
if cj.exists():
    names |= set(json.loads(cj.read_text()).get("mcpServers", {}))

by_tag = {}
for f in sorted(glob.glob(os.path.join(sys.argv[1], "*"))):
    by_tag.setdefault(os.path.basename(f).split("-0")[0], []).append(Path(f).read_text(errors="replace"))

for tag, bodies in by_tag.items():
    if tag == "setup":
        continue
    text = "\n".join(bodies)
    parsed = [json.loads(b) for b in bodies if b.strip()]
    tools = sorted({t.get("name") or t.get("type") for d in parsed for t in d.get("tools", [])})
    skills = set(re.findall(r"<name>([\w:-]+)</name>", text))
    for heading in ["skills are available", "### Available skills", "## Available Skills"]:
        i = text.find(heading)
        if i >= 0:
            skills |= set(re.findall(r"\\n- ([\w:.-]+): ", text[i:i + 30000]))
    skills = sorted(skills)
    leaked = sorted({n for n in names if re.search(rf"\b{re.escape(n)}\b", text)} | {l[:60] for l in lines if l in text.replace("\\n", "\n")})
    print(f"\n{tag}\n  tools: {', '.join(tools) or '(none top-level)'}\n  skills: {', '.join(skills)}\n  user-level matches: {', '.join(leaked) or 'none'}")
EOF
fi
echo "Logs: $OUT"
