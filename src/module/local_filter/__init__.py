from src.utils.element_utils import Actions


class LocalFilterBase:
    def __init__(self, actions: Actions):
        self.actions = actions
