import sys

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()

        with open('new_hero.html', 'r', encoding='utf-8') as f:
            new_hero = f.read()

        start_marker = "<!-- ═══════════════════════════════════════════\n     HERO\n═══════════════════════════════════════════ -->"
        end_marker = "<style>\n  /* Premium Trust Section */"

        start_idx = content.find(start_marker)
        end_idx = content.find(end_marker)

        if start_idx == -1:
            print("Error: Start marker not found in index.html.")
            sys.exit(1)
        if end_idx == -1:
            print("Error: End marker not found in index.html.")
            sys.exit(1)

        new_content = content[:start_idx] + new_hero + "\n" + content[end_idx:]

        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)

        print("Hero section replaced successfully!")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
