import re

with open('index.html', 'r') as f:
    html = f.read()

def replace_video(match):
    full_match = match.group(0)
    
    # Extract title and tags from the wc-foot
    foot_match = re.search(r'<div class="wc-foot-left"><h3>(.*?)</h3><span>(.*?)</span></div>', full_match)
    if foot_match:
        title = foot_match.group(1)
        tags = foot_match.group(2)
    else:
        title = "Video"
        tags = "Cinematic"

    # remove autoplay from video, add poster and loading
    new_match = re.sub(r'<video class="wc-vid" autoplay muted loop playsinline preload="metadata">', 
                       r'<video class="wc-vid" poster="image/logo.png" loading="lazy" muted loop playsinline preload="metadata">', 
                       full_match)
                       
    # Add the overlay after the video
    overlay_html = f'''
              <div class="wc-custom-overlay">
                <div class="wc-play-btn">
                  <svg viewBox="0 0 24 24" fill="currentColor"><polygon points="5,3 19,12 5,21"/></svg>
                </div>
                <h3>{title}</h3>
                <span>{tags}</span>
              </div>'''
              
    new_match = re.sub(r'(<source[^>]+>\s*</video>)', r'\1' + overlay_html, new_match)
    return new_match

# Find all work-card blocks and replace
new_html = re.sub(r'<article class="work-card[^>]*>[\s\S]*?</article>', replace_video, html)

with open('index.html', 'w') as f:
    f.write(new_html)
print("Updated index.html")
