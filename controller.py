from view import View
from model import Acad


def main():
    ui = View()
    acad = Acad()
    ui.window.show()
    acad.attach(ui.initial_data)
    ui.initial_data.choose_pos_btn.connect_action(acad.select_items)
    ui.results.attach(acad)
    ui.window.exec_app()


if __name__ == "__main__":
    main()
