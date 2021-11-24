from .uinterface import Ui_Form
from .components import Button


class Waste:
    def __init__(self, form: Ui_Form):
        self._form = form
        self.draw_waste_btn = Button(self._form.draw_bin)
        self.calc_waste_btn = Button(self._form.calc_waste)
