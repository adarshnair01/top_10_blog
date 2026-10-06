import json
import uuid
import os
import re
from datetime import datetime
from typing import Dict, Any, List
from llm_client import LLMClient
from fact_checker import FactChecker

class Top10GeneratorEngine:
    def __init__(self, llm_client: LLMClient):
        self.llm_client = llm_client
        self.fact_checker = FactChecker()

    def generate_top10_blog(
        self,
        topic: str,
        tone: str = "Cinematic & Immersive",
        audience: str = "Curiosity Seekers & General Readers",
        category: str = "places"
    ) -> Dict[str, Any]:
        """
        Executes full workflow:
        1. Fact Checking & Web Source Dossier
        2. Clean Text-Only Storytelling Top 10 Countdown Generation (No images)
        """
        print(f"🔍 Step 1: Fact checking topic '{topic}'...")
        dossier = self.fact_checker.verify_topic_facts(topic)
        facts_text = "\n".join(dossier.get("evidence_snippets", []))

        print(f"✍️ Step 2: Generating text-only storytelling blog via Gemini LLM...")
        
        prompt = f"""
You are an award-winning investigative storyteller and viral magazine chief editor.
Your task is to generate an EXTREMELY HIGH QUALITY, CREATIVE, and FACT-CHECKED "TOP 10" COUNTDOWN BLOG POST.

Topic: "{topic}"
Writing Tone: "{tone}" (Use vivid sensory details, emotional hooks, cinematic prose, and suspense).
Target Audience: "{audience}"

VERIFIED FACTS DOSSIER FROM REAL-TIME WEB SOURCES:
{facts_text}

CRITICAL REQUIREMENTS:
1. Generate EXACTLY 10 distinct, thoroughly fact-checked countdown items ordered from Rank #10 DOWN TO Rank #1.
2. Every item (#10 to #1) MUST include:
   - Rank (integer 10 to 1)
   - Title: Thrilling, descriptive name of the place/thing/breakthrough.
   - Location or Technical Specs: Exact geographic location, specs, or dimensions.
   - Narrative Story: 2 to 3 paragraphs of deep, engaging, creative storytelling. Write with atmosphere, narrative mystery, human interest, and vivid imagery.
   - Verified Fact: An exact verified statistic, date, metric, or scientific observation from real records.
   - Why Trending: The exact surge reason why people are searching/talking about this right now.
   - Pro Tip or Mind-Blowing Secret: A fascinating insider tip or secret trivia.
3. DO NOT INCLUDE ANY IMAGE PROMPTS OR IMAGE URLS.
4. The blog MUST include:
   - Viral Title (clickable, dramatic, SEO optimized)
   - Catchy Subtitle
   - Category
   - Read Time (e.g. "9 min read")
   - Introduction: Atmospheric 2-paragraph hook setting the stage.
   - Conclusion: Inspiring reflection summarizing what this tells us about our world/future.
   - Reader Poll: A thought-provoking question with 4 distinct options.

YOU MUST RETURN STRICT VALID JSON ONLY. DO NOT INCLUDE ANY MARKDOWN WRAPPERS OR TEXT OUTSIDE THE JSON OBJECT.

Stricly follow this JSON structure:
{{
  "title": "...",
  "subtitle": "...",
  "category": "{category}",
  "read_time": "9 min read",
  "introduction": "...",
  "items": [
    {{
      "rank": 10,
      "title": "...",
      "location_or_specs": "...",
      "narrative_story": "...",
      "verified_fact": "...",
      "why_trending": "...",
      "pro_tip_or_secret": "..."
    }},
    ... (continue through rank 1)
  ],
  "conclusion": "...",
  "reader_poll": {{
    "question": "...",
    "options": ["Option A", "Option B", "Option C", "Option D"]
  }}
}}
"""

        raw_output = self.llm_client.call_llm(
            prompt=prompt,
            system_prompt="You return raw valid JSON only for viral Top 10 story posts.",
            max_tokens=8192
        )

        try:
            blog_data = json.loads(raw_output)
        except Exception:
            cleaned = raw_output.replace("```json", "").replace("```", "").strip()
            blog_data = json.loads(cleaned)

        post_id = str(uuid.uuid4())[:8]
        current_time = datetime.now().strftime("%Y-%m-%d")

        return {
            "id": post_id,
            "created_at": current_time,
            "topic": topic,
            "tone": tone,
            "audience": audience,
            "fact_dossier": dossier,
            "blog": blog_data
        }

    def format_as_jekyll_markdown(self, post: Dict[str, Any]) -> str:
        """Converts structured Top 10 post to clean, text-only Light Theme Markdown."""
        blog = post.get("blog", {})
        title = blog.get("title", "Top 10 Trends")
        subtitle = blog.get("subtitle", "")
        intro = blog.get("introduction", "")
        conclusion = blog.get("conclusion", "")
        items = blog.get("items", [])
        poll = blog.get("reader_poll", {})
        category = blog.get("category", "trends")
        date_str = post.get("created_at", datetime.now().strftime("%Y-%m-%d"))
        
        md_lines = [
            "---",
            "layout: post",
            f'title: "{title}"',
            f'subtitle: "{subtitle}"',
            f'date: {date_str}',
            f'category: "{category}"',
            f'read_time: "{blog.get("read_time", "8 min read")}"',
            'author: "Top 10 AI Story Engine"',
            "---",
            "",
            '<div class="glass-card" style="border-left: 4px solid #2563eb; background: #ffffff;">',
            '  <h4 style="font-size: 0.8rem; font-weight: 700; text-transform: uppercase; color: #2563eb; margin-bottom: 8px; letter-spacing: 0.05em;">EDITORIAL PROLOGUE</h4>',
            f'  <p style="font-family: var(--font-serif); font-size: 1.15rem; line-height: 1.7; color: #334155;">{intro}</p>',
            '</div>',
            "",
            "---",
            ""
        ]

        # Countdown items from 10 down to 1 (No images)
        for item in items:
            rank = item.get("rank")
            item_title = item.get("title", "")
            specs = item.get("location_or_specs", "")
            story = item.get("narrative_story", "")
            fact = item.get("verified_fact", "")
            trending = item.get("why_trending", "")
            secret = item.get("pro_tip_or_secret", "")
            is_top1 = rank == 1
            
            card_class = "glass-card glass-card-top1" if is_top1 else "glass-card"
            badge_class = "rank-badge rank-badge-gold" if is_top1 else "rank-badge"

            md_lines.append(f'<div class="{card_class}">')
            md_lines.append('  <div style="display: flex; align-items: flex-start; gap: 16px; margin-bottom: 16px;">')
            md_lines.append(f'    <div class="{badge_class}">#{rank}</div>')
            md_lines.append('    <div>')
            if specs:
                md_lines.append(f'      <span style="font-size: 0.78rem; font-weight: 700; background: #f1f5f9; padding: 4px 10px; border-radius: 6px; color: #0284c7; display: inline-block; margin-bottom: 6px;">📍 {specs}</span>')
            md_lines.append(f'      <h3 style="font-family: var(--font-serif); font-size: 1.5rem; font-weight: 700; color: #0f172a; line-height: 1.3;">{item_title}</h3>')
            md_lines.append('    </div>')
            md_lines.append('  </div>')
            
            md_lines.append(f'  <div style="font-size: 1.05rem; line-height: 1.75; color: #334155; margin-bottom: 20px;">{story}</div>')
            
            # Fact Grid Callout
            md_lines.append('  <div class="fact-grid">')
            md_lines.append('    <div class="fact-box fact-box-verified">')
            md_lines.append('      <div class="fact-title" style="color: #166534;">🛡️ Verified Fact Check</div>')
            md_lines.append(f'      <div>{fact}</div>')
            md_lines.append('    </div>')
            
            md_lines.append('    <div class="fact-box fact-box-trending">')
            md_lines.append('      <div class="fact-title" style="color: #9f1239;">🔥 Why People Are Talking</div>')
            md_lines.append(f'      <div>{trending}</div>')
            md_lines.append('    </div>')
            
            if secret:
                md_lines.append('    <div class="fact-box fact-box-secret">')
                md_lines.append('      <div class="fact-title" style="color: #92400e;">💡 Insider Secret / Pro Tip</div>')
                md_lines.append(f'      <div>{secret}</div>')
                md_lines.append('    </div>')
            md_lines.append('  </div>')

            md_lines.append('</div>')
            md_lines.append("")

        md_lines.append('<div class="glass-card" style="border-left: 4px solid #0f172a;">')
        md_lines.append('  <h2 style="font-family: var(--font-serif); font-size: 1.4rem; font-weight: 700; color: #0f172a; margin-bottom: 10px;">Conclusion & Editorial Summary</h2>')
        md_lines.append(f'  <p style="font-size: 1.05rem; line-height: 1.75; color: #334155;">{conclusion}</p>')
        md_lines.append('</div>')
        md_lines.append("")

        if poll and poll.get("question"):
            md_lines.append('<div class="glass-card" style="background: #f8fafc; border: 1px solid #cbd5e1;">')
            md_lines.append(f'  <h3 style="font-family: var(--font-serif); font-size: 1.2rem; font-weight: 700; color: #0f172a; margin-bottom: 8px;">🗣️ Reader Interactive Poll</h3>')
            md_lines.append(f'  <p style="font-size: 0.95rem; color: #475569; margin-bottom: 14px;">{poll.get("question")}</p>')
            md_lines.append('  <ul style="list-style: none; display: flex; flex-direction: column; gap: 8px;">')
            for opt in poll.get("options", []):
                md_lines.append(f'    <li style="padding: 12px 16px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; font-size: 0.92rem; color: #0f172a; font-weight: 600;">{opt}</li>')
            md_lines.append('  </ul>')
            md_lines.append('</div>')

        return "\n".join(md_lines)
