import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH_LOCAL = os.path.join(BASE_DIR, ".env")
ENV_PATH_POST_GEN = os.path.expanduser("~/Development/post_generator/auto-blogger/.env")

def load_env_file(filepath: str):
    if not os.path.exists(filepath):
        return
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().strip('"').strip("'")
                if key and not os.environ.get(key):
                    os.environ[key] = val
    except Exception as e:
        print(f"Notice: env read info ({e})")

# Load environment
if os.path.exists(ENV_PATH_LOCAL):
    load_env_file(ENV_PATH_LOCAL)
elif os.path.exists(ENV_PATH_POST_GEN):
    load_env_file(ENV_PATH_POST_GEN)

CONFIG = {
    "llm_api_url": os.getenv("LLM_API_URL", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"),
    "llm_api_key": os.getenv("GEMINI_API_KEY", os.getenv("LLM_API_KEY", "")),
    "llm_model": os.getenv("LLM_MODEL", "gemini-2.5-flash"),
    "unsplash_access_key": os.getenv("UNSPLASH_ACCESS_KEY", ""),
    "drafts_dir": os.path.join(BASE_DIR, "drafts"),
    "posts_dir": os.path.join(BASE_DIR, "published_posts")
}

os.makedirs(CONFIG["drafts_dir"], exist_ok=True)
os.makedirs(CONFIG["posts_dir"], exist_ok=True)
