from __future__ import annotations
from collections import namedtuple
from typing import List, TYPE_CHECKING, Tuple
from projectutils import round_half_up
from dataclasses import dataclass

if TYPE_CHECKING:
    from .initial_data import Data

RecCoordinates = namedtuple(
    "RecCoordinates", ["max_x", "min_x", "max_y", "min_y"])
Sizes = namedtuple("Sizes", ["width", "height"])


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
    coordinates: List[Tuple[float, ...]]

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


class TableData:
    def __init__(self):
        self._data: List[DataItem] = []

    @property
    def data(self):
        return self._data

    @staticmethod
    def _calc_sizes(scale: float, coordinates: RecCoordinates) -> Sizes:
        return Sizes(
            int(abs(coordinates.max_x - coordinates.min_x) * scale),
            int(abs(coordinates.max_y - coordinates.min_y) * scale)
        )

    @staticmethod
    def _calc_volume(width: int, height: int, depth: int) -> float:
        return round_half_up((width / 1000) * (height / 1000) * (depth / 1000), 2, False)

    @staticmethod
    def _transform_coordinates(coordinates: Tuple[float, ...]) -> RecCoordinates:
        x_coordinates = []
        y_coordinates = []
        for index, item in enumerate(coordinates):
            if index % 2 == 0:
                x_coordinates.append(item)
            else:
                y_coordinates.append(item)
        return RecCoordinates(
            max(x_coordinates),
            min(x_coordinates),
            max(y_coordinates),
            min(y_coordinates)
        )

    def _coordinates_is_exist(self, item_coordinates: Tuple[float, ...]) -> bool:
        for el in self._data:
            for coord in el.coordinates:
                if item_coordinates == coord:
                    return True
        return False

    def _increase_amount_if_exist(self, item: DataItem) -> bool:
        pos_index = 0
        amount_index = 5
        for el in self._data:
            first_item = el.data_to_list()
            second_item = item.data_to_list()
            first_item.pop(amount_index)
            first_item.pop(pos_index)
            second_item.pop(amount_index)
            second_item.pop(pos_index)
            first_item.sort()
            second_item.sort()
            if first_item == second_item:
                el.increase_amount()
                el.coordinates.append(item.coordinates[0])
                return True
        return False

    def update_data(self, acad_data: Data) -> None:
        for item in acad_data.coordinates:
            sizes = TableData._calc_sizes(
                acad_data.scale,
                TableData._transform_coordinates(item.coordinates)
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
                [item.coordinates]
            )
            if not self._coordinates_is_exist(data_item.coordinates[0]):
                if len(self._data) == 0 or not self._increase_amount_if_exist(data_item):
                    self._data.append(data_item)

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
