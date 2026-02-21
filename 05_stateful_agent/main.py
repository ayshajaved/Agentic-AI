# ============================================================
# main.py — Entry Point for Stateful Agent Demo
# ============================================================

import asyncio
import os
import sys

# Ensure UTF-8 output
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from dotenv import load_dotenv
from google.adk import Runner
from google.genai import types

from agents import memory_agent
from persistence import JsonFileSessionService

# Load API Key from the root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

APP_NAME   = "memory_app"
USER_ID    = "user_123"
SESSION_ID = "persistent_session_001"

async def run_query(runner: Runner, query: str) -> None:
    print(f"\n  USER  : {query}")
    user_message = types.Content(role="user", parts=[types.Part(text=query)])
    
    for event in runner.run(user_id=USER_ID, session_id=SESSION_ID, new_message=user_message):
        if event.is_final_response() and event.content and event.content.parts:
            response = "".join(p.text for p in event.content.parts if hasattr(p, "text") and p.text)
            print(f"  AGENT : {response}")

async def main() -> None:
    # Use our custom File-based session service
    session_service = JsonFileSessionService(storage_path="sessions.json")
    
    # We no longer need to manually create/get the session here.
    # The Runner will handle it if we set auto_create_session=True.

    runner = Runner(
        app_name=APP_NAME,
        agent=memory_agent,
        session_service=session_service,
        auto_create_session=True, # THIS simplifies everything
    )

    print("\n" + "=" * 60)
    print("   Google ADK — Stateful Agent (Persistence Demo)")
    print("=" * 60)

    # Check if we have arguments passed to the script to simulate "Run 1" and "Run 2"
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
        await run_query(runner, query)
    else:
        print("\n[TIP] Run this script twice to see memory in action:")
        print("  1. python main.py My name is Antigravity")
        print("  2. python main.py Do you remember my name?")
        
        # Just run a status check for now
        await run_query(runner, "Hi! Just checking if you remember anything about me.")

if __name__ == "__main__":
    asyncio.run(main())
