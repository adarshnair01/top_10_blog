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
        tone: str = "Authoritative & Pragmatic",
        audience: str = "Indian Professionals & Everyday Readers",
        category: str = "General"
    ) -> Dict[str, Any]:
        """
        Executes full workflow:
        1. Fact Checking & Web Source Dossier
        2. Clean Text-Only Practical Indian Top 10 Countdown Generation
        """
        print(f"🔍 Step 1: Fact checking topic '{topic}'...")
        dossier = self.fact_checker.verify_topic_facts(topic)
        facts_text = "\n".join(dossier.get("evidence_snippets", []))

        print(f"✍️ Step 2: Generating practical guide via Gemini LLM...")
        
        prompt = f"""
You are an expert Indian investigative analyst, legal/financial advisor, and practical guide chief editor.
Your task is to write an EXTREMELY DETAILED, HIGHLY ACCURATE, and PRACTICAL "TOP 10" GUIDE.

Topic: "{topic}"
Category: "{category}"
Writing Tone: "{tone}" (Clear, authoritative, highly structured, practical, and engaging).
Target Audience: "{audience}"

VERIFIED FACTS DOSSIER FROM REAL-TIME WEB SOURCES:
{facts_text}

CRITICAL REQUIREMENTS:
1. Generate EXACTLY 10 distinct, thoroughly researched countdown items ordered from Rank #10 DOWN TO Rank #1.
2. Every item (#10 to #1) MUST include:
   - Rank (integer 10 to 1)
   - Title: Precise, informative title for the rule, hack, tool, error code, pass, or route.
   - Specs / Core Mechanics: Technical details, relevant section numbers, official portals, speed limits, or regulatory bodies (e.g. RBI, Income Tax Dept, BRO, DGCA, IRCTC).
   - Detailed Explanation / Story: 2 to 3 detailed paragraphs explaining the underlying rules, practical steps, workarounds, real-life consequences, or step-by-step procedures.
   - Official Rule / Fact: An exact verified statistic, section number, official guideline, or rule from Indian authorities.
   - Key Context / Impact: Why this rule or edge case is crucial for professionals and citizens today.
   - Practical Tip: High-value insider tip (e.g., specific portal links, document checklists, helpline numbers, override flags).
3. STRICTLY NO IMAGES OR IMAGE TAGS. Pure text only.
4. DO NOT INCLUDE ANY META-DESCRIPTIVE TEXT OR SELF-PROMOTIONAL FLUFF (e.g. "fact-checked guide", "authoritative countdown"). Write directly for the reader.
5. The guide MUST include:
   - Catchy, SEO-Optimized Title
   - Category
   - Read Time (e.g. "8 min read")
   - Introduction: Direct, engaging 2-paragraph overview setting the context for this topic in India.
   - Conclusion: Strategic summary with actionable takeaways.
   - Reader Discussion Poll: A thought-provoking question with 4 options.

YOU MUST RETURN STRICT VALID JSON ONLY. DO NOT INCLUDE ANY MARKDOWN WRAPPERS OR TEXT OUTSIDE THE JSON OBJECT.

Strictly follow this JSON structure:
{{
  "title": "...",
  "category": "{category}",
  "read_time": "8 min read",
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
            system_prompt="You return raw valid JSON only for practical Indian Top 10 guides.",
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
        """Converts structured Top 10 post to clean Markdown for Just the Docs theme."""
        blog = post.get("blog", {})
        title = blog.get("title", "Top 10 Practical Guides")
        intro = blog.get("introduction", "")
        conclusion = blog.get("conclusion", "")
        items = blog.get("items", [])
        poll = blog.get("reader_poll", {})
        category = blog.get("category", "General")
        date_str = post.get("created_at", datetime.now().strftime("%Y-%m-%d"))
        
        md_lines = [
            "---",
            "layout: default",
            "nav_exclude: true",
            f'title: "{title}"',
            f'date: {date_str}',
            f'categories: [{category}]',
            'author: "Adarsh Nair"',
            "---",
            "",
            f"{intro}",
            "",
            "---",
            ""
        ]

        for item in items:
            rank = item.get("rank")
            item_title = item.get("title", "")
            specs = item.get("location_or_specs", "")
            story = item.get("narrative_story", "")
            fact = item.get("verified_fact", "")
            trending = item.get("why_trending", "")
            secret = item.get("pro_tip_or_secret", "")

            md_lines.append(f"## {rank}. {item_title}")
            md_lines.append("")
            if specs:
                md_lines.append(f"**Core Specs & Mechanics:** `{specs}`")
                md_lines.append("")
            
            md_lines.append(story)
            md_lines.append("")
            
            if fact:
                md_lines.append(f"> **Official Rule / Fact:** {fact}")
            if trending:
                md_lines.append(f"> **Key Context:** {trending}")
            if secret:
                md_lines.append(f"> **Practical Tip:** {secret}")
            
            md_lines.append("")
            md_lines.append("---")
            md_lines.append("")

        md_lines.append("## Summary")
        md_lines.append("")
        md_lines.append(conclusion)
        md_lines.append("")

        if poll and poll.get("question"):
            md_lines.append("### Interactive Reader Discussion")
            md_lines.append("")
            md_lines.append(f"**{poll.get('question')}**")
            md_lines.append("")
            for opt in poll.get("options", []):
                md_lines.append(f"- {opt}")
            md_lines.append("")

        return "\n".join(md_lines)
