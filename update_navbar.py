#!/usr/bin/env python3
"""
Script to add dropdown navbar to remaining HTML files
"""

import os
import re

# Dropdown HTML to insert after nav-container closing div
DROPDOWN_HTML = '''        
        <!-- Dropdown Backdrop Blur -->
        <div class="dropdown-backdrop"></div>
        
        <!-- Programs Dropdown Menu -->
        <div class="dropdown-menu">
            <div class="dropdown-container">
                <div class="dropdown-section">
                    <h3 class="dropdown-heading">Our Programs</h3>
                    <ul class="dropdown-list">
                        <li><a href="grassroots_development.html" class="dropdown-link">Grassroots Development</a></li>
                        <li><a href="athlete_management.html" class="dropdown-link">Athlete Management</a></li>
                        <li><a href="hockey.html" class="dropdown-link">Hockey Programs</a></li>
                        <li><a href="#" class="dropdown-link">Coach Training</a></li>
                    </ul>
                </div>
                <div class="dropdown-section">
                    <h3 class="dropdown-heading">Sports</h3>
                    <ul class="dropdown-list">
                        <li><a href="hockey.html" class="dropdown-link">Hockey</a></li>
                        <li><a href="football.html" class="dropdown-link">Football</a></li>
                        <li><a href="athletics.html" class="dropdown-link">Athletics</a></li>
                        <li><a href="badminton.html" class="dropdown-link">Badminton</a></li>
                    </ul>
                </div>
                <div class="dropdown-section">
                    <h3 class="dropdown-heading">Support</h3>
                    <ul class="dropdown-list">
                        <li><a href="impact.html" class="dropdown-link">Program Impact</a></li>
                        <li><a href="#" class="dropdown-link">Success Stories</a></li>
                        <li><a href="contact_us.html" class="dropdown-link">Get Involved</a></li>
                    </ul>
                </div>
            </div>
        </div>'''

# JavaScript to insert before </body>
DROPDOWN_JS = '''    
    <script>
        // Dropdown menu functionality
        const programsDropdown = document.querySelector('.programs-dropdown');
        const dropdownMenu = document.querySelector('.dropdown-menu');
        const dropdownBackdrop = document.querySelector('.dropdown-backdrop');
        let dropdownTimeout;

        // Show dropdown on hover
        programsDropdown.addEventListener('mouseenter', () => {
            clearTimeout(dropdownTimeout);
            dropdownMenu.classList.add('active');
            dropdownBackdrop.classList.add('active');
        });

        // Keep dropdown open when hovering over the menu
        dropdownMenu.addEventListener('mouseenter', () => {
            clearTimeout(dropdownTimeout);
            dropdownMenu.classList.add('active');
            dropdownBackdrop.classList.add('active');
        });

        // Hide dropdown when leaving the trigger
        programsDropdown.addEventListener('mouseleave', () => {
            dropdownTimeout = setTimeout(() => {
                dropdownMenu.classList.remove('active');
                dropdownBackdrop.classList.remove('active');
            }, 100);
        });

        // Hide dropdown when leaving the menu
        dropdownMenu.addEventListener('mouseleave', () => {
            dropdownTimeout = setTimeout(() => {
                dropdownMenu.classList.remove('active');
                dropdownBackdrop.classList.remove('active');
            }, 100);
        });

        // Hide dropdown when clicking on backdrop
        dropdownBackdrop.addEventListener('click', () => {
            dropdownMenu.classList.remove('active');
            dropdownBackdrop.classList.remove('active');
        });
    </script>'''

# Files to update (excluding already completed ones)
FILES_TO_UPDATE = [
    "about.html",
    "athletics.html",
    "badminton.html",
    "donate.html",
    "drug_awareness.html",
    "football.html",
    "get_involved.html",
    "impact.html",
    "job_skilling.html",
    "kabaddi.html",
    "mental_heath.html",
    "Programs.html",
    "rugby.html",
    "women_empowerment.html"
]

def update_html_file(filepath):
    """Add dropdown menu and JavaScript to an HTML file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already updated
        if 'dropdown-backdrop' in content:
            print(f"  ⏭️  {filepath} - Already has dropdown, skipping")
            return False
        
        # Add dropdown HTML after nav-container closing div, before </nav>
        # Find the pattern: </div>\n        </nav> or </div>\n    </nav>
        pattern = r'(</div>\s*)(</nav>)'
        
        # Check if we can find the nav closing tag
        if not re.search(pattern, content):
            print(f"  ❌ {filepath} - Could not find nav closing pattern")
            return False
        
        # Insert dropdown HTML
        content = re.sub(
            pattern,
            r'\1' + DROPDOWN_HTML + r'\n        \2',
            content,
            count=1
        )
        
        # Add JavaScript before </body>
        content = content.replace('</body>', DROPDOWN_JS + '\n</body>')
        
        # Write back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"  ✅ {filepath} - Successfully updated")
        return True
        
    except Exception as e:
        print(f"  ❌ {filepath} - Error: {str(e)}")
        return False

def main():
    print("🚀 Starting navbar dropdown update...\n")
    
    updated = 0
    skipped = 0
    failed = 0
    
    for filename in FILES_TO_UPDATE:
        if os.path.exists(filename):
            result = update_html_file(filename)
            if result:
                updated += 1
            elif result is False and 'Already has dropdown' in str(result):
                skipped += 1
            else:
                failed += 1
        else:
            print(f"  ⚠️  {filename} - File not found")
            failed += 1
    
    print(f"\n📊 Summary:")
    print(f"  ✅ Updated: {updated}")
    print(f"  ⏭️  Skipped: {skipped}")
    print(f"  ❌ Failed: {failed}")
    print(f"\n✨ Done!")

if __name__ == "__main__":
    main()
