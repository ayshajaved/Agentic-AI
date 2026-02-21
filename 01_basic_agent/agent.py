# ============================================================
# agent.py — Agent Definition
# ============================================================
# An LlmAgent is the core building block of Google ADK.
#
# Key parameters:
#   name        : Unique ID for this agent (lowercase, no spaces)
#   model       : The LLM that powers the agent's reasoning
#   description : Short summary (used by parent agents in multi-agent systems)
#   instruction : The system prompt — tells the agent how to behave
#   tools       : List of Python functions the agent can call
# ============================================================

from google.adk.agents import LlmAgent
from google.adk.models import Gemini

from tools import get_weather


weather_agent = LlmAgent(
    name="weather_assistant",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="A weather assistant that fetches real-time weather for any city.",
    instruction=(
        "You are a friendly Weather Assistant. "
        "When the user asks about weather in any location, "
        "always call the 'get_weather' tool with that location. "
        "Present the result in a warm, conversational tone."
    ),
    tools=[get_weather],
)
