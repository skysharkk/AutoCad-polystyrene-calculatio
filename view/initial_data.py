from typing import Callable
from view.components import Input, GroupBox, Button, TreeWidget
from view.uinterface import Ui_Form


class InitialData:
    scale: Input
    width: Input
    poly_type_group: GroupBox
    add_type_btn: Button
    delete_type_btn: Button
    types_table: TreeWidget
    choose_pos_btn: Button

    def __init__(self, form: Ui_Form) -> None:
        self.form = form
        self.scale = Input(self.form.init_data_scale)
        self.width = Input(self.form.init_data_width)
        self.poly_type_group = GroupBox(self.form.init_data_type)
        self.add_type_btn = Button(self.form.init_data_add, is_enabled=False)
        self.delete_type_btn = Button(
            self.form.init_data_delete, is_enabled=False)
        self.types_table = TreeWidget(self.form.init_data_table)
        self.choose_pos_btn = Button(
            self.form.acad_select_positions, is_enabled=False)

        self.scale.set_validator("^[0-9]*[.]?[0-9]+$")
        self.width.set_validator("^[0-9]*[.]?[0-9]+$")
        self.scale.connect_text_changed_event(self.change_choose_pos_btn_state)
        self.width.connect_text_changed_event(self.change_add_type_btn_state)
        self.add_type_btn.connect_action(self.add_char)
        self.types_table.connect_clicked_event(self.delete_type_btn.enable_btn)
        self.delete_type_btn.connect_action(self.remove_table_item)

    def add_char(self) -> None:
        poly_type = self.poly_type_group.get_checked_radio_button()
        width_value = self.width.get_value()
        self.types_table.add_element(int(width_value), poly_type)
        if not self.scale.is_empty():
            self.choose_pos_btn.enable_btn()

    def remove_table_item(self) -> None:
        self.types_table.delete_selected_widget_item()
        if self.types_table.is_epmty():
            self.delete_type_btn.disable_btn()
            self.choose_pos_btn.disable_btn()

    def change_add_type_btn_state(self) -> None:
        if self.width.is_empty():
            self.add_type_btn.disable_btn()
        else:
            self.add_type_btn.enable_btn()

    def change_choose_pos_btn_state(self):
        if self.scale.is_empty() or self.types_table.is_epmty():
            self.choose_pos_btn.disable_btn()
        else:
            self.choose_pos_btn.enable_btn()
