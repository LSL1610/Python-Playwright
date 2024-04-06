from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from time import time, sleep
from loguru import logger

host_name = 'https://www.lazada.vn/'
product_name = 'legging'

@logger.catch()
def get_info_product_by_name(host_name, product_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                    channel='chrome',
                                    ignore_default_args=['--mute-audio'],
                                    timeout=80000,)
        
        context = browser.new_context()
        context.set_default_timeout(30000)
        context.set_default_navigation_timeout(60000)
        
        page = context.new_page()
        try:
            page.goto(host_name)
            sleep(3)
            page.get_by_placeholder('Search in Lazada').fill(product_name)
            sleep(3)
            page.get_by_text('SEARCH').click()
            sleep(3)
            lst_name = page.get_attribute(page.locator('//*[@id="root"]/div/div[2]/div[1]/div/div[1]/div[2]/div[*]/div/div/div[2]/div[2]/a'), name='title')
            logger.debug(f'list product ==> {lst_name}')
            
        except Exception as e:
            logger.debug(e)
        page.close()
        
get_info_product_by_name(host_name, product_name)