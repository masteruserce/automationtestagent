import pytest
import requests

BASE_URL = "http://localhost"  # Change to your API base URL

@pytest.fixture
def login_url():
    return f"{BASE_URL}/login"

def test_oauth2_password_login(login_url):
    form_data = {
        "grant_type": "password",
        "username": "admin@acme.com",
        "password": "admin123",
        "scope": "",
        "client_id": "string",
        "client_secret": ""
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = requests.post(login_url, data=form_data, headers=headers)
    assert response.status_code == 200
    json_response = response.json()
    assert "access_token" in json_response
    assert isinstance(json_response["access_token"], str)
    assert len(json_response["access_token"]) > 0