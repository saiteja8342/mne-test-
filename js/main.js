/* ═══════════════════════════════════════════════════════════
   MOTIONNODEEDITS — Main JavaScript
   TESTED & BUG-FIXED VERSION
   ═══════════════════════════════════════════════════════════

   BUGS FIXED:
   [B1] cursor:none bleeds onto mobile — fixed via initCursor early return
   [B2] GSAP .to() hero animations run before GSAP plugin registered — registerPlugin moved first
   [B3] Before/After video overflow when dragged narrow — fixed ba-after video sizing
   [B4] ScrollTrigger.update used before gsap.registerPlugin — order fixed
   [B5] initSmoothScroll anchor breaks on href="#" — added guard
   [B6] process-timeline needs position:relative — fixed in CSS
   [B7] form-success layout broken in 2-col grid — fixed via JS grid-column span
   [B8] Work card video play race condition — load() called before play()
   [B9] Preloader delay mismatch — initAll only called once after preloader done
   [B10] Showreel pause event fires when user uses native controls — fixed logic
   ═══════════════════════════════════════════════════════════ */

;(function () {
  'use strict';

  /* ─────────────────── GSAP PLUGIN REGISTRATION (must be first) ─────────────────── */
  // B4 FIX: Register ScrollTrigger before any other init that uses it
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
  }

  /* ─────────────────── PRELOADER ─────────────────── */
  const preloader = document.getElementById('preloader');
  const preloaderFill = document.getElementById('preloaderFill');
  const preloaderPercent = document.getElementById('preloaderPercent');

  let loadProgress = 0;
  let initDone = false; // B9 FIX: Guard against double init

  const loadInterval = setInterval(() => {
    loadProgress += Math.random() * 12 + 3;
    if (loadProgress >= 100) {
      loadProgress = 100;
      clearInterval(loadInterval);
      if (preloaderFill) preloaderFill.style.width = '100%';
      if (preloaderPercent) preloaderPercent.textContent = '100%';
      setTimeout(() => {
        if (preloader) preloader.classList.add('done');
        if (!initDone) {
          initDone = true;
          initAll();
        }
      }, 500);
    } else {
      if (preloaderFill) preloaderFill.style.width = loadProgress + '%';
      if (preloaderPercent) preloaderPercent.textContent = Math.floor(loadProgress) + '%';
    }
  }, 60);

  /* ─────────────────── INIT ALL ─────────────────── */
  function initAll() {
    initCursor();
    initNavbar();
    initMobileMenu();
    initSmoothScroll();    // Lenis first
    initHeroAnimations();  // Hero text reveal
    initScrollReveal();    // Scroll-triggered reveals (uses ScrollTrigger registered above)
    initScrollProgress();
    initCounters();
    initWorkCards();
    initServiceTilt();
    initCardLighting();
    initBeforeAfterSlider();
    initProcessTimeline();
    initTestimonials();
    initShowreel();
    initContactForm();
    initMagneticButtons();
    initParticles();
  }

  /* ─────────────────── CUSTOM CURSOR ─────────────────── */
  function initCursor() {
    // B1 FIX: Completely skip cursor init on touch/small screens
    if (window.innerWidth <= 1024 || 'ontouchstart' in window) return;

    const dot = document.getElementById('cursorDot');
    const ring = document.getElementById('cursorRing');
    if (!dot || !ring) return;

    // Show cursors (hidden by default via CSS opacity:0)
    dot.style.opacity = '1';
    ring.style.opacity = '1';

    let mx = 0, my = 0, rx = 0, ry = 0;
    let started = false;

    window.addEventListener('mousemove', (e) => {
      mx = e.clientX;
      my = e.clientY;
      dot.style.left = mx + 'px';
      dot.style.top = my + 'px';
      if (!started) {
        started = true;
        // Snap ring to position on first move so it doesn't fly in from 0,0
        rx = mx; ry = my;
      }
    });

    (function renderCursor() {
      rx += (mx - rx) * 0.12;
      ry += (my - ry) * 0.12;
      ring.style.left = rx + 'px';
      ring.style.top = ry + 'px';
      requestAnimationFrame(renderCursor);
    })();

    // Hover state
    const hoverSelector = 'a, button, .work-card, .service-card, .social-link, .magnetic, input, textarea';
    document.addEventListener('mouseover', (e) => {
      if (e.target.closest(hoverSelector)) ring.classList.add('hover');
    });
    document.addEventListener('mouseout', (e) => {
      if (e.target.closest(hoverSelector)) ring.classList.remove('hover');
    });

    // Click state
    document.addEventListener('mousedown', () => ring.classList.add('click'));
    document.addEventListener('mouseup', () => ring.classList.remove('click'));
  }

  /* ─────────────────── NAVBAR ─────────────────── */
  function initNavbar() {
    const navbar = document.getElementById('navbar');
    if (!navbar) return;

    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 60);
    }, { passive: true });
  }

  /* ─────────────────── MOBILE MENU ─────────────────── */
  function initMobileMenu() {
    const hamburger = document.getElementById('navHamburger');
    const menu = document.getElementById('mobileMenu');
    if (!hamburger || !menu) return;

    function closeMenu() {
      hamburger.classList.remove('active');
      menu.classList.remove('open');
      document.body.style.overflow = '';
    }

    hamburger.addEventListener('click', () => {
      const isOpen = menu.classList.contains('open');
      if (isOpen) {
        closeMenu();
      } else {
        hamburger.classList.add('active');
        menu.classList.add('open');
        document.body.style.overflow = 'hidden';
      }
    });

    menu.querySelectorAll('.mobile-link').forEach(link => {
      link.addEventListener('click', closeMenu);
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && menu.classList.contains('open')) closeMenu();
    });
  }

  /* ─────────────────── SMOOTH SCROLL (LENIS) ─────────────────── */
  function initSmoothScroll() {
    if (typeof Lenis === 'undefined') return;

    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true
    });

    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add((time) => lenis.raf(time * 1000));
      gsap.ticker.lagSmoothing(0);
    }

    // B5 FIX: Guard against href="#" and invalid selectors
    document.querySelectorAll('a[href^="#"]').forEach(a => {
      a.addEventListener('click', (e) => {
        const href = a.getAttribute('href');
        if (!href || href === '#') return; // Skip bare # links
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          lenis.scrollTo(target, { offset: -80, duration: 1.5 });
        }
      });
    });
  }

  /* ─────────────────── HERO GSAP ANIMATIONS ─────────────────── */
  function initHeroAnimations() {
    if (typeof gsap === 'undefined') return;

    // B2 FIX: Use gsap.fromTo so the start state is controlled by GSAP
    // not by CSS, avoiding conflicts between GSAP and CSS initial values
    const tl = gsap.timeline({ delay: 0.2 });

    // Badge
    tl.fromTo('#heroBadge',
      { opacity: 0, y: 20 },
      { opacity: 1, y: 0, duration: 0.8, ease: 'power3.out' },
      0
    );

    // Heading lines reveal
    tl.fromTo('.hero-heading .line span',
      { y: '110%', opacity: 0 },
      { y: '0%', opacity: 1, duration: 1.2, stagger: 0.12, ease: 'power4.out' },
      0.15
    );

    // Subtitle
    tl.fromTo('.hero-sub',
      { opacity: 0, y: 24 },
      { opacity: 1, y: 0, duration: 1, ease: 'power3.out' },
      0.7
    );

    // CTA buttons
    tl.fromTo('.hero-cta',
      { opacity: 0, y: 24 },
      { opacity: 1, y: 0, duration: 1, ease: 'power3.out' },
      0.9
    );

    // Stats
    tl.fromTo('.hero-stats',
      { opacity: 0, y: 24 },
      { opacity: 1, y: 0, duration: 1, ease: 'power3.out' },
      1.1
    );
  }

  /* ─────────────────── SCROLL REVEAL ─────────────────── */
  function initScrollReveal() {
    const revealEls = document.querySelectorAll('.reveal-up');
    if (!revealEls.length) return;

    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      // ScrollTrigger already registered above (B4 fix)
      revealEls.forEach(el => {
        // Skip hero children — handled separately
        if (el.closest('.hero-content')) return;

        ScrollTrigger.create({
          trigger: el,
          start: 'top 88%',
          once: true,
          onEnter: () => el.classList.add('visible')
        });
      });

      // Section heading animations
      document.querySelectorAll('.split-text').forEach(el => {
        if (el.closest('.hero-content')) return;
        gsap.fromTo(el,
          { y: 60, opacity: 0 },
          {
            y: 0,
            opacity: 1,
            duration: 1.2,
            ease: 'power4.out',
            scrollTrigger: { trigger: el, start: 'top 85%', once: true }
          }
        );
      });
    } else {
      // Fallback: IntersectionObserver
      const obs = new IntersectionObserver((entries) => {
        entries.forEach(e => {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            obs.unobserve(e.target);
          }
        });
      }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
      revealEls.forEach(el => {
        if (!el.closest('.hero-content')) obs.observe(el);
      });
    }
  }

  /* ─────────────────── SCROLL PROGRESS ─────────────────── */
  function initScrollProgress() {
    const bar = document.getElementById('scrollProgress');
    if (!bar) return;

    window.addEventListener('scroll', () => {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      if (h <= 0) return;
      const pct = (window.scrollY / h) * 100;
      bar.style.width = pct + '%';
    }, { passive: true });
  }

  /* ─────────────────── STAT COUNTERS ─────────────────── */
  function initCounters() {
    const counters = document.querySelectorAll('.stat-value[data-target]');
    if (!counters.length) return;

    const obs = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = parseFloat(el.dataset.target);
        if (isNaN(target)) return;

        const duration = 2000;
        const start = performance.now();

        function step(now) {
          const p = Math.min((now - start) / duration, 1);
          const eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.floor(target * eased);
          if (p < 1) requestAnimationFrame(step);
          else el.textContent = target; // Ensure exact final value
        }
        requestAnimationFrame(step);
        obs.unobserve(el);
      });
    }, { threshold: 0.5 });

    counters.forEach(c => obs.observe(c));
  }

  /* ─────────────────── WORK CARDS (HOVER VIDEO) ─────────────────── */
  function initWorkCards() {
    document.querySelectorAll('.work-card').forEach(card => {
      const video = card.querySelector('.work-preview');
      if (!video) return;

      let playing = false;

      card.addEventListener('mouseenter', () => {
        // B8 FIX: Call load() first if not yet loaded, then play
        if (video.readyState === 0) {
          video.load();
        }
        video.play().catch(() => {
          // Autoplay blocked — silently ignore
        });
        playing = true;
      });

      card.addEventListener('mouseleave', () => {
        if (playing) {
          video.pause();
          video.currentTime = 0;
          playing = false;
        }
      });
    });
  }

  /* ─────────────────── SERVICE CARD 3D TILT ─────────────────── */
  function initServiceTilt() {
    if (window.innerWidth <= 768) return;

    document.querySelectorAll('[data-tilt]').forEach(card => {
      card.addEventListener('mouseenter', () => {
        card.style.transition = 'none';
      });

      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const cx = rect.width / 2;
        const cy = rect.height / 2;
        const rotateX = ((y - cy) / cy) * -5;
        const rotateY = ((x - cx) / cx) * 5;

        card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
      });

      card.addEventListener('mouseleave', () => {
        card.style.transition = 'transform 0.6s cubic-bezier(.16,1,.3,1), border-color 0.5s, box-shadow 0.5s';
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
        // Reset transition after animation completes
        setTimeout(() => { card.style.transition = ''; }, 650);
      });
    });
  }

  /* ─────────────────── CARD LIGHTING ─────────────────── */
  function initCardLighting() {
    document.querySelectorAll('.glass-card').forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - rect.left) + 'px');
        card.style.setProperty('--my', (e.clientY - rect.top) + 'px');
      });
    });
  }

  /* ─────────────────── BEFORE / AFTER SLIDER ─────────────────── */
  function initBeforeAfterSlider() {
    const slider = document.getElementById('baSlider');
    const handle = document.getElementById('baHandle');
    if (!slider || !handle) return;

    const afterEl = slider.querySelector('.ba-after');
    if (!afterEl) return;

    let dragging = false;

    function move(clientX) {
      const rect = slider.getBoundingClientRect();
      let x = clientX - rect.left;
      // Clamp with small margin so labels are always visible
      x = Math.max(30, Math.min(x, rect.width - 30));
      const pct = (x / rect.width) * 100;
      afterEl.style.width = pct + '%';
      handle.style.left = pct + '%';
    }

    // Mouse events
    slider.addEventListener('mousedown', (e) => {
      dragging = true;
      move(e.clientX);
      e.preventDefault(); // Prevent text selection while dragging
    });

    // Touch events
    slider.addEventListener('touchstart', (e) => {
      dragging = true;
      move(e.touches[0].clientX);
    }, { passive: true });

    window.addEventListener('mousemove', (e) => { if (dragging) move(e.clientX); }, { passive: true });
    window.addEventListener('touchmove', (e) => { if (dragging) move(e.touches[0].clientX); }, { passive: true });
    window.addEventListener('mouseup', () => { dragging = false; });
    window.addEventListener('touchend', () => { dragging = false; });
  }

  /* ─────────────────── PROCESS TIMELINE ─────────────────── */
  function initProcessTimeline() {
    if (typeof gsap === 'undefined' || typeof ScrollTrigger === 'undefined') {
      // Fallback: activate all steps if no GSAP
      document.querySelectorAll('.process-step').forEach(s => s.classList.add('active'));
      return;
    }

    const fill = document.getElementById('processLineFill');
    if (fill) {
      gsap.to(fill, {
        height: '100%',
        ease: 'none',
        scrollTrigger: {
          trigger: '.process-timeline',
          start: 'top 65%',
          end: 'bottom 35%',
          scrub: 1.5
        }
      });
    }

    document.querySelectorAll('.process-step').forEach(step => {
      ScrollTrigger.create({
        trigger: step,
        start: 'top 62%',
        onEnter: () => step.classList.add('active'),
        onLeaveBack: () => step.classList.remove('active')
      });
    });
  }

  /* ─────────────────── TESTIMONIALS (AUTO SLIDE) ─────────────────── */
  function initTestimonials() {
    const track = document.getElementById('testimonialTrack');
    if (!track) return;

    // Clone original cards for seamless infinite loop
    const originals = Array.from(track.querySelectorAll('.testimonial-card'));
    if (originals.length === 0) return;

    originals.forEach(card => {
      const clone = card.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });
  }

  /* ─────────────────── SHOWREEL ─────────────────── */
  function initShowreel() {
    const video = document.getElementById('showreelVideo');
    const overlay = document.getElementById('showreelOverlay');
    const btn = document.getElementById('showreelPlayBtn');
    if (!video || !overlay || !btn) return;

    function showOverlay() {
      overlay.classList.remove('hidden');
      video.controls = false;
    }

    function hideOverlay() {
      overlay.classList.add('hidden');
      video.controls = true;
    }

    btn.addEventListener('click', () => {
      video.play().then(() => {
        hideOverlay();
      }).catch(() => {
        // Play blocked — keep overlay visible
      });
    });

    // B10 FIX: Only show overlay on ended, not on every pause
    // (native controls cause pause events constantly)
    video.addEventListener('ended', showOverlay);

    // Also show overlay if the video errors
    video.addEventListener('error', showOverlay);
  }

  /* ─────────────────── CONTACT FORM ─────────────────── */
  function initContactForm() {
    const form = document.getElementById('contactForm');
    const success = document.getElementById('formSuccess');
    if (!form) return;

    // B7 FIX: Ensure success card spans full grid width
    if (success) {
      success.style.gridColumn = '1 / -1';
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();

      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.disabled = true;
        const span = submitBtn.querySelector('.btn-text');
        if (span) span.textContent = 'Sending...';
      }

      const data = new FormData(form);

      try {
        const res = await fetch(form.action, {
          method: 'POST',
          body: data,
          headers: { 'Accept': 'application/json' }
        });

        if (res.ok) {
          form.style.display = 'none';
          if (success) {
            success.style.display = 'block';
          }
        } else {
          if (submitBtn) {
            submitBtn.disabled = false;
            const span = submitBtn.querySelector('.btn-text');
            if (span) span.textContent = 'Send Message';
          }
          alert('Something went wrong. Please WhatsApp us directly.');
        }
      } catch {
        if (submitBtn) {
          submitBtn.disabled = false;
          const span = submitBtn.querySelector('.btn-text');
          if (span) span.textContent = 'Send Message';
        }
        alert('Network error. Please WhatsApp us directly.');
      }
    });
  }

  /* ─────────────────── MAGNETIC BUTTONS ─────────────────── */
  function initMagneticButtons() {
    if (window.innerWidth <= 1024 || typeof gsap === 'undefined') return;

    document.querySelectorAll('.magnetic').forEach(el => {
      const strength = parseFloat(el.dataset.strength) || 20;

      el.addEventListener('mousemove', (e) => {
        const rect = el.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        gsap.to(el, {
          x: x * (strength / 100),
          y: y * (strength / 100),
          duration: 0.4,
          ease: 'power2.out'
        });
      });

      el.addEventListener('mouseleave', () => {
        gsap.to(el, {
          x: 0, y: 0,
          duration: 0.7,
          ease: 'elastic.out(1, 0.3)'
        });
      });
    });
  }

  /* ─────────────────── PARTICLES ─────────────────── */
  function initParticles() {
    const container = document.getElementById('heroParticles');
    if (!container) return;

    const canvas = document.createElement('canvas');
    canvas.style.cssText = 'position:absolute;inset:0;width:100%;height:100%;';
    container.appendChild(canvas);
    const ctx = canvas.getContext('2d');

    let w, h;
    const count = Math.min(50, Math.floor(window.innerWidth / 28));
    const particles = [];

    function resize() {
      w = canvas.width = container.offsetWidth;
      h = canvas.height = container.offsetHeight;
    }
    resize();

    const resizeObs = window.ResizeObserver
      ? new ResizeObserver(resize)
      : null;
    if (resizeObs) resizeObs.observe(container);
    else window.addEventListener('resize', resize, { passive: true });

    for (let i = 0; i < count; i++) {
      particles.push({
        x: Math.random() * (w || window.innerWidth),
        y: Math.random() * (h || window.innerHeight),
        vx: (Math.random() - 0.5) * 0.25,
        vy: (Math.random() - 0.5) * 0.25,
        r: Math.random() * 1.5 + 0.5,
        a: Math.random() * 0.2 + 0.04
      });
    }

    let animId;
    function draw() {
      ctx.clearRect(0, 0, w, h);
      particles.forEach(p => {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0) p.x = w;
        else if (p.x > w) p.x = 0;
        if (p.y < 0) p.y = h;
        else if (p.y > h) p.y = 0;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255,255,255,${p.a})`;
        ctx.fill();
      });
      animId = requestAnimationFrame(draw);
    }
    draw();

    // Pause animation when tab is hidden (performance)
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        cancelAnimationFrame(animId);
      } else {
        draw();
      }
    });
  }

})();
