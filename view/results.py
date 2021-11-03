from .uinterface import Ui_Form
from .components import Button, TableWidget


class Results:
    def __init__(self, form: Ui_Form):
        self._form = form
        self.del_table_btn = Button(self._form.res_delete_position)
        self.acad_table = TableWidget(self._form.res_table)
        self.del_table_btn.connect_action(self.acad_table.remove_row)
        self.test_data = [
            ["1", "1", "1", "33333333333333333333331", "1", "1", "1", "1"],
            ["2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2"],
            ["2", "2", "2", "2", "2", "2", "2", "2"],
        ]
        self.acad_table.import_data(self.test_data)

    def enable(self) -> None:
        self._form.results.setEnabled(True)

    def disable(self) -> None:
        self._form.results.setDisabled(True)
