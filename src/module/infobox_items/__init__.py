from src.utils.common_utils import cook_element
from src.utils.element_utils import Actions


class InfoboxItemBase:
    __ITEM_TITLE = "//span[text()='{}' and ./ancestor::{}-box]"
    __CREATE_OBJ_BTN = "//div[contains(@class, 'create-object-btn') and ./ancestor::{}-box]"
    __VIEW_TITLE_TXT = ('//div[contains(@class, "view-title-wrapper")]//span[contains(@class, "view-title") '
                        'and text()[normalize-space()="{}"]]')

    def __init__(self, actions: Actions):
        self.__actions = actions

    def _click_item(self, title, item_type):
        self.__actions.click(cook_element(self.__ITEM_TITLE, title, item_type))

    def _click_create_obj_btn(self, item_type):
        self.__actions.click(cook_element(self.__CREATE_OBJ_BTN, item_type))

    def _verify_panel_opened(self, text):
        self.__actions.is_displayed(cook_element(self.__VIEW_TITLE_TXT, text))
