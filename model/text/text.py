from pyautocad import Autocad
from view.table_data import DataItem
from .text_item import TextItem
from typing import List
from view.table_data import DataItem


class Text:
    def __init__(self, acad: Autocad) -> None:
        self.acad = acad
        self.text_items: List[TextItem] = []

    def inscribe_text_items(self, data_items: List[DataItem], scale: float) -> None:
        text_height = 120 / scale
        text_width = 360 / scale
        for data_item in data_items:
            for coordinate in data_item.coordinates:
                text_item = TextItem(
                    self.acad, data_item.pos, text_height, text_width)
                text_item.inscribe_text(coordinate)
