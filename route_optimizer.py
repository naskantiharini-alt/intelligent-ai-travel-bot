
from travel_data import destinations


def calculate_destination_cost(destination, days):
    """
    Calculate the estimated cost for visiting one destination.
    """
    if destination not in destinations:
        return None

    details = destinations[destination]

    travel_cost = details.get("travel_cost", 0)
    hotel_per_day = details.get("hotel_per_day", 0)
    activities = details.get("activities", [])

    if isinstance(activities, (int, float)):
        activity_cost = activities
    else:
        activity_cost = sum(
            value for value in activities
            if isinstance(value, (int, float))
        )

    total_cost = travel_cost + (hotel_per_day * days) + activity_cost

    return {
        "destination": destination,
        "days": days,
        "travel_cost": travel_cost,
        "hotel_cost": hotel_per_day * days,
        "activity_cost": activity_cost,
        "total_cost": total_cost
    }


def optimize_route(selected_destinations, days_per_destination=1):
    """
    Create a simple cost-based itinerary for selected destinations.

    Note: This version sorts destinations by estimated trip cost.
    It does not calculate geographical distance or actual travel time.
    """
    if not selected_destinations:
        return {
            "route": [],
            "total_cost": 0,
            "details": [],
            "message": "Please select at least one destination."
        }

    route_details = []

    for destination in selected_destinations:
        result = calculate_destination_cost(
            destination, days_per_destination
        )

        if result is not None:
            route_details.append(result)

    if not route_details:
        return {
            "route": [],
            "total_cost": 0,
            "details": [],
            "message": "No valid destinations were found."
        }

    # Sort by estimated cost, from lowest to highest.
    route_details.sort(key=lambda item: item["total_cost"])

    total_cost = sum(
        item["total_cost"] for item in route_details
    )

    return {
        "route": [
            item["destination"] for item in route_details
        ],
        "total_cost": total_cost,
        "details": route_details,
        "message": "Estimated itinerary created successfully."
    }
