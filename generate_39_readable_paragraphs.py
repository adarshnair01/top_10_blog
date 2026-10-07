#!/usr/bin/env python3
"""
Master Builder for 39 Pure Narrative Top 10 Posts across 13 Categories.
- Pure readable paragraphs.
- Zero tables, zero key specs lines, zero blockquotes.
- Frontmatter includes `image:` for homepage cards.
"""

import os
import re
from datetime import datetime, timedelta

from post_data_part1 import PART_1_POSTS
from post_data_part2 import PART_2_POSTS
from post_data_part3 import PART_3_POSTS
from post_data_part4 import PART_4_POSTS
from post_data_part5 import PART_5_POSTS
from post_data_part6 import PART_6_POSTS
from post_data_part7 import PART_7_POSTS
from post_data_part8 import PART_8_POSTS
from post_data_part9 import PART_9_POSTS
from post_data_part10 import PART_10_POSTS
from post_data_part11 import PART_11_POSTS
from post_data_part12 import PART_12_POSTS
from post_data_part13 import PART_13_POSTS
from post_data_part14 import PART_14_POSTS
from post_data_part15 import PART_15_POSTS
from post_data_part16 import PART_16_POSTS

ALL_POSTS = (
    PART_1_POSTS + PART_2_POSTS + PART_3_POSTS + PART_4_POSTS +
    PART_5_POSTS + PART_6_POSTS + PART_7_POSTS + PART_8_POSTS +
    PART_9_POSTS + PART_10_POSTS + PART_11_POSTS + PART_12_POSTS +
    PART_13_POSTS + PART_14_POSTS + PART_15_POSTS + PART_16_POSTS
)

posts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_posts")

if os.path.exists(posts_dir):
    for f in os.listdir(posts_dir):
        if f.endswith(".md"):
            os.remove(os.path.join(posts_dir, f))
else:
    os.makedirs(posts_dir, exist_ok=True)

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')[:55]

IMAGES = {
    "travel_logistics": [
        "https://images.unsplash.com/photo-1532105956626-9569c03602f6?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1200&q=80"
    ],
    "remote_work": [
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1200&q=80"
    ],
    "ai_professions": [
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1677442136019-21780efad99a?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80"
    ],
    "can_i_queries": [
        "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&q=80"
    ],
    "what_happens_if": [
        "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1508873696983-2df515122519?auto=format&fit=crop&w=1200&q=80"
    ],
    "bureaucracy": [
        "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=1200&q=80"
    ],
    "banking_problems": [
        "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?auto=format&fit=crop&w=1200&q=80"
    ],
    "credit_cards": [
        "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1542903660-eedba2cda473?auto=format&fit=crop&w=1200&q=80"
    ],
    "tax_edge_cases": [
        "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&q=80"
    ],
    "error_dictionary": [
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=80"
    ],
    "remote_work_logistics": [
        "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1200&q=80"
    ],
    "moving_to_india": [
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
    ],
    "can_i_carry": [
        "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1530521954074-e64f6810b32d?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1553531384-cc64ac80f931?auto=format&fit=crop&w=1200&q=80"
    ]
}

print(f"Generating {len(ALL_POSTS)} pure narrative blog posts...")

start_date = datetime(2026, 10, 7)
cat_counters = {}

for idx, post in enumerate(ALL_POSTS):
    cat_key = post["category"]
    title = post["title"]
    p1 = post.get("intro_p1", post.get("p1", ""))
    p2 = post.get("intro_p2", post.get("p2", ""))
    items = post["items"]
    
    cat_counters[cat_key] = cat_counters.get(cat_key, 0) + 1
    cat_idx = cat_counters[cat_key] - 1
    
    date_str = (start_date - timedelta(days=idx)).strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(posts_dir, filename)
    
    img_list = IMAGES.get(cat_key, [
        "https://images.unsplash.com/photo-1532105956626-9569c03602f6?auto=format&fit=crop&w=1200&q=80"
    ])
    img_url = img_list[cat_idx % len(img_list)]
    
    md = []
    md.append("---")
    md.append("layout: default")
    md.append(f'title: "{title}"')
    md.append(f"date: {date_str}")
    md.append(f"categories: [{cat_key}]")
    md.append('author: "Adarsh Nair"')
    md.append("nav_exclude: true")
    md.append(f'image: "{img_url}"')
    md.append("---\n")
    
    # Clean introductory paragraphs
    md.append(f"{p1}\n")
    md.append(f"{p2}\n")
    
    # 10 Countdown Items (#10 to #1) formatted as pure, highly readable paragraphs
    for rank in range(10, 0, -1):
        item = items[10 - rank]
        item_title, specs, desc, rule, context, tip = item
        
        md.append(f"## {rank}. {item_title}\n")
        
        # Paragraph 1: Description and context woven together
        para1 = f"{desc} {context} Key operational metrics show {specs.lower() if specs[0].isupper() else specs}."
        md.append(f"{para1}\n")
        
        # Paragraph 2: Official rule and practical tip in smooth narrative prose
        tip_text = tip if tip.startswith("Keep") or tip.startswith("Ensure") or tip.startswith("Apply") or tip.startswith("Book") else f"For best results, {tip[0].lower() + tip[1:]}"
        para2 = f"{rule} {tip_text}\n"
        md.append(para2)
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

print(f"SUCCESS! Built all {len(ALL_POSTS)} narrative blog posts in _posts/.")
