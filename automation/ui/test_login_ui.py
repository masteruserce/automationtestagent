import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

def test_login(page):
    page.goto("https://example.com/login")
    page.fill('input[name="username"]', "testuser")
    page.fill('input[name="password"]', "password123")
    page.click('button[type="submit"]')
    page.wait_for_url("https://example.com/dashboard")
    assert page.url == "https://example.com/dashboard"