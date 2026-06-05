import re

# 1. Update HTML
with open('index.html', 'r') as f:
    html = f.read()

# I will replace the entire `.work-grid` section with two carousels.

new_work_section = """
      <div class="work-group fade-up">
        <h3 class="wg-title">Cinematic Commercials</h3>
        <div class="work-carousel" data-cursor="drag">
          
          <article class="work-card horizontal">
            <div class="wc-thumb">
              <video class="wc-vid" autoplay muted loop playsinline preload="metadata">
                <source src="assets/videos/ai-coffee.mp4" type="video/mp4">
              </video>
              <div class="wc-over" aria-hidden="true">
                <span class="wc-num">01</span>
                <div class="wc-controls">
                  <button class="wc-btn-mute" aria-label="Unmute">
                    <svg class="icon-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
                    <svg class="icon-unmuted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                  </button>
                  <button class="wc-btn-playpause" aria-label="Pause">
                    <svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                    <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><polygon points="5,3 19,12 5,21"/></svg>
                  </button>
                </div>
              </div>
            </div>
            <div class="wc-foot">
              <div class="wc-foot-left"><h3>AI Coffee Commercial</h3><span>Product · Cinematic</span></div>
              <div class="wc-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M17 7H7M17 7v10"/></svg></div>
            </div>
          </article>

          <article class="work-card horizontal">
            <div class="wc-thumb">
              <video class="wc-vid" autoplay muted loop playsinline preload="metadata">
                <source src="assets/videos/ai-sweet.mp4" type="video/mp4">
              </video>
              <div class="wc-over" aria-hidden="true">
                <span class="wc-num">02</span>
                <div class="wc-controls">
                  <button class="wc-btn-mute" aria-label="Unmute">
                    <svg class="icon-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
                    <svg class="icon-unmuted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                  </button>
                  <button class="wc-btn-playpause" aria-label="Pause">
                    <svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                    <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><polygon points="5,3 19,12 5,21"/></svg>
                  </button>
                </div>
              </div>
            </div>
            <div class="wc-foot">
              <div class="wc-foot-left"><h3>Sweet AI Concept</h3><span>AI Ad · Creative</span></div>
              <div class="wc-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M17 7H7M17 7v10"/></svg></div>
            </div>
          </article>

        </div>
      </div>

      <div class="work-group fade-up" style="margin-top: 64px;">
        <h3 class="wg-title">Viral Reels & Shorts</h3>
        <div class="work-carousel" data-cursor="drag">

          <article class="work-card vertical">
            <div class="wc-thumb">
              <video class="wc-vid" autoplay muted loop playsinline preload="metadata">
                <source src="assets/videos/ai-avatar-intro.mov" type="video/quicktime">
              </video>
              <div class="wc-over" aria-hidden="true">
                <span class="wc-num">01</span>
                <div class="wc-controls">
                  <button class="wc-btn-mute" aria-label="Unmute">
                    <svg class="icon-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
                    <svg class="icon-unmuted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                  </button>
                  <button class="wc-btn-playpause" aria-label="Pause">
                    <svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                    <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><polygon points="5,3 19,12 5,21"/></svg>
                  </button>
                </div>
              </div>
            </div>
            <div class="wc-foot">
              <div class="wc-foot-left"><h3>AI Avatar Intro</h3><span>Virtual Identity · AI</span></div>
              <div class="wc-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M17 7H7M17 7v10"/></svg></div>
            </div>
          </article>

          <article class="work-card vertical">
            <div class="wc-thumb">
              <video class="wc-vid" autoplay muted loop playsinline preload="metadata">
                <source src="assets/videos/ai-reel.mov" type="video/quicktime">
              </video>
              <div class="wc-over" aria-hidden="true">
                <span class="wc-num">02</span>
                <div class="wc-controls">
                  <button class="wc-btn-mute" aria-label="Unmute">
                    <svg class="icon-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
                    <svg class="icon-unmuted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                  </button>
                  <button class="wc-btn-playpause" aria-label="Pause">
                    <svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                    <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><polygon points="5,3 19,12 5,21"/></svg>
                  </button>
                </div>
              </div>
            </div>
            <div class="wc-foot">
              <div class="wc-foot-left"><h3>AI Viral Reel</h3><span>Short Form · Viral</span></div>
              <div class="wc-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M17 7H7M17 7v10"/></svg></div>
            </div>
          </article>
          
          <article class="work-card vertical">
            <div class="wc-thumb">
              <video class="wc-vid" autoplay muted loop playsinline preload="metadata">
                <source src="assets/videos/ai-avatar-virtual.mov" type="video/quicktime">
              </video>
              <div class="wc-over" aria-hidden="true">
                <span class="wc-num">03</span>
                <div class="wc-controls">
                  <button class="wc-btn-mute" aria-label="Unmute">
                    <svg class="icon-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
                    <svg class="icon-unmuted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none;"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                  </button>
                  <button class="wc-btn-playpause" aria-label="Pause">
                    <svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                    <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><polygon points="5,3 19,12 5,21"/></svg>
                  </button>
                </div>
              </div>
            </div>
            <div class="wc-foot">
              <div class="wc-foot-left"><h3>AI Avatar Virtual</h3><span>Virtual Identity · AI</span></div>
              <div class="wc-arrow"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M17 7H7M17 7v10"/></svg></div>
            </div>
          </article>

        </div>
      </div>
"""

