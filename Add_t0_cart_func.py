from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from time import time, sleep
from loguru import logger

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False,
                                channel="chrome",
                                slow_mo=2000)
    
    context = browser.new_context(viewport=
                                  {"width": 1920, "height": 1080})
    
    context.set_default_timeout(30000)
    context.set_default_navigation_timeout(60000)
    
    page = context.new_page()
    page.goto("https://www.demoblaze.com/")
    
    page.get_by_role("link", name="Log in").click()
    
    page.locator('//*[@id="loginusername"]').fill('lamdeptrai')
    sleep(3)
    page.locator('//*[@id="loginpassword"]').fill('lamdeptrai')
    sleep(3)
    page.get_by_role("button", name="Log in").click()
    sleep(3)
    lst = page.query_selector_all("//div[@class='col-lg-4 col-md-6 mb-4']")
    for loca in lst:
        try:
            with context.expect_page() as new_page_info:
                loca.click(button='middle')
                sleep(3)
        
            new_page = new_page_info.value      
            new_page.wait_for_load_state()
            new_page.bring_to_front()
            sleep(3)
            new_page.get_by_text('Add to cart').click()
            sleep(3)
            new_page.press("body", "Enter")
            sleep(3)
            new_page.close()
            sleep(3)
        except Exception as e:
            print(e)
    
    page.close()