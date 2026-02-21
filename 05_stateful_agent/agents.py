# ============================================================
# agents.py — Stateful Memory Agent
# ============================================================

from google.adk.agents import LlmAgent
from google.adk.models import Gemini

memory_agent = LlmAgent(
    name="memory_assistant",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="An agent that remembers user details across conversations.",
    instruction=(
        "You are a helpful assistant with a perfect memory. "
        "Your goal is to remember details the user tells you (like their name, preferences, or goals). "
        "If you already know something about the user, greet them personally. "
        "If you don't know their name yet, ask for it politely."
    ),
)
