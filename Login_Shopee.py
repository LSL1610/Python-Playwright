from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import openpyxl
from urllib.parse import urlparse
from time import time, sleep

def check_access():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            ignore_default_args=["--mute-audio"],
            args=['--window-position=950,0', 
                  '--blink-settings=imagesEnabled=false',
                  '--disable-popup-blocking'])
        
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://shopee.vn/")
        sleep(5)
        page.close()

check_access()
