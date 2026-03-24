
import pytest
import os
from pytest_html import extras
from playwright.sync_api import sync_playwright

BROWSERS = ["chromium", "firefox", "webkit"]

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

@pytest.fixture(scope="function", name="NormalBrowser")
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

@pytest.fixture(scope="function", params=BROWSERS, name="MultipleBrowsers")
def page(request):
    browser_name = request.param

    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        yield page

        browser.close()