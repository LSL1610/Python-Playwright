from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
import openpyxl
from urllib.parse import urlparse
from time import time, sleep
from loguru import logger

@logger.catch()
def check_access():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            channel="chrome",
            ignore_default_args=["--mute-audio"],
            args=['--window-position=0,0', 
                  '--blink-settings=imagesEnabled=false',
                  '--disable-popup-blocking'])
        
        context = browser.new_context(
            viewport={"width": 1920, "height": 1080})
        
        page = context.new_page()
        
        page.goto("https://shopee.vn/")
        page.keyboard.down('Escape')
        
        page.get_by_text('Đăng Nhập').click()
        sleep(2)
        page.get_by_placeholder('Email/Số điện thoại/Tên đăng nhập').fill(value='12345678')
        sleep(2)
        page.get_by_placeholder('Mật khẩu').fill(value='8492347238974')
        sleep(2)
        page.get_by_role("button", name="Đăng nhập").click()
        sleep(10)
        login_stt = page.get_by_text('lamdeptraicute').is_visible()
        logger.debug(login_stt)

        page.close()
        
check_access()
