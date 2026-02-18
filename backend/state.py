# backend/state.py

from typing import Dict, List, Any


class AppState:
    def __init__(self):
        self.swagger_spec: Dict[str, Any] = {}
        self.endpoints: List[Dict[str, Any]] = []
        self.intent_model: List[Dict[str, Any]] = []
        self.scenarios: List[Dict[str, Any]] = []
        self.base_url: str = ""


# SINGLE GLOBAL INSTANCE
state = AppState()
