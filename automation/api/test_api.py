import pytest
import requests

BASE_URL = "https://example.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/api/users")
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "users" in json_data

def test_post_login():
    payload = {
        "username": "testuser",
        "password": "testpass"
    }
    response = requests.post(f"{BASE_URL}/api/login", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert isinstance(json_data, dict)
    assert "token" in json_data