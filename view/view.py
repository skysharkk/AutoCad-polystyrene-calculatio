from PyQt6.QtWidgets import QApplication, QWidget
from uinterface import Ui_Form
import sys
from components import Input, GroupBox, Button, TreeWidget


app = QApplication(sys.argv)
Form = QWidget()
window = Ui_Form()
window.setupUi(Form)
Form.show()

scale = Input(window.init_data_scale)
thickness = Input(window.init_data_thickness)
poly_type_group = GroupBox(window.init_data_type)
add_type_btn = Button(window.init_data_add)
delete_type_btn = Button(window.init_data_delete)
types_table = TreeWidget(window.init_data_table)
choose_pos_btn = Button(window.choose_autocad_el)


def add_char() -> None:
    poly_type = poly_type_group.get_checked_radio_button()
    thickness_value = thickness.get_value()
    types_table.add_element(int(thickness_value), poly_type)


add_type_btn.connect_action(add_char)
delete_type_btn.connect_action(types_table.delete_selected_widget_item)



sys.exit(app.exec())
