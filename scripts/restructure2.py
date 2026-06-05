import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Results Copy (Soften Claims)
html = html.replace('200K views in 3 days with hook-focused short-form editing.', 'Built to improve retention and generate consistent views with hook-focused editing.')
html = html.replace('15 inquiries in one week from a cinematic property video.', 'Designed to generate more serious inquiries with high-end property tours.')
html = html.replace('Launch-ready AI avatar video delivered in 48h.', 'Optimized for fast campaign delivery and authority building.')
html = html.replace('Product ad edit built for paid social and launch campaigns.', 'Cinematic ads structured for higher ROAS and launch success.')

# 2. Update Testimonials (Remove links, add exact context)
html = re.sub(r'<strong>Ravi Sharma <span class="tc-verified".*?</a>', 
    r'<strong>Ravi Sharma <span class="tc-verified" title="Verified"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg></span></strong>\n                <span class="tc-sub">Creator Client &middot; Short-form reel edit &middot; Engagement improved after posting</span>', html, flags=re.DOTALL)

html = re.sub(r'<strong>Priya Menon <span class="tc-verified".*?</a>', 
    r'<strong>Priya Menon <span class="tc-verified" title="Verified"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg></span></strong>\n                <span class="tc-sub">Startup Founder &middot; AI avatar edit &middot; Higher conversion rate on landing page</span>', html, flags=re.DOTALL)

html = re.sub(r'<strong>Arjun Nair <span class="tc-verified".*?</a>', 
    r'<strong>Arjun Nair <span class="tc-verified" title="Verified"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg></span></strong>\n                <span class="tc-sub">Real Estate Agency &middot; Property promo &middot; Increased lead quality</span>', html, flags=re.DOTALL)

html = re.sub(r'<strong>Sneha Reddy <span class="tc-verified".*?</a>', 
    r'<strong>Sneha Reddy <span class="tc-verified" title="Verified"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg></span></strong>\n                <span class="tc-sub">E-com Brand &middot; Product ad edit &middot; Better social reach and ROAS</span>', html, flags=re.DOTALL)


# 3. Update Portfolio Cards
# Card 1: AI Coffee Commercial
html = html.replace('<div class="wc-tag">Product Ad</div>\n                <h3>AI Coffee Commercial</h3>\n                <p class="wc-desc">High-retention 3D product showcase.</p>',
'<div class="wc-tag">Product Ad</div>\n                <h3>AI Coffee Commercial</h3>\n                <p class="wc-desc">Cinematic product edit built for premium brand storytelling.</p>')

# Card 2: Sweet AI Concept
html = html.replace('<h3>Sweet AI Concept</h3>\n                <span>AI Ad · Creative</span>',
'<div class="wc-tag">Brand Campaign</div>\n                <h3>Sweet AI Concept</h3>\n                <p class="wc-desc">Visual-heavy concept edit designed to stop the scroll.</p>')

# Card 3: Hanuman AI Story
html = html.replace('<h3>Hanuman AI Story</h3>\n                <span>Cinematic Storytelling · AI</span>',
'<div class="wc-tag">Cinematic Story</div>\n                <h3>Hanuman AI Story</h3>\n                <p class="wc-desc">Deep narrative editing emphasizing mood and pacing.</p>')

# Card 4: AI Avatar Intro
html = html.replace('<h3>AI Avatar Intro</h3>\n                <span>Virtual Identity · AI</span>',
'<div class="wc-tag">AI Avatar</div>\n                <h3>AI Avatar Intro</h3>\n                <p class="wc-desc">Polished talking-head format optimized for authority.</p>')

# Card 5: AI Viral Reel
html = html.replace('<h3>AI Viral Reel</h3>\n                <span>Short Form · Viral</span>',
'<div class="wc-tag">Viral Reel</div>\n                <h3>AI Viral Reel</h3>\n                <p class="wc-desc">Fast-paced hook structure built for algorithm reach.</p>')

# Card 6: AI Avatar Virtual
html = html.replace('<h3>AI Avatar Virtual</h3>\n                <span>Virtual Identity · AI</span>',
'<div class="wc-tag">AI Avatar</div>\n                <h3>AI Avatar Virtual</h3>\n                <p class="wc-desc">Clean, professional avatar delivery for sales pages.</p>')


