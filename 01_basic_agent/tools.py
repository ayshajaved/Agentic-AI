# ============================================================
# tools.py — Custom Tools for the Weather Agent
# ============================================================
# In Google ADK, a "Tool" is simply a Python function.
# The LLM reads the function name, args, and docstring to
# understand what it does and when to call it.
# ============================================================

import random


def get_weather(location: str) -> str:
    """Returns the current weather for a given location.

    Args:
        location: The city or place name (e.g. 'Tokyo', 'New York').

    Returns:
        A string with weather condition, temperature, humidity, and wind.
    """
    conditions = ["Sunny", "Cloudy", "Rainy", "Partly Cloudy", "Thunderstorm"]
    temp_c = random.randint(15, 38)
    temp_f = round(temp_c * 9 / 5 + 32)

    return (
        f"Weather in {location}:\n"
        f"  Condition : {random.choice(conditions)}\n"
        f"  Temperature: {temp_c}C / {temp_f}F\n"
        f"  Humidity  : {random.randint(40, 90)}%\n"
        f"  Wind      : {random.randint(5, 30)} km/h"
    )
