from fastapi import APIRouter
from backend.app.models.swagger_models import (
    SwaggerImportRequest,
    SwaggerImportResponse,
    EndpointModel,
)
from backend.app.services.swagger_service import SwaggerService
from backend.state import state

router = APIRouter(prefix="/swagger", tags=["Swagger"])
service = SwaggerService()


@router.post("/import", response_model=SwaggerImportResponse)
def import_swagger(request: SwaggerImportRequest):

    swagger_json, endpoints = service.load_swagger(
        request.swagger_url,
        request.swagger_json,
    )

    state.swagger_spec = swagger_json
    state.endpoints = endpoints
    state.base_url = request.server_url
    print(f"state.swagger_spec: {state.swagger_spec}")
    return SwaggerImportResponse(
        title=swagger_json.get("info", {}).get("title", "Unknown"),
        version=swagger_json.get("info", {}).get("version", "Unknown"),
        total_endpoints=len(endpoints),
        endpoints=[EndpointModel(**ep) for ep in endpoints],
    )
