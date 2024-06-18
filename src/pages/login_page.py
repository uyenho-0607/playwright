from src.utils.element_utils import Actions
from src.consts import TIMEOUT


class LoginPage:
    __USERNAME_TXT = "input#login-form-username"
    __PASSWORD = "#txtPassword"
    __SIGNIN_BTN = ".btn-default.btn-cta"
    __WELCOME_TEXT = ".welcome-text"

    def __init__(self, actions: Actions):
        self.actions = actions

    def login(self, username, password):
        (
            self.actions
            .fill(self.__USERNAME_TXT, username)
            .fill(self.__PASSWORD, password)
            .click(self.__SIGNIN_BTN)
        )
