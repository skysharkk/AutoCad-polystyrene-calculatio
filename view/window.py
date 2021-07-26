from PyQt6 import uic, QtWidgets

Form, _ = uic.loadUiType('../assets/uinterface.ui')


class Window(QtWidgets.QDialog, Form):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
