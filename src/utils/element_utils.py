import builtins
import time

import allure
import pytest_check
from playwright.sync_api import Page, expect

from data.logs import MsgLog
from data.project_info import ProjectInfo
from src.consts import TIMEOUT


def assertion_decorator(f):
    def wrapper(*args):

        page: Page = getattr(builtins, "list_page")[0]
        __tracebackhide__ = True

        f(*args)
        err_msg = args[-1]

        # log failures and status_details if anys
        if pytest_check.check_log.get_failures():

            MsgLog.failures.extend(pytest_check.check_log.get_failures())
            MsgLog.status_details.append(pytest_check.check_log.get_failures())

            # save failed verify steps
            if "verify" in MsgLog.msg_log[-1].lower():
                MsgLog.verify_log_failed.append((MsgLog.msg_log[-1], err_msg))

                # take screenshot if any failures
                if ProjectInfo.allure_dir:
                    allure.attach(
                        page.screenshot(),
                        name=f"{round(time.time(), 3)}_failed.png",
                        attachment_type=allure.attachment_type.PNG
                    )

            pytest_check.check_log.clear_failures()

    return wrapper


@assertion_decorator
def check_equal(*args):
    __tracebackhide__ = True
    pytest_check.equal(*args)


class Elements:
    def __init__(self, page: Page = None):
        self.page = page or getattr(builtins, "list_page")[0]


class Actions(Elements):

    def click(self, locator, timeout=TIMEOUT):
        self.page.click(locator, timeout=timeout)
        return self

    def fill(self, locator, value, timeout=TIMEOUT):
        self.page.fill(locator, value, timeout=timeout)
        return self

    def hover(self, locator, timeout=TIMEOUT):
        self.page.hover(locator, timeout=timeout)
        return self

    def is_displayed(self, locator, timeout=TIMEOUT):

        res = True
        try:
            expect(self.page.locator(locator)).to_be_visible(timeout=timeout)
        except AssertionError:
            res = False
        check_equal(res, True, f"Element with locator {locator} is not displayed")
        return self

    def is_enabled(self, locator, timeout=TIMEOUT):
        res = self.page.locator(locator).is_enabled(timeout=timeout)
        check_equal(res, True, f"Element with locator {locator} is not enabled")
        return self
