from view.table_data import DataItem
from typing import List
from dataclasses import dataclass


@dataclass
class Sizes:
    width: int
    height: int


def format_data_for_waste(data: List[DataItem]) -> dict:
    result = {}
    for data_item in data:
        poly_type = data_item.poly_type.decode()
        depth = data_item.depth
        if poly_type not in result:
            result[poly_type] = {}
        if depth not in result[poly_type]:
            result[poly_type][depth] = []
        for _ in range(int(data_item.amount)):
            result[poly_type][depth].append(
                Sizes(
                    int(data_item.width),
                    int(data_item.height)
                )
            )
    return result
