import json
import random
from typing import List, Dict

CATEGORIZED_TOPICS = {
    "travel_logistics": [
        "Top 10 Vande Bharat Express Routes Ranked by Speed, Comfort & Transit Logistics",
        "Top 10 High-Altitude Himalayan Mountain Passes & Seasonal Road Closure Logistics",
        "Top 10 Multi-Modal Transit Corridors to Remote Indian Destinations",
        "Top 10 Coastal Ferry & Island Transit Corridors in India",
        "Top 10 Night Superfast Express Trains with Best Punctuality and Catering"
    ],
    "remote_work": [
        "Top 10 Work-From-Hills Destinations in Himachal and Uttarakhand for Remote Workers",
        "Top 10 High-Speed Broadband & ISP Failover Strategies for Remote Workers in India",
        "Top 10 Co-Living Spaces for Digital Nomads in Goa, Kerala, and Bengaluru",
        "Top 10 Time-Zone Management Strategies for Indian Remote Workers Supporting US/EU Clients",
        "Top 10 Remote Work Community Hubs and Workation Cafes in India"
    ],
    "ai_professions": [
        "Top 10 AI Tools Revolutionizing Daily Workflows for Indian Chartered Accountants",
        "Top 10 AI Automation Tools for Indian Legal Advocates and Litigation Researchers",
        "Top 10 AI Coding Assistants Designed for Indian Enterprise Developers",
        "Top 10 AI Tools Transforming Medical Diagnostics & Clinic Operations in India",
        "Top 10 AI Content & Graphic Tools Built for Indian Marketing Agencies"
    ],
    "can_i_queries": [
        "Top 10 'Can I Drive an Other-State Vehicle in India?' RTO Road Tax Laws Explained",
        "Top 10 'Can I Rent Out My DDA/MHADA Flat?' Housing Society By-Laws Demystified",
        "Top 10 'Can I Change My Name in Official Records?' Gazette Notification Steps",
        "Top 10 'Can I Work Two Remote Jobs in India?' Moonlighting & PF Linkage Rules",
        "Top 10 'Can I Carry Homemade Food on Domestic Flights?' BCAS Rules Explained"
    ],
    "what_happens_if": [
        "Top 10 'What Happens If You Miss Your Connecting Train?' Indian Railways Rules",
        "Top 10 'What Happens If Fastag Fails at a Toll Plaza?' NHAI Regulations Decoded",
        "Top 10 'What Happens If a Bank Fails in India?' DICGC Insurance Coverage Explained",
        "Top 10 'What Happens If Your Flight Is Delayed Over 6 Hours?' DGCA Refund Charter",
        "Top 10 'What Happens If You Lose Your Passport Abroad?' Embassy Emergency Certificate Rules"
    ],
    "bureaucracy": [
        "Top 10 Indian Bureaucracy Hacks: Passport Tatkal, Police Verification & Re-issuance",
        "Top 10 Property Registration & Khata / Mutation Transfer Steps Explained Simply",
        "Top 10 Aadhaar Correction Hacks: Name, Address, and Biometric Updates",
        "Top 10 Driving License Renewal & International Driving Permit (IDP) Steps via Parivahan",
        "Top 10 Provident Fund (EPF) Transfer & UAN Merger Problem Fixes"
    ],
    "banking_problems": [
        "Top 10 Common UPI Failure Modes (Server Timeout, Debit Without Credit) & Instant Fixes",
        "Top 10 Dormant Bank Account Recovery & Inoperative Account KYC Steps",
        "Top 10 Unauthorized Bank Transaction Dispute & RBI Cyber-Fraud Chargeback Rules",
        "Top 10 Credit Bureau (CIBIL/Experian) Score Error Correction Hacks",
        "Top 10 International Wire Transfer Delay Fixes (SWIFT / Purpose Code Clarifications)"
    ],
    "credit_cards": [
        "Top 10 Credit Cards for Maximizing Reward Points on Indian Railway & Flight Bookings",
        "Top 10 Airport Lounge Access Credit Cards in India (2026 Access Criteria)",
        "Top 10 Zero Forex Markup Credit Cards for Indian Travelers & Freelancers",
        "Top 10 Cashback Credit Cards for Indian Utility Bills, Groceries, and Fuel",
        "Top 10 Premium Metal Credit Cards in India Ranked by Milestone Benefits"
    ],
    "tax_edge_cases": [
        "Top 10 Tax Edge Cases for Freelancers Receiving Foreign Remittances (Form 15CA/CB & FIRC)",
        "Top 10 Tax Loss Harvesting Strategies Under Indian Income Tax Act",
        "Top 10 Section 54F Real Estate Capital Gains Reinvestment Rules",
        "Top 10 Tax Implications of ESOPs for Employees in Indian Startups",
        "Top 10 Presumptive Taxation (Section 44ADA) Nuances for Professionals"
    ],
    "error_dictionary": [
        "Top 10 Mysterious IRCTC Error Messages Decoded (Session Expired, M-4, Payment Pending)",
        "Top 10 Income Tax e-Filing Portal Error Codes & Instant Workarounds",
        "Top 10 GST Portal Processing Errors and How to Resolve Them",
        "Top 10 EPFO Member Portal Errors (Invalid OAP, Name Mismatch) & Fixes",
        "Top 10 DigiLocker Sync Failures and Document Fetching Solutions"
    ],
    "remote_work_logistics": [
        "Top 10 Dual-ISP Load Balancing Routers & Power Backup Setups for Indian Home Offices",
        "Top 10 Ergonomic Chairs & Height-Adjustable Desk Setup Guide for Indian Homes",
        "Top 10 Noise-Cancelling Headsets for Working in Noisy Indian Neighborhoods",
        "Top 10 Portable Power Banks & Solar Generators for Off-Grid Remote Work in India",
        "Top 10 Invoice & Expense Management Tools for Indian Remote Consultants"
    ],
    "moving_to_india": [
        "Top 10 Relocation Logistics Essentials When Moving to Bengaluru (Rent, Deposit, Commute)",
        "Top 10 Relocation Hacks When Moving to Mumbai (Locality Guide, Deposit & Water Timings)",
        "Top 10 NRI Moving Back to India Checklist (Banking Conversion, Tax Residency & Baggage)",
        "Top 10 Relocation Essentials When Moving to Gurgaon / NCR (Gated Societies, Power Backup)",
        "Top 10 Inter-State Vehicle Relocation & NOC Transfer Steps in India"
    ],
    "can_i_carry": [
        "Top 10 'Can I Carry This in Flight Cabin Baggage?' BCAS Security Rules",
        "Top 10 'Can I Carry This on Indian Railways?' Baggage Weight & Prohibited Items Rules",
        "Top 10 'Can I Carry Lithium Power Banks & Batteries?' Domestic Airline Regulations",
        "Top 10 'Can I Carry Medicines & Medical Equipment on Domestic Flights?' Rules",
        "Top 10 Restricted Items Rules for Metro Trains (Delhi, Mumbai, Bengaluru, Kolkata)"
    ]
}

