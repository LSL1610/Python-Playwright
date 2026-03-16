
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            channel="chrome",
            args=[
                "--blink-settings=imagesEnabled=false",
                "--disable-popup-blocking"
            ],
            slow_mo=1000,
        )
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(
        # viewport={"width": 1920, "height": 1080}
        no_viewport=True,
    )
    page = context.new_page()
    page.set_default_navigation_timeout(30000)
    page.set_default_timeout(30000)
    yield page
    context.close()