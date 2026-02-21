# ============================================================
# main.py — Entry Point for Sequential Pipeline Demo
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

from agents import content_pipeline

# Load API Key from the root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
if not GOOGLE_API_KEY or GOOGLE_API_KEY == "your_api_key_here":
    print("[ERROR] GOOGLE_API_KEY not set in root .env file.")
    sys.exit(1)

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
print(f"[OK] API Key loaded (ends with: ...{GOOGLE_API_KEY[-6:]})\n")

APP_NAME   = "content_pipeline_app"
USER_ID    = "creator_001"
SESSION_ID = "pipeline_run_001"

async def main() -> None:
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    # Runner initialized with the SequentialAgent
    runner = Runner(
        app_name=APP_NAME,
        agent=content_pipeline,
        session_service=session_service,
    )

    print("=" * 60)
    print("   Google ADK — Sequential Content Pipeline")
    print("=" * 60 + "\n")

    topic = "The wonders of Space"
    print(f"  TOPIC : {topic}\n")

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=f"I want a LinkedIn post about {topic}")],
    )

    # In a SequentialAgent, ADK handles the flow from Researcher to Writer
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message,
    ):
        # Watch for tool calls from the Researcher
        tool_calls = event.get_function_calls()
        if tool_calls:
            for call in tool_calls:
                print(f"  [RESEARCHING] {call.name} (args: {call.args})")

        # In SequentialAgent, the final response event comes after the last agent finishes
        if event.is_final_response() and event.content and event.content.parts:
            response = "".join(
                p.text for p in event.content.parts
                if hasattr(p, "text") and p.text
            )
            print(f"\n  FINAL POST :\n{'-' * 40}\n{response}\n{'-' * 40}\n")

if __name__ == "__main__":
    asyncio.run(main())
