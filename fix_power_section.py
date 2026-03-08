import os
import re

sports = ['rugby', 'football', 'kabaddi', 'athletics', 'tabletennis', 'badminton']

for sport in sports:
    filename = f'{sport}.css'
    if not os.path.exists(filename):
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Remove padding-top: 100px; from the <sport>-left-column
    # Specifically replacing:
    # .<sport>-left-column {
    #     display: flex;
    #     flex-direction: column;
    #     padding-top: 100px;
    # }
    
    # We can just remove "padding-top: 100px;" anywhere it occurs inside the block for .<sport>-left-column
    pattern_left = r'(\.' + sport + r'-left-column\s*\{[^}]*?)\s*padding-top:\s*100px;\s*([^}]*\})'
    content = re.sub(pattern_left, r'\1\2', content)
    
    # Replace grid-template-columns: repeat(2, 1fr); with grid-template-columns: 1fr;
    # in the <sport>-benefits class block
    pattern_benefits = r'(\.' + sport + r'-benefits\s*\{[^}]*?)grid-template-columns:\s*repeat\(2,\s*1fr\);([^}]*\})'
    content = re.sub(pattern_benefits, r'\1grid-template-columns: 1fr;\2', content)

    # We also need to do this globally for .<sport>-benefits without getting too greedy.
    # Actually, a simpler approach is to find:
    # .<sport>-benefits {
    #     grid-template-columns: repeat(2, 1fr);
    # }
    # and replace the repeat(2, 1fr);
    # Lets just replace it everywhere within the file as long as it's following .<sport>-benefits
    content = re.sub(r'(\.' + sport + r'-benefits[^{]*\{[^}]*?)grid-template-columns:\s*repeat\(2,\s*1fr\);', r'\1grid-template-columns: 1fr;', content)
    # in case there are multiple, re-run
    content = re.sub(r'(\.' + sport + r'-benefits[^{]*\{[^}]*?)grid-template-columns:\s*repeat\(2,\s*1fr\);', r'\1grid-template-columns: 1fr;', content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
