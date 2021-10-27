from PyQt6.QtWidgets import QLineEdit
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QRegularExpressionValidator
from projectutils import show_error_window
from typing import Callable, Union


class Input:
    def __init__(self, input_field: QLineEdit) -> None:
        self.input_field = input_field

    def get_value(self) -> Union[float, bool]:
        try:
            return float(self.input_field.displayText())
        except ValueError:
            show_error_window('Введено неверное значение')
            return False

    def set_validator(self, reg_exp: str):
        q_reg_exp = QRegularExpression(reg_exp)
        input_validator = QRegularExpressionValidator(q_reg_exp, self.input_field)
        self.input_field.setValidator(input_validator)

    def connect_text_changed_event(self, func: Callable[..., None]):
        self.input_field.textChanged.connect(func)

    def is_empty(self):
        return not self.input_field.text()
