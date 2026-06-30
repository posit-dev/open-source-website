---
title: "raghilda `v0.2`: crawl APIs, PostgreSQL, and more"
description: >
  raghilda v0.2 introduces a crawl and ingest API with caching and concurrency,
  a CloudflareCrawler for JavaScript-rendered sites, a PostgreSQL store backend,
  and NVIDIA NIM embeddings.
people:
  - Rich Iannone
  - Tomasz Kalinowski
date: '2026-07-01'
image: assets/raghilda-updated.png
image-alt: The raghilda logo with the `v0.2` version number
software:
  - raghilda
languages:
  - Python
topics:
  - Artificial Intelligence
tags:
  - raghilda
  - RAG
  - Python Packages
---

When we [introduced
raghilda](https://opensource.posit.co/blog/2026-04-14_rag-with-raghilda/)
in April, the package handled the core RAG workflow: read documents,
chunk them, embed them into a store, and retrieve relevant chunks at
query time. raghilda `v0.2` broadens that scope considerably. The
release adds a structured crawl and ingest API that replaces the manual
read-and-upsert loop with a pipeline built around caching, concurrency,
and composable crawlers (including a `CloudflareCrawler` that can index
JavaScript-rendered sites without running a local headless browser). It
also ships a PostgreSQL store backend and NVIDIA NIM embedding support.

This post walks through the major additions. The package's fundamentals
have not changed (stores, chunkers, retrievers, and the pattern for
connecting to chatlas all work as before), but the surface area for
building and maintaining stores in production has grown substantially.

## The crawl and ingest API

The largest change in `v0.2` is a new API for crawling sources and
ingesting them into a store. In `v0.1`, building a store meant calling
`read_as_markdown()` on individual URLs, chunking each result, and
upserting them one by one. That works for a handful of pages, but it
becomes unwieldy for larger collections, where you also want caching (to
avoid re-fetching unchanged content) and concurrency (to finish in
minutes rather than hours).

The new API introduces a clean separation between crawling and storage.
On the crawl side, a crawler object produces `MarkdownDocument` objects
from a defined scope. On the store side, `store.ingest()` consumes those
documents lazily, applies an optional preparation step (typically
chunking), and writes them to the store with configurable parallelism.
The pipeline looks like this:

```python
from raghilda.chunker import MarkdownChunker
from raghilda.crawl import CrawlScope, WebCrawler
from raghilda.embedding import EmbeddingOpenAI
from raghilda.store import DuckDBStore

crawler = WebCrawler(cache_dir=".cache/crawl", max_workers=4)

scope = CrawlScope(
    roots=["https://example.com/docs"],
    include_patterns=["https://example.com/docs/**"],
    depth=2,
)

documents = crawler.markdown_documents(scope)

store = DuckDBStore.create(
    location="raghilda.duckdb",
    embed=EmbeddingOpenAI(),
    overwrite=True,
)

summary = store.ingest(
    documents,
    prepare=MarkdownChunker(chunk_size=1000).chunk,
    max_workers=4,
)

print(summary)
```

    IngestSummary(inserted=142, replaced=0, skipped=0)

The `CrawlScope` dataclass defines the traversal policy: root URLs,
include/exclude patterns, depth limits, and page count caps. The crawler
handles the mechanics of fetching and converting pages to Markdown,
while the scope tells it where to go. This separation means you can
change the backend (swap `WebCrawler` for `CloudflareCrawler`, for
instance) without redefining the scope, and vice versa.

Three concrete crawlers ship with `v0.2`. `DirectoryCrawler` walks local
file trees and converts supported formats to Markdown. `WebCrawler`
fetches pages over HTTP using `requests` and converts them locally.
`CloudflareCrawler` delegates both fetching and rendering to
Cloudflare's Browser Rendering API (the right tool for sites that load
content through JavaScript). All three implement the same interface:
`origins()` to discover pages, `fetch_raw()` and `fetch_markdown()` for
single-page access, and `markdown_documents()` for the full pipeline.

Caching is built into the crawler layer. When you pass `cache_dir=True`
(or an explicit path), each crawler stores fetched content and converted
Markdown in a flat directory of files with metadata sidecars. On
subsequent runs, cached entries are reused if they are still fresh. For
`WebCrawler` and `CloudflareCrawler`, freshness is controlled by
`cache_stale_after=`, a `timedelta` that defines how long a cached entry
remains valid. This makes interrupted workflows resumable without any
explicit checkpoint logic: rerun the script and the cache supplies
everything that was already fetched, while only new or stale pages
trigger network requests.

Concurrency operates on both sides of this boundary independently. The
crawler can fetch and convert pages in parallel (controlled by
`max_workers=` on the crawler constructor), and `store.ingest()` can
write to the store concurrently (controlled by its own `max_workers=`
argument). For `WebCrawler`, the breadth-first frontier is explored
concurrently while preserving stable output order, so results come back
in a consistent sequence regardless of which pages respond first.

## `CloudflareCrawler`

