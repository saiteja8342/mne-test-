const fs = require('fs');

let html = fs.readFileSync('index.html', 'utf8');

// Pre-logo img
html = html.replace(
  /<img src="image\/logo.png" alt="Logo">/,
  '<img src="image/logo.png" alt="Logo" width="200" height="50" fetchpriority="high" decoding="async">'
);

// Nav logo img
html = html.replace(
  /<img src="image\/logo.png" alt="MOTIONNODEEDITS" class="nav-logo-img">/,
  '<img src="image/logo.png" alt="MOTIONNODEEDITS" class="nav-logo-img" width="156" height="28" fetchpriority="high" decoding="async">'
);

// Foot logo img
html = html.replace(
  /<img src="image\/logo.png" alt="MOTIONNODEEDITS" class="foot-logo-img">/,
  '<img src="image/logo.png" alt="MOTIONNODEEDITS" class="foot-logo-img" width="180" height="32" loading="lazy" decoding="async">'
);

// Hero video
html = html.replace(
  /<video class="hero-vid" autoplay muted loop playsinline preload="metadata" aria-hidden="true">/,
  '<video class="hero-vid lazy-vid" muted loop playsinline preload="none" aria-hidden="true" poster="assets/posters/showreel-poster.webp" autoplay>'
);

html = html.replace(
  /<source src="assets\/ai-reel.mov" type="video\/mp4">/,
  '<source data-src="assets/posters/showreel-hero.webm" type="video/webm">\n      <source data-src="assets/posters/showreel-hero.mp4" type="video/mp4">'
);

// We'll just replace all portfolio videos with data-src and poster
let wcRegex = /<video class="wc-vid" poster="image\/logo.png" loading="lazy" muted loop playsinline preload="metadata">\s*<source src="assets\/videos\/([^"]+)" type="([^"]+)">\s*<\/video>/g;

html = html.replace(wcRegex, (match, src, type) => {
  let name = src.split('.')[0];
  return `<video class="wc-vid lazy-vid" poster="assets/posters/${name}.webp" loading="lazy" muted loop playsinline preload="none">
                <source data-src="assets/posters/${name}-preview.webm" type="video/webm">
                <source data-src="assets/posters/${name}-preview.mp4" type="video/mp4">
              </video>`;
});

// Remove defer from all script tags and then add it
html = html.replace(/<script src="js\/app.js"><\/script>/, '<script src="js/app.js" defer></script>');
html = html.replace(/<script src="https:\/\/cdnjs.cloudflare.com\/ajax\/libs\/gsap\/3.12.5\/gsap.min.js"><\/script>/, '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js" defer></script>');
html = html.replace(/<script src="https:\/\/cdnjs.cloudflare.com\/ajax\/libs\/gsap\/3.12.5\/ScrollTrigger.min.js"><\/script>/, '<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js" defer></script>');
html = html.replace(/<script src="https:\/\/cdn.jsdelivr.net\/npm\/lenis@1.1.18\/dist\/lenis.min.js"><\/script>/, '<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.18/dist/lenis.min.js" defer></script>');


fs.writeFileSync('index.html', html);
console.log("HTML optimized");
