import re

with open('index.html', 'r') as f:
    html = f.read()

new_grid = '''<div class="res-grid stagger" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px; margin-top: 48px;">
        <div class="res-card fade-up" style="background: rgba(124,58,237,.05); padding: 32px; border-radius: var(--r-lg); border: 1px solid rgba(124,58,237,.2); display: flex; flex-direction: column; align-items: flex-start; text-align: left; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #7c3aed;"></div>
          <h3 style="font-size: 1.4rem; font-weight: 700; font-family: var(--ff-head); color: #fff; margin-bottom: 12px;">Creator Growth</h3>
          <p style="color: rgba(255,255,255,.7); font-weight: 400; line-height: 1.6; font-size: 0.95rem;">Short-form edits built for hooks, retention, and replay value.</p>
        </div>
        <div class="res-card fade-up" style="background: rgba(37,99,235,.05); padding: 32px; border-radius: var(--r-lg); border: 1px solid rgba(37,99,235,.2); display: flex; flex-direction: column; align-items: flex-start; text-align: left; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #2563eb;"></div>
          <h3 style="font-size: 1.4rem; font-weight: 700; font-family: var(--ff-head); color: #fff; margin-bottom: 12px;">Real Estate Leads</h3>
          <p style="color: rgba(255,255,255,.7); font-weight: 400; line-height: 1.6; font-size: 0.95rem;">Cinematic property videos designed to generate serious inquiries.</p>
        </div>
        <div class="res-card fade-up" style="background: rgba(16,185,129,.05); padding: 32px; border-radius: var(--r-lg); border: 1px solid rgba(16,185,129,.2); display: flex; flex-direction: column; align-items: flex-start; text-align: left; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #10b981;"></div>
          <h3 style="font-size: 1.4rem; font-weight: 700; font-family: var(--ff-head); color: #fff; margin-bottom: 12px;">Brand Campaigns</h3>
          <p style="color: rgba(255,255,255,.7); font-weight: 400; line-height: 1.6; font-size: 0.95rem;">AI-enhanced product ads for launches, offers, and social campaigns.</p>
        </div>
        <div class="res-card fade-up" style="background: rgba(255,255,255,.03); padding: 32px; border-radius: var(--r-lg); border: 1px solid rgba(255,255,255,.1); display: flex; flex-direction: column; align-items: flex-start; text-align: left; position: relative; overflow: hidden;">
          <div style="position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: #fff;"></div>
          <h3 style="font-size: 1.4rem; font-weight: 700; font-family: var(--ff-head); color: #fff; margin-bottom: 12px;">Fast Delivery</h3>
          <p style="color: rgba(255,255,255,.7); font-weight: 400; line-height: 1.6; font-size: 0.95rem;">48h average delivery for urgent content needs.</p>
        </div>
      </div>'''

html = re.sub(r'<div class="res-grid stagger".*?</div>\s*</div>\s*</div>\s*</section>', new_grid + '\n    </div>\n  </div>\n</section>', html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)
print('Updated results section')
