from pages.excel_reader import read_excel
from locator import Paralle as pr
from pages.login_page import LoginPage
from pathlib import Path
from loguru import logger


CURDIR = Path.cwd()

data = read_excel()

def test_login(NormalBrowser):
    logger.debug(CURDIR)
    NormalBrowser.goto(pr.host_name)
    
    login = LoginPage(NormalBrowser)
    login.login_return_stt()