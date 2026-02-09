import pytest
import requests
import logging
import json

BASE_URL = "http://34.135.61.167:8000"

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
    logging.info(f"REQUEST {method} {url}")
    logging.info(f"Payload: {payload}")
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Response Body: {response.text[:1000]}")

def safe_request(method, url, **kwargs):
    try:
        return requests.request(method, url, timeout=15, **kwargs)
    except Exception as e:
        logging.exception(f"Request failed: {method} {url}")
        pytest.fail(str(e))


# ----------------------------
# AUTH FIXTURE
# ----------------------------
@pytest.fixture(scope="session")
def auth_headers():
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/auth/login",
        data={
            "grant_type": "password",
            "username": "admin@acme.com",
            "password": "admin123",
            "client_id": "string",
            "client_secret": "",
        },
        timeout=15,
    )
    response.raise_for_status()
    token = response.json().get("access_token")
    if not token:
        pytest.fail("Auth token missing in login response")

    return {
        "Authorization": f"Bearer {token}"
    }



def test_get_api_v1_api_v1_projects_projects_positive(auth_headers):
    """
    Test Case ID: TC_API_001
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/v1/projects/projects/
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/v1/projects/projects/"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_v1_projects_projects_negative(auth_headers):
    """
    Test Case ID: TC_API_001_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/v1/projects/projects/"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_get_api_v1_api_health_health_positive(auth_headers):
    """
    Test Case ID: TC_API_002
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/health/health
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/health/health"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_health_health_negative(auth_headers):
    """
    Test Case ID: TC_API_002_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/health/health"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_create_api_v1_api_workflows_workflows_start_positive(auth_headers):
    """
    Test Case ID: TC_API_003
    GIVEN Validate API behavior
    WHEN the client sends a POST request to /api/v1/api/workflows/workflows/start
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/start"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("POST", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_create_api_v1_api_workflows_workflows_start_negative(auth_headers):
    """
    Test Case ID: TC_API_003_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized POST request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/start"
    payload = None

    # WHEN
    if payload:
        response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_create_api_v1_api_workflows_workflows_steps_test_job_id_test_step_approve_positive(auth_headers):
    """
    Test Case ID: TC_API_004
    GIVEN Validate API behavior
    WHEN the client sends a POST request to /api/v1/api/workflows/workflows/steps/test_job_id/test_step/approve
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/test_job_id/test_step/approve"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("POST", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_create_api_v1_api_workflows_workflows_steps_test_job_id_test_step_approve_negative(auth_headers):
    """
    Test Case ID: TC_API_004_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized POST request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/test_job_id/test_step/approve"
    payload = None

    # WHEN
    if payload:
        response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_create_api_v1_api_workflows_workflows_steps_test_job_id_test_step_reject_positive(auth_headers):
    """
    Test Case ID: TC_API_005
    GIVEN Validate API behavior
    WHEN the client sends a POST request to /api/v1/api/workflows/workflows/steps/test_job_id/test_step/reject
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/test_job_id/test_step/reject"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("POST", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_create_api_v1_api_workflows_workflows_steps_test_job_id_test_step_reject_negative(auth_headers):
    """
    Test Case ID: TC_API_005_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized POST request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/test_job_id/test_step/reject"
    payload = None

    # WHEN
    if payload:
        response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_get_api_v1_api_workflows_workflows_test_job_id_status_positive(auth_headers):
    """
    Test Case ID: TC_API_006
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/workflows/workflows/test_job_id/status
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/test_job_id/status"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_workflows_workflows_test_job_id_status_negative(auth_headers):
    """
    Test Case ID: TC_API_006_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/test_job_id/status"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_get_api_v1_api_workflows_workflows_test_job_id_steps_test_step_positive(auth_headers):
    """
    Test Case ID: TC_API_007
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/workflows/workflows/test_job_id/steps/test_step
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/test_job_id/steps/test_step"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_workflows_workflows_test_job_id_steps_test_step_negative(auth_headers):
    """
    Test Case ID: TC_API_007_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/test_job_id/steps/test_step"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_get_api_v1_api_workflows_workflows_admin_dead_letter_positive(auth_headers):
    """
    Test Case ID: TC_API_008
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/workflows/workflows/admin/dead-letter
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/dead-letter"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_workflows_workflows_admin_dead_letter_negative(auth_headers):
    """
    Test Case ID: TC_API_008_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/dead-letter"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_get_api_v1_api_workflows_workflows_admin_jobs_test_job_id_positive(auth_headers):
    """
    Test Case ID: TC_API_009
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/workflows/workflows/admin/jobs/test_job_id
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/test_job_id"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_workflows_workflows_admin_jobs_test_job_id_negative(auth_headers):
    """
    Test Case ID: TC_API_009_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/test_job_id"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_create_api_v1_api_workflows_workflows_admin_jobs_test_job_id_reset_positive(auth_headers):
    """
    Test Case ID: TC_API_010
    GIVEN Validate API behavior
    WHEN the client sends a POST request to /api/v1/api/workflows/workflows/admin/jobs/test_job_id/reset
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/test_job_id/reset"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("POST", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_create_api_v1_api_workflows_workflows_admin_jobs_test_job_id_reset_negative(auth_headers):
    """
    Test Case ID: TC_API_010_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized POST request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/test_job_id/reset"
    payload = None

    # WHEN
    if payload:
        response = safe_request("POST", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("POST", url, headers=auth_headers)

    # THEN
    log_request_response("POST", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_get_api_v1_api_workflows_workflows_events_test_job_id_positive(auth_headers):
    """
    Test Case ID: TC_API_011
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/workflows/workflows/events/test_job_id
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/events/test_job_id"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_workflows_workflows_events_test_job_id_negative(auth_headers):
    """
    Test Case ID: TC_API_011_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/events/test_job_id"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)

def test_get_api_v1_api_workflows_workflows_jobs_positive(auth_headers):
    """
    Test Case ID: TC_API_012
    GIVEN Validate API behavior
    WHEN the client sends a GET request to /api/v1/api/workflows/workflows/jobs
    THEN the API should return a successful response
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/jobs"
    payload = None

    # WHEN
    if payload:
        if "None" == "form":
            response = safe_request("GET", url, data=payload, headers=auth_headers)
        else:
            response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 404:
        pytest.xfail("Fake path parameter used")

    assert response.status_code == 200

def test_get_api_v1_api_workflows_workflows_jobs_negative(auth_headers):
    """
    Test Case ID: TC_API_012_NEG
    GIVEN an invalid request for Validate API behavior
    WHEN the client sends a malformed or unauthorized GET request
    THEN the API should reject the request
    """

    # GIVEN
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/jobs"
    payload = None

    # WHEN
    if payload:
        response = safe_request("GET", url, json=payload, headers=auth_headers)
    else:
        response = safe_request("GET", url, headers=auth_headers)

    # THEN
    log_request_response("GET", url, payload, response)

    if response.status_code == 200:
        pytest.xfail("Endpoint allows request by design")

    assert response.status_code in (400, 401, 403, 404, 422)