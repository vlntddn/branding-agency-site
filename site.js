/* Studio Dudin — monochrome site behavior.
   Safe by default: if this script fails to run, or the viewer has asked
   for reduced motion, nothing here ever hides content — the CSS only
   reveals-on-scroll under body.js-reveal, which this file alone adds. */
(function () {
  try {
    var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // Mobile nav toggle already runs inline per-page; nothing to do here.

    if (reduceMotion) return;

    document.documentElement.classList.add('js-ready');
    document.body.classList.add('js-reveal');

    if ('IntersectionObserver' in window) {
      var targets = document.querySelectorAll('section:not(.hero) .wrap > *, .index-row');
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-visible');
            io.unobserve(entry.target);
          }
        });
      }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
      targets.forEach(function (el) { io.observe(el); });
    } else {
      // No IntersectionObserver support — reveal everything immediately.
      document.querySelectorAll('section:not(.hero) .wrap > *, .index-row').forEach(function (el) {
        el.classList.add('is-visible');
      });
    }

    // Subtle cursor-kinetic effect on the hero headline — a few pixels of
    // parallax, nothing more. Skipped entirely under reduced motion above.
    var heroH1 = document.querySelector('.hero h1');
    if (heroH1) {
      heroH1.style.transition = 'transform 0.3s ' + 'cubic-bezier(0.16, 1, 0.3, 1)';
      window.addEventListener('mousemove', function (e) {
        var cx = window.innerWidth / 2;
        var cy = window.innerHeight / 2;
        var dx = (e.clientX - cx) / cx;
        var dy = (e.clientY - cy) / cy;
        heroH1.style.transform = 'translate(' + (dx * 6).toFixed(2) + 'px, ' + (dy * 4).toFixed(2) + 'px)';
      }, { passive: true });
    }
  } catch (err) {
    // Fail silent and safe — content stays visible via the default CSS.
  }
})();
