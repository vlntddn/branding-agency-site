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
    var status = document.getElementById('form-status');
    var button = form.querySelector('button[type=submit]');
    var say = function (t) { if (status) status.textContent = t; };
    var mailtoFallback = function () {
      var f = form.elements;
      var subject = 'Studio Dudin — ' + (f.company.value ? f.company.value : f.name.value);
      var body = ['Name: ' + f.name.value, 'Email: ' + f.email.value, 'Company: ' + (f.company.value || '—'),
        'Stage: ' + f.stage.value, 'Interested in: ' + f.interest.value, '', f.message.value].join('\n');
      window.location.href = 'mailto:' + form.getAttribute('data-to') +
        '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      say('Your email app should open with the message ready to send. If it doesn’t, write to ' + form.getAttribute('data-to') + ' directly.');
    };
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var endpoint = form.getAttribute('data-endpoint');
      if (!endpoint || !window.fetch || !window.URLSearchParams) { mailtoFallback(); return; }
      var data = new URLSearchParams(new FormData(form));
      data.append('page', window.location.href);
      if (button) { button.disabled = true; button.textContent = 'Sending…'; }
      say('');
      fetch(endpoint, { method: 'POST', body: data })
        .then(function (r) { return r.json(); })
        .then(function (res) {
          if (!res || !res.ok) throw new Error('rejected');
          form.reset();
          form.classList.add('is-sent');
          if (button) button.textContent = 'Sent';
          say('Thank you — your message is in. I’ll reply from ' + form.getAttribute('data-to') + ', usually within a day.');
        })
        .catch(function () {
          if (button) { button.disabled = false; button.textContent = 'Send'; }
          say('Something went wrong on my side. Please write to ' + form.getAttribute('data-to') + ' — or press Send again.');
        });
    });
  }

  // Home motion graphics. Decorative only: without JS or with reduced motion
  // the graphics show their finished state and nothing is hidden.
  try {
    var calm = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var NS = 'http://www.w3.org/2000/svg';
    var ease = function (x) { return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
    var clamp = function (x) { return Math.max(0, Math.min(1, x)); };
    var seg = function (t, a, b) { return clamp((t - a) / (b - a)); };

    // 1. Positioning map: one brand steps out of a crowd of look-alikes.
    var map = document.getElementById('viz-map');
    if (map) {
      var svg = map.querySelector('svg');
      var crowd = map.querySelector('[data-crowd]');
      var you = map.querySelector('[data-you]');
      var ring = map.querySelector('[data-ring]');
      var dot = you.querySelector('.map-dot-you');
      var crowdTag = map.querySelector('[data-crowd-tag]');
      var youTag = map.querySelector('[data-you-tag]');
      var open = map.querySelector('[data-open]');
      var stateEl = map.querySelector('[data-state]');
      var CX = 240, CY = 290, TX = 368, TY = 110;
      var seed = 7, rnd = function () { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
      var dots = [];
      for (var i = 0; i < 24; i++) {
        var a = rnd() * Math.PI * 2, r = 12 + Math.sqrt(rnd()) * 66;
        var c = document.createElementNS(NS, 'circle');
        c.setAttribute('class', 'map-dot'); c.setAttribute('r', '5');
        crowd.appendChild(c);
        dots.push({ el: c, x: CX + Math.cos(a) * r, y: CY + Math.sin(a) * r * 0.95, ph: rnd() * 6.28, sp: 0.6 + rnd() * 0.8 });
      }
      var trail = document.createElementNS(NS, 'line');
      trail.setAttribute('class', 'map-trail');
      trail.setAttribute('x1', CX); trail.setAttribute('y1', CY);
      svg.insertBefore(trail, you);
      var guideV = document.createElementNS(NS, 'line'), guideH = document.createElementNS(NS, 'line');
      guideV.setAttribute('class', 'map-guide'); guideH.setAttribute('class', 'map-guide');
      guideV.setAttribute('x1', TX); guideV.setAttribute('x2', TX); guideV.setAttribute('y1', TY); guideV.setAttribute('y2', 420);
      guideH.setAttribute('y1', TY); guideH.setAttribute('y2', TY); guideH.setAttribute('x1', 40); guideH.setAttribute('x2', TX);
      svg.insertBefore(guideV, you); svg.insertBefore(guideH, you);

      var last = '';
      var setState = function (txt) { if (txt !== last) { stateEl.textContent = txt; last = txt; } };
      // Timeline (ms): 0-1600 crowd, 1600-3400 move, 3400-8200 hold, 8200-9800 return.
      var LOOP = 9800;
      var draw = function (t, moving) {
        var out = ease(seg(t, 1600, 3400)), back = ease(seg(t, 8200, 9800)), p = out * (1 - back);
        var x = CX + (TX - CX) * p, y = CY + (TY - CY) * p;
        you.setAttribute('transform', 'translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ')');
        dot.setAttribute('r', (5 + 4.5 * clamp(p * 1.6)).toFixed(2));
        dot.style.opacity = (0.55 + 0.45 * clamp(p * 2)).toFixed(2);
        dot.style.fill = p > 0.02 ? '' : 'var(--gray)';
        trail.setAttribute('x2', x); trail.setAttribute('y2', y);
        trail.style.opacity = clamp(p * 3) * (1 - back);
        var hold = out * (1 - back);
        open.style.opacity = (hold * 0.9).toFixed(2);
        guideV.style.opacity = guideH.style.opacity = (hold * 0.35).toFixed(2);
        crowdTag.style.opacity = (1 - clamp(p * 2.2)).toFixed(2);
        youTag.style.opacity = clamp((p - 0.7) / 0.3).toFixed(2);
        var pulse = ((t % 1600) / 1600);
        ring.setAttribute('r', (12 + pulse * 22).toFixed(1));
        ring.style.opacity = (p > 0.98 ? (1 - pulse) * 0.7 : 0).toFixed(2);
        setState(p > 0.98 ? 'Clear' : p > 0.02 ? 'Positioning' : 'Unclear');
        for (var k = 0; k < dots.length; k++) {
          var d = dots[k], w = moving ? t * 0.0009 * d.sp : 0;
          d.el.setAttribute('cx', (d.x + Math.sin(w + d.ph) * 5).toFixed(1));
          d.el.setAttribute('cy', (d.y + Math.cos(w * 1.2 + d.ph) * 5).toFixed(1));
        }
      };
      if (calm || !window.requestAnimationFrame) {
        draw(5000, false);
      } else {
        var running = false, t0 = 0, raf = 0;
        var frame = function (now) {
          if (!running) return;
          if (!t0) t0 = now;
          draw((now - t0) % LOOP, true);
          raf = requestAnimationFrame(frame);
        };
        var toggle = function (on) {
          if (on && !running) { running = true; t0 = 0; raf = requestAnimationFrame(frame); }
          else if (!on && running) { running = false; cancelAnimationFrame(raf); }
        };
        var inView = true;
        if ('IntersectionObserver' in window) {
          new IntersectionObserver(function (es) { inView = es[0].isIntersecting; toggle(inView && !document.hidden); }, { threshold: 0.05 }).observe(map);
        }
        document.addEventListener('visibilitychange', function () { toggle(inView && !document.hidden); });
        draw(0, true); toggle(true);
      }
    }

    // 2. Chart lines and 3. stat counters play once, when scrolled into view.
    var chart = document.getElementById('viz-chart');
    var statsEl = document.querySelector('.stats');
    if (!calm && 'IntersectionObserver' in window && (chart || statsEl)) {
      document.documentElement.classList.add('viz-on');
      var play = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('is-play');
          if (e.target === statsEl) countUp(statsEl);
          play.unobserve(e.target);
        });
      }, { threshold: 0.35 });
      if (chart) play.observe(chart);
      if (statsEl) play.observe(statsEl);
    }
    function countUp(root) {
      root.querySelectorAll('[data-count]').forEach(function (el) {
        var end = parseFloat(el.getAttribute('data-count')), suf = el.getAttribute('data-suffix') || '', t0 = null;
        el.textContent = '0' + suf;
        var step = function (now) {
          if (t0 === null) t0 = now;
          var k = clamp((now - t0) / 1400);
          el.textContent = Math.round(end * (1 - Math.pow(1 - k, 3))) + suf;
          if (k < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      });
    }
  } catch (err) { /* fail safe: graphics stay in their finished state */ }

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
