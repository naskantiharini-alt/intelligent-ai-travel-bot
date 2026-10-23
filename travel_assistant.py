
import os
import json

from dotenv import load_dotenv
from google import genai
from travel_data import destinations

load_dotenv()


def answer_travel_question(question, chat_history=None):
    """Answer travel questions using Gemini and project data."""

    if not question or not question.strip():
        return "Please enter a travel question."

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return (
            "Gemini API key not found. Check your .env file "
            "and make sure GEMINI_API_KEY is configured."
        )

    try:
        client = genai.Client(api_key=api_key)

        travel_context = json.dumps(
            destinations,
            ensure_ascii=False,
            default=str
        )

        prompt_parts = [
            "You are WanderWise, an intelligent AI travel assistant.",
            "Help with travel planning, itineraries, budgets, "
            "destinations, activities, and packing.",
            "Use simple, friendly, practical language.",
            "Use the supplied project destination data when relevant.",
            "Treat costs as estimates, not live prices.",
            "Do not invent bookings, live prices, or current weather.",
            "Clearly state when information is unavailable.",
            "",
            "PROJECT DESTINATION DATA:",
            travel_context,
            "",
            "RECENT CONVERSATION:"
        ]

        for message in (chat_history or [])[-10:]:
            if (
                isinstance(message, dict)
                and message.get("role") in ("user", "assistant")
                and isinstance(message.get("content"), str)
            ):
                role = message["role"].upper()
                content = message["content"]
                prompt_parts.append(f"{role}: {content}")

        prompt_parts.append(
            f"USER: {question.strip()}\nWANDERWISE:"
        )

        response = client.interactions.create(
            model="gemini-3.8-flash",
            input="\n".join(prompt_parts)
        )
        return response.output_text

        if response.text:
            return response.text

        return "I couldn't generate an answer. Please try again."

    except Exception as error:
        # Print diagnostic details, never the API key.
        print("WanderWise Gemini error:", type(error).__name__)
        print("Error details:", str(error))

        return (
            "Sorry, I couldn't get an AI response. Check the "
            "terminal error and your Gemini API configuration."
        )
