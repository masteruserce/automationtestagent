from fastapi import APIRouter
from backend.app.models.scenario_models import (
ScenarioRequest,
ScenarioResponse,
ScenarioModel,
ScenarioStep as ScenarioStepModel,
)
from backend.app.services.scenario_service import ScenarioService
from backend.state import state

router = APIRouter(prefix="/scenarios", tags=["Scenarios"])
service = ScenarioService()

@router.post("/generate", response_model=ScenarioResponse)
def generate_scenarios(request: ScenarioRequest):
    scenarios = service.generate(
    state.intent_model,
    request.selected_endpoints,
    state.swagger_spec,
)

    state.scenarios = scenarios

    formatted = []

    for idx, scenario in enumerate(scenarios):

        steps = [
            ScenarioStepModel(
                step_number=i + 1,
                method=step.method,
                endpoint=step.endpoint,
            )
            for i, step in enumerate(scenario.steps)
        ]

        formatted.append(
            ScenarioModel(
                scenario_name=f"Scenario_{idx+1}",
                steps=steps,
            )
        )

    return ScenarioResponse(
        total_scenarios=len(formatted),
        scenarios=formatted,
    )
