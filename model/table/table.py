from comtypes.client import Constants
from pyautocad import Autocad
from typing import List, Union
from model.table.poly_table_data import RowData, PolyTableData
from view.table_data import DataItem, TableData


class Table:
    def __init__(self, acad: Autocad, scale: float, initial_point) -> None:
        self.scale = scale
        self._acad = acad
        self._constants = Constants(self._acad.app)
        self._ms = self._acad.doc.ModelSpace
        self._table = None
        self.initial_point = initial_point

    def _get_constant(self, attr: Union[str, List[str]]) -> int:
        res = 0
        if type(attr) == list:
            for el in attr:
                res += getattr(self._constants, el)
        else:
            res += getattr(self._constants, attr)
        return res

    def _update_table(self, data: List[RowData]):
        for row_index, row_el in enumerate(data):
            self._table.SetRowHeight(row_index, row_el.row_height)
            if row_index == 0:
                for index, col_size in enumerate(row_el.column_width):
                    self._table.SetColumnWidth(index, col_size)
            for cell_index, cell_el in enumerate(row_el.row_data):
                self._table.SetTextHeight2(
                    row_index, cell_index, 1, cell_el.text_height)
                self._table.SetCellAlignment(
                    row_index, cell_index, self._get_constant(cell_el.aline))
                self._table.SetGridLineWeight2(
                    row_index,
                    cell_index,
                    self._get_constant(cell_el.line_type),
                    self._get_constant(cell_el.line_weight)
                )
                self._table.SetText(row_index, cell_index, cell_el.data)

    def draw_table(self, data: TableData) -> None:
        converted_data = PolyTableData(self.scale, data).create_table_data()
        if self._table:
            self._table.Delete()
            self._table = None
        column_amount = len(converted_data[0].row_data)
        row_amount = len(converted_data)
        self._table = self._ms.AddTable(
            self.initial_point,
            row_amount + 1,
            column_amount,
            1,
            1
        )
        self._table.DeleteRows(0, 1)
        self._table.VertCellMargin = 0
        self._table.HorzCellMargin = 100 / self.scale
        self._update_table(converted_data)
