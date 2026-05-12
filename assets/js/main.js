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
    } else if (target.closest('.dropdown-toggle') || target.closest('.dropdown-menu')) {
      // Don't close the mobile menu when interacting with dropdowns
    } else {
      closeMenu();
      navbarLang && navbarLang.classList.add('hidden');
    }
  });

  // Dropdown menu handling
  document.addEventListener('DOMContentLoaded', function() {
    function openDropdown(toggle, menu) {
      menu.classList.remove('hidden');
      toggle.setAttribute('aria-expanded', 'true');
      var chevron = toggle.querySelector('.dropdown-chevron');
      if (chevron) chevron.classList.add('rotate-180');
      if (isMobile()) {
        menu.style.maxHeight = menu.scrollHeight + 'px';
      }
    }

    function closeDropdown(toggle, menu) {
      toggle.setAttribute('aria-expanded', 'false');
      var chevron = toggle.querySelector('.dropdown-chevron');
      if (chevron) chevron.classList.remove('rotate-180');
      if (isMobile()) {
        menu.style.maxHeight = '0';
        menu.addEventListener('transitionend', function handler() {
          menu.classList.add('hidden');
          menu.removeEventListener('transitionend', handler);
        });
      } else {
        menu.classList.add('hidden');
      }
    }

    function closeAllDropdowns(exceptMenu) {
      document.querySelectorAll('.dropdown-toggle').forEach(function(otherToggle) {
        var otherMenu = otherToggle.nextElementSibling;
        if (otherMenu !== exceptMenu && otherToggle.getAttribute('aria-expanded') === 'true') {
          closeDropdown(otherToggle, otherMenu);
        }
      });
    }

    document.querySelectorAll('.dropdown-toggle').forEach(function(toggle) {
      var menu = toggle.nextElementSibling;
      var listItem = toggle.parentElement;

      // Desktop: hover behavior
      listItem.addEventListener('mouseenter', function() {
        if (!isMobile()) {
          closeAllDropdowns(menu);
          openDropdown(toggle, menu);
        }
      });

      listItem.addEventListener('mouseleave', function() {
        if (!isMobile()) {
          closeDropdown(toggle, menu);
        }
      });

      // Mobile: click/tap behavior
      toggle.addEventListener('click', function(e) {
        if (isMobile()) {
          e.preventDefault();
          var isExpanded = toggle.getAttribute('aria-expanded') === 'true';

          closeAllDropdowns(menu);

          if (isExpanded) {
            closeDropdown(toggle, menu);
          } else {
            openDropdown(toggle, menu);
          }
        }
      });
    });

    // Handle window resize
    var lastMobileState = isMobile();
    window.addEventListener('resize', function() {
      var currentMobileState = isMobile();
      if (lastMobileState !== currentMobileState) {
        document.querySelectorAll('.dropdown-toggle').forEach(function(toggle) {
          var menu = toggle.nextElementSibling;
          menu.classList.add('hidden');
          menu.style.maxHeight = '';
          toggle.setAttribute('aria-expanded', 'false');
          var chevron = toggle.querySelector('.dropdown-chevron');
          if (chevron) chevron.classList.remove('rotate-180');
        });
        lastMobileState = currentMobileState;
      }
    });
  });
})();
