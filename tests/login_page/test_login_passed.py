
from data.config_info import ConfigInfo
from src.utils import logger


def test_login_passed(pages):

    logger.info("Step 1: Login with valid username and password")
    pages.login_page.login(ConfigInfo.username, ConfigInfo.password)

    logger.info("verify login page is displayed")
    pages.home_page.verify_home_page_loaded()
