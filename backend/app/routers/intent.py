from backend.app.models.swagger_models import SwaggerImportRequest
from fastapi import APIRouter
from backend.app.services.intent_service import IntentService
from backend.app.models.intent_models import IntentBuildResponse
from backend.state import state

router = APIRouter(prefix="/intent", tags=["Intent"])
service = IntentService()


@router.post("/build", response_model=IntentBuildResponse)
def build_intent():
    
    if not state.swagger_spec:
        raise ValueError("Swagger not loaded")

    intent_model = service.build_intent_model(
        state.swagger_spec,
        state.base_url,
        state.endpoints
    )

    state.intent_model = intent_model

    return IntentBuildResponse(
        total_endpoints=len(intent_model),
        intent_model=intent_model
    )
