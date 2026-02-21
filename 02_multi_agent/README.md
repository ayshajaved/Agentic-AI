# Module 02 — Multi-Agent System (Delegation)

This module demonstrates how to build a **Multi-Agent System** where a "Coordinator" agent delegates tasks to specialized sub-agents.

## Concepts Covered

| Concept | Description |
|---|---|
| **Delegation** | The ability of one agent to hand over control to another agent based on the task requirement. |
| **Sub-Agents** | Specialized agents that focus on a specific domain (Weather, Finance). |
| **Root Agent** | The entry point agent (`travel_coordinator`) that manages the sub-agents. |

## How it Works

1.  **User Request**: "What's the weather in Tokyo and how much is 500 USD in JPY?"
2.  **Coordinator Inference**: The `travel_coordinator` realizes it needs weather info and currency info.
3.  **Delegation 1**: It hands over control to the `weather_assistant`.
4.  **Tool Execution 1**: `weather_assistant` calls `get_weather('Tokyo')`.
5.  **Delegation 2**: Control returns to coordinator, which then delegates to `finance_assistant`.
6.  **Tool Execution 2**: `finance_assistant` calls `convert_currency(500, 'USD', 'JPY')`.
7.  **Synthesis**: The coordinator summarizes both results into a single friendly response.

## Setup & Run

1.  **Dependencies**: (Same as root)
2.  **API Key**: Uses the `.env` in the root folder.
3.  **Run**:
```powershell
cd 02_multi_agent
python main.py
```

## expected output
You will see tool calls from DIFFERENT agents being triggered automatically by the coordinator.
