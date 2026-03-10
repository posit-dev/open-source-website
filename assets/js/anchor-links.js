document.addEventListener('DOMContentLoaded', function() {
    const headings=document.querySelectorAll('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]');

    headings.forEach(heading=> {
        heading.classList.add('heading-anchor');

        const anchor=document.createElement('a');
        anchor.href='#' + heading.id;
        anchor.className='anchor-link';
        anchor.setAttribute('aria-label', 'Link to this section');
        anchor.innerHTML=' #';

        heading.appendChild(anchor);
      });
  });
