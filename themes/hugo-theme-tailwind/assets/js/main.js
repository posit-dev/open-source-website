(function() {
  const navbarMenuToggle = document.getElementById('navbar-menu-toggle');
  const navbarMenu = document.getElementById('navbar-menu');
  const navbarLangToggle =
    document.getElementById("navbar-lang-toggle") ||
    document.createElement("div"); // fix #56
  const navbarLang = document.getElementById('navbar-lang');

  document.addEventListener('click', function (event) {
    const target = event.target;
    if (navbarMenuToggle.contains(target)) {
      navbarLang && navbarLang.classList.add('hidden');
      navbarMenu && navbarMenu.classList.toggle('hidden');
    } else if (navbarLangToggle.contains(target)) {
      navbarMenu && navbarMenu.classList.add('hidden');
      navbarLang && navbarLang.classList.toggle('hidden');
    } else {
      navbarMenu && navbarMenu.classList.add('hidden');
      navbarLang && navbarLang.classList.add('hidden');
    }
  });
})();
