---
layout: default
title: Home
nav_order: 1
description: "Indian Travel Logistics & Transit Guides"
permalink: /
---

# Indian Travel Logistics

Welcome to **Indian Travel Logistics**. Below are the comprehensive travel and transit navigation guides for train routes, mountain passes, IRCTC booking strategies, multi-modal journeys, and island ferry networks across India.

## Latest Transit Guides

{% for post in site.posts %}
### [{{ post.title }}]({{ post.url | relative_url }})
*Published on {{ post.date | date: "%B %d, %Y" }}*

{% endfor %}
