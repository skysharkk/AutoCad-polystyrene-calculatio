class Button:
    def __init__(self, btn) -> None:
        self.btn = btn

    def connect_action(self, func) -> None:
        self.btn.clicked.connect(func)
