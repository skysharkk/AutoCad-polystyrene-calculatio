import pyautocad  # type: ignore
from win32com import client  # type: ignore


class Autocad:
    def __init__(self):
        self.acad = pyautocad.Autocad(create_if_not_exists=True)
        self.doc = self.acad.doc
        self.shell = client.Dispatch("WScript.Shell")

    def change_focus_window(self):
        self.shell.AppActivate(self.acad.app.Caption)

