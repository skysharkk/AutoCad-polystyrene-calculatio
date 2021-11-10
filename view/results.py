from __future__ import annotations
from typing import List, TYPE_CHECKING
from observer import Observer, Subject
from .table_data import TableData
from .uinterface import Ui_Form
from .components import Button, TableWidget


if TYPE_CHECKING:
    from .initial_data import InitialData


class Results(Observer, Subject):
    def __init__(self, form: Ui_Form):
        self._form = form
        self.del_table_btn = Button(self._form.res_delete_position)
        self.acad_table = TableWidget(self._form.res_table)
        self.del_table_btn.connect_action(self._remove_row)
        self.table_data = TableData()
        self._observers: List[Observer] = []
        self.scale = None

    def enable(self) -> None:
        self._form.results.setEnabled(True)

    def disable(self) -> None:
        self._form.results.setDisabled(True)

    def update(self, subject: InitialData) -> None:
        self.scale = subject.scale.get_value()
        self.table_data.update_data(subject.data)
        self.acad_table.import_data(self.table_data.data_to_list())
        self.notify()

    def _remove_row(self) -> None:
        self.table_data. remove_item(self.acad_table.remove_row())
        self.acad_table.import_data(self.table_data.data_to_list())
        self.notify()

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)
