from pages.login_page import LoginPage

def test_login_pass(MultipleBrowsers):
    MultipleBrowsers.goto("https://www.saucedemo.com")

    login_page = LoginPage(MultipleBrowsers)
    login_page.login("standard_user", "secret_sauce")
    
    assert "inventory" in MultipleBrowsers.url
    
def test_login_fail(MultipleBrowsers):
    MultipleBrowsers.goto("https://www.saucedemo.com")

    login_page = LoginPage(MultipleBrowsers)
    login_page.login("standard_user", "wrong_password")

    assert "inventory" in MultipleBrowsers.url