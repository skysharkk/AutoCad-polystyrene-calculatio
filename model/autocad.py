from pyautocad import Autocad
import win32com.client
from comtypes.automation import VARIANT
from ctypes import byref


class Acad:
    def __init__(self) -> None:
        self.acad = Autocad(create_if_not_exists=True)
        self.model = self.acad.model
        self.shell = win32com.client.Dispatch("WScript.Shell")

    def expand_acad(self) -> None:
        self.self.shell.AppActivate(self.acad.app.Caption)