The `CloudflareCrawler` moves the work of a crawl off the local machine.
Instead of fetching pages and converting them to Markdown with local
processes, it hands both jobs to Cloudflare's Browser Rendering API, so
a long crawl over a large site runs on Cloudflare's distributed
infrastructure rather than competing for local CPU and bandwidth. For
collections large enough that concurrent local requests become the
bottleneck, this is the primary reason to reach for it: the slow,
sustained part of building a store happens remotely, and what returns is
ready-to-chunk Markdown. The same arrangement resolves a problem that
defeats a plain HTTP fetch, because the API renders each page in a real
browser, executing JavaScript and waiting for the DOM to settle before
extracting content. Sites built with React, Vue, or Angular, which an
ordinary request reduces to an empty shell, are therefore handled
without extra configuration or a locally installed headless browser.

The usage looks almost identical to `WebCrawler`, because both share the
same crawl interface. The key difference is that the constructor takes
Cloudflare credentials instead of an HTTP session, and Cloudflare's
infrastructure handles the rendering remotely (so there is no need to
install Playwright, Selenium, or any other local headless browser):

```python
import os
from raghilda.crawl import CloudflareCrawler, CrawlScope

crawler = CloudflareCrawler(
    account_id=os.environ["CLOUDFLARE_ACCOUNT_ID"],
    api_token=os.environ["CLOUDFLARE_API_TOKEN"],
    cache_dir=True,
    render=True,
    max_workers=4,
)

scope = CrawlScope(
    roots=["https://my-spa-docs.example.com/"],
    depth=2,
    include_patterns=["https://my-spa-docs.example.com/**"],
    limit=500,
)

documents = crawler.markdown_documents(scope)
```

Iterating the result performs the crawl lazily, yielding one
`MarkdownDocument` per page. Each document exposes the page's `origin`
alongside its rendered Markdown `content`, so a quick pass confirms that
the JavaScript-rendered pages came back with real text rather than the
empty shells a plain HTTP fetch would have produced:

```python
for doc in documents:
    print(doc.origin, f"({len(doc.content):,} chars)")
```

    https://my-spa-docs.example.com/ (3,214 chars)
    https://my-spa-docs.example.com/guide/install (5,902 chars)
    https://my-spa-docs.example.com/guide/config (8,477 chars)
    https://my-spa-docs.example.com/api/reference (12,043 chars)

The `render=True` default tells Cloudflare to execute JavaScript before
extracting content. For server-rendered sites where JavaScript execution
is unnecessary, setting `render=False` reduces crawl time and API usage.
The `source=` parameter controls how pages are discovered: `"all"` (the
default) combines multiple discovery methods, `"sitemap"` reads from the
site's `sitemap.xml`, `"crawl"` follows links from the rendered DOM, and
`"urls"` processes only the explicitly provided roots.

For stores that need regular updates, the `modified_since=` parameter
restricts the crawl to pages modified after a given Unix timestamp,
keeping refresh jobs lightweight. Combined with the crawl cache and the
store's own deduplication (identical documents are not re-embedded), an
incremental update script can run daily without redundant work:

```python
import time
from datetime import timedelta

one_week_ago = int(time.time()) - (7 * 24 * 60 * 60)

crawler = CloudflareCrawler(
    account_id=os.environ["CLOUDFLARE_ACCOUNT_ID"],
    api_token=os.environ["CLOUDFLARE_API_TOKEN"],
    cache_dir=True,
    cache_stale_after=timedelta(days=1),
    modified_since=one_week_ago,
)
```

The tradeoff is cost: `CloudflareCrawler` requires a Cloudflare account
with Browser Rendering access. For static HTML sites where a plain HTTP
fetch returns the full content, `WebCrawler` remains the simpler and
free option. Both crawlers share the same interface, so switching
between them requires only a constructor change.

## PostgreSQL store

raghilda `v0.1` shipped with three store backends: DuckDB (local,
zero-config), ChromaDB, and OpenAI Vector Stores. `v0.2` adds
`PostgreSQLStore`, backed by `psycopg2` and `pgvector`. This is the
natural choice for production deployments where the store needs to be
shared across services, or where you already have PostgreSQL
infrastructure.

```python
from raghilda.store import PostgreSQLStore
from raghilda.embedding import EmbeddingOpenAI

store = PostgreSQLStore.create(
    connection="postgresql://user:pass@localhost:5432/mydb",
    embed=EmbeddingOpenAI(),
    name="docs_store",
    overwrite=True,
)
```

The store supports full-text search via PostgreSQL's native
`tsvector`/`tsquery` with a pre-computed column and GIN index, vector
similarity search via pgvector with HNSW indexes (supporting cosine, L2,
and inner product distance metrics), and combined retrieval that merges
both result sets with deoverlap support.

Retrieval uses the same interface as every other backend: a single
`retrieve()` call returns a ranked list of chunks, each carrying its
similarity score under `metrics` and its heading-hierarchy `context`.
Running a query against a store populated with the raghilda
documentation returns the most relevant chunks first:

