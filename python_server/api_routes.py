from fastapi import APIRouter, HTTPException, BackgroundTask
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import os
import json
from config import CONFIG
from llm_client import LLMClient
from trend_fetcher import TrendFetcher
from fact_checker import FactChecker
from top10_generator import Top10GeneratorEngine

router = APIRouter(prefix="/api")

# Initialize core services
trend_fetcher = TrendFetcher()
fact_checker = FactChecker()
llm_client = LLMClient(
    api_url=CONFIG["llm_api_url"],
    api_key=CONFIG["llm_api_key"],
    model=CONFIG["llm_model"]
)
generator_engine = Top10GeneratorEngine(llm_client=llm_client)

class GenerateRequest(BaseModel):
    topic: str
    tone: Optional[str] = "Cinematic & Immersive"
    audience: Optional[str] = "Curiosity Seekers & General Readers"
    category: Optional[str] = "places"

class FactCheckRequest(BaseModel):
    topic: str

@router.get("/categories")
def get_categories():
    return trend_fetcher.get_trending_categories()

@router.get("/trends")
def get_trends(category: str = "all", search: str = ""):
    if search:
        return trend_fetcher.fetch_live_web_buzz(search)
    return trend_fetcher.get_trends(category)

@router.post("/fact-check")
def do_fact_check(req: FactCheckRequest):
    try:
        dossier = fact_checker.verify_topic_facts(req.topic)
        return dossier
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate")
def generate_post(req: GenerateRequest):
    try:
        post = generator_engine.generate_top10_blog(
            topic=req.topic,
            tone=req.tone,
            audience=req.audience,
            category=req.category
        )
        
        # Save to drafts directory
        post_id = post["id"]
        filepath = os.path.join(CONFIG["drafts_dir"], f"{post_id}.json")
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(post, f, indent=2)

        return post
    except Exception as e:
        print(f"Generation error: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to generate top 10 post: {str(e)}")

@router.get("/posts")
def list_posts():
    posts = []
    drafts_dir = CONFIG["drafts_dir"]
    if os.path.exists(drafts_dir):
        for filename in os.listdir(drafts_dir):
            if filename.endswith(".json"):
                try:
                    with open(os.path.join(drafts_dir, filename), "r", encoding="utf-8") as f:
                        data = json.load(f)
                        posts.append({
                            "id": data.get("id"),
                            "topic": data.get("topic"),
                            "created_at": data.get("created_at"),
                            "title": data.get("blog", {}).get("title"),
                            "read_time": data.get("blog", {}).get("read_time"),
                            "category": data.get("blog", {}).get("category")
                        })
                except Exception:
                    pass
    return sorted(posts, key=lambda x: x.get("id"), reverse=True)

@router.get("/posts/{post_id}")
def get_post(post_id: str):
    filepath = os.path.join(CONFIG["drafts_dir"], f"{post_id}.json")
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Post not found.")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

@router.get("/posts/{post_id}/export/markdown")
def export_markdown(post_id: str):
    filepath = os.path.join(CONFIG["drafts_dir"], f"{post_id}.json")
    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Post not found.")
    with open(filepath, "r", encoding="utf-8") as f:
        post = json.load(f)
    
    md_content = generator_engine.format_as_markdown(post)
    return {"markdown": md_content, "filename": f"{post_id}_top10.md"}
