import builtins

import pytest

from data.config_info import ConfigInfo
from data.logs import MsgLog
from data.project_info import ProjectInfo
from src.utils import load_config, setup_logging, logger
from src.utils.allure_utils import modified_allure_report, log_step_to_allure
from src.utils.browser_utils import init_browser


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="staging")
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--user", action="store", default="")
    parser.addoption("--password", action="store", default="")
    parser.addoption("--headless", action="store_true", default=False)


def pytest_sessionstart(session):
    option = vars(session.config.option)
    setup_logging()

    logger.info(" ======== Pytest Session Started ======== ")
    load_config(option["env"])

    logger.info(f"------ Init {option["browser"]} browser -------- ")
    browser = init_browser(option["browser"], headless=option["headless"])
    page = browser.new_context().new_page()
    setattr(builtins, "list_page", [page])
    setattr(builtins, "browser", browser)
    ProjectInfo.allure_dir = session.config.option.allure_report_dir

    logger.info("- Navigating to application page....")
    page = getattr(builtins, "list_page")[0]
    page.goto(ConfigInfo.url)


def pytest_sessionfinish(session):
    if not ProjectInfo.allure_dir:
        return

    modified_allure_report()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    MsgLog.failures = []
    test_name = item.name
    package = item.location[0].split("/", 1)[-1]
    logger.info(f"- Executing test case: {test_name}, from package: {package}")

    location, *_ = item.location
    ProjectInfo.test_name = test_name


def pytest_runtest_teardown(item):
    MsgLog.verify_log_failed.append("end test")
    # logger.info(f"- Tear down of test case {item.name}")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Check if the report is from the 'call' phase
    if report.when == "call":
        log_step_to_allure()

        if MsgLog.failures:
            report.outcome = "failed"
            report.longrepr = "\n".join(MsgLog.failures)

            del MsgLog.failures[:]