```python
results = store.retrieve("How are vector indexes configured?", top_k=2)

for r in results:
    print(f"Score: {r.metrics[0].value:.4f}")
    print(r.context)
    print(r.text)
    print("---")
```

    Score: 0.5142
    # PostgreSQL store
    Vector similarity search runs through pgvector with HNSW indexes,
    supporting cosine, L2, and inner product distance metrics. Call
    build_index() after ingestion to create them.
    ---
    Score: 0.4417
    # PostgreSQL store > Combined retrieval
    Combined retrieval merges the vector and full-text result sets and
    applies deoverlap to drop redundant overlapping chunks, returning a
    single ranked list from one retrieve() call.
    ---

Attributes work as expected: scalar types map to columns, struct types
map to JSONB, and attribute filters can query into JSONB fields using
the `->>` operator. The `build_index()` method creates HNSW indexes
after ingestion, and the `vss_index=` parameter on `create()` controls
the default index type.

Connection strings are accepted directly in `create()` and `connect()`,
so you can point the store at any PostgreSQL instance with pgvector
installed. If the pgvector extension is missing, the store raises an
informative error rather than failing cryptically on the first vector
operation.

## NVIDIA NIM embeddings

The embedding layer gains a new provider: `EmbeddingNVIDIA`, which
connects to NVIDIA's OpenAI-compatible embedding API. The default model
is `nvidia/llama-nemotron-embed-1b-v2`, a compact embedding model
suitable for retrieval workloads. The provider reads its API key from
the `NVIDIA_API_KEY` environment variable.

```python
from raghilda.embedding import EmbeddingNVIDIA

embedding = EmbeddingNVIDIA()
```

One notable feature of NVIDIA's embedding API is differentiated input
types: queries and documents are embedded with different prefixes
(`"query"` and `"passage"`), which can improve retrieval quality for
asymmetric search where the query is short and the documents are long.
raghilda handles this distinction automatically when the store calls the
embedding provider during ingestion and retrieval.

The provider includes built-in rate limit handling with exponential
backoff. NVIDIA's 429 responses carry no `Retry-After` header or rate
limit metadata, so backoff is the only viable strategy. For users who
want to keep embedding computation entirely local, NVIDIA NIM can also
be self-hosted, in which case you point the provider at your local
endpoint with a `base_url=` override.

## Improved DuckDB error messages

A smaller but practical improvement: `DuckDBStore` now raises clear,
actionable errors when BM25 retrieval is attempted before the index has
been built, or after writes have made the index stale. Previously, this
produced a cryptic `CatalogException` from DuckDB about a missing
`match_bm25` function. The new message tells you exactly what to do:

    RuntimeError: DuckDBStore retrieval requires a current BM25 index.
    Call `store.build_index("bm25")` after inserting or updating documents
    and before calling `retrieve_bm25()` or `retrieve()`.

The store now tracks BM25 freshness internally: the index is marked
stale after any `upsert()` call and marked current after
`build_index("bm25")`. This tracking happens off the retrieval hot path,
so there is no per-query overhead. HNSW indexes are unaffected because
DuckDB maintains them across writes automatically.

## Why even use raghilda?

raghilda is a retrieval library, not an orchestration framework. Larger
projects like LangChain and LlamaIndex offer composable retrieval
components too, but they also ship agent runtimes, chain abstractions,
prompt management, and memory systems. If all you need is the retrieval
pipeline (crawl, chunk, embed, store, retrieve), raghilda gives you that
without the surrounding framework. The API surface is small: plain
dataclasses, iterators, and direct function calls. There are fewer
layers of indirection between your code and the underlying operations,
which makes the pipeline easier to debug and reason about.

raghilda `v0.2` makes that focused scope practical at scale. The crawl
API adds caching and concurrency while keeping each step a separate,
inspectable call. The storage layer lets you start with a local DuckDB
file and move to PostgreSQL or OpenAI Vector Stores later without
changing retrieval code. And every backend provides hybrid retrieval
(semantic search, BM25, and attribute filtering combined in a single
`retrieve()` call) out of the box, without assembling separate retriever
classes or configuring a pipeline graph.

## Getting started

raghilda `v0.2` is available now on PyPI (`pip install raghilda`). The
[raghilda documentation site](https://posit-dev.github.io/raghilda/)
covers all of the features described here in more detail. The [Getting
Started](https://posit-dev.github.io/raghilda/user-guide/getting-started.html)
guide walks through building a store from scratch, and the [Crawling and
Ingestion](https://posit-dev.github.io/raghilda/user-guide/crawling-and-ingestion.html)
guide covers the new crawl API in depth. A dedicated
[CloudflareCrawler](https://posit-dev.github.io/raghilda/user-guide/cloudflare-crawler.html)
guide explains browser rendering, page discovery, caching, and
incremental updates. The [GitHub
repository](https://github.com/posit-dev/raghilda) has the source, issue
tracker, and full changelog. If you run into problems or have feature
requests, open an issue there.
