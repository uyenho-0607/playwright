
from src.pages.login_page import LoginPage
from src.pages.note_page import NotePage
from src.utils.element_utils import Actions
import pytest


@pytest.fixture(scope="session")
def pages():
    actions = Actions()

    class PageContainer:
        login_page = LoginPage(actions)
        note_page = NotePage(actions)

    return PageContainer
