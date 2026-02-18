from pydantic import BaseModel
from typing import Optional, Dict, Any, List


class SwaggerImportRequest(BaseModel):
    server_url: str
    swagger_url: Optional[str] = None
    swagger_json: Optional[Dict[str, Any]] = None


class EndpointModel(BaseModel):
    endpoint: str
    method: str


class SwaggerImportResponse(BaseModel):
    title: str
    version: str
    total_endpoints: int
    endpoints: List[EndpointModel]
