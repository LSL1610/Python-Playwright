from time import time, sleep
from loguru import logger
from locator import Shopee, Lazada, DemoBlaze, Food
import pytest

class TestVibing:
    @pytest.fixture(autouse=True)
    def setup(self, page):
        self.page = page

    def test_login_shopee_fail(self):
        try:
            self.page.goto(Shopee.DOMAIN)
            self.page.keyboard.down('Escape')
            self.page.get_by_text(text=Shopee.popup_language).click()
            
            self.page.get_by_placeholder(Shopee.usn).fill(value=Shopee.username)
            self.page.get_by_placeholder(Shopee.pw).fill(value=Shopee.passworld)
            self.page.get_by_role("button", name=Shopee.login_submit).click()
            login_stt = self.page.get_by_text(Shopee.login_vrf).is_visible()
            if not login_stt:
                raise Exception("Login Fail")
            
            logger.debug("Login Success")
        except Exception as e:
            logger.error(e)
        finally:
            self.page.close()

    def test_get_data_lazada(self):
        try:
            self.page.goto(Lazada.host_name)
            self.page.get_by_placeholder(Lazada.search_place).fill(Lazada.product_name)
            self.page.get_by_text(Lazada.search_btn).click()
            lst_name = self.page.get_attribute(self.page.locator(Lazada.lst_product), name='title')
            logger.debug(f'list product ==> {lst_name}')
                
        except Exception as e:
            logger.debug(e)

        finally:
            self.page.close()

    def add_cart_demoblaze(self):
        self.page.goto(DemoBlaze.DOMAIN)
        self.page.get_by_role("link", name="Log in").click()
        self.page.locator(DemoBlaze.login_usn).fill(DemoBlaze.username)
        self.page.locator(DemoBlaze.login_pw).fill(DemoBlaze.passworld)
        self.page.get_by_role("button", name=DemoBlaze.login_submit).click()
        lst = self.page.query_selector_all("//div[@class='col-lg-4 col-md-6 mb-4']")
        for loca in lst:
            try:
                with context.expect_page() as new_page_info:
                    loca.click(button='middle')
            
                new_page = new_page_info.value      
                new_page.wait_for_load_state()
                new_page.bring_to_front()
                new_page.get_by_text('Add to cart').click()
                new_page.press("body", "Enter")
                new_page.close()

            except Exception as e:
                print(e)

    def food_for_friend(self):
        with open('bubletea.txt', 'w', encoding='utf-8') as f:
            try:
                self.page.goto(Food.host_name)
                self.page.bring_to_front()
                self.page.get_by_placeholder(Food.search_ipt).fill(Food.product_name)
                self.page.locator(Food.search_btn).click()
                number_of_list = self.page.query_selector_all(Food.lst_product)
                logger.debug(f'number of page product is ==> {len(number_of_list) - 2}')
                for i in range(2, len(number_of_list) - 2):
                    self.page.locator(f'//*[@id="app"]/div/div[1]/ul/li[{i}]').click()
                    list_name = self.page.query_selector_all(Food.name_product)
                    for item in list_name:
                        brand = item.get_attribute('title')
                        logger.debug(brand)
                        f.write(brand + '\n')

            except Exception as e:
                logger.debug(e)

            finally:
                self.page.close()