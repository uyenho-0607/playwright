from src.module.infobox_filter.note import InfoboxFilter
from src.module.infobox_items.note import InfoboxItems
from src.module.local_filter.note import LocalFilter
from src.module.settings.note import Settings
from src.module.workspace.note import Workspace


class NotePage:

    def __init__(self, actions):
        self.__actions = actions
        self.infobox_items = InfoboxItems(self.__actions)
        self.infobox_filter = InfoboxFilter(self.__actions)
        self.settings = Settings(self.__actions)
        self.workspace = Workspace(self.__actions)
        self.local_filter = LocalFilter(self.__actions)

