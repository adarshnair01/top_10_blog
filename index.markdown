---
layout: default
title: Home
nav_order: 1
description: "Practical Top 10 Guides for Indian Logistics, Bureaucracy, Banking, Tax Edge Cases & Remote Work"
permalink: /
---

<style>
  .magazine-hero {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-left: 5px solid #2563eb;
    border-radius: 8px;
    padding: 28px;
    margin-bottom: 32px;
  }
  .magazine-hero-badge {
    display: inline-block;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #2563eb;
    background: #eff6ff;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 12px;
  }
  .magazine-hero-title {
    font-size: 1.65rem;
    font-weight: 800;
    line-height: 1.3;
    margin: 8px 0 12px 0;
  }
  .magazine-hero-title a {
    color: #0f172a;
    text-decoration: none;
  }
  .magazine-hero-title a:hover {
    color: #2563eb;
  }
  .magazine-hero-date {
    font-size: 0.85rem;
    color: #64748b;
    margin-bottom: 14px;
  }
  .magazine-hero-cta {
    display: inline-block;
    font-weight: 600;
    font-size: 0.9rem;
    color: #2563eb;
    text-decoration: none;
    margin-top: 10px;
  }
  .magazine-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    margin-top: 20px;
  }
  .magazine-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 22px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .magazine-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.05);
    border-color: #cbd5e1;
  }
  .magazine-card-badge {
    font-size: 0.7rem;
    font-weight: 700;
    text-transform: uppercase;
    color: #475569;
    background: #f1f5f9;
    padding: 3px 8px;
    border-radius: 4px;
    width: fit-content;
    margin-bottom: 10px;
  }
  .magazine-card-title {
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.4;
    margin: 0 0 10px 0;
  }
  .magazine-card-title a {
    color: #0f172a;
    text-decoration: none;
  }
  .magazine-card-title a:hover {
    color: #2563eb;
  }
  .magazine-card-date {
    font-size: 0.8rem;
    color: #94a3b8;
  }
</style>

# The Indian Playbook

Practical Top 10 Guides for Indian Logistics, Bureaucracy, Banking, Tax Edge Cases, AI Tools & Remote Work.

---

{% assign hero_post = site.posts.first %}
{% if hero_post %}
<div class="magazine-hero">
  <span class="magazine-hero-badge">🔥 FEATURED PRACTICAL GUIDE</span>
  <h2 class="magazine-hero-title">
    <a href="{{ hero_post.url | relative_url }}">{{ hero_post.title }}</a>
  </h2>
  <div class="magazine-hero-date">
    Published on {{ hero_post.date | date: "%B %d, %Y" }} • By {{ hero_post.author | default: "Adarsh Nair" }}
  </div>
  <a href="{{ hero_post.url | relative_url }}" class="magazine-hero-cta">Read Full Playbook &rarr;</a>
</div>
{% endif %}

### 📚 Latest Editions & Guides

<div class="magazine-grid">
  {% for post in site.posts offset:1 %}
  <div class="magazine-card">
    <div>
      <span class="magazine-card-badge">{{ post.categories | first | default: "Guide" }}</span>
      <h3 class="magazine-card-title">
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      </h3>
    </div>
    <div class="magazine-card-date">
      {{ post.date | date: "%b %d, %Y" }}
    </div>
  </div>
  {% endfor %}
</div>
