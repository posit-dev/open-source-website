(function() {
  let pagefind = null;
  let selectedIndex = -1;

  // Modal elements
  const modal = document.getElementById('search-modal');
  const backdrop = document.getElementById('search-backdrop');
  const searchInput = document.getElementById('search-input');
  const searchLoading = document.getElementById('search-loading');
  const searchEmpty = document.getElementById('search-empty');
  const searchNoResults = document.getElementById('search-no-results');
  const searchResultsList = document.getElementById('search-results-list');

  // Toggle buttons
  const searchToggle = document.getElementById('search-toggle');
  const searchToggleMobile = document.getElementById('search-toggle-mobile');

  // Initialize Pagefind
  async function initPagefind() {
    if (!pagefind) {
      pagefind = await import('/pagefind/pagefind.js');
    }
    return pagefind;
  }

  // Open modal
  function openModal() {
    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';
    setTimeout(() => {
      searchInput.focus();
    }, 100);
  }

  // Close modal
  function closeModal() {
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    searchInput.value = '';
    clearResults();
    selectedIndex = -1;
  }

  // Clear results
  function clearResults() {
    searchResultsList.innerHTML = '';
    searchLoading.classList.add('hidden');
    searchEmpty.classList.remove('hidden');
    searchNoResults.classList.add('hidden');
  }

  // Show loading state
  function showLoading() {
    searchEmpty.classList.add('hidden');
    searchNoResults.classList.add('hidden');
    searchLoading.classList.remove('hidden');
  }

  // Show no results
  function showNoResults() {
    searchLoading.classList.add('hidden');
    searchEmpty.classList.add('hidden');
    searchNoResults.classList.remove('hidden');
    searchResultsList.innerHTML = '';
  }

  // Create result item HTML
  function createResultItem(result, index) {
    const li = document.createElement('li');
    li.className = 'search-result-item cursor-pointer';
    li.dataset.index = index;
    li.dataset.url = result.url;

    const link = document.createElement('a');
    link.href = result.url;
    link.className = 'flex gap-3 px-4 py-3 hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors';

    // Image (if available)
    if (result.meta.image) {
      const imageContainer = document.createElement('div');
      imageContainer.className = 'flex-none w-16 h-16 rounded overflow-hidden bg-gray-100 dark:bg-gray-700';

      const img = document.createElement('img');
      img.src = result.meta.image;
      img.alt = result.meta.title || '';
      img.className = 'w-full h-full object-cover';
      img.loading = 'lazy';

      imageContainer.appendChild(img);
      link.appendChild(imageContainer);
    }

    // Content container
    const contentContainer = document.createElement('div');
    contentContainer.className = 'flex-1 min-w-0';

    // Title
    const title = document.createElement('div');
    title.className = 'text-sm font-medium text-gray-900 dark:text-gray-100';
    title.innerHTML = result.meta.title || 'Untitled';

    // Excerpt
    const excerpt = document.createElement('div');
    excerpt.className = 'mt-1 text-sm text-gray-600 dark:text-gray-400 line-clamp-2';
    excerpt.innerHTML = result.excerpt || '';

    contentContainer.appendChild(title);
    contentContainer.appendChild(excerpt);
    link.appendChild(contentContainer);
    li.appendChild(link);

    return li;
  }

  // Perform search
  async function performSearch(query) {
    if (!query || query.trim() === '') {
      clearResults();
      return;
    }

    showLoading();

    try {
      const pf = await initPagefind();
      const search = await pf.search(query);

      if (search.results.length === 0) {
        showNoResults();
        return;
      }

      // Load and display results
      searchLoading.classList.add('hidden');
      searchEmpty.classList.add('hidden');
      searchNoResults.classList.add('hidden');
      searchResultsList.innerHTML = '';

      // Limit to first 10 results
      const resultsToShow = search.results.slice(0, 10);

      for (const [index, result] of resultsToShow.entries()) {
        const data = await result.data();
        const resultItem = createResultItem(data, index);
        searchResultsList.appendChild(resultItem);
      }

      selectedIndex = -1;
    } catch (error) {
      console.error('Search error:', error);
      showNoResults();
    }
  }

  // Update selected result
  function updateSelection() {
    const items = searchResultsList.querySelectorAll('.search-result-item');
    items.forEach((item, index) => {
      if (index === selectedIndex) {
        item.querySelector('a').classList.add('bg-gray-50', 'dark:bg-gray-700');
        item.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
      } else {
        item.querySelector('a').classList.remove('bg-gray-50', 'dark:bg-gray-700');
      }
    });
  }

  // Navigate to selected result
  function navigateToSelected() {
    const items = searchResultsList.querySelectorAll('.search-result-item');
    if (selectedIndex >= 0 && selectedIndex < items.length) {
      const url = items[selectedIndex].dataset.url;
      window.location.href = url;
    }
  }

  // Event Listeners

  // Open modal on button click
  if (searchToggle) {
    searchToggle.addEventListener('click', openModal);
  }
  if (searchToggleMobile) {
    searchToggleMobile.addEventListener('click', openModal);
  }

  // Close modal on backdrop click
  if (backdrop) {
    backdrop.addEventListener('click', closeModal);
  }

  // Handle search input
  let searchTimeout;
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(() => {
        performSearch(e.target.value);
      }, 300); // Debounce 300ms
    });
  }

  // Keyboard navigation
  document.addEventListener('keydown', (e) => {
    // ESC to close modal
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
      e.preventDefault();
      closeModal();
      return;
    }

    // Only handle other keys if modal is open
    if (modal.classList.contains('hidden')) {
      return;
    }

    const items = searchResultsList.querySelectorAll('.search-result-item');
    const maxIndex = items.length - 1;

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

  // Click on result
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
