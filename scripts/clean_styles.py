import re

with open('index.html', 'r') as f:
    html = f.read()

# Inline styles to replace:
# 1. <span style="display:block; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:4px 0;"> -> class="tc-sub"
html = html.replace('style="display:block; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:4px 0;"', 'class="tc-sub"')

# 2. <h3 style="font-size: 1.4rem; font-weight: 700; font-family: var(--ff-head); color: #fff; margin-bottom: 12px;"> -> class="res-h3"
html = html.replace('style="font-size: 1.4rem; font-weight: 700; font-family: var(--ff-head); color: #fff; margin-bottom: 12px;"', 'class="res-h3"')

# 3. <p style="color: rgba(255,255,255,.7); font-weight: 400; line-height: 1.6; font-size: 0.95rem;"> -> class="res-p"
html = html.replace('style="color: rgba(255,255,255,.7); font-weight: 400; line-height: 1.6; font-size: 0.95rem;"', 'class="res-p"')

# 4. <h3 style="font-size: 1.5rem; font-weight: 700; color: var(--off-white); margin-bottom: 24px; font-family: var(--ff-head);"> -> class="price-h3"
html = html.replace('style="font-size: 1.5rem; font-weight: 700; color: var(--off-white); margin-bottom: 24px; font-family: var(--ff-head);"', 'class="price-h3"')

# 5. <div style="flex-grow: 1; margin-bottom: 32px;"> -> class="price-body"
html = html.replace('style="flex-grow: 1; margin-bottom: 32px;"', 'class="price-body"')

# 6. <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7); margin-bottom: 12px;"> -> class="price-p-mb"
html = html.replace('style="font-size: 0.95rem; color: rgba(255,255,255,0.7); margin-bottom: 12px;"', 'class="price-p-mb"')

# 7. <p style="font-size: 0.95rem; color: rgba(255,255,255,0.7);"> -> class="price-p"
html = html.replace('style="font-size: 0.95rem; color: rgba(255,255,255,0.7);"', 'class="price-p"')

# 8. <a ... style="width: 100%; justify-content: center;"> -> add class w-full-center
html = html.replace('style="width: 100%; justify-content: center;"', 'class="btn-primary mag w-full-center"')
html = html.replace('class="btn-ghost mag w-full-center"', '') # Re-clean if already has it
# Actually the a tags had `class="btn-ghost mag" data-mag="10" style="width: 100%; justify-content: center;"`
# Or similar. Let's use regex for this one.
html = re.sub(r'class="([^"]+)" data-mag="10" style="width: 100%; justify-content: center;"', r'class="\1 w-full-center" data-mag="10"', html)

# 9. <p style="margin-bottom: 16px;"> -> class="svc-p"
html = html.replace('style="margin-bottom: 16px;"', 'class="svc-p"')

# 10. <div style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;"> -> class="svc-foot"
html = html.replace('style="margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5;"', 'class="svc-foot"')

# 11. <div style="color: rgba(255,255,255,0.7);"> -> class="svc-text"
html = html.replace('style="color: rgba(255,255,255,0.7);"', 'class="svc-text"')

# 12. <div style="color: var(--purple-light); margin-top: 4px;"> -> class="svc-highlight"
html = html.replace('style="color: var(--purple-light); margin-top: 4px;"', 'class="svc-highlight"')

with open('index.html', 'w') as f:
    f.write(html)

new_css = """
/* --- Cleaned Inline Styles --- */
.tc-sub { display:block; color:rgba(255,255,255,0.7); font-size:0.85rem; margin:4px 0; }
.res-h3 { font-size: 1.4rem; font-weight: 700; font-family: var(--ff-head); color: #fff; margin-bottom: 12px; }
.res-p { color: rgba(255,255,255,.7); font-weight: 400; line-height: 1.6; font-size: 0.95rem; }
.price-h3 { font-size: 1.5rem; font-weight: 700; color: var(--off-white); margin-bottom: 24px; font-family: var(--ff-head); }
.price-body { flex-grow: 1; margin-bottom: 32px; }
.price-p-mb { font-size: 0.95rem; color: rgba(255,255,255,0.7); margin-bottom: 12px; }
.price-p { font-size: 0.95rem; color: rgba(255,255,255,0.7); }
.w-full-center { width: 100%; justify-content: center; }
.svc-p { margin-bottom: 16px; }
.svc-foot { margin-top: auto; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 16px; font-size: 0.9rem; line-height: 1.5; }
.svc-text { color: rgba(255,255,255,0.7); }
.svc-highlight { color: var(--purple-light); margin-top: 4px; }
"""

with open('css/main.css', 'a') as f:
    f.write(new_css)

print("Inline styles cleaned up!")
