import pytest

@pytest.fixture(scope="session")
def admin_headers():
    return {"Authorization": "Bearer <ADMIN_TOKEN>"}

@pytest.fixture(scope="session")
def user_headers():
    return {"Authorization": "Bearer <USER_TOKEN>"}
