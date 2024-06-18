from src.utils.element_utils import Actions
from src.consts import TIMEOUT


class HomePage:
    __NAV_BAR = "#nav-bar-on-top"

    def __init__(self, actions: Actions):
        self.actions = actions

    def verify_home_page_loaded(self, timeout=TIMEOUT):
        self.actions.is_displayed(self.__NAV_BAR, timeout=timeout)
