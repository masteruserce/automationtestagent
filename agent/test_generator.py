from pathlib import Path
import textwrap
import re
import itertools

API_TEST_FILE = Path("automation/api/test_generated_api.py")

TC_COUNTER = itertools.count(1)


# ----------------------------
# Helpers
# ----------------------------

def next_tc_id() -> str:
    return f"TC_API_{next(TC_COUNTER):03d}"


def safe_test_name(value: str) -> str:
    value = value.strip("/")
    value = re.sub(r"[{}\\/]+", "_", value)
    value = re.sub(r"-+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.lower().strip("_")


def bdd_test_name(method: str, path: str) -> str:
    clean = safe_test_name(path)
    action = {
        "GET": "get",
        "POST": "create",
        "PUT": "update",
        "DELETE": "delete",
        "PATCH": "update",
    }.get(method.upper(), method.lower())
    return f"{action}_{clean}"


# ----------------------------
# Main generator
# ----------------------------

def generate_tests(base_url: str, intent_model: list):

    API_TEST_FILE.parent.mkdir(parents=True, exist_ok=True)

    code = f"""
import pytest
import requests
import logging

BASE_URL = "{base_url}"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("api_test.log"), logging.StreamHandler()]
)

def log_request_response(method, url, response):
    logging.info(f"REQUEST {{method}} {{url}}")
    logging.info(f"Status Code: {{response.status_code}}")
    logging.info(f"Response Body: {{response.text[:1000]}}")

def safe_request(method, url, **kwargs):
    try:
        return requests.request(method, url, timeout=15, **kwargs)
    except Exception as e:
        logging.exception("Request failed")
        pytest.fail(str(e))
"""

    # ----------------------------
    # Generate tests per endpoint
    # ----------------------------

    for ep in intent_model:

        method = ep["method"].upper()
        path = ep["endpoint"]
        classification = ep.get("classification", "unknown")
        risk = ep.get("risk_level", "medium")
        roles_info = ep.get("roles", {})
        role_access = roles_info.get("role_access", {})
        requires_auth = roles_info.get("requires_auth", False)

        test_base_name = bdd_test_name(method, path)
        url_expr = f'f"{{BASE_URL}}{path}"'

        # ----------------------------------
        # ROLE-BASED TEST GENERATION
        # ----------------------------------

        for role_name, is_allowed in role_access.items():

            tc_id = next_tc_id()
            fixture_name = f"{role_name}_headers"

            if is_allowed:

                code += textwrap.dedent(f"""
@pytest.mark.functional
@pytest.mark.rbac
@pytest.mark.{risk}
def test_{test_base_name}_as_{role_name}({fixture_name}):
    \"\"\"
    Test Case ID: {tc_id}
    Role: {role_name}
    Classification: {classification}
    Risk Level: {risk}
    \"\"\"

    url = {url_expr}
    response = safe_request("{method}", url, headers={fixture_name})

    log_request_response("{method}", url, response)

    assert response.status_code in (200, 201, 202, 204)
""")

            else:

                code += textwrap.dedent(f"""
@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.{risk}
def test_{test_base_name}_as_{role_name}_forbidden({fixture_name}):
    \"\"\"
    Test Case ID: {tc_id}_SEC
    Role: {role_name}
    Expected: Forbidden
    \"\"\"

    url = {url_expr}
    response = safe_request("{method}", url, headers={fixture_name})

    log_request_response("{method}", url, response)

    assert response.status_code in (401, 403)
""")

        # ----------------------------------
        # UNAUTHENTICATED ACCESS TEST
        # ----------------------------------

        if requires_auth:

            tc_id = next_tc_id()

            code += textwrap.dedent(f"""
@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.{risk}
def test_{test_base_name}_without_auth():
    \"\"\"
    Test Case ID: {tc_id}_NOAUTH
    Verify unauthenticated access is rejected
    \"\"\"

    url = {url_expr}
    response = safe_request("{method}", url)

    log_request_response("{method}", url, response)

    assert response.status_code in (401, 403)
""")

        # ----------------------------------
        # CONTRACT SAFETY TEST
        # ----------------------------------

        tc_id = next_tc_id()

        code += textwrap.dedent(f"""
@pytest.mark.contract
@pytest.mark.{risk}
def test_{test_base_name}_contract_stability():
    \"\"\"
    Test Case ID: {tc_id}_CONTRACT
    Verify endpoint does not produce 5xx errors
    \"\"\"

    url = {url_expr}
    response = safe_request("{method}", url)

    log_request_response("{method}", url, response)

    assert response.status_code < 500
""")

    API_TEST_FILE.write_text(code.strip(), encoding="utf-8")
    print(f"[GENERATED] {API_TEST_FILE}")
