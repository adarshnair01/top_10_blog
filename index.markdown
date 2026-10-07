---
layout: default
title: Home
nav_order: 1
description: "Practical Top 10 Guides for Indian Logistics, Bureaucracy, Banking, Tax Edge Cases & Remote Work"
permalink: /
---

<style>
  :root {
    --playbook-primary: #1e40af;
    --playbook-accent: #2563eb;
    --playbook-bg-subtle: #f8fafc;
    --playbook-border: #e2e8f0;
  }

  .playbook-hero {
    position: relative;
    background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #1e3a8a 100%);
    border-radius: 16px;
    padding: 36px 32px;
    color: #ffffff;
    overflow: hidden;
    box-shadow: 0 20px 30px -10px rgba(30, 58, 138, 0.25);
    margin-bottom: 40px;
  }

  .playbook-hero::before {
    content: "";
    position: absolute;
    top: -50%;
    right: -20%;
    width: 350px;
    height: 350px;
    background: radial-gradient(circle, rgba(59, 130, 246, 0.35) 0%, rgba(0, 0, 0, 0) 70%);
    border-radius: 50%;
    pointer-events: none;
  }

  .playbook-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    background: rgba(255, 255, 255, 0.12);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: #93c5fd;
    padding: 5px 12px;
    border-radius: 20px;
    margin-bottom: 16px;
  }

  .playbook-hero-title {
    font-size: 2rem;
    font-weight: 800;
    line-height: 1.25;
    margin: 0 0 14px 0;
  }

  .playbook-hero-title a {
    color: #ffffff !important;
    text-decoration: none;
    transition: color 0.2s ease;
  }

  .playbook-hero-title a:hover {
    color: #93c5fd !important;
  }

  .playbook-hero-desc {
    font-size: 1.05rem;
    line-height: 1.6;
    color: #cbd5e1;
    max-width: 680px;
    margin-bottom: 24px;
  }

  .playbook-hero-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #2563eb;
    color: #ffffff !important;
    font-weight: 700;
    font-size: 0.95rem;
    padding: 12px 24px;
    border-radius: 8px;
    text-decoration: none;
    box-shadow: 0 4px 14px rgba(37, 99, 235, 0.4);
    transition: all 0.2s ease;
  }

  .playbook-hero-btn:hover {
    background: #1d4ed8;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.5);
  }

  .topics-ribbon-title {
    font-size: 0.8rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #64748b;
    margin-bottom: 14px;
  }

  .topics-ribbon {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 40px;
  }

  .topic-card-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    padding: 10px 18px;
    border-radius: 10px;
    color: #1e293b !important;
    font-weight: 600;
    font-size: 0.9rem;
    text-decoration: none;
    transition: all 0.2s ease;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
  }

  .topic-card-link:hover {
    border-color: #2563eb;
    color: #2563eb !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.12);
  }

  .section-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 24px;
    padding-bottom: 10px;
    border-bottom: 2px solid #e2e8f0;
  }

  .section-title {
    font-size: 1.35rem;
    font-weight: 800;
    color: #0f172a;
    margin: 0;
  }

  .magazine-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;
    margin-bottom: 40px;
  }

  .mag-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: all 0.25s ease;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
  }

  .mag-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 24px -4px rgba(0, 0, 0, 0.08);
    border-color: #cbd5e1;
  }

  .mag-card-body {
    padding: 24px;
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    justify-content: space-between;
  }

  .mag-card-cat-inline {
    display: inline-block;
    font-size: 0.72rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: #2563eb;
    background: #eff6ff;
    padding: 4px 10px;
    border-radius: 4px;
    margin-bottom: 14px;
  }

  .mag-card-title {
    font-size: 1.15rem;
    font-weight: 700;
    line-height: 1.45;
    color: #0f172a;
    margin: 0 0 16px 0;
  }

  .mag-card-title a {
    color: #0f172a !important;
    text-decoration: none;
  }

  .mag-card-title a:hover {
    color: #2563eb !important;
  }

  .mag-card-footer {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 16px;
    padding-top: 14px;
    border-top: 1px solid #f1f5f9;
    font-size: 0.85rem;
    font-weight: 600;
    color: #2563eb;
  }
</style>

{% assign lead_post = site.posts.first %}

{% if lead_post %}
<div class="playbook-hero">
  <div class="playbook-badge">
    <span>🔥</span> FEATURED EDITION
  </div>
  <h1 class="playbook-hero-title">
    <a href="{{ lead_post.url | relative_url }}">{{ lead_post.title }}</a>
  </h1>
  <p class="playbook-hero-desc">
    An in-depth practical guide breaking down exact mechanics, technical specifications, official regulatory rules, and insider tips.
  </p>
  <a href="{{ lead_post.url | relative_url }}" class="playbook-hero-btn">
    Read Full Playbook <span>&rarr;</span>
  </a>
</div>
{% endif %}

<div class="topics-ribbon-title">Explore Topic Playbooks</div>
<div class="topics-ribbon">
  <a href="{{ '/topics/travel-logistics/' | relative_url }}" class="topic-card-link">
    <span>🚂</span> Travel Logistics
  </a>
  <a href="{{ '/topics/bureaucracy/' | relative_url }}" class="topic-card-link">
    <span>🏛️</span> Bureaucracy
  </a>
  <a href="{{ '/topics/banking/' | relative_url }}" class="topic-card-link">
    <span>🏦</span> Banking & UPI
  </a>
  <a href="{{ '/topics/credit-cards/' | relative_url }}" class="topic-card-link">
    <span>💳</span> Credit Cards
  </a>
  <a href="{{ '/topics/tax-edge-cases/' | relative_url }}" class="topic-card-link">
    <span>📊</span> Tax Edge Cases
  </a>
  <a href="{{ '/topics/remote-work/' | relative_url }}" class="topic-card-link">
    <span>💻</span> Remote Work
  </a>
</div>

<div class="section-header">
  <h2 class="section-title">Latest Playbook Editions</h2>
</div>

<div class="magazine-grid">
  {% for post in site.posts offset:1 %}
  <div class="mag-card">
    <div class="mag-card-body">
      <div>
        <span class="mag-card-cat-inline">{{ post.categories | first | default: "Guide" | replace: "_", " " }}</span>
        <h3 class="mag-card-title">
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        </h3>
      </div>
      <div class="mag-card-footer">
        <span>Read Edition</span>
        <span>&rarr;</span>
      </div>
    </div>
  </div>
  {% endfor %}
</div>
