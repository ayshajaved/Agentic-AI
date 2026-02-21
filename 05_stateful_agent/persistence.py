# ============================================================
# persistence.py — Custom JSON File-Based Session Service
# ============================================================

import json
import os
from typing import Optional
from google.adk.sessions import InMemorySessionService, Session


class JsonFileSessionService(InMemorySessionService):
    def __init__(self, storage_path: str = "sessions.json"):
        super().__init__()
        self.storage_path = storage_path
        self._load_from_disk()

    def _load_from_disk(self):
        """Loads sessions from the JSON file if it exists."""
        if not os.path.exists(self.storage_path):
            return

        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, sess_dict in data.items():
                    # Reconstruct the Session object using Pydantic's model_validate
                    session = Session.model_validate(sess_dict)
                    
                    app_name = session.app_name
                    user_id = session.user_id
                    session_id = session.id
                    
                    self.sessions.setdefault(app_name, {}).setdefault(user_id, {})[session_id] = session
            print(f"[STORAGE] Loaded existing sessions from {self.storage_path}")
        except Exception as e:
            print(f"[STORAGE] Error loading sessions: {e}")

    async def append_event(self, session, event) -> None:
        """Saves data to disk every time a new event happens."""
        await super().append_event(session=session, event=event)
        self._save_to_disk()

    def _save_to_disk(self):
        """Saves current in-memory sessions to a JSON file."""
        try:
            storage_data = {}
            for app_name, users in self.sessions.items():
                for user_id, sess_dict in users.items():
                    for session_id, session in sess_dict.items():
                        key = f"{app_name}:{user_id}:{session_id}"
                        # Use Pydantic's model_dump to get a serializable dict
                        storage_data[key] = session.model_dump(mode="json")
            
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(storage_data, f, indent=2)
        except Exception as e:
            print(f"[STORAGE] Error saving sessions: {e}")
