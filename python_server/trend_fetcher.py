import json
import random
from typing import List, Dict

INDIAN_TRAVEL_LOGISTICS_TOPICS = [
    "Top 10 Vande Bharat Express Routes Ranked by Speed, Comfort & Transit Logistics",
    "Top 10 High-Altitude Himalayan Mountain Passes & Seasonal Road Closure Logistics",
    "Top 10 IRCTC Tatkal Hacks & Railway Station Transit Logistics in India",
    "Top 10 Multi-Modal Transit Corridors to Remote Indian Destinations",
    "Top 10 Coastal Ferry & Island Transit Corridors in India"
]

class TrendFetcher:
    def __init__(self):
        pass

    def get_trending_categories(self) -> List[Dict[str, str]]:
        return [
            {"id": "logistics", "label": "🚂 Indian Travel Logistics", "icon": "train"}
        ]

    def get_trends(self, category: str = "logistics") -> List[Dict[str, str]]:
        results = []
        for count, topic in enumerate(INDIAN_TRAVEL_LOGISTICS_TOPICS, 1):
            results.append({
                "id": f"topic_{count}",
                "topic": topic,
                "category": "logistics",
                "search_volume": "High Search Volume",
                "growth_rate": "Trending Transit Guide",
                "badge": "INDIAN LOGISTICS",
                "description": "Fact-checked travel & transit logistics guide."
            })
        return results
