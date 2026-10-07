#!/usr/bin/env python3
"""
Update topic pages to have clean, minimal titles with subtle emojis and ordered navigation for the sidebar.
"""

import os

topics_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "topics")

TOPICS = [
    ("travel-logistics.md", "🚂 Travel Logistics", 2, "travel_logistics", "Logistics", "Travel"),
    ("remote-work.md", "💻 Remote Work", 3, "remote_work", "Remote Work"),
    ("ai-professions.md", "🤖 AI for Professions", 4, "ai_professions", "AI"),
    ("can-i-queries.md", "❓ \"Can I...?\" Queries", 5, "can_i_queries", "Can I"),
    ("what-happens-if.md", "🔮 \"What Happens If...?\"", 6, "what_happens_if", "What Happens"),
    ("bureaucracy.md", "🏛️ Bureaucracy", 7, "bureaucracy", "Bureaucracy"),
    ("banking.md", "🏦 Banking Problems", 8, "banking_problems", "Banking"),
    ("credit-cards.md", "💳 Credit Cards", 9, "credit_cards", "Credit Cards"),
    ("tax-edge-cases.md", "📊 Tax Edge Cases", 10, "tax_edge_cases", "Tax"),
    ("error-dictionary.md", "⚠️ Error Dictionary", 11, "error_dictionary", "Error Dictionary"),
    ("remote-work-logistics.md", "🔌 Remote Work Logistics", 12, "remote_work_logistics"),
    ("moving-to-india.md", "✈️ \"Moving to...\" India", 13, "moving_to_india"),
    ("can-i-carry.md", "🧳 \"Can I Carry This?\"", 14, "can_i_carry")
]

for filename, title, order, *cat_matches in TOPICS:
    filepath = os.path.join(topics_dir, filename)
    
    # Build Liquid match conditions
    conds = " or ".join([f"cat == '{c}'" for c in cat_matches])
    
    content = f"""---
layout: default
title: "{title}"
nav_order: {order}
description: "Practical guides and reports on {title} in India."
---

# {title}

Explore in-depth practical guides, official rules, technical mechanics, and insider tips regarding **{title}**.

---

### 📚 Published Guides in this Category

{{% assign category_posts = site.posts %}}
{{% for post in category_posts %}}
  {{% assign is_match = false %}}
  {{% for cat in post.categories %}}
    {{% if {conds} %}}
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
        f.write(content)

print(f"Updated {len(TOPICS)} topic pages for minimal sidebar navigation.")
