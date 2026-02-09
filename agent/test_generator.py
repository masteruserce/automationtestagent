from pathlib import Path
import json
import textwrap
import re


API_TEST_FILE = Path("automation/api/test_generated_api.py")


# ----------------------------
# Helpers
# ----------------------------


def resolve_path_params(path: str, parameters: list) -> str:
    for param in parameters or []:
        if param.get("in") == "path":
            name = param["name"]
            path = path.replace("{" + name + "}", f"test_{name}")
    return path


def safe_test_name(value: str) -> str:
    value = value.strip("/")
    value = re.sub(r"[{}\-\/]+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.lower().strip("_")


def requires_auth(endpoint: dict) -> bool:
    """
    Detect whether endpoint requires authentication.
    Default: True unless explicitly public.
    """
    security = endpoint.get("security")
    if security is None:
        return True
    return bool(security)


# ----------------------------
# Main generator
# ----------------------------


def generate_tests(base_url: str, endpoints: list):
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
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("api_test.log"),
        logging.StreamHandler()
    ]
)

def log_request_response(method, url, payload, response):
    logging.info(f"REQUEST {{method}} {{url}}")
    logging.info(f"Payload: {{payload}}")
    logging.info(f"Status Code: {{response.status_code}}")
    logging.info(f"Response Body: {{response.text[:1000]}}")

# ----------------------------
# Safe request wrapper
# ----------------------------
def safe_request(method, url, **kwargs):
    try:
        return requests.request(method, url, timeout=15, **kwargs)
    except Exception as e:
        logging.exception(f"Request failed: {{method}} {{url}}")
        pytest.fail(str(e))


# ----------------------------
# AUTH FIXTURE
# ----------------------------
@pytest.fixture(scope="session")
def auth_headers():
    try:
        response = requests.post(
            f"{{BASE_URL}}/api/v1/auth/auth/login",
            data={{
                "grant_type": "password",
                "username": "admin@acme.com",
                "password": "admin123",
                "client_id": "string",
                "client_secret": "",
            }},
            timeout=15,
        )
        response.raise_for_status()
        token = response.json().get("access_token")
        if not token:
            pytest.fail("Auth token missing in login response")

        return {{
            "Authorization": f"Bearer {{token}}"
        }}
    except Exception as e:
        pytest.fail(f"Authentication failed: {{e}}")


"""

    for ep in endpoints:
        method = ep["method"].upper()
        path = resolve_path_params(ep["path"], ep.get("parameters", []))
        url_expr = f'f"{{BASE_URL}}{path}"'
        test_name = safe_test_name(path)
        auth_needed = requires_auth(ep)

        payload, payload_type = generate_positive_payload(ep)
        payload_code = json.dumps(payload, indent=4) if payload else "None"

        headers_line = "headers=auth_headers" if auth_needed else ""

        # ----------------------------
        # POSITIVE TEST
        # ----------------------------
        positive_test = f"""
def test_{test_name}_{method.lower()}_positive({ "auth_headers" if auth_needed else "" }):
    url = {url_expr}
    payload = {payload_code}

    if payload:
        if "{payload_type}" == "form":
            response = safe_request("{method}", url, data=payload, {headers_line})
        else:
            response = safe_request("{method}", url, json=payload, {headers_line})
    else:
        response = safe_request("{method}", url, {headers_line})

    log_request_response("{method}", url, payload, response)
    assert response.status_code < 400
"""

        # ----------------------------
        # NEGATIVE TEST
        # ----------------------------
        neg_payload = generate_negative_payload(ep)
        neg_payload_code = json.dumps(neg_payload, indent=4) if neg_payload else "None"

        negative_test = f"""
def test_{test_name}_{method.lower()}_negative({ "auth_headers" if auth_needed else "" }):
    url = {url_expr}
    payload = {neg_payload_code}

    if payload:
        response = safe_request("{method}", url, json=payload, {headers_line})
    else:
        response = safe_request("{method}", url, {headers_line})

    log_request_response("{method}", url, payload, response)
    assert response.status_code in (400, 401, 403, 404, 422)
"""

        code += textwrap.dedent(positive_test)
        code += textwrap.dedent(negative_test)

    API_TEST_FILE.write_text(code.strip(), encoding="utf-8")
    print(f"[GENERATED] {API_TEST_FILE}")


# ----------------------------
# Payload generators
# ----------------------------


def generate_positive_payload(endpoint: dict):
    body = endpoint.get("requestBody")
    if not body:
        return None, None

    content = body.get("content", {})

    if "application/x-www-form-urlencoded" in content:
        schema = content["application/x-www-form-urlencoded"].get("schema", {})
        payload_type = "form"
    elif "application/json" in content:
        schema = content["application/json"].get("schema", {})
        payload_type = "json"
    else:
        return None, None

    properties = schema.get("properties", {})
    if not properties:
        return None, None

    payload = {
        key: example_value(value.get("type")) for key, value in properties.items()
    }

    return payload, payload_type


def generate_negative_payload(endpoint: dict):
    payload, _ = generate_positive_payload(endpoint)
    if not payload:
        return None

    payload = payload.copy()
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
