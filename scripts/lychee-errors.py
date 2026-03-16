#!/usr/bin/env python3
"""
Generate a markdown table of lychee errors grouped by domain.

Usage:
    scripts/lychee-errors.py content/blog/_lychee/ai.json > content/blog/_lychee/ai-errors.md
    scripts/lychee-errors.py content/blog/_lychee/ai.json -o content/blog/_lychee/ai-errors.md
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


def extract_domain(url: str) -> str:
    """Extract domain from URL."""
    match = re.match(r'https?://([^/]+)', url)
    return match.group(1) if match else url


def get_status_code(status: dict) -> str:
    """Extract status code from lychee status object."""
    code = status.get('code')
    if code:
        return str(code)
    # For errors without a code, extract from text
    text = status.get('text', '')
    if 'Timeout' in text:
        return 'timeout'
    if 'Network error' in text:
        return 'network'
    return ''


def print_summary(data: dict) -> None:
    """Print summary stats to stderr."""
    print(f"Total: {data.get('total', 0)}", file=sys.stderr)
    print(f"  Successful: {data.get('successful', 0)}", file=sys.stderr)
    print(f"  Errors: {data.get('errors', 0)}", file=sys.stderr)
    print(f"  Excluded: {data.get('excludes', 0)}", file=sys.stderr)


def generate_table(data: dict, exclude_localhost: bool = False) -> str:
    """Generate markdown table from lychee JSON data."""
    # Group errors by URL
    url_info = defaultdict(lambda: {'posts': [], 'domain': '', 'status': ''})
    localhost_count = 0

    error_map = data.get('error_map', {})
    for file_path, errors in error_map.items():
        for error in errors:
            url = error.get('url', '')
            status = get_status_code(error.get('status', {}))

            if url.startswith('http://localhost'):
                localhost_count += 1
                if exclude_localhost:
                    continue

            domain = extract_domain(url)
            url_info[url]['domain'] = domain
            url_info[url]['status'] = status
            if file_path not in url_info[url]['posts']:
                url_info[url]['posts'].append(file_path)

    if localhost_count > 0:
        print(f"  Localhost: {localhost_count}", file=sys.stderr)

    if not url_info:
        return "No errors found.\n"

    # Sort by domain, then URL
    sorted_urls = sorted(url_info.keys(), key=lambda u: (url_info[u]['domain'], u))

    # Build table
    lines = [
        "| Domain | Status | URL | Posts | Count |",
        "|--------|--------|-----|-------|-------|"
    ]

    for url in sorted_urls:
        info = url_info[url]
        domain = info['domain']
        status = info['status']
        posts = ', '.join(info['posts'])
        count = len(info['posts']) if len(info['posts']) > 1 else ''
        lines.append(f"| {domain} | {status} | {url} | {posts} | {count} |")

    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(
        description='Generate markdown table of lychee errors grouped by domain.'
    )
    parser.add_argument('json_file', help='Path to lychee JSON output file')
    parser.add_argument('-o', '--output', help='Output file (default: stdout)')
    parser.add_argument(
        '--exclude-localhost',
        action='store_true',
        help='Exclude localhost URLs from output'
    )

    args = parser.parse_args()

    if not Path(args.json_file).exists():
        print(f"Error: {args.json_file} not found", file=sys.stderr)
        sys.exit(1)

    with open(args.json_file) as f:
        data = json.load(f)

    print_summary(data)
    table = generate_table(data, args.exclude_localhost)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(table)
        print(f"Written to {args.output}", file=sys.stderr)
    else:
        print(table)


if __name__ == '__main__':
    main()
