# Agentic AI with Google ADK — Learning Repository

A structured, hands-on repository to learn **Google Agent Development Kit (ADK)** from zero to multi-agent production systems. Each folder is a self-contained project that builds on the previous one.

## 🚀 Learning Roadmap

| Folder | Topic | Concepts Covered |
|---|---|---|
| `01_basic_agent/` | Simple Agent + Tool | LlmAgent, Tool, Runner, Session, Events |
| `02_multi_agent/` | Multi-Agent (Delegation) | Intent-based delegation, `transfer_to_agent` |
| `03_sequential_pipeline/` | Sequential Pipelines | `SequentialAgent`, fixed linear workflows |
| `04_parallel_agents/` | Parallel Agents | `ParallelAgent`, high-speed concurrency |
| `05_stateful_agent/` | Stateful & Persistent | `SessionService`, JSON file persistence |
| `06_rag_agent/` | RAG (Retrieval) | Retrieval-Augmented Generation, Search tools |

---

## 🛠️ Quick Start

### 1. Clone the repo
```powershell
git clone https://github.com/ayshajaved/Agentic-AI.git
cd Agentic-AI
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
Create a `.env` in the **root** folder:
```env
GOOGLE_API_KEY=your_api_key_here
```

---

## 📂 Modules Overview

### 01. Basic Agent + Tool
Build a single agent that can fetch real-time weather using function calling (tools).
- **Run:** `cd 01_basic_agent; python main.py`

### 02. Multi-Agent Delegation
A coordinator agent that intelligently transfers tasks to specialized sub-agents.
- **Run:** `cd 02_multi_agent; python main.py`

### 03. Sequential Pipelines
Create a "Production Line" where agents hand off data in a fixed order (Researcher → Writer).
- **Run:** `cd 03_sequential_pipeline; python main.py`

### 04. Parallel Agents
Gather diverse data from multiple sources simultaneously for high-speed execution.
- **Run:** `cd 04_parallel_agents; python main.py`

### 05. Stateful & Persistent Agents 🧠
Give your agent long-term memory that persists even after you restart the script.
- **Run:** `cd 05_stateful_agent; python main.py`

### 06. RAG Agent (Retrieval)
A factual assistant that searches local documents to answer questions without hallucinating.
- **Run:** `cd 06_rag_agent; python main.py`

---

## 🧩 Core ADK Concepts

- **LlmAgent**: Your AI "Brain" with instructions and tools.
- **Tool**: Python functions the LLM can "act" through.
- **Runner**: The engine that drives the agentic loop.
- **SessionService**: Manages the agent's memory (RAM or Disk).
- **Sequential/Parallel Agent**: specialized containers for complex multi-agent flows.

---

## 🚀 Tech Stack

- **Google ADK** (`google-adk`)
- **Gemini 2.0 Flash** — Recommended for high-speed agentic loops.
- **Python 3.11+**
- **dotenv** for API security.
