from pydantic import BaseModel
from typing import List


class IntentBuildResponse(BaseModel):
    total_endpoints: int
    intent_model: List[dict] = []
