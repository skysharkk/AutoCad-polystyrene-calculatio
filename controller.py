from view import View
from model import Acad
import sys
import os


sys.path.append(os.getcwd())


def main():
    ui = View()
    acad = Acad()
    ui.window.show()
    acad.attach(ui.initial_data)
    ui.initial_data.choose_pos_btn.connect_action(acad.select_items)
    ui.results.export_to_acad_btn.connect_action(
        acad.create_table(ui.initial_data.scale, ui.results.table_data)
    )
    ui.results.attach(acad)
    ui.results.draw_objects_btn.connect_action(
        acad.draw_objects(ui.results.table_data)
    )
    ui.waste.draw_waste_btn.connect_action(
        acad.draw_waste
    )
    ui.waste.calc_waste_btn.connect_action(
        acad.draw_waste_result(ui.initial_data.scale,
                               ui.results.table_data.calc_overall_volume)
    )
    ui.window.exec_app()


if __name__ == "__main__":
    import PyQt5

    dirname = os.path.dirname(PyQt5.__file__)
    plugin_path = os.path.join(dirname, 'Qt5', 'plugins', 'platforms')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
    main()
