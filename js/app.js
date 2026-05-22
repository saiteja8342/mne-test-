/* ============================================================
   MOTIONNODEEDITS — app.js
   Clean, modular, production-ready
   ============================================================ */

;(function () {
  'use strict';

  /* ── GSAP plugin registration (always first) ── */
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);
  }

  /* ============================================================
     PRELOADER
     ============================================================ */
  const preEl    = document.getElementById('preloader');
  const preFill  = document.getElementById('preFill');
  let   pct      = 0;
  let   started  = false;

  const pInt = setInterval(() => {
    pct += Math.random() * 14 + 4;
    if (pct >= 100) {
      pct = 100;
      clearInterval(pInt);
      if (preFill) preFill.style.width = '100%';
      setTimeout(() => {
        if (preEl) preEl.classList.add('out');
        if (!started) { started = true; boot(); }
      }, 350);
    } else {
      if (preFill) preFill.style.width = pct + '%';
    }
  }, 55);

  /* ============================================================
     BOOT — called after preloader
     ============================================================ */
  function boot() {
    initCursor();
    initCarouselDrag();
    initNavbar();
    initMobileMenu();
    initLenis();
    initHero();
    initScrollReveal();
    initScrollProgress();
    initCounters();
    initWorkCards();
    initServiceLighting();
    initShowreel();
    initTestimonials();
    initProcess();
    initMagnetics();
    initContactForm();
    initParticles();
  }

  /* ============================================================
     CUSTOM CURSOR
     ============================================================ */
  function initCursor() {
    if (!window.matchMedia('(hover: hover) and (min-width: 1025px)').matches) return;

    const dot  = document.getElementById('cDot');
    const ring = document.getElementById('cRing');
    if (!dot || !ring) return;

    dot.style.opacity = '1';
    ring.style.opacity = '1';

    let mx = 0, my = 0, rx = 0, ry = 0, snap = true;

    window.addEventListener('mousemove', e => {
      mx = e.clientX; my = e.clientY;
      dot.style.left = mx + 'px';
      dot.style.top  = my + 'px';
      if (snap) { rx = mx; ry = my; snap = false; }
    });

    (function loop() {
      rx += (mx - rx) * .12;
      ry += (my - ry) * .12;
      ring.style.left = rx + 'px';
      ring.style.top  = ry + 'px';
      requestAnimationFrame(loop);
    })();

    const sel = 'a, button, [data-mag], .work-card, .svc-card, input, textarea';
    document.addEventListener('mouseover', e => {
      if (e.target.closest(sel)) ring.classList.add('on');
    });
    document.addEventListener('mouseout', e => {
      if (e.target.closest(sel)) ring.classList.remove('on');
    });
    document.addEventListener('mousedown', () => ring.classList.add('tap'));
    document.addEventListener('mouseup',   () => ring.classList.remove('tap'));
  }

  /* ============================================================
     NAVBAR
     ============================================================ */
  
  /* ============================================================
     CAROUSEL DRAG & CURSOR
     ============================================================ */
  function initCarouselDrag() {
    const carousels = document.querySelectorAll('.work-carousel');
    if (!carousels.length) return;

    // Create drag cursor element
    const cDrag = document.createElement('div');
    cDrag.className = 'c-drag';
    cDrag.textContent = 'DRAG';
    document.body.appendChild(cDrag);

    let isDown = false;
    let startX;
    let scrollLeft;

    carousels.forEach(slider => {
      // Drag scrolling
      slider.addEventListener('mousedown', (e) => {
        isDown = true;
        slider.style.scrollSnapType = 'none'; // disable snap while dragging
        startX = e.pageX - slider.offsetLeft;
        scrollLeft = slider.scrollLeft;
      });
      slider.addEventListener('mouseleave', () => {
        isDown = false;
        slider.style.scrollSnapType = 'x mandatory';
        cDrag.classList.remove('on');
      });
      slider.addEventListener('mouseup', () => {
        isDown = false;
        slider.style.scrollSnapType = 'x mandatory';
      });
      slider.addEventListener('mousemove', (e) => {
        // Move custom cursor
        cDrag.style.left = e.clientX + 'px';
        cDrag.style.top = e.clientY + 'px';
        
        if (!isDown) return;
        e.preventDefault();
        const x = e.pageX - slider.offsetLeft;
        const walk = (x - startX) * 2; // scroll speed
        slider.scrollLeft = scrollLeft - walk;
      });

      // Show/hide drag cursor
      slider.addEventListener('mouseenter', () => {
        if(window.matchMedia('(hover: hover) and (min-width: 1025px)').matches) {
          cDrag.classList.add('on');
          // Hide normal c-ring if exists
          const cRing = document.getElementById('cRing');
          if(cRing) cRing.style.opacity = '0';
        }
      });
      slider.addEventListener('mouseleave', () => {
        cDrag.classList.remove('on');
        const cRing = document.getElementById('cRing');
        if(cRing) cRing.style.opacity = '1';
      });
    });
  }

  function initNavbar() {
    const nav = document.getElementById('navbar');
    if (!nav) return;
    window.addEventListener('scroll', () => {
      nav.classList.toggle('stuck', window.scrollY > 40);
    }, { passive: true });
  }

  /* ============================================================
     MOBILE MENU
     ============================================================ */
  function initMobileMenu() {
    const toggle  = document.getElementById('navToggle');
    const drawer  = document.getElementById('drawer');
    if (!toggle || !drawer) return;

    function close() {
      toggle.classList.remove('open');
      drawer.classList.remove('open');
      drawer.setAttribute('aria-hidden', 'true');
      toggle.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    }

    toggle.addEventListener('click', () => {
      const open = drawer.classList.toggle('open');
      toggle.classList.toggle('open', open);
      drawer.setAttribute('aria-hidden', String(!open));
      toggle.setAttribute('aria-expanded', String(open));
      document.body.style.overflow = open ? 'hidden' : '';
    });

    drawer.querySelectorAll('.d-item, .d-cta').forEach(a => a.addEventListener('click', close));
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); });
  }

  /* ============================================================
     LENIS SMOOTH SCROLL
     ============================================================ */
  function initLenis() {
    if (typeof Lenis === 'undefined') return;

    const lenis = new Lenis({
      duration: 1.15,
      easing: t => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true
    });

    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
      lenis.on('scroll', ScrollTrigger.update);
      gsap.ticker.add(t => lenis.raf(t * 1000));
      gsap.ticker.lagSmoothing(0);
    }

    /* Smooth anchor links */
    document.querySelectorAll('a[href^="#"]').forEach(a => {
      a.addEventListener('click', e => {
        const id = a.getAttribute('href');
        if (!id || id === '#') return;
        const target = document.querySelector(id);
        if (target) {
          e.preventDefault();
          lenis.scrollTo(target, { offset: -72, duration: 1.4 });
        }
      });
    });
  }

  /* ============================================================
     HERO ANIMATIONS
     ============================================================ */
  function initHero() {
    /* No-GSAP fallback */
    if (typeof gsap === 'undefined') {
      document.querySelectorAll('.hero-pill, .hero-sub, .hero-actions, .hero-stats').forEach(el => {
        el.style.opacity = '1'; el.style.transform = 'none';
      });
      document.querySelectorAll('.h1-row > *').forEach(el => {
        el.style.transform = 'translateY(0)';
      });
      return;
    }

    const tl = gsap.timeline({ delay: .12 });

    /* Status pill */
    tl.fromTo('.hero-pill',
      { opacity: 0, y: 16 },
      { opacity: 1, y: 0, duration: .65, ease: 'power3.out' },
      0
    );

    /* Heading rows — direct children (span OR em) staggered reveal */
    tl.fromTo('.h1-row > span, .h1-row > em',
      { y: '110%' },
      { y: '0%', duration: 1.05, stagger: .1, ease: 'power4.out' },
      .18
    );

    /* Subtitle */
    tl.fromTo('.hero-sub',
      { opacity: 0, y: 18 },
      { opacity: 1, y: 0, duration: .85, ease: 'power3.out' },
      .72
    );

    /* CTA buttons */
    tl.fromTo('.hero-actions',
      { opacity: 0, y: 18 },
      { opacity: 1, y: 0, duration: .85, ease: 'power3.out' },
      .9
    );

    /* Stats strip */
    tl.fromTo('.hero-stats',
      { opacity: 0, y: 22 },
      { opacity: 1, y: 0, duration: .85, ease: 'power3.out' },
      1.08
    );
  }

  /* ============================================================
     SCROLL REVEAL (fade-up)
     ============================================================ */
  function initScrollReveal() {
    const els = document.querySelectorAll('.fade-up');
    if (!els.length) return;

    if (typeof ScrollTrigger !== 'undefined') {
      els.forEach((el, i) => {
        if (el.closest('.hero')) return;

        /* Staggered delay for items inside a .stagger parent */
        const parent = el.parentElement;
        if (parent && parent.classList.contains('stagger')) {
          const siblings = Array.from(parent.querySelectorAll(':scope > .fade-up'));
          const idx = siblings.indexOf(el);
          if (idx > 0) el.style.transitionDelay = (idx * 0.08) + 's';
        }

        ScrollTrigger.create({
          trigger: el, start: 'top 88%', once: true,
          onEnter: () => el.classList.add('in')
        });
      });
    } else {
      /* IO fallback */
      const io = new IntersectionObserver(entries => {
        entries.forEach(e => {
          if (!e.isIntersecting || e.target.closest('.hero')) return;
          const parent = e.target.parentElement;
          if (parent && parent.classList.contains('stagger')) {
            const siblings = Array.from(parent.querySelectorAll(':scope > .fade-up'));
            const idx = siblings.indexOf(e.target);
            if (idx > 0) e.target.style.transitionDelay = (idx * 0.08) + 's';
          }
          e.target.classList.add('in');
          io.unobserve(e.target);
        });
      }, { threshold: .08, rootMargin: '0px 0px -40px 0px' });
      els.forEach(el => { if (!el.closest('.hero')) io.observe(el); });
    }

    /* Process step activation */
    if (typeof ScrollTrigger !== 'undefined') {
      document.querySelectorAll('.proc-item').forEach(item => {
        ScrollTrigger.create({
          trigger: item, start: 'top 65%',
          onEnter:     () => item.classList.add('in'),
          onLeaveBack: () => item.classList.remove('in')
        });
      });
    }
  }

  /* ============================================================
     SCROLL PROGRESS BAR
     ============================================================ */
  function initScrollProgress() {
    const bar = document.getElementById('scrollProg');
    if (!bar) return;
    window.addEventListener('scroll', () => {
      const h = document.documentElement.scrollHeight - window.innerHeight;
      if (h > 0) bar.style.width = ((window.scrollY / h) * 100) + '%';
    }, { passive: true });
  }

  /* ============================================================
     COUNTERS
     ============================================================ */
  function initCounters() {
    const els = document.querySelectorAll('[data-count]');
    if (!els.length) return;

    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el  = e.target;
        const end = parseFloat(el.dataset.count);
        if (isNaN(end)) return;
        const dur = 1800, t0 = performance.now();
        const run = now => {
          const p = Math.min((now - t0) / dur, 1);
          el.textContent = Math.floor(end * (1 - Math.pow(1 - p, 3)));
          if (p < 1) requestAnimationFrame(run);
          else el.textContent = end;
        };
        requestAnimationFrame(run);
        io.unobserve(el);
      });
    }, { threshold: .6 });

    els.forEach(el => io.observe(el));
  }

  /* ============================================================
     WORK CARDS — hover video play
     ============================================================ */
  function initWorkCards() {
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        const vid = e.target.querySelector('.wc-vid');
        if (!vid) return;
        
        if (e.isIntersecting) {
          if (vid.dataset.manualPause !== 'true') {
            vid.play().catch(() => {});
            updatePlayBtn(e.target, true);
          }
        } else {
          if (!vid.paused) {
             vid.pause();
             updatePlayBtn(e.target, false);
          }
        }
      });
    }, { threshold: 0.1 });

    function updatePlayBtn(card, isPlaying) {
      const iconPause = card.querySelector('.icon-pause');
      const iconPlay = card.querySelector('.icon-play');
      if (iconPause && iconPlay) {
        iconPause.style.display = isPlaying ? 'block' : 'none';
        iconPlay.style.display = isPlaying ? 'none' : 'block';
      }
    }

    document.querySelectorAll('.work-card').forEach(card => {
      const vid = card.querySelector('.wc-vid');
      if (!vid) return;

      io.observe(card);

      const btnPlayPause = card.querySelector('.wc-btn-playpause');
      const btnMute = card.querySelector('.wc-btn-mute');

      if (btnPlayPause) {
        btnPlayPause.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          if (vid.paused) {
            vid.dataset.manualPause = 'false';
            vid.play().catch(() => {});
            updatePlayBtn(card, true);
          } else {
            vid.dataset.manualPause = 'true';
            vid.pause();
            updatePlayBtn(card, false);
          }
        });
      }

      if (btnMute) {
        btnMute.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          vid.muted = !vid.muted;
          const iconMuted = card.querySelector('.icon-muted');
          const iconUnmuted = card.querySelector('.icon-unmuted');
          if (vid.muted) {
            if(iconUnmuted) iconUnmuted.style.display = 'none';
            if(iconMuted) iconMuted.style.display = 'block';
          } else {
            if(iconMuted) iconMuted.style.display = 'none';
            if(iconUnmuted) iconUnmuted.style.display = 'block';
          }
        });
      }

      const btnFullscreen = card.querySelector('.wc-btn-fullscreen');
      if (btnFullscreen) {
        btnFullscreen.addEventListener('click', (e) => {
          e.preventDefault();
          e.stopPropagation();
          if (vid.requestFullscreen) {
            vid.requestFullscreen();
          } else if (vid.webkitRequestFullscreen) { /* Safari */
            vid.webkitRequestFullscreen();
          } else if (vid.msRequestFullscreen) { /* IE11 */
            vid.msRequestFullscreen();
          }
        });
      }

    });
  }
  /* ============================================================
     SERVICE CARD — mouse-follow lighting
     ============================================================ */
  function initServiceLighting() {
    document.querySelectorAll('.svc-card').forEach(card => {
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        card.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        card.style.setProperty('--my', (e.clientY - r.top) + 'px');
      });
    });
  }

  /* ============================================================
     SHOWREEL PLAYER
     ============================================================ */
  function initShowreel() {
    const vid  = document.getElementById('reelVid');
    const over = document.getElementById('reelOver');
    const btn  = document.getElementById('reelBtn');
    if (!vid || !over || !btn) return;

    btn.addEventListener('click', () => {
      vid.play().then(() => {
        over.classList.add('gone');
        vid.controls = true;
      }).catch(() => {});
    });

    vid.addEventListener('ended', () => {
      over.classList.remove('gone');
      vid.controls = false;
    });
    vid.addEventListener('error', () => {
      over.classList.remove('gone');
      vid.controls = false;
    });
  }

  /* ============================================================
     TESTIMONIALS — clone for infinite scroll
     ============================================================ */
  function initTestimonials() {
    const track = document.getElementById('testTrack');
    if (!track) return;
    const orig = Array.from(track.querySelectorAll('.test-card'));
    orig.forEach(c => {
      const clone = c.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      track.appendChild(clone);
    });
  }

  /* ============================================================
     PROCESS — step activation
     ============================================================ */
  function initProcess() {
    /* Already handled by initScrollReveal via .proc-item.in */
    /* Activate first step immediately if in viewport */
    const first = document.querySelector('.proc-item');
    if (first) {
      const r = first.getBoundingClientRect();
      if (r.top < window.innerHeight * .65) first.classList.add('in');
    }
  }

  /* ============================================================
     MAGNETIC BUTTONS
     ============================================================ */
  function initMagnetics() {
    if (!window.matchMedia('(hover: hover) and (min-width: 1025px)').matches) return;
    if (typeof gsap === 'undefined') return;

    document.querySelectorAll('[data-mag]').forEach(el => {
      const str = parseFloat(el.dataset.mag) || 18;

      el.addEventListener('mousemove', e => {
        const r = el.getBoundingClientRect();
        const x = e.clientX - r.left - r.width  / 2;
        const y = e.clientY - r.top  - r.height / 2;
        gsap.to(el, { x: x * str / 100, y: y * str / 100, duration: .35, ease: 'power2.out' });
      });
      el.addEventListener('mouseleave', () => {
        gsap.to(el, { x: 0, y: 0, duration: .65, ease: 'elastic.out(1,.3)' });
      });
    });
  }

  /* ============================================================
     CONTACT FORM
     ============================================================ */
  function initContactForm() {
    const form    = document.getElementById('ctaForm');
    const success = document.getElementById('cfSuccess');
    const submitBtn = document.getElementById('cfSubmit');
    if (!form) return;

    form.addEventListener('submit', async e => {
      e.preventDefault();
      if (submitBtn) {
        submitBtn.disabled = true;
        const sp = submitBtn.querySelector('span');
        if (sp) sp.textContent = 'Sending…';
      }

      try {
        const res = await fetch(form.action, {
          method: 'POST',
          body: new FormData(form),
          headers: { Accept: 'application/json' }
        });

        if (res.ok) {
          form.style.display = 'none';
          if (success) success.style.display = 'block';
        } else {
          resetBtn('Error — try WhatsApp');
        }
      } catch {
        resetBtn('Network error');
      }
    });

    function resetBtn(msg) {
      if (!submitBtn) return;
      submitBtn.disabled = false;
      const sp = submitBtn.querySelector('span');
      if (sp) sp.textContent = msg || 'Send Message';
      setTimeout(() => { if (sp) sp.textContent = 'Send Message'; }, 3000);
    }
  }

  /* ============================================================
     PARTICLES (hero canvas)
     ============================================================ */
  function initParticles() {
    const canvas = document.getElementById('heroCanvas');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    let W, H, particles = [];
    const N = Math.min(45, Math.floor(window.innerWidth / 32));

    const resize = () => {
      W = canvas.width  = canvas.offsetWidth;
      H = canvas.height = canvas.offsetHeight;
    };

    const ro = window.ResizeObserver
      ? new ResizeObserver(resize)
      : null;
    ro ? ro.observe(canvas) : window.addEventListener('resize', resize);
    resize();

    for (let i = 0; i < N; i++) {
      particles.push({
        x:  Math.random() * W,
        y:  Math.random() * H,
        vx: (Math.random() - .5) * .22,
        vy: (Math.random() - .5) * .22,
        r:  Math.random() * 1.4 + .4,
        a:  Math.random() * .18 + .04
      });
    }

    /* Assign a varied colour (purple or blue) to each particle */
    particles.forEach(p => {
      p.color = Math.random() > .65
        ? `rgba(96,165,250,${p.a})`   /* blue-light */
        : `rgba(167,139,250,${p.a})`; /* purple-light */
    });

    let raf;
    const draw = () => {
      ctx.clearRect(0, 0, W, H);
      particles.forEach(p => {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0) p.x = W;
        if (p.x > W) p.x = 0;
        if (p.y < 0) p.y = H;
        if (p.y > H) p.y = 0;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = p.color;
        ctx.fill();
      });
      raf = requestAnimationFrame(draw);
    };
    draw();

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) cancelAnimationFrame(raf);
      else draw();
    });
  }

})();
