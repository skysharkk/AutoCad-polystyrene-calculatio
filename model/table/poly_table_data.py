from typing import List
from dataclasses import dataclass
from view.table_data import DataItem


@dataclass
class CellData:
    data: str
    text_height: float
    aline: str
    line_weight: str
    line_type: List[str]


@dataclass
class RowData:
    row_data: List[CellData]
    column_width: List[float]
    row_height: float


class PolyTableData:
    def __init__(self, scale: float, ui_table_data: List[DataItem]) -> None:
        self._ui_table_data = PolyTableData.convert_ui_data(ui_table_data)
        self._scale = scale
        self._column_sizes = [
            el / self._scale for el in [600, 2400, 2600, 400, 600, 800]]
        self._row_sizes = [el / self._scale for el in [600, 320]]
        self._initial_data: List[List[str]] = [
            ["Поз.", "Обозначение", "Наименование", "Кол.", "Объем ед. м\u00b3", "Примичание"],
            ["", "", "Плиты пенополистирольные", "", "", ""],
            *self._ui_table_data,
            ["", "", "Плиты минераловатные", "", "", ""],
            ["ПМ", "СТБ 1995", "ПТМ х ,у=125кг/м\u00b3,Lобщ.= м.п", "", "", ""],
            ["", "", "Длина стыков утеплителя", "", "", "м.п"]
        ]
        self._title_aline = [
            "acMiddleCenter",
            "acMiddleCenter",
            "acMiddleCenter",
            "acMiddleCenter",
            "acMiddleCenter",
            "acMiddleCenter"
        ]
        self._common_aline = [
            "acMiddleCenter",
            "acMiddleCenter",
            "acMiddleLeft",
            "acMiddleCenter",
            "acMiddleCenter",
            "acMiddleCenter"
        ]
        self._title_line_type = ["acVertLeft", "acVertRight", "acHorzBottom", "acHorzTop"]
        self._common_line_type = ["acVertLeft", "acVertRight"]
        self._last_item_line_type = ["acVertLeft", "acVertRight", "acHorzBottom"]
        self._table_data: List[RowData] = []
        self.rows_amount= None
        self.columns_amount = None

    @staticmethod
    def create_row(
        data: List[str],
        column_width: List[float],
        row_height: float,
        aline: List[str],
        line_weight: str,
        line_type: List[str],
        text_height: float
    ) -> RowData:
        row = []
        for index, el in enumerate(data):
            cell = CellData(el, text_height, aline[index], line_weight, line_type)
            row.append(cell)
        return RowData(row, column_width, row_height)

    @staticmethod
    def convert_ui_data(ui_table_data: List[DataItem]) -> List[List[str]]:
        res = []
        standard = {
            "Эффективный утеплитель λ ≤ 0,034 Вт/(м·°C)": "Эффективный утеплитель λ ≤ 0,034 Вт/(м·°C)",
            "ППТ-15-А-Р": "СТБ 1437"
        }
        poly_type = {
            "Эффективный утеплитель λ ≤ 0,034 Вт/(м·°C)": "",
            "ППТ-15-А-Р": "ППТ-15-А-Р "
        }
        for data_el in ui_table_data:
            res.append(
                [
                    data_el.pos,
                    standard[data_el.poly_type.decode()],
                    f"{poly_type[data_el.poly_type.decode()]}{data_el.width}x{data_el.height}x{data_el.depth},  м\u00b3",
                    data_el.amount,
                    data_el.volume,
                    data_el.note
                ]
            )
        return res

    def create_table_data(self) -> List[RowData]:
        for index, template_el in enumerate(self._initial_data):
            self._table_data.append(
                PolyTableData.create_row(
                    template_el,
                    self._column_sizes,
                    self._row_sizes[0] if index == 0 else self._row_sizes[1],
                    self._title_aline if index == 0 or index == 1 or index == len(
                        self._initial_data
                    ) - 3 else self._common_aline,
                    "acLnWt060",
                    self._title_line_type if index == 0 else self._last_item_line_type if index == len(
                        self._initial_data
                    ) - 1 else self._common_line_type,
                    108 / self._scale
                )
            )
        self.rows_amount = len(self._table_data)
        self.columns_amount = len(self._column_sizes)
        return self._table_data
