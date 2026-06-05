import re

with open('index.html', 'r') as f:
    html = f.read()

# 1. Update Head section
new_head = """<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- Primary Meta Tags -->
  <title>MOTIONNODEEDITS | Premier AI Video Editing Agency</title>
  <meta name="title" content="MOTIONNODEEDITS | Premier AI Video Editing Agency">
  <meta name="description" content="MOTIONNODEEDITS is a premium AI video editing agency specializing in cinematic video editing, viral reels editing, commercial ads, and AI avatar videos.">
  <meta name="keywords" content="AI video editing agency, cinematic video editing, reels editing, short-form video editing, commercial ad editing, AI avatar videos">
  <meta name="author" content="MOTIONNODEEDITS">
  <meta name="robots" content="index, follow">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://motionnodeedits.com/">
  <meta property="og:title" content="MOTIONNODEEDITS | AI Video Editing Agency">
  <meta property="og:description" content="Premium short-form video editing, cinematic commercial ads, and AI avatar videos designed to scale your brand.">
  <meta property="og:image" content="https://motionnodeedits.com/image/logo.png">

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://motionnodeedits.com/">
  <meta name="twitter:title" content="MOTIONNODEEDITS | AI Video Editing Agency">
  <meta name="twitter:description" content="Premium short-form video editing, cinematic commercial ads, and AI avatar videos designed to scale your brand.">
  <meta name="twitter:image" content="https://motionnodeedits.com/image/logo.png">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://motionnodeedits.com/">

  <link rel="icon" href="image/logo.png" type="image/png">

  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="css/main.min.css">
</head>"""

html = re.sub(r'<head>.*?</head>', new_head, html, flags=re.DOTALL)

# 2. Update H2s
# "Cinematic Showcase" -> "Cinematic <em>Video Editing</em> Showcase"
html = re.sub(r'<h2 class="sec-title" id="work-title">Cinematic <em>Showcase</em></h2>', '<h2 class="sec-title" id="work-title">Cinematic <em>Video Editing</em> Showcase</h2>', html)

# "Creative Services" -> "AI & Cinematic <em>Services</em>"
html = re.sub(r'<h2 class="sec-title" id="svc-title">Creative <em>Services</em></h2>', '<h2 class="sec-title" id="svc-title">AI & Cinematic <em>Editing Services</em></h2>', html)

# "The Results" -> "Client <em>Results</em> & ROI"
html = re.sub(r'<h2 class="sec-title" id="res-title">The <em>Results</em></h2>', '<h2 class="sec-title" id="res-title">Client <em>Results</em> & ROI</h2>', html)

# Add keywords naturally in the hero subheadline if they aren't there.
# It currently is: "Premium AI cinematic edits for creators, brands, and businesses.<br>Built for reels, ads, launches, and social growth."
# It's already good.

# Write it out
with open('index.html', 'w') as f:
    f.write(html)

print('SEO Updated!')
