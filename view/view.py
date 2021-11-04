from .initial_data import InitialData
from .window import Window
from .results import Results


class View:
    def __init__(self):
        self.window = Window()
        self.initial_data = InitialData(self.window.form)
        self.results = Results(self.window.form)
        self.initial_data.attach(self.results)
