// Initialize Tabby.js for all tabsets
document.addEventListener('DOMContentLoaded', function() {
  var tablists = document.querySelectorAll('.panel-tabset-tabby');
  tablists.forEach(function(tablist) {
    new Tabby('#' + tablist.id);
  });
});
