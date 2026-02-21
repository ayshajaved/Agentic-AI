# ============================================================
# tools.py — Tools for Parallel Agent Briefing
# ============================================================

import random


def get_weather(city: str) -> str:
    """Returns the current weather for a given city.

    Args:
        city: The name of the city (e.g. 'Paris', 'New York').

    Returns:
        A string with weather details.
    """
    conditions = ["Sunny", "Overcast", "Drizzling", "Clear Skies", "Breezy"]
    temp = random.randint(10, 35)
    return f"Weather in {city}: {random.choice(conditions)}, {temp}C."


def get_culture_fact(city: str) -> str:
    """Returns a legendary cultural fact or landmark for a city.

    Args:
        city: The name of the city.

    Returns:
        A cultural snippet about the city.
    """
    facts = {
        "Paris": "The Eiffel Tower was originally intended to be a temporary installation.",
        "Tokyo": "Tokyo is home to the world's busiest pedestrian crossing, Shibuya Crossing.",
        "New York": "The Statue of Liberty was a gift from France to the United States.",
        "London": "The 'Big Ben' is actually the name of the bell inside the clock tower, not the tower itself."
    }
    
    fact = facts.get(city, f"{city} is a vibrant place with a rich history and unique traditions.")
    return f"Cultural Insight ({city}): {fact}"
