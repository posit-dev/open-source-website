(function () {
  'use strict';

  function debounce(fn, ms) {
    let id;
    return function (...args) {
      clearTimeout(id);
      id = setTimeout(() => fn.apply(this, args), ms);
    };
  }

  function toRegex(pattern) {
    try { return new RegExp(pattern); } catch (_) { return null; }
  }

  function normalize(str) {
    return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[-_]/g, ' ').toLowerCase();
  }

  // Decode HTML entities produced by Hugo's html/template escaping in partials
  const _decodeEl = document.createElement('textarea');
  function decodeHTML(str) {
    if (!str || !str.includes('&')) return str;
    _decodeEl.innerHTML = str;
    return _decodeEl.value;
  }

  // Field qualifier → pre-computed key on each item (set during _hydrate)
  const TEXT_FIELDS = {
    title:       '_qTitle',
    author:      '_qAuthor',
    description: '_qDescription',
    topic:       '_qTopic',
    tag:         '_qTag',
    software:    '_qSoftware',
    language:    '_qLanguage',
    location:    '_qLocation',
    source:      '_qSource',
  };

  const NUMERIC_FIELDS = {
    stars:    item => item.stars || 0,
    views:    item => item.views || 0,
    duration: item => (item.duration || 0) / 60,
  };

  const DATE_FIELDS = {
    date: item => item._dateTs,
  };

  // ---- Tokenizer ----
  // Converts raw search string into flat token array.
  // Token types: 'term', 'field', 'and', 'or', 'not', 'lparen', 'rparen'

  // Separate ( and ) from adjacent text, respecting quoted strings.
  // Turns "(author:"jane doe")" into "( author:"jane doe" )"
  // so the main regex always sees parens as standalone tokens.
  function separateParens(raw) {
    let out = '';
    let inQuote = false;
    for (let i = 0; i < raw.length; i++) {
      const ch = raw[i];
      if (ch === '"') {
        inQuote = !inQuote;
        out += ch;
      } else if (!inQuote && (ch === '(' || ch === ')')) {
        out += ' ' + ch + ' ';
      } else {
        out += ch;
      }
    }
    return out;
  }

  function tokenize(raw) {
    raw = separateParens(raw);
    const tokens = [];
    // Groups: 1=neg, 2=field, 3=op, 4=quoted, 5=dateRange1, 6=dateRange2,
    //         7=date, 8=numRange1, 9=numRange2, 10=number, 11=bareword,
    //         12=phrase, 13=word
    const re = /(-?)(\w+):(>=?|<=?)?(?:"([^"]*)"|(\d{4}-\d{2}-\d{2})\.\.(\d{4}-\d{2}-\d{2})|(\d{4}-\d{2}-\d{2})|(\d+(?:\.\d+)?)\.\.(\d+(?:\.\d+)?)|(\d+(?:\.\d+)?)|(\S+))|"([^"]*)"|(\S+)/g;
    let m;
    while ((m = re.exec(raw)) !== null) {
      if (m[2]) {
        const neg = m[1] === '-';
        const field = m[2].toLowerCase();
        const op = m[3] || '';

        if (neg) tokens.push({ type: 'not' });

        if (m[4] !== undefined) {
          // field:"quoted value" — supports regex syntax
          if (TEXT_FIELDS[field]) {
            const val = normalize(m[4]);
            tokens.push({ type: 'field', kind: 'text', field, value: val, regex: toRegex(val) });
          }
        } else if (m[5] && m[6]) {
          // field:date..date
          if (DATE_FIELDS[field]) {
            tokens.push({ type: 'field', kind: 'date', field, op: '..', low: new Date(m[5]).getTime(), high: new Date(m[6]).getTime() + 86400000 - 1 });
          }
        } else if (m[7]) {
          // field:date
          if (DATE_FIELDS[field]) {
            const ts = new Date(m[7]).getTime();
            const effectiveOp = op || '>=';
            const value = effectiveOp === '<=' ? ts + 86400000 - 1 : ts;
            tokens.push({ type: 'field', kind: 'date', field, op: effectiveOp, value });
          }
        } else if (m[8] !== undefined && m[9] !== undefined) {
          // field:num..num
          if (NUMERIC_FIELDS[field]) {
            tokens.push({ type: 'field', kind: 'numeric', field, op: '..', low: parseFloat(m[8]), high: parseFloat(m[9]) });
          }
        } else if (m[10] !== undefined) {
          // field:number
          if (NUMERIC_FIELDS[field]) {
            tokens.push({ type: 'field', kind: 'numeric', field, op: op || '==', value: parseFloat(m[10]) });
          } else if (TEXT_FIELDS[field]) {
            tokens.push({ type: 'field', kind: 'text', field, value: normalize(m[10]) });
          }
        } else if (m[11]) {
          // field:bareword
          if (TEXT_FIELDS[field]) {
            tokens.push({ type: 'field', kind: 'text', field, value: normalize(m[11]) });
          } else {
            tokens.push({ type: 'term', value: normalize(field + ':' + m[11]) });
          }
        }
      } else if (m[12] !== undefined) {
        // "quoted phrase" — supports regex syntax
        const val = normalize(m[12]);
        if (val) tokens.push({ type: 'term', value: val, regex: toRegex(val) });
      } else if (m[13]) {
        const word = m[13];
        if (word === 'AND') {
          tokens.push({ type: 'and' });
        } else if (word === 'OR') {
          tokens.push({ type: 'or' });
        } else if (word === 'NOT' || word === '-') {
          tokens.push({ type: 'not' });
        } else if (word === '(') {
          tokens.push({ type: 'lparen' });
        } else if (word === ')') {
          tokens.push({ type: 'rparen' });
        } else if (word.startsWith('-') && word.length > 1) {
          // -term or -field:value — emit NOT then re-tokenize the rest
          tokens.push({ type: 'not' });
          const sub = tokenize(word.slice(1));
          tokens.push(...sub);
        } else {
          const val = normalize(word);
          if (val) tokens.push({ type: 'term', value: val });
        }
      }
    }
    return tokens;
  }

  // ---- Parser (recursive descent) ----
  // Precedence: OR (lowest) → AND (implicit or explicit) → NOT → primary
  // Returns an AST node.
  function parseQuery(raw) {
    const tokens = tokenize(raw);
    let pos = 0;

    function peek() { return pos < tokens.length ? tokens[pos] : null; }
    function advance() { return tokens[pos++]; }

    // orExpr → andExpr ( OR andExpr )*
    function orExpr() {
      let left = andExpr();
      if (!left) return null;
      while (peek() && peek().type === 'or') {
        advance(); // consume OR
        const right = andExpr();
        if (!right) break;
        left = { type: 'or', left, right };
      }
      return left;
    }

    // andExpr → notExpr ( AND? notExpr )*
    // Implicit AND: two adjacent primaries without an operator
    function andExpr() {
      let left = notExpr();
      if (!left) return null;
      while (peek()) {
        const t = peek();
        // Stop at OR or rparen — those belong to outer rules
        if (t.type === 'or' || t.type === 'rparen') break;
        // Consume explicit AND if present
        if (t.type === 'and') advance();
        const right = notExpr();
        if (!right) break;
        left = { type: 'and', left, right };
      }
      return left;
    }

    // notExpr → NOT* primary
    function notExpr() {
      if (peek() && peek().type === 'not') {
        advance();
        const operand = notExpr(); // allow NOT NOT x
        if (!operand) return null;
        return { type: 'not', operand };
      }
      return primary();
    }

    // primary → LPAREN orExpr RPAREN | FIELD | TERM
    function primary() {
      // Skip unexpected tokens (stray AND/OR) without recursion
      while (peek()) {
        const t = peek();
        if (t.type === 'lparen') {
          advance();
          const node = orExpr();
          if (peek() && peek().type === 'rparen') advance();
          return node;
        }
        if (t.type === 'term' || t.type === 'field') {
          return advance();
        }
        advance(); // skip unexpected token
      }
      return null;
    }

    const ast = orExpr();
    return ast;
  }

  // ---- Evaluator ----
  function matchNumeric(node, item) {
    const val = NUMERIC_FIELDS[node.field](item);
    if (node.op === '..') return val >= node.low && val <= node.high;
    if (node.op === '==') return val === node.value;
    if (node.op === '>') return val > node.value;
    if (node.op === '>=') return val >= node.value;
    if (node.op === '<') return val < node.value;
    if (node.op === '<=') return val <= node.value;
    return false;
  }

  function matchDate(node, item) {
    const val = DATE_FIELDS[node.field](item);
    if (node.op === '..') return val >= node.low && val <= node.high;
    if (node.op === '>') return val > node.value;
    if (node.op === '>=') return val >= node.value;
    if (node.op === '<') return val < node.value;
    if (node.op === '<=') return val <= node.value;
    return false;
  }

  // Recursively evaluate an AST node against an item.
  // null AST (empty query) matches all items.
  function evaluate(node, item) {
    if (!node) return true;
    if (node.type === 'and') return evaluate(node.left, item) && evaluate(node.right, item);
    if (node.type === 'or') return evaluate(node.left, item) || evaluate(node.right, item);
    if (node.type === 'not') return !evaluate(node.operand, item);
    if (node.type === 'term') return node.regex ? node.regex.test(item._search) : item._search.includes(node.value);
    if (node.type === 'field') {
      if (node.kind === 'text') {
        const key = TEXT_FIELDS[node.field];
        if (!key) return false;
        return node.regex ? node.regex.test(item[key]) : item[key].includes(node.value);
      }
      if (node.kind === 'numeric') return matchNumeric(node, item);
      if (node.kind === 'date') return matchDate(node, item);
    }
    return true;
  }

  class ItemManager {
    constructor(containerEl) {
      this.container = containerEl;
      this.config = JSON.parse(containerEl.dataset.filterConfig || '{}');

      // All item data (from JSON index)
      this.items = [];
      // Filtered + sorted subset
      this.filteredItems = [];
      // Map of id → DOM element (reuses Hugo-rendered elements)
      this.renderedMap = new Map();
      this.totalCount = 0;
      this.displayedCount = 0;
      this.pageSize = parseInt(containerEl.dataset.pageSize, 10) || 60;

      this.sectionHeadings = [];
      this.itemSettings = {};
      this.format = 'card';

      const parent = containerEl.parentNode;
      this.controlsEl = parent.querySelector('[data-filter-controls]');
      this.barEl = parent.querySelector('[data-filter-bar]');
      this.showBtn = parent.querySelector('[data-filter-show]');
      this._stickyObserved = false;

      if (this.barEl) {
        this.barEl.classList.remove('invisible');
      }
      if (this.showBtn) {
        this.showBtn.addEventListener('click', () => {
          if (this.controlsEl.classList.contains('hidden')) {
            this.state.showFilters = true;
            this._showControls();
          } else {
            this.state.showFilters = false;
            this.controlsEl.classList.add('hidden');
            if (this.barEl) this.barEl.classList.add('mb-4');
          }
          this._updateShowBtnLabel();
          this._updateURL();
        });
      }

      this._defaultSortCfg = this.config.sort
        ? this.config.sort.find(s => s.default) || this.config.sort[0]
        : null;

      this.state = {
        search: '',
        sort: {
          key: this._defaultSortCfg ? this._defaultSortCfg.key : '',
          direction: this._defaultSortCfg ? (this._defaultSortCfg.direction || 'asc') : 'asc',
        },
        filters: {},
      };

      if (this.config.filters) {
        this.config.filters.forEach(f => {
          this.state.filters[f.key] = new Set();
        });
      }

      this._filterCfgMap = {};
      if (this.config.filters) {
        this.config.filters.forEach(f => {
          this._filterCfgMap[f.key] = {
            aliases: f.aliases || {},
            otherExcludes: f.other ? new Set(f.other) : null,
          };
        });
      }

      this._sortCfgMap = {};
      if (this.config.sort) {
        this.config.sort.forEach(s => { this._sortCfgMap[s.key] = s; });
      }

      this._interactive = false;
      this.sentinel = null;
      this.observer = null;

      this._init();
    }

    async _init() {
      this._loadItemSettings();
      await this._hydrate();
      this._hidePagination();
      this._readURL();
      if (this._hasActiveFilters()) {
        const featured = this.container.parentElement?.querySelector('[data-featured]');
        if (featured) featured.classList.add('hidden');
      }
      this._updateSourceAnnouncement();
      if (this.state.showFilters || this._hasActiveFilters()) this._showControls();
      this._updateShowBtnLabel();
      this._bindControls();
      this._applyFilters();
      this._setupInfiniteScroll();
      this._interactive = true;
    }

    _loadItemSettings() {
      const el = document.getElementById('item-settings');
      if (el) {
        try {
          this.itemSettings = JSON.parse(el.textContent);
        } catch (e) {
          // ignore
        }
      }
    }

    _hidePagination() {
      const nav = this.container.parentNode.querySelector('[data-pagination]');
      if (nav) nav.style.display = 'none';
      // If on a /page/N/ URL, redirect to base path so infinite scroll starts from page 1
      if (/\/page\/\d+\/?$/.test(window.location.pathname)) {
        const base = window.location.pathname.replace(/\/page\/\d+\/?$/, '/');
        window.history.replaceState({}, '', base + window.location.search);
      }
    }

    _hasActiveFilters() {
      if (this.state.search) return true;
      for (const set of Object.values(this.state.filters)) {
        if (set.size > 0) return true;
      }
      if (this.state.sort.key && this._defaultSortCfg && this.state.sort.key !== this._defaultSortCfg.key) return true;
      return false;
    }

    _isDefaultSort() {
      return this.config.defaultSort && (!this.state.sort.key || this.state.sort.key === this.config.defaultSort);
    }

    _showControls() {
      if (this.controlsEl) {
        this.controlsEl.classList.remove('hidden');
        if (this.barEl) this.barEl.classList.remove('mb-4');
        if (!this._stickyObserved) {
          this._observeSticky();
          this._stickyObserved = true;
        }
      }
    }

    _observeSticky() {
      const sentinel = document.createElement('div');
      this.controlsEl.parentNode.insertBefore(sentinel, this.controlsEl);
      new IntersectionObserver(([entry]) => {
        this.controlsEl.classList.toggle('border-b', !entry.isIntersecting);
        this.controlsEl.classList.toggle('border-gray-200', !entry.isIntersecting);
      }).observe(sentinel);
    }

    async _hydrate() {
      // Fetch item index JSON — strip /page/N/ suffix for paginated pages
      const basePath = window.location.pathname.replace(/\/page\/\d+\/?$/, '/').replace(/\/$/, '');
      const indexUrl = basePath + '/item-index.json';
      let index = [];
      try {
        const res = await fetch(indexUrl, { signal: AbortSignal.timeout(10000) });
        if (res.ok) index = await res.json();
      } catch (e) {
        // Fall back to empty index (timeout, network error, or bad JSON)
      }

      // Build items array from JSON with pre-computed search/sort/filter keys
      this.items = index.map((entry, idx) => {
        // Decode HTML entities from Hugo partial escaping
        if (entry.description) entry.description = decodeHTML(entry.description);

        const authors = entry.authors || [];
        const topics = entry.topics || [];
        const tags = entry.tags || [];
        const software = entry.software || [];
        const languages = entry.languages || [];
        const authorNames = authors.map(a => a.name).join(' ');

        const searchParts = [
          entry.title || '',
          entry.description || '',
          software.join(' '),
          topics.join(' '),
          tags.join(' '),
          authorNames,
          entry.location || '',
          entry.source || '',
        ];

        return {
          ...entry,
          // Pre-normalized text fields for search qualifiers
          _qTitle:       normalize(entry.title || ''),
          _qAuthor:      normalize(authorNames),
          _qDescription: normalize(entry.description || ''),
          _qTopic:       normalize(topics.join(' ')),
          _qTag:         normalize(tags.join(' ')),
          _qSoftware:    normalize(software.join(' ')),
          _qLanguage:    normalize(languages.join(' ')),
          _qLocation:    normalize(entry.location || ''),
          _qSource:      normalize(entry.source || ''),
          // Full-text search index
          _search: normalize(searchParts.join(' ')),
          // Sort keys
          _sortTitle: normalize(entry.title || '').replace(/[^a-z0-9 ]/g, '').trim(),
          _idx: idx,
          _dateTs: entry.date ? new Date(entry.date).getTime() : 0,
          _firstCommitTs: entry.firstCommit ? new Date(entry.firstCommit).getTime() : 0,
        };
      });

      // Match existing Hugo-rendered DOM elements to items
      this.items.forEach(item => {
        const el = this.container.querySelector('#' + CSS.escape(item.id));
        if (el) this.renderedMap.set(item.id, el);
      });

      this.sectionHeadings = Array.from(
        this.container.querySelectorAll('[data-section-heading]')
      );
      this.totalCount = this.items.length;
    }

    _renderFromTemplate(entry, format) {
      format = format || this.format;
      const tpl = document.getElementById('item-tpl-' + format);
      if (!tpl) return null;

      const clone = tpl.content.cloneNode(true);
      const root = clone.firstElementChild;
      if (!root) return null;

      root.id = entry.id;

      const slot = (name) => root.querySelector('[data-slot="' + name + '"]');
      const settings = this.itemSettings[entry.itemType] || {};

      // Link
      const linkEl = slot('link') || root;
      if (linkEl.tagName === 'A' || linkEl.hasAttribute('data-slot')) {
        linkEl.href = entry.permalink;
        linkEl.title = entry.title;
      }
      // For row format, root is the <a>
      if (root.tagName === 'A') {
        root.href = entry.permalink;
        root.title = entry.title;
      }

      // Card class
      if (settings.card_class && format === 'card') {
        const linkTarget = slot('link') || root;
        settings.card_class.split(' ').filter(Boolean).forEach(c => linkTarget.classList.add(c));
      }
      if (settings.tile_class && format === 'tile') {
        const linkTarget = slot('link') || root;
        settings.tile_class.split(' ').filter(Boolean).forEach(c => linkTarget.classList.add(c));
      }
      if (settings.row_class && format === 'row') {
        root.classList.add(...settings.row_class.split(' ').filter(Boolean));
      }

      // Badge
      const badgeEl = slot('badge');
      if (badgeEl && settings.badge_icon) {
        badgeEl.classList.remove('hidden');
        const badgeIcon = slot('badge-icon');
        if (badgeIcon) badgeIcon.className = 'icon-[' + settings.badge_icon + ']';
        const badgeText = slot('badge-text');
        if (badgeText) badgeText.textContent = settings.badge_text || '';
      }

      // Image
      if (entry.image && entry.image.src) {
        const imageWrap = slot('image-wrap');
        if (imageWrap && entry.color) {
          imageWrap.style.backgroundColor = 'color-mix(in srgb, ' + entry.color + ' 25%, white 75%)';
        }
        const img = slot('image');
        if (img) {
          img.src = entry.image.src;
          img.alt = entry.image.alt || '';
          if (entry.image.width) img.width = entry.image.width;
          if (entry.image.height) img.height = entry.image.height;
          // Image class from settings
          const imgClass = settings.image_class || '';
          if (imgClass) imgClass.split(' ').filter(Boolean).forEach(c => img.classList.add(c));
        }
      }

      // Title
      const titleEl = slot('title');
      if (titleEl) {
        titleEl.textContent = entry.title;
        const titleClass = settings.title_class || '';
        if (titleClass) titleClass.split(' ').filter(Boolean).forEach(c => titleEl.classList.add(c));
      }

      // Description
      const descEl = slot('description');
      if (descEl) {
        descEl.textContent = entry.description || '';
        const descClass = settings.description_class || '';
        if (descClass) descClass.split(' ').filter(Boolean).forEach(c => descEl.classList.add(c));
      }

      // People (authors with headshots)
      if (entry.authors && entry.authors.length && settings.people_show) {
        const peopleEl = slot('people');
        if (peopleEl) {
          peopleEl.classList.remove('hidden');
          const frag = document.createDocumentFragment();
          const wrapper = document.createElement('div');
          wrapper.className = 'flex flex-row gap-x-5 items-center';

          // Headshot images
          const hasImages = entry.authors.some(a => a.image);
          if (hasImages) {
            const imgWrap = document.createElement('div');
            imgWrap.className = 'flex flex-row';
            entry.authors.forEach((a, i) => {
              if (a.image) {
                const img = document.createElement('img');
                img.src = a.image;
                img.alt = a.name;
                img.className = 'my-0 w-6 h-6 rounded-full object-cover ring-2 ring-white' + (i > 0 ? ' -ml-2' : '');
                img.style.zIndex = 10 - i;
                img.loading = 'lazy';
                imgWrap.appendChild(img);
              }
            });
            wrapper.appendChild(imgWrap);
          }

          // Names
          const namesDiv = document.createElement('div');
          namesDiv.className = 'truncate text-slate-900';
          namesDiv.textContent = entry.authors.map(a => a.name).join(', ');
          wrapper.appendChild(namesDiv);
          frag.appendChild(wrapper);
          peopleEl.appendChild(frag);
        }
      }

      // Conditional metadata
      const conditionals = [
        ['location', entry.location],
        ['date', entry.dateFormatted],
        ['duration', entry.durationFormatted],
        ['views', entry.viewsFormatted],
        ['stars', entry.starsFormatted],
      ];
      for (const [name, value] of conditionals) {
        if (value) {
          const el = slot(name);
          if (el) {
            el.style.display = '';
            const textEl = slot(name + '-text');
            if (textEl) textEl.textContent = value;
          }
        }
      }

      // Tags (combination of software + topics + tags)
      const allTags = [
        ...(entry.software || []),
        ...(entry.topics || []),
        ...(entry.tags || []),
      ];
      if (allTags.length) {
        const tagsEl = slot('tags');
        if (tagsEl) {
          // For tile format, tags container has a nested div
          const target = tagsEl.querySelector('div') || tagsEl;
          allTags.forEach(tag => {
            const span = document.createElement('span');
            span.className = 'pill';
            span.textContent = tag;
            target.appendChild(span);
          });
          // Show the tags container
          if (format === 'tile') {
            tagsEl.classList.remove('hidden');
          }
        }
      }

      return root;
    }

    _getOrRenderElement(item) {
      if (this.renderedMap.has(item.id)) {
        return this.renderedMap.get(item.id);
      }
      const el = this._renderFromTemplate(item);
      if (el) {
        this.renderedMap.set(item.id, el);
      }
      return el;
    }

    _renderBatch() {
      const start = this.displayedCount;
      const end = Math.min(start + this.pageSize, this.filteredItems.length);
      if (start >= end) return;

      const frag = document.createDocumentFragment();
      for (let i = start; i < end; i++) {
        const item = this.filteredItems[i];
        const el = this._getOrRenderElement(item);
        if (el) frag.appendChild(el);
      }
      this.container.appendChild(frag);
      this.displayedCount = end;

      // Update sentinel visibility
      if (this.sentinel) {
        if (this.displayedCount >= this.filteredItems.length) {
          this.sentinel.style.display = 'none';
        } else {
          this.sentinel.style.display = '';
        }
      }
    }

    _setupInfiniteScroll() {
      this.sentinel = document.createElement('div');
      this.sentinel.className = 'h-1';
      this.container.parentNode.insertBefore(this.sentinel, this.container.nextSibling);

      this.observer = new IntersectionObserver(
        ([entry]) => {
          if (entry.isIntersecting && this.displayedCount < this.filteredItems.length) {
            this._renderBatch();
          }
        },
        { rootMargin: '200px' }
      );
      this.observer.observe(this.sentinel);
    }

    _bindControls() {
      if (!this.controlsEl) return;

      const searchInput = this.controlsEl.querySelector('[data-filter-search]');
      if (searchInput) {
        searchInput.value = this.state.search;
        searchInput.addEventListener(
          'input',
          debounce(() => {
            this.state.search = searchInput.value;
            this._applyFilters();
          }, 150)
        );
      }

      // Search help toggle
      const helpToggle = this.controlsEl.querySelector('[data-search-help-toggle]');
      const helpPanel = this.controlsEl.querySelector('[data-search-help]');
      if (helpToggle && helpPanel) {
        helpToggle.addEventListener('click', (e) => {
          e.stopPropagation();
          helpPanel.classList.toggle('hidden');
        });
        helpPanel.addEventListener('click', (e) => e.stopPropagation());
        document.addEventListener('click', () => helpPanel.classList.add('hidden'));
      }

      const sortTrigger = this.controlsEl.querySelector('[data-sort-trigger]');
      const sortPanel = this.controlsEl.querySelector('[data-sort-panel]');
      if (sortTrigger && sortPanel) {
        // Sync initial state (e.g. from URL params)
        const activeKey = this.state.sort.key || (this._defaultSortCfg ? this._defaultSortCfg.key : '');
        if (activeKey) {
          sortPanel.querySelectorAll('[data-sort-check]').forEach(c => c.classList.add('opacity-0'));
          const activeBtn = sortPanel.querySelector('[data-sort-key="' + activeKey + '"]');
          if (activeBtn) {
            activeBtn.querySelector('[data-sort-check]').classList.remove('opacity-0');
            const cfg = this.config.sort.find(s => s.key === activeKey);
            const label = sortTrigger.querySelector('[data-sort-label]');
            if (label && cfg) label.textContent = cfg.label || activeKey;
          }
        }
        sortTrigger.addEventListener('click', (e) => {
          e.stopPropagation();
          this.controlsEl.querySelectorAll('[data-filter-panel]').forEach(p => p.classList.add('hidden'));
          sortPanel.classList.toggle('hidden');
        });
        sortPanel.addEventListener('click', (e) => e.stopPropagation());
        sortPanel.querySelectorAll('[data-sort-option]').forEach(btn => {
          btn.addEventListener('click', () => {
            const key = btn.dataset.sortKey;
            const cfg = this.config.sort.find(s => s.key === key);
            this.state.sort.key = key;
            this.state.sort.direction = cfg ? (cfg.direction || 'asc') : 'asc';
            sortPanel.querySelectorAll('[data-sort-check]').forEach(c => c.classList.add('opacity-0'));
            btn.querySelector('[data-sort-check]').classList.remove('opacity-0');
            const label = sortTrigger.querySelector('[data-sort-label]');
            if (label) label.textContent = btn.querySelector('span:last-child').textContent;
            sortPanel.classList.add('hidden');
            this._applyFilters();
          });
        });
      }

      // Filter dropdowns
      this.controlsEl.querySelectorAll('[data-filter-trigger]').forEach(trigger => {
        const key = trigger.dataset.filterTrigger;
        const panel = this.controlsEl.querySelector('[data-filter-panel="' + key + '"]');
        if (!panel) return;
        trigger.addEventListener('click', (e) => {
          e.stopPropagation();
          this.controlsEl.querySelectorAll('[data-filter-panel]').forEach(p => {
            if (p !== panel) p.classList.add('hidden');
          });
          const sp = this.controlsEl.querySelector('[data-sort-panel]');
          if (sp) sp.classList.add('hidden');
          panel.classList.toggle('hidden');
        });
        panel.addEventListener('click', (e) => e.stopPropagation());
      });

      document.addEventListener('click', () => {
        if (!this.controlsEl) return;
        this.controlsEl.querySelectorAll('[data-filter-panel]').forEach(p => {
          p.classList.add('hidden');
        });
        const sp = this.controlsEl.querySelector('[data-sort-panel]');
        if (sp) sp.classList.add('hidden');
      });

      const filterBtns = this.controlsEl.querySelectorAll('[data-filter-group]');
      filterBtns.forEach(btn => {
        const group = btn.dataset.filterGroup;
        const value = btn.dataset.filterValue;
        const check = btn.querySelector('[data-filter-check]');
        if (this.state.filters[group] && this.state.filters[group].has(value)) {
          if (check) check.classList.remove('opacity-0');
        }
        btn.addEventListener('click', () => {
          const set = this.state.filters[group];
          if (!set) return;
          if (set.has(value)) {
            set.delete(value);
            if (check) check.classList.add('opacity-0');
          } else {
            set.add(value);
            if (check) check.classList.remove('opacity-0');
          }
          this._updateBadge(group);
          this._applyFilters();
        });
      });

      // Set initial badge counts
      for (const key of Object.keys(this.state.filters)) {
        this._updateBadge(key);
      }

      if (this.barEl) {
        const resetBtn = this.barEl.querySelector('[data-filter-reset]');
        if (resetBtn) {
          resetBtn.addEventListener('click', () => this.reset());
        }
      }
    }

    _matchesFilters(item) {
      for (const [key, activeSet] of Object.entries(this.state.filters)) {
        if (activeSet.size === 0) continue;
        const cfg = this._filterCfgMap[key] || {};
        const aliases = cfg.aliases || {};
        const otherExcludes = cfg.otherExcludes || null;

        // Use original arrays from JSON; fall back to item[key] for 'type' etc.
        const raw = item[key];
        const values = Array.isArray(raw) ? raw : (raw ? [raw] : []);

        let matched = false;
        for (const active of activeSet) {
          if (active === 'Other' && otherExcludes) {
            if (values.length === 0 || values.some(v => !otherExcludes.has(v))) {
              matched = true;
              break;
            }
          } else if (aliases[active]) {
            if (values.some(v => aliases[active].includes(v))) {
              matched = true;
              break;
            }
          } else if (values.includes(active)) {
            matched = true;
            break;
          }
        }
        if (!matched) return false;
      }
      return true;
    }

    _sortItems(items) {
      const { key, direction } = this.state.sort;
      if (!key) return items;
      const cfg = this._sortCfgMap[key];
      if (!cfg) return items;
      const dir = direction === 'desc' ? -1 : 1;
      const prop = key.replace(/-([a-z])/g, (_, c) => c.toUpperCase());

      return items.slice().sort((a, b) => {
        let cmp;
        if (cfg.type === 'number') {
          cmp = ((a[prop] || 0) - (b[prop] || 0)) * dir;
        } else if (cfg.type === 'date') {
          const tsKey = '_' + prop + 'Ts';
          cmp = ((a[tsKey] || a._dateTs) - (b[tsKey] || b._dateTs)) * dir;
        } else {
          const sortKey = '_sort' + prop.charAt(0).toUpperCase() + prop.slice(1);
          const sa = a[sortKey] !== undefined ? a[sortKey] : String(a[prop] || '').toLowerCase();
          const sb = b[sortKey] !== undefined ? b[sortKey] : String(b[prop] || '').toLowerCase();
          cmp = sa.localeCompare(sb) * dir;
        }
        // Stable tie-break: preserve original JSON index order
        return cmp || (a._idx - b._idx);
      });
    }

    _applyFilters() {
      const ast = parseQuery(this.state.search);

      // Filter all items at data level
      let filtered = this.items.filter(
        item => evaluate(ast, item) && this._matchesFilters(item)
      );

      // Sort
      filtered = this._sortItems(filtered);

      // Handle section headings for events-style pages
      if (this.sectionHeadings.length > 0 && this._isDefaultSort()) {
        // Group by section, preserving heading order
        const sectionOrder = this.sectionHeadings.map(h => h.dataset.sectionHeading);
        const grouped = [];
        sectionOrder.forEach(section => {
          const sectionItems = filtered.filter(item => item.section === section);
          if (sectionItems.length > 0) {
            grouped.push({ heading: section, items: sectionItems });
          }
        });
        this._renderSectioned(grouped);
      } else {
        // Hide section headings when not in default sort
        this.sectionHeadings.forEach(h => h.classList.add('hidden'));
        this.filteredItems = filtered;
        this._clearContainer();
        this.displayedCount = 0;
        this._renderBatch();
      }

      this._updateCount(filtered.length);
      this._updateEmpty(filtered.length === 0);
      this._updateResetBtn();
      this._updateSourceAnnouncement();
      this._updateURL();

      if (this._interactive && this.controlsEl) {
        const controlsHeight = this.controlsEl.offsetHeight;
        const containerTop = this.container.getBoundingClientRect().top;
        if (containerTop < controlsHeight) {
          const target = window.scrollY + containerTop - controlsHeight;
          window.scrollTo({ top: target, behavior: 'smooth' });
        }
      }
    }

    _renderSectioned(groups) {
      this._clearContainer();
      const frag = document.createDocumentFragment();
      const allFiltered = [];

      groups.forEach(group => {
        const heading = this.sectionHeadings.find(
          h => h.dataset.sectionHeading === group.heading
        );
        if (heading) {
          heading.classList.remove('hidden');
          frag.appendChild(heading);
        }
        group.items.forEach(item => {
          const el = this._getOrRenderElement(item);
          if (el) {
            el.classList.remove('hidden');
            frag.appendChild(el);
          }
          allFiltered.push(item);
        });
      });

      // Hide headings with no visible items
      this.sectionHeadings.forEach(h => {
        if (!groups.some(g => g.heading === h.dataset.sectionHeading)) {
          h.classList.add('hidden');
        }
      });

      this.container.appendChild(frag);
      this.filteredItems = allFiltered;
      this.displayedCount = allFiltered.length;
    }

    _clearContainer() {
      this.container.replaceChildren();
    }

    _updateShowBtnLabel() {
      if (!this.showBtn) return;
      const label = this.showBtn.querySelector('[data-filter-show-label]');
      if (label) {
        const isHidden = this.controlsEl.classList.contains('hidden');
        label.textContent = isHidden ? 'Show Filters' : 'Hide Filters';
      }
    }

    _updateResetBtn() {
      if (!this.barEl) return;
      const resetBtn = this.barEl.querySelector('[data-filter-reset]');
      if (resetBtn) {
        const active = this._hasActiveFilters();
        resetBtn.classList.toggle('hidden', !active);
        resetBtn.classList.toggle('inline-flex', active);
      }
    }

    _updateBadge(group) {
      if (!this.controlsEl) return;
      const badge = this.controlsEl.querySelector('[data-filter-badge="' + group + '"]');
      if (!badge) return;
      const count = this.state.filters[group] ? this.state.filters[group].size : 0;
      badge.textContent = count;
      badge.classList.toggle('hidden', count === 0);
    }

    _updateCount(count) {
      if (!this.barEl) return;
      const countEl = this.barEl.querySelector('[data-filter-count]');
      const totalEl = this.barEl.querySelector('[data-filter-total]');
      if (countEl) countEl.textContent = count;
      if (totalEl) totalEl.textContent = this.totalCount;
    }

    _updateEmpty(isEmpty) {
      const emptyEl = this.container.parentNode.querySelector('[data-filter-empty]');
      if (emptyEl) emptyEl.classList.toggle('hidden', !isEmpty);
    }

    _updateSourceAnnouncement() {
      const parent = this.container.parentElement;
      if (!parent) return;
      const announcements = parent.querySelectorAll('[data-source-announcement]');
      if (!announcements.length) return;

      // Extract source value from search query (e.g. "source:quarto" → "quarto")
      const match = this.state.search.match(/\bsource:(\S+)/i);
      const source = match ? match[1].toLowerCase().replace(/^"(.*)"$/, '$1') : '';

      announcements.forEach(el => {
        el.classList.toggle('hidden', el.dataset.sourceAnnouncement !== source);
      });

      // Also hide featured when a source announcement is visible
      const featured = parent.querySelector('[data-featured]');
      if (featured && source) {
        featured.classList.add('hidden');
      }
    }

    _updateURL() {
      const params = new URLSearchParams();
      const defaultSortKey = this._defaultSortCfg ? this._defaultSortCfg.key : '';

      if (this.state.sort.key && this.state.sort.key !== defaultSortKey) {
        params.set('sort', this.state.sort.key);
      }

      if (this.state.search.trim()) {
        params.set('q', this.state.search.trim());
      }

      for (const [key, set] of Object.entries(this.state.filters)) {
        if (set.size > 0) {
          params.set(key, Array.from(set).join(','));
        }
      }

      if (this.state.showFilters) {
        params.set('showFilters', 'true');
      }

      const qs = params.toString();
      const url = qs ? window.location.pathname + '?' + qs : window.location.pathname;
      window.history.replaceState({}, '', url);
    }

    _readURL() {
      const params = new URLSearchParams(window.location.search);

      if (params.has('sort')) {
        const sortKey = params.get('sort');
        const cfg = this.config.sort
          ? this.config.sort.find(s => s.key === sortKey)
          : null;
        if (cfg) {
          this.state.sort.key = sortKey;
          this.state.sort.direction = cfg.direction || 'asc';
        }
      }

      if (params.has('q')) {
        this.state.search = params.get('q');
      }

      this.state.showFilters = params.get('showFilters') === 'true';

      if (this.config.filters) {
        this.config.filters.forEach(f => {
          if (params.has(f.key)) {
            const vals = params
              .get(f.key)
              .split(',')
              .filter(Boolean);
            this.state.filters[f.key] = new Set(vals);
          }
        });
      }
    }

    reset() {
      this.state.search = '';
      if (this._defaultSortCfg) {
        this.state.sort.key = this._defaultSortCfg.key;
        this.state.sort.direction = this._defaultSortCfg.direction || 'asc';
      }
      for (const key of Object.keys(this.state.filters)) {
        this.state.filters[key] = new Set();
      }

      if (this.controlsEl) {
        const searchInput = this.controlsEl.querySelector('[data-filter-search]');
        if (searchInput) searchInput.value = '';

        if (this._defaultSortCfg) {
          const sortPanel = this.controlsEl.querySelector('[data-sort-panel]');
          if (sortPanel) {
            sortPanel.querySelectorAll('[data-sort-check]').forEach(c => c.classList.add('opacity-0'));
            const defaultBtn = sortPanel.querySelector('[data-sort-key="' + this._defaultSortCfg.key + '"]');
            if (defaultBtn) defaultBtn.querySelector('[data-sort-check]').classList.remove('opacity-0');
          }
          const sortLabel = this.controlsEl.querySelector('[data-sort-label]');
          if (sortLabel) sortLabel.textContent = this._defaultSortCfg.label || this._defaultSortCfg.key;
        }

        this.controlsEl.querySelectorAll('[data-filter-check]').forEach(check => {
          check.classList.add('opacity-0');
        });
        this.controlsEl.querySelectorAll('[data-filter-badge]').forEach(badge => {
          badge.classList.add('hidden');
        });
      }

      this._applyFilters();
    }
  }

  function init() {
    const containers = document.querySelectorAll('[data-item-container]');
    if (!containers.length) return;
    containers.forEach(el => new ItemManager(el));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
