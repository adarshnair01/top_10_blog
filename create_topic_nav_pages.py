#!/usr/bin/env python3
"""
Fixes Liquid syntax in 13 Topic Navigation pages for Just the Docs.
Removes dates as requested.
"""

import os

topics_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "topics")
os.makedirs(topics_dir, exist_ok=True)

topic_pages = [
    {
        "filename": "travel-logistics.md",
        "title": "Travel Logistics",
        "nav_order": 2,
        "icon": "🚂",
        "category_matches": ["Logistics", "travel_logistics", "Travel"]
    },
    {
        "filename": "remote-work.md",
        "title": "Remote Work",
        "nav_order": 3,
        "icon": "💻",
        "category_matches": ["remote_work", "Remote Work"]
    },
    {
        "filename": "ai-professions.md",
        "title": "AI for Professions",
        "nav_order": 4,
        "icon": "🤖",
        "category_matches": ["ai_professions", "AI"]
    },
    {
        "filename": "can-i-queries.md",
        "title": "Indian 'Can I...?'",
        "nav_order": 5,
        "icon": "❓",
        "category_matches": ["can_i_queries", "Can I"]
    },
    {
        "filename": "what-happens-if.md",
        "title": "'What Happens If...?'",
        "nav_order": 6,
        "icon": "⚡",
        "category_matches": ["what_happens_if", "What Happens"]
    },
    {
        "filename": "bureaucracy.md",
        "title": "Bureaucracy Explained",
        "nav_order": 7,
        "icon": "🏛️",
        "category_matches": ["bureaucracy", "Bureaucracy"]
    },
    {
        "filename": "banking.md",
        "title": "Banking Problems",
        "nav_order": 8,
        "icon": "🏦",
        "category_matches": ["banking_problems", "Banking"]
    },
    {
        "filename": "credit-cards.md",
        "title": "Credit Card Optimization",
        "nav_order": 9,
        "icon": "💳",
        "category_matches": ["credit_cards", "Credit Cards"]
    },
    {
        "filename": "tax-edge-cases.md",
        "title": "Tax Edge Cases",
        "nav_order": 10,
        "icon": "📊",
        "category_matches": ["tax_edge_cases", "Tax"]
    },
    {
        "filename": "error-dictionary.md",
        "title": "Error Dictionary",
        "nav_order": 11,
        "icon": "🔍",
        "category_matches": ["error_dictionary", "Error Dictionary"]
    },
    {
        "filename": "remote-work-logistics.md",
        "title": "Remote Work Logistics",
        "nav_order": 12,
        "icon": "🔌",
        "category_matches": ["remote_work_logistics"]
    },
    {
        "filename": "moving-to-india.md",
        "title": "'Moving To...' India",
        "nav_order": 13,
        "icon": "📦",
        "category_matches": ["moving_to_india"]
    },
    {
        "filename": "can-i-carry.md",
        "title": "'Can I Carry This?'",
        "nav_order": 14,
        "icon": "🧳",
        "category_matches": ["can_i_carry"]
    }
]

for topic in topic_pages:
    filepath = os.path.join(topics_dir, topic["filename"])
    
    # Liquid OR condition
    or_condition = " or ".join([f"cat == '{m}'" for m in topic['category_matches']])
    
    content = f"""---
layout: default
title: "{topic['title']}"
nav_order: {topic['nav_order']}
description: "Practical guides and reports on {topic['title']} in India."
---

# {topic['icon']} {topic['title']}

Explore in-depth practical guides, official rules, technical mechanics, and insider tips regarding **{topic['title']}**.

---

### 📚 Published Guides in this Category

{{% assign category_posts = site.posts %}}
{{% for post in category_posts %}}
  {{% assign is_match = false %}}
  {{% for cat in post.categories %}}
    {{% if {or_condition} %}}
      {{% assign is_match = true %}}
    {{% endif %}}
  {{% endfor %}}
  {{% if is_match %}}
- [{{{{ post.title }}}}]({{{{ post.url | relative_url }}}})
  {{% endif %}}
{{% else %}}
*No published guides in this category yet. New practical editions published weekly.*
{{% endfor %}}
"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"✅ Fixed topic page: {topic['filename']}")

print("\n🎉 All 13 topic navigation pages fixed with clean Liquid titles and no dates!")
