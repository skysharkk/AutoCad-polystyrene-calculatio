from PyQt6.QtWidgets import QPushButton


class Button:
    def __init__(self, btn: QPushButton) -> None:
        self.btn = btn

    def connect_action(self, func) -> None:
        self.btn.clicked.connect(func)
