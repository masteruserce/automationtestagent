from collections import defaultdict
from typing import Dict, List


class ScenarioStep:
    def __init__(self, endpoint: str, method: str, classification: str):
        self.endpoint = endpoint
        self.method = method
        self.classification = classification


class Scenario:
    def __init__(self, resource: str):
        self.resource = resource
        self.steps: List[ScenarioStep] = []

    def add_step(self, step: ScenarioStep):
        self.steps.append(step)


class ScenarioGenerator:
    """
    Dynamically builds lifecycle scenarios from Swagger.
    """

    def __init__(self, swagger_spec: Dict):
        self.swagger_spec = swagger_spec

    def generate(self) -> List[Scenario]:

        paths = self.swagger_spec.get("paths", {})
        resource_map = defaultdict(list)
        print(f"Generating scenarios from paths: {list(paths.items())}")
        # -----------------------------
        # 1. Group endpoints by resource
        # -----------------------------
        for path, methods in paths.items():

            segments = [seg for seg in path.split("/") if seg and "{" not in seg]

            if not segments:
                continue

            resource = segments[-1]

            for method in methods.keys():

                classification = self._classify(method)

                resource_map[resource].append(
                    ScenarioStep(path, method.upper(), classification)
                )

        # -----------------------------
        # 2. Build lifecycle scenarios
        # -----------------------------
        scenarios = []

        for resource, steps in resource_map.items():

            scenario = Scenario(resource)

            # Ordered lifecycle
            ordered = sorted(
                steps,
                key=lambda s: self._lifecycle_order(s.classification)
            )

            for step in ordered:
                scenario.add_step(step)

            scenarios.append(scenario)

        return scenarios

    def _classify(self, method: str) -> str:
        method = method.upper()

        if method == "POST":
            return "create"
        if method == "GET":
            return "read"
        if method in ["PUT", "PATCH"]:
            return "update"
        if method == "DELETE":
            return "delete"

        return "other"

    def _lifecycle_order(self, classification: str) -> int:
        order = {
            "create": 1,
            "read": 2,
            "update": 3,
            "delete": 4,
            "other": 5,
        }
        return order.get(classification, 99)
