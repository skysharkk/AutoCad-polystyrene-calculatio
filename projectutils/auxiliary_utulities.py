import math
import ctypes
from array import array
from typing import Union, NamedTuple, List, Tuple, Any, NoReturn


def round_half_up(number: float, decimals: int = 0, int_result: bool = True) -> Union[int, float]:
    if int_result and decimals > 0:
        raise ValueError
    multiplier = 10 ** decimals
    result = math.floor(number * multiplier + 0.5) / multiplier
    if int_result:
        return int(result)
    else:
        return result


class Points(NamedTuple):
    min_x: float
    max_x: float
    min_y: float
    max_y: float


def get_corner_coordinates(coordinates_tuple: Tuple[float, ...]) -> Points:
    x_coordinates_list: List[float] = []
    y_coordinates_list: List[float] = []
    for index in range(len(coordinates_tuple)):
        if index % 2 == 0:
            x_coordinates_list.append(coordinates_tuple[index])
        else:
            y_coordinates_list.append(coordinates_tuple[index])
    max_x: float = max(x_coordinates_list)
    min_x: float = min(x_coordinates_list)
    max_y: float = max(y_coordinates_list)
    min_y: float = min(y_coordinates_list)
    return Points(min_x, max_x, min_y, max_y)


def get_rectangle_sizes(coordinates_tuple: Tuple[float, ...], scale: float) -> Tuple[float, float]:
    coordinates: Points = get_corner_coordinates(coordinates_tuple)
    width: float = abs(round_half_up(
        (coordinates.max_x - coordinates.min_x) * scale))
    height: float = abs(round_half_up(
        (coordinates.max_y - coordinates.min_y) * scale))
    return width, height


def compare_list_or_tuple(first_list: Union[List[Any], Tuple[Any]],
                          second_list: Union[List[Any], Tuple[Any]]) -> bool:
    return set(first_list) == set(second_list)


def is_elem_exist_in_collection(elem: Any, collection: Union[List[Any], Tuple[Any]]) -> bool:
    for item in collection:
        if compare_list_or_tuple(item.coord, elem):
            return True
    return False


def show_error_window(error_message: str, window_name: str = u"Ошибка") -> NoReturn:
    ctypes.windll.user32.MessageBoxW(
        0, error_message, window_name, 0)


def create_array_of_double(converted_list: List[Any]) -> array:
    return array("d", converted_list)


def two_dimension_list_to_list(converted_list: List[Any]) -> List[Any]:
    formatted_list = []
    for item in converted_list:
        formatted_list.extend(item)
    return formatted_list
