from typing import List, Any, Union

from PyQt5 import QtWidgets

from .cell import Cell


class Row:
    row_cells: List[Cell]
    row_data: List[Any]

    def __init__(self, row_index: int, table: QtWidgets.QTableWidget):
        self.row_index = row_index
        self.table = table
        self.row_cells = []

    def set_data_to_row(self, row_data: List[Any]) -> None:
        self.row_data = row_data
        for column_index, cell_data in enumerate(self.row_data):
            cell = Cell(self.table, (self.row_index, column_index))
            self.row_cells.append(cell)
            cell.set_data_to_cell(cell_data)

    def compare_rows(self, compared_row: List[Cell]) -> bool:
        for cell_index, cell in enumerate(self.row_cells):
            if not compared_row[cell_index].data == cell.data:
                return False
        return True

    def change_cell_value(self, cell_index: int, value: str):
        self.row_cells[cell_index].set_data_to_cell(value)
