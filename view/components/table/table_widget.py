from PyQt6.QtWidgets import QTableWidget
from typing import List

from .row import Row


class TableWidget:
    table_data: List[Row]

    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget
        self.table_data = []
        self.table_widget.horizontalHeader().setStretchLastSection(True)

    def insert_row(self, row_data: List[str], row_index: int) -> None:
        self.table_widget.insertRow(len(self.table_data))
        row = Row(row_index, self.table_widget)
        row.set_data_to_row(row_data)
        self.table_data.append(row)
        self.table_widget.resizeColumnsToContents()

    def import_data(self, data: List[List[str]]) -> None:
        for data_index, data_el in enumerate(data):
            self.insert_row(data_el, data_index)

    def change_cell_value(self, row_index: int, column_index: int, value: str):
        self.table_data[row_index].change_cell_value(column_index, value)

    def get_current_row(self):
        return self.table_widget.currentRow()

    def remove_row(self) -> None:
        self.table_widget.removeRow(self.get_current_row())
        self.table_widget.resizeColumnsToContents()
