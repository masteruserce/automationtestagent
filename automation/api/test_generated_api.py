import pytest
import requests
import logging

BASE_URL = "http://34.56.161.228:8000/"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("api_test.log"), logging.StreamHandler()]
)

def log_request_response(method, url, response):
    logging.info(f"REQUEST {method} {url}")
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Response Body: {response.text[:1000]}")

def safe_request(method, url, **kwargs):
    try:
        return requests.request(method, url, timeout=15, **kwargs)
    except Exception as e:
        logging.exception("Request failed")
        pytest.fail(str(e))

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_auth_auth_login_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_001_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/auth/auth/login"
    response = safe_request("POST", url, headers=admin_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_auth_auth_login_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_002_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/auth/auth/login"
    response = safe_request("POST", url, headers=user_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.high
def test_create_api_v1_auth_auth_login_contract_stability():
    """
    Test Case ID: TC_API_003_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/auth/auth/login"
    response = safe_request("POST", url)

    log_request_response("POST", url, response)

    assert response.status_code < 500

@pytest.mark.functional
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_v1_projects_projects_as_admin(admin_headers):
    """
    Test Case ID: TC_API_004
    Role: admin
    Classification: read
    Risk Level: low
    """

    url = f"{BASE_URL}/api/v1/api/v1/projects/projects/"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (200, 201, 202, 204)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_v1_projects_projects_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_005_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/v1/projects/projects/"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_v1_projects_projects_contract_stability():
    """
    Test Case ID: TC_API_006_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/v1/projects/projects/"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500

@pytest.mark.functional
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_health_health_as_admin(admin_headers):
    """
    Test Case ID: TC_API_007
    Role: admin
    Classification: read
    Risk Level: low
    """

    url = f"{BASE_URL}/api/v1/api/health/health"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (200, 201, 202, 204)

@pytest.mark.functional
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_health_health_as_user(user_headers):
    """
    Test Case ID: TC_API_008
    Role: user
    Classification: read
    Risk Level: low
    """

    url = f"{BASE_URL}/api/v1/api/health/health"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (200, 201, 202, 204)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_health_health_contract_stability():
    """
    Test Case ID: TC_API_009_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/health/health"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_start_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_010_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/start"
    response = safe_request("POST", url, headers=admin_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_start_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_011_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/start"
    response = safe_request("POST", url, headers=user_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_start_contract_stability():
    """
    Test Case ID: TC_API_012_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/start"
    response = safe_request("POST", url)

    log_request_response("POST", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_steps_job_id_step_approve_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_013_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/approve"
    response = safe_request("POST", url, headers=admin_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_steps_job_id_step_approve_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_014_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/approve"
    response = safe_request("POST", url, headers=user_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_steps_job_id_step_approve_contract_stability():
    """
    Test Case ID: TC_API_015_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/approve"
    response = safe_request("POST", url)

    log_request_response("POST", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_steps_job_id_step_reject_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_016_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/reject"
    response = safe_request("POST", url, headers=admin_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_steps_job_id_step_reject_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_017_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/reject"
    response = safe_request("POST", url, headers=user_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_steps_job_id_step_reject_contract_stability():
    """
    Test Case ID: TC_API_018_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/reject"
    response = safe_request("POST", url)

    log_request_response("POST", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_job_id_status_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_019_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/status"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_job_id_status_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_020_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/status"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_job_id_status_contract_stability():
    """
    Test Case ID: TC_API_021_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/status"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_job_id_steps_step_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_022_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/steps/{step}"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_job_id_steps_step_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_023_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/steps/{step}"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_job_id_steps_step_contract_stability():
    """
    Test Case ID: TC_API_024_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/steps/{step}"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500

@pytest.mark.functional
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_admin_dead_letter_as_admin(admin_headers):
    """
    Test Case ID: TC_API_025
    Role: admin
    Classification: read
    Risk Level: low
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/dead-letter"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (200, 201, 202, 204)

@pytest.mark.functional
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_admin_dead_letter_as_user(user_headers):
    """
    Test Case ID: TC_API_026
    Role: user
    Classification: read
    Risk Level: low
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/dead-letter"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (200, 201, 202, 204)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_admin_dead_letter_contract_stability():
    """
    Test Case ID: TC_API_027_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/dead-letter"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_admin_jobs_job_id_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_028_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_admin_jobs_job_id_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_029_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_admin_jobs_job_id_contract_stability():
    """
    Test Case ID: TC_API_030_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_admin_jobs_job_id_reset_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_031_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}/reset"
    response = safe_request("POST", url, headers=admin_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_admin_jobs_job_id_reset_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_032_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}/reset"
    response = safe_request("POST", url, headers=user_headers)

    log_request_response("POST", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.high
def test_create_api_v1_api_workflows_workflows_admin_jobs_job_id_reset_contract_stability():
    """
    Test Case ID: TC_API_033_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}/reset"
    response = safe_request("POST", url)

    log_request_response("POST", url, response)

    assert response.status_code < 500

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_events_job_id_as_admin_forbidden(admin_headers):
    """
    Test Case ID: TC_API_034_SEC
    Role: admin
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/events/{job_id}"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_events_job_id_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_035_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/events/{job_id}"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_events_job_id_contract_stability():
    """
    Test Case ID: TC_API_036_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/events/{job_id}"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500

@pytest.mark.functional
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_jobs_as_admin(admin_headers):
    """
    Test Case ID: TC_API_037
    Role: admin
    Classification: read
    Risk Level: low
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/jobs"
    response = safe_request("GET", url, headers=admin_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (200, 201, 202, 204)

@pytest.mark.security
@pytest.mark.rbac
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_jobs_as_user_forbidden(user_headers):
    """
    Test Case ID: TC_API_038_SEC
    Role: user
    Expected: Forbidden
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/jobs"
    response = safe_request("GET", url, headers=user_headers)

    log_request_response("GET", url, response)

    assert response.status_code in (401, 403)

@pytest.mark.contract
@pytest.mark.low
def test_get_api_v1_api_workflows_workflows_jobs_contract_stability():
    """
    Test Case ID: TC_API_039_CONTRACT
    Verify endpoint does not produce 5xx errors
    """

    url = f"{BASE_URL}/api/v1/api/workflows/workflows/jobs"
    response = safe_request("GET", url)

    log_request_response("GET", url, response)

    assert response.status_code < 500