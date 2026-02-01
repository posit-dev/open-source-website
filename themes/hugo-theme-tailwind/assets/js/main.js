(function() {
  const navbarMenuToggle = document.getElementById('navbar-menu-toggle');
  const navbarMenu = document.getElementById('navbar-menu');
  const navbarMenuContent = document.getElementById('navbar-menu-content');
  const menuIconHamburger = document.getElementById('menu-icon-hamburger');
  const menuIconClose = document.getElementById('menu-icon-close');
  const navbarLangToggle =
    document.getElementById("navbar-lang-toggle") ||
    document.createElement("div"); // fix #56
  const navbarLang = document.getElementById('navbar-lang');

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
    }
  }

  function openMenu() {
    if (navbarMenu && isMobile()) {
      navbarMenu.style.height = 'calc(100vh - 5rem)';
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
})();
