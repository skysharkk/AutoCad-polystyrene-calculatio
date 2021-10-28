from typing import Callable
from PyQt5.QtWidgets import QPushButton


class Button:
    btn: QPushButton
    is_enabled: bool

    def __init__(self, btn: QPushButton, is_enabled=True) -> None:
        self.btn = btn
        self.btn.setEnabled(is_enabled)

    def connect_action(self, func: Callable[..., None]) -> None:
        self.btn.clicked.connect(func)

    def enable_btn(self) -> None:
        self.btn.setEnabled(True)

    def disable_btn(self) -> None:
        self.btn.setEnabled(False)
