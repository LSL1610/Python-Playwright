import pytest 
from pages.login_page import LoginPage
from locator import Paralle as pr

# @pytest.mark.skip("No Run")
def test_login_pass(MultipleBrowsers):
    MultipleBrowsers.goto(pr.host_name)

    login_page = LoginPage(MultipleBrowsers)
    login_page.login(pr.username_true, pr.pw_true)
    
    assert "inventory" in MultipleBrowsers.url
 
# @pytest.mark.skip("No Run")
def test_login_fail(MultipleBrowsers):
    MultipleBrowsers.goto(pr.host_name)

    login_page = LoginPage(MultipleBrowsers)
    login_page.login(pr.username_true, pr.pw_false)

    assert "inventory" in MultipleBrowsers.url
    
def test_get_all_username(MultipleBrowsers):
    MultipleBrowsers.goto(pr.host_name)
    
    login_page = LoginPage(MultipleBrowsers)
    lst_usename = login_page.getallatt(locator="#login_credentials",
                                       att="textContent")
    print(lst_usename)