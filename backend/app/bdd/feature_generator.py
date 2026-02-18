from pathlib import Path
from collections import defaultdict

class FeatureGenerator:
    def __init__(self, swagger_spec):
        self.swagger_spec = swagger_spec

    def _extract_resource(self, path):
            parts = [p for p in path.split("/") if p and "{" not in p]
            return parts[-1] if parts else "general"

    def _generate_feature_file(self, resource, endpoints, output_dir):

        feature_content = f"""Feature: {resource.capitalize()} Endpoints"""
        for method, path in endpoints:
            feature_content += f"""
            Scenario: {method} {path}
            When I send a "{method}" request to "{path}"
            Then I should receive a valid response
            """
            file_path = Path(output_dir) / f"{resource}.feature"
            file_path.write_text(feature_content.strip())
        
    def generate(self, output_dir="features"):

        Path(output_dir).mkdir(parents=True, exist_ok=True)

        paths = self.swagger_spec.get("paths", {})
        resource_map = defaultdict(list)

        for path, methods in paths.items():
            resource = self._extract_resource(path)

            for method in methods.keys():
                resource_map[resource].append((method.upper(), path))

        for resource, endpoints in resource_map.items():
            self._generate_feature_file(resource, endpoints, output_dir)



