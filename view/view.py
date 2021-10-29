from view.initial_data import InitialData
from view.components import Button, TableWidget
from view.window import Window


def view() -> None:
    window = Window()
    window.show()

    acad_table_data = [
        ["1", "1", "1", "33333333333333333333331", "1", "1", "1", "1"],
        ["2", "2", "2", "2", "2", "2", "2", "2"],
        ["2", "2", "2", "2", "2", "2", "2", "2"],
        ["2", "2", "2", "2", "2", "2", "2", "2"],
    ]

    initial_data = InitialData(window.form)

    del_table_btn = Button(window.form.res_delete_position)
    acad_table = TableWidget(window.form.res_table)
    acad_table.import_data(acad_table_data)
    del_table_btn.connect_action(acad_table.remove_row)

    window.exec_app()
