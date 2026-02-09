import pytest
import requests

BASE_URL = "http://34.135.61.167:8000/api/v1"


@pytest.fixture
def login_url():
    return f"{BASE_URL}/auth/auth/login"


def test_login_status_code_and_json_keys(login_url):
    payload = {"username": "admin@acme.com", "password": "admin123"}
    response = requests.post(login_url, json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    # Replace these keys with expected keys from the login response
    expected_keys = {"access_token", "refresh_token", "token_type"}
    assert expected_keys.issubset(json_data.keys())
