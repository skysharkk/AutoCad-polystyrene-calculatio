from comtypes.client import Constants
from comtypes.automation import VARIANT
from ctypes import byref
from pyautocad import Autocad
from array import array
from projectutils import get_corner_coordinates
from typing import List, Tuple


class TextItem:
    def __init__(self, acad: Autocad, text: str, height: float, width: float) -> None:
        self.insertion_point = None
        self.acad = acad
        self.text = text
        self.height = height
        self.acad_text = None
        self._constants = Constants(acad.app)

    @staticmethod
    def get_bounding_box(entity) -> List[array]:
        min_point = VARIANT(array("d", array("d", [0, 0, 0])))
        max_point = VARIANT(array("d", array("d", [0, 0, 0])))
        ref_min_point = byref(min_point)
        ref_max_point = byref(max_point)
        entity.GetBoundingBox(ref_min_point, ref_max_point)
        return [array("d", list(*min_point)), array("d", list(*max_point))]

    @staticmethod
    def get_mtext_line_height(text_obj) -> float:
        bounding_box_coordinates = TextItem.get_bounding_box(text_obj)
        return abs(bounding_box_coordinates[1][1] - bounding_box_coordinates[0][1])

    @staticmethod
    def calc_object_center(coordinates: Tuple[float, ...]) -> array:
        coord = get_corner_coordinates(coordinates)
        x = (coord.max_x + coord.min_x) / 2
        y = (coord.max_y + coord.min_y) / 2
        return array("d", [x, y, 0])

    def draw_text(self, insertion_point: array) -> None:
        self.acad_text = self.acad.doc.ModelSpace.AddMText(
            insertion_point, self.width, self.text)
        self.acad_text.Height = self.height

    def inscribe_text(self, coordinates: Tuple[float, ...]) -> None:
        self.insertion_point = TextItem.calc_object_center(coordinates)
        self.draw_text(self.insertion_point)
        self.acad_text.AttachmentPoint = self._constants.acAttachmentPointMiddleCenter
        mtext_height = TextItem.get_mtext_line_height(self.acad_text)
        new_x = self.insertion_point[0] - (self.width / 2)
        new_y = self.insertion_point[1] + (mtext_height / 2)
        self.acad_text.Move(self.insertion_point, array("d", [new_x, new_y, 0]))
