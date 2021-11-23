import _ctypes
from pyautocad import Autocad
import win32com.client
from array import array
from projectutils import show_error_window
from view.components import Input
from view.results import Results
from .items import Items
from observer import Subject, Observer
from typing import List, Union, Callable
from .polyline import Polyline
from .text import Text, TextItem
from view.table_data import DataItem, TableData
from comtypes.automation import VARIANT
from model.table import Table


class Acad(Subject, Observer):
    def __init__(self) -> None:
        self.acad = Autocad(create_if_not_exists=True)
        self.model = self.acad.model
        self.doc = self.acad.doc
        self._shell = win32com.client.Dispatch("WScript.Shell")
        self._selected_items = None
        self.acad_text: Union[Text, None] = None
        self.acad_table: Union[Table, None] = None
        self.polyline = Polyline(self.model)
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def expand_acad(self) -> None:
        self._shell.AppActivate(self.acad.app.Caption)

    def select_items(self, text="Выберете объект") -> None:
        self.expand_acad()
        self.doc.Utility.prompt(text)
        try:
            if self.doc.SelectionSets.Count > 0:
                self.doc.SelectionSets.Item("SS1").Delete()
            selected = self.doc.SelectionSets.Add("SS1")
            selected.SelectOnScreen()
            self._selected_items = Items(selected).get_items
            self.notify()
        except Exception:
            show_error_window('Ошибка при выделение объектов!')

    def inscribe_text(self, data_items: List[DataItem], scale: float) -> None:
        self.acad_text = Text(self.acad)
        self.acad_text.inscribe_text_items(data_items, scale)

    @property
    def selected_items(self):
        return self._selected_items

    def update(self, subject: Results) -> None:
        if self.acad_text:
            self.acad_text.clear()
        self.inscribe_text(subject.table_data.get_data(), subject.scale)

    def get_point(self, message_text="Выберете точку") -> array:
        self.expand_acad()
        return array('d', self.doc.Utility.GetPoint(VARIANT.missing, message_text))

    def create_table(self, scale: Input, ui_data: TableData) -> Callable:
        def fun() -> None:
            if not scale.is_empty():
                try:
                    initial_point = self.get_point()
                    self.acad_table = Table(
                        self.acad, scale.get_value(), initial_point)
                    self.acad_table.draw_table(ui_data.get_data())
                except _ctypes.COMError:
                    print("point not selected")
            else:
                show_error_window('Введите масштаб!')
        return fun

    def draw_objects(self, ui_data: TableData) -> Callable:
        def fn() -> None:
            initial_point = self.get_point()
            data = ui_data.get_data()
            for data_item in data:
                for _ in range(int(data_item.amount)):
                    initial_point[1] -= 50
                    obj_description = TextItem(
                        self.acad, f"{data_item.poly_type.decode()} {data_item.depth}",
                        50,
                        1000
                    )
                    obj_description.draw_text(initial_point)
                    initial_point[1] -= 50
                    self.polyline.draw_rectangle(
                        initial_point,
                        float(data_item.width),
                        float(data_item.height)
                    )
                    initial_point[1] -= float(data_item.height)

        return fn
