from PyQt5.QtWidgets import QApplication, QWidget
from view.uinterface import Ui_Form
import sys


class Window():
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.widget = QWidget()
        self.font = self.widget.font()
        self.font.setPointSize(8)
        self.widget.setFont(self.font)
        self.form = Ui_Form()
        self.form.setupUi(self.widget)

    def show(self) -> None:
        self.widget.show()

    def exec_app(self) -> None:
        sys.exit(self.app.exec())
