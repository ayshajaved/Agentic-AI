# Agentic AI with Google ADK — Learning Repository

A structured, hands-on repository to learn **Google Agent Development Kit (ADK)** from zero to multi-agent systems. Each folder is a self-contained project that builds on the previous one.

## Learning Roadmap

| Folder | Topic | Concepts Covered |
|---|---|---|
| `01_basic_agent/` | Simple Agent + Tool | LlmAgent, Tool, Runner, Session, Events |
| `02_multi_agent/` | *(coming soon)* | Coordinator agent, sub-agents, delegation |
| `03_sequential_pipeline/` | *(coming soon)* | SequentialAgent, chaining multiple agents |
| `04_parallel_agents/` | *(coming soon)* | ParallelAgent, concurrent task execution |
| `05_stateful_agent/` | *(coming soon)* | Persistent sessions, state management |
| `06_rag_agent/` | *(coming soon)* | Retrieval-Augmented Generation with tools |

---

## Quick Start

### 1. Clone the repo
```powershell
git clone https://github.com/yourname/adk-learning.git
cd adk-learning
```

### 2. Create a virtual environment
```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```powershell
pip install google-adk python-dotenv
```

### 4. Set your Gemini API Key
Get a **free key** at: https://aistudio.google.com/app/apikey

Create `.env` in the **root** of this repo:
```env
GOOGLE_API_KEY=your_api_key_here
```
> All sub-projects read from this single `.env` file.

---

## Module 01 — Basic Agent

> **Learn:** How to build a single AI agent with a custom tool.

```powershell
cd 01_basic_agent
python main.py
```

**What you'll see:**
```
[OK] API Key loaded (ends with: ...xyzABC)

============================================================
   Google ADK — Simple Weather Agent
============================================================

  USER  : What's the weather like in Tokyo?
  [TOOL] get_weather  args={'location': 'Tokyo'}
  AGENT : The weather in Tokyo is Sunny with 28C...
```

**Files:**
```
01_basic_agent/
├── agent.py   # LlmAgent definition with instruction + tools
├── tools.py   # get_weather() — a custom tool function
├── main.py    # Runner + Session + Event loop
└── README.md  # Detailed explanation of this module
```

---

## Core ADK Concepts (Quick Reference)

```
Tool        → A Python function the LLM can call
LlmAgent    → AI agent powered by Gemini; has instruction + tools
Runner      → Orchestrator: connects agent + session + messages
Session     → A conversation thread (user ↔ agent history)
Event       → Every action (text, tool call, result) is an Event
```

---

## Tech Stack

- **Google ADK** — `google-adk`
- **Gemini 2.5 Flash** — LLM powering all agents
- **Python 3.11+**
- **python-dotenv** — API key management
