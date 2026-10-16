---
academy_url: https://academy.posit.co/path/introduction-to-positron
course_type: learning path
courses:
- navigating-the-positron-interface
- working-with-data-in-positron
- running-and-managing-code-in-positron
date: '2026-07-31'
description: A collection of courses to get started using Positron!
image: image.svg
resource_type: course
software:
- positron
title: Introduction to Positron
weight: 21

external:  # updated automatically, do not edit
  courses:
  - navigating-the-positron-interface
  - working-with-data-in-positron
  - running-and-managing-code-in-positron
  created_at: '2026-07-31T15:10:17.066002Z'
  description: A collection of courses to get started using Positron!
  id: 3gmbmss8v70zy
  image_url: https://everpath-course-content.s3.amazonaws.com/instructor/dfepv3avie8n-posit-academy/path/3gmbmss8v70zy/promo-image.1791515913.svg
  kind: learning path
  modified_at: '2026-10-09T03:18:34.429202Z'
  order: 21
  slug: introduction-to-positron
  software:
  - positron
  title: Introduction to Positron
  url: https://academy.posit.co/path/introduction-to-positron
---

<div id="pa-positron-path-root"></div>
<p>
<script>
  fetch('https://academy-customer.netlify.app/intro-positron-path.html')
    .then(function(r){ return r.text(); })
    .then(function(html){
      var d = document.createElement('div');
      d.innerHTML = html;
      d.querySelectorAll('style').forEach(function(s){
        document.head.appendChild(s.cloneNode(true));
      });
      var root = document.getElementById('pa-positron-path-root');
      if (root) {
        root.innerHTML = d.innerHTML;
        root.querySelectorAll('script').forEach(function(s){
          var n = document.createElement('script');
          n.textContent = s.textContent;
          document.body.appendChild(n);
        });
      }
    })
    .catch(function(e){ console.error('pa-positron-path load error:', e); });
  </script>
</p>
