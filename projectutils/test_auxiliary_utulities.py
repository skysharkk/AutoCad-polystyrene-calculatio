from .auxiliary_utulities import round_half_up, get_corner_coordinates, Points, get_rectangle_sizes, \
    compare_list_or_tuple, create_array_of_double, two_dimension_list_to_list
import pytest
from array import array

coordinates_tuples = [
    (4624.191812087005, 2906.176533298964, 4674.191812087005, 2906.176533298964, 4674.191812087005,
     2890.676533298964,
     4624.191812087005, 2890.676533298964),
    (4574.191812087005, 2890.676533298964, 4524.191812087005, 2890.676533298964, 4524.191812087005, 2865.676533298964,
     4574.191812087005, 2865.676533298964),
    (4512.197349122538, 2890.676533298964, 4524.191812087005, 2890.676533298964, 4524.191812087005, 2865.676533298964,
     4512.197349122538, 2865.676533298964),
    (4488.860024132563, 2957.655998805511, 4506.235710559515, 2957.655998805511, 4506.235710559515, 2946.310342917864,
     4498.248499364086, 2946.310342917864, 4472.325094064036, 2946.310342917864, 4472.325094064036, 2957.655998805511,
     4488.860024132563, 2957.655998805511)
]

corner_coordinates_results = [
    Points(4624.191812087005, 4674.191812087005, 2890.676533298964, 2906.176533298964),
    Points(4524.191812087005, 4574.191812087005, 2865.676533298964, 2890.676533298964),
    Points(4512.197349122538, 4524.191812087005, 2865.676533298964, 2890.676533298964),
    Points(4472.325094064036, 4506.235710559515, 2946.310342917864, 2957.655998805511)
]

rectangle_sizes_results = [
    (2000, 620),
    (2000, 1000),
    (480, 1000),
    (1356, 454)
]


def create_params(param, results):
    return list(zip(param, results))


# test round_half_up function


def test_get_int():
    assert round_half_up(2.17) == 2
    assert round_half_up(2.5) == 3


def test_get_float():
    assert round_half_up(2.17, 1, False) == 2.2
    assert round_half_up(2.55, 1, False) == 2.6


def test_incorrect_params():
    with pytest.raises(ValueError):
        round_half_up(2.17, 1)


# test get_corner_coordinates function


@pytest.mark.parametrize("coordinates_tuple, result", create_params(coordinates_tuples, corner_coordinates_results))
def test_get_corner_coordinates(coordinates_tuple, result):
    assert get_corner_coordinates(coordinates_tuple) == result


# test get_rectangle_sizes function


@pytest.mark.parametrize("coordinates_tuple, result", create_params(coordinates_tuples, rectangle_sizes_results))
def test_get_rectangle_sizes(coordinates_tuple, result):
    scale = 40
    assert get_rectangle_sizes(coordinates_tuple, scale) == result


# test compare_list_or_tuple function

def test_compare_list_or_tuple():
    assert compare_list_or_tuple([1, 2, 3], [4, 5, 6]) is False
    assert compare_list_or_tuple([1, 2, 3], [1, 2, 3]) is True


def test_create_array_of_double():
    assert create_array_of_double([1, 2, 3]) == array("d", [1, 2, 3])


def test_two_dimension_list_to_list():
    assert two_dimension_list_to_list([[1, 2], [3, 4]]) == [1, 2, 3, 4]
