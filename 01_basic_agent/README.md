# Google ADK — Simple Weather Agent

A beginner-friendly project to learn **Google Agent Development Kit (ADK)** by building a weather agent that uses a custom tool, a Gemini LLM, and a session-based runner.

## What You Learn

| Concept | File | Description |
|---|---|---|
| **Tool** | `tools.py` | A Python function the agent can call |
| **Agent** | `agent.py` | LLM-powered AI with instructions + tools |
| **Runner** | `main.py` | Orchestrates sessions, messages, and events |
| **Session** | `main.py` | Conversation history stored in memory |
| **Events** | `main.py` | Stream of actions the agent takes |

## Project Structure

```
ADK/
├── agent.py       # Agent definition (LlmAgent + Gemini model)
├── tools.py       # Custom tool: get_weather()
├── main.py        # Entry point: Runner + Session + Event loop
├── .env           # Your API key (not committed to Git)
├── .gitignore     # Excludes venv, .env, logs, cache
└── README.md      # This file
```

## Setup

### 1. Create a virtual environment
```powershell
python -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies
```powershell
pip install google-adk python-dotenv
```

### 3. Set your Gemini API Key
Get a free key at: https://aistudio.google.com/app/apikey

Create a `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
```

### 4. Run the agent
```powershell
python main.py
```

## Expected Output

```
[OK] API Key loaded (ends with: ...xyzABC)

============================================================
   Google ADK — Simple Weather Agent
============================================================

  USER  : What's the weather like in Tokyo?
  [TOOL] get_weather  args={'location': 'Tokyo'}
  AGENT : The weather in Tokyo is currently Sunny with a temperature
          of 28C. Humidity is 65% and winds are at 12 km/h. Enjoy!

  USER  : How about the weather in London?
  [TOOL] get_weather  args={'location': 'London'}
  AGENT : London is experiencing Rainy conditions at 16C...
```

## Key ADK Concepts

### Tool
Any Python function with a clear docstring. ADK passes the name, arguments, and docstring to the LLM so it knows when and how to call it.

### LlmAgent
The core AI agent. It receives a user message, reasons with the LLM, decides to call tools, and returns a final response.

### Runner
The orchestrator. It connects the agent to a session and processes the stream of events (tool calls, model responses, final output).

### InMemorySessionService
Stores conversation history in RAM. No database needed — perfect for learning and local development.

### Events
Every action the agent takes (text, tool call, tool result) is emitted as an `Event`. You iterate events to capture the final response.

## Next Steps

- Add more tools (e.g., news, calculator, database lookup)
- Build a **Multi-Agent System** with a coordinator and sub-agents
- Add **persistent sessions** using a database-backed session service
- Deploy with **Vertex AI Agent Engine**
