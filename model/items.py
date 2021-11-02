from .item import Item
from typing import List


class Items:

    def __init__(self, acad_items) -> None:
        self._acad_items = acad_items
        self._items: List[Item] = []
        self._convert_acad_items()

    def _convert_acad_items(self) -> None:
        for index in range(self._acad_items.Count):
            el = self._acad_items.Item(index)
            self._items.append(Item(el))

    @property
    def get_items(self):
        return self._items
