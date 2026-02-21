# ============================================================
# main.py — Entry Point for RAG Agent Demo
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

from agents import hr_expert

# Load API Key from the root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

APP_NAME   = "rag_policy_app"
USER_ID    = "employee_101"
SESSION_ID = "policy_check_001"

async def main() -> None:
    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
    )

    runner = Runner(
        app_name=APP_NAME,
        agent=hr_expert,
        session_service=session_service,
    )

    print("=" * 60)
    print("   Google ADK — RAG (Retrieval-Augmented Generation)")
    print("=" * 60 + "\n")

    query = "What is the policy for working from home and internet stipend?"
    print(f"  USER : {query}\n")

    user_message = types.Content(
        role="user",
        parts=[types.Part(text=query)],
    )

    # The agent will:
    # 1. Analyze query
    # 2. Call search_policies() tool
    # 3. Use the tool results to write the final answer
    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=user_message,
    ):
        # Tools will be called by the agent to retrieve data
        tool_calls = event.get_function_calls()
        if tool_calls:
            for call in tool_calls:
                print(f"  [RETRIEVING] {call.name} (args: {call.args})")

        if event.is_final_response() and event.content and event.content.parts:
            response = "".join(
                p.text for p in event.content.parts
                if hasattr(p, "text") and p.text
            )
            print(f"\n  FINAL ANSWER :\n{'-' * 40}\n{response}\n{'-' * 40}\n")

if __name__ == "__main__":
    asyncio.run(main())
