from PyQt6.QtWidgets import QLineEdit
from projectutils import show_error_window


class Input:
    def __init__(self, input_field: QLineEdit) -> None:
        self.input_field = input_field

    def get_value(self) -> float:
        try:
            return float(self.input_field.displayText())
        except ValueError:
            show_error_window('Введено неверное значение')