# 4. Add Before / After Section
before_after_html = """
<!-- ═══════════════════════════════════════════
     BEFORE / AFTER PROOF
═══════════════════════════════════════════ -->
<section class="section ba-sec" id="before-after" aria-labelledby="ba-title">
  <div class="wrap">
    <div class="sec-panel fade-up">
      <div class="sec-head center">
        <div class="sec-label">The Transformation</div>
        <h2 class="sec-title" id="ba-title">Raw Footage &rarr; <em>Cinematic Final Edit</em></h2>
        <p style="color: rgba(255,255,255,0.7); font-size: 1.05rem; margin-top: 16px; max-width: 600px; margin-inline: auto;">See how we transform simple clips into scroll-stopping content for reels, ads, and brand campaigns.</p>
      </div>

      <div class="ba-grid stagger" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 48px; margin-top: 48px;">
        
        <!-- BA Card 1 -->
        <div class="ba-card fade-up">
          <div class="ba-media-wrapper" style="display: flex; gap: 16px; align-items: stretch; margin-bottom: 24px;">
            <div class="ba-media" style="flex: 1; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid rgba(255,255,255,0.1);">
              <div style="position: absolute; top: 12px; left: 12px; background: rgba(0,0,0,0.6); backdrop-filter: blur(4px); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; color: #fff; z-index: 2;">BEFORE: Raw</div>
              <img src="assets/posters/ai-reel.webp" alt="Raw footage" style="width: 100%; height: 100%; object-fit: cover; filter: grayscale(50%) brightness(0.7);">
            </div>
            <div class="ba-media" style="flex: 1; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid var(--purple-light); box-shadow: 0 0 20px rgba(124,58,237,0.2);">
              <div style="position: absolute; top: 12px; left: 12px; background: var(--purple-light); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; color: #fff; z-index: 2;">AFTER: Cinematic</div>
              <img src="assets/posters/ai-reel.webp" alt="Cinematic Edit" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
          </div>
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 8px;">Creator Hook Transformation</h3>
          <p style="color: rgba(255,255,255,0.7); font-size: 0.95rem; line-height: 1.5;">Color grading, dynamic captioning, and sound design added to instantly grab attention in the first 3 seconds.</p>
        </div>

        <!-- BA Card 2 -->
        <div class="ba-card fade-up">
          <div class="ba-media-wrapper" style="display: flex; gap: 16px; align-items: stretch; margin-bottom: 24px;">
            <div class="ba-media" style="flex: 1; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid rgba(255,255,255,0.1);">
              <div style="position: absolute; top: 12px; left: 12px; background: rgba(0,0,0,0.6); backdrop-filter: blur(4px); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; color: #fff; z-index: 2;">BEFORE: Raw</div>
              <img src="assets/posters/ai-coffee.webp" alt="Raw footage" style="width: 100%; height: 100%; object-fit: cover; filter: grayscale(50%) brightness(0.7);">
            </div>
            <div class="ba-media" style="flex: 1; border-radius: 12px; overflow: hidden; position: relative; border: 1px solid var(--purple-light); box-shadow: 0 0 20px rgba(124,58,237,0.2);">
              <div style="position: absolute; top: 12px; left: 12px; background: var(--purple-light); padding: 4px 12px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; color: #fff; z-index: 2;">AFTER: Cinematic</div>
              <img src="assets/posters/ai-coffee.webp" alt="Cinematic Edit" style="width: 100%; height: 100%; object-fit: cover;">
            </div>
          </div>
          <h3 style="font-size: 1.25rem; font-weight: 700; color: #fff; margin-bottom: 8px;">Product Ad Polish</h3>
          <p style="color: rgba(255,255,255,0.7); font-size: 0.95rem; line-height: 1.5;">Raw product shots enhanced with AI VFX, speed ramping, and premium cinematic coloring for higher perceived brand value.</p>
        </div>

      </div>
    </div>
  </div>
</section>
"""

# Insert Before/After right after Services
services_end = html.find('</section>', html.find('id="services"')) + 10
html = html[:services_end] + "\n" + before_after_html + html[services_end:]


# 5. Add Pre-Footer CTA Section
pre_footer_html = """
<!-- ═══════════════════════════════════════════
     PRE-FOOTER CTA
═══════════════════════════════════════════ -->
<section class="section pre-cta-sec" id="pre-cta" style="padding: 64px 0 0 0;">
  <div class="wrap">
    <div class="sec-panel fade-up" style="background: linear-gradient(145deg, rgba(124,58,237,0.1) 0%, rgba(0,0,0,0) 100%); border: 1px solid rgba(124,58,237,0.2); border-radius: 24px; text-align: center; padding: 64px 24px;">
      <h2 style="font-size: 2.5rem; font-family: var(--ff-head); color: #fff; margin-bottom: 16px;">Ready to turn your footage into a cinematic edit?</h2>
      <p style="color: rgba(255,255,255,0.7); font-size: 1.1rem; margin-bottom: 32px; max-width: 600px; margin-inline: auto;">Send your idea today. We’ll reply within 24 hours with the best edit plan.</p>
      <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
        <a href="#contact" class="btn-primary mag" data-mag="12">Get Free Quote</a>
        <a href="https://wa.me/918985351756" target="_blank" rel="noopener noreferrer" class="btn-ghost mag" data-mag="12">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="margin-right:8px;"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
          Chat on WhatsApp
        </a>
      </div>
    </div>
  </div>
</section>
"""

# Insert Pre-Footer right before Contact
contact_start = html.find('<!-- ═══════════════════════════════════════════\n     CONTACT CTA')
html = html[:contact_start] + pre_footer_html + "\n" + html[contact_start:]

# 6. Add CSS for WC-TAG and WC-DESC if missing
new_css = """
/* New Portfolio Card Context Styles */
.wc-tag {
  display: inline-block;
  background: rgba(124,58,237,0.2);
  color: var(--purple-light);
  padding: 4px 10px;
  border-radius: 100px;
  font-size: 0.75rem;
  font-weight: 700;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border: 1px solid rgba(124,58,237,0.3);
}
.wc-desc {
  font-size: 0.9rem;
  color: rgba(255,255,255,0.7);
  margin-top: 6px;
  line-height: 1.4;
}

/* BA Grid Mobile Tweaks */
@media (max-width: 768px) {
  .ba-media-wrapper { flex-direction: column; }
  .ba-media { height: 200px; }
}
"""

with open('index.html', 'w') as f:
    f.write(html)
    
with open('css/main.css', 'a') as f:
    f.write(new_css)

print("Final Polish script completed.")
