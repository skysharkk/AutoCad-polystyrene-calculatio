from typing import Tuple, Callable, List
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem


class TreeWidget:
    el_list: List[Tuple[int, str]]

    def __init__(self, tree_widget: QTreeWidget):
        self.tree_widget = tree_widget
        self.el_list = []

    def is_exist(self, characteristic: Tuple[int, str]) -> bool:
        for el in self.el_list:
            if el == characteristic:
                return True
        return False

    def add_element(self, width: int, poly_type: str) -> None:
        char = (width, poly_type.encode("utf-8"))
        if not self.is_exist(char):
            self.el_list.append(char)
            widget_item = QTreeWidgetItem(self.tree_widget)
            widget_item.setText(0, str(width))
            widget_item.setText(1, poly_type)

    def get_selected_item(self) -> Tuple[int, Tuple[int, str]]:
        item = self.tree_widget.currentItem()
        index = self.tree_widget.indexOfTopLevelItem(item)
        return index, self.el_list[index]

    def delete_selected_widget_item(self) -> bool:
        if len(self.el_list) > 0:
            item_index = self.get_selected_item()[0]
            self.el_list.pop(item_index)
            self.tree_widget.takeTopLevelItem(item_index)
            return True
        return False

    def connect_clicked_event(self, func: Callable[..., None]) -> None:
        self.tree_widget.itemClicked.connect(func)

    def is_empty(self) -> bool:
        if len(self.el_list) > 0:
            return False
        return True
