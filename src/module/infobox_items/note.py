
from src.module.infobox_items import InfoboxItemBase


class InfoboxItems(InfoboxItemBase):

    def __init__(self, actions):
        super().__init__(actions)

    def click_item(self, title):
        super()._click_item(title, item_type="note")

    def click_create_obj_btn(self):
        super()._click_create_obj_btn("note")

    def verify_panel_is_opened(self):
        super()._verify_panel_opened(text="Notes")


