#!/usr/bin/env python3
"""
Strip Images Script
===================
Removes image boxes and image tags from all generated Jekyll posts in _posts/
"""

import os
import re

posts_dir = os.path.join(os.path.dirname(__file__), "_posts")

def clean_post(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove <div class="post-img-box">...</div> blocks
    cleaned = re.sub(r'<div class="post-img-box">.*?</div>', '', content, flags=re.DOTALL)
    
    # Remove markdown image syntax ![...](...)
    cleaned = re.sub(r'!\[.*?\]\(.*?\)', '', cleaned)
    
    # Remove empty lines left behind by image removal
    cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(cleaned)

def main():
    if not os.path.exists(posts_dir):
        print("No _posts directory found.")
        return

    files = [f for f in os.listdir(posts_dir) if f.endswith(".md")]
    print(f"Cleaning image tags from {len(files)} post files...")

    for filename in files:
        filepath = os.path.join(posts_dir, filename)
        clean_post(filepath)

    print("✨ Successfully stripped all images from posts!")

if __name__ == "__main__":
    main()
