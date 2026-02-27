import pytest
from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext


BASE_URL = "https://rahulshettyacademy.com/seleniumPractise/#/"


@pytest.fixture(scope="session")
def browser_instance():
    """Create a browser instance for the test session."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def context(browser_instance: Browser):
    """Create a new browser context for each test."""
    context = browser_instance.new_context(
        viewport={"width": 1280, "height": 720}
    )
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """Create a new page for each test."""
    page = context.new_page()
    page.goto(BASE_URL)
    page.wait_for_load_state("networkidle")
    yield page
    page.close()

# Made with Bob
