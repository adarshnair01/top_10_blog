#!/usr/bin/env python3
"""
Master Builder for 39 Pure Text-Only Long-Form Magazine Blog Posts across 13 Categories.
- Comprehensive 2,500+ word detailed articles per post.
- Multi-paragraph narrative under every countdown item (#10 to #1).
- Text-only design: Zero images, zero tables, zero key spec badges, zero blockquotes.
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

print(f"Generating {len(ALL_POSTS)} text-only long-form narrative blog posts...")

start_date = datetime(2026, 10, 7)

for idx, post in enumerate(ALL_POSTS):
    cat_key = post["category"]
    title = post["title"]
    p1 = post.get("intro_p1", post.get("p1", ""))
    p2 = post.get("intro_p2", post.get("p2", ""))
    items = post["items"]
    
    date_str = (start_date - timedelta(days=idx)).strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(posts_dir, filename)
    
    md = []
    md.append("---")
    md.append("layout: default")
    md.append(f'title: "{title}"')
    md.append(f"date: {date_str}")
    md.append(f"categories: [{cat_key}]")
    md.append('author: "Adarsh Nair"')
    md.append("nav_exclude: true")
    md.append("---\n")
    
    # 4-Paragraph Article Introduction (Text-Only)
    md.append(f"{p1}\n")
    md.append(f"{p2}\n")
    md.append(
        f"Navigating this landscape effectively requires analyzing key operational metrics, statutory provisions, "
        f"and real-world edge cases. In this guide, we break down the top 10 aspects you need to know, combining official regulatory "
        f"guidelines with actionable insider insights for seamless execution across India.\n"
    )
    md.append(
        f"Whether you are planning long-term strategies or resolving immediate operational hurdles, the following comprehensive breakdown "
        f"provides a clear roadmap tailored to current Indian frameworks and administrative realities.\n"
    )
    
    # 10 Detailed Long-Form Items (#10 down to #1)
    for rank in range(10, 0, -1):
        item = items[10 - rank]
        item_title, specs, desc, rule, context, tip = item
        
        md.append(f"## {rank}. {item_title}\n")
        
        # Paragraph 1: Operational Overview & Specs
        para1 = (
            f"{desc} From an operational standpoint, this is governed by key parameters including {specs}. "
            f"Understanding these core mechanics is essential for ensuring smooth execution and avoiding unexpected bottlenecks."
        )
        md.append(f"{para1}\n")
        
        # Paragraph 2: System Mechanics & Background Context
        para2 = (
            f"{context} Over recent years, administrative and service frameworks across Indian states have undergone rapid modernization. "
            f"The integration of digital verification portals and automated tracking has streamlined processing, but it also means users must maintain accurate documentation and adhere strictly to procedural standards."
        )
        md.append(f"{para2}\n")
        
        # Paragraph 3: Statutory Rule & Legal Provisions
        para3 = (
            f"Under official guidelines, {rule.lower() if rule[0].isupper() else rule} "
            f"Regulatory bodies and statutory authorities enforce these rules firmly, and non-compliance can lead to processing delays, administrative fines, or formal notices. Keeping verified digital copies and official reference numbers ready is strongly recommended."
        )
        md.append(f"{para3}\n")
        
        # Paragraph 4: Practical Tip & Execution Strategy
        tip_text = tip if tip.startswith("Keep") or tip.startswith("Ensure") or tip.startswith("Apply") or tip.startswith("Book") or tip.startswith("Select") or tip.startswith("Check") or tip.startswith("Use") else f"For optimal results, {tip[0].lower() + tip[1:]}"
        para4 = (
            f"{tip_text} Experienced practitioners suggest planning ahead, double-checking portal requirements before initiating requests, "
            f"and keeping a dedicated record of all transactions to handle any edge cases smoothly."
        )
        md.append(f"{para4}\n")
    
    # Comprehensive Conclusion / Summary Section
    md.append("## Summary & Best Practices\n")
    md.append(
        f"Mastering {title.lower()} demands a proactive approach combining regulatory awareness and practical preparation. "
        f"By following the structured guidance outlined in this guide, you can successfully navigate procedural requirements, "
        f"minimize compliance risks, and achieve reliable, hassle-free outcomes.\n"
    )
    md.append(
        f"Stay updated with official portal announcements, maintain organized digital archives of your documentation, "
        f"and leverage verified channels whenever seeking assistance or submitting formal applications.\n"
    )
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

print(f"SUCCESS! Built all {len(ALL_POSTS)} text-only long-form narrative blog posts in _posts/.")
