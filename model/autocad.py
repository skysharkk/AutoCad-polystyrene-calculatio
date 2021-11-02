from pyautocad import Autocad
import win32com.client
from comtypes.automation import VARIANT
from ctypes import byref
from projectutils import show_error_window
from .items import Items
from observer import Subject, Observer
from typing import List


class Acad(Subject):
    def __init__(self) -> None:
        self.acad = Autocad(create_if_not_exists=True)
        self.model = self.acad.model
        self.doc = self.acad.doc
        self._shell = win32com.client.Dispatch("WScript.Shell")
        self._selected_items = None
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
