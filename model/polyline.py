from typing import Any
from array import array


class Polyline:
    def __init__(self, ms: Any) -> None:
        self.ms = ms
        self.polyline = None

    def draw_polyline(self, points: array, color: int) -> None:
        self.polyline = self.ms.AddPolyline(points)
        self.polyline.Color = color

    def draw_rectangle(self, initial_point: array, width: float, height: float, color=250) -> None:
        coordinates = [*list(initial_point)]
        for index in range(3):
            item = coordinates[-3:]
            if index == 0:
                item[0] += width
            if index == 1:
                item[1] += height
            if index == 2:
                item[0] -= width
            coordinates += item
        coordinates += list(initial_point)
        self.draw_polyline(array("d", coordinates), color)
