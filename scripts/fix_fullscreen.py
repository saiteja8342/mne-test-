import re

# 1. Update HTML: Add fullscreen button to every wc-controls
with open('index.html', 'r') as f:
    html = f.read()

fullscreen_btn = """
                  <button class="wc-btn-fullscreen" aria-label="Fullscreen">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="width:14px;height:14px;"><path d="M8 3H5a2 2 0 0 0-2 2v3m18 0V5a2 2 0 0 0-2-2h-3m0 18h3a2 2 0 0 0 2-2v-3M3 16v3a2 2 0 0 0 2 2h3"></path></svg>
                  </button>
                </div>"""

# Replace `</button>\n                </div>` with the new button
html = re.sub(r'</button>\s*</div>\s*(?=\s*</div>\s*</div>\s*<div class="wc-foot")', 
              '</button>' + fullscreen_btn, html)

with open('index.html', 'w') as f:
    f.write(html)


# 2. Update CSS: Hide controls by default, show on hover. Also style the new button.
with open('css/main.css', 'r') as f:
    css = f.read()

# Replace the control styles
old_css_match = re.search(r'\.wc-controls \{.*?\.wc-btn-playpause \.icon-play \{ margin-left: 2px; \}', css, flags=re.DOTALL)
if old_css_match:
    old_css = old_css_match.group(0)
    new_css = """
.wc-controls {
  display: flex; align-items: center; gap: 8px;
  opacity: 0; transform: translateY(8px);
  transition: opacity .4s var(--ease), transform .4s var(--ease);
}
.work-card:hover .wc-controls {
  opacity: 1; transform: translateY(0);
}

.wc-btn-playpause, .wc-btn-mute, .wc-btn-fullscreen {
  width: 36px; height: 36px; border-radius: 50%;
  background: rgba(0,0,0,.4);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(255,255,255,.15);
  display: flex; align-items: center; justify-content: center;
  color: #fff; cursor: pointer;
  transition: background .3s, transform .3s;
}
.wc-btn-playpause:hover, .wc-btn-mute:hover, .wc-btn-fullscreen:hover {
  background: rgba(124,58,237,.6);
  transform: scale(1.05);
}
.wc-btn-playpause svg, .wc-btn-mute svg, .wc-btn-fullscreen svg { width: 14px; height: 14px; }
.wc-btn-playpause .icon-play { margin-left: 2px; }
"""
    css = css.replace(old_css, new_css.strip())

with open('css/main.css', 'w') as f:
    f.write(css)


# 3. Update JS: Add fullscreen functionality
with open('js/app.js', 'r') as f:
    js = f.read()

fullscreen_js = """
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
"""

if "btnFullscreen.addEventListener" not in js:
    # Insert after btnMute logic
    js = re.sub(r'(if \(btnMute\) \{.*?\n      \})', r'\1' + '\n' + fullscreen_js, js, flags=re.DOTALL)

with open('js/app.js', 'w') as f:
    f.write(js)
