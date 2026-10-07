---
layout: default
title: "Remote Work"
nav_order: 3
description: "Practical guides and reports on Remote Work in India."
---

# 💻 Remote Work

Explore in-depth practical guides, official rules, technical mechanics, and insider tips regarding **Remote Work**.

---

### 📚 Published Guides in this Category

{% assign category_posts = site.posts %}
{% for post in category_posts %}
  {% assign is_match = false %}
  {% for cat in post.categories %}
    {% if cat == 'remote_work' || cat == 'Remote Work' %}
      {% assign is_match = true %}
    {% endif %}
  {% endfor %}
  {% if is_match %}
- **[{ post.title }]({{ post.url | relative_url }})** — *{{ post.date | date: "%B %d, %Y" }}*
  {% endif %}
{% else %}
*No published guides in this category yet. New practical editions published weekly.*
{% endfor %}
