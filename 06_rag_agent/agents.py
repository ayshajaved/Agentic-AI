# ============================================================
# agents.py — RAG-powered HR Expert
# ============================================================

from google.adk.agents import LlmAgent
from google.adk.models import Gemini

from tools import search_policies

hr_expert = LlmAgent(
    name="hr_policy_assistant",
    model=Gemini(model="models/gemini-2.0-flash"),
    description="An HR assistant that answers questions using the company policy handbook.",
    instruction=(
        "You are an HR Specialist. Your goal is to answer employee questions accurately. "
        "ALWAYS use the 'search_policies' tool before answering to find the latest facts. "
        "If the policy doesn't contain the answer, say 'I'm sorry, I couldn't find information on that in our handbook.' "
        "Do not invent policies or guess."
    ),
    tools=[search_policies],
)
