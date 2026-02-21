# ============================================================
# agents.py — Parallel Agent Configuration
# ============================================================

from google.adk.agents import LlmAgent, ParallelAgent
from google.adk.models import Gemini

from tools import get_weather, get_culture_fact

# 1. The Weather Expert
weather_expert = LlmAgent(
    name="weather_expert",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="Provides meteorological data for cities.",
    instruction="Provide a brief weather report for the requested city.",
    tools=[get_weather],
)

# 2. The Culture Expert
culture_expert = LlmAgent(
    name="culture_expert",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="Provides cultural and historical facts about cities.",
    instruction="Provide one interesting cultural fact or landmark for the requested city.",
    tools=[get_culture_fact],
)

# 3. The City Briefer (Parallel Agent)
# This agent runs its sub-agents concurrently. 
# The results from all sub-agents are collected before moving to the next step.
city_briefer = ParallelAgent(
    name="city_briefer",
    description="Briefs the user on a city by gathering weather and culture in parallel.",
    sub_agents=[weather_expert, culture_expert],
)
