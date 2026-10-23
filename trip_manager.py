
import json
from pathlib import Path
from datetime import datetime


DATA_FILE = Path(__file__).parent / "trip_data.json"


def load_data():
    """Load saved trip data from the JSON file."""

    if not DATA_FILE.exists():
        return {
            "trips": [],
            "expenses": [],
            "packing_lists": {}
        }

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        data.setdefault("trips", [])
        data.setdefault("expenses", [])
        data.setdefault("packing_lists", {})

        return data

    except (json.JSONDecodeError, OSError):
        return {
            "trips": [],
            "expenses": [],
            "packing_lists": {}
        }


def save_data(data):
    """Save trip data to the JSON file."""

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def save_trip(destination, days, budget, itinerary=None):
    """Save a new trip and return its ID."""

    data = load_data()

    trip_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

    trip = {
        "id": trip_id,
        "destination": destination,
        "days": int(days),
        "budget": float(budget),
        "itinerary": itinerary or [],
        "created_at": datetime.now().isoformat(timespec="seconds")
    }

    data["trips"].append(trip)
    data["packing_lists"].setdefault(trip_id, [])
    save_data(data)

    return trip_id


def get_trips():
    """Return all saved trips."""

    return load_data()["trips"]


def delete_trip(trip_id):
    """Delete a trip, its expenses, and its packing list."""

    data = load_data()

    data["trips"] = [
        trip for trip in data["trips"]
        if trip["id"] != trip_id
    ]

    data["expenses"] = [
        expense for expense in data["expenses"]
        if expense["trip_id"] != trip_id
    ]

    data["packing_lists"].pop(trip_id, None)

    save_data(data)


def add_expense(trip_id, description, amount):
    """Record an expense for a saved trip."""

    data = load_data()

    if not any(trip["id"] == trip_id for trip in data["trips"]):
        return False

    expense = {
        "id": datetime.now().strftime("%Y%m%d%H%M%S%f"),
        "trip_id": trip_id,
        "description": description,
        "amount": float(amount),
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    data["expenses"].append(expense)
    save_data(data)

    return True


def get_expenses(trip_id):
    """Return expenses for one trip."""

    data = load_data()

    return [
        expense for expense in data["expenses"]
        if expense["trip_id"] == trip_id
    ]


def add_packing_item(trip_id, item):
    """Add an item to a trip's packing list."""

    data = load_data()

    if not any(trip["id"] == trip_id for trip in data["trips"]):
        return False

    packing_list = data["packing_lists"].setdefault(trip_id, [])

    if not any(
        entry["item"].casefold() == item.casefold()
        for entry in packing_list
    ):
        packing_list.append({
            "item": item,
            "packed": False
        })

    save_data(data)

    return True


def update_packing_item(trip_id, item, packed):
    """Mark a packing item as packed or unpacked."""

    data = load_data()

    for entry in data["packing_lists"].get(trip_id, []):
        if entry["item"] == item:
            entry["packed"] = bool(packed)
            save_data(data)
            return True

    return False


def get_packing_list(trip_id):
    """Return a trip's packing list."""

    data = load_data()

    return data["packing_lists"].get(trip_id, [])
