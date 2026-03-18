(function() {
  const toc = document.querySelector('.blog-toc');
  if (!toc) return;

  const tocLinks = toc.querySelectorAll('a');
  const headings = [];

  // Build a map of heading IDs to TOC links
  tocLinks.forEach(link => {
    const id = link.getAttribute('href')?.slice(1); // Remove the '#'
    if (id) {
      const heading = document.getElementById(id);
      if (heading) {
        headings.push({ element: heading, link: link });
      }
    }
  });

  if (headings.length === 0) return;

  // Hide all nested lists immediately on page load
  const allNestedUls = toc.querySelectorAll('.blog-toc-content ul > li > ul');
  allNestedUls.forEach(ul => {
    ul.classList.remove('expanded');
  });

  // Function to show/hide nested items based on active H2
  function updateNestedVisibility(activeLink) {
    // Hide all nested ul elements first
    const allNestedUls = toc.querySelectorAll('.blog-toc-content ul > li > ul');
    allNestedUls.forEach(ul => {
      ul.classList.remove('expanded');
    });

    if (activeLink) {
      // Find the parent li of the active link
      const activeLi = activeLink.closest('li');

      // Check if this is a top-level item (H2) by checking if it has a nested ul
      const hasNestedUl = activeLi.querySelector(':scope > ul');

      // Also check if this li's parent ul is directly under TableOfContents (top-level)
      const parentUl = activeLi.parentElement;
      const isTopLevel = parentUl && parentUl.parentElement &&
                        parentUl.parentElement.id === 'TableOfContents';

      if (isTopLevel) {
        // This is an H2 - show its nested ul (H3s)
        if (hasNestedUl) {
          hasNestedUl.classList.add('expanded');
        }
      } else {
        // This is an H3 - find and show its parent ul
        const parentNestedUl = activeLi.closest('.blog-toc-content ul > li > ul');
        if (parentNestedUl) {
          parentNestedUl.classList.add('expanded');
        }
      }
    }
  }

  // Intersection Observer to track which heading is visible
  const observerOptions = {
    rootMargin: '-80px 0px -80% 0px', // Trigger when heading is near top of viewport
    threshold: 0
  };

  let activeLink = null;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        // Find the corresponding TOC link
        const heading = headings.find(h => h.element === entry.target);
        if (heading) {
          // Remove active class from all links
          tocLinks.forEach(link => link.classList.remove('active'));

          // Add active class to current link only
          heading.link.classList.add('active');
          activeLink = heading.link;

          // Update nested item visibility
          updateNestedVisibility(activeLink);
        }
      }
    });
  }, observerOptions);

  // Observe all headings
  headings.forEach(heading => {
    observer.observe(heading.element);
  });

  // Initial state: hide all nested items
  updateNestedVisibility(null);

  // Handle clicks on TOC links for smooth scrolling
  tocLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          const offsetTop = target.getBoundingClientRect().top + window.pageYOffset - 80;
          window.scrollTo({
            top: offsetTop,
            behavior: 'smooth'
          });
        }
      }
    });
  });
})();
