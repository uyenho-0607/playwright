
from src.pages.call_page import CallPage
from src.pages.home_page import HomePage
from src.pages.login_page import LoginPage
from src.utils.element_utils import Actions
import pytest


@pytest.fixture(scope="session")
def pages():
    actions = Actions()

    class PageContainer:
        login_page = LoginPage(actions)
        call_page = CallPage(actions)
        home_page = HomePage(actions)

    return PageContainer
