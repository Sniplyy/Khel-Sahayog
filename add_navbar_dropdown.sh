#!/bin/bash

# Script to add dropdown navbar to all HTML files
# This script adds the dropdown menu structure and JavaScript to HTML files

# Define the dropdown HTML to insert after </div> closing the nav-container
DROPDOWN_HTML='        
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
        </div>'

# Define the JavaScript to insert before </body>
DROPDOWN_JS='    
    <script>
        // Dropdown menu functionality
        const programsDropdown = document.querySelector('\''.programs-dropdown'\'');
        const dropdownMenu = document.querySelector('\''.dropdown-menu'\'');
        const dropdownBackdrop = document.querySelector('\''.dropdown-backdrop'\'');
        let dropdownTimeout;

        // Show dropdown on hover
        programsDropdown.addEventListener('\''mouseenter'\'', () => {
            clearTimeout(dropdownTimeout);
            dropdownMenu.classList.add('\''active'\'');
            dropdownBackdrop.classList.add('\''active'\'');
        });

        // Keep dropdown open when hovering over the menu
        dropdownMenu.addEventListener('\''mouseenter'\'', () => {
            clearTimeout(dropdownTimeout);
            dropdownMenu.classList.add('\''active'\'');
            dropdownBackdrop.classList.add('\''active'\'');
        });

        // Hide dropdown when leaving the trigger
        programsDropdown.addEventListener('\''mouseleave'\'', () => {
            dropdownTimeout = setTimeout(() => {
                dropdownMenu.classList.remove('\''active'\'');
                dropdownBackdrop.classList.remove('\''active'\'');
            }, 100);
        });

        // Hide dropdown when leaving the menu
        dropdownMenu.addEventListener('\''mouseleave'\'', () => {
            dropdownTimeout = setTimeout(() => {
                dropdownMenu.classList.remove('\''active'\'');
                dropdownBackdrop.classList.remove('\''active'\'');
            }, 100);
        });

        // Hide dropdown when clicking on backdrop
        dropdownBackdrop.addEventListener('\''click'\'', () => {
            dropdownMenu.classList.remove('\''active'\'');
            dropdownBackdrop.classList.remove('\''active'\'');
        });
    </script>'

# List of HTML files to update (excluding homepage.html and hockey.html which are already done)
FILES=(
    "grassroots_development.html"
    "athlete_management.html"
    "contact_us.html"
    "about.html"
    "athletics.html"
    "badminton.html"
    "donate.html"
    "drug_awareness.html"
    "football.html"
    "get_involved.html"
    "impact.html"
    "job_skilling.html"
    "kabaddi.html"
    "mental_heath.html"
    "Programs.html"
    "rugby.html"
    "women_empowerment.html"
)

echo "Starting navbar dropdown update for HTML files..."

for file in "${FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Processing $file..."
        
        # Create backup
        cp "$file" "$file.bak"
        
        # Add dropdown HTML after nav-container closing div (before </nav>)
        sed -i '' '/<\/div>$/N; s/<\/div>\n\([ ]*\)<\/nav>/&\n'"$DROPDOWN_HTML"'\n\1<\/nav>/' "$file" 2>/dev/null || \
        perl -i -pe 's/(<\/div>\s*<\/nav>)/$1\n'"$(echo "$DROPDOWN_HTML" | sed 's/\\/\\\\/g; s/\//\\\//g; s/&/\\&/g')"'\n/g' "$file"
        
        # Add JavaScript before </body>
        sed -i '' 's/<\/body>/'"$(echo "$DROPDOWN_JS" | sed 's/\\/\\\\/g; s/\//\\\//g; s/&/\\&/g')"'\n<\/body>/' "$file"
        
        echo "✓ Updated $file"
    else
        echo "✗ File not found: $file"
    fi
done

echo "Done! All HTML files have been updated."
echo "Backup files created with .bak extension"
