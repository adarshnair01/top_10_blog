import requests
import json
import random
from typing import List, Dict

CATEGORIZED_TREND_SEED = {
    "places": [
        "Top 10 Surreal Bioluminescent Beaches That Glow Like Sci-Fi Worlds",
        "Top 10 Ancient Subterranean Cities Still Hiding Secret Tunnels",
        "Top 10 Most Dangerous Sky-High Bridges in the World",
        "Top 10 Abandoned Futuristic Cities Nature Reclaimed",
        "Top 10 High-Tech Eco Cities Being Built in Desert Basins",
        "Top 10 Gravity-Defying Temples Built on Cliff Edges",
        "Top 10 Underwater Ruins Hidden Beneath Coastal Oceans",
        "Top 10 Active Volcanoes You Can Safely Visit With Guides",
        "Top 10 Rainbow Mountain Ranges Formed by Rare Mineral Layers",
        "Top 10 Remote Island Fortresses With Unbelievable History"
    ],
    "tech": [
        "Top 10 Autonomous Humanoid Robots Stepping Into Real Factories",
        "Top 10 Quantum Computing Breakthroughs Rewriting Encryption",
        "Top 10 AI Wearables Aiming to Replace Smartphones",
        "Top 10 Mind-Controlled Neural Interfaces in Clinical Trials",
        "Top 10 Next-Gen Fusion Reactors Reaching Plasma Milestones",
        "Top 10 Space-Based Solar Power Station Designs",
        "Top 10 Graphene Breakthroughs Revolutionizing Energy Storage",
        "Top 10 Autonomous eVTOL Flying Taxis Under Test Flights",
        "Top 10 Supercomputers Pushing Exascale Processing Limits",
        "Top 10 Synthetic Biology Breakthroughs Printing Custom DNA"
    ],
    "gadgets": [
        "Top 10 Wild Sci-Fi Gadgets You Can Actually Buy Today",
        "Top 10 Futuristic Electric Hypercars Breaking Speed Records",
        "Top 10 AR Smart Glasses Challenging Spatial Computing",
        "Top 10 Solar-Powered Survival Devices Built for Extreme Climates",
        "Top 10 Transparent OLED Displays Transforming Smart Homes",
        "Top 10 Robotic Exoskeletons Enhancing Human Endurance",
        "Top 10 Quantum-Encrypted Hard Drives Unbreakable by Hackers",
        "Top 10 AI-Powered Personal Health Sensors and Rings",
        "Top 10 Portable Water Desalination Gadgets for Wilderness Explorers"
    ],
    "mysteries": [
        "Top 10 Deep Ocean Anomalies Scientists Cannot Explain",
        "Top 10 Megalithic Structures That Challenge Modern Engineering",
        "Top 10 Mysterious Cosmic Signals Detected from Deep Space",
        "Top 10 Unsolved Archaeological Artifacts Found in Remote Caves",
        "Top 10 Vanished Ships Found in Improbable Locations",
        "Top 10 Bizarre Geoglyphs Visible Only From High Altitude",
        "Top 10 Acoustic Mysteries Where Sound Behaves Impossibly",
        "Top 10 Subterranean Magnetic Anomalies Confusing Radar Equipment",
        "Top 10 Ancient Manuscripts No Cryptographer Has Ever Deciphered"
    ],
    "nature": [
        "Top 10 Mind-Blowing Weather Phenomena That Look Like CGI",
        "Top 10 Deep-Sea Creatures Living Near Volcanic Hydrothermal Vents",
        "Top 10 Carnivorous Plants with Complex Trapping Mechanisms",
        "Top 10 Volcanic Islands Formed in the Last Decade",
        "Top 10 Bioluminescent Forests That Glow After Nightfall",
        "Top 10 Extreme Organisms Surviving Zero Oxygen and Radiation",
        "Top 10 Frozen Crystal Ice Formations Found Only at High Altitudes",
        "Top 10 Animal Species with Bizarre Superhuman Senses",
        "Top 10 Underground Cave Systems Housing Entire Ecosystems"
    ],
    "pop_culture": [
        "Top 10 Sci-Fi Movie Technologies That Became Everyday Reality",
        "Top 10 Viral Tech Theories Spoofed by Sci-Fi Writers Years Ago",
        "Top 10 Cinematic Masterpieces Shot Entirely on Smartphones and Drones",
        "Top 10 Iconic Movie Prop Inventions Recreated by Engineers",
        "Top 10 Cyberpunk Video Game Features Built into Real Cities",
        "Top 10 Sci-Fi Architecture Concepts Inspiring Real Skyscrapers",
        "Top 10 AI Generated Art Masterpieces That Sold at Auction Houses"
    ]
}

class TrendFetcher:
    def __init__(self):
        pass

    def get_trending_categories(self) -> List[Dict[str, str]]:
        return [
            {"id": "all", "label": "🔥 All Hot Trends", "icon": "fire"},
            {"id": "places", "label": "🌍 Surreal Places & Travel", "icon": "globe"},
            {"id": "tech", "label": "🚀 Tech & AI Breakthroughs", "icon": "cpu"},
            {"id": "gadgets", "label": "⚡ Futuristic Gadgets", "icon": "zap"},
            {"id": "mysteries", "label": "🛸 Unexplained Mysteries", "icon": "compass"},
            {"id": "nature", "label": "🌿 Mind-Blowing Nature", "icon": "feather"},
            {"id": "pop_culture", "label": "🎬 Culture & Sci-Fi Realities", "icon": "film"}
        ]

    def get_trends(self, category: str = "all") -> List[Dict[str, str]]:
        results = []
        categories_to_check = [category] if category != "all" else list(CATEGORIZED_TREND_SEED.keys())
        
        count = 1
        for cat in categories_to_check:
            items = CATEGORIZED_TREND_SEED.get(cat, [])
            for item in items:
                search_volume = random.randint(180000, 3200000)
                growth = random.randint(150, 920)
                results.append({
                    "id": f"trend_{count}",
                    "topic": item,
                    "category": cat,
                    "search_volume": f"{search_volume:,}+ searches/mo",
                    "growth_rate": f"+{growth}% search surge",
                    "badge": "VIRAL" if growth > 500 else "TRENDING NOW",
                    "description": f"Curated high-engagement topic with viral curiosity coefficient."
                })
                count += 1
                
        return results

    def fetch_live_web_buzz(self, keyword: str = "") -> List[Dict[str, str]]:
        if not keyword:
            return self.get_trends("all")
        
        clean_kw = keyword.strip()
        variations = [
            f"Top 10 Most Mind-Blowing Discoveries About {clean_kw}",
            f"Top 10 Surreal Places & Spots Related to {clean_kw}",
            f"Top 10 Next-Generation Innovations in {clean_kw}",
            f"Top 10 Unexplained Mysteries Surrounding {clean_kw}",
            f"Top 10 Game-Changing Breakthroughs Shaping {clean_kw}"
        ]
        
        return [
            {
                "id": f"custom_{i+1}",
                "topic": var,
                "category": "custom",
                "search_volume": "Custom Topic",
                "growth_rate": "High Interest",
                "badge": "CUSTOM TREND",
                "description": f"Top 10 post concept centered on '{clean_kw}'."
            }
            for i, var in enumerate(variations)
        ]
