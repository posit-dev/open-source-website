"""
Calculate contributor and issue stats for all four Python
type checker projects, combining across related repos.

Repos:
  Pyrefly:      facebook/pyrefly
  ty:           astral-sh/ty, astral-sh/ty-vscode,
                astral-sh/ruff (label:ty only)
  Basedpyright: detachhead/basedpyright
  Zuban:        zubanls/zuban, zubanls/vscode-zubanls
"""

import json
import subprocess

NINETY_DAYS_START = "2026-01-01"
NINETY_DAYS_END = "2026-03-31"

PROJECTS = {
    "Pyrefly": {
        "repos": [
            {"repo": "facebook/pyrefly"},
        ],
    },
    "ty": {
        "repos": [
            {"repo": "astral-sh/ty"},
            {"repo": "astral-sh/ty-vscode"},
            {"repo": "astral-sh/ruff", "label": "ty"},
        ],
    },
    "Basedpyright": {
        "repos": [
            {"repo": "detachhead/basedpyright"},
        ],
    },
    "Zuban": {
        "repos": [
            {"repo": "zubanls/zuban"},
            {"repo": "zubanls/vscode-zubanls"},
        ],
    },
}

# Date ranges for repos that might exceed the 1000-result
# search cap. Keyed by "repo:label" or just "repo".
SPLIT_RANGES = {
    "astral-sh/ruff:ty": [
        ("*", "2024-12-31"),
        ("2025-01-01", "2025-03-31"),
        ("2025-04-01", "2025-06-30"),
        ("2025-07-01", "2025-09-30"),
        ("2025-10-01", "2025-12-31"),
        ("2026-01-01", "2026-03-31"),
    ],
}


def graphql(query: str) -> dict:
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def search_all(query_str: str) -> list[dict]:
    """Paginate through GitHub search results via GraphQL."""
    nodes = []
    cursor = None
    page = 0
    total = 0
    while True:
        page += 1
        after = f', after: "{cursor}"' if cursor else ""
        q = f"""
        {{
          search(query: "{query_str}", type: ISSUE, first: 100{after}) {{
            issueCount
            pageInfo {{ hasNextPage endCursor }}
            nodes {{
              ... on Issue {{ author {{ login }} createdAt closedAt }}
              ... on PullRequest {{ author {{ login }} createdAt closedAt }}
            }}
          }}
        }}
        """
        data = graphql(q)
        search = data["data"]["search"]
        nodes.extend(search["nodes"])
        total = search["issueCount"]

        if page == 1:
            print(f"    Total matching: {total}")
        if page % 5 == 0:
            print(f"    Page {page}: {len(nodes)} fetched so far")

        if not search["pageInfo"]["hasNextPage"]:
            break
        cursor = search["pageInfo"]["endCursor"]

    if len(nodes) < total:
        print(
            f"    WARNING: only fetched {len(nodes)}/{total} "
            f"(hit 1000 cap, split this range further)"
        )
    print(f"    Done: {len(nodes)} across {page} pages")
    return nodes


def get_authors(query_str: str) -> set[str]:
    nodes = search_all(query_str)
    return {
        n["author"]["login"] for n in nodes if n.get("author")
    }


def repo_key(repo_cfg: dict) -> str:
    key = repo_cfg["repo"]
    if "label" in repo_cfg:
        key += f":{repo_cfg['label']}"
    return key


def base_query(repo_cfg: dict, extra: str = "") -> str:
    q = f"repo:{repo_cfg['repo']}"
    if "label" in repo_cfg:
        q += f" label:{repo_cfg['label']}"
    if extra:
        q += f" {extra}"
    return q


def collect_pr_authors(repo_cfg: dict) -> set[str]:
    """Collect unique PR authors, splitting by date if needed."""
    key = repo_key(repo_cfg)
    ranges = SPLIT_RANGES.get(key)
    if not ranges:
        print(f"  {key}: PRs (all time)")
        return get_authors(base_query(repo_cfg, "is:pr"))

    authors = set()
    for i, (start, end) in enumerate(ranges):
        created = (
            f"created:<={end}"
            if start == "*"
            else f"created:{start}..{end}"
        )
        print(f"  {key}: PRs ({start} to {end})")
        batch = get_authors(
            base_query(repo_cfg, f"is:pr {created}")
        )
        print(f"    Unique in range: {len(batch)}")
        authors |= batch
    return authors


def collect_project_stats(name: str, config: dict) -> dict:
    print(f"\n{'=' * 60}")
    print(f" {name}")
    print(f"{'=' * 60}")

    # Contributors (unique PR authors across all repos)
    all_authors = set()
    for repo_cfg in config["repos"]:
        authors = collect_pr_authors(repo_cfg)
        key = repo_key(repo_cfg)
        print(f"    {key} unique authors: {len(authors)}")
        all_authors |= authors
    print(f"  -> Combined unique contributors: {len(all_authors)}")

    # Issues opened in 90-day window
    total_opened = 0
    print(f"\n  Issues opened ({NINETY_DAYS_START}..{NINETY_DAYS_END}):")
    for repo_cfg in config["repos"]:
        key = repo_key(repo_cfg)
        print(f"  {key}:")
        nodes = search_all(
            base_query(
                repo_cfg,
                f"is:issue created:{NINETY_DAYS_START}..{NINETY_DAYS_END}",
            )
        )
        total_opened += len(nodes)
    print(f"  -> Total opened: {total_opened}")

    # Issues closed in 90-day window
    total_closed = 0
    print(f"\n  Issues closed ({NINETY_DAYS_START}..{NINETY_DAYS_END}):")
    for repo_cfg in config["repos"]:
        key = repo_key(repo_cfg)
        print(f"  {key}:")
        nodes = search_all(
            base_query(
                repo_cfg,
                f"is:issue closed:{NINETY_DAYS_START}..{NINETY_DAYS_END}",
            )
        )
        total_closed += len(nodes)
    print(f"  -> Total closed: {total_closed}")

    return {
        "contributors": len(all_authors),
        "issues_opened": total_opened,
        "issues_closed": total_closed,
    }


def main():
    print("Python type checker ecosystem stats")
    print(
        f"90-day window: {NINETY_DAYS_START} to {NINETY_DAYS_END}"
    )

    results = {}
    for name, config in PROJECTS.items():
        results[name] = collect_project_stats(name, config)

    # Summary table
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    header = f"{'':20} {'Contributors':>14} {'Opened (90d)':>14} {'Closed (90d)':>14}"
    print(header)
    print("-" * len(header))
    for name, stats in results.items():
        print(
            f"{name:20} {stats['contributors']:>14} "
            f"{stats['issues_opened']:>14} "
            f"{stats['issues_closed']:>14}"
        )


if __name__ == "__main__":
    main()
