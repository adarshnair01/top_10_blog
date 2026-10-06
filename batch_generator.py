#!/usr/bin/env python3
"""
Batch Top 10 Jekyll Post Generator
====================================
Generates multiple Top 10 Jekyll posts automatically into _posts/
"""

import sys
import os
import time
import argparse
import re
from datetime import datetime

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

def main():
    parser = argparse.ArgumentParser(description="Batch generate Jekyll Top 10 posts.")
    parser.add_argument("--count", type=int, default=3, help="Number of posts to generate.")
    parser.add_argument("--category", type=str, default="all", help="Category filter or 'all'")
    parser.add_argument("--posts-dir", type=str, default=os.path.join(os.path.dirname(__file__), "_posts"))
    args = parser.parse_args()

    print("=" * 70)
    print(f"🔥 BATCH GENERATING {args.count} FACT-CHECKED JEKYLL TOP 10 POSTS")
    print("=" * 70)

    trend_fetcher = TrendFetcher()
    llm_client = LLMClient(
        api_url=CONFIG["llm_api_url"],
        api_key=CONFIG["llm_api_key"],
        model=CONFIG["llm_model"]
    )
    generator_engine = Top10GeneratorEngine(llm_client=llm_client)

    trends = trend_fetcher.get_trends(args.category)
    selected_trends = trends[:args.count]

    os.makedirs(args.posts_dir, exist_ok=True)
    today_str = datetime.now().strftime("%Y-%m-%d")

    for i, item in enumerate(selected_trends, 1):
        topic = item["topic"]
        category = item["category"]
        print(f"\n[{i}/{len(selected_trends)}] Generating Jekyll Top 10 for: '{topic}' ({category})...")

        try:
            post = generator_engine.generate_top10_blog(
                topic=topic,
                category=category
            )
            jekyll_markdown = generator_engine.format_as_jekyll_markdown(post)

            title_slug = slugify(post['blog'].get('title', topic))
            filename = f"{today_str}-{title_slug}.md"
            filepath = os.path.join(args.posts_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(jekyll_markdown)

            print(f"  ✓ Saved to Jekyll _posts: {filepath}")
            time.sleep(2)
        except Exception as e:
            print(f"  ❌ Failed for '{topic}': {e}")

    print("\n" + "=" * 70)
    print("✨ BATCH JEKYLL POST GENERATION COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
