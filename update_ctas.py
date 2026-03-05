import os
import re

def get_original_content(content, filename):
    # Find title
    title_match = re.search(r'<h2 class="(?:join-title|support-title|hockey-cta-title|join-mission-title|section-title)">(.*?)</h2>', content)
    # Find text
    text_match = re.search(r'<p class="(?:join-description|support-description|hockey-cta-text|join-mission-text|section-text)">([\s\S]*?)</p>', content)
    
    # Defaults
    original_title = title_match.group(1).strip() if title_match else "JOIN OUR MISSION"
    original_text = text_match.group(1).strip() if text_match else "Whether you're a corporate partner, individual donor, or volunteer, there's a role for you in transforming India's sports landscape."
    
    return original_title, original_text

def replace_cta_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_title, original_text = get_original_content(content, filepath)
    
    replacement = f"""  <section class="cta-section">
    <h2 class="cta-title">{original_title}</h2>
    <p class="cta-text">
      {original_text}
    </p>
    <div class="cta-buttons">
      <button class="btn-cta-primary"><a href="donate.html">Support Our Mission</a></button>
      <button class="btn-cta-secondary"><a href="get_involved.html">Get Involved</a></button>
    </div>
  </section>"""

    # We need to replace specific CTA sections
    modified = False
    
    if filepath == 'index.html':
        # Replace join-section and support-section
        regex = r'<section class="join-section">[\s\S]*?</section>\s*<!-- Support Section -->\s*<section class="support-section">[\s\S]*?</section>'
        if re.search(regex, content):
            content = re.sub(regex, replacement, content)
            modified = True
    elif filepath == 'hockey.html':
        # Replace hockey-cta-section
        regex = r'<!-- Bottom CTA Section -->\s*<section class="hockey-cta-section">[\s\S]*?</section>'
        if re.search(regex, content):
            content = re.sub(regex, "<!-- Bottom CTA Section -->\n" + replacement, content)
            modified = True
    else:
        # Most pages use join-mission-section
        regex = r'<!-- JOIN OUR MISSION Section -->\s*<section class="join-mission-section">[\s\S]*?</section>'
        if re.search(regex, content):
            content = re.sub(regex, "<!-- Bottom CTA Section -->\n" + replacement, content)
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        replace_cta_in_file(filename)
