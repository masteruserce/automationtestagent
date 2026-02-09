import pytest
import requests
import logging
import json

BASE_URL = "http://34.135.61.167:8000"

# ----------------------------
# Logging configuration
# ----------------------------
logging.basicConfig(
    filename="api_test.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)


def log_request_response(method, url, payload, response):
    logging.info(f"REQUEST {method} {url}")
    logging.info(f"Payload: {payload}")
    logging.info(f"Status Code: {response.status_code}")
    logging.info(f"Response Body: {response.text[:1000]}")


# ----------------------------
# Helper for safe request
# ----------------------------
def safe_request(method, url, **kwargs):
    try:
        response = requests.request(method, url, timeout=15, **kwargs)
        return response
    except Exception as e:
        logging.exception(f"Request failed: {method} {url}")
        pytest.fail(str(e))


def test_api_v1_auth_auth_login_post_positive():
    url = f"{BASE_URL}/api/v1/auth/auth/login"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code < 400


def test_api_v1_auth_auth_login_post_negative():
    url = f"{BASE_URL}/api/v1/auth/auth/login"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_v1_projects_projects_get_positive():
    url = f"{BASE_URL}/api/v1/api/v1/projects/projects/"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_v1_projects_projects_get_negative():
    url = f"{BASE_URL}/api/v1/api/v1/projects/projects/"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_health_health_get_positive():
    url = f"{BASE_URL}/api/v1/api/health/health"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_health_health_get_negative():
    url = f"{BASE_URL}/api/v1/api/health/health"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_start_post_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/start"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_start_post_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/start"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_steps_job_id_step_approve_post_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/approve"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_steps_job_id_step_approve_post_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/approve"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_steps_job_id_step_reject_post_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/reject"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_steps_job_id_step_reject_post_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/steps/{job_id}/{step}/reject"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_job_id_status_get_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/status"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_job_id_status_get_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/status"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_job_id_steps_step_get_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/steps/{step}"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_job_id_steps_step_get_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/{job_id}/steps/{step}"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_admin_dead_letter_get_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/dead-letter"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_admin_dead_letter_get_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/dead-letter"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_admin_jobs_job_id_get_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_admin_jobs_job_id_get_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_admin_jobs_job_id_reset_post_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}/reset"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_admin_jobs_job_id_reset_post_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/admin/jobs/{job_id}/reset"
    payload = None

    response = safe_request(
        "POST",
        url,
        json=payload if payload else None,
        data=payload if payload else None,
    )

    log_request_response("POST", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_events_job_id_get_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/events/{job_id}"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_events_job_id_get_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/events/{job_id}"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400


def test_api_v1_api_workflows_workflows_jobs_get_positive():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/jobs"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code < 400


def test_api_v1_api_workflows_workflows_jobs_get_negative():
    url = f"{BASE_URL}/api/v1/api/workflows/workflows/jobs"
    payload = None

    response = safe_request(
        "GET", url, json=payload if payload else None, data=payload if payload else None
    )

    log_request_response("GET", url, payload, response)

    assert response.status_code >= 400
