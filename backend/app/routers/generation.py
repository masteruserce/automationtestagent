from fastapi import APIRouter
from backend.app.bdd.feature_generator import FeatureGenerator
from backend.app.bdd.step_definition_generator import StepDefinitionGenerator

from backend.app.models.generation_models import (
    GenerationRequest,
    GenerationResponse,
)
from backend.app.services.generation_service import GenerationService
from backend.state import state

router = APIRouter(prefix="/generation", tags=["Generation"])
service = GenerationService()


@router.post("/tests", response_model=GenerationResponse)
def generate_tests_file(request: GenerationRequest):

    filtered = [
        ep for ep in state.intent_model
        if ep["endpoint"] in request.selected_endpoints
    ]

    file_path = service.generate_tests_file(
        base_url=request.base_url,
        intent_model=filtered,
        swagger_spec=state.swagger_spec,
    )

    return GenerationResponse(
        message="Test file generated successfully",
        generated_file=file_path,
    )

@router.post("/generate-bdd")
def generate_bdd():
        if not state.swagger_spec:
              raise ValueError("Swagger not loaded")
            
        FeatureGenerator(state.swagger_spec).generate()
        StepDefinitionGenerator().generate()
        return {"message": "BDD features and steps generated"}