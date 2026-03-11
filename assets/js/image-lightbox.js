// Image Lightbox for blog post images

(function() {
  'use strict';

  // Create lightbox modal
  const lightbox = document.createElement('div');
  lightbox.id = 'image-lightbox';
  lightbox.className = 'fixed inset-0 z-50 hidden items-center justify-center bg-blue-100/80 dark:bg-blue-300/25 transition-opacity';
  lightbox.innerHTML = `
    <button id="lightbox-close" class="absolute top-4 right-4 text-gray-700 dark:text-gray-300 text-4xl font-light hover:text-gray-900 dark:hover:text-gray-100 transition-colors z-10" aria-label="Close lightbox">
      <svg class="w-10 h-10" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
      </svg>
    </button>
    <img id="lightbox-image" class="max-w-[90vw] max-h-[90vh] object-contain" alt="">
  `;
  document.body.appendChild(lightbox);

  const lightboxImg = document.getElementById('lightbox-image');
  const closeBtn = document.getElementById('lightbox-close');

  // Find all images in prose content
  const proseImages = document.querySelectorAll('.prose img:not(a img)');

  proseImages.forEach(img => {
    // Make images clickable
    img.style.cursor = 'pointer';
    img.setAttribute('role', 'button');
    img.setAttribute('tabindex', '0');

    img.addEventListener('click', function() {
      lightboxImg.src = this.src;
      lightboxImg.alt = this.alt || '';
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
    lightbox.classList.add('hidden');
    lightbox.classList.remove('flex');
    document.body.style.overflow = '';
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
