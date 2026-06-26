(function() {
  'use strict';

  const images = document.querySelectorAll('[data-gallery-group]');
  if (!images.length) return;

  // Build group index
  const groups = {};
  images.forEach(img => {
    const group = img.dataset.galleryGroup;
    if (!groups[group]) groups[group] = [];
    groups[group].push(img);
  });

  let currentGroup = null;
  let currentIndex = 0;

  // Create lightbox DOM
  const lightbox = document.createElement('div');
  lightbox.id = 'gallery-lightbox';
  lightbox.className = 'fixed inset-0 z-50 hidden items-center justify-center bg-blue-900/90 transition-opacity duration-300 opacity-0';
  lightbox.innerHTML = `
    <button class="gallery-lb-close absolute top-3 right-3 md:top-4 md:right-4 text-white text-4xl hover:text-gray-300 transition-colors z-10" aria-label="Close">
      <svg class="w-8 h-8 md:w-10 md:h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
      </svg>
    </button>
    <button class="gallery-lb-prev absolute left-2 md:left-4 top-1/2 -translate-y-1/2 text-white hover:text-gray-300 transition-colors z-10 p-2" aria-label="Previous image">
      <svg class="w-8 h-8 md:w-10 md:h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
      </svg>
    </button>
    <button class="gallery-lb-next absolute right-2 md:right-4 top-1/2 -translate-y-1/2 text-white hover:text-gray-300 transition-colors z-10 p-2" aria-label="Next image">
      <svg class="w-8 h-8 md:w-10 md:h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
      </svg>
    </button>
    <div class="gallery-lb-content flex flex-col items-center transition-transform duration-300 ease-out">
      <picture class="gallery-lb-picture transition-opacity duration-200" style="display:block">
        <source class="gallery-lb-source-webp" type="image/webp">
        <source class="gallery-lb-source-jpeg" type="image/jpeg">
        <img class="gallery-lb-img" alt="">
      </picture>
      <iframe class="gallery-lb-pdf hidden transition-opacity duration-200" frameborder="0"></iframe>
      <div class="gallery-lb-bar flex items-center justify-between px-4 py-2 bg-white text-base text-gray-700 md:rounded-b-lg">
        <span class="gallery-lb-caption"></span>
        <span class="gallery-lb-counter whitespace-nowrap ml-4"></span>
      </div>
    </div>
  `;
  document.body.appendChild(lightbox);

  const lbContent = lightbox.querySelector('.gallery-lb-content');
  const lbPicture = lightbox.querySelector('.gallery-lb-picture');
  const lbSourceWebp = lightbox.querySelector('.gallery-lb-source-webp');
  const lbSourceJpeg = lightbox.querySelector('.gallery-lb-source-jpeg');
  const lbImg = lightbox.querySelector('.gallery-lb-img');
  const lbPdf = lightbox.querySelector('.gallery-lb-pdf');
  const lbBar = lightbox.querySelector('.gallery-lb-bar');
  const lbCaption = lightbox.querySelector('.gallery-lb-caption');
  const lbCounter = lightbox.querySelector('.gallery-lb-counter');
  const btnClose = lightbox.querySelector('.gallery-lb-close');
  const btnPrev = lightbox.querySelector('.gallery-lb-prev');
  const btnNext = lightbox.querySelector('.gallery-lb-next');

  var MARGIN = 20;
  var BAR_HEIGHT = 44;
  var isPdfShowing = false;

  function syncLayout() {
    var isMobile = window.innerWidth < 768;

    if (isMobile) {
      lbContent.style.width = '100vw';
      lbContent.style.height = '100vh';

      if (isPdfShowing) {
        lbPdf.style.width = '100%';
        lbPdf.style.height = 'calc(100% - ' + BAR_HEIGHT + 'px)';
      } else {
        lbPicture.style.width = '100%';
        lbPicture.style.height = 'calc(100% - ' + BAR_HEIGHT + 'px)';
        lbImg.style.width = '100%';
        lbImg.style.height = '100%';
        lbImg.style.objectFit = 'contain';
      }
      lbBar.style.width = '100%';
      return;
    }

    var maxW = window.innerWidth - MARGIN * 2;
    var maxH = window.innerHeight - MARGIN * 2 - BAR_HEIGHT;

    if (isPdfShowing) {
      // PDFs get fixed dimensions
      var w = Math.min(maxW, 1000);
      var h = maxH;
      lbPdf.style.width = w + 'px';
      lbPdf.style.height = h + 'px';
      lbBar.style.width = w + 'px';
      lbContent.style.width = '';
      lbContent.style.height = '';
      return;
    }

    if (!lbImg.naturalWidth || !lbImg.naturalHeight) return;

    var imgRatio = lbImg.naturalWidth / lbImg.naturalHeight;

    var w, h;
    if (maxW / maxH > imgRatio) {
      h = maxH;
      w = Math.floor(h * imgRatio);
    } else {
      w = maxW;
      h = Math.floor(w / imgRatio);
    }

    lbPicture.style.width = w + 'px';
    lbPicture.style.height = h + 'px';
    lbImg.style.width = '100%';
    lbImg.style.height = '100%';
    lbImg.style.objectFit = 'contain';
    lbBar.style.width = w + 'px';
    lbContent.style.width = '';
    lbContent.style.height = '';
  }

  lbImg.addEventListener('load', syncLayout);
  window.addEventListener('resize', function() {
    if (!lightbox.classList.contains('hidden')) syncLayout();
  });

  function open(group, index) {
    currentGroup = group;
    currentIndex = index;

    // Prepare content while hidden
    lightbox.classList.remove('hidden');
    lightbox.classList.add('flex');
    lightbox.classList.add('opacity-0');

    showInitial(() => {
      // Content is ready, now fade in
      requestAnimationFrame(() => {
        lightbox.classList.remove('opacity-0');
        lightbox.classList.add('opacity-100');
        lbContent.style.transform = 'scale(0.95)';
        requestAnimationFrame(() => {
          lbContent.style.transform = 'scale(1)';
        });
      });
    });

    document.body.style.overflow = 'hidden';
  }

  var LB_SIZES = '(max-width: 768px) 100vw, 80vw';

  function showInitial(callback) {
    // Initial show - set up content immediately without fade, then callback
    updateContent();
    // Give browser time to layout before callback
    requestAnimationFrame(() => {
      requestAnimationFrame(callback);
    });
  }

  function updateContent() {
    // Shared logic for setting content (used by showInitial and show)
    const items = groups[currentGroup];
    const img = items[currentIndex];
    const pdfUrl = img.dataset.galleryPdf || '';
    const pdfPage = img.dataset.galleryPdfPage || '1';

    if (pdfUrl) {
      isPdfShowing = true;
      lbPicture.classList.add('hidden');
      lbPdf.classList.remove('hidden');
      lbPdf.src = pdfUrl + '#page=' + pdfPage;
      lbCaption.textContent = img.dataset.galleryCaption || '';
      lbCounter.textContent = items.length > 1 ? `${currentIndex + 1} / ${items.length}` : '';
      syncLayout();
    } else {
      isPdfShowing = false;
      lbPdf.classList.add('hidden');
      lbPicture.classList.remove('hidden');

      const srcsetWebp = img.dataset.gallerySrcsetWebp || '';
      const srcsetJpeg = img.dataset.gallerySrcsetJpeg || '';

      if (srcsetWebp) {
        lbSourceWebp.setAttribute('srcset', srcsetWebp);
        lbSourceWebp.setAttribute('sizes', LB_SIZES);
      } else {
        lbSourceWebp.removeAttribute('srcset');
        lbSourceWebp.removeAttribute('sizes');
      }

      if (srcsetJpeg) {
        lbSourceJpeg.setAttribute('srcset', srcsetJpeg);
        lbSourceJpeg.setAttribute('sizes', LB_SIZES);
      } else {
        lbSourceJpeg.removeAttribute('srcset');
        lbSourceJpeg.removeAttribute('sizes');
      }

      lbImg.src = img.dataset.gallerySrc;
      lbImg.alt = img.alt || '';
      lbCaption.textContent = img.dataset.galleryCaption || '';
      lbCounter.textContent = items.length > 1 ? `${currentIndex + 1} / ${items.length}` : '';
    }

    const single = items.length <= 1;
    btnPrev.classList.toggle('hidden', single);
    btnNext.classList.toggle('hidden', single);
  }

  function show() {
    // Fade out current content
    const activeElement = isPdfShowing ? lbPdf : lbPicture;
    activeElement.style.opacity = '0';

    // Wait for fade out, then switch content
    setTimeout(() => {
      // Determine what we're switching to
      const items = groups[currentGroup];
      const img = items[currentIndex];
      const pdfUrl = img.dataset.galleryPdf || '';
      const willShowPdf = !!pdfUrl;

      // Pre-set opacity to 0 before showing new content to avoid flash
      if (willShowPdf) {
        lbPdf.style.opacity = '0';
      } else {
        lbPicture.style.opacity = '0';
      }

      // Update content
      updateContent();

      // Fade in new content after layout
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          if (willShowPdf) {
            lbPdf.style.opacity = '1';
          } else {
            lbPicture.style.opacity = '1';
          }
        });
      });
    }, 200); // Match transition duration
  }

  function close() {
    // Fade out
    lightbox.classList.remove('opacity-100');
    lightbox.classList.add('opacity-0');
    lbContent.style.transform = 'scale(0.95)';

    // Wait for animation, then clean up
    setTimeout(() => {
      lightbox.classList.add('hidden');
      lightbox.classList.remove('flex');
      document.body.style.overflow = '';
      lbSourceWebp.removeAttribute('srcset');
      lbSourceWebp.removeAttribute('sizes');
      lbSourceJpeg.removeAttribute('srcset');
      lbSourceJpeg.removeAttribute('sizes');
      lbImg.src = '';
      lbPdf.src = '';
      isPdfShowing = false;
      lbImg.style.width = '';
      lbImg.style.height = '';
      lbPdf.style.width = '';
      lbPdf.style.height = '';
      lbPicture.style.width = '';
      lbPicture.style.height = '';
      lbPicture.style.opacity = '';
      lbPdf.style.opacity = '';
      lbBar.style.width = '';
      lbContent.style.width = '';
      lbContent.style.height = '';
      lbContent.style.transform = '';
    }, 300); // Match transition duration
  }

  function prev() {
    const items = groups[currentGroup];
    currentIndex = (currentIndex - 1 + items.length) % items.length;
    show();
  }

  function next() {
    const items = groups[currentGroup];
    currentIndex = (currentIndex + 1) % items.length;
    show();
  }

  // Touch swipe support
  let touchStartX = 0;
  let touchStartY = 0;
  let touchMoved = false;

  lightbox.addEventListener('touchstart', function(e) {
    touchStartX = e.changedTouches[0].clientX;
    touchStartY = e.changedTouches[0].clientY;
    touchMoved = false;
  }, { passive: true });

  lightbox.addEventListener('touchmove', function() {
    touchMoved = true;
  }, { passive: true });

  lightbox.addEventListener('touchend', function(e) {
    if (!touchMoved) return;
    const dx = e.changedTouches[0].clientX - touchStartX;
    const dy = e.changedTouches[0].clientY - touchStartY;
    if (Math.abs(dx) < 50 || Math.abs(dy) > Math.abs(dx)) return;
    if (dx > 0) prev();
    else next();
  }, { passive: true });

  // Attach click handlers to thumbnails
  images.forEach(img => {
    img.addEventListener('click', function() {
      const group = this.dataset.galleryGroup;
      const index = groups[group].indexOf(this);
      open(group, index);
    });

    img.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  });

  btnClose.addEventListener('click', close);
  btnPrev.addEventListener('click', prev);
  btnNext.addEventListener('click', next);

  lightbox.addEventListener('click', function(e) {
    if (e.target === lightbox) close();
  });

  document.addEventListener('keydown', function(e) {
    if (lightbox.classList.contains('hidden')) return;
    if (e.key === 'Escape') close();
    else if (e.key === 'ArrowLeft') prev();
    else if (e.key === 'ArrowRight') next();
  });
})();
