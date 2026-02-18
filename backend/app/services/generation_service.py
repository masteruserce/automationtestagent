from agent.test_generator import generate_tests


class GenerationService:

    def generate_tests_file(
        self,
        base_url: str,
        intent_model: list,
        swagger_spec: dict,
    ):
        generate_tests(base_url, intent_model, swagger_spec)
        return "automation/api/test_generated_api.py"
