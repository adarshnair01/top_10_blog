#!/usr/bin/env python3
"""
Mass Article Generator (50 Top 10 Posts for Jekyll Blog)
======================================================
Generates ~50 fact-checked, high-engagement storytelling Top 10 posts for Jekyll.
"""

import sys
import os
import time
import re
import random
from datetime import datetime, timedelta

SERVER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "python_server")
if SERVER_DIR not in sys.path:
    sys.path.insert(0, SERVER_DIR)

from config import CONFIG
from llm_client import LLMClient
from trend_fetcher import TrendFetcher
from top10_generator import Top10GeneratorEngine

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')[:55]

def main():
    print("=" * 75)
    print("🔥 MASS GENERATION PIPELINE: GENERATING 50 FACT-CHECKED TOP 10 JEKYLL POSTS")
    print("=" * 75)

    trend_fetcher = TrendFetcher()
    llm_client = LLMClient(
        api_url=CONFIG["llm_api_url"],
        api_key=CONFIG["llm_api_key"],
        model=CONFIG["llm_model"]
    )
    generator_engine = Top10GeneratorEngine(llm_client=llm_client)

    all_trends = trend_fetcher.get_trends("all")
    total_target = min(50, len(all_trends))
    selected_trends = all_trends[:total_target]

    posts_dir = os.path.join(os.path.dirname(__file__), "_posts")
    os.makedirs(posts_dir, exist_ok=True)

    base_date = datetime.now() - timedelta(days=90)
    success_count = 0

    for idx, item in enumerate(selected_trends, 1):
        topic = item["topic"]
        category = item["category"]

        # Calculate a realistic publish date spread out over past weeks
        post_date = base_date + timedelta(days=int((idx / total_target) * 90))
        date_str = post_date.strftime("%Y-%m-%d")

        print(f"\n[{idx}/{total_target}] Generating [{category.upper()}]: '{topic}'...")

        try:
            post = generator_engine.generate_top10_blog(
                topic=topic,
                category=category
            )
            
            # Override created_at date with realistic historical timeline date
            post["created_at"] = date_str

            jekyll_markdown = generator_engine.format_as_jekyll_markdown(post)

            title_slug = slugify(post['blog'].get('title', topic))
            filename = f"{date_str}-{title_slug}.md"
            filepath = os.path.join(posts_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(jekyll_markdown)

            success_count += 1
            print(f"  ✅ [{success_count}/{total_target}] Saved: _posts/{filename}")
            
            # Short sleep to prevent Gemini RPM rate limits
            time.sleep(1.5)

        except Exception as e:
            print(f"  ⚠️ Error generating post '{topic}': {e}")
            # Retrying once after pause
            time.sleep(5)
            try:
                post = generator_engine.generate_top10_blog(topic=topic, category=category)
                post["created_at"] = date_str
                jekyll_markdown = generator_engine.format_as_jekyll_markdown(post)
                title_slug = slugify(post['blog'].get('title', topic))
                filename = f"{date_str}-{title_slug}.md"
                filepath = os.path.join(posts_dir, filename)
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(jekyll_markdown)
                success_count += 1
                print(f"  ✅ [RETRY SUCCESS] Saved: _posts/{filename}")
            except Exception as retry_err:
                print(f"  ❌ Retry failed for '{topic}': {retry_err}")

    print("\n" + "=" * 75)
    print(f"🎉 GENERATION COMPLETE: Successfully generated {success_count} Top 10 Jekyll Posts!")
    print("=" * 75)

if __name__ == "__main__":
    main()
