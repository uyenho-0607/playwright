
from src.module.infobox_items import InfoboxItemBase


class InfoboxItems(InfoboxItemBase):
    __ADD_NEW_OBJ_BTN = "//div[contains(@class, 'add-new-btn') and ./ancestor::todo-box]"

    def click_item(self, title):
        super()._click_item(title, item_type="todo")

    def click_add_new_btn(self):
        self.actions.click(self.__ADD_NEW_OBJ_BTN)

    def verify_panel_is_opened(self):
        super()._verify_panel_opened(text="ToDo\'s")
