import re

# 1. Update HTML
with open('index.html', 'r') as f:
    html = f.read()

old_proc = """<div class="proc-list">
        <div class="proc-item fade-up">
          <div class="pi-num" aria-hidden="true">01</div>
          <div class="pi-body">
            <h3>Strategy &amp; Brief</h3>
            <p>We analyze your brand, audience, and goals to craft a viral content blueprint tailored to your vision and platform.</p>
          </div>
        </div>
        <div class="proc-item fade-up">
          <div class="pi-num" aria-hidden="true">02</div>
          <div class="pi-body">
            <h3>AI Enhancement</h3>
            <p>Our AI pipeline upscales footage, interpolates frames, removes noise, and refines audio at unprecedented speed.</p>
          </div>
        </div>
        <div class="proc-item fade-up">
          <div class="pi-num" aria-hidden="true">03</div>
          <div class="pi-body">
            <h3>Cinematic Edit</h3>
            <p>Expert editors assemble, color grade, and sound design every frame — human artistry meets AI speed.</p>
          </div>
        </div>
        <div class="proc-item fade-up">
          <div class="pi-num" aria-hidden="true">04</div>
          <div class="pi-body">
            <h3>Final Delivery</h3>
            <p>Ultra-premium deliverables optimized for every platform — ready to go live and dominate your niche.</p>
          </div>
        </div>
      </div>"""

new_proc = """<div class="proc-grid stagger">
        <div class="proc-card fade-up">
          <div class="pc-num" aria-hidden="true">01</div>
          <h3>Strategy &amp; Brief</h3>
          <p>We analyze your brand, audience, and goals to craft a viral content blueprint tailored to your vision and platform.</p>
        </div>
        <div class="proc-card fade-up">
          <div class="pc-num" aria-hidden="true">02</div>
          <h3>AI Enhancement</h3>
          <p>Our AI pipeline upscales footage, interpolates frames, removes noise, and refines audio at unprecedented speed.</p>
        </div>
        <div class="proc-card fade-up">
          <div class="pc-num" aria-hidden="true">03</div>
          <h3>Cinematic Edit</h3>
          <p>Expert editors assemble, color grade, and sound design every frame — human artistry meets AI speed.</p>
        </div>
        <div class="proc-card fade-up">
          <div class="pc-num" aria-hidden="true">04</div>
          <h3>Final Delivery</h3>
          <p>Ultra-premium deliverables optimized for every platform — ready to go live and dominate your niche.</p>
        </div>
      </div>"""

if old_proc in html:
    html = html.replace(old_proc, new_proc)
else:
    # Use regex if exact match fails
    html = re.sub(r'<div class="proc-list">.*?</div>\s*</div>', new_proc + '\n    </div>', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update CSS
with open('css/main.css', 'r') as f:
    css = f.read()

# Remove old process css
css = re.sub(r'\.proc-list \{.*?@media \(max-width: 580px\) \{[^\}]+\}', '', css, flags=re.DOTALL)

new_css = """
.proc-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.proc-card {
  padding: 40px 28px; border-radius: var(--r-lg);
  background: var(--glass); border: 1px solid var(--border);
  position: relative; overflow: hidden;
  transition: transform .4s, border-color .4s, background .4s, box-shadow .4s;
}
.proc-card:hover {
  background: var(--glass-2); border-color: rgba(124,58,237,.25);
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0,0,0,.3), 0 0 0 1px rgba(124,58,237,.08);
}
.pc-num {
  font-family: var(--ff-head); font-size: 3.5rem; font-weight: 800;
  color: transparent; -webkit-text-stroke: 1px rgba(255,255,255,.1);
  margin-bottom: 24px; transition: -webkit-text-stroke-color .4s, color .4s;
  line-height: 1;
}
.proc-card:hover .pc-num {
  color: rgba(124,58,237,.1); -webkit-text-stroke-color: rgba(124,58,237,.5);
}
.proc-card h3 {
  font-family: var(--ff-head); font-size: 1.25rem; font-weight: 700;
  color: var(--off-white); margin-bottom: 12px;
}
.proc-card p { font-size: .88rem; color: var(--muted); line-height: 1.7; }

@media (max-width: 1024px) { .proc-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 540px) { .proc-grid { grid-template-columns: 1fr; } }
"""

# Insert new css
css = css.replace('.proc-sec .sec-panel { background: rgba(255,255,255,.015); }', '.proc-sec .sec-panel { background: rgba(255,255,255,.015); }\n' + new_css)

with open('css/main.css', 'w') as f:
    f.write(css)

