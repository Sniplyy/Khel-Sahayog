import os
import re
import glob

css_files = [
    'hockey.css', 'rugby.css', 'kabaddi.css', 'athletics.css',
    'tabletennis.css', 'badminton.css'
]

for filename in css_files:
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
        
    # Remove the broken 'min-' and 'max-' lines left over
    content = re.sub(r'\n\s*min-\n\s*max-\n', '\n', content)
    
    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filename}")

