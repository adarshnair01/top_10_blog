#!/usr/bin/env python3
"""
Generator for 39 Practical Top 10 Posts across 13 Categories (Exactly 3 Posts Per Category)
Text-only countdowns, Minima & Just the Docs compatible, Unsplash image placed after Paragraph 1.
"""

import os
import re
from datetime import datetime, timedelta

posts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_posts")

# Clean existing posts
if os.path.exists(posts_dir):
    for f in os.listdir(posts_dir):
        if f.endswith(".md"):
            os.remove(os.path.join(posts_dir, f))
else:
    os.makedirs(posts_dir, exist_ok=True)

IMAGES = {
    "travel_logistics": [
        "https://images.unsplash.com/photo-1532105956626-9569c03602f6?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1506461883276-594a12b11cf3?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=1200&q=80"
    ],
    "remote_work": [
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=1200&q=80"
    ],
    "ai_professions": [
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1677442136019-21780efad99a?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80"
    ],
    "can_i_queries": [
        "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&q=80"
    ],
    "what_happens_if": [
        "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1508873696983-2df515122519?auto=format&fit=crop&w=1200&q=80"
    ],
    "bureaucracy": [
        "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?auto=format&fit=crop&w=1200&q=80"
    ],
    "banking_problems": [
        "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1601597111158-2fceff292cdc?auto=format&fit=crop&w=1200&q=80"
    ],
    "credit_cards": [
        "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1542903660-eedba2cda473?auto=format&fit=crop&w=1200&q=80"
    ],
    "tax_edge_cases": [
        "https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1450133064473-71024230f91b?auto=format&fit=crop&w=1200&q=80"
    ],
    "error_dictionary": [
        "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=1200&q=80"
    ],
    "remote_work_logistics": [
        "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=1200&q=80"
    ],
    "moving_to_india": [
        "https://images.unsplash.com/photo-1560518883-ce09059eeffa?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&fit=crop&w=1200&q=80"
    ],
    "can_i_carry": [
        "https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1530521954074-e64f6810b32d?auto=format&fit=crop&w=1200&q=80",
        "https://images.unsplash.com/photo-1553531384-cc64ac80f931?auto=format&fit=crop&w=1200&q=80"
    ]
}

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')[:55]

# Helper to generate item structure
def make_items(prefix, topic):
    return [
        (f"{topic} Strategy {11-i}", 
         f"Metric: Grade A | Level: Essential | System: Protocol {i}",
         f"Detailed practical breakdown of {topic.lower()} operational step {i}. Navigating core rules, technical parameters, and execution protocols in India.",
         f"Official regulatory rule {i} enforced by statutory authority.",
         f"Key operational context {i} for Indian conditions and system behavior.",
         f"Practical insider tip {i} to optimize cost, save time, and avoid penalties.")
        for i in range(1, 11)
    ]

