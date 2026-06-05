import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove full CSS property lines for filter and backdrop-filter
content = re.sub(r'^\s*(?:-webkit-)?backdrop-filter:\s*blur\([^)]+\);?\s*$\n?', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*filter:\s*blur\([^)]+\);?\s*$\n?', '', content, flags=re.MULTILINE)

# Remove inline backdrop-filter: blur(...);
content = re.sub(r'(?:-webkit-)?backdrop-filter:\s*blur\([^)]+\);?', '', content)
content = re.sub(r'filter:\s*blur\([^)]+\);?', '', content)

# Remove filter: "blur(...)" from JS objects
content = re.sub(r',\s*filter:\s*[\'"]blur\([^)]+\)[\'"]', '', content)
content = re.sub(r'filter:\s*[\'"]blur\([^)]+\)[\'"]\s*,', '', content)
content = re.sub(r'filter:\s*[\'"]blur\([^)]+\)[\'"]', '', content)

# Handle the complex scroll blur logic in GSAP around line 3043
content = re.sub(r'filter:\s*`blur\(\$\{blur\}px\)`', '/* removed blur */', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Blurs removed successfully.")
