# ============================================================
# main.py — Entry Point for Parallel Agent Demo
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

from agents import city_briefer

# Load API Key from the root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_api_key_here":
    print("[ERROR] GOOGLE_API_KEY not set in root .env file.")
    sys.exit(1)

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
print(f"[OK] API Key loaded (ends with: ...{GOOGLE_API_KEY[-6:]})\n")

APP_NAME   = "city_briefing_app"
USER_ID    = "traveler_777"
SESSION_ID = "visit_paris_001"

async def main() -> None:
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    # Runner initialized with the ParallelAgent
    runner = Runner(
        app_name=APP_NAME,
        agent=city_briefer,
        session_service=session_service,
    )

    print("=" * 60)
    print("   Google ADK — Parallel City Intelligence Briefing")
    print("=" * 60 + "\n")

    city = "Paris"
    print(f"  CITY : {city}\n")

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=f"Give me a briefing on {city}")],
    )

    # In a ParallelAgent, ADK triggers all sub-agents at the same time
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message,
    ):
        # Tools will be called by different agents concurrently
        tool_calls = event.get_function_calls()
        if tool_calls:
            for call in tool_calls:
                print(f"  [PARALLEL TASK] {call.name} (args: {call.args})")

        if event.is_final_response() and event.content and event.content.parts:
            response = "".join(
                p.text for p in event.content.parts
                if hasattr(p, "text") and p.text
            )
            print(f"\n  CONSOLIDATED BRIEFING :\n{'-' * 40}\n{response}\n{'-' * 40}\n")

if __name__ == "__main__":
    asyncio.run(main())
