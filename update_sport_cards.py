import os
import re
import glob

css_files = [
    'hockey.css', 'rugby.css', 'kabaddi.css', 'athletics.css',
    'tabletennis.css', 'badminton.css'
]

# We want to replace width: 80%; or width: calc(...); or whatever is there with width: 100%;
# and we also might need to add max-width: 100%; and min-width: 0;

for filename in css_files:
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
        
    # Find .program-card1 block and adjust
    def replace_width(match):
        block = match.group(1)
        # remove existing width, min-width, max-width
        block = re.sub(r'\s*width:\s*[^;]+;', '', block)
        block = re.sub(r'\s*min-width:\s*[^;]+;', '', block)
        block = re.sub(r'\s*max-width:\s*[^;]+;', '', block)
        
        # trim trailing space before closing brace
        block = block.rstrip()
        
        # add our new properties
        new_props = "\n    min-width: 0;\n    max-width: 100%;\n    width: 100%;\n"
        return block + new_props + "}"
        
    content = re.sub(r'(\.program-card1\s*\{[^\}]*)\}', replace_width, content)
    content = re.sub(r'(\.program-card2\s*\{[^\}]*)\}', replace_width, content)
    content = re.sub(r'(\.program-card\s*\{[^\}]*)\}', replace_width, content) # Catch .program-card if used
    
    # Also adjust .programs-grid if needed
    def replace_grid(match):
        block = match.group(1)
        block = re.sub(r'\s*max-width:\s*[^;]+;', '', block)
        block = re.sub(r'\s*width:\s*[^;]+;', '', block)
        block = block.rstrip()
        
        # match football.css's max-width: 1000px
        new_props = "\n    max-width: 1000px;\n    width: 100%;\n"
        return block + new_props + "}"

    content = re.sub(r'(\.programs-grid\s*\{[^\}]*)\}', replace_grid, content)
    
    if content != original:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename}")

