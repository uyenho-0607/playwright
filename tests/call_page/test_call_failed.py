import builtins
import time

import allure
import pytest_check as check
import pytest_check.check_log
from playwright.sync_api import Page

from data.logs import MsgLog
from data.project_info import ProjectInfo
from src.utils import logger


def decorator(f):
    def wrap(*args):
        page: Page = getattr(builtins, "list_page")[0]
        err_msg = args[-1]

        __tracebackhide__ = True
        f(*args)

        MsgLog.failures.extend(pytest_check.check_log.get_failures())
        MsgLog.status_details.append(pytest_check.check_log.get_failures())

        if pytest_check.check_log.any_failures():
            if "verify" in MsgLog.msg_log[-1].lower():
                MsgLog.verify_log_failed.append((MsgLog.msg_log[-1], err_msg))

                if ProjectInfo.allure_dir:
                    allure.attach(
                        page.screenshot(),
                        name=f"{round(time.time(), 3)}_failed.png",
                        attachment_type=allure.attachment_type.PNG
                    )

            pytest_check.check_log.clear_failures()

    return wrap


@decorator
def check_equal(*args):
    __tracebackhide__ = True
    check.equal(*args)


def check_func_1():
    logger.info("- Verify func_1")
    check_equal(1, 2, "failed")


def check_func_2():
    logger.info("- Verify func_2")
    check_equal(1, 14, "failed")


def check_func_3():
    logger.info("- verify func_3")
    check_equal(1, 1, "failed")


def test_1():
    logger.info("Step 1")

    logger.info("Step 2")
    check_func_1()
    check_func_3()

    logger.info("Step 3")
    check_func_2()


def test_2():
    logger.info("Step 1")

    logger.info("Step 2")
    check_func_1()
    check_func_2()
