/* Studio Dudin — site behaviour. Nothing here hides content if it fails. */
(function () {
  // Mobile menu
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Contact form: the site is static (GitHub Pages), so the form composes an
  // email in the visitor's own mail app instead of posting to a server.
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements;
      var subject = 'Studio Dudin — ' + (f.company.value ? f.company.value : f.name.value);
      var body = [
        'Name: ' + f.name.value,
        'Email: ' + f.email.value,
        'Company: ' + (f.company.value || '—'),
        'Stage: ' + f.stage.value,
        'Interested in: ' + f.interest.value,
        '',
        f.message.value
      ].join('\n');
      var href = 'mailto:' + form.getAttribute('data-to') +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
      window.location.href = href;
      var status = document.getElementById('form-status');
      if (status) status.textContent = 'Your email app should open with the message ready to send. If it doesn’t, write to ' + form.getAttribute('data-to') + ' directly.';
    });
  }

  // Gentle reveal on scroll — skipped under reduced motion.
  try {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (!('IntersectionObserver' in window)) return;
    var targets = document.querySelectorAll('section:not(.hero):not(.page-hero) .wrap > *');
    if (!targets.length) return;
    document.body.classList.add('js-reveal');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { entry.target.classList.add('is-visible'); io.unobserve(entry.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    targets.forEach(function (el) { el.classList.add('reveal'); io.observe(el); });
  } catch (err) { /* fail safe: content stays visible */ }
})();
