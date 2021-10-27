from PyQt6.QtWidgets import QGroupBox, QRadioButton


class GroupBox:
    def __init__(self, group_box: QGroupBox) -> None:
        self.group_box = group_box

    def get_checked_radio_button(self) -> str:
        for el in self.group_box.children():
            if el.inherits("QRadioButton"):
                if el.isChecked():
                    return el.text()
        return "empty"

