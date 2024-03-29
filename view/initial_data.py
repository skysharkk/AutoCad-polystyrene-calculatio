from __future__ import annotations
from ast import In
from collections import namedtuple
from typing import List, TYPE_CHECKING
from view.components import Input, GroupBox, Button, TreeWidget
from view.uinterface import Ui_Form
from observer import Observer, Subject

if TYPE_CHECKING:
    from model import Acad

Data = namedtuple("Data", ["scale", "poly_type", "depth", "coordinates", "width", "height"])


class InitialData(Observer, Subject):
    scale: Input
    depth: Input
    poly_type_group: GroupBox
    add_type_btn: Button
    delete_type_btn: Button
    types_table: TreeWidget
    choose_pos_btn: Button
    data: Data

    def __init__(self, form: Ui_Form) -> None:
        self.form = form
        self.scale = Input(self.form.init_data_scale)
        self.depth = Input(self.form.init_data_depth)
        self.height = Input(self.form.init_data_height)
        self.width = Input(self.form.init_data_width)
        self.poly_type_group = GroupBox(self.form.init_data_type)
        self.add_type_btn = Button(self.form.init_data_add, is_enabled=False)
        self.delete_type_btn = Button(
            self.form.init_data_delete, is_enabled=False)
        self.types_table = TreeWidget(self.form.init_data_table)
        self.choose_pos_btn = Button(
            self.form.acad_select_positions, is_enabled=False)

        self.scale.set_validator("^[0-9]*[.]?[0-9]+$")
        self.depth.set_validator("^[0-9]*[.]?[0-9]+$")
        self.width.set_validator("^[0-9]*[.]?[0-9]+$")
        self.height.set_validator("^[0-9]*[.]?[0-9]+$")
        self.scale.connect_text_changed_event(self.change_choose_pos_btn_state)
        self.height.connect_text_changed_event(self.change_choose_pos_btn_state)
        self.width.connect_text_changed_event(self.change_choose_pos_btn_state)
        self.depth.connect_text_changed_event(self.change_add_type_btn_state)
        self.add_type_btn.connect_action(self.add_char)
        self.types_table.connect_clicked_event(self.types_table_event)
        self.delete_type_btn.connect_action(self.remove_table_item)
        self._observers: List[Observer] = []

    def types_table_event(self):
        self.delete_type_btn.enable_btn()
        if not self.scale.is_empty():
            self.choose_pos_btn.enable_btn()

    def add_char(self) -> None:
        poly_type = self.poly_type_group.get_checked_radio_button()
        depth_value = self.depth.get_value()
        self.types_table.add_element(int(depth_value), poly_type)

    def remove_table_item(self) -> None:
        self.types_table.delete_selected_widget_item()
        if self.types_table.is_empty():
            self.delete_type_btn.disable_btn()
            self.choose_pos_btn.disable_btn()

    def change_add_type_btn_state(self) -> None:
        if self.depth.is_empty():
            self.add_type_btn.disable_btn()
        else:
            self.add_type_btn.enable_btn()

    def change_choose_pos_btn_state(self) -> None:
        if self.scale.is_empty() or self.types_table.is_empty() or self.width.is_empty() or self.height.is_empty():
            self.choose_pos_btn.disable_btn()
        else:
            self.choose_pos_btn.enable_btn()

    def enable(self) -> None:
        self.form.init_data.setEnabled(True)

    def disable(self) -> None:
        self.form.init_data.setEnabled(False)

    def update(self, subject: Acad, event: str) -> None:
        if event == "update":
            self.data = Data(
                self.scale.get_value(),
                self.types_table.get_selected_item()[1][1].decode(),
                self.types_table.get_selected_item()[1][0],
                subject.selected_items,
                self.width.get_value(),
                self.height.get_value()
            )
            self.notify("update")

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, event: str) -> None:
        for observer in self._observers:
            observer.update(self, event)
