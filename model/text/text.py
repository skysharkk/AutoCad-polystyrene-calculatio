from dataclasses import dataclass
from pyautocad import Autocad
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
            if data_item.coordinates:
                for coordinate in data_item.coordinates:
                    text_item = TextItem(
                        self.acad, data_item.pos, text_height, text_width)
                    text_item.inscribe_text(coordinate)
                    self.text_items.append(text_item)

    def clear(self) -> None:
        for item in self.text_items:
            try:
                item.acad_text.Delete()
            except Exception:
                print("Text is not exist")
        self.text_items = []

    def detach_text(self):
        self.text_items.clear()
