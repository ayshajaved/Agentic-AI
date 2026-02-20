# ============================================================
# main.py — Entry Point: Run the Weather Agent
# ============================================================
#
# Google ADK Core Concepts used here:
#
#   Runner               - Orchestrates the full agent lifecycle.
#                          Connects agent + session + message together.
#
#   InMemorySessionService - Stores conversation history in RAM.
#                            No database needed. Great for learning.
#
#   Session              - A single conversation context for one user.
#                          Identified by app_name + user_id + session_id.
#
#   types.Content        - The message format ADK uses (from google.genai).
#                          Wraps text/parts into a structured object.
#
#   Event                - Everything the agent does is an Event:
#                          sending text, calling a tool, or receiving a result.
#                          We iterate events to get the final response.
#
# Setup:
#   1. Create a .env file with: GOOGLE_API_KEY=your_key_here
#   2. Get a free key at: https://aistudio.google.com/app/apikey
#   3. Run: python main.py
# ============================================================

import asyncio
import os
import sys

# Ensure UTF-8 output on all platforms (avoids encoding errors on Windows)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from agent import weather_agent

# ------------------------------------------------------------
# Load API Key from .env
# ------------------------------------------------------------
# Load .env from the repo root (one level up from this folder)
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_api_key_here":
    print("[ERROR] GOOGLE_API_KEY not set in .env file.")
    print("  Get a free key: https://aistudio.google.com/app/apikey")
    sys.exit(1)

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
print(f"[OK] API Key loaded (ends with: ...{GOOGLE_API_KEY[-6:]})\n")


# ------------------------------------------------------------
# Constants
# ------------------------------------------------------------
APP_NAME   = "weather_app"
USER_ID    = "user_001"
SESSION_ID = "session_001"


async def run_agent(runner: Runner, query: str) -> None:
    """Sends a single query to the agent and prints the response.

    Args:
        runner: The configured ADK Runner instance.
        query:  The user's text message.
    """
    # Wrap the plain text query into the ADK message format
    user_message = types.Content(
        role="user",
        parts=[types.Part(text=query)],
    )

    print(f"  USER  : {query}")

    # runner.run() streams Events. We iterate until we get the final response.
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message,
    ):
        # Print any tool calls so we can see the agent "thinking"
        tool_calls = event.get_function_calls()
        if tool_calls:
            for call in tool_calls:
                print(f"  [TOOL] {call.name}  args={call.args}")

        # The final response event contains the agent's text reply
        if event.is_final_response() and event.content and event.content.parts:
            response = "".join(
                p.text for p in event.content.parts
                if hasattr(p, "text") and p.text
            )
            print(f"  AGENT : {response}\n")


async def main() -> None:
    """Sets up the ADK runner and runs the agent with sample queries."""

    # Step 1: Create a session service (in-memory, no DB required)
    session_service = InMemorySessionService()

    # Step 2: Create a session — this is the "conversation thread"
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    # Step 3: Build the Runner — the orchestrator that ties everything together
    runner = Runner(
        app_name=APP_NAME,
        agent=weather_agent,
        session_service=session_service,
    )

    # Step 4: Send queries to the agent
    print("=" * 60)
    print("   Google ADK — Simple Weather Agent")
    print("=" * 60 + "\n")

    queries = [
        "What's the weather like in Tokyo?",
        "How about the weather in London?",
        "Is it hot in Dubai right now?",
    ]

    for query in queries:
        await run_agent(runner, query)


if __name__ == "__main__":
    asyncio.run(main())
