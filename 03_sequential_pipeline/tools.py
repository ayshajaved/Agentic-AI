# ============================================================
# tools.py — Tools for Sequential Pipeline
# ============================================================

import random


def search_wiki(topic: str) -> str:
    """Simulates searching for facts about a topic.

    Args:
        topic: The subject to research (e.g. 'Artificial Intelligence', 'Space').

    Returns:
        A list of simulated facts about the topic.
    """
    facts_db = {
        "Space": [
            "The universe is approximately 13.8 billion years old.",
            "There are more stars in the universe than grains of sand on Earth.",
            "Venus is the hottest planet in our solar system."
        ],
        "AI": [
            "The term 'Artificial Intelligence' was coined in 1956.",
            "Machine Learning is a subset of AI.",
            "Neural networks are inspired by the human brain."
        ],
        "Coffee": [
            "Coffee is the second most traded commodity in the world.",
            "Brazil produces about 40% of the world's coffee.",
            "The world's most expensive coffee is made from civet poop."
        ]
    }
    
    # Simple fuzzy search
    topic_key = next((k for k in facts_db if k.lower() in topic.lower()), "Random")
    facts = facts_db.get(topic_key, ["Fact: The world is full of interesting things.", "Fact: Learning is fun!"])
    
    return f"Research facts about {topic}:\n- " + "\n- ".join(facts)
