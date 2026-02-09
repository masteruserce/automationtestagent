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
    page.goto("https://www.saucedemo.com/")
    page.fill("input#user-name", "standard_user")
    page.fill("input#password", "secret_sauce")
    page.click("input#login-button")
    page.wait_for_selector("div.inventory_list", timeout=5000)
    assert page.url == "https://www.saucedemo.com/inventory.html"