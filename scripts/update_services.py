import re

with open('index.html', 'r') as f:
    html = f.read()

# Update Cinematic Editing
html = re.sub(
    r'<h3>Cinematic Editing</h3>.*?<p class="svc-tag".*?</p>',
    '''<h3>Cinematic Editing</h3>
          <p style="margin-bottom: 16px;">Hollywood-grade post-production with precision pacing and emotional storytelling.</p>
          <div style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;">
            <div style="color: rgba(255,255,255,0.7);"><strong style="color:#fff;">Who it\'s for:</strong> Brands, Creators, Studios</div>
            <div style="color: var(--purple-light); margin-top: 4px;"><strong style="color:#fff;">Benefit:</strong> Elevates perceived brand value & trust.</div>
          </div>''',
    html, flags=re.DOTALL
)

# Update AI Enhancement
html = re.sub(
    r'<h3>AI Enhancement</h3>.*?<p class="svc-tag".*?</p>',
    '''<h3>AI Enhancement</h3>
          <p style="margin-bottom: 16px;">Upscaling, frame interpolation, noise reduction, and AI-driven effects.</p>
          <div style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;">
            <div style="color: rgba(255,255,255,0.7);"><strong style="color:#fff;">Who it\'s for:</strong> Creators, Agencies, Startups</div>
            <div style="color: var(--purple-light); margin-top: 4px;"><strong style="color:#fff;">Benefit:</strong> Maximizes visual quality without reshoots.</div>
          </div>''',
    html, flags=re.DOTALL
)

# Update Reels & Shorts
html = re.sub(
    r'<h3>Reels &amp; Shorts</h3>.*?<p class="svc-tag".*?</p>',
    '''<h3>Reels &amp; Shorts</h3>
          <p style="margin-bottom: 16px;">High-retention short-form content engineered for TikTok, IG, and YouTube.</p>
          <div style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;">
            <div style="color: rgba(255,255,255,0.7);"><strong style="color:#fff;">Who it\'s for:</strong> Creators, Coaches, Brands</div>
            <div style="color: var(--purple-light); margin-top: 4px;"><strong style="color:#fff;">Benefit:</strong> Drives viral growth and follower conversion.</div>
          </div>''',
    html, flags=re.DOTALL
)

# Update Commercial Ads
html = re.sub(
    r'<h3>Commercial Ads</h3>.*?<p class="svc-tag".*?</p>',
    '''<h3>Commercial Ads</h3>
          <p style="margin-bottom: 16px;">Scroll-stopping advertisements with strong hooks and clear calls to action.</p>
          <div style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;">
            <div style="color: rgba(255,255,255,0.7);"><strong style="color:#fff;">Who it\'s for:</strong> E-commerce, SaaS, Real Estate</div>
            <div style="color: var(--purple-light); margin-top: 4px;"><strong style="color:#fff;">Benefit:</strong> Decreases CPA and increases direct leads.</div>
          </div>''',
    html, flags=re.DOTALL
)

# Update Color Grading
html = re.sub(
    r'<h3>Color Grading</h3>.*?<p class="svc-tag".*?</p>',
    '''<h3>Color Grading</h3>
          <p style="margin-bottom: 16px;">Cinematic color science that transforms the mood and emotion of your footage.</p>
          <div style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;">
            <div style="color: rgba(255,255,255,0.7);"><strong style="color:#fff;">Who it\'s for:</strong> Filmmakers, Brands, Agencies</div>
            <div style="color: var(--purple-light); margin-top: 4px;"><strong style="color:#fff;">Benefit:</strong> Creates a distinct, premium visual identity.</div>
          </div>''',
    html, flags=re.DOTALL
)

# Update Sound Design
html = re.sub(
    r'<h3>Sound Design</h3>.*?<p class="svc-tag".*?</p>',
    '''<h3>Sound Design</h3>
          <p style="margin-bottom: 16px;">Immersive audio engineering, cinematic scores, and SFX mixing.</p>
          <div style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;">
            <div style="color: rgba(255,255,255,0.7);"><strong style="color:#fff;">Who it\'s for:</strong> Creators, Studios, Brands</div>
            <div style="color: var(--purple-light); margin-top: 4px;"><strong style="color:#fff;">Benefit:</strong> Increases viewer retention through immersion.</div>
          </div>''',
    html, flags=re.DOTALL
)


# Add CTA title
html = re.sub(
    r'<div class="conv-block fade-up" style="margin-top: 64px; text-align: center;">\s*<div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">',
    '<div class="conv-block fade-up" style="margin-top: 72px; text-align: center; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); padding: 40px; border-radius: 24px;">\\n        <h3 style="font-size: 1.8rem; font-weight: 700; color: #fff; margin-bottom: 24px; font-family: var(--ff-head);">Choose Your Edit Style</h3>\\n        <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">',
    html
)

# We need to make .svc-card a flex column so `margin-top: auto` works properly.
# We'll check css/main.css for .svc-card
with open('index.html', 'w') as f:
    f.write(html)

with open('css/main.css', 'r') as f:
    css = f.read()

# Make svc-card flex column
css = re.sub(
    r'\.svc-card \{\n\s*background: rgba\(255,255,255,\.03\);\n\s*border: 1px solid var\(--border\);\n\s*border-radius: var\(--r-lg\);\n\s*padding: 32px;\n\s*position: relative;\n\s*overflow: hidden;\n\s*transition: background \.3s, transform \.3s;\n\}',
    '.svc-card {\\n  background: rgba(255,255,255,.03);\\n  border: 1px solid var(--border);\\n  border-radius: var(--r-lg);\\n  padding: 32px;\\n  position: relative;\\n  overflow: hidden;\\n  transition: background .3s, transform .3s;\\n  display: flex; flex-direction: column;\\n}',
    css
)

with open('css/main.css', 'w') as f:
    f.write(css)

print('Updated services section')
