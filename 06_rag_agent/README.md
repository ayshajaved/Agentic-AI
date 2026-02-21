# Module 06 — RAG Agent (Retrieval-Augmented Generation)

This final module demonstrates how to give agents access to **Private Data** (documents, PDFs, handbooks) using RAG.

## Concepts Covered

| Concept | Description |
|---|---|
| **Retrieval** | Searching through local data (like `company_policies.txt`) to find relevant information. |
| **Augmentation** | Adding that retrieved information into the LLM's prompt context. |
| **Generation** | Creating a factual answer based *only* on the provided data. |

## How it Works

1.  **Tooling**: We created a `search_policies` tool that mimics a database search.
2.  **Reasoning**: When the user asks about "WFH" or "Sick Leave", the agent identifies that it needs to call the search tool.
3.  **Factual Handoff**: The tool returns the raw text from the file, and the agent "rewrites" it as a helpful assistant.

## Setup & Run

1.  **Run**:
```powershell
cd 06_rag_agent
python main.py
```

## Why RAG?
-   **No Hallucinations**: The agent is tethered to a real document.
-   **Privacy**: You don't need to re-train the model; you just give it a tool to read your private files.
-   **Up-to-date**: Changing the text file instantly updates the agent's knowledge.
