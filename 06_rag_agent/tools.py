# ============================================================
# tools.py — Simple Keyword Search Tool for RAG
# ============================================================

import os


def search_policies(query: str) -> str:
    """Searches the company policy handbook for relevant information.

    Args:
        query: The search term or question to look up.

    Returns:
        The most relevant sections of the policy found.
    """
    # In a real RAG system, you'd use Vector Embeddings and a DB.
    # For this learning module, we implement a simple keyword search.
    
    file_path = os.path.join(os.path.dirname(__file__), "data", "company_policies.txt")
    
    if not os.path.exists(file_path):
        return "Error: Policy handbook not found."

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split policy into sections by [TITLE]
    sections = content.split("\n\n")
    relevant_sections = []

    # Find sections containing any keywords from the query
    keywords = query.lower().split()
    for section in sections:
        if any(keyword in section.lower() for keyword in keywords):
            relevant_sections.append(section)

    if not relevant_sections:
        return "No specific policy found matching that query. Please ask about WFH, Leave, Travel, or Office Hours."

    return "\n\n".join(relevant_sections)
