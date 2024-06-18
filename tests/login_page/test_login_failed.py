from data.config_info import ConfigInfo
from src.utils import logger


def test_login_failed(pages):

    logger.info("Step 1: Login with invalid username and password")
    pages.login_page.login("hihi_haha", ConfigInfo.password)

    logger.info("verify home page is displayed")
    pages.home_page.verify_home_page_loaded()
