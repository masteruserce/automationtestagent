from pydantic import BaseModel
from typing import List


class GenerationRequest(BaseModel):
    base_url: str
    selected_endpoints: List[str]
    generate_scenarios: bool = True


class GenerationResponse(BaseModel):
    message: str
    generated_file: str