CATEGORIES = [
    {"id": "travel_logistics", "label": "🚂 Indian Travel Logistics", "icon": "train"},
    {"id": "remote_work", "label": "💻 Remote Work", "icon": "laptop"},
    {"id": "ai_professions", "label": "🤖 AI for Indian Professions", "icon": "cpu"},
    {"id": "can_i_queries", "label": "❓ Indian 'Can I...?'", "icon": "help-circle"},
    {"id": "what_happens_if", "label": "⚡ 'What Happens If...?' India", "icon": "alert-circle"},
    {"id": "bureaucracy", "label": "🏛️ Indian Bureaucracy Explained", "icon": "file-text"},
    {"id": "banking_problems", "label": "🏦 Indian Banking Problems", "icon": "credit-card"},
    {"id": "credit_cards", "label": "💳 Credit Card Optimization", "icon": "dollar-sign"},
    {"id": "tax_edge_cases", "label": "📊 Tax Edge Cases", "icon": "pie-chart"},
    {"id": "error_dictionary", "label": "🔍 Error Message Dictionary", "icon": "code"},
    {"id": "remote_work_logistics", "label": "🔌 Remote Work Logistics", "icon": "zap"},
    {"id": "moving_to_india", "label": "📦 'Moving To...' India", "icon": "home"},
    {"id": "can_i_carry", "label": "🧳 'Can I Carry This?'", "icon": "briefcase"}
]

class TrendFetcher:
    def __init__(self):
        pass

    def get_trending_categories(self) -> List[Dict[str, str]]:
        return CATEGORIES

    def get_trends(self, category: str = "all") -> List[Dict[str, str]]:
        results = []
        categories_to_check = [category] if category != "all" and category in CATEGORIZED_TOPICS else list(CATEGORIZED_TOPICS.keys())
        
        count = 1
        for cat in categories_to_check:
            items = CATEGORIZED_TOPICS.get(cat, [])
            for item in items:
                results.append({
                    "id": f"topic_{count}",
                    "topic": item,
                    "category": cat,
                    "search_volume": "High Volume",
                    "growth_rate": "Trending Guide",
                    "badge": "PRACTICAL GUIDE",
                    "description": f"Fact-checked practical guide for {cat} in India."
                })
                count += 1
                
        return results
