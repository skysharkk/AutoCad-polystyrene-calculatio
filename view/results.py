from observer import Observer
from .uinterface import Ui_Form
from .components import Button, TableWidget
from .initial_data import InitialData


class Results(Observer):
    def __init__(self, form: Ui_Form):
        self._form = form
        self.del_table_btn = Button(self._form.res_delete_position)
        self.acad_table = TableWidget(self._form.res_table)
        self.del_table_btn.connect_action(self.acad_table.remove_row)

    def enable(self) -> None:
        self._form.results.setEnabled(True)

    def disable(self) -> None:
        self._form.results.setDisabled(True)

    def update_table_data(self):
        pass

    def update(self, subject: InitialData) -> None:
        self.update_table_data()