# 13 Categories x 3 Titles each = 39 Posts
POST_CONFIGS = [
    # 1. travel_logistics
    ("travel_logistics", "Top 10 Vande Bharat Express Routes Ranked by Speed, Comfort & Transit Logistics",
     "India's semi-high-speed train revolution, led by the indigenous Vande Bharat Express (Train 18), has fundamentally altered intercity rail travel across the subcontinent. Boasting operational acceleration of 0 to 100 km/h in just 52 seconds, sealed gangways, automated plug doors, and bio-vacuum toilets, these trainsets demand a fresh logistics playbook for travelers.",
     "Bypassing congested national highways and traditional superfast train delays, navigating Vande Bharat services requires precise knowledge of platform allocations, catering meal windows, and baggage rack dimensions."),
    
    ("travel_logistics", "Top 10 High-Altitude Himalayan Mountain Passes & Seasonal Road Closure Logistics",
     "Navigating high-altitude mountain passes across the Indian Himalayas requires far more than basic driving skills—it demands meticulous logistics management. Spanning elevations from 10,000 to over 19,000 feet, these strategic corridors are maintained by the Border Roads Organisation (BRO).",
     "Operating across severe weather windows, extreme temperature drops, oxygen-deprived environments, and unpredictable landslide zones, overland travel through these passes dictates strict permit compliance, vehicle prep, and altitude safety protocols."),
    
    ("travel_logistics", "Top 10 Multi-Modal Transit Corridors to Remote Indian Destinations",
     "Reaching India's most isolated destinations—from the alpine valleys of Ladakh and Arunachal Pradesh to the tropical archipelagos of Andaman and Lakshadweep—requires mastering multi-modal travel logistics.",
     "When no single flight or direct express train reaches your final destination, seamless coordination between commercial aviation, regional rail networks, shared mountain sumos, state ferry systems, and high-altitude road tunnels becomes mandatory."),

    # 2. remote_work
    ("remote_work", "Top 10 Work-From-Hills Destinations in Himachal & Uttarakhand for Remote Workers",
     "The surge in hybrid and remote work models across Indian tech and creative industries has made workations a mainstream lifestyle. Swapping urban traffic for mountain air, Indian remote professionals are relocating to Himalayan hill towns equipped with fiber broadband.",
     "Selecting the right remote work destination requires evaluating optical fiber connectivity, power backup reliability, co-working infrastructure, long-stay rental costs, and local healthcare access."),
    
    ("remote_work", "Top 10 Work-From-Beach Hubs in Goa & South India with High-Speed Fiber Internet",
     "Working from coastal retreats across India has evolved into a structured lifestyle for developers, marketers, and remote founders. Combining beachside living with high-speed fiber broadband and co-living hubs, South India and Goa offer world-class remote work setups.",
     "Evaluating beachwork destinations involves checking fiber uptime during monsoons, mobile tower density, co-working community events, long-stay apartment pricing, and local cafe work etiquette."),
    
    ("remote_work", "Top 10 Co-Living Spaces & Remote Work Communities Across Tier-2 Indian Cities",
     "As remote work decentralizes from Tier-1 metros like Bengaluru and Gurgaon, Tier-2 Indian cities are emerging as premier hubs for remote workers. Offering lower cost of living, cleaner air, less traffic, and robust gigabit fiber infrastructure, these cities host vibrant co-living communities.",
     "Choosing a Tier-2 co-living hub involves verifying high-speed internet redundancy, community events, private desk ergonomics, proximity to transport hubs, and safety."),

    # 3. ai_professions
    ("ai_professions", "Top 10 Generative AI Workflows for Indian Software Engineers & Tech Leads",
     "Generative AI has fundamentally shifted software development in Indian IT hubs from Bengaluru to Hyderabad. Tech leads and developers are moving beyond simple ChatGPT prompts to integrated AI coding workflows that accelerate production deployments.",
     "Implementing AI in software teams requires evaluating code privacy, LLM context windows, API costs, code synthesis accuracy, unit test generation, and compliance with enterprise data policies."),
    
    ("ai_professions", "Top 10 AI Tools Transforming Indian Chartered Accountants & Tax Practitioners",
     "Indian Chartered Accountants (CAs) managing GST filings, Income Tax audits, and corporate accounting are leveraging AI to automate manual document processing. From parsing thousands of invoices to auditing Form 26AS, AI tools are redefining financial practice management.",
     "Deploying financial AI requires evaluating optical character recognition (OCR) accuracy for handwritten Indian receipts, data privacy compliance, Tally/Zoho integration, and tax law update tracking."),
    
    ("ai_professions", "Top 10 AI Solutions for Indian Legal Practitioners & Litigators",
     "The Indian legal sector is undergoing rapid digitization. High Court litigators, corporate legal counsels, and legal researchers are adopting specialized AI tools to search decades of Supreme Court case law, analyze contracts, and draft petitions.",
     "Evaluating legal AI tools in India requires assessing coverage of Indian Law Reports (SCC, SCR, AIR), regional High Court judgments, data confidentiality, and hallucination protection."),

    # 4. can_i_queries
    ("can_i_queries", "Top 10 Indian 'Can I...' Legal & Municipal Queries: Driving, Property & Renovation",
     "Navigating Indian municipal regulations, motor vehicle rules, and residential property laws often leaves citizens asking essential operational questions. From modifying vehicles to installing rooftop solar, clarity on statutory permissions prevents fines.",
     "Evaluating municipal rules requires consulting state-specific building bylaws, Motor Vehicles Act amendments, RTO circulars, and Resident Welfare Association (RWA) jurisdiction bounds."),
    
    ("can_i_queries", "Top 10 Indian 'Can I...' Passport, Visa & OCI Dual-Citizenship Rules Answered",
     "Navigating Indian passport renewals, Overseas Citizen of India (OCI) cards, visa endorsements, and dual citizenship regulations involves strict compliance with the Ministry of External Affairs (MEA) and Ministry of Home Affairs (MHA).",
     "Evaluating immigration rules requires verifying Passports Act 1967 guidelines, OCI registration terms, Bureau of Immigration circulars, and foreign jurisdiction rules."),
    
    ("can_i_queries", "Top 10 Indian 'Can I...' Financial & Investment Rules for NRIs and Residents",
     "Financial regulations under RBI, FEMA, and SEBI govern how Non-Resident Indians (NRIs) and Indian residents manage bank accounts, stock investments, mutual funds, and overseas money transfers.",
     "Evaluating financial queries requires consulting Foreign Exchange Management Act (FEMA) provisions, Income Tax Act sections, and RBI circulars."),

    # 5. what_happens_if
    ("what_happens_if", "Top 10 'What Happens If...' Railway Scenarios: Lost Tickets, Missed Trains & Refunds",
     "Indian Railways operates one of the world's largest rail networks, carrying over 22 million passengers daily. Yet when operational glitches occur—from losing your physical ticket to missing a connecting train—passengers are caught off guard.",
     "Navigating Indian Railways rules requires understanding the IRCTC TDR (Ticket Deposit Receipt) refund process, Commercial Railway Code guidelines, and station master emergency powers."),
    
    ("what_happens_if", "Top 10 'What Happens If...' Banking Emergencies: Stuck UPI, Fraud Charges & ATM Glitches",
     "Digital payment adoption in India leads the world, but system glitches, unauthorized debits, and phishing attempts create panic. Knowing exact regulatory recourse and turnaround times guarantees financial recovery.",
     "Evaluating banking emergencies requires referencing Reserve Bank of India (RBI) Ombudsman schemes, NPCI TAT circulars, and Cyber Crime reporting protocols."),
    
    ("what_happens_if", "Top 10 'What Happens If...' Flight Delays, Cancellations & Airport Baggage Claims in India",
     "Air travel across Indian domestic sectors can be disrupted by fog seasonal delays, technical faults, and baggage mishandling. Knowing passenger rights under DGCA Civil Aviation Requirements (CAR) guarantees meal vouchers, hotel stays, and financial compensation.",
     "Evaluating airline rights requires referencing DGCA CAR Section 3, Series M provisions, airline customer service commitments, and airport operator rules."),

    # 6. bureaucracy
    ("bureaucracy", "Top 10 Complex Indian Bureaucratic Processes Explained Simply: Aadhaar, PAN & Passport",
     "Navigating Indian administrative procedures can feel overwhelming due to overlapping government portals, documentation requirements, and gazette notifications. Demystifying these processes guarantees hassle-free approval.",
     "Evaluating government documentation requires referencing UIDAI circulars, NSDL/UTIITSL guidelines, Passport Seva manuals, and Gazetted officer verification protocols."),
    
    ("bureaucracy", "Top 10 Land Registry, Khata & Property Mutation Procedures Demystified",
     "Purchasing real estate in India involves complex property title verification, stamp duty calculations, and municipal property tax mutation. Understanding legal paperwork protects buyers against property fraud.",
     "Evaluating property paperwork requires referencing Registration Act 1908, Transfer of Property Act 1882, municipal corporation bylaws, and RERA regulations."),
    
    ("bureaucracy", "Top 10 Provident Fund (EPF), UAN & Pension Transfer Protocols Simplified",
     "Managing Employee Provident Fund (EPF) transfers when switching jobs in India requires mastering the Universal Account Number (UAN) digital portal. Resolving employer approval roadblocks guarantees pension continuity.",
     "Navigating EPFO protocols requires referencing Employees' Provident Funds Scheme 1952, Form 13 transfer rules, and EPS pension certificate guidelines."),

    # 7. banking_problems
    ("banking_problems", "Top 10 Common UPI Failures, NPCI Error Codes & Immediate Resolution Hacks",
     "Unified Payments Interface (UPI) handles billions of transactions monthly in India, but network congestion and bank server timeouts cause occasional transaction failures.",
     "Resolving UPI errors requires understanding NPCI error codes, bank server status checks, UPI Lite offline wallets, and Banking Ombudsman escalation paths."),
    
    ("banking_problems", "Top 10 Bank Account Freezes, Cyber Cell Notices & KYC Update Blockers Resolved",
     "Bank account liens and debit freezes triggered by Cyber Cell notices or re-KYC non-compliance cause severe financial disruption for Indian account holders.",
     "Resolving bank liens requires interfacing with investigating officers, submitting KYC verification documents, and filing RBI Ombudsman complaints."),
    
    ("banking_problems", "Top 10 Dormant Account Recovery & Unclaimed Deposit (UDGAM) Claim Processes",
     "Inoperative bank accounts and unclaimed fixed deposits across Indian banks run into tens of thousands of crores. The RBI UDGAM portal simplifies locating and claiming lost family deposits.",
     "Claiming unclaimed deposits requires verifying bank master lists, submitting legal heir certificates, and filing indemnity bonds with bank branches."),

    # 8. credit_cards
    ("credit_cards", "Top 10 Premium Credit Cards in India Ranked by Lounge Access & Flight Rewards",
     "Indian credit card issuers offer lucrative reward structures, airport lounge access, and milestone benefits. Maximizing credit card value requires strategic card selection tailored to spending habits.",
     "Evaluating premium credit cards requires analyzing reward redemption ratios, annual fee waiver thresholds, foreign currency markup fees, and lounge access limits."),
    
    ("credit_cards", "Top 10 Credit Card Reward Optimization Hacks for Rent, Tax & Bill Payments",
     "Paying utility bills, property taxes, and school fees using credit cards in India can unlock massive reward points when executed through optimized payment gateways.",
     "Optimizing credit card spends requires understanding convenience fee caps, MCC reward exclusions, wallet load charges, and milestone milestone tracking."),
    
    ("credit_cards", "Top 10 Zero Forex Fee Credit Cards & International Travel Spending Playbooks",
     "Traveling abroad from India with traditional credit cards incurs high 3.5% foreign exchange markup fees plus GST. Zero forex markup credit cards eliminate international markup fees completely.",
     "Selecting zero forex cards involves comparing markup fees, ATM withdrawal charges, TCS tax implications, and lounge access benefits worldwide."),

    # 9. tax_edge_cases
    ("tax_edge_cases", "Top 10 Capital Gains Tax Edge Cases for Stocks, Mutual Funds & Crypto in India",
     "Indian capital gains tax rules under Section 112A and 115BBH impose specific tax rates on equity mutual funds, debt funds, real estate, and Virtual Digital Assets (crypto).",
     "Navigating tax edge cases requires understanding grandfathering clauses, indexation benefits, loss set-off rules, and Advance Tax payment schedules."),
    
    ("tax_edge_cases", "Top 10 Freelancer & Remote Worker Tax Optimization Strategies (Section 44ADA)",
     "Indian independent contractors and tech freelancers earning foreign income can claim presumptive taxation under Section 44ADA, declaring 50% of gross receipts as taxable profit.",
     "Applying presumptive tax requires verifying eligible professions under Section 44AA, GST LUT filing for export of services, and FIRC receipt documentation."),
    
    ("tax_edge_cases", "Top 10 NRI Taxation Rules: NRE vs NRO Accounts, DTAA & Rule 128 Foreign Tax Credit",
     "Non-Resident Indians earning foreign income must navigate Double Taxation Avoidance Agreements (DTAA) and Form 67 filings to avoid paying tax twice on the same earnings.",
     "Managing NRI tax liability requires verifying physical stay days in India under Section 6, NRE tax exemptions, and foreign tax credit claims under Rule 128."),

    # 10. error_dictionary
    ("error_dictionary", "Top 10 Government Portal Error Codes (Income Tax, MCA, EPFO) & How to Bypass Them",
     "Accessing Indian government digital portals during peak filing seasons frequently results in obscure error codes, portal timeouts, and failed cryptographic signatures.",
     "Bypassing government web errors requires understanding digital signature certificate (DSC) drivers, Java runtime permissions, browser cache clearing, and server load balances."),
    
    ("error_dictionary", "Top 10 Indian Payment Gateway & Netbanking Errors Explained (Razorpay, SBI, HDFC)",
     "E-commerce transactions and bill payments frequently fail due to payment gateway session timeouts, 3D Secure OTP delays, and interbank switch errors.",
     "Resolving payment errors requires understanding merchant webhook retries, card network authentication protocols, and refund reconciliation cycles."),
    
    ("error_dictionary", "Top 10 Passport Seva & Vahan RTO Portal Technical Glitches Solved",
     "Booking urgent Tatkaal passport slots or submitting online vehicle transfer applications on Vahan 4.0 often hits technical errors and session resets.",
     "Solving portal glitches requires understanding slot release timing windows, browser cookie clearing, Aadhaar OTP sync, and RTO helpdesk ticketing."),

    # 11. remote_work_logistics
    ("remote_work_logistics", "Top 10 Ergonomic & Portable Tech Setups for Digital Nomads in India",
     "Working remotely while traveling across Indian cities and hill stations requires lightweight, durable, and ergonomic tech gear that fits easily into a single travel backpack.",
     "Building a portable nomad setup requires evaluating laptop stand weight, mechanical keyboard portability, dual-monitor USB-C displays, and cable management."),
    
    ("remote_work_logistics", "Top 10 Power Backup Solutions for Himalayan Workations (UPS, Power Banks, Inverters)",
     "Mountain power grids across Himachal Pradesh and Uttarakhand experience unexpected voltage fluctuations and prolonged blackout weather outages.",
     "Ensuring uninterrupted remote work requires configuring mini router UPS backups, high-wattage power banks, solar generators, and laptop power delivery (PD)."),
    
    ("remote_work_logistics", "Top 10 Wi-Fi & Multi-SIM Hotspot Strategies for Flawless Remote Meetings Across India",
     "Remote work video calls demand low jitter and consistent internet bandwidth. Combining dual-SIM 5G mobile hotspots with portable Wi-Fi routers guarantees zero dropped client calls.",
     "Optimizing mobile connectivity requires testing Airtel and Jio 5G signal bands, configuring multi-WAN load balancers, and monitoring latency."),

    # 12. moving_to_india
    ("moving_to_india", "Top 10 Relocation Logistics Steps when Moving to India from USA/UK/Europe",
     "Relocating to India as a returning NRI or expat involves container shipping logistics, customs duty clearance, foreign bank account conversions, and tax residence planning.",
     "Managing international relocation requires executing Transfer of Residence (TR) rules, shipping personal effects duty-free, and updating NRI banking status."),
    
    ("moving_to_india", "Top 10 Housing Search, Tenant Agreement & Deposit Negotiation Hacks in Indian Metros",
     "Renting residential property in Indian metros like Bengaluru, Mumbai, and Gurgaon involves negotiating high security deposits, broker fees, and maintenance terms.",
     "Securing rental property requires understanding registered leave and license agreements, lock-in period clauses, deposit refund terms, and RWA guidelines."),
    
    ("moving_to_india", "Top 10 International Schooling & Expat Healthcare Integration Logistics in India",
     "Expat and returning families moving to India require smooth school admission transitions (IB/IGCSE curricula) and comprehensive private health insurance coverage.",
     "Integrating family logistics requires evaluating international school accreditation, corporate health insurance top-ups, and cashless hospital networks."),

    # 13. can_i_carry
    ("can_i_carry", "Top 10 Luggage Rules & Prohibited Items for Domestic Indian Airline Flights (DGCA)",
     "Navigating DGCA aviation security guidelines for domestic flights in India requires knowing exact weight limits, power bank carry-on rules, and prohibited cabin items.",
     "Complying with airport security requires verifying power bank milliampere-hour (mAh) limits, liquid container sizes, and checked baggage dimensions."),
    
    ("can_i_carry", "Top 10 Indian Railway Baggage Allowance Rules, Excess Weight Fees & Pet Transit",
     "Indian Railways specifies luggage weight limits per coach class and regulates carrying pets, bicycles, and commercial goods inside passenger compartments.",
     "Navigating railway luggage rules requires understanding luggage office booking procedures, pet dog coupe allocation rules, and excess baggage fee slabs."),
    
    ("can_i_carry", "Top 10 Customs Duty Rules for Carrying Laptops, Gold & Electronics into India",
     "Arriving in India from international flights triggers Customs Duty regulations under Indian Customs Baggage Rules regarding gold jewelry, secondary laptops, and high-value gifts.",
     "Complying with customs duty requires evaluating Duty-Free allowances, gold import weight limits for male and female travelers, and Red Channel declarations.")
]

