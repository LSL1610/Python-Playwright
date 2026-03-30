from playwright.sync_api import Page
import time

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = "#user-name"
        self.password = "#password"
        self.login_btn = "#login-button"

    def login(self, user, pwd):
        self.page.fill(self.username, user)
        self.page.fill(self.password, pwd)
        self.page.click(self.login_btn)
        time.sleep(10)
    
    def getallatt(self, locator, att):
        content = self.page.get_attribute(locator, att)
        return content
        