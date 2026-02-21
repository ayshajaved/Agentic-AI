# Module 04 — Parallel Agents

This module demonstrates how to use `ParallelAgent` to perform multiple tasks at the same time.

## Concepts Covered

| Concept | Description |
|---|---|
| **Parallelization** | Concurrent execution of multiple agents to gather data from different sources independently. |
| **ParallelAgent** | A built-in agent type that triggers all its sub-agents simultaneously. |
| **Consolidation** | The process where results from multiple parallel branches are unified into a final output. |

## How it Works

1.  **Input**: User query ("Give me a briefing on Paris").
2.  **Concurrency**: ADK triggers BOTH the **Weather Expert** and **Culture Expert** at once.
3.  **Independence**: Each agent executes its own tools and logic without waiting for the other.
4.  **Final Response**: The LLM receives the outcomes of all parallel branches and writes a complete briefing.

## Setup & Run

1.  **API Key**: Uses the `.env` in the root folder.
2.  **Run**:
```powershell
cd 04_parallel_agents
python main.py
```

## Why use Parallel Agents?
-   **Speed**: Faster than running tasks one-by-one.
-   **Comparison**: Great for comparing prices, reviews, or facts from different sources.
-   **Independence**: Cleanly separates specialized logic into different agents that don't need to know about each other.
