from projectutils import BinManager, Item
from typing import List, Callable
from .format_data_for_waste import Sizes
from projectutils import round_half_up


class Waste:
    def __init__(self, data: dict) -> None:
        self.data = data
        self.original_width = 2000
        self.original_height = 1000
        self.result = {}
        self._pack_objets()

    def _pack_objets(self) -> None:
        for poly_type in self.data.keys():
            self.result[poly_type] = {}
            for depth in self.data[poly_type].keys():
                self.result[poly_type][depth] = self._create_bins(
                    self.data[poly_type][depth])

    @staticmethod
    def _create_items(sizes: List[Sizes]) -> List[Item]:
        result = []
        for sizes_item in sizes:
            result.append(
                Item(
                    sizes_item.width,
                    sizes_item.height
                )
            )

        return result

    def _create_bins(self, sizes: List[Sizes]) -> list:
        manager = BinManager(
            self.original_width,
            self.original_height,
            pack_algo="guillotine",
            heuristic="best_shortside",
            rectangle_merge=True,
            rotation=True,
            split_heuristic="SplitMinimizeArea"
        )
        items = Waste._create_items(sizes)
        manager.add_items(*items)
        manager.execute()
        return manager.bins

    def calc_waste(self, overall_volume_func: Callable[..., dict]) -> dict:
        returnable = "returnable"
        non_returnable = "non_returnable"
        non_returnable_percent = "non_returnable_percent"
        overall_volume = overall_volume_func()
        waste_dict = {}
        for poly_type in self.result.keys():
            if poly_type not in waste_dict:
                waste_dict[poly_type] = {}
            waste_dict[poly_type][returnable] = 0
            waste_dict[poly_type][non_returnable] = 0
            for depth in self.result[poly_type].keys():
                for bins in self.result[poly_type][depth]:
                    for free_rect in bins.freerects:
                        volume = (free_rect.width / 1000) * (free_rect.height / 1000) * (int(depth) / 1000)

                        if free_rect.width < 100 or free_rect.height < 100:
                            waste_dict[poly_type][non_returnable] += volume
                        else:
                            waste_dict[poly_type][returnable] += volume
            volume_sum = (waste_dict[poly_type][returnable] + overall_volume[poly_type])
            waste_dict[poly_type][non_returnable_percent] = (100 * waste_dict[poly_type][non_returnable]) / volume_sum
        for poly_type in waste_dict.keys():
            for volume_type in waste_dict[poly_type].keys():
                waste_dict[poly_type][volume_type] = round_half_up(
                    waste_dict[poly_type][volume_type],
                    2,
                    False
                )
        return waste_dict
