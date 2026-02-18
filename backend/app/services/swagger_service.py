import requests
from agent.swagger_reader import read_swagger, extract_endpoints


class SwaggerService:

    def load_swagger(self, swagger_url: str = None, swagger_json: dict = None):

        if swagger_url:
            swagger_json = read_swagger(swagger_url)

        if not swagger_json:
            raise ValueError("No Swagger data provided")

        base_url, endpoints_raw = extract_endpoints(swagger_json)

        # Normalize to UI-friendly structure
        endpoints = []
        for ep in endpoints_raw:
            endpoints.append({
                "endpoint": ep["path"],
                "method": ep["method"],
                "classification": None,
                "risk_level": None,
            })

        return swagger_json, endpoints
