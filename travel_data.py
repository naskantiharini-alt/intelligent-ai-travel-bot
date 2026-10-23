# Knowledge Base for Intelligent Travel Bot


destinations = {
    "Agra": {
        "type": ["History", "Architecture", "Photography"],
        "description": "Explore the Taj Mahal and Mughal architecture.",
        "travel_cost": 1500,
        "hotel_per_day": 1800,
        "activities": {"Taj Mahal": 1100, "Agra Fort": 650}
    },
    "Ahmedabad": {
        "type": ["History", "Food", "Culture"],
        "description": "Discover heritage sites, museums, and Gujarati food.",
        "travel_cost": 1200,
        "hotel_per_day": 1600,
        "activities": {"Heritage Walk": 300, "Museum Visit": 250}
    },
    "Amritsar": {
        "type": ["History", "Food", "Culture"],
        "description": "Visit the Golden Temple and experience Punjabi culture.",
        "travel_cost": 1500,
        "hotel_per_day": 1700,
        "activities": {"Golden Temple Visit": 0, "Wagah Border": 500}
    },
    "Andaman": {
        "type": ["Beach", "Nature", "Adventure"],
        "description": "Enjoy turquoise waters, islands, and water activities.",
        "travel_cost": 6000,
        "hotel_per_day": 3000,
        "activities": {"Island Tour": 1500, "Snorkelling": 1200}
    },
    "Bengaluru": {
        "type": ["Food", "Nature", "Shopping"],
        "description": "Explore gardens, cafés, shopping, and city attractions.",
        "travel_cost": 1000,
        "hotel_per_day": 2000,
        "activities": {"Garden Visit": 100, "Museum Visit": 200}
    },
    "Bhopal": {
        "type": ["History", "Nature", "Culture"],
        "description": "Discover lakes, museums, and historical monuments.",
        "travel_cost": 1000,
        "hotel_per_day": 1500,
        "activities": {"Museum Visit": 200, "Lake Tour": 300}
    },
    "Bhubaneswar": {
        "type": ["History", "Culture", "Architecture"],
        "description": "Explore ancient temples and Odisha's cultural heritage.",
        "travel_cost": 1200,
        "hotel_per_day": 1600,
        "activities": {"Temple Tour": 300, "Museum Visit": 150}
    },
    "Chandigarh": {
        "type": ["Architecture", "Nature", "Shopping"],
        "description": "Visit modern architecture, gardens, and city attractions.",
        "travel_cost": 1200,
        "hotel_per_day": 2000,
        "activities": {"Rock Garden": 100, "Garden Visit": 100}
    },
    "Chennai": {
        "type": ["Beach", "Food", "Culture"],
        "description": "Enjoy Marina Beach, temples, and South Indian cuisine.",
        "travel_cost": 1200,
        "hotel_per_day": 1800,
        "activities": {"Museum Visit": 200, "Beach Visit": 0}
    },
    "Coimbatore": {
        "type": ["Nature", "Food", "Spirituality"],
        "description": "Explore nature, local cuisine, and nearby hill destinations.",
        "travel_cost": 1000,
        "hotel_per_day": 1500,
        "activities": {"Temple Visit": 200, "Nature Tour": 500}
    },
    "Darjeeling": {
        "type": ["Nature", "Mountains", "Photography"],
        "description": "Enjoy Himalayan views, tea gardens, and toy-train rides.",
        "travel_cost": 2500,
        "hotel_per_day": 2200,
        "activities": {"Tea Garden Visit": 300, "Toy Train": 1000}
    },
    "Delhi": {
        "type": ["History", "Food", "Shopping"],
        "description": "Explore India's capital, monuments, markets, and food.",
        "travel_cost": 1000,
        "hotel_per_day": 2000,
        "activities": {"Red Fort": 150, "Qutub Minar": 100}
    },
    "Goa": {
        "type": ["Beach", "Adventure", "Nightlife"],
        "description": "Relax on beaches and enjoy water sports and local cuisine.",
        "travel_cost": 2500,
        "hotel_per_day": 2500,
        "activities": {"Water Sports": 1500, "Fort Visit": 200}
    },
    "Guwahati": {
        "type": ["Nature", "Culture", "Spirituality"],
        "description": "Discover Assam's culture, river views, and nearby nature.",
        "travel_cost": 1800,
        "hotel_per_day": 1800,
        "activities": {"Temple Visit": 200, "River Cruise": 500}
    },
    "Hyderabad": {
        "type": ["History", "Food", "Shopping"],
        "description": "Explore Charminar, Golconda Fort, and famous Hyderabadi food.",
        "travel_cost": 1000,
        "hotel_per_day": 1800,
        "activities": {"Golconda Fort": 200, "Museum Visit": 100}
    },
    "Indore": {
        "type": ["Food", "Culture", "Shopping"],
        "description": "Discover street food, markets, and historic city attractions.",
        "travel_cost": 1200,
        "hotel_per_day": 1600,
        "activities": {"Food Tour": 500, "Palace Visit": 200}
    },
    "Jaipur": {
        "type": ["History", "Architecture", "Shopping"],
        "description": "Explore forts, palaces, colourful markets, and Rajasthani food.",
        "travel_cost": 1800,
        "hotel_per_day": 2000,
        "activities": {"Amber Fort": 500, "City Palace": 400}
    },
    "Jaisalmer": {
        "type": ["Desert", "Adventure", "History"],
        "description": "Experience desert landscapes, forts, and camel safaris.",
        "travel_cost": 2500,
        "hotel_per_day": 2200,
        "activities": {"Fort Visit": 200, "Desert Safari": 1500}
    },
    "Kochi": {
        "type": ["Beach", "History", "Food"],
        "description": "Enjoy Fort Kochi, waterfront views, and Kerala cuisine.",
        "travel_cost": 1500,
        "hotel_per_day": 2000,
        "activities": {"Heritage Walk": 300, "Boat Ride": 500}
    },
    "Kolkata": {
        "type": ["History", "Food", "Culture"],
        "description": "Explore colonial architecture, museums, and Bengali cuisine.",
        "travel_cost": 1300,
        "hotel_per_day": 1800,
        "activities": {"Museum Visit": 200, "Heritage Tour": 400}
    },
    "Kashmir": {
        "type": ["Mountains", "Nature", "Adventure"],
        "description": "Discover scenic valleys, lakes, and Himalayan landscapes.",
        "travel_cost": 4000,
        "hotel_per_day": 3000,
        "activities": {"Shikara Ride": 800, "Valley Tour": 1200}
    },
    "Lucknow": {
        "type": ["History", "Food", "Architecture"],
        "description": "Explore Nawabi architecture and famous Awadhi cuisine.",
        "travel_cost": 1200,
        "hotel_per_day": 1700,
        "activities": {"Monument Tour": 300, "Food Tour": 500}
    },
    "Manali": {
        "type": ["Mountains", "Adventure", "Nature"],
        "description": "Enjoy mountain scenery, trekking, and outdoor adventures.",
        "travel_cost": 3000,
        "hotel_per_day": 2500,
        "activities": {"Solang Valley": 1000, "Local Sightseeing": 500}
    },
    "Mumbai": {
        "type": ["Beach", "Food", "Shopping"],
        "description": "Discover Marine Drive, historic landmarks, and city life.",
        "travel_cost": 1800,
        "hotel_per_day": 2800,
        "activities": {"Elephanta Caves": 500, "City Tour": 600}
    },
    "Mysuru": {
        "type": ["History", "Culture", "Architecture"],
        "description": "Visit Mysore Palace, gardens, and cultural attractions.",
        "travel_cost": 1200,
        "hotel_per_day": 1700,
        "activities": {"Palace Visit": 200, "Garden Visit": 100}
    },
    "Ooty": {
        "type": ["Mountains", "Nature", "Photography"],
        "description": "Enjoy tea gardens, mountain views, and scenic train journeys.",
        "travel_cost": 1800,
        "hotel_per_day": 2200,
        "activities": {"Botanical Garden": 100, "Lake Visit": 200}
    },
    "Pondicherry": {
        "type": ["Beach", "Culture", "Food"],
        "description": "Explore French-style streets, cafés, and peaceful beaches.",
        "travel_cost": 1500,
        "hotel_per_day": 2000,
        "activities": {"Heritage Walk": 300, "Beach Visit": 0}
    },
    "Pune": {
        "type": ["History", "Food", "Nature"],
        "description": "Discover forts, cafés, museums, and nearby hill destinations.",
        "travel_cost": 1200,
        "hotel_per_day": 1800,
        "activities": {"Fort Visit": 200, "Museum Visit": 150}
    },
    "Rishikesh": {
        "type": ["Adventure", "Nature", "Spirituality"],
        "description": "Experience river rafting, yoga, and Himalayan foothills.",
        "travel_cost": 1500,
        "hotel_per_day": 1700,
        "activities": {"River Rafting": 1000, "Yoga Session": 300}
    },
    "Shimla": {
        "type": ["Mountains", "Nature", "Shopping"],
        "description": "Explore Himalayan views, colonial streets, and hill trails.",
        "travel_cost": 2800,
        "hotel_per_day": 2400,
        "activities": {"Local Sightseeing": 500, "Nature Walk": 200}
    },
    "Udaipur": {
        "type": ["History", "Architecture", "Culture"],
        "description": "Enjoy lakes, palaces, heritage streets, and Rajasthani culture.",
        "travel_cost": 1800,
        "hotel_per_day": 2300,
        "activities": {"City Palace": 500, "Lake Boat Ride": 500}
    },
    "Varanasi": {
        "type": ["Spirituality", "History", "Culture"],
        "description": "Experience the ghats, temples, river views, and local culture.",
        "travel_cost": 1500,
        "hotel_per_day": 1700,
        "activities": {"Boat Ride": 500, "Heritage Walk": 300}
    },
    "Vijayawada": {
        "type": ["Spirituality", "Food", "Culture"],
        "description": "Visit riverside landmarks, temples, and local food spots.",
        "travel_cost": 1000,
        "hotel_per_day": 1500,
        "activities": {"Temple Visit": 100, "City Tour": 300}
    },
    "Visakhapatnam": {
        "type": ["Beach", "Nature", "Adventure"],
        "description": "Explore beaches, coastal viewpoints, and nearby hills.",
        "travel_cost": 1500,
        "hotel_per_day": 2000,
        "activities": {"Beach Visit": 0, "Nature Tour": 500}
    }
}



# Knowledge representation using IF-THEN rules

def get_travel_advice(budget, interest):
    if budget <= 3000:
        advice = "Choose budget-friendly transport and accommodation."
    elif budget <= 7000:
        advice = "Choose affordable hotels and compare transport options."
    else:
        advice = "You can consider more comfortable travel options."

    if interest == "beach":
        activity_advice = "Look for beaches and water activities."
    elif interest == "history":
        activity_advice = "Look for forts, palaces and historical sites."
    elif interest == "nature":
        activity_advice = "Look for gardens, mountains and nature walks."
    elif interest == "adventure":
        activity_advice = "Look for adventure sports and outdoor activities."
    elif interest == "culture":
        activity_advice = "Look for cultural attractions and local experiences."
    else:
        activity_advice = "Explore sightseeing and local attractions."

    return advice, activity_advice