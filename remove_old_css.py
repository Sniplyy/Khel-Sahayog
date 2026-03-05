import os
import re

css_files = [f for f in os.listdir('.') if f.endswith('.css') and f != 'style.css' and f != 'cta-styles.css']

def remove_cta_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_length = len(content)
    
    classes_to_remove = [
        '.join-mission-section', '.join-mission-title', '.join-mission-text', '.join-mission-buttons',
        '.btn-partner', '.btn-donate-white', '.hockey-cta-section', '.hockey-cta-title', '.hockey-cta-text', '.hockey-cta-buttons',
        '.btn-support-yellow', '.btn-get-involved-white'
    ]
    
    for cls in classes_to_remove:
        # Match standard class block
        # Matches: .classname { ... }
        content = re.sub(r'(?m)^\s*' + cls.replace('.', r'\.') + r'\s*(?::hover)?\s*\{[^}]*\}', '', content)
        # Match class block with potential pseudo-classes like :hover or child selectors inside media queries
        content = re.sub(r'(?m)^\s*' + cls.replace('.', r'\.') + r'(?:[^\{]*?)\s*\{[^}]*\}', '', content)

    # Some classes might be combined like .join-mission-buttons .btn-partner
    content = re.sub(r'(?m).*?join-mission-.*?\{[^}]*\}', '', content)
    content = re.sub(r'(?m).*?hockey-cta-.*?\{[^}]*\}', '', content)

    if len(content) != original_length:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Cleaned {filepath}")

for f in css_files:
    remove_cta_css(f)
