---
layout: default
title: "Tax Edge Cases"
nav_order: 10
description: "Practical guides and reports on Tax Edge Cases in India."
---

# 📊 Tax Edge Cases

Explore in-depth practical guides, official rules, technical mechanics, and insider tips regarding **Tax Edge Cases**.

---

### 📚 Published Guides in this Category

{% assign category_posts = site.posts %}
{% for post in category_posts %}
  {% assign is_match = false %}
  {% for cat in post.categories %}
    {% if cat == 'tax_edge_cases' || cat == 'Tax' %}
      {% assign is_match = true %}
    {% endif %}
  {% endfor %}
  {% if is_match %}
- **[{ post.title }]({{ post.url | relative_url }})** — *{{ post.date | date: "%B %d, %Y" }}*
  {% endif %}
{% else %}
*No published guides in this category yet. New practical editions published weekly.*
{% endfor %}
