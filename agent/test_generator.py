from pathlib import Path
import json
import textwrap

API_TEST_FILE = Path("automation/api/test_generated_api.py")


def generate_tests(base_url: str, endpoints: list):
    """
    Generates pytest API tests (positive + negative) from Swagger endpoints.
    Always overwrites generated file.
    """

    API_TEST_FILE.parent.mkdir(parents=True, exist_ok=True)

    code = f"""
import pytest
import requests
import logging
import json

BASE_URL = "{base_url}"

# ----------------------------
# Logging configuration
# ----------------------------
logging.basicConfig(
    filename="api_test.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_request_response(method, url, payload, response):
    logging.info(f"REQUEST {{method}} {{url}}")
    logging.info(f"Payload: {{payload}}")
    logging.info(f"Status Code: {{response.status_code}}")
    logging.info(f"Response Body: {{response.text[:1000]}}")

# ----------------------------
# Helper for safe request
# ----------------------------
def safe_request(method, url, **kwargs):
    try:
        response = requests.request(method, url, timeout=15, **kwargs)
        return response
    except Exception as e:
        logging.exception(f"Request failed: {{method}} {{url}}")
        pytest.fail(str(e))


"""
    for ep in endpoints:
        method = ep["method"]
        path = ep["path"]
        name = path.strip("/").replace("/", "_").replace("{", "").replace("}", "")
        url_expr = f'f"{{BASE_URL}}{path}"'
        payload = generate_positive_payload(ep)
        payload_code = json.dumps(payload, indent=4) if payload else "None"
        # ----------------------------
        # POSITIVE TEST
        # ----------------------------
        positive_test = f"""
def test_{name}_{method.lower()}_positive():
    url = {url_expr}
    payload ={payload_code}

    response = safe_request(
        "{method}",
        url,
        json=payload if payload else None,
        data=payload if payload else None
    )

    log_request_response("{method}", url, payload, response)

    assert response.status_code < 400
"""
        # ----------------------------
        # NEGATIVE TEST
        # ----------------------------
        negative_test = f"""
def test_{name}_{method.lower()}_negative():
    url = {url_expr}
    payload = {generate_negative_payload(ep)}

    response = safe_request(
        "{method}",
        url,
        json=payload if payload else None,
        data=payload if payload else None
    )

    log_request_response("{method}", url, payload, response)

    assert response.status_code >= 400
"""

        code += textwrap.dedent(positive_test)
        code += textwrap.dedent(negative_test)

    API_TEST_FILE.write_text(code.strip(), encoding="utf-8")
    print(f"[GENERATED] {API_TEST_FILE}")


# ----------------------------
# Payload generators
# ----------------------------


def generate_positive_payload(endpoint: dict):
    """
    Safely creates a valid payload from Swagger requestBody.
    Returns None if no request body is defined.
    """

    body = endpoint.get("requestBody")
    if not body:
        return None

    content = body.get("content")
    if not content:
        return None

    app_json = content.get("application/json") or content.get(
        "application/x-www-form-urlencoded"
    )

    if not app_json:
        return None

    schema = app_json.get("schema", {})
    properties = schema.get("properties", {})

    if not properties:
        return None

    payload = {}
    for key, value in properties.items():
        payload[key] = example_value(value.get("type"))

    return payload or None


def generate_negative_payload(endpoint: dict):
    """
    Creates an invalid payload (missing required fields).
    """
    payload = generate_positive_payload(endpoint)
    if payload:
        payload.pop(next(iter(payload)))
    return payload


def example_value(type_name: str):
    if type_name == "string":
        return "invalid"
    if type_name == "integer":
        return -1
    if type_name == "boolean":
        return False
    return None
