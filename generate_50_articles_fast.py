#!/usr/bin/env python3
"""
Fast Parallel Mass Article Generator (50 Top 10 Posts for Jekyll)
===============================================================
Generates 50 fact-checked Top 10 Jekyll posts in parallel threads.
"""

import sys
import os
import time
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
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
    return text.strip('-')[:50]

def generate_single_post(item, idx, total_target, base_date, posts_dir):
    topic = item["topic"]
    category = item["category"]

    # Check exact topic slug match
    topic_slug = slugify(topic)
    existing = [f for f in os.listdir(posts_dir) if topic_slug in f]
    if existing:
        print(f"  ⏭️ [{idx}/{total_target}] Already exists: {existing[0]}")
        return True

    post_date = base_date + timedelta(days=int((idx / total_target) * 90))
    date_str = post_date.strftime("%Y-%m-%d")

    llm_client = LLMClient(
        api_url=CONFIG["llm_api_url"],
        api_key=CONFIG["llm_api_key"],
        model=CONFIG["llm_model"]
    )
    generator_engine = Top10GeneratorEngine(llm_client=llm_client)

    print(f"🚀 [{idx}/{total_target}] Generating [{category.upper()}]: '{topic}'...")

    for attempt in range(2):
        try:
            post = generator_engine.generate_top10_blog(
                topic=topic,
                category=category
            )
            post["created_at"] = date_str

            jekyll_markdown = generator_engine.format_as_jekyll_markdown(post)

            filename = f"{date_str}-{topic_slug}.md"
            filepath = os.path.join(posts_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(jekyll_markdown)

            print(f"  ✅ [{idx}/{total_target}] Saved: _posts/{filename}")
            return True
        except Exception as e:
            print(f"  ⚠️ Attempt {attempt+1} failed for '{topic}': {e}")
            time.sleep(2)

    print(f"  ❌ Failed after retries: '{topic}'")
    return False

def main():
    print("=" * 75)
    print("🔥 PARALLEL FAST PIPELINE: GENERATING 50 TOP 10 JEKYLL POSTS")
    print("=" * 75)

    trend_fetcher = TrendFetcher()
    all_trends = trend_fetcher.get_trends("all")
    total_target = min(50, len(all_trends))
    selected_trends = all_trends[:total_target]

    posts_dir = os.path.join(os.path.dirname(__file__), "_posts")
    os.makedirs(posts_dir, exist_ok=True)
    base_date = datetime.now() - timedelta(days=90)

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [
            executor.submit(generate_single_post, item, idx, total_target, base_date, posts_dir)
            for idx, item in enumerate(selected_trends, 1)
        ]
        
        success_count = 0
        for f in as_completed(futures):
            if f.result():
                success_count += 1

    print("\n" + "=" * 75)
    print(f"🎉 PARALLEL GENERATION COMPLETE: {success_count}/{total_target} Top 10 Posts Ready!")
    print("=" * 75)

if __name__ == "__main__":
    main()
