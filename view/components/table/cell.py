from typing import Union, Tuple

from PyQt5 import QtWidgets, QtCore

from collections import namedtuple

Position = namedtuple("Position", ["row", "column"])


class Cell:
    data: Union[None, str]
    item: Union[None, QtWidgets.QTableWidgetItem]
    position: Position

    def __init__(self, table: QtWidgets.QTableWidget, position: Tuple[int, int]):
        self.table = table
        self.data = None
        self.item = None
        self.position = Position(position[0], position[1])

    def create_cell_item(self) -> None:
        self.item = QtWidgets.QTableWidgetItem(str(self.data))

    def set_data_to_cell(self, data: Union[str, bytes]) -> None:
        self.data = data.decode() if type(data) == bytes else data
        self.create_cell_item()
        self.table.setItem(self.position.row, self.position.column, self.item)
        self.item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