html = re.sub(r'<div class="work-grid stagger">.*?</div>\s*</div>\s*</div>\s*</section>', new_work_section + '\n    </div>\n  </div>\n</section>', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update CSS
with open('css/main.css', 'r') as f:
    css = f.read()

# Replace .work-grid and its related styles
css = re.sub(r'/\* Featured first card full width \*/.*?\.work-card:hover \{[^}]+\}', '', css, flags=re.DOTALL)

new_carousel_css = """
/* Carousel grouping */
.wg-title {
  font-family: var(--ff-head); font-size: 1.5rem; font-weight: 700;
  color: var(--off-white); margin-bottom: 24px; padding-left: 8px;
}
.work-carousel {
  display: flex; gap: 24px;
  overflow-x: auto; scroll-snap-type: x mandatory;
  padding-bottom: 24px; margin-bottom: -24px;
  scrollbar-width: none;
}
.work-carousel::-webkit-scrollbar { display: none; }
.work-carousel:active { cursor: grabbing; }

.work-card {
  border-radius: var(--r-lg); overflow: hidden;
  background: var(--ink-3); border: 1px solid var(--border);
  transition: border-color .4s var(--ease), transform .5s var(--ease), box-shadow .5s;
  flex-shrink: 0; scroll-snap-align: start;
}
.work-card.horizontal {
  width: 70%; max-width: 800px; min-width: 320px;
}
.work-card.horizontal .wc-thumb { aspect-ratio: 16/9; }

.work-card.vertical {
  width: 320px;
}
.work-card.vertical .wc-thumb { aspect-ratio: 9/16; }

.work-card:hover {
  border-color: rgba(124,58,237,.25);
  transform: translateY(-5px);
  box-shadow: 0 20px 60px rgba(0,0,0,.4), 0 0 0 1px rgba(124,58,237,.08);
}

/* Custom drag cursor element */
.c-drag {
  position: fixed; width: 64px; height: 64px;
  background: rgba(255,255,255,.1); border: 1px solid rgba(255,255,255,.3);
  backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);
  border-radius: 50%; pointer-events: none; z-index: 100002;
  display: flex; align-items: center; justify-content: center;
  font-family: var(--ff-head); font-size: 0.75rem; font-weight: 700; color: #fff;
  letter-spacing: .1em; opacity: 0; transform: translate(-50%, -50%) scale(0.5);
  transition: opacity .3s, transform .3s;
}
.c-drag.on { opacity: 1; transform: translate(-50%, -50%) scale(1); }

@media (max-width: 640px) {
  .work-card.horizontal { width: 90%; }
  .work-card.vertical { width: 85%; max-width: 320px; }
  .work-carousel { gap: 16px; }
}
"""

# Insert new css
css = css.replace('.work-sec .sec-panel { background: rgba(255,255,255,.018); }', '.work-sec .sec-panel { background: rgba(255,255,255,.018); }\n' + new_carousel_css)

with open('css/main.css', 'w') as f:
    f.write(css)

# 3. Update JS to handle drag scrolling and custom cursor
with open('js/app.js', 'r') as f:
    js = f.read()

# I need to add custom drag cursor logic to JS. 
# Also add horizontal mouse dragging to the carousels.
# Let's insert this before initNavbar

js_drag = """
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
"""

js = js.replace('function initNavbar()', js_drag + '\n  function initNavbar()')
js = js.replace('initCursor();', 'initCursor();\n    initCarouselDrag();')

with open('js/app.js', 'w') as f:
    f.write(js)

