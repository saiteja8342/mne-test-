import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Testimonials Polish (add mobile padding and subtext)
html = html.replace('<span>Creator · Engagement tripled in 30 days</span>', '<span style="display:block; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:4px 0;">Creator &middot; Engagement tripled in 30 days</span>')
html = html.replace('<span>Startup Founder · AI avatar launch video delivered in 48h</span>', '<span style="display:block; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:4px 0;">Startup Founder &middot; AI avatar launch video delivered in 48h</span>')
html = html.replace('<span>Real Estate · 15 inquiries in one week</span>', '<span style="display:block; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:4px 0;">Real Estate &middot; 15 inquiries in one week</span>')
html = html.replace('<span>Brand · Doubled social reach</span>', '<span style="display:block; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:4px 0;">Brand &middot; Doubled social reach</span>')

# Fix Testimonial padding for mobile
with open('css/main.css', 'r') as f:
    css = f.read()
if '.test-card {' in css:
    css = re.sub(r'\.test-card \{([^\}]+)\}', r'.test-card {\1 padding: 24px; }', css)

# 2. Extract sections
sections = {}
# Find all sections. A section starts with <section class="section ... id="..." ...>
# and ends with </section>
# We can use regex to find them.
matches = list(re.finditer(r'<section class="section[^>]+id="([^"]+)"[^>]*>.*?</section>', html, flags=re.DOTALL))
for m in matches:
    sections[m.group(1)] = m.group(0)

# Replace the sections in the body with a single marker to place them in order
body_start = html.find('<main>')
if body_start == -1:
    body_start = html.find('<section')
body_end = html.rfind('</section>') + len('</section>')

# We will build the new main content
merged_section = """<!-- ═══════════════════════════════════════════
     BUILT FOR
═══════════════════════════════════════════ -->
<section class="section built-sec" id="built-for" aria-labelledby="built-title">
  <div class="wrap">
    <div class="sec-panel fade-up">
      <div class="sec-head center">
        <div class="sec-label">Our Focus</div>
        <h2 class="sec-title" id="built-title">Built For <em>Creators, Brands & Businesses</em></h2>
      </div>

      <div class="built-grid stagger">
        <div class="built-card fade-up">
          <h3>Creators</h3>
          <p>Reels, shorts, viral edits, captions, hooks.</p>
        </div>
        <div class="built-card fade-up">
          <h3>Brands</h3>
          <p>Product ads, launch videos, campaign creatives.</p>
        </div>
        <div class="built-card fade-up">
          <h3>Businesses</h3>
          <p>Property walkthroughs, AI avatars, explainers.</p>
        </div>
        <div class="built-card fade-up">
          <h3>Agencies</h3>
          <p>Cinematic color grading and fast 48h turnaround.</p>
        </div>
      </div>
    </div>
  </div>
</section>"""

# New Contact Section
new_contact = """<!-- ═══════════════════════════════════════════
     CONTACT CTA
═══════════════════════════════════════════ -->
<section class="section cta-sec" id="contact" aria-labelledby="cta-title">
  <div class="cta-glow" aria-hidden="true"></div>
  <div class="wrap">
    <div class="sec-panel fade-up">

      <div class="cta-inner">
        <div class="sec-label">Get Started</div>
        <h2 class="cta-title" id="cta-title">Tell us what you need<br><em>edited</em></h2>
        <p class="cta-sub">Want a quick quote? Send your footage or idea on WhatsApp.</p>

        <form class="cta-form" id="ctaForm" action="https://formspree.io/f/mzdokokr" method="POST">
          <input type="hidden" name="_subject" value="New Project Enquiry — MOTIONNODEEDITS">
          <div class="cf-row">
            <div class="cf-field">
              <input type="text" name="name" id="cfName" required placeholder=" " autocomplete="name">
              <label for="cfName">Your Name</label>
            </div>
            <div class="cf-field">
              <input type="email" name="email" id="cfEmail" required placeholder=" " autocomplete="email">
              <label for="cfEmail">Email Address</label>
            </div>
          </div>
          <div class="cf-field">
            <input type="tel" name="whatsapp" id="cfWa" placeholder=" " autocomplete="tel">
            <label for="cfWa">WhatsApp Number (Optional)</label>
          </div>
          <div class="cf-field">
            <select name="needs" id="cfNeeds" required class="cf-select">
              <option value="" disabled selected>Select what you need</option>
              <option value="Reel / Short">Reel / Short</option>
              <option value="Commercial Ad">Commercial Ad</option>
              <option value="AI Avatar">AI Avatar</option>
              <option value="YouTube Video">YouTube Video</option>
              <option value="Brand Campaign">Brand Campaign</option>
              <option value="Other">Other</option>
            </select>
            <label for="cfNeeds" class="cf-select-label">What do you need?</label>
          </div>
          <div class="cf-row">
            <div class="cf-field">
              <input type="text" name="budget" id="cfBudget" placeholder=" " autocomplete="off">
              <label for="cfBudget">Budget Range</label>
            </div>
            <div class="cf-field">
              <input type="text" name="deadline" id="cfDeadline" placeholder=" " autocomplete="off">
              <label for="cfDeadline">Deadline</label>
            </div>
          </div>
          <div class="cf-field">
            <textarea name="details" id="cfDetails" required placeholder=" "></textarea>
            <label for="cfDetails">Project Details</label>
          </div>
          <div class="cf-foot">
            <button type="submit" class="btn-primary mag" data-mag="12">Submit Request</button>
            <p class="cf-sec-text">Or <a href="https://wa.me/918985351756" target="_blank" rel="noopener noreferrer">chat on WhatsApp</a></p>
          </div>
        </form>
      </div>

    </div>
  </div>
</section>"""

# Order: work, showreel, results, services, built-for, pricing, process, testimonials, contact
new_body = "\n\n".join([
    sections.get('work', ''),
    sections.get('showreel', ''),
    sections.get('results', ''),
    sections.get('services', ''),
    merged_section,
    sections.get('pricing', ''),
    sections.get('process', ''),
    sections.get('testimonials', ''),
    new_contact
])

# Replace old sections with new_body
html = html[:matches[0].start()] + new_body + html[matches[-1].end():]

# Add CSS for new merged section and updated contact form
new_css = """
/* Built For Section */
.built-grid {
  display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 24px; margin-top: 48px;
}
.built-card {
  background: var(--glass); padding: 32px; border-radius: var(--r-lg); border: 1px solid var(--border);
  transition: border-color .3s, transform .3s;
}
.built-card:hover { border-color: var(--purple-light); transform: translateY(-4px); }
.built-card h3 { font-size: 1.25rem; font-weight: 700; color: var(--off-white); margin-bottom: 12px; }
.built-card p { color: var(--muted); font-size: 0.95rem; line-height: 1.6; }

/* Contact Form Cleanups */
.cf-select {
  width: 100%; padding: 18px 20px; padding-top: 26px; background: rgba(255,255,255,0.03); 
  border: 1px solid var(--border); border-radius: 12px; color: var(--off-white); 
  font-size: .95rem; appearance: none; cursor: pointer; outline: none;
}
.cf-select:focus { border-color: rgba(124,58,237,.45); background: rgba(255,255,255,.055); }
.cf-select option { background: #141428; color: #fff; }
.cf-select-label {
  transform: translateY(-22px) scale(0.85); color: rgba(255,255,255,0.4); pointer-events: none; position: absolute; top: 17px; left: 18px;
}
"""
css += new_css

with open('index.html', 'w') as f:
    f.write(html)
with open('css/main.css', 'w') as f:
    f.write(css)

print('Restructure completed successfully')
