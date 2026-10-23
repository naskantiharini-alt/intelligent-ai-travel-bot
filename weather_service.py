
import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


def get_weather(city):
    """
    Fetch current weather and a daily forecast for a city.
    No API key is required for ordinary non-commercial use.
    """

    if not city or not city.strip():
        return {
            "success": False,
            "message": "Please enter a city name."
        }

    try:
        # Find the city's geographical coordinates
        geo_response = requests.get(
            GEOCODING_URL,
            params={
                "name": city.strip(),
                "count": 1,
                "language": "en",
                "format": "json"
            },
            timeout=10
        )
        geo_response.raise_for_status()
        geo_data = geo_response.json()

        locations = geo_data.get("results", [])

        if not locations:
            return {
                "success": False,
                "message": f"No location found for '{city}'."
            }

        location = locations[0]
        latitude = location["latitude"]
        longitude = location["longitude"]

        # Fetch current weather and a 7-day forecast
        weather_response = requests.get(
            WEATHER_URL,
            params={
                "latitude": latitude,
                "longitude": longitude,
                "current": (
                    "temperature_2m,"
                    "relative_humidity_2m,"
                    "apparent_temperature,"
                    "is_day,"
                    "precipitation,"
                    "weather_code,"
                    "wind_speed_10m"
                ),
                "daily": (
                    "weather_code,"
                    "temperature_2m_max,"
                    "temperature_2m_min,"
                    "precipitation_probability_max"
                ),
                "forecast_days": 7,
                "timezone": "auto"
            },
            timeout=10
        )
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        current = weather_data.get("current", {})
        daily = weather_data.get("daily", {})

        return {
            "success": True,
            "city": location["name"],
            "country": location.get("country", ""),
            "current": current,
            "daily": daily
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "message": "Weather service timed out. Please try again."
        }

    except requests.exceptions.RequestException:
        return {
            "success": False,
            "message": (
                "Unable to connect to the weather service. "
                "Check your internet connection."
            )
        }

    except (ValueError, KeyError, TypeError):
        return {
            "success": False,
            "message": "Unable to process the weather data."
        }


def get_weather_description(code):
    """Convert a WMO weather code into a readable description."""

    descriptions = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        56: "Light freezing drizzle",
        57: "Dense freezing drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Slight snowfall",
        73: "Moderate snowfall",
        75: "Heavy snowfall",
        77: "Snow grains",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        85: "Slight snow showers",
        86: "Heavy snow showers",
        95: "Thunderstorm",
        96: "Thunderstorm with slight hail",
        99: "Thunderstorm with heavy hail"
    }

    try:
        return descriptions.get(int(code), "Weather information unavailable")
    except (ValueError, TypeError):
        return "Weather information unavailable"
