#!/usr/bin/env python3
"""
Fix Markdown Links Script
This script fixes the remaining broken image links after the images were moved to assets/
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple

# Configuration
REPO_ROOT = Path(__file__).parent
MOVED_IMAGES_LOG = REPO_ROOT / "moved_images_log.json"

def load_moved_images_info() -> Dict[str, Dict[str, str]]:
    """Load the moved images information from the log file"""
    try:
        with open(MOVED_IMAGES_LOG, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: {MOVED_IMAGES_LOG} not found. Please run the image organization script first.")
        return {}

def find_markdown_files() -> List[Path]:
    """Find all markdown files in the repository"""
    markdown_files = []
    for root, dirs, files in os.walk(REPO_ROOT):
        for file in files:
            if file.endswith('.md') and not file.startswith('README_image_organizer'):
                file_path = Path(root) / file
                markdown_files.append(file_path)
    return markdown_files

def fix_broken_links(markdown_files: List[Path], moved_images_info: Dict[str, Dict[str, str]]) -> int:
    """
    Fix broken image links in markdown files
    Returns: Number of files that were updated
    """
    files_updated = 0
    total_links_fixed = 0
    
    print(f"🔗 Checking and fixing broken links in {len(markdown_files)} markdown files...")
    
    for md_file in markdown_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            links_fixed_in_file = 0
            
            # Check each moved image
            for original_relative_path, move_info in moved_images_info.items():
                # Convert Windows path separators to forward slashes for cross-platform compatibility
                original_relative_path_unix = original_relative_path.replace('\\', '/')
                
                # Get just the filename for local references
                original_filename = Path(original_relative_path).name
                new_filename = move_info['new_filename']
                
                # Calculate the correct relative path from this markdown file to the new assets location
                md_file_relative_to_repo = md_file.relative_to(REPO_ROOT)
                md_file_depth = len(md_file_relative_to_repo.parts) - 1
                
                if md_file_depth == 0:
                    new_relative_path = f"help/assets/{new_filename}"
                else:
                    dots = '../' * md_file_depth
                    new_relative_path = f"{dots}help/assets/{new_filename}"
                
                # Create patterns to search for and replace
                patterns_to_fix = [
                    # Local filename references (most common case)
                    (rf'(\[.*?\]\()({re.escape(original_filename)})(\))', new_relative_path),
                    (rf'(<img[^>]*src=")({re.escape(original_filename)})(")', new_relative_path),
                    (rf'(<img[^>]*src=\')({re.escape(original_filename)})(\')', new_relative_path),
                    
                    # Full relative path references
                    (rf'(\[.*?\]\()({re.escape(original_relative_path_unix)})(\))', new_relative_path),
                    (rf'(<img[^>]*src=")({re.escape(original_relative_path_unix)})(")', new_relative_path),
                    (rf'(<img[^>]*src=\')({re.escape(original_relative_path_unix)})(\')', new_relative_path),
                    
                    # Relative path variations
                    (rf'(\[.*?\]\()(\.\./[^)]*{re.escape(original_filename)})(\))', new_relative_path),
                    (rf'(\[.*?\]\()(\./[^)]*{re.escape(original_filename)})(\))', new_relative_path),
                    (rf'(<img[^>]*src=")(\.\./[^"]*{re.escape(original_filename)})(")', new_relative_path),
                    (rf'(<img[^>]*src=\')(\.\./[^\']*{re.escape(original_filename)})(\')', new_relative_path),
                ]
                
                # Apply each pattern
                for pattern, replacement_path in patterns_to_fix:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        replacement = rf'\g<1>{replacement_path}\g<3>'
                        new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)
                        
                        if new_content != content:
                            content = new_content
                            links_fixed_in_file += len(matches)
                            print(f"    🔧 Fixed {len(matches)} link(s) in {md_file_relative_to_repo}")
                            print(f"      {matches[0][1]} → {replacement_path}")
            
            # Write back if content changed
            if content != original_content:
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_updated += 1
                total_links_fixed += links_fixed_in_file
                
        except Exception as e:
            print(f"  ❌ Error processing {md_file}: {e}")
    
    return files_updated, total_links_fixed

def main():
    """Main execution function"""
    print("🚀 Starting broken link fix process...\n")
    
    # Load moved images information
    moved_images_info = load_moved_images_info()
    if not moved_images_info:
        return
    
    print(f"📋 Loaded information for {len(moved_images_info)} moved images")
    
    # Find markdown files
    markdown_files = find_markdown_files()
    print(f"📝 Found {len(markdown_files)} markdown files to check")
    
    # Fix broken links
    files_updated, total_links_fixed = fix_broken_links(markdown_files, moved_images_info)
    
    # Summary
    print(f"\n🎉 Link fixing complete!")
    print(f"  📝 Markdown files updated: {files_updated}")
    print(f"  🔗 Total links fixed: {total_links_fixed}")
    
    if files_updated > 0:
        print(f"\n💡 Tip: Use 'git diff' to review the changes made.")
    else:
        print(f"\n✅ No broken links found - all links are already correctly pointing to assets folder!")

if __name__ == "__main__":
    main()