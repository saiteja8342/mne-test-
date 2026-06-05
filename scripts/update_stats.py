import re

with open('css/main.css', 'r') as f:
    css = f.read()

# Replace .hero-stats through .hs-l { ... }
new_stats_css = """/* Stats strip */
.hero-stats {
  position: relative; z-index: 2;
  display: inline-flex; align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  margin-top: 56px;
  background: rgba(255,255,255,.02);
  border: 1px solid rgba(255,255,255,.08);
  border-radius: 100px;
  backdrop-filter: blur(24px) saturate(140%);
  overflow: hidden;
  opacity: 0; transform: translateY(20px);
}
.hs-item {
  display: flex; flex-direction: row; align-items: center; justify-content: center; gap: 8px;
  padding: 16px 32px;
  position: relative;
}
.hs-item + .hs-item::before {
  content: ''; position: absolute; left: 0; top: 12px; bottom: 12px;
  width: 1px; background: rgba(255,255,255,.08);
}
.hs-n {
  font-family: var(--ff-head); font-size: 1.15rem;
  font-weight: 700; line-height: 1; display: inline; color: #fff;
}
.hs-s {
  font-family: var(--ff-head); font-size: 1.15rem;
  color: var(--purple-light); font-weight: 700;
  margin-left: 1px; line-height: 1;
}
.hs-l {
  font-size: .9rem; color: rgba(255,255,255,.7);
  font-weight: 500;
  letter-spacing: .02em; white-space: nowrap;
}"""

css = re.sub(r'/\* Stats strip \*/.*?\.hs-l \{[^}]+\}', new_stats_css, css, flags=re.DOTALL)

# Update mobile CSS
new_mobile_stats = """.hero-stats { flex-direction: column; width: calc(100% - 32px); border-radius: 16px; margin-top: 32px; }
  .hs-item { padding: 16px 24px; width: 100%; justify-content: space-between; gap: 16px; }
  .hs-item + .hs-item::before { top: 0; left: 24px; right: 24px; bottom: auto; width: auto; height: 1px; }"""

css = re.sub(r'\.hero-stats \{ flex-direction: column; width: calc\(100% - 32px\); \}', new_mobile_stats, css)

with open('css/main.css', 'w') as f:
    f.write(css)

print("Updated stats CSS")
