import re

# 1. Delay Analytics in index.html
with open('index.html', 'r') as f:
    html = f.read()

analytics_script = """<script async src="https://www.googletagmanager.com/gtag/js?id=G-Y6RTH7XM5F"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-Y6RTH7XM5F');
  </script>"""

delayed_analytics = """<script>
    // Delayed Analytics
    setTimeout(function(){
      var s = document.createElement('script');
      s.async = true;
      s.src = "https://www.googletagmanager.com/gtag/js?id=G-Y6RTH7XM5F";
      document.head.appendChild(s);
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-Y6RTH7XM5F');
    }, 3500);
  </script>"""

html = html.replace(analytics_script, delayed_analytics)

# Update CSS/JS paths to .min versions
html = html.replace('href="css/main.css"', 'href="css/main.min.css"')
html = html.replace('src="js/app.js"', 'src="js/app.min.js"')

with open('index.html', 'w') as f:
    f.write(html)

# 2. Basic CSS Minification
with open('css/main.css', 'r') as f:
    css = f.read()

# Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
# Remove newlines and tabs
css = re.sub(r'\s+', ' ', css)
# Remove spaces around important chars
css = re.sub(r'\s*([\{\}\:\;\,\>\+\~])\s*', r'\1', css)
css = css.replace(';}', '}')

with open('css/main.min.css', 'w') as f:
    f.write(css)

# 3. Basic JS Minification
with open('js/app.js', 'r') as f:
    js = f.read()

# Remove multi-line comments
js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
# Remove single line comments (careful with URLs like http://)
js = re.sub(r'(?<!:)\/\/.*', '', js)
# Remove extra newlines
js = re.sub(r'\n+', '\n', js)
js = re.sub(r'\s+', ' ', js)
# Remove spaces around ops
js = re.sub(r'\s*([\{\}\(\)\=\;\,\>\<\+\-\*\/\:\!])\s*', r'\1', js)

with open('js/app.min.js', 'w') as f:
    f.write(js)

print('Optimizations applied!')
