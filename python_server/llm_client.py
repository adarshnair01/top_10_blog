import json
import random
import time
import urllib.request
import urllib.parse
from typing import Dict, Any, Optional

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

class LLMClient:
    def __init__(self, api_url: str, api_key: str, model: str):
        self.api_url = api_url
        self.api_key = api_key
        self.model = model

    def call_llm(self, prompt: str, system_prompt: Optional[str] = None, max_tokens: int = 8192, max_retries: int = 4) -> str:
        """Calls Gemini / LLM endpoint with retry logic, backoff, and fallback models."""
        is_gemini = "generativelanguage" in self.api_url or "key=" in self.api_url or self.api_key.startswith("AIza")
        
        fallback_models = [
            "gemini-2.5-flash",
            "gemini-3.5-flash-lite",
            "gemini-1.5-flash"
        ]

        current_url = self.api_url
        current_model = self.model

        default_sys = system_prompt or (
            "You are a master storyteller, investigative journalist, and viral content strategist. "
            "Your writing is captivating, deeply immersive, creative, and rigorously fact-checked."
        )

        for attempt in range(max_retries):
            try:
                if is_gemini:
                    if "generativelanguage.googleapis.com" in current_url:
                        url_with_key = f"https://generativelanguage.googleapis.com/v1beta/models/{current_model}:generateContent?key={self.api_key}"
                    else:
                        url_with_key = f"{current_url}?key={self.api_key}" if "?" not in current_url else f"{current_url}&key={self.api_key}"

                    payload = {
                        "contents": [
                            {
                                "parts": [
                                    {"text": f"System: {default_sys}\n\nUser instructions:\n{prompt}"}
                                ]
                            }
                        ],
                        "generationConfig": {
                            "temperature": 0.85,
                            "maxOutputTokens": max_tokens
                        }
                    }
                else:
                    url_with_key = current_url
                    payload = {
                        "model": current_model,
                        "messages": [
                            {"role": "system", "content": default_sys},
                            {"role": "user", "content": prompt}
                        ],
                        "max_tokens": max_tokens,
                        "temperature": 0.85
                    }

                # Execution via requests or urllib
                if HAS_REQUESTS:
                    headers = {"Content-Type": "application/json"}
                    if not is_gemini:
                        headers["Authorization"] = f"Bearer {self.api_key}"
                    
                    response = requests.post(url_with_key, headers=headers, json=payload, timeout=120)
                    if response.status_code == 429:
                        print(f"⚠️ Rate limit 429 on model {current_model}. Failover to fallback...")
                        if fallback_models:
                            current_model = fallback_models.pop(0)
                            time.sleep(2.0)
                            continue
                        time.sleep(10.0)
                        continue

                    response.raise_for_status()
                    data = response.json()
                else:
                    req_data = json.dumps(payload).encode("utf-8")
                    req = urllib.request.Request(
                        url_with_key,
                        data=req_data,
                        headers={"Content-Type": "application/json"}
                    )
                    if not is_gemini:
                        req.add_header("Authorization", f"Bearer {self.api_key}")
                    
                    with urllib.request.urlopen(req, timeout=120) as resp:
                        resp_text = resp.read().decode("utf-8")
                        data = json.loads(resp_text)

                if is_gemini:
                    candidates = data.get("candidates", [])
                    if candidates and "content" in candidates[0]:
                        parts = candidates[0]["content"].get("parts", [])
                        if parts and "text" in parts[0]:
                            return self._clean_markdown(parts[0]["text"])
                    raise ValueError(f"Gemini API returned candidate without text parts.")
                else:
                    choices = data.get("choices", [])
                    if choices and "message" in choices[0]:
                        return self._clean_markdown(choices[0]["message"].get("content", ""))
                    raise ValueError(f"Invalid API response format.")

            except Exception as e:
                print(f"⚠️ Error calling LLM (attempt {attempt+1}/{max_retries}): {e}")
                if attempt < max_retries - 1:
                    time.sleep(3.0 * (attempt + 1))
                else:
                    raise

        raise RuntimeError("Failed to generate content from LLM API after retries.")

    def _clean_markdown(self, content: str) -> str:
        content = content.strip()
        if content.startswith("```json"):
            content = content[len("```json"):].strip()
        if content.startswith("```markdown"):
            content = content[len("```markdown"):].strip()
        if content.startswith("```"):
            content = content[3:].strip()
        if content.endswith("```"):
            content = content[:-3].strip()
        return content
