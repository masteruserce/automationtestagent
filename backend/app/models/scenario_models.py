from pydantic import BaseModel
from typing import List


class ScenarioStep(BaseModel):
    step_number: int
    method: str
    endpoint: str


class ScenarioModel(BaseModel):
    scenario_name: str
    steps: List[ScenarioStep]


class ScenarioRequest(BaseModel):
    selected_endpoints: List[str]


class ScenarioResponse(BaseModel):
    total_scenarios: int
    scenarios: List[ScenarioModel]
