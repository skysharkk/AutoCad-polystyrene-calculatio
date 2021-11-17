from __future__ import annotations
from typing import List, TYPE_CHECKING
from observer import Observer, Subject
from projectutils.auxiliary_utulities import show_error_window
from view.components import button
from .table_data import TableData
from .uinterface import Ui_Form
from .components import Button, TableWidget
from PyQt5.QtWidgets import QFileDialog
from projectutils import Excel
from datetime import datetime
from openpyxl.utils.exceptions import InvalidFileException


if TYPE_CHECKING:
    from .initial_data import InitialData


class Results(Observer, Subject):
    def __init__(self, form: Ui_Form):
        self._form = form
        self.del_table_btn = Button(self._form.res_delete_position)
        self.acad_table = TableWidget(self._form.res_table)
        self.del_table_btn.connect_action(self._remove_row)
        self.import_from_excel_btn = Button(
            self._form.res_import_data_from_excel)
        self.import_from_excel_btn.connect_action(self.import_data_from_excel)
        self.table_data = TableData()
        self._observers: List[Observer] = []
        self.export_to_acad_btn = Button(self._form.res_export_table_to_acad)
        self.template_btn = Button(self._form.res_excel_template)
        self.template_btn.connect_action(self.template_btn_action)
        self.export_to_excel_btn = Button(self._form.res_export_table_to_excel)
        self.export_to_excel_btn.connect_action(self.export_to_excel_action)
        self.scale = None
        self.draw_objects_btn = Button(self._form.res_draw_pos)

    def import_data_from_excel(self) -> None:
        try:
            path = QFileDialog.getOpenFileName(
                filter="Excel (*.xls *.xlsx);;All Files (*)")
            excel_data = Excel(path[0]).get_data()
            self.table_data.import_data_from_list(excel_data)
            self.acad_table.import_data(self.table_data.data_to_list())
        except InvalidFileException:
            print("invalid file format")

    def export_to_excel_action(self) -> None:
        try:
            title = [
                "Поз.",
                "Обозначение",
                "Длина, мм",
                "Высота, мм",
                "Ширина, мм",
                "Кол., шт.",
                "Объем, м3",
                "Примечания"
            ],
            path = QFileDialog.getSaveFileName(
                directory=f"acad_table_{datetime.now().second}.xlsx", filter="Excel (*.xls *.xlsx)")[0]
            Excel.get_template(path, [*title, *self.table_data.data_to_list()])
        except FileNotFoundError:
            print("invalid file format")

    def template_btn_action(self) -> None:
        try:
            template = [
                [
                    "Поз.",
                    "Обозначение",
                    "Длина, мм",
                    "Высота, мм",
                    "Ширина, мм",
                    "Кол., шт.",
                    "Объем, м3",
                    "Примечания"
                ],
                ["1", "ППТ-15-А-Р", "", "", "", "", "", ""],
                ["2",
                    "Эффективный утеплитель λ ≤ 0,034 Вт/(м·°C)", "", "", "", "", "", ""],
            ]
            path = QFileDialog.getSaveFileName(
                directory="template.xlsx", filter="Excel (*.xls *.xlsx)")[0]
            Excel.get_template(path, template)
        except FileNotFoundError:
            print("invalid file format")

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
