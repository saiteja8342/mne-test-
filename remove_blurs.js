const fs = require('fs');

let content = fs.readFileSync('index.html', 'utf8');

// Remove full CSS property lines for filter and backdrop-filter
content = content.replace(/^\s*(?:-webkit-)?backdrop-filter:\s*blur\([^)]+\);?\s*$/gm, '');
content = content.replace(/^\s*filter:\s*blur\([^)]+\);?\s*$/gm, '');

// Remove inline backdrop-filter: blur(...);
content = content.replace(/backdrop-filter:\s*blur\([^)]+\);?/g, '');
content = content.replace(/-webkit-backdrop-filter:\s*blur\([^)]+\);?/g, '');
content = content.replace(/filter:\s*blur\([^)]+\);?/g, '');

// Remove filter: "blur(...)" from JS objects
content = content.replace(/,\s*filter:\s*['"]blur\([^)]+\)['"]/g, '');
content = content.replace(/filter:\s*['"]blur\([^)]+\)['"]\s*,/g, '');
content = content.replace(/filter:\s*['"]blur\([^)]+\)['"]/g, '');

// Handle the complex scroll blur logic in GSAP around line 3043
// This was likely a custom cursor or scroll effect that had blur. 
// We'll replace filter: `blur(${blur}px)` with nothing.
content = content.replace(/filter:\s*`blur\(\$\{blur\}px\)`/g, '/* removed blur */');

fs.writeFileSync('index.html', content, 'utf8');
console.log("Blurs removed successfully.");
