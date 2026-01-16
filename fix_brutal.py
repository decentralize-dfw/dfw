#!/usr/bin/env python3
import re

# Read the file
with open('/home/user/dfw/index-beton.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and extract the style block
style_match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
if not style_match:
    print("Style block not found!")
    exit(1)

old_style = style_match.group(1)

# FIX 1: Desktop/Mobile visibility
# Replace mobile media query section
old_mobile_media = r'@media \(max-width:768px\)\{body\{padding:0 !important\}\.finder-window,#desktop-icons,#minimized-icon-container,#window-container\{display:none !important\}#mobile-interface\{display:flex !important\}\}'

new_mobile_media = '''@media (max-width:768px){
  body{padding:0 !important}
  .finder-window,#desktop-icons,#minimized-icon-container,#window-container{display:none !important}
  #mobile-interface{display:flex !important}
  #circular-navigation{display:none !important}
}'''

old_style = re.sub(old_mobile_media, new_mobile_media, old_style)

# FIX 2: Desktop media query - SHOW circular-navigation
old_desktop_media = r'@media \(min-width:769px\)\{\.finder-window\{display:none !important\}#circular-navigation\{display:flex !important\}\}'

new_desktop_media = '''@media (min-width:769px){
  .finder-window{display:none !important}
  #circular-navigation{display:flex !important}
}'''

old_style = re.sub(old_desktop_media, new_desktop_media, old_style)

# FIX 3: Lighten icon filters - PNGs must be visible!
# Mobile app icons
old_style = old_style.replace(
    'filter: grayscale(0.9) contrast(1.3) !important;',
    'filter: grayscale(0.3) contrast(1.05) !important;'
)

# FIX 4: Remove noise overlay - too heavy
# Remove ::after noise from mobile icons
old_style = re.sub(
    r'\.mobile-app-icon-image::after \{[^}]+\}',
    '',
    old_style
)

# Remove ::after noise from circular icons
old_style = re.sub(
    r'\.circular-item-icon::after \{[^}]+\}',
    '',
    old_style
)

# FIX 5: Make sure #circular-navigation has correct default display
old_style = old_style.replace(
    '#circular-navigation {\n  display: none;',
    '#circular-navigation {\n  display: flex;'
)

# Write the fixed content
new_content = content.replace(f'<style>{style_match.group(1)}</style>', f'<style>{old_style}</style>')

with open('/home/user/dfw/index-beton.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ Desktop/Mobile visibility FIXED!")
print("✅ #circular-navigation: Desktop SHOW, Mobile HIDE")
print("✅ Icon filters lightened: grayscale(0.3) contrast(1.05)")
print("✅ Noise overlay REMOVED - PNGs now visible!")
