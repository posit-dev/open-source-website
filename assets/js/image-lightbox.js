// Image Lightbox for blog post images

(function() {
  'use strict';

  // Create lightbox modal
  const lightbox = document.createElement('div');
  lightbox.id = 'image-lightbox';
  lightbox.className = 'fixed inset-0 z-50 hidden items-center justify-center bg-blue-100/80 transition-opacity';
  lightbox.innerHTML = `
    <button id="lightbox-close" class="absolute top-4 right-4 text-gray-700 text-4xl font-light hover:text-gray-900 transition-colors z-10" aria-label="Close lightbox">
      <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
      </svg>
    </button>
    <img id="lightbox-image" class="max-w-[90vw] max-h-[90vh] object-contain" alt="">
    <iframe id="lightbox-pdf" class="max-w-[90vw] max-h-[90vh] w-full h-full hidden" frameborder="0"></iframe>
  `;
  document.body.appendChild(lightbox);

  const lightboxImg = document.getElementById('lightbox-image');
  const lightboxPdf = document.getElementById('lightbox-pdf');
  const closeBtn = document.getElementById('lightbox-close');

  // Find all images in prose content and cheatsheet thumbnails
  const proseImages = document.querySelectorAll('.prose img:not(a img), .cheatsheet-thumbnail img');

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
      // Check if this is a cheatsheet thumbnail with a PDF
      const pdfUrl = this.dataset.pdfUrl;

      if (pdfUrl) {
        // Show PDF in iframe
        lightboxPdf.src = pdfUrl;
        lightboxPdf.classList.remove('hidden');
        lightboxImg.classList.add('hidden');
      } else {
        // Show image
        lightboxImg.src = this.src;
        lightboxImg.alt = this.alt || '';
        lightboxImg.classList.remove('hidden');
        lightboxPdf.classList.add('hidden');
      }

      lightbox.classList.remove('hidden');
      lightbox.classList.add('flex');
      document.body.style.overflow = 'hidden';
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
    lightbox.style.opacity = '0';
    setTimeout(function() {
      lightbox.classList.add('hidden');
      lightbox.classList.remove('flex');
      lightbox.style.opacity = '';
      document.body.style.overflow = '';
      // Clear sources
      lightboxImg.src = '';
      lightboxPdf.src = '';
    }, 200);
  }

  closeBtn.addEventListener('click', closeLightbox);

  // Close on background click
  lightbox.addEventListener('click', function(e) {
    if (e.target === lightbox) {
      closeLightbox();
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && !lightbox.classList.contains('hidden')) {
      closeLightbox();
    }
  });
})();
