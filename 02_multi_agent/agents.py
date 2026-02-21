# ============================================================
# agents.py — Multi-Agent Configuration
# ============================================================
# This file defines a hierarchy of agents.
# The 'travel_coordinator' can delegate to specialized sub-agents.
# ============================================================

from google.adk.agents import LlmAgent
from google.adk.models import Gemini

from tools import get_weather, convert_currency

# 1. Specialized Weather Agent
weather_agent = LlmAgent(
    name="weather_assistant",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="Specialist in weather forecasts and climate information.",
    instruction="You are a weather expert. Provide detailed yet concise weather information.",
    tools=[get_weather],
)

# 2. Specialized Finance Agent
finance_agent = LlmAgent(
    name="finance_assistant",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="Specialist in currency conversion and financial math.",
    instruction="You are a finance expert. Help users convert money accurately.",
    tools=[convert_currency],
)

# 3. Travel Coordinator (The Root Agent)
# It has sub_agents and can delegate to them when it identifies a need.
travel_coordinator = LlmAgent(
    name="travel_coordinator",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="A master travel assistant that helps with planning and logistics.",
    instruction=(
        "You are a Travel Coordinator. Your job is to help the user with their travel plans. "
        "You have access to a Weather Assistant and a Finance Assistant. "
        "If the user asks about weather, delegate to the Weather Assistant. "
        "If the user asks about money or currency, delegate to the Finance Assistant. "
        "Summarize all the information provided by your assistants for the user."
    ),
    sub_agents=[weather_agent, finance_agent],
)
