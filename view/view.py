from PyQt5.QtWidgets import QApplication, QWidget
from view.uinterface import Ui_Form
from typing import Callable
import sys
from view.components import Input, GroupBox, Button, TreeWidget, TableWidget


def view() -> None:
    app = QApplication(sys.argv)
    form = QWidget()
    font = form.font()
    font.setPointSize(8)
    form.setFont(font)
    window = Ui_Form()
    window.setupUi(form)
    form.show()

    acad_table_data = [
        ["1", "1", "1", "33333333333333333333331", "1", "1", "1", "1"],
        ["2", "2", "2", "2", "2", "2", "2", "2"],
        ["2", "2", "2", "2", "2", "2", "2", "2"],
        ["2", "2", "2", "2", "2", "2", "2", "2"],
    ]

    scale = Input(window.init_data_scale)
    width = Input(window.init_data_width)
    poly_type_group = GroupBox(window.init_data_type)
    add_type_btn = Button(window.init_data_add, is_enabled=False)
    delete_type_btn = Button(window.init_data_delete, is_enabled=False)
    types_table = TreeWidget(window.init_data_table)
    choose_pos_btn = Button(window.acad_select_positions, is_enabled=False)
    del_table_btn = Button(window.res_delete_position)

    acad_table = TableWidget(window.res_table)
    acad_table.import_data(acad_table_data)
    del_table_btn.connect_action(acad_table.remove_row)

    scale.set_validator("^[0-9]*[.]?[0-9]+$")
    width.set_validator("^[0-9]*[.]?[0-9]+$")

    def add_char() -> None:
        poly_type = poly_type_group.get_checked_radio_button()
        width_value = width.get_value()
        types_table.add_element(int(width_value), poly_type)

    def enabled_and_disabled_btn(input_field: Input, btn: Button) -> Callable[..., None]:
        def returned_function() -> None:
            if input_field.is_empty():
                btn.disable_btn()
            else:
                btn.enable_btn()
        return returned_function

    def enabled_delete_type_btn() -> None:
        delete_type_btn.enable_btn()

    def delete_type_btn_action() -> None:
        types_table.delete_selected_widget_item()
        if len(types_table.el_list) == 0:
            delete_type_btn.disable_btn()

    scale.connect_text_changed_event(
        enabled_and_disabled_btn(scale, choose_pos_btn))
    width.connect_text_changed_event(
        enabled_and_disabled_btn(width, add_type_btn))
    types_table.connect_clicked_event(enabled_delete_type_btn)
    add_type_btn.connect_action(add_char)
    delete_type_btn.connect_action(delete_type_btn_action)
    sys.exit(app.exec())
