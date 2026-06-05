import re

with open('index.html', 'r') as f:
    html = f.read()

# Remove the .wc-foot block from each work-card
html = re.sub(r'<div class="wc-foot">.*?</div>\s*</article>', r'</article>', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print("Removed .wc-foot")

with open('css/main.css', 'r') as f:
    css = f.read()

# Add the new overlay CSS
overlay_css = """
/* Custom Video Overlay */
.wc-custom-overlay {
  position: absolute; inset: 0; z-index: 3;
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  background: rgba(0,0,0,0.4); backdrop-filter: blur(4px); -webkit-backdrop-filter: blur(4px);
  transition: opacity 0.4s var(--ease), visibility 0.4s;
  pointer-events: none;
}
.wc-play-btn {
  width: 64px; height: 64px; border-radius: 50%;
  background: rgba(124,58,237,0.8); display: flex; align-items: center; justify-content: center;
  margin-bottom: 16px; color: #fff; box-shadow: 0 8px 24px rgba(124,58,237,0.4);
  transition: transform 0.3s; pointer-events: auto;
}
.wc-play-btn svg { width: 24px; height: 24px; margin-left: 4px; }
.work-card:hover .wc-play-btn { transform: scale(1.1); }
.wc-custom-overlay h3 { font-family: var(--ff-head); font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 4px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); text-align: center; }
.wc-custom-overlay span { font-size: 0.85rem; color: rgba(255,255,255,0.9); letter-spacing: 0.05em; text-transform: uppercase; text-shadow: 0 1px 2px rgba(0,0,0,0.5); text-align: center; }

.work-card:hover .wc-custom-overlay { opacity: 0; visibility: hidden; }
"""

# ensure .wc-thumb is 16/9
css = re.sub(r'\.wc-thumb \{\s*position: relative; aspect-ratio: 16/10;', r'.wc-thumb {\n  position: relative; aspect-ratio: 16/9;', css)
css = re.sub(r'\.work-card\.vertical \.wc-thumb \{ aspect-ratio: 9/16; \}', r'.work-card.vertical .wc-thumb { aspect-ratio: 16/9; }', css)
css = re.sub(r'\.work-card:first-child \.wc-thumb \{ aspect-ratio: 16/10; \}', r'.work-card:first-child .wc-thumb { aspect-ratio: 16/9; }', css)

# Append custom css
if '.wc-custom-overlay' not in css:
    css += overlay_css

with open('css/main.css', 'w') as f:
    f.write(css)
print("Updated CSS")
