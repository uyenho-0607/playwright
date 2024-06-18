import allure
import pytest_check
from src.utils import logger


# def test():
#     logger.info("Step 1")
#     pytest_check.equal(1, 1, "failed")
#     logger.info("Step 2")
#     pytest_check.equal(1, 2, "failed")
#     logger.info("Step 3")
#     pytest_check.equal(1, 3, "failed")
#
#     pytest_check.raises(AssertionError)
#


# Example test
@allure.feature("Feature 1")
@allure.story("Story 1")
def test_example():
    with allure.step("Step inside test"):
        assert True

