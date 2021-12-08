from __future__ import annotations
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING
from .row import Row
from observer import Subject, Observer

if TYPE_CHECKING:
    from view.table_data import TableData


@dataclass
class ChangedItem:
    row: int
    column: int
    new_data: str


class TableWidget(Subject):
    table_data: List[Row]

    def __init__(self, table_widget: QTableWidget):
        self.table_widget = table_widget
        self.table_data = []
        self.table_widget.horizontalHeader().setStretchLastSection(True)
        self.table_widget.itemChanged.connect(self.get_changed_item)
        self._observers: List[Observer] = []
        self.changed_item_data: Union[None, ChangedItem] = None

    def insert_row(self, row_data: List[str], row_index: int, disabled_cells: List[int]) -> None:
        self.table_widget.insertRow(len(self.table_data))
        row = Row(row_index, self.table_widget)
        row.set_data_to_row(row_data)
        self.table_data.append(row)
        self.table_widget.resizeColumnsToContents()
        for disabled_cell_pos in disabled_cells:
            row.disable_cell(disabled_cell_pos)

    def import_data(self, table_data: TableData) -> None:
        self._clear_table()
        data = table_data.data_to_list()
        for data_index, data_el in enumerate(data):
            self.insert_row(data_el, data_index, table_data.get_data()[data_index].disabled_cells)

    def change_cell_value(self, row_index: int, column_index: int, value: str):
        self.table_data[row_index].change_cell_value(column_index, value)

    def get_current_row(self) -> int:
        return self.table_widget.currentRow()

    def get_current_item(self) -> QTableWidgetItem:
        return self.table_widget.currentItem()

    def remove_row(self) -> int:
        current_row = self.get_current_row()
        self.table_widget.removeRow(current_row)
        self.table_widget.resizeColumnsToContents()
        return current_row

    def _clear_table(self) -> None:
        while self.table_widget.rowCount() > 0:
            self.table_widget.removeRow(0)
        self.table_data.clear()

    def get_changed_item(self):
        current_item = self.get_current_item()
        if current_item:
            self.changed_item_data = ChangedItem(
                current_item.row(),
                current_item.column(),
                current_item.text()
            )
            self.notify()

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
