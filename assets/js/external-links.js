// Automatically open external links in new tab
document.addEventListener('DOMContentLoaded', function() {
  // Get current domain
  const currentDomain = window.location.hostname;

  // Find all links
  const links = document.querySelectorAll('a[href]');

  links.forEach(link => {
    const href = link.getAttribute('href');

    // Skip if already has target attribute
    if (link.hasAttribute('target')) {
      return;
    }

    // Check if it's an external link
    // External = starts with http/https AND not the current domain
    if (href && (href.startsWith('http://') || href.startsWith('https://'))) {
      try {
        const url = new URL(href);
        if (url.hostname !== currentDomain) {
          link.setAttribute('target', '_blank');
          link.setAttribute('rel', 'noopener noreferrer');
        }
      } catch (e) {
        // Invalid URL, skip
      }
    }
  });
});
