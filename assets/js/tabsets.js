// Initialize Tabby.js for all tabsets with group synchronization
document.addEventListener('DOMContentLoaded', function() {
  var tabbyInstances = {};
  var tablists = document.querySelectorAll('.panel-tabset-tabby');
  var syncing = false;

  tablists.forEach(function(tablist) {
    tabbyInstances[tablist.id] = new Tabby('#' + tablist.id);
  });

  // Sync tabs within groups
  document.addEventListener('tabby', function(event) {
    if (syncing) return;

    var clickedTab = event.target;
    var tabset = clickedTab.closest('.panel-tabset');
    var group = tabset && tabset.dataset.tabsetGroup;

    if (!group) return;

    syncing = true;
    var tabTitle = clickedTab.textContent.trim();
    var scrollY = window.scrollY;

    // Find all other tabsets in the same group
    var groupTabsets = document.querySelectorAll('[data-tabset-group="' + group + '"]');
    groupTabsets.forEach(function(otherTabset) {
      if (otherTabset === tabset) return;

      var otherTablist = otherTabset.querySelector('.panel-tabset-tabby');
      if (!otherTablist || !tabbyInstances[otherTablist.id]) return;

      var matchingTab = Array.from(otherTablist.querySelectorAll('a')).find(function(a) {
        return a.textContent.trim() === tabTitle;
      });

      if (matchingTab && matchingTab.getAttribute('aria-selected') !== 'true') {
        tabbyInstances[otherTablist.id].toggle(matchingTab);
      }
    });

    // Restore scroll position after all toggles
    window.scrollTo(window.scrollX, scrollY);
    syncing = false;
  }, false);
});