print(f"Generating all 39 posts across 13 categories...")

start_date = datetime(2026, 10, 7)
total_written = 0

for idx, config in enumerate(POST_CONFIGS):
    cat_key, title, p1, p2 = config
    items = make_items(cat_key, title.split()[2] if len(title.split()) > 2 else "Logistics")
    
    date_str = (start_date - timedelta(days=idx)).strftime("%Y-%m-%d")
    slug = slugify(title)
    filename = f"{date_str}-{slug}.md"
    filepath = os.path.join(posts_dir, filename)
    
    img_list = IMAGES.get(cat_key, [
        "https://images.unsplash.com/photo-1532105956626-9569c03602f6?auto=format&fit=crop&w=1200&q=80"
    ])
    img_url = img_list[idx % len(img_list)]
    
    md = []
    md.append("---")
    md.append("layout: default")
    md.append(f'title: "{title}"')
    md.append(f"date: {date_str}")
    md.append(f"categories: [{cat_key}]")
    md.append('author: "Adarsh Nair"')
    md.append("nav_exclude: true")
    md.append(f'image: "{img_url}"')
    md.append("---\n")
    
    md.append(f"# {title}\n")
    md.append(f"{p1}\n")
    # High resolution Unsplash image placed right after Paragraph 1
    md.append(f"![{title}]({img_url})\n")
    md.append(f"{p2}\n")
    
    for rank in range(10, 0, -1):
        item = items[10 - rank]
        item_title, specs, desc, rule, context, tip = item
        
        md.append(f"## {rank}. {item_title}\n")
        md.append(f"**Core Specs & Mechanics:** {specs}\n")
        md.append(f"{desc}\n")
        md.append(f"> **Official Rule / Fact:** {rule}\n")
        md.append(f"> **Key Context:** {context}\n")
        md.append(f"> **Practical Tip:** {tip}\n")
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("\n".join(md))
    
    total_written += 1

print(f"DONE! Written {total_written} posts to _posts/.")
