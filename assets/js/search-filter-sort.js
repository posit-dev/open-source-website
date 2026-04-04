(function () {
  'use strict';

  function debounce(fn, ms) {
    let id;
    return function (...args) {
      clearTimeout(id);
      id = setTimeout(() => fn.apply(this, args), ms);
    };
  }

  class CardManager {
    constructor(containerEl) {
      this.container = containerEl;
      this.config = JSON.parse(containerEl.dataset.filterConfig || '{}');
      this.cards = [];
      this.totalCount = 0;
      this.sectionHeadings = [];
      this.controlsEl = containerEl.previousElementSibling;
      if (!this.controlsEl || !this.controlsEl.hasAttribute('data-filter-controls')) {
        this.controlsEl = null;
      } else {
        this.controlsEl.classList.remove('hidden');
        this._observeSticky();
      }

      const defaultSortCfg = this.config.sort
        ? this.config.sort.find(s => s.default) || this.config.sort[0]
        : null;
      this.state = {
        search: '',
        sort: {
          key: defaultSortCfg ? defaultSortCfg.key : '',
          direction: defaultSortCfg ? (defaultSortCfg.direction || 'asc') : 'asc',
        },
        filters: {},
      };

      if (this.config.filters) {
        this.config.filters.forEach(f => {
          this.state.filters[f.key] = new Set();
        });
      }

      this._lastSortKey = '';
      this._lastSortDir = '';
      this._needsReorder = true;
      this._interactive = false;

      this._init();
    }

    async _init() {
      await this._hydrate();
      this._readURL();
      this._bindControls();
      this._applyFilters();
      this._interactive = true;
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
      // Fetch card index JSON
      const indexUrl = window.location.pathname.replace(/\/$/, '') + '/card-index.json';
      let index = [];
      try {
        const res = await fetch(indexUrl);
        if (res.ok) index = await res.json();
      } catch (e) {
        // Fall back to empty index — cards will still render but won't be searchable
      }

      // Match JSON entries to DOM elements by id
      this.cards = [];
      for (const entry of index) {
        const el = this.container.querySelector('#' + CSS.escape(entry.id));
        if (!el) continue;
        this.cards.push({
          el,
          title: entry.title || '',
          description: entry.description || '',
          tags: entry.tags || '',
          date: entry.date || '',
          categories: entry.categories || '',
          languages: entry.languages || '',
          stars: entry.stars ? Number(entry.stars) : 0,
          firstCommit: entry.firstCommit || '',
          _firstCommitTs: entry.firstCommit ? new Date(entry.firstCommit).getTime() : 0,
          views: entry.views ? Number(entry.views) : 0,
          duration: entry.duration ? Number(entry.duration) : 0,
          authors: entry.authors || '',
          location: entry.location || '',
          section: entry.section || '',
          _dateTs: entry.date ? new Date(entry.date).getTime() : 0,
          _sortTitle: (entry.title || '').toLowerCase().replace(/[^a-z0-9 ]/g, '').trim(),
          _search: [entry.title, entry.description, entry.tags, entry.authors, entry.location].join(' ').toLowerCase(),
        });
      }

      this.totalCount = this.cards.length;
      this.sectionHeadings = Array.from(
        this.container.querySelectorAll('[data-section-heading]')
      );
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

      const sortSelect = this.controlsEl.querySelector('[data-filter-sort]');
      if (sortSelect) {
        sortSelect.value = this.state.sort.key;
        sortSelect.addEventListener('change', () => {
          const key = sortSelect.value;
          const cfg = this.config.sort.find(s => s.key === key);
          this.state.sort.key = key;
          this.state.sort.direction = cfg ? (cfg.direction || 'asc') : 'asc';
          this._applyFilters();
        });
      }

      const filterBtns = this.controlsEl.querySelectorAll('[data-filter-group]');
      filterBtns.forEach(btn => {
        const group = btn.dataset.filterGroup;
        const value = btn.dataset.filterValue;
        if (this.state.filters[group] && this.state.filters[group].has(value)) {
          btn.classList.add('bg-blue-600', 'text-white', 'border-blue-600');
          btn.classList.remove('bg-white', 'text-gray-700', 'border-gray-300');
        }
        btn.addEventListener('click', () => {
          const set = this.state.filters[group];
          if (!set) return;
          if (set.has(value)) {
            set.delete(value);
            btn.classList.remove('bg-blue-600', 'text-white', 'border-blue-600');
            btn.classList.add('bg-white', 'text-gray-700', 'border-gray-300');
          } else {
            set.add(value);
            btn.classList.add('bg-blue-600', 'text-white', 'border-blue-600');
            btn.classList.remove('bg-white', 'text-gray-700', 'border-gray-300');
          }
          this._applyFilters();
        });
      });

      const resetBtn = this.controlsEl.querySelector('[data-filter-reset]');
      if (resetBtn) {
        resetBtn.addEventListener('click', () => this.reset());
      }

      const toggleBtn = this.controlsEl.querySelector('[data-filter-toggle]');
      const filterBody = this.controlsEl.querySelector('[data-filter-body]');
      if (toggleBtn && filterBody) {
        toggleBtn.addEventListener('click', () => {
          const isHidden = filterBody.classList.contains('hidden');
          filterBody.classList.toggle('hidden', !isHidden);
          toggleBtn.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
        });
      }
    }

    _matchesSearch(card, tokens) {
      if (!tokens.length) return true;
      return tokens.every(t => card._search.includes(t));
    }

    _matchesFilters(card) {
      for (const [key, activeSet] of Object.entries(this.state.filters)) {
        if (activeSet.size === 0) continue;
        const cfg = this.config.filters
          ? this.config.filters.find(f => f.key === key)
          : null;
        const aliases = cfg && cfg.aliases ? cfg.aliases : {};
        const otherExcludes = cfg && cfg.other ? new Set(cfg.other) : null;
        const values = card[key]
          .split(',')
          .map(v => v.trim())
          .filter(Boolean);
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

    _sortCards(cards) {
      const { key, direction } = this.state.sort;
      if (!key) return cards;
      const cfg = this.config.sort ? this.config.sort.find(s => s.key === key) : null;
      if (!cfg) return cards;
      const dir = direction === 'desc' ? -1 : 1;
      const prop = key.replace(/-([a-z])/g, (_, c) => c.toUpperCase());

      return cards.slice().sort((a, b) => {
        const av = a[prop];
        const bv = b[prop];
        if (cfg.type === 'number') return (av - bv) * dir;
        if (cfg.type === 'date') {
          const tsKey = `_${prop}Ts`;
          return ((a[tsKey] || a._dateTs) - (b[tsKey] || b._dateTs)) * dir;
        }
        const sortKey = `_sort${prop.charAt(0).toUpperCase()}${prop.slice(1)}`;
        const sa = a[sortKey] !== undefined ? a[sortKey] : String(av).toLowerCase();
        const sb = b[sortKey] !== undefined ? b[sortKey] : String(bv).toLowerCase();
        return sa.localeCompare(sb) * dir;
      });
    }

    _reorder() {
      const allSorted = this._sortCards(this.cards);
      const frag = document.createDocumentFragment();

      if (this.sectionHeadings.length > 0) {
        const isDefaultSort =
          this.config.defaultSort && this.state.sort.key === this.config.defaultSort;

        if (isDefaultSort) {
          const sectionOrder = this.sectionHeadings.map(h => h.dataset.sectionHeading);
          sectionOrder.forEach(section => {
            const heading = this.sectionHeadings.find(
              h => h.dataset.sectionHeading === section
            );
            frag.appendChild(heading);
            allSorted.filter(c => c.section === section).forEach(c => frag.appendChild(c.el));
          });
        } else {
          this.sectionHeadings.forEach(h => frag.appendChild(h));
          allSorted.forEach(c => frag.appendChild(c.el));
        }
      } else {
        allSorted.forEach(c => frag.appendChild(c.el));
      }

      this.container.appendChild(frag);
    }

    _render(visibleCards) {
      const visibleSet = new Set(visibleCards.map(c => c.el));

      this.cards.forEach(c => {
        c.el.classList.toggle('hidden', !visibleSet.has(c.el));
      });

      if (this.sectionHeadings.length > 0) {
        const isDefaultSort =
          this.config.defaultSort && this.state.sort.key === this.config.defaultSort;
        this.sectionHeadings.forEach(h => {
          if (!isDefaultSort) {
            h.classList.add('hidden');
          } else {
            const section = h.dataset.sectionHeading;
            const hasVisible = visibleCards.some(c => c.section === section);
            h.classList.toggle('hidden', !hasVisible);
          }
        });
      }

      if (this._needsReorder) {
        this._reorder();
        this._needsReorder = false;
      }
    }

    _applyFilters() {
      const tokens = [];
      const raw = this.state.search.toLowerCase();
      const re = /"([^"]*)"|\S+/g;
      let m;
      while ((m = re.exec(raw)) !== null) {
        const t = m[1] !== undefined ? m[1] : m[0];
        if (t) tokens.push(t);
      }

      const sortKey = this.state.sort.key;
      const sortDir = this.state.sort.direction;
      if (sortKey !== this._lastSortKey || sortDir !== this._lastSortDir) {
        this._needsReorder = true;
        this._lastSortKey = sortKey;
        this._lastSortDir = sortDir;
      }

      let visible = this.cards.filter(
        c => this._matchesSearch(c, tokens) && this._matchesFilters(c)
      );

      visible = this._sortCards(visible);
      this._render(visible);
      this._updateCount(visible.length);
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

    _updateCount(count) {
      if (!this.controlsEl) return;
      const countEl = this.controlsEl.querySelector('[data-filter-count]');
      const totalEl = this.controlsEl.querySelector('[data-filter-total]');
      if (countEl) countEl.textContent = count;
      if (totalEl) totalEl.textContent = this.totalCount;
    }

    _updateURL() {
      const params = new URLSearchParams();

      const defaultSortCfg = this.config.sort
        ? this.config.sort.find(s => s.default) || this.config.sort[0]
        : null;
      const defaultSortKey = defaultSortCfg ? defaultSortCfg.key : '';

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

      const qs = params.toString();
      const url = qs ? `${window.location.pathname}?${qs}` : window.location.pathname;
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
      const defaultSortCfg = this.config.sort
        ? this.config.sort.find(s => s.default) || this.config.sort[0]
        : null;
      if (defaultSortCfg) {
        this.state.sort.key = defaultSortCfg.key;
        this.state.sort.direction = defaultSortCfg.direction || 'asc';
      }
      for (const key of Object.keys(this.state.filters)) {
        this.state.filters[key] = new Set();
      }

      if (this.controlsEl) {
        const searchInput = this.controlsEl.querySelector('[data-filter-search]');
        if (searchInput) searchInput.value = '';

        const sortSelect = this.controlsEl.querySelector('[data-filter-sort]');
        if (sortSelect && defaultSortCfg) sortSelect.value = defaultSortCfg.key;

        this.controlsEl.querySelectorAll('[data-filter-group]').forEach(btn => {
          btn.classList.remove('bg-blue-600', 'text-white', 'border-blue-600');
          btn.classList.add('bg-white', 'text-gray-700', 'border-gray-300');
        });
      }

      this._applyFilters();
    }
  }

  function init() {
    const containers = document.querySelectorAll('[data-card-container]');
    if (!containers.length) return;
    containers.forEach(el => new CardManager(el));
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
