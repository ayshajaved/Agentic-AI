# ============================================================
# tools.py — Tools for Multi-Agent System
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


def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    """Converts an amount from one currency to another using simulated exchange rates.

    Args:
        amount: The amount of money to convert.
        from_currency: The source currency code (e.g. 'USD', 'EUR').
        to_currency: The target currency code (e.g. 'JPY', 'GBP').

    Returns:
        A string showing the converted amount.
    """
    # Simulated rates
    rates = {
        ("USD", "JPY"): 150.0,
        ("USD", "EUR"): 0.92,
        ("USD", "GBP"): 0.79,
        ("EUR", "USD"): 1.08,
        ("GBP", "USD"): 1.26,
    }
    
    pair = (from_currency.upper(), to_currency.upper())
    rate = rates.get(pair, random.uniform(0.5, 200.0))
    converted = amount * rate
    
    return f"{amount} {from_currency.upper()} is approximately {converted:.2f} {to_currency.upper()} (Rate: {rate})"
