from typing import ForwardRef
from PyQt6.QtWidgets import QApplication, QWidget
from uinterface import Ui_Form
import sys


app = QApplication(sys.argv)
Form = QWidget()
window = Ui_Form()
window.setupUi(Form)
Form.show()

sys.exit(app.exec())
