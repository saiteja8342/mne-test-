import re

# 1. Update HTML
with open('index.html', 'r') as f:
    html = f.read()

html = re.sub(r'<video class="wc-vid" muted loop playsinline preload="none"', 
              r'<video class="wc-vid" autoplay muted loop playsinline preload="metadata"', html)

replacement = """<div class="wc-controls">
                <button class="wc-btn-mute" aria-label="Unmute">
                  <svg class="icon-muted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><line x1="23" y1="9" x2="17" y2="15"></line><line x1="17" y1="9" x2="23" y2="15"></line></svg>
                  <svg class="icon-unmuted" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="display:none;"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                </button>
                <button class="wc-btn-playpause" aria-label="Pause">
                  <svg class="icon-pause" viewBox="0 0 24 24" fill="currentColor"><rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/></svg>
                  <svg class="icon-play" viewBox="0 0 24 24" fill="currentColor" style="display:none;"><polygon points="5,3 19,12 5,21"/></svg>
                </button>
              </div>"""

html = re.sub(r'<div class="wc-play">.*?</div>', replacement, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update CSS
with open('css/main.css', 'r') as f:
    css = f.read()

css = re.sub(r'\.wc-vid\s*\{[^}]+\}', 
             r'.wc-vid {\n  position: absolute; inset: 0;\n  width: 100%; height: 100%; object-fit: cover;\n}', css)
css = re.sub(r'\.work-card:hover \.wc-vid\s*\{[^}]+\}', '', css)

controls_css = """
.wc-controls {
  display: flex; align-items: center; gap: 8px;
}
.wc-btn-playpause, .wc-btn-mute {
  width: 36px; height: 36px; border-radius: 50%;
  background: rgba(0,0,0,.4);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.15);
  display: flex; align-items: center; justify-content: center;
  color: #fff; cursor: pointer;
  transition: background .3s, transform .3s;
}
.wc-btn-playpause:hover, .wc-btn-mute:hover {
  background: rgba(124,58,237,.6);
  transform: scale(1.05);
}
.wc-btn-playpause svg, .wc-btn-mute svg { width: 14px; height: 14px; }
.wc-btn-playpause .icon-play { margin-left: 2px; }
"""

css = re.sub(r'\.wc-play\s*\{.*?\.wc-play svg\s*\{[^}]+\}', controls_css, css, flags=re.DOTALL)

with open('css/main.css', 'w') as f:
    f.write(css)

# 3. Update JS
with open('js/app.js', 'r') as f:
    js = f.read()

js_replacement = """function initWorkCards() {
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
    });
  }"""

js = re.sub(r'function initWorkCards\(\)\s*\{.*?\}\n\s*(?=\n\s*/\* =+)', js_replacement, js, flags=re.DOTALL)

with open('js/app.js', 'w') as f:
    f.write(js)

