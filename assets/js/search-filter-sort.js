(function () {
  'use strict';

  function debounce(fn, ms) {
    let id;
    return function (...args) {
      clearTimeout(id);
      id = setTimeout(() => fn.apply(this, args), ms);
    };
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
      this.pageSize = 60;

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
          }
          this._updateShowBtnLabel();
          this._updateURL();
        });
      }

      this.state = {
        search: '',
        sort: { key: '', direction: 'asc' },
        filters: {},
      };

      if (this.config.filters) {
        this.config.filters.forEach(f => {
          this.state.filters[f.key] = new Set();
        });
      }

      this._defaultSortCfg = this.config.sort
        ? this.config.sort.find(s => s.default) || this.config.sort[0]
        : null;
      this._filterCfgMap = {};
      if (this.config.filters) {
        this.config.filters.forEach(f => {
          this._filterCfgMap[f.key] = {
            aliases: f.aliases || {},
            otherExcludes: f.other ? new Set(f.other) : null,
          };
        });
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
      // Fetch item index JSON
      const indexUrl = window.location.pathname.replace(/\/$/, '') + '/item-index.json';
      let index = [];
      try {
        const res = await fetch(indexUrl);
        if (res.ok) index = await res.json();
      } catch (e) {
        // Fall back to empty index
      }

      // Build items array from JSON
      this.items = index.map(entry => {
        // Pre-compute search index and sort keys
        const searchIndex = (entry.searchIndex || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
        const sortTitle = (entry.title || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase().replace(/[^a-z0-9 ]/g, '').trim();
        const dateTs = entry.date ? new Date(entry.date).getTime() : 0;
        const firstCommitTs = entry.firstCommit ? new Date(entry.firstCommit).getTime() : 0;

        return {
          ...entry,
          // Arrays for filter matching (join for backwards-compat with comma-split logic)
          _categoriesStr: (entry.categories || []).join(','),
          _languagesStr: (entry.languages || []).join(','),
          _tagsStr: (entry.tags || []).join(','),
          _softwareStr: (entry.software || []).join(','),
          _typeStr: entry.type || '',
          // Search and sort
          _search: searchIndex,
          _sortTitle: sortTitle,
          _dateTs: dateTs,
          _firstCommitTs: firstCommitTs,
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

      // Tags (combination of software + categories + tags)
      const allTags = [
        ...(entry.software || []),
        ...(entry.categories || []),
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

      const sortSelect = this.controlsEl.querySelector('[data-filter-sort]');
      if (sortSelect) {
        sortSelect.value = this.state.sort.key || (this._defaultSortCfg ? this._defaultSortCfg.key : '');
        sortSelect.addEventListener('change', () => {
          const key = sortSelect.value;
          const cfg = this.config.sort.find(s => s.key === key);
          this.state.sort.key = key;
          this.state.sort.direction = cfg ? (cfg.direction || 'asc') : 'asc';
          this._applyFilters();
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
          panel.classList.toggle('hidden');
        });
        panel.addEventListener('click', (e) => e.stopPropagation());
      });

      document.addEventListener('click', () => {
        if (!this.controlsEl) return;
        this.controlsEl.querySelectorAll('[data-filter-panel]').forEach(p => {
          p.classList.add('hidden');
        });
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

    _matchesSearch(item, tokens) {
      if (!tokens.length) return true;
      return tokens.every(t => item._search.includes(t));
    }

    _matchesFilters(item) {
      for (const [key, activeSet] of Object.entries(this.state.filters)) {
        if (activeSet.size === 0) continue;
        const cfg = this._filterCfgMap[key] || {};
        const aliases = cfg.aliases || {};
        const otherExcludes = cfg.otherExcludes || null;

        // Get values from the appropriate string field
        const strKey = '_' + key + 'Str';
        const rawStr = item[strKey] !== undefined ? item[strKey] : (item[key] || '');
        const values = typeof rawStr === 'string'
          ? rawStr.split(',').map(v => v.trim()).filter(Boolean)
          : (Array.isArray(rawStr) ? rawStr : []);

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
      const cfg = this.config.sort ? this.config.sort.find(s => s.key === key) : null;
      if (!cfg) return items;
      const dir = direction === 'desc' ? -1 : 1;
      const prop = key.replace(/-([a-z])/g, (_, c) => c.toUpperCase());

      return items.slice().sort((a, b) => {
        if (cfg.type === 'number') {
          return ((a[prop] || 0) - (b[prop] || 0)) * dir;
        }
        if (cfg.type === 'date') {
          const tsKey = '_' + prop + 'Ts';
          return ((a[tsKey] || a._dateTs) - (b[tsKey] || b._dateTs)) * dir;
        }
        const sortKey = '_sort' + prop.charAt(0).toUpperCase() + prop.slice(1);
        const sa = a[sortKey] !== undefined ? a[sortKey] : String(a[prop] || '').toLowerCase();
        const sb = b[sortKey] !== undefined ? b[sortKey] : String(b[prop] || '').toLowerCase();
        return sa.localeCompare(sb) * dir;
      });
    }

    _applyFilters() {
      const tokens = [];
      const raw = this.state.search.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
      const re = /"([^"]*)"|\S+/g;
      let m;
      while ((m = re.exec(raw)) !== null) {
        const t = m[1] !== undefined ? m[1] : m[0];
        if (t) tokens.push(t);
      }

      // Filter all items at data level
      let filtered = this.items.filter(
        item => this._matchesSearch(item, tokens) && this._matchesFilters(item)
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
      // Remove all children but keep them in renderedMap for reuse
      while (this.container.firstChild) {
        this.container.removeChild(this.container.firstChild);
      }
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

        const sortSelect = this.controlsEl.querySelector('[data-filter-sort]');
        if (sortSelect && this._defaultSortCfg) sortSelect.value = this._defaultSortCfg.key;

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
