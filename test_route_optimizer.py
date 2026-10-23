from route_optimizer import optimize_route
from travel_data import destinations

available = list(destinations.keys())

print("Available destinations:", available)

if len(available) >= 2:
    selected = available[:2]

    result = optimize_route(selected, days_per_destination=2)

    print("\nRoute:", " -> ".join(result["route"]))
    print("Estimated total cost: Rs.", result["total_cost"])

    for item in result["details"]:
        print(
            item["destination"],
            "| Travel:", item["travel_cost"],
            "| Hotel:", item["hotel_cost"],
            "| Activities:", item["activity_cost"],
            "| Total:", item["total_cost"]
        )
else:
    print("Add at least two destinations to travel_data.py.")