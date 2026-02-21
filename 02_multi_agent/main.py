# ============================================================
# main.py — Entry Point for Multi-Agent Demo
# ============================================================

import asyncio
import os
import sys

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
from google.adk import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Use relative import for the agents defined in this folder
from agents import travel_coordinator

# Load API Key from the root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_api_key_here":
    print("[ERROR] GOOGLE_API_KEY not set in root .env file.")
    sys.exit(1)

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
print(f"[OK] API Key loaded (ends with: ...{GOOGLE_API_KEY[-6:]})\n")

APP_NAME   = "travel_multi_agent_app"
USER_ID    = "explorer_001"
SESSION_ID = "trip_to_japan_001"

async def main() -> None:
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    # The Runner will track the state across multiple agents automatically
    runner = Runner(
        app_name=APP_NAME,
        agent=travel_coordinator,
        session_service=session_service,
    )

    print("=" * 60)
    print("   Google ADK — Multi-Agent Travel Coordinator")
    print("=" * 60 + "\n")

    query = "I'm planning a trip to Tokyo. What's the weather there, and how much is 500 USD in JPY?"
    print(f"  USER  : {query}")

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=query)],
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message,
    ):
        # Tool calls can now come from different agents
        tool_calls = event.get_function_calls()
        if tool_calls:
            for call in tool_calls:
                print(f"  [TOOL] {call.name} (args: {call.args})")

        # Monitor transfers between agents
        # (ADK internally handles the transfer of control)

        if event.is_final_response() and event.content and event.content.parts:
            response = "".join(
                p.text for p in event.content.parts
                if hasattr(p, "text") and p.text
            )
            print(f"\n  AGENT : {response}\n")

if __name__ == "__main__":
    asyncio.run(main())
