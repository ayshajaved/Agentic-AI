# ============================================================
# agents.py — Sequential Agent Configuration
# ============================================================

from google.adk.agents import LlmAgent, SequentialAgent
from google.adk.models import Gemini

from tools import search_wiki

# 1. The Researcher Agent
# Its goal is to find facts using the search tool.
research_agent = LlmAgent(
    name="researcher",
    model=Gemini(model="gemini-2.5-flash"),
    description="A meticulous researcher who finds data and facts.",
    instruction=(
        "You are an expert Researcher. "
        "Use the 'search_wiki' tool to find facts about the user's topic. "
        "Provide only the facts found, clearly listed."
    ),
    tools=[search_wiki],
)

# 2. The Writer Agent
# Its goal is to take input (from the researcher) and turn it into a post.
writer_agent = LlmAgent(
    name="writer",
    model=Gemini(model="gemini-2.5-flash"),
    description="A creative content writer for social media.",
    instruction=(
        "You are a Creative Writer. "
        "You will receive a list of facts. "
        "Your job is to rewrite those facts into a catchy, viral LinkedIn post. "
        "Use emojis and a professional yet engaging tone."
    ),
)

# 3. The Content Pipeline (The Sequential Agent)
# This agent chains sub_agents together. 
# They will execute in the exact order specified in 'agents'.
content_pipeline = SequentialAgent(
    name="content_pipeline",
    description="A pipeline that researches a topic and writes a post about it.",
    sub_agents=[research_agent, writer_agent],
)
