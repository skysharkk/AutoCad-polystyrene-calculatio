from pyautocad import Autocad
import win32com.client
from comtypes.automation import VARIANT
from ctypes import byref
from projectutils import show_error_window
from view.results import Results
from .items import Items
from observer import Subject, Observer
from typing import List, Union
from .text import Text
from view.table_data import DataItem


class Acad(Subject, Observer):
    def __init__(self) -> None:
        self.acad = Autocad(create_if_not_exists=True)
        self.model = self.acad.model
        self.doc = self.acad.doc
        self._shell = win32com.client.Dispatch("WScript.Shell")
        self._selected_items = None
        self.acad_text: Union[Text, None] = None
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
        except AssertionError:
            show_error_window('Ошибка при выделение объектов!')
        finally:
            selected = self.doc.SelectionSets.Add("SS1")
            selected.SelectOnScreen()
            self._selected_items = Items(selected).get_items
            self.notify()

    def inscribe_text(self, data_items: List[DataItem], scale: float) -> None:
        self.acad_text = Text(self.acad)
        self.acad_text.inscribe_text_items(data_items, scale)

    @property
    def selected_items(self):
        return self._selected_items

    def update(self, subject: Results) -> None:
        if self.acad_text:
            self.acad_text.clear()
        self.inscribe_text(subject.table_data.data, subject.scale)
