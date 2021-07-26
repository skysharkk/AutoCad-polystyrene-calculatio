from typing import Union

from projectutils import show_error_window


class Input:
    def __init__(self, input_field) -> None:
        self.input_field = input_field

    def get_value(self) -> Union[None, int]:
        try:
            return int(self.input_field.displayText())
        except ValueError:
            show_error_window('Введено неверное значение')

