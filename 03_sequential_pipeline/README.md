# Module 03 — Sequential Pipelines

This module demonstrates how to use `SequentialAgent` to build linear task pipelines.

## Concepts Covered

| Concept | Description |
|---|---|
| **Pipeline** | A sequence of steps where the output of one agent becomes the input of the next. |
| **SequentialAgent** | A built-in agent type that executes a list of agents in a fixed, predefined order. |
| **Zero-Transfer Context** | Unlike delegation (where the LLM decides when to switch), a pipeline switches automatically as each step finishes. |

## How it Works

1.  **Input**: User query ("Write a post about Space").
2.  **Step 1 (Researcher)**: Finds facts about Space.
3.  **Handoff**: ADK automatically takes the Researcher's summary and gives it to the Writer.
4.  **Step 2 (Writer)**: Transforms the facts into a polished LinkedIn post.
5.  **Output**: The final creative content.

## Setup & Run

1.  **API Key**: Uses the `.env` in the root folder.
2.  **Run**:
```powershell
cd 03_sequential_pipeline
python main.py
```

## Difference from Module 02
In Module 02 (**Delegation**), the `travel_coordinator` acted like a manager choosing who to talk to. 
In Module 03 (**Pipelines**), the code defines a "factory line" where the work flows automatically through agents A and B.
