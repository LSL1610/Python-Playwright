from playwright.sync_api import sync_playwright
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from time import time, sleep
from loguru import logger

host_name = 'https://shopeefood.vn/'
product_name = 'su kem'

@logger.catch()
def get_some_food_info(host_name, product_name):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,
                                    channel='chrome',
                                    ignore_default_args=['--mute-audio'],
                                    timeout=80000,)
        
        context = browser.new_context()
        context.set_default_timeout(30000)
        context.set_default_navigation_timeout(60000)
        
        page = context.new_page()
        with open('bubletea.txt', 'w', encoding='utf-8') as f:
            try:
                page.goto(host_name)
                page.bring_to_front()
                page.get_by_placeholder('Tìm địa điểm, món ăn, địa chỉ...').fill(product_name)
                page.locator("a > .btn").click()
                sleep(5)
                number_of_list = page.query_selector_all('//*[@id="app"]/div/div[1]/ul/li')
                logger.debug(f'number of page product is ==> {len(number_of_list) - 2}')
                for i in range(2, len(number_of_list) - 2):
                    page.locator(f'//*[@id="app"]/div/div[1]/ul/li[{i}]').click()
                    sleep(3)
                    list_name = page.query_selector_all('//*[@id="app"]/div/div[1]/div[2]/div/div/a/div/div/h4')
                    for item in list_name:
                        brand = item.get_attribute('title')
                        logger.debug(brand)
                        f.write(brand + '\n')
                page.close()
            except Exception as e:
                logger.debug(e)
        
get_some_food_info(host_name, product_name)