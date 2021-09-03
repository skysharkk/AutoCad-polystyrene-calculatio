from typing import Tuple

from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem


class TreeWidget:
    def __init__(self, tree_widget: QTreeWidget):
        self.tree_widget = tree_widget
        self.el_list = []

    def is_exist(self, characteristic: Tuple[int, str]) -> bool:
        for el in self.el_list:
            if el == characteristic:
                return True
        return False

    def add_element(self, thickness: int, poly_type: str) -> None:
        char = (thickness, poly_type)
        if not self.is_exist(char):
            self.el_list.append(char)
            widget_item = QTreeWidgetItem(self.tree_widget)
            widget_item.setText(0, str(thickness))
            widget_item.setText(1, poly_type)

    def get_selected_item(self) -> Tuple[int, Tuple[int, str]]:
        item = self.tree_widget.currentItem()
        index = self.tree_widget.indexOfTopLevelItem(item)
        print(index, self.el_list[index])
        return index, self.el_list[index]

    def delete_selected_widget_item(self) -> bool:
        if len(self.el_list) > 0:
            item_index = self.get_selected_item()[0]
            self.el_list.pop(item_index)
            self.tree_widget.takeTopLevelItem(item_index)
            return True
        return False
