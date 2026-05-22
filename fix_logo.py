import re

# 1. Update HTML
with open('index.html', 'r') as f:
    html = f.read()

# Replace Preloader text with image
html = html.replace('<div class="pre-logo">MNE</div>', 
                    '<div class="pre-logo"><img src="image/logo.png" alt="Logo"></div>')

# Replace Navbar text with image
nav_logo_old = """    <a href="#hero" class="nav-logo" aria-label="MOTIONNODEEDITS — Back to top">
      <span class="logo-mark">MNE</span>
      <span class="logo-sep" aria-hidden="true"></span>
    </a>"""
nav_logo_new = """    <a href="#hero" class="nav-logo" aria-label="MOTIONNODEEDITS — Back to top">
      <img src="image/logo.png" alt="MOTIONNODEEDITS" class="nav-logo-img">
    </a>"""
html = html.replace(nav_logo_old, nav_logo_new)

# Replace Footer text with image
foot_logo_old = '<div class="foot-brand">MOTIONNODEEDITS</div>'
foot_logo_new = '<img src="image/logo.png" alt="MOTIONNODEEDITS" class="foot-logo-img">'
html = html.replace(foot_logo_old, foot_logo_new)

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update CSS
with open('css/main.css', 'r') as f:
    css = f.read()

# Preloader image style
css = css.replace('.pre-logo {\n  font-family: var(--ff-head);\n  font-size: 2.2rem; font-weight: 800;', 
                  '.pre-logo img { width: 64px; height: auto; }\n.pre-logo {\n  font-family: var(--ff-head);\n  font-size: 2.2rem; font-weight: 800;')

# Navbar image style
# Let's find `.nav-logo {`
# We'll just append `.nav-logo-img { height: 32px; width: auto; }` and `.foot-logo-img { height: 48px; width: auto; margin-bottom: 16px; }` to the end of the file.
new_logo_css = """
/* Logo Image Styles */
.nav-logo-img { height: 36px; width: auto; object-fit: contain; }
.foot-logo-img { height: 56px; width: auto; margin-bottom: 24px; object-fit: contain; }
@media (max-width: 768px) {
  .nav-logo-img { height: 28px; }
  .foot-logo-img { height: 48px; margin-bottom: 20px; }
}
"""

css += new_logo_css

with open('css/main.css', 'w') as f:
    f.write(css)

