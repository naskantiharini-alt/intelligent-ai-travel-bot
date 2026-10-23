
# AI Search and Recommendation Logic

import heapq
from travel_data import destinations, get_travel_advice


def uniform_cost_search(destination_data):
    """Find destinations in increasing estimated travel cost."""

    priority_queue = []

    for name, details in destination_data.items():
        heapq.heappush(
            priority_queue,
            (details["travel_cost"], name)
        )

    sorted_destinations = []

    while priority_queue:
        cost, name = heapq.heappop(priority_queue)
        sorted_destinations.append((name, cost))

    return sorted_destinations


def recommend_destinations(budget, interest, days):
    """Recommend destinations using budget and interest."""

    recommendations = []

    for name, details in destinations.items():

        # Calculate estimated trip cost
        hotel_cost = details["hotel_per_day"] * days

        activity_cost = sum(
            details["activities"].values()
        )

        total_cost = (
            details["travel_cost"]
            + hotel_cost
            + activity_cost
        )

        # Check whether the destination matches interest
        interest_match = interest.lower() in [
            item.lower() for item in details["type"]
        ]

        # Also allow relevant interests from the activity data
        if interest.lower() == "sightseeing":
            interest_match = True

        # Keep destinations matching budget and interest
        if total_cost <= budget and interest_match:
            recommendations.append({
                "name": name,
                "description": details["description"],
                "travel_cost": details["travel_cost"],
                "hotel_cost": hotel_cost,
                "activity_cost": activity_cost,
                "total_cost": total_cost,
                "activities": details["activities"]
            })

    # Sort by estimated total cost
    recommendations.sort(
        key=lambda item: item["total_cost"]
    )

    advice, activity_advice = get_travel_advice(
        budget, interest.lower()
    )

    return recommendations, advice, activity_advice
