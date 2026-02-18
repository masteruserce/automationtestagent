from typing import Any, Dict
from agent.scenario.scenario_generator import ScenarioGenerator


class ScenarioService:

    def generate(self, intent_model: list, selected_endpoints: list, swagger_spec: Dict[str, Any] = None):

        filtered = [
            ep for ep in intent_model
            if ep["endpoint"] in selected_endpoints
        ]

        generator = ScenarioGenerator(swagger_spec=swagger_spec)
        return generator.generate()
