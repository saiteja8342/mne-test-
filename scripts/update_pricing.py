import re

with open('index.html', 'r') as f:
    html = f.read()

new_grid = '''<div class="price-grid stagger" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; margin-top: 48px;">
        
        <div class="price-card fade-up" style="background: var(--glass); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 40px 32px; display: flex; flex-direction: column; text-align: left; position: relative; transition: border-color .3s, transform .3s;">
          <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--off-white); margin-bottom: 24px; font-family: var(--ff-head);">Reels &amp; Shorts</h3>
          <div style="flex-grow: 1; margin-bottom: 32px;">
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7); margin-bottom: 12px;"><strong style="color: #fff;">Best for:</strong> TikTok, IG, YouTube</p>
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7);"><strong style="color: #fff;">Typical delivery:</strong> 24-48 hours</p>
          </div>
          <a href="#contact" class="btn-ghost mag" data-mag="10" style="width: 100%; justify-content: center;">Request Quote</a>
        </div>

        <div class="price-card fade-up" style="background: var(--glass); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 40px 32px; display: flex; flex-direction: column; text-align: left; position: relative; transition: border-color .3s, transform .3s;">
          <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--off-white); margin-bottom: 24px; font-family: var(--ff-head);">Commercial Ads</h3>
          <div style="flex-grow: 1; margin-bottom: 32px;">
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7); margin-bottom: 12px;"><strong style="color: #fff;">Best for:</strong> Social media ad campaigns</p>
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7);"><strong style="color: #fff;">Typical delivery:</strong> 3-5 days</p>
          </div>
          <a href="#contact" class="btn-ghost mag" data-mag="10" style="width: 100%; justify-content: center;">Request Quote</a>
        </div>

        <div class="price-card fade-up" style="background: var(--glass); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 40px 32px; display: flex; flex-direction: column; text-align: left; position: relative; transition: border-color .3s, transform .3s;">
          <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--off-white); margin-bottom: 24px; font-family: var(--ff-head);">AI Avatar Videos</h3>
          <div style="flex-grow: 1; margin-bottom: 32px;">
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7); margin-bottom: 12px;"><strong style="color: #fff;">Best for:</strong> Explainers, Spokesperson</p>
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7);"><strong style="color: #fff;">Typical delivery:</strong> 2-4 days</p>
          </div>
          <a href="#contact" class="btn-ghost mag" data-mag="10" style="width: 100%; justify-content: center;">Request Quote</a>
        </div>

        <div class="price-card fade-up" style="background: var(--glass); border: 1px solid var(--border); border-radius: var(--r-lg); padding: 40px 32px; display: flex; flex-direction: column; text-align: left; position: relative; transition: border-color .3s, transform .3s;">
          <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--off-white); margin-bottom: 24px; font-family: var(--ff-head);">Brand Campaign Edits</h3>
          <div style="flex-grow: 1; margin-bottom: 32px;">
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7); margin-bottom: 12px;"><strong style="color: #fff;">Best for:</strong> Product launches, Promos</p>
            <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7);"><strong style="color: #fff;">Typical delivery:</strong> 5-7 days</p>
          </div>
          <a href="#contact" class="btn-ghost mag" data-mag="10" style="width: 100%; justify-content: center;">Request Quote</a>
        </div>

      </div>'''

html = re.sub(
    r'<div class="price-grid stagger".*?</div>\s*</div>\s*</div>\s*</section>',
    new_grid + '\n\n    </div>\n  </div>\n</section>',
    html, flags=re.DOTALL
)

with open('index.html', 'w') as f:
    f.write(html)
print('Updated pricing section')
