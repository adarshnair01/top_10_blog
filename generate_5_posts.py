#!/usr/bin/env python3
"""
Generate 5 Text-Only Indian Travel Logistics Posts for Jekyll Minima Theme
"""

import sys
import os
import time
from datetime import datetime, timedelta

SERVER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "python_server")
if SERVER_DIR not in sys.path:
    sys.path.insert(0, SERVER_DIR)

from config import CONFIG
from llm_client import LLMClient
from top10_generator import Top10GeneratorEngine
from trend_fetcher import INDIAN_TRAVEL_LOGISTICS_TOPICS, TrendFetcher

def slugify(text: str) -> str:
    import re
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')[:50]

def main():
    print("=" * 70)
    print("🚂 GENERATING 5 INDIAN TRAVEL LOGISTICS POSTS (MINIMA THEME, TEXT ONLY)")
    print("=" * 70)

    llm_client = LLMClient(
        api_url=CONFIG["llm_api_url"],
        api_key=CONFIG["llm_api_key"],
        model=CONFIG["llm_model"]
    )
    generator = Top10GeneratorEngine(llm_client=llm_client)

    posts_dir = os.path.join(os.path.dirname(__file__), "_posts")
    os.makedirs(posts_dir, exist_ok=True)

    # Base date starting today
    base_date = datetime.now()

    for idx, topic in enumerate(INDIAN_TRAVEL_LOGISTICS_TOPICS, 1):
        print(f"\n[{idx}/5] Generating topic: '{topic}'...")
        post_date = (base_date - timedelta(days=(5 - idx))).strftime("%Y-%m-%d")

        try:
            result = generator.generate_top10_blog(
                topic=topic,
                tone="Authoritative & Pragmatic",
                audience="Indian Travelers & Transit Enthusiasts",
                category="Logistics"
            )
            
            # Override created_at for chronological dates in Jekyll
            result["created_at"] = post_date

            md_content = generator.format_as_jekyll_markdown(result)

            title = result.get("blog", {}).get("title", topic)
            filename = f"{post_date}-{slugify(title)}.md"
            filepath = os.path.join(posts_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(md_content)

            print(f"✅ Generated & Saved: {filename}")
            
            # Brief sleep to avoid hitting rate limits
            time.sleep(2)

        except Exception as e:
            print(f"❌ Failed to generate post {idx}: {e}")

    print("\n" + "=" * 70)
    print("🎉 All 5 Indian Travel Logistics posts generated successfully!")
    print("=" * 70)

if __name__ == "__main__":
    main()
