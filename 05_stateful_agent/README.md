# Module 05 — Stateful & Persistent Agents

This module demonstrates how to give agents **long-term memory** by persisting session data to a file.

## Concepts Covered

| Concept | Description |
|---|---|
| **Statefulness** | The ability of an agent to retain information across different interactions. |
| **SessionService** | The ADK component responsible for storing the conversation history and agent state. |
| **Persistence** | Moving data from temporary memory (RAM) to permanent storage (JSON/Database). |

## How it Works

1.  **Custom Service**: We created `JsonFileSessionService` which extends the standard ADK service.
2.  **Disk I/O**: Every time an event occurs, the service saves a snapshot of the session to `sessions.json`.
3.  **Resume**: When the script starts, it checks `sessions.json` and reconstructs the previous conversation context.

## Setup & Run

### Step 1: Tell the agent your name
```powershell
cd 05_stateful_agent
python main.py "My name is Antigravity and I love space."
```

### Step 2: Close and Restart (Check memory)
```powershell
python main.py "What do you know about me?"
```

## Why is this important?
Without persistence, robots/assistants start every day with amnesia. For real-world apps, you would replace the JSON file with a database like **Firestore**, **PostgreSQL**, or **Redis**.
