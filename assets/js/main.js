(function() {
  const navbarMenuToggle = document.getElementById('navbar-menu-toggle');
  const navbarMenu = document.getElementById('navbar-menu');
  const navbarMenuContent = document.getElementById('navbar-menu-content');
  const navbarMenuBg = document.getElementById('navbar-menu-bg');
  const siteHeader = document.getElementById('site-header');
  const menuIconHamburger = document.getElementById('menu-icon-hamburger');
  const menuIconClose = document.getElementById('menu-icon-close');
  const navbarLangToggle =
    document.getElementById("navbar-lang-toggle") ||
    document.createElement("div"); // fix #56
  const navbarLang = document.getElementById('navbar-lang');
  const isHomePage = navbarMenu && navbarMenu.dataset.isHome === 'true';

  function isMobile() {
    return window.innerWidth < 768; // 768px is Tailwind's md breakpoint
  }

  function closeMenu() {
    if (navbarMenu && isMobile()) {
      navbarMenu.style.height = '0';
      if (navbarMenuContent) navbarMenuContent.style.opacity = '0';
      if (menuIconHamburger) menuIconHamburger.classList.remove('hidden');
      if (menuIconClose) menuIconClose.classList.add('hidden');
      // Re-enable body scroll
      document.body.style.overflow = '';
      // Reset background to yellow-50 on homepage
      if (isHomePage) {
        if (navbarMenuBg) {
          navbarMenuBg.classList.remove('bg-white');
          navbarMenuBg.classList.add('bg-yellow-50');
        }
        if (siteHeader) {
          siteHeader.classList.remove('bg-white');
        }
      }
    }
  }

  function openMenu() {
    if (navbarMenu && isMobile()) {
      navbarMenu.style.height = 'calc(100vh - 5rem)';
      // Change background to white on homepage when menu opens
      if (isHomePage) {
        if (navbarMenuBg) {
          navbarMenuBg.classList.remove('bg-yellow-50');
          navbarMenuBg.classList.add('bg-white');
        }
        if (siteHeader) {
          siteHeader.classList.add('bg-white');
        }
      }
      // Delay content fade-in slightly so background animates first
      setTimeout(() => {
        if (navbarMenuContent) navbarMenuContent.style.opacity = '1';
      }, 100);
      if (menuIconHamburger) menuIconHamburger.classList.add('hidden');
      if (menuIconClose) menuIconClose.classList.remove('hidden');
      // Prevent body scroll when menu is open
      document.body.style.overflow = 'hidden';
    }
  }

  function toggleMenu() {
    const isOpen = navbarMenu && navbarMenu.style.height && navbarMenu.style.height !== '0' && navbarMenu.style.height !== '0px';
    if (isOpen) {
      closeMenu();
    } else {
      openMenu();
    }
  }

  // Clear inline styles when resizing to desktop
  window.addEventListener('resize', function() {
    if (!isMobile() && navbarMenu) {
      navbarMenu.style.height = '';
      if (navbarMenuContent) navbarMenuContent.style.opacity = '';
      document.body.style.overflow = '';
      // Reset background to yellow-50 on homepage
      if (isHomePage) {
        if (navbarMenuBg) {
          navbarMenuBg.classList.remove('bg-white');
          navbarMenuBg.classList.add('bg-yellow-50');
        }
        if (siteHeader) {
          siteHeader.classList.remove('bg-white');
        }
      }
    }
  });

  document.addEventListener('click', function (event) {
    if (!isMobile()) return; // Only handle clicks on mobile

    const target = event.target;
    if (navbarMenuToggle && navbarMenuToggle.contains(target)) {
      navbarLang && navbarLang.classList.add('hidden');
      toggleMenu();
    } else if (navbarLangToggle.contains(target)) {
      closeMenu();
      navbarLang && navbarLang.classList.toggle('hidden');
    } else {
      closeMenu();
      navbarLang && navbarLang.classList.add('hidden');
    }
  });

  // Dropdown menu handling
  document.addEventListener('DOMContentLoaded', function() {
    const dropdowns = document.querySelectorAll('.dropdown-toggle');

    dropdowns.forEach(function(toggle) {
      const menu = toggle.nextElementSibling;
      const listItem = toggle.parentElement;

      // Desktop: hover behavior
      if (!isMobile()) {
        listItem.addEventListener('mouseenter', function() {
          menu.classList.remove('hidden');
          toggle.setAttribute('aria-expanded', 'true');
        });

        listItem.addEventListener('mouseleave', function() {
          menu.classList.add('hidden');
          toggle.setAttribute('aria-expanded', 'false');
        });
      }

      // Mobile: click behavior
      toggle.addEventListener('click', function(e) {
        if (isMobile()) {
          e.preventDefault();
          const isExpanded = toggle.getAttribute('aria-expanded') === 'true';

          // Close all other dropdowns
          document.querySelectorAll('.dropdown-menu').forEach(function(m) {
            if (m !== menu) {
              m.classList.add('hidden');
              m.previousElementSibling.setAttribute('aria-expanded', 'false');
            }
          });

          // Toggle this dropdown
          if (isExpanded) {
            menu.classList.add('hidden');
            toggle.setAttribute('aria-expanded', 'false');
          } else {
            menu.classList.remove('hidden');
            toggle.setAttribute('aria-expanded', 'true');
          }
        }
      });
    });

    // Handle window resize
    let lastMobileState = isMobile();
    window.addEventListener('resize', function() {
      const currentMobileState = isMobile();
      if (lastMobileState !== currentMobileState) {
        // Reset all dropdowns when switching between mobile/desktop
        document.querySelectorAll('.dropdown-menu').forEach(function(menu) {
          menu.classList.add('hidden');
          menu.previousElementSibling.setAttribute('aria-expanded', 'false');
        });
        lastMobileState = currentMobileState;
      }
    });
  });
})();
