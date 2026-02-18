from pathlib import Path

class StepDefinitionGenerator:
    def generate(self, output_dir="features/steps"):

        Path(output_dir).mkdir(parents=True, exist_ok=True)

        steps_code = """
    from behave import given, when, then
    import requests

    BASE_URL = ""

    @given("Base API URL is configured")
    def step_base_url(context):
    context.base_url = BASE_URL

    @when('I send a "{method}" request to "{endpoint}"')
    def step_send_request(context, method, endpoint):

    url = context.base_url + endpoint
    context.response = requests.request(method, url)
    @then("I should receive a valid response")
    def step_validate(context):
    assert context.response.status_code < 500
    """

        Path(output_dir, "api_steps.py").write_text(steps_code.strip())