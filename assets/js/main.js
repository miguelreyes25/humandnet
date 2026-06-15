(function () {
  'use strict';

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isTouch = window.matchMedia('(hover: none), (pointer: coarse)').matches;

  /* ---------- Nav: scrolled state + mobile toggle ---------- */
  var nav = document.getElementById('nav');
  var toggle = document.getElementById('navToggle');
  var links = document.querySelector('.nav-links');

  function onScroll() {
    if (window.scrollY > 20) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (toggle && links) {
    toggle.addEventListener('click', function () {
      links.classList.toggle('open');
    });
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () { links.classList.remove('open'); });
    });
  }

  /* ---------- Hero cursor-tilt 3D (Motion A) ---------- */
  var amp = document.getElementById('amp');
  var hero = document.getElementById('hero');
  if (amp && hero && !isTouch && !reduceMotion) {
    hero.addEventListener('mousemove', function (e) {
      var px = e.clientX / window.innerWidth - 0.5;
      var py = e.clientY / window.innerHeight - 0.5;
      amp.style.transform = 'rotateY(' + (px * 28) + 'deg) rotateX(' + (-py * 22) + 'deg) scale(1.03)';
    });
    hero.addEventListener('mouseleave', function () {
      amp.style.transform = '';
    });
  }

  /* ---------- Reduced motion: reveal everything, skip GSAP ---------- */
  if (reduceMotion || typeof gsap === 'undefined') {
    document.querySelectorAll('[data-reveal],[data-reveal-left],[data-reveal-right]').forEach(function (el) {
      el.style.opacity = 1;
      el.style.transform = 'none';
    });
    document.querySelectorAll('[data-count]').forEach(function (el) {
      el.textContent = el.getAttribute('data-count') + (el.getAttribute('data-suffix') || '');
    });
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  /* ---------- Hero entrance: staggered fade-up ---------- */
  gsap.set('.hero [data-anim]', { opacity: 0, y: 24 });
  gsap.to('.hero [data-anim]', {
    opacity: 1, y: 0, duration: 0.8, ease: 'power3.out', stagger: 0.12, delay: 0.15
  });

  /* ---------- Generic reveals on scroll (one-shot) ---------- */
  document.querySelectorAll('[data-reveal]:not(.card)').forEach(function (el) {
    gsap.to(el, {
      opacity: 1, y: 0, duration: 0.7, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 85%', once: true }
    });
  });
  document.querySelectorAll('[data-reveal-left]').forEach(function (el) {
    gsap.to(el, {
      opacity: 1, x: 0, duration: 0.8, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 82%', once: true }
    });
  });
  document.querySelectorAll('[data-reveal-right]').forEach(function (el) {
    gsap.to(el, {
      opacity: 1, x: 0, duration: 0.8, ease: 'power3.out',
      scrollTrigger: { trigger: el, start: 'top 82%', once: true }
    });
  });

  /* ---------- Stagger service cards ---------- */
  ScrollTrigger.batch('.card[data-reveal]', {
    start: 'top 88%',
    once: true,
    onEnter: function (batch) {
      gsap.to(batch, { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out', stagger: 0.1 });
    }
  });

  /* ---------- Stat count-up ---------- */
  document.querySelectorAll('[data-count]').forEach(function (el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var suffix = el.getAttribute('data-suffix') || '';
    var obj = { val: 0 };
    ScrollTrigger.create({
      trigger: el,
      start: 'top 90%',
      once: true,
      onEnter: function () {
        gsap.to(obj, {
          val: target,
          duration: 1.6,
          ease: 'power2.out',
          onUpdate: function () { el.textContent = Math.round(obj.val) + suffix; }
        });
      }
    });
  });

  /* ---------- Subtle parallax on Hôlos image ---------- */
  var holosImg = document.querySelector('.holos-visual img');
  if (holosImg) {
    gsap.to(holosImg, {
      y: -40,
      ease: 'none',
      scrollTrigger: {
        trigger: '.holos',
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    });
  }

  var ctaForm = document.querySelector('.cta-form');
  if (ctaForm) {
    ctaForm.addEventListener('submit', function (e) {
      e.preventDefault();
      var nameEl = ctaForm.querySelector('[aria-label="Nombre"]');
      var emailEl = ctaForm.querySelector('[aria-label="Correo electrónico"]');
      var name = nameEl ? nameEl.value.trim() : '';
      var email = emailEl ? emailEl.value.trim() : '';
      if (!name || !email) return;
      var subject = encodeURIComponent('Demo request — ' + name);
      var body = encodeURIComponent('Nombre: ' + name + '\nEmail: ' + email + '\n\nMe interesa agendar una demo de Hôlos ERP® / CONTPAQi®.');
      window.location.href = 'mailto:ventas@humandnet.com?subject=' + subject + '&body=' + body;
    });
  }
})();
