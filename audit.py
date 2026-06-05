import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.errors = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr', 'path', 'circle', 'polyline', 'line', 'rect', 'polygon'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.tags.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.tags:
            self.errors.append(f"Line {self.getpos()[0]}: Unexpected end tag </{tag}> (no open tags left)")
            return
        
        last_tag, pos = self.tags[-1]
        if last_tag == tag:
            self.tags.pop()
        else:
            self.errors.append(f"Line {self.getpos()[0]}: Mismatched end tag </{tag}>. Expected </{last_tag}> which was opened at line {pos[0]}")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

print("--- HTML VALIDATION ---")
parser = MyHTMLParser()
parser.feed(content)
if parser.errors:
    for e in parser.errors:
        print(e)
elif parser.tags:
    print(f"Unclosed tags remaining: {[t[0] for t in parser.tags]}")
else:
    print("HTML Structure is WELL-FORMED.")

print("\n--- CSS VALIDATION ---")
styles = re.findall(r'<style>(.*?)</style>', content, re.DOTALL)
css_errors = 0
for i, style in enumerate(styles):
    open_braces = style.count('{')
    close_braces = style.count('}')
    if open_braces != close_braces:
        print(f"Style block {i+1} has mismatched braces! {{ count: {open_braces}, }} count: {close_braces}")
        css_errors += 1
if css_errors == 0:
    print("CSS Braces are BALANCED.")

print("\n--- JS VALIDATION ---")
scripts = re.findall(r'<script>(.*?)</script>', content, re.DOTALL)
js_errors = 0
for i, script in enumerate(scripts):
    open_braces = script.count('{')
    close_braces = script.count('}')
    open_paren = script.count('(')
    close_paren = script.count(')')
    if open_braces != close_braces:
        print(f"Script block {i+1} has mismatched braces! {{ count: {open_braces}, }} count: {close_braces}")
        js_errors += 1
    if open_paren != close_paren:
        print(f"Script block {i+1} has mismatched parentheses! ( count: {open_paren}, ) count: {close_paren}")
        js_errors += 1
if js_errors == 0:
    print("JS Braces & Parentheses are BALANCED.")
    
