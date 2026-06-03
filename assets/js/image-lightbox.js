// Image Lightbox for blog post images

(function() {
  'use strict';

  // Create lightbox modal
  const lightbox = document.createElement('div');
  lightbox.id = 'image-lightbox';
  lightbox.className = 'fixed inset-0 z-50 hidden items-center justify-center bg-blue-100/80 transition-opacity';
  lightbox.innerHTML = `
    <div role="dialog" aria-modal="true" aria-label="Image lightbox" class="contents">
      <button id="lightbox-close" class="absolute top-4 right-4 text-gray-700 text-4xl font-light hover:text-gray-900 transition-colors z-10" aria-label="Close lightbox">
        <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
      <div id="lightbox-loading" class="absolute inset-0 flex items-center justify-center text-gray-600 hidden" aria-live="polite">
        <div class="text-center">
          <svg class="animate-spin h-12 w-12 mx-auto mb-2" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          <span>Loading...</span>
        </div>
      </div>
      <div id="lightbox-error" class="absolute inset-0 flex items-center justify-center text-red-600 hidden" role="alert" aria-live="assertive">
        <div class="text-center">
          <p class="text-lg font-medium">Failed to load PDF</p>
          <p class="text-sm mt-2">The file may not exist or cannot be displayed.</p>
        </div>
      </div>
      <img id="lightbox-image" class="max-w-[95vw] max-h-[95vh] md:max-w-[90vw] md:max-h-[90vh] object-contain" alt="">
      <iframe id="lightbox-pdf" class="max-w-[95vw] max-h-[95vh] md:max-w-[90vw] md:max-h-[90vh] w-full h-full hidden" frameborder="0" title="PDF viewer" sandbox="allow-same-origin allow-scripts"></iframe>
      <div id="lightbox-announcement" class="sr-only" role="status" aria-live="polite" aria-atomic="true"></div>
    </div>
  `;
  document.body.appendChild(lightbox);

  const lightboxImg = document.getElementById('lightbox-image');
  const lightboxPdf = document.getElementById('lightbox-pdf');
  const closeBtn = document.getElementById('lightbox-close');
  const loadingIndicator = document.getElementById('lightbox-loading');
  const errorIndicator = document.getElementById('lightbox-error');
  const announcement = document.getElementById('lightbox-announcement');
  let isTransitioning = false;
  let lastFocusedElement = null;
  let pdfLoadTimeout = null;

  // Constants
  const TRANSITION_DURATION = 200;
  const FOCUS_DELAY = 100;
  const PDF_TIMEOUT = 10000;

  // Helper to hide all indicators
  function hideIndicators() {
    errorIndicator.classList.add('hidden');
    loadingIndicator.classList.add('hidden');
  }

  // Find all images in prose content and cheatsheet thumbnails (excluding linked images)
  const proseImages = document.querySelectorAll('.prose img:not(a img), .cheatsheet-thumbnail img:not(a img)');

  proseImages.forEach(img => {
    // Skip images with no-lightbox class
    if (img.classList.contains('no-lightbox')) {
      return;
    }

    // Make images clickable
    img.style.cursor = 'pointer';
    img.setAttribute('role', 'button');
    img.setAttribute('tabindex', '0');

    img.addEventListener('click', function() {
      // Prevent rapid clicks during transition
      if (isTransitioning) return;

      // Save current focus
      lastFocusedElement = document.activeElement;

      // Check if this is a cheatsheet thumbnail with a PDF
      const pdfUrl = this.dataset.pdfUrl;

      // Clear any existing timeout
      if (pdfLoadTimeout) {
        clearTimeout(pdfLoadTimeout);
        pdfLoadTimeout = null;
      }

      // Hide error/loading indicators
      hideIndicators();

      if (pdfUrl) {
        // Show loading indicator
        loadingIndicator.classList.remove('hidden');

        // Show PDF in iframe
        lightboxPdf.src = pdfUrl;
        lightboxPdf.classList.remove('hidden');
        lightboxImg.classList.add('hidden');

        // Handle PDF load
        lightboxPdf.onload = function() {
          loadingIndicator.classList.add('hidden');
          announcement.textContent = 'PDF loaded';
        };

        // Handle PDF error
        lightboxPdf.onerror = function() {
          loadingIndicator.classList.add('hidden');
          errorIndicator.classList.remove('hidden');
          announcement.textContent = 'Failed to load PDF';
        };

        // Timeout for slow loads
        pdfLoadTimeout = setTimeout(function() {
          if (!loadingIndicator.classList.contains('hidden')) {
            hideIndicators();
            errorIndicator.classList.remove('hidden');
            announcement.textContent = 'PDF load timeout';
          }
          pdfLoadTimeout = null;
        }, PDF_TIMEOUT);
      } else {
        // Show image
        lightboxImg.src = this.src;
        lightboxImg.alt = this.alt || '';
        lightboxImg.classList.remove('hidden');
        lightboxPdf.classList.add('hidden');
        announcement.textContent = 'Image opened in lightbox';
      }

      lightbox.classList.remove('hidden');
      lightbox.classList.add('flex');
      document.body.style.overflow = 'hidden';

      // Focus close button for accessibility
      setTimeout(function() {
        closeBtn.focus();
      }, FOCUS_DELAY);
    });

    // Keyboard support
    img.addEventListener('keydown', function(e) {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        this.click();
      }
    });
  });

  // Close lightbox
  function closeLightbox() {
    if (isTransitioning) return;
    isTransitioning = true;

    announcement.textContent = 'Lightbox closed';
    lightbox.style.opacity = '0';

    // Clear pending timeout
    if (pdfLoadTimeout) {
      clearTimeout(pdfLoadTimeout);
      pdfLoadTimeout = null;
    }

    setTimeout(function() {
      lightbox.classList.add('hidden');
      lightbox.classList.remove('flex');
      lightbox.style.opacity = '';
      document.body.style.overflow = '';

      // Clear sources and stop any loading
      lightboxImg.src = '';

      // Stop PDF loading (cross-browser)
      try {
        if (lightboxPdf.contentWindow) {
          if (lightboxPdf.contentWindow.stop) {
            lightboxPdf.contentWindow.stop();
          } else if (lightboxPdf.contentWindow.document && lightboxPdf.contentWindow.document.execCommand) {
            lightboxPdf.contentWindow.document.execCommand('Stop');
          }
        }
      } catch (e) {
        // Cross-origin iframe access might throw, ignore
      }
      lightboxPdf.src = '';

      // Hide indicators
      hideIndicators();

      // Reset image transform
      lightboxImg.style.transform = '';

      // Restore focus
      if (lastFocusedElement) {
        lastFocusedElement.focus();
        lastFocusedElement = null;
      }

      isTransitioning = false;
    }, TRANSITION_DURATION);
  }

  closeBtn.addEventListener('click', closeLightbox);

  // Close on background click
  lightbox.addEventListener('click', function(e) {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });

  // Close on Escape key and handle focus trap
  document.addEventListener('keydown', function(e) {
    if (lightbox.classList.contains('hidden')) return;

    if (e.key === 'Escape') {
      closeLightbox();
    }

    // Focus trap - keep focus within lightbox
    if (e.key === 'Tab') {
      const focusableElements = lightbox.querySelectorAll('button:not([disabled]), [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      const firstFocusable = focusableElements[0];
      const lastFocusable = focusableElements[focusableElements.length - 1];

      if (e.shiftKey) {
        // Shift + Tab
        if (document.activeElement === firstFocusable) {
          e.preventDefault();
          lastFocusable.focus();
        }
      } else {
        // Tab
        if (document.activeElement === lastFocusable) {
          e.preventDefault();
          firstFocusable.focus();
        }
      }
    }
  });

  // Enable panning for images on mobile
  let panning = false;
  let pointX = 0;
  let pointY = 0;
  let start = { x: 0, y: 0 };

  lightboxImg.addEventListener('touchstart', function(e) {
    if (e.touches.length === 1) {
      start = { x: e.touches[0].clientX - pointX, y: e.touches[0].clientY - pointY };
      panning = true;
    }
  });

  lightboxImg.addEventListener('touchmove', function(e) {
    if (panning && e.touches.length === 1) {
      e.preventDefault();
      pointX = e.touches[0].clientX - start.x;
      pointY = e.touches[0].clientY - start.y;
      this.style.transform = `translate(${pointX}px, ${pointY}px)`;
    }
  });

  lightboxImg.addEventListener('touchend', function() {
    panning = false;
    // Reset position on release for simplicity
    pointX = 0;
    pointY = 0;
    this.style.transform = '';
  });
})();
