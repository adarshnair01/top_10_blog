#!/usr/bin/env python3
"""
Top 10 AI Story Generator for Jekyll Blog
========================================
Fact-checked, storytelling Jekyll blog post generator.
Automatically writes ready-to-publish Jekyll posts to _posts/
"""

import sys
import os
import argparse
import json
import re
from datetime import datetime

SERVER_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "python_server")
if SERVER_DIR not in sys.path:
    sys.path.insert(0, SERVER_DIR)

from config import CONFIG
from llm_client import LLMClient
from trend_fetcher import TrendFetcher
from fact_checker import FactChecker
from top10_generator import Top10GeneratorEngine

def print_banner():
    print("=" * 70)
    print("🔥  TOP 10 AI JEKYLL BLOG GENERATOR")
    print("    Fact-Checked • Immersive Storytelling • Lightweight Jekyll Posts")
    print("=" * 70)

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')[:50]

def main():
    print_banner()

    parser = argparse.ArgumentParser(description="Generate fact-checked Jekyll Top 10 blog posts.")
    parser.add_argument("--topic", type=str, help="Custom topic or trend to generate Top 10 post for.")
    parser.add_argument("--category", type=str, default="places", help="Category: places, tech, gadgets, mysteries, nature, pop_culture.")
    parser.add_argument("--tone", type=str, default="Cinematic & Immersive", help="Tone: Cinematic & Immersive, Mind-Blowing, Journalistic, Sci-Fi, Humorous.")
    parser.add_argument("--audience", type=str, default="Curiosity Seekers & General Readers", help="Target audience.")
    parser.add_argument("--auto-trend", action="store_true", help="Auto-pick top trending search topic.")
    parser.add_argument("--posts-dir", type=str, default=os.path.join(os.path.dirname(__file__), "_posts"), help="Directory for Jekyll posts.")
    
    args = parser.parse_args()

    trend_fetcher = TrendFetcher()
    llm_client = LLMClient(
        api_url=CONFIG["llm_api_url"],
        api_key=CONFIG["llm_api_key"],
        model=CONFIG["llm_model"]
    )
    generator_engine = Top10GeneratorEngine(llm_client=llm_client)

    topic = args.topic

    if args.auto_trend and not topic:
        trends = trend_fetcher.get_trends(args.category)
        if trends:
            selected = trends[0]
            topic = selected["topic"]
            print(f"🔥 Auto-selected Hot Trend: '{topic}' ({selected['growth_rate']})")

    if not topic:
        print("\nSELECT A TREND CATEGORY OR TYPE A CUSTOM TOPIC:\n")
        categories = trend_fetcher.get_trending_categories()
        for idx, cat in enumerate(categories, 1):
            print(f"  [{idx}] {cat['label']}")
        print("  [C] ✏️ Type Custom Topic")

        choice = input("\nEnter choice [1-7 or C]: ").strip().upper()
        
        if choice == "C" or not choice.isdigit():
            topic = input("\nEnter your custom topic (e.g. 'Surreal Desert Cities'): ").strip()
        else:
            cat_idx = int(choice) - 1
            if 0 <= cat_idx < len(categories):
                selected_cat = categories[cat_idx]["id"]
                trends = trend_fetcher.get_trends(selected_cat)
                print(f"\nTrending topics in '{selected_cat}':\n")
                for t_idx, t in enumerate(trends[:5], 1):
                    print(f"  [{t_idx}] {t['topic']} ({t['growth_rate']})")
                
                t_choice = input("\nPick a trend [1-5] or press Enter to type custom: ").strip()
                if t_choice.isdigit() and 1 <= int(t_choice) <= len(trends[:5]):
                    topic = trends[int(t_choice) - 1]["topic"]
                else:
                    topic = input("\nEnter your topic: ").strip()

    if not topic:
        print("❌ No topic specified. Exiting.")
        sys.exit(1)

    print(f"\n🚀 Generating Jekyll Top 10 Post for topic: '{topic}'...")
    print(f"   • Tone: {args.tone}")
    print(f"   • Category: {args.category}")
    print(f"   • Target Directory: {args.posts_dir}")
    print("-" * 70)

    try:
        post = generator_engine.generate_top10_blog(
            topic=topic,
            tone=args.tone,
            audience=args.audience,
            category=args.category
        )

        jekyll_markdown = generator_engine.format_as_jekyll_markdown(post)

        # Create _posts directory if needed
        os.makedirs(args.posts_dir, exist_ok=True)
        
        today_str = datetime.now().strftime("%Y-%m-%d")
        title_slug = slugify(post['blog'].get('title', topic))
        filename = f"{today_str}-{title_slug}.md"
        filepath = os.path.join(args.posts_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(jekyll_markdown)

        print("\n" + "=" * 70)
        print("🎉 SUCCESS! Jekyll Top 10 Blog Post Generated.")
        print("=" * 70)
        print(f"📄 Title: {post['blog'].get('title')}")
        print(f"📂 Saved Jekyll Post: {filepath}")
        print("-" * 70)
        print("\n📖 BLOG PROLOGUE PREVIEW:\n")
        print(post['blog'].get('introduction', '')[:350] + "...\n")
        print("=" * 70)

    except Exception as e:
        print(f"\n❌ Error generating post: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
