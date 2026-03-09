(function() {
  let pagefind = null;
  let selectedIndex = -1;
  let lastSearchResults = null;

  const modal = document.getElementById('search-modal');
  const backdrop = document.getElementById('search-backdrop');
  const searchInput = document.getElementById('search-input');
  const searchLoading = document.getElementById('search-loading');
  const searchEmpty = document.getElementById('search-empty');
  const searchNoResults = document.getElementById('search-no-results');
  const searchResultsList = document.getElementById('search-results-list');
  const searchResultsHeader = document.getElementById('search-results-header');
  const resultsCountText = document.getElementById('results-count-text');

  const searchToggle = document.getElementById('search-toggle');
  const searchToggleMobile = document.getElementById('search-toggle-mobile');

  const filterCheckboxes = document.querySelectorAll('#search-filters input[type="checkbox"]');

  const countElements = {
    'Software': document.getElementById('count-software'),
    'People': document.getElementById('count-people'),
    'Events': document.getElementById('count-events'),
    'Resources': document.getElementById('count-resources'),
    'Blog': document.getElementById('count-blog'),
    'Other': document.getElementById('count-other')
  };

  const mobileFilterToggle = document.getElementById('mobile-filter-toggle');
  const mobileFilterIcon = document.getElementById('mobile-filter-icon');
  const searchFilters = document.getElementById('search-filters');

  const selectAllButton = document.getElementById('select-all-filters');
  const clearAllButton = document.getElementById('clear-all-filters');

  async function initPagefind() {
    if (!pagefind) {
      pagefind = await import('/pagefind/pagefind.js');
      pagefind.options({
        ranking: {
          termSaturation: 0.25
        }
      });
    }
    return pagefind;
  }

  function getSelectedFilters() {
    const selected = [];
    filterCheckboxes.forEach(checkbox => {
      if (checkbox.checked) {
        selected.push(checkbox.value);
      }
    });
    return selected;
  }

  function saveFilterState() {
    const selected = getSelectedFilters();
    localStorage.setItem('search-filters', JSON.stringify(selected));
  }

  function restoreFilterState() {
    try {
      const saved = localStorage.getItem('search-filters');
      if (saved) {
        const selectedTypes = JSON.parse(saved);
        filterCheckboxes.forEach(checkbox => {
          checkbox.checked = false;
        });
        filterCheckboxes.forEach(checkbox => {
          if (selectedTypes.includes(checkbox.value)) {
            checkbox.checked = true;
          }
        });
      }
    } catch (e) {
      console.error('Error restoring filter state:', e);
    }
  }

  function updateFilterCounts(filters) {
    Object.keys(countElements).forEach(type => {
      if (countElements[type]) {
        countElements[type].textContent = '(0)';
      }
      const checkbox = document.querySelector(`input[value="${type}"]`);
      if (checkbox) {
        checkbox.disabled = false;
        checkbox.parentElement.parentElement.classList.remove('opacity-50');
      }
    });

    if (filters && filters.type) {
      Object.keys(filters.type).forEach(type => {
        if (countElements[type]) {
          const count = filters.type[type];
          countElements[type].textContent = `(${count})`;

          const checkbox = document.querySelector(`input[value="${type}"]`);
          if (checkbox && count === 0 && !checkbox.checked) {
            checkbox.disabled = true;
            checkbox.parentElement.parentElement.classList.add('opacity-50');
          }
        }
      });
    }
  }

  function updateResultsHeader(totalResults) {
    if (!searchResultsHeader || !resultsCountText) return;

    if (totalResults === 0) {
      searchResultsHeader.classList.add('hidden');
      return;
    }

    const selectedTypes = getSelectedFilters();
    const typesText = selectedTypes.length === 6
      ? 'all types'
      : selectedTypes.join(', ');

    const resultWord = totalResults === 1 ? 'result' : 'results';
    resultsCountText.textContent = `Showing ${totalResults} ${resultWord} in ${typesText}`;
    searchResultsHeader.classList.remove('hidden');
  }

  function openModal() {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    restoreFilterState();
    setTimeout(() => {
      searchInput.focus();
    }, 100);
  }

  function closeModal() {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    searchInput.value = '';
    clearResults();
    selectedIndex = -1;
    lastSearchResults = null;
  }

  function clearResults() {
    searchResultsList.innerHTML = '';
    searchLoading.classList.add('hidden');
    searchEmpty.classList.remove('hidden');
    searchNoResults.classList.add('hidden');

    if (searchResultsHeader) {
      searchResultsHeader.classList.add('hidden');
    }

    Object.values(countElements).forEach(el => {
      if (el) el.textContent = '(0)';
    });
  }

  function showLoading() {
    searchEmpty.classList.add('hidden');
    searchNoResults.classList.add('hidden');
    searchLoading.classList.remove('hidden');
  }

  function showNoResults() {
    searchLoading.classList.add('hidden');
    searchEmpty.classList.add('hidden');
    searchNoResults.classList.remove('hidden');
    searchResultsList.innerHTML = '';
    if (searchResultsHeader) {
      searchResultsHeader.classList.add('hidden');
    }
  }

  function createResultItem(result, index) {
    const li = document.createElement('li');
    li.className = 'search-result-item cursor-pointer';
    li.dataset.index = index;
    li.dataset.url = result.url;

    const link = document.createElement('a');
    link.href = result.url;
    link.className = 'flex gap-3 px-4 py-3 hover:bg-blue-50 dark:hover:bg-blue-900 transition-colors';

    if (result.meta.image) {
      const imageContainer = document.createElement('div');
      imageContainer.className = 'flex-none w-16 h-16 rounded overflow-hidden';

      const img = document.createElement('img');
      img.src = result.meta.image;
      img.alt = result.meta.title || '';
      img.className = 'w-full h-full object-contain';
      img.loading = 'lazy';

      imageContainer.appendChild(img);
      link.appendChild(imageContainer);
    }

    const contentContainer = document.createElement('div');
    contentContainer.className = 'flex-1 min-w-0';

    const titleRow = document.createElement('div');
    titleRow.className = 'flex items-start justify-between gap-2';

    const title = document.createElement('div');
    title.className = 'text-sm font-medium text-gray-900 dark:text-gray-100';
    title.innerHTML = result.meta.title || 'Untitled';

    const score = document.createElement('div');
    score.className = 'text-xs text-gray-500 dark:text-gray-400 flex-shrink-0';
    score.textContent = result._score ? result._score.toFixed(2) : '0.00';

    titleRow.appendChild(title);
    titleRow.appendChild(score);

    const excerpt = document.createElement('div');
    excerpt.className = 'mt-1 text-sm text-gray-600 dark:text-gray-400 line-clamp-2';
    excerpt.innerHTML = result.excerpt || '';

    contentContainer.appendChild(titleRow);
    contentContainer.appendChild(excerpt);
    link.appendChild(contentContainer);
    li.appendChild(link);

    return li;
  }

  const MAX_DISPLAYED_RESULTS = 50;

  async function performSearch(query) {
    if (!query || query.trim() === '') {
      clearResults();
      lastSearchResults = null;
      return;
    }

    showLoading();

    try {
      const pf = await initPagefind();

      const selectedTypes = getSelectedFilters();

      if (selectedTypes.length === 0) {
        // Still run unfiltered search for counts
        const unfilteredSearch = await pf.search(query);
        updateFilterCounts(unfilteredSearch.filters);
        showNoResults();
        return;
      }

      // Run unfiltered (for counts) and single filtered search in parallel
      const [unfilteredSearch, filteredSearch] = await Promise.all([
        pf.search(query),
        pf.search(query, {
          filters: { type: { any: selectedTypes } }
        })
      ]);

      updateFilterCounts(unfilteredSearch.filters);

      const topResults = filteredSearch.results.slice(0, MAX_DISPLAYED_RESULTS);

      if (topResults.length === 0) {
        showNoResults();
        return;
      }

      // Resolve only the top results, in parallel
      const combinedResults = await Promise.all(
        topResults.map(async (result) => {
          const data = await result.data();
          data._score = result.score;
          return data;
        })
      );

      lastSearchResults = { results: combinedResults };

      searchLoading.classList.add('hidden');
      searchEmpty.classList.add('hidden');
      searchNoResults.classList.add('hidden');
      searchResultsList.innerHTML = '';

      for (const [index, data] of combinedResults.entries()) {
        const resultItem = createResultItem(data, index);
        searchResultsList.appendChild(resultItem);
      }

      updateResultsHeader(combinedResults.length);

      selectedIndex = -1;
    } catch (error) {
      console.error('Search error:', error);
      showNoResults();
    }
  }

  function updateSelection() {
    const items = searchResultsList.querySelectorAll('.search-result-item');
    items.forEach((item, index) => {
      if (index === selectedIndex) {
        item.querySelector('a').classList.add('bg-blue-100', 'dark:bg-blue-800');
        item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      } else {
        item.querySelector('a').classList.remove('bg-blue-100', 'dark:bg-blue-800');
      }
    });
  }

  function navigateToSelected() {
    const items = searchResultsList.querySelectorAll('.search-result-item');
    if (selectedIndex >= 0 && selectedIndex < items.length) {
      const url = items[selectedIndex].dataset.url;
      window.location.href = url;
    }
  }

  if (searchToggle) {
    searchToggle.addEventListener('click', openModal);
  }
  if (searchToggleMobile) {
    searchToggleMobile.addEventListener('click', openModal);
  }

  if (backdrop) {
    backdrop.addEventListener('click', closeModal);
  }

  if (mobileFilterToggle && searchFilters) {
    mobileFilterToggle.addEventListener('click', () => {
      const isHidden = searchFilters.classList.contains('hidden');
      if (isHidden) {
        searchFilters.classList.remove('hidden');
        mobileFilterIcon.style.transform = 'rotate(180deg)';
      } else {
        searchFilters.classList.add('hidden');
        mobileFilterIcon.style.transform = 'rotate(0deg)';
      }
    });
  }

  let searchTimeout;
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        performSearch(e.target.value);
      }, 300);
    });
  }

  filterCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', () => {
      saveFilterState();
      const query = searchInput.value;
      if (query && query.trim() !== '') {
        performSearch(query);
      }
    });
  });

  if (selectAllButton) {
    selectAllButton.addEventListener('click', () => {
      filterCheckboxes.forEach(checkbox => {
        checkbox.checked = true;
      });
      saveFilterState();
      const query = searchInput.value;
      if (query && query.trim() !== '') {
        performSearch(query);
      }
    });
  }

  if (clearAllButton) {
    clearAllButton.addEventListener('click', () => {
      filterCheckboxes.forEach(checkbox => {
        checkbox.checked = false;
      });
      saveFilterState();
      const query = searchInput.value;
      if (query && query.trim() !== '') {
        performSearch(query);
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      e.preventDefault();
      closeModal();
      return;
    }

    if (modal.classList.contains('hidden')) {
      return;
    }

    const items = searchResultsList.querySelectorAll('.search-result-item');
    const maxIndex = items.length - 1;

    if (items.length === 0) {
      return;
    }

    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        selectedIndex = Math.min(selectedIndex + 1, maxIndex);
        updateSelection();
        break;

      case 'ArrowUp':
        e.preventDefault();
        selectedIndex = Math.max(selectedIndex - 1, -1);
        updateSelection();
        break;

      case 'Enter':
        e.preventDefault();
        navigateToSelected();
        break;
    }
  });

  if (searchResultsList) {
    searchResultsList.addEventListener('click', (e) => {
      const resultItem = e.target.closest('.search-result-item');
      if (resultItem) {
        const url = resultItem.dataset.url;
        window.location.href = url;
      }
    });
  }
})();
