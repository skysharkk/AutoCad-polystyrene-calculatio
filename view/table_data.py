from __future__ import annotations
from collections import namedtuple
from typing import List, TYPE_CHECKING, Tuple, Union
from observer import Observer
from projectutils import round_half_up
from dataclasses import dataclass
from projectutils import get_corner_coordinates
from projectutils import Points
from projectutils.auxiliary_utulities import show_error_window
from enum import Enum

if TYPE_CHECKING:
    from .initial_data import Data
    from .components.table import TableWidget

Sizes = namedtuple("Sizes", ["width", "height"])


class DataItemPos(Enum):
    pos = 0
    poly_type = 1
    width = 2
    height = 3
    depth = 4
    amount = 5
    volume = 6
    note = 7


@dataclass
class DataItem:
    pos: str
    poly_type: bytes
    width: str
    height: str
    depth: str
    amount: str
    volume: str
    note: str
    disabled_cells: List[int]
    coordinates: Union[List[Tuple[float, ...]], None]

    def increase_amount(self):
        self.amount = str(int(self.amount) + 1)

    def data_to_list(self) -> List[str]:
        return [
            self.pos,
            self.poly_type,
            self.width,
            self.height,
            self.depth,
            self.amount,
            self.volume,
            self.note
        ]

    def get_sizes(self) -> List[str]:
        return [self.width, self.height, self.depth]


class TableData(Observer):
    def __init__(self):
        self._data: List[DataItem] = []
        self._overall_volume = {}

    def get_data(self):
        return self._data

    def get_overall_volume(self):
        return self._overall_volume

    @staticmethod
    def _calc_sizes(scale: float, coordinates: Points) -> Sizes:
        return Sizes(
            int(abs(coordinates.max_x - coordinates.min_x) * scale),
            int(abs(coordinates.max_y - coordinates.min_y) * scale)
        )

    @staticmethod
    def _calc_volume(width: int, height: int, depth: int) -> float:
        return round_half_up((width / 1000) * (height / 1000) * (depth / 1000), 2, False)

    def _coordinates_is_exist(self, item_coordinates: Tuple[float, ...]) -> bool:
        for el in self._data:
            for coord in el.coordinates:
                if item_coordinates == coord:
                    return True
        return False

    def _increase_amount_if_exist(self, item: DataItem) -> bool:
        for el in self._data:
            first_item_sizes = el.get_sizes()
            second_item_sizes = item.get_sizes()
            first_item_sizes.sort()
            second_item_sizes.sort()
            if el.poly_type == item.poly_type and first_item_sizes == second_item_sizes:
                el.increase_amount()
                el.coordinates.append(item.coordinates[0])
                return True
        return False

    def update_data(self, acad_data: Data) -> None:
        for item in acad_data.coordinates:
            sizes = TableData._calc_sizes(
                acad_data.scale,
                get_corner_coordinates(item.coordinates)
            )
            data_item = DataItem(
                str(len(self._data) + 1),
                acad_data.poly_type.encode("utf-8"),
                str(sizes.width),
                str(sizes.height),
                str(int(acad_data.depth)),
                str(1),
                str(TableData._calc_volume(
                    sizes.width, sizes.height, acad_data.depth)),
                "",
                [1],
                [item.coordinates]
            )
            if not self._coordinates_is_exist(data_item.coordinates[0]):
                if len(self._data) == 0 or not self._increase_amount_if_exist(data_item):
                    self._data.append(data_item)

    def import_data_from_list(self, data: List[List[str]]) -> None:
        if len(self._data) == 0:
            for data_el in data:
                self._data.append(
                    DataItem(
                        *data_el,
                        coordinates=None
                    )
                )
        else:
            show_error_window("Очистите таблицу")

    def data_to_list(self) -> List[List[str]]:
        res = []
        for item in self._data:
            res.append(item.data_to_list())
        return res

    def _update_pos(self) -> None:
        for index, item in enumerate(self._data):
            item.pos = str(index + 1)

    def remove_item(self, pos: int) -> None:
        self._data.pop(pos)
        self._update_pos()

    def calc_overall_volume(self) -> dict:
        overall_volume = {}
        for item in self._data:
            if item.poly_type.decode() not in overall_volume:
                overall_volume[item.poly_type.decode()] = 0
            overall_volume[item.poly_type.decode()] = round_half_up(
                overall_volume[item.poly_type.decode()] + (float(item.volume) * (float(item.amount))),
                2,
                False
            )
        return overall_volume

    def update(self, subject: TableWidget) -> None:
        item = self._data[subject.changed_item_data.row]
        prop_name = DataItemPos(subject.changed_item_data.column).name
        if prop_name == "poly_type":
            new_data = subject.changed_item_data.new_data.encode()
        else:
            new_data = subject.changed_item_data.new_data
        setattr(item, prop_name, new_data)
