from PyQt6 import uic, QtWidgets
import os
from PyQt6.QtGui import QIcon

Form, _ = uic.loadUiType(os.path.join(os.getcwd(), "assets", "uinterface.ui"))


class Window(QtWidgets.QDialog, Form):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowIcon(
            QIcon(os.path.join(os.getcwd(), "assets", "logo.png")))
        self.setupUi(self)
