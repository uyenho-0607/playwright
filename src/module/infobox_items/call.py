
from src.module.infobox_items import InfoboxItemBase


class InfoboxItems(InfoboxItemBase):

    def click_item(self, title):
        super()._click_item(title, item_type="calls")

    def click_create_obj_btn(self):
        super()._click_create_obj_btn("note")

    def verify_panel_is_opened(self):
        super()._verify_panel_opened(text="Calls")

